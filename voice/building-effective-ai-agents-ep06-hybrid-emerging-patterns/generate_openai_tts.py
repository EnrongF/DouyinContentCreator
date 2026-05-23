import json
import os
import re
import shutil
import subprocess
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
SLUG = Path(__file__).resolve().parent.name
VOICE_ROOT = ROOT / "voice" / SLUG
SCENE_GRAPH = ROOT / "scene-graphs" / f"{SLUG}.json"
VOICE_MANIFEST = VOICE_ROOT / "voice-manifest.json"
CHUNK_DIR = VOICE_ROOT / "chunks"
REMOTION_AUDIO_DIR = ROOT / "remotion" / "public" / SLUG / "audio"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

MODEL = os.environ.get("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
VOICE = os.environ.get("OPENAI_TTS_VOICE", "marin")
SPEED = float(os.environ.get("OPENAI_TTS_SPEED", "1.0"))
PADDING_SECONDS = float(os.environ.get("VOICE_SCENE_PADDING_SECONDS", "0.35"))

INSTRUCTIONS = """
用自然、口语化的标准普通话朗读，像一个冷静的播客型技术顾问在解释判断。
不要播音腔，不要新闻腔，不要网红语气，也不要把每句话读成同一种重音。
把输入当成短 speech chunk：一段只表达一个意思，语气稳定，但节奏要像真人说话。
遇到换行，做一次自然的节奏重置；遇到逗号，短停；遇到问号，轻微上扬；遇到冒号，停一下再解释。
关键词可以稍微加重，但不要夸张。整体保持温和、可信、略带思考感。
英文术语自然读出，不要突然切换成夸张英文口音。
Agent 可以自然读作 Agent；Single Agent、Multi-Agent、Workflow、evaluator 保持清楚。
""".strip()


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


def main() -> None:
    load_env_file(DEFAULT_ENV)
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit(
            "OPENAI_API_KEY is missing. Set it in the environment or "
            f"add it to {DEFAULT_ENV}."
        )

    manifest = json.loads(VOICE_MANIFEST.read_text(encoding="utf-8"))
    scene_graph = json.loads(SCENE_GRAPH.read_text(encoding="utf-8"))
    scenes_by_id = {scene["id"]: scene for scene in scene_graph["scenes"]}
    client = OpenAI(timeout=90.0, max_retries=2)

    CHUNK_DIR.mkdir(parents=True, exist_ok=True)
    REMOTION_AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    total_duration = 0.0
    for chunk in manifest["chunks"]:
        chunk_id = chunk["id"]
        text = chunk["text"].strip()
        output = CHUNK_DIR / f"{chunk_id}.mp3"
        remotion_output = REMOTION_AUDIO_DIR / f"{chunk_id}.mp3"

        reuse = output.exists() and output.stat().st_size > 2048 and not chunk.get("forceRegenerate")
        if not reuse:
            print(f"tts {chunk_id}", flush=True)
            with client.audio.speech.with_streaming_response.create(
                model=MODEL,
                voice=VOICE,
                input=text,
                instructions=INSTRUCTIONS,
                response_format="mp3",
                speed=SPEED,
            ) as response:
                response.stream_to_file(output)

        if output.stat().st_size < 2048:
            raise RuntimeError(f"TTS output too small: {output}")

        shutil.copy2(output, remotion_output)
        measured = audio_duration(output)
        pause_after = float(chunk.get("pauseAfterMs", PADDING_SECONDS * 1000)) / 1000
        duration = round(measured + pause_after, 3)
        total_duration += duration

        chunk["actualDurationSeconds"] = duration
        chunk["measuredSpeechSeconds"] = round(measured, 3)
        chunk["audioFile"] = f"chunks/{chunk_id}.mp3"
        chunk["remotionAudioFile"] = f"{SLUG}/audio/{chunk_id}.mp3"
        chunk["ttsModel"] = MODEL
        chunk["ttsVoice"] = VOICE
        chunk["ttsSpeed"] = SPEED
        chunk["paddingSeconds"] = round(pause_after, 3)
        chunk.pop("forceRegenerate", None)

        scene = scenes_by_id[chunk_id]
        scene["durationSeconds"] = duration
        scene["audioFile"] = chunk["remotionAudioFile"]

    manifest["status"] = "timed_audio_ready"
    manifest["ttsStatus"] = "complete"
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
