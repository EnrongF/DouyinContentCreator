import subprocess
import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEPS = Path("/private/tmp/codex_imageio_ffmpeg")
sys.path.insert(0, str(DEPS))

import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
frames = ROOT / "frames"
voice_candidates = [
    ROOT / "voiceover.final.mp3",
    ROOT / "voiceover.openai.mp3",
    ROOT / "voiceover.aiff",
]
voice = next((candidate for candidate in voice_candidates if candidate.exists()), None)
if voice is None:
    raise SystemExit("No voiceover found. Generate voiceover.final.mp3 first.")
concat = ROOT / "frames.txt"
silent_video = ROOT / "video.silent.mp4"
final_video = ROOT / "video.mp4"

minimum_duration = 85.54


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


voice_duration = media_duration(voice)
target_duration = max(minimum_duration, (voice_duration or minimum_duration) + 0.35)
frame_paths = sorted(frames.glob("scene_*.png"))
if not frame_paths:
    raise SystemExit(f"No frames found in {frames}.")
duration_per_frame = target_duration / len(frame_paths)

lines = []
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
        "-movflags",
        "+faststart",
        str(silent_video),
    ],
    check=True,
)

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
