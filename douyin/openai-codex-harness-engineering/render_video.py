import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEPS = Path("/private/tmp/codex_imageio_ffmpeg")
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

try:
    import imageio_ffmpeg

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    ffmpeg = shutil.which("ffmpeg")

if not ffmpeg:
    raise SystemExit("ffmpeg not found. Install ffmpeg or imageio_ffmpeg.")
frames = ROOT / "frames"
frame_manifest = ROOT / "frame_durations.json"
voice_candidates = [
    ROOT / "voiceover.final.mp3",
    ROOT / "voiceover.openai.mp3",
    ROOT / "voiceover.aiff",
]
voice = next((candidate for candidate in voice_candidates if candidate.exists()), None)
concat = ROOT / "frames.txt"
silent_video = ROOT / "video.silent.mp4"
final_video = ROOT / "video.mp4"

minimum_duration = 75.0


def media_duration(path: Path) -> float | None:
    result = subprocess.run(
        [ffmpeg, "-i", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", result.stderr)
    if not match:
        return None
    hours, minutes, seconds = match.groups()
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


frame_paths = sorted(frames.glob("scene_*.png"))
if not frame_paths:
    raise SystemExit(f"No frames found in {frames}.")

voice_duration = media_duration(voice) if voice else None
target_duration = max(minimum_duration, (voice_duration or minimum_duration) + 0.35)

lines = []
if frame_manifest.exists():
    manifest = json.loads(frame_manifest.read_text(encoding="utf-8"))
    manifest_frames = manifest.get("frames", [])
    raw_total = sum(float(item.get("duration_hint", 0.0)) for item in manifest_frames)
    if raw_total <= 0:
        raise SystemExit(f"Invalid timing manifest: {frame_manifest}")
    use_audio_timing = manifest.get("timing_source") == "beat_audio_manifest"
    scale = 1.0 if use_audio_timing else target_duration / raw_total
    if use_audio_timing:
        target_duration = max(raw_total, voice_duration or raw_total) + 0.08
    frame_paths = []
    for item in manifest_frames:
        frame = ROOT / item["file"]
        if not frame.exists():
            raise SystemExit(f"Manifest frame missing: {frame}")
        frame_paths.append(frame)
        lines.append(f"file '{frame}'")
        lines.append(f"duration {max(0.03, float(item['duration_hint']) * scale):.4f}")
else:
    duration_per_frame = target_duration / len(frame_paths)
    for frame in frame_paths:
        lines.append(f"file '{frame}'")
        lines.append(f"duration {duration_per_frame:.2f}")
lines.append(f"file '{frame_paths[-1]}'")
concat.write_text("\n".join(lines) + "\n", encoding="utf-8")

subprocess.run(
    [
        ffmpeg,
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat),
        "-vf",
        "fps=30,format=yuv420p",
        "-c:v",
        "libx264",
        "-crf",
        "18",
        "-preset",
        "slow",
        "-movflags",
        "+faststart",
        str(silent_video),
    ],
    check=True,
)

if voice is None:
    print(silent_video)
    raise SystemExit(0)

subprocess.run(
    [
        ffmpeg,
        "-y",
        "-i",
        str(silent_video),
        "-i",
        str(voice),
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-t",
        f"{target_duration:.2f}",
        "-c:v",
        "libx264",
        "-crf",
        "18",
        "-preset",
        "slow",
        "-profile:v",
        "high",
        "-level",
        "4.1",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-movflags",
        "+faststart",
        str(final_video),
    ],
    check=True,
)

print(final_video)
