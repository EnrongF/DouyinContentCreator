import os
import re
import subprocess
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
VOICE_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = VOICE_ROOT / "voice-tests"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

MODEL = os.environ.get("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
VOICES = ["marin", "cedar", "nova", "shimmer", "fable"]
SAMPLE_TEXT = """一上来就问：要不要混合架构？
这个问题，其实有点早。

混合架构不是起点。
它更像系统跑起来之后，慢慢长出来的形态。"""

INSTRUCTIONS = """
用自然、口语化的标准普通话朗读，像一个冷静的播客型技术顾问在解释判断。
不要播音腔，不要新闻腔，不要网红语气。
遇到换行，做一次自然的节奏重置；遇到问号，轻微上扬。
整体保持温和、可信、略带思考感。
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
        raise SystemExit("OPENAI_API_KEY is missing.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    client = OpenAI(timeout=90.0, max_retries=2)

    for voice in VOICES:
        output = OUTPUT_DIR / f"ep06-sample-{voice}.mp3"
        with client.audio.speech.with_streaming_response.create(
            model=MODEL,
            voice=voice,
            input=SAMPLE_TEXT,
            instructions=INSTRUCTIONS,
            response_format="mp3",
            speed=1.0,
        ) as response:
            response.stream_to_file(output)
        print(f"{voice}\t{audio_duration(output):.3f}s\t{output}")


if __name__ == "__main__":
    main()
