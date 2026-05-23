import json
import os
import re
from difflib import SequenceMatcher
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
SLUG = Path(__file__).resolve().parent.name
VOICE_ROOT = ROOT / "voice" / SLUG
VOICE_MANIFEST = VOICE_ROOT / "voice-manifest.json"
ASR_OUTPUT = VOICE_ROOT / "asr.txt"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

TERMS = [
    "Agent",
    "Workflow",
    "Single Agent",
    "Multi-Agent",
    "Agentic Workflows",
    "Token",
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


def normalize(text: str) -> str:
    value = text.lower()
    for source, target in {
        "架構": "架构",
        "起點": "起点",
        "系統": "系统",
        "型態": "形态",
        "觀測": "观测",
        "業務": "业务",
        "價值": "价值",
        "還": "还",
        "解決": "解决",
        "真實": "真实",
        "讓": "让",
        "跟著": "跟着",
        "證據": "证据",
        "進": "进",
    }.items():
        value = value.replace(source, target)
    for source, target in {
        "agentic workflows": "工作流",
        "agentic workflow": "工作流",
        "multi-agent": "多智能体",
        "multi agent": "多智能体",
        "single agent": "单智能体",
        "workflow": "工作流",
        "agent": "智能体",
        "token": "token",
        "十到十五": "10到15",
        "10-15": "10到15",
        "10 到 15": "10到15",
    }.items():
        value = value.replace(source, target)
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]", "", value)


def main() -> None:
    load_env_file(DEFAULT_ENV)
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is missing.")

    manifest = json.loads(VOICE_MANIFEST.read_text(encoding="utf-8"))
    client = OpenAI(timeout=90.0, max_retries=2)

    sections = []
    misses = []
    for chunk in manifest["chunks"]:
        audio_path = VOICE_ROOT / chunk["audioFile"]
        with audio_path.open("rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model=os.environ.get("OPENAI_TRANSCRIBE_MODEL", "gpt-4o-mini-transcribe"),
                file=audio_file,
                response_format="text",
            )

        expected = chunk["text"].strip()
        actual = str(transcript).strip()
        expected_norm = normalize(expected)
        actual_norm = normalize(actual)
        similarity = SequenceMatcher(None, expected_norm, actual_norm).ratio()
        contains_core = similarity >= 0.72

        if not contains_core:
            misses.append(chunk["id"])

        sections.append(
            "\n".join(
                [
                    f"## {chunk['id']}",
                    f"Expected: {expected}",
                    f"ASR: {actual}",
                    f"Similarity: {similarity:.3f}",
                    f"Core match: {'pass' if contains_core else 'review'}",
                ]
            )
        )

    ASR_OUTPUT.write_text("\n\n".join(sections) + "\n", encoding="utf-8")

    manifest["asrTranscript"] = "asr.txt"
    manifest["asrStatus"] = "review_required" if misses else "pass"
    manifest["asrReviewChunks"] = misses
    manifest["termQa"] = {
        "terms": TERMS,
        "note": "ASR may translate English terms into Chinese; final QA should be by listening.",
    }
    VOICE_MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"asr={ASR_OUTPUT}")
    print(f"status={manifest['asrStatus']}")
    print(f"review_chunks={','.join(misses) if misses else 'none'}")


if __name__ == "__main__":
    main()
