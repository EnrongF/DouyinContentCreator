import os
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
DEPS = Path("/private/tmp/codex_imageio_ffmpeg")
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")
INPUT = ROOT / "narration.txt"
OUTPUT = ROOT / "voiceover.openai.mp3"
FINAL = ROOT / "voiceover.final.mp3"
CHUNK_DIR = ROOT / "voiceover_chunks"
PHRASE_CHUNK_DIR = ROOT / "voiceover_phrase_chunks"
CONCAT_LIST = ROOT / "voiceover_chunks.txt"
BEAT_AUDIO_MANIFEST = ROOT / "beat_audio_manifest.json"
SCENE_AUDIO_MANIFEST = ROOT / "scene_audio_manifest.json"

MODEL = os.environ.get("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
VOICE = os.environ.get("OPENAI_TTS_VOICE", "alloy")
SPEED = float(os.environ.get("OPENAI_TTS_SPEED", "1.2"))

INSTRUCTIONS = """
用自然、口语化的标准普通话朗读，像技术播客里正常聊天，不要每个分句都下结论。
语速用正常聊天速度，略放松，不要赶，不要端着，也不要像播新闻。
语气冷静、有判断力，但要有真实说话的起伏：有轻重、有短暂停顿、有自然连接。
同一段里的句子要连贯地说出来，不要像逐条念清单。
技术词清楚即可，不要故意加重；遇到英文术语不要升调表演。
中文解释性短语要说得像真人口语，不要把“代码合并请求”“持续集成”“独立工作区”念成术语清单。
英文术语保持英文发音：
OpenAI, Codex, Harness Engineering, Chrome DevTools, Providers, PR, golden principles。
如果文本里出现 PR，读作“代码合并请求”；如果出现 CI，读作“持续集成”；如果出现 worktree，读作“独立工作区”。
AGENTS.md 读作 Agents M D。不要把“零行人工”读成“零房人工”，不要把“智能体”读成“机器人体”。
数字必须读准：五个月、一千五百、百分之二十、三点五、六个小时。
""".strip()

VOICE_PROFILE = {
    "model": MODEL,
    "voice": VOICE,
    "speed": SPEED,
    "chunking": "phrase_v1_natural_conversation",
    "instructions_sha256": hashlib.sha256(INSTRUCTIONS.encode("utf-8")).hexdigest(),
}


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def ffmpeg_exe() -> str:
    if DEPS.exists():
        sys.path.insert(0, str(DEPS))
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        ffmpeg = shutil.which("ffmpeg")
        if not ffmpeg:
            raise SystemExit("ffmpeg not found. Install ffmpeg or imageio_ffmpeg.")
        return ffmpeg


def split_chunks(text: str) -> list[str]:
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    if not chunks:
        raise SystemExit(f"{INPUT} is empty.")
    return chunks


def media_duration(ffmpeg: str, path: Path) -> float:
    result = subprocess.run(
        [ffmpeg, "-i", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", result.stderr)
    if not match:
        raise RuntimeError(f"Could not read duration for {path}")
    hours, minutes, seconds = match.groups()
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def speech_weight(text: str) -> float:
    chinese = len(re.findall(r"[\u4e00-\u9fff]", text))
    ascii_tokens = re.findall(r"[A-Za-z0-9][A-Za-z0-9.\-+]*", text)
    ascii_weight = sum(max(1.0, len(token) * 0.55) for token in ascii_tokens)
    punctuation = len(re.findall(r"[，。；：、,.!?！？;:]", text))
    return max(3.0, chinese + ascii_weight + punctuation * 1.6 + 7.0)


def scene_groups(beats: list[dict], scenes: list) -> list[dict]:
    scene_ids = {scene: index for index, scene in enumerate(scenes, start=1)}
    groups = []
    for beat_index, beat in enumerate(beats, start=1):
        scene_id = scene_ids[beat["scene"]]
        if not groups or groups[-1]["scene"] != scene_id:
            groups.append({"scene": scene_id, "beats": []})
        groups[-1]["beats"].append((beat_index, beat))
    return groups


def phrase_groups(beats: list[dict], scenes: list, max_beats: int = 3) -> list[dict]:
    groups = []
    for scene_group in scene_groups(beats, scenes):
        scene_beats = scene_group["beats"]
        for chunk_index, start in enumerate(range(0, len(scene_beats), max_beats), start=1):
            groups.append(
                {
                    "scene": scene_group["scene"],
                    "chunk": chunk_index,
                    "chunk_id": f"{scene_group['scene']:02d}-{chunk_index:02d}",
                    "beats": scene_beats[start : start + max_beats],
                }
            )
    return groups


def group_text(group: dict) -> str:
    return " ".join(beat["voice"].strip() for _, beat in group["beats"])


def allocate_group_duration(group: dict, group_duration: float) -> list[dict]:
    weights = [speech_weight(beat["voice"]) for _, beat in group["beats"]]
    total_weight = sum(weights)
    cursor = 0.0
    allocations = []
    for (beat_index, beat), weight in zip(group["beats"], weights):
        duration = group_duration * weight / total_weight
        allocations.append(
            {
                "beat": beat_index,
                "scene": group["scene"],
                "chunk": group["chunk"],
                "chunk_id": group["chunk_id"],
                "chunk_start": cursor,
                "chunk_end": cursor + duration,
                "audio_duration": duration,
                "voice": beat["voice"],
                "caption": beat["caption"],
                "alignment_weight": weight,
                "alignment_method": "phrase_tts_weighted_beat_allocation",
            }
        )
        cursor += duration
    if allocations:
        drift = group_duration - allocations[-1]["chunk_end"]
        allocations[-1]["audio_duration"] += drift
        allocations[-1]["chunk_end"] = group_duration
    return allocations


def main() -> None:
    load_env_file(DEFAULT_ENV)
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is missing.")

    from render_assets import BEATS, SCENES

    groups = phrase_groups(BEATS, SCENES)
    INPUT.write_text("\n\n".join(group_text(group) for group in groups) + "\n", encoding="utf-8")
    ffmpeg = ffmpeg_exe()

    client = OpenAI(timeout=90.0, max_retries=2)
    PHRASE_CHUNK_DIR.mkdir(exist_ok=True)
    old_entries = {}
    if SCENE_AUDIO_MANIFEST.exists():
        old_manifest = json.loads(SCENE_AUDIO_MANIFEST.read_text(encoding="utf-8"))
        old_items = old_manifest.get("chunks", old_manifest.get("scenes", []))
        old_entries = {str(item.get("chunk_id", item.get("scene"))): item for item in old_items}

    chunk_paths = []
    chunk_entries = []
    beat_entries = []
    for index, group in enumerate(groups, start=1):
        scene_id = group["scene"]
        chunk_id = group["chunk_id"]
        chunk_text = group_text(group)
        chunk_path = PHRASE_CHUNK_DIR / f"phrase_{chunk_id}.mp3"
        old_entry = old_entries.get(chunk_id)
        if (
            old_entry
            and old_entry.get("text") == chunk_text
            and old_entry.get("voice_profile") == VOICE_PROFILE
            and chunk_path.exists()
        ):
            print(f"tts phrase {index}/{len(groups)} reuse", flush=True)
            chunk_duration = float(old_entry["audio_duration"])
        else:
            for attempt in range(1, 5):
                print(f"tts phrase {index}/{len(groups)} attempt {attempt}", flush=True)
                try:
                    if chunk_path.exists():
                        chunk_path.unlink()
                    with client.audio.speech.with_streaming_response.create(
                        model=MODEL,
                        voice=VOICE,
                        input=chunk_text,
                        instructions=INSTRUCTIONS,
                        speed=SPEED,
                        response_format="mp3",
                    ) as response:
                        response.stream_to_file(chunk_path)
                    if chunk_path.stat().st_size < 2048:
                        raise RuntimeError(f"chunk too small: {chunk_path}")
                    break
                except Exception:
                    if chunk_path.exists():
                        chunk_path.unlink()
                    if attempt == 4:
                        raise
                    time.sleep(attempt * 2)
            chunk_duration = media_duration(ffmpeg, chunk_path)

        chunk_paths.append(chunk_path)
        allocations = allocate_group_duration(group, chunk_duration)
        for allocation in allocations:
            allocation["audio_file"] = str(chunk_path.relative_to(ROOT))
            allocation["voice_profile"] = VOICE_PROFILE
        beat_entries.extend(allocations)
        chunk_entries.append(
            {
                "scene": scene_id,
                "chunk": group["chunk"],
                "chunk_id": chunk_id,
                "audio_file": str(chunk_path.relative_to(ROOT)),
                "audio_duration": chunk_duration,
                "text": chunk_text,
                "beat_start": group["beats"][0][0],
                "beat_end": group["beats"][-1][0],
                "beat_count": len(group["beats"]),
                "voice_profile": VOICE_PROFILE,
            }
        )

    CONCAT_LIST.write_text(
        "\n".join(f"file '{chunk}'" for chunk in chunk_paths) + "\n",
        encoding="utf-8",
    )
    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(CONCAT_LIST),
            "-c:a",
            "libmp3lame",
            "-b:a",
            "128k",
            str(OUTPUT),
        ],
        check=True,
    )

    FINAL.write_bytes(OUTPUT.read_bytes())
    BEAT_AUDIO_MANIFEST.write_text(
        json.dumps(
            {
                "timing_source": "phrase_openai_tts_weighted_alignment",
                "voice_profile": VOICE_PROFILE,
                "beat_count": len(beat_entries),
                "total_audio_duration": sum(item["audio_duration"] for item in beat_entries),
                "chunk_count": len(chunk_entries),
                "beats": beat_entries,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    SCENE_AUDIO_MANIFEST.write_text(
        json.dumps(
            {
                "timing_source": "phrase_openai_tts",
                "voice_profile": VOICE_PROFILE,
                "chunk_count": len(chunk_entries),
                "scene_count": len(scene_groups(BEATS, SCENES)),
                "total_audio_duration": sum(item["audio_duration"] for item in chunk_entries),
                "chunks": chunk_entries,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(FINAL)


if __name__ == "__main__":
    main()
