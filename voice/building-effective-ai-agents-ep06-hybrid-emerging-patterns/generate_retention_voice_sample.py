import os
import re
import subprocess
from pathlib import Path

from openai import OpenAI

VOICE_ROOT = Path(__file__).resolve().parent
OUTPUT = VOICE_ROOT / "voice-tests" / "ep06-opening-retention-marin.mp3"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

MODEL = os.environ.get("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
VOICE = os.environ.get("OPENAI_TTS_VOICE", "marin")

TEXT = """一上来就问：要不要混合架构？

这个问题，其实有点早。

混合架构不是起点。
它更像系统跑起来之后，慢慢长出来的形态。"""

INSTRUCTIONS = """
用自然、口语化的标准普通话朗读。
这是短视频前五秒的开场，要制造轻微认知冲突：不是夸张，不是吓人，而是冷静地指出观众的问题问早了。

表演要求：
- 语气：冷静、略带挑战感，像技术播客主持人提出一个反直觉判断。
- 第一句直接一点，“混合架构”稍微加重，问号轻微上扬。
- 问句之后停一下。
- “这个问题，其实有点早。”放慢一点，“有点早”要有判断感。
- 后两句转为解释，语气更稳。
- 不要播音腔，不要新闻腔，不要网红语气。
- 换行处做自然节奏重置。
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

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    client = OpenAI(timeout=90.0, max_retries=2)

    with client.audio.speech.with_streaming_response.create(
        model=MODEL,
        voice=VOICE,
        input=TEXT,
        instructions=INSTRUCTIONS,
        response_format="mp3",
        speed=1.0,
    ) as response:
        response.stream_to_file(OUTPUT)

    print(f"{VOICE}\t{MODEL}\t{audio_duration(OUTPUT):.3f}s\t{OUTPUT}")


if __name__ == "__main__":
    main()
