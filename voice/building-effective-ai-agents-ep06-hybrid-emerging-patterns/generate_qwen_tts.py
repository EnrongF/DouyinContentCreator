import json
import os
import re
import shutil
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLUG = Path(__file__).resolve().parent.name
VOICE_ROOT = ROOT / "voice" / SLUG
SCENE_GRAPH = ROOT / "scene-graphs" / f"{SLUG}.json"
VOICE_MANIFEST = VOICE_ROOT / "voice-manifest.json"
CHUNK_DIR = VOICE_ROOT / "chunks-qwen"
REMOTION_AUDIO_DIR = ROOT / "remotion" / "public" / SLUG / "audio"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

MODEL = os.environ.get("QWEN_TTS_MODEL", "qwen3-tts-instruct-flash")
VOICE = os.environ.get("QWEN_TTS_VOICE", "Ethan")
PADDING_SECONDS = float(os.environ.get("VOICE_SCENE_PADDING_SECONDS", "0.35"))
ENDPOINTS = [
    "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
    "https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
]

INSTRUCTION = (
    "自然口语化的标准普通话。像冷静的技术播客主持人，略带判断感，"
    "不要播音腔，不要新闻腔，不要网红语气。遇到换行做自然节奏重置；"
    "问句轻微上扬，关键判断稍微放慢。整体温和、可信、适合高信任技术短视频。"
)


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def audio_duration(path: Path) -> float:
    result = subprocess.run(
        ["afinfo", str(path)],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    match = re.search(r"estimated duration:\s*([0-9.]+)\s*sec", result.stdout)
    if not match:
        raise RuntimeError(f"Could not measure audio duration for {path}")
    return float(match.group(1))


def post_json(url: str, api_key: str, payload: dict) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        return json.loads(response.read().decode("utf-8"))


def find_audio_url(response: dict) -> str | None:
    candidates = [
        response.get("output", {}).get("audio", {}).get("url"),
        response.get("output", {}).get("url"),
        response.get("audio", {}).get("url"),
    ]
    for value in candidates:
        if isinstance(value, str) and value.startswith("http"):
            return value
    return None


def download(url: str, path: Path) -> None:
    with urllib.request.urlopen(url, timeout=90) as response:
        path.write_bytes(response.read())


def synthesize(api_key: str, text: str, output: Path) -> None:
    payload = {
        "model": MODEL,
        "input": {
            "text": text,
            "voice": VOICE,
            "language_type": "Chinese",
            "instruction": INSTRUCTION,
            "optimize_instructions": True,
        },
    }
    last_error = None
    for endpoint in ENDPOINTS:
        try:
            response = post_json(endpoint, api_key, payload)
            audio_url = find_audio_url(response)
            if not audio_url:
                raise RuntimeError(f"No audio URL in response: {json.dumps(response, ensure_ascii=False)[:500]}")
            download(audio_url, output)
            return
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            last_error = exc
            time.sleep(0.25)
    raise RuntimeError(f"Qwen TTS failed: {last_error}")


def main() -> None:
    load_env_file(DEFAULT_ENV)
    api_key = os.environ.get("DASHSCOPE_API_KEY") or os.environ.get("QWEN_API_KEY")
    if not api_key:
        raise SystemExit("QWEN_API_KEY or DASHSCOPE_API_KEY is missing.")

    manifest = json.loads(VOICE_MANIFEST.read_text(encoding="utf-8"))
    scene_graph = json.loads(SCENE_GRAPH.read_text(encoding="utf-8"))
    scenes_by_id = {scene["id"]: scene for scene in scene_graph["scenes"]}

    CHUNK_DIR.mkdir(parents=True, exist_ok=True)
    REMOTION_AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    total_duration = 0.0
    for chunk in manifest["chunks"]:
        chunk_id = chunk["id"]
        output = CHUNK_DIR / f"{chunk_id}.wav"
        remotion_output = REMOTION_AUDIO_DIR / f"{chunk_id}.wav"
        reuse = output.exists() and output.stat().st_size > 2048 and not chunk.get("forceRegenerate")

        if not reuse:
            print(f"qwen tts {chunk_id}", flush=True)
            synthesize(api_key, chunk["text"].strip(), output)

        if output.stat().st_size < 2048:
            raise RuntimeError(f"TTS output too small: {output}")

        shutil.copy2(output, remotion_output)
        measured = audio_duration(output)
        pause_after = float(chunk.get("pauseAfterMs", PADDING_SECONDS * 1000)) / 1000
        duration = round(measured + pause_after, 3)
        total_duration += duration

        chunk["actualDurationSeconds"] = duration
        chunk["measuredSpeechSeconds"] = round(measured, 3)
        chunk["audioFile"] = f"chunks-qwen/{chunk_id}.wav"
        chunk["remotionAudioFile"] = f"{SLUG}/audio/{chunk_id}.wav"
        chunk["ttsProvider"] = "qwen-dashscope"
        chunk["ttsModel"] = MODEL
        chunk["ttsVoice"] = VOICE
        chunk["paddingSeconds"] = round(pause_after, 3)
        chunk.pop("forceRegenerate", None)

        scene = scenes_by_id[chunk_id]
        scene["durationSeconds"] = duration
        scene["audioFile"] = chunk["remotionAudioFile"]

    manifest["status"] = "timed_audio_ready"
    manifest["ttsStatus"] = "complete"
    manifest["ttsProvider"] = "qwen-dashscope"
    manifest["defaultVoiceMaker"] = {
        "provider": "qwen-dashscope",
        "model": MODEL,
        "voice": VOICE,
    }
    manifest["finalAudio"] = "remotion_sequence_audio"
    manifest["totalDurationSeconds"] = round(total_duration, 3)
    manifest["asrTranscript"] = "asr.txt"

    VOICE_MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    SCENE_GRAPH.write_text(
        json.dumps(scene_graph, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"voice_duration={total_duration:.3f}")
    print(VOICE_MANIFEST)


if __name__ == "__main__":
    main()
