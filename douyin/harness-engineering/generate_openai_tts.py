import os
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")
INPUT = ROOT / "narration.txt"
OUTPUT = ROOT / "voiceover.openai.mp3"
FINAL = ROOT / "voiceover.final.mp3"

MODEL = os.environ.get("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
VOICE = os.environ.get("OPENAI_TTS_VOICE", "marin")

INSTRUCTIONS = """
用自然、口语化的标准普通话朗读，像冷静的 AI 系统架构师在做高密度技术纪录片旁白。
语速略快但清晰，不要播音腔，不要系统提示音风格，不要网红夸张语气。
情绪稳定、有判断力、可信，重点句稍微加重，长句之间自然停顿。
英文术语保持英文发音，并在术语前后自然停顿：
AI, Coding Agent, Delivery Agent, Harness engineering, delivery harness,
Prompt Engineering, Context Engineering, software delivery knowledge graph,
feature flag, scorecard, rollback, audit log, API key, Delegate, MCP Server, Skills。
""".strip()


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def main() -> None:
    load_env_file(DEFAULT_ENV)
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit(
            "OPENAI_API_KEY is missing. Set it in the environment or "
            f"add it to {DEFAULT_ENV}."
        )

    text = INPUT.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit(f"{INPUT} is empty.")

    client = OpenAI()
    with client.audio.speech.with_streaming_response.create(
        model=MODEL,
        voice=VOICE,
        input=text,
        instructions=INSTRUCTIONS,
        response_format="mp3",
    ) as response:
        response.stream_to_file(OUTPUT)

    FINAL.write_bytes(OUTPUT.read_bytes())
    print(FINAL)


if __name__ == "__main__":
    main()
