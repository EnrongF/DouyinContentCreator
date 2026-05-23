import os
import re
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")
AUDIO = ROOT / "voiceover.final.mp3"
TRANSCRIPT = ROOT / "voiceover.transcript.txt"

TERMS = [
    "OpenAI",
    "Codex",
    "Harness",
    "AGENTS",
    "Chrome DevTools",
    "日志",
    "指标",
    "链路",
    "Providers",
    "AI",
]

FORBIDDEN_SPOKEN_PATTERNS = [
    (r"\bPR\b", "Use `代码合并请求` in narration; keep `PR` for visuals only."),
    (r"\bCI\b", "Use `持续集成` in narration; keep `CI` for visuals only."),
    (r"\bworktree\b", "Use `独立工作区` in narration; keep `worktree` for visuals only."),
    (r"\bagent\b", "Use `智能体` in narration unless the exact source term must be spoken."),
    (r"\bbug\b", "Use `问题` in narration; English `bug` sounds less natural in this Mandarin cut."),
    (r"docs\s*目录", "Use `文档目录` in narration; keep `docs/` for visuals only."),
]

REQUIRED_NATURAL_PHRASES = [
    "代码合并请求",
    "持续集成",
    "独立工作区",
    "智能体",
    "黄金原则",
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


def validate_spoken_script() -> None:
    from render_assets import BEAT_VOICE_TEXTS

    script = "\n".join(BEAT_VOICE_TEXTS)
    failures = []
    for pattern, message in FORBIDDEN_SPOKEN_PATTERNS:
        if re.search(pattern, script, re.IGNORECASE):
            failures.append(message)
    for phrase in REQUIRED_NATURAL_PHRASES:
        if phrase not in script:
            failures.append(f"Expected natural spoken phrase missing: `{phrase}`.")
    if failures:
        print("script_pronunciation_gate=fail")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)
    print("script_pronunciation_gate=pass")


def main() -> None:
    load_env_file(DEFAULT_ENV)
    validate_spoken_script()
    if os.environ.get("VOICEOVER_VALIDATE_SKIP_TRANSCRIBE") == "1":
        print("transcription_gate=skipped")
        return
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

    transcript = str(text).strip()
    TRANSCRIPT.write_text(transcript + "\n", encoding="utf-8")
    normalized = transcript.lower()
    compact = "".join(ch for ch in normalized if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")
    missing = []
    for term in TERMS:
        term_normalized = term.lower()
        term_compact = "".join(ch for ch in term_normalized if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")
        accepted_compacts = {term_compact}
        if term == "AGENTS":
            accepted_compacts.update({"agent", "agents", "agentmd", "agentsmd"})
        if term == "Harness":
            accepted_compacts.update({"harnes", "harnesengineering"})
        if term_normalized not in normalized and term_compact not in compact:
            if not any(alias in compact for alias in accepted_compacts):
                missing.append(term)
    print(f"transcript={TRANSCRIPT}")
    print(f"missing_terms={', '.join(missing) if missing else 'none'}")
    if missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
