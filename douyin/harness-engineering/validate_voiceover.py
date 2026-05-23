import os
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")
AUDIO = ROOT / "voiceover.final.mp3"
TRANSCRIPT = ROOT / "voiceover.transcript.txt"

TERMS = [
    "AI",
    "Prompt Engineering",
    "Context Engineering",
    "Harness Engineering",
    "Coding Agent",
    "Delivery Agent",
    "Harness",
    "harness",
    "delivery harness",
    "software delivery knowledge graph",
    "feature flag",
    "scorecard",
    "rollback",
    "audit log",
    "API key",
    "Delegate",
    "MCP Server",
    "Skills",
]


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def main() -> None:
    load_env_file(DEFAULT_ENV)
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is missing.")
    if not AUDIO.exists():
        raise SystemExit(f"{AUDIO} does not exist.")

    client = OpenAI()
    with AUDIO.open("rb") as audio_file:
        text = client.audio.transcriptions.create(
            model=os.environ.get("OPENAI_TRANSCRIBE_MODEL", "gpt-4o-mini-transcribe"),
            file=audio_file,
            response_format="text",
        )

    TRANSCRIPT.write_text(str(text).strip() + "\n", encoding="utf-8")
    normalized = str(text).lower()
    missing = [term for term in TERMS if term.lower() not in normalized]
    print(f"transcript={TRANSCRIPT}")
    print(f"missing_terms={', '.join(missing) if missing else 'none'}")


if __name__ == "__main__":
    main()
