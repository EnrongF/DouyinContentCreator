import json
import os
import re
from difflib import SequenceMatcher
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
VOICE_ROOT = ROOT / "voice" / "building-effective-ai-agents"
VOICE_MANIFEST = VOICE_ROOT / "voice-manifest.json"
ASR_OUTPUT = VOICE_ROOT / "asr.txt"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

TERMS = [
    "Agent",
    "Workflow",
    "Single Agent",
    "Multi-Agent",
    "Harness",
    "CRM",
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
        "agent": "智能体",
        "multi-agent": "多智能体",
        "multi agent": "多智能体",
        "single agent": "单智能体",
        "workflow": "工作流",
        "sequential workflow": "顺序工作流",
        "harness": "运行护栏",
        "crm": "crm",
        "企業": "企业",
        "問": "问",
        "錯": "错",
        "這": "这",
        "選": "选",
        "項": "项",
        "誌": "志",
        "監": "监",
        "評": "评",
        "滾": "滚",
        "權": "权",
        "限": "限",
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

    full_transcript = "\n\n".join(sections) + "\n"
    ASR_OUTPUT.write_text(full_transcript, encoding="utf-8")

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
