import os
import re
from difflib import SequenceMatcher
from pathlib import Path

from openai import OpenAI

from generate_qwen_tts import CHUNKS, OUTPUT_DIR, SLUG, VOICE_ROOT

ASR_OUTPUT = VOICE_ROOT / "asr.txt"
QA_OUTPUT = VOICE_ROOT / "asr-qa.md"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")
MODEL = os.environ.get("OPENAI_TRANSCRIBE_MODEL", "gpt-4o-mini-transcribe")

TERM_CHECKS = {
    "c01": ["AI", "Demo"],
    "c02": ["Demo", "验证"],
    "c03": ["Demo"],
    "c08": ["MVP"],
    "c11": ["Demo"],
    "c12": ["真实痛点", "Demo"],
    "c13": ["Demo", "证明有人要"],
    "c14": ["AI", "边界"],
}

NORMALIZE_REPLACEMENTS = {
    "ＡＩ": "AI",
    "A I": "AI",
    "A.I.": "AI",
    "人工智能": "AI",
    "M V P": "MVP",
    "M.V.P.": "MVP",
    "Minimum Viable Product": "MVP",
    "minimum viable product": "MVP",
    "演示": "Demo",
    "展示": "Demo",
    "DEMO": "Demo",
    "驗證": "验证",
    "問題": "问题",
    "實": "实",
    "體": "体",
    "頻": "频",
    "夠": "够",
    "階段": "阶段",
    "邊界": "边界",
    "讓": "让",
    "寫": "写",
    "嗎": "吗",
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


def normalize(text: str) -> str:
    value = text.strip()
    for source, target in NORMALIZE_REPLACEMENTS.items():
        value = value.replace(source, target)
    value = value.lower()
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]", "", value)


def term_status(chunk_id: str, actual: str) -> tuple[str, list[str]]:
    terms = TERM_CHECKS.get(chunk_id, [])
    if not terms:
        return "not_applicable", []
    actual_norm = normalize(actual)
    misses = [term for term in terms if normalize(term) not in actual_norm]
    return ("pass" if not misses else "review"), misses


def main() -> None:
    load_env_file(DEFAULT_ENV)
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is missing.")

    client = OpenAI(timeout=90.0, max_retries=2)
    transcript_sections = []
    qa_rows = []
    review_chunks = []

    for chunk in CHUNKS:
        chunk_id = chunk["id"]
        audio_path = OUTPUT_DIR / f"{chunk_id}.wav"
        if not audio_path.exists():
            raise SystemExit(f"Missing selected audio chunk: {audio_path}")

        with audio_path.open("rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model=MODEL,
                file=audio_file,
                response_format="text",
            )

        expected = chunk["tts"].strip()
        actual = str(transcript).strip()
        similarity = SequenceMatcher(None, normalize(expected), normalize(actual)).ratio()
        term_result, term_misses = term_status(chunk_id, actual)

        core_status = "pass" if similarity >= 0.78 else "review"
        status = "pass" if core_status == "pass" and term_result != "review" else "review"
        if status == "review":
            review_chunks.append(chunk_id)

        transcript_sections.append(
            "\n".join(
                [
                    f"## {chunk_id}",
                    f"Expected: {expected}",
                    f"ASR: {actual}",
                    f"Similarity: {similarity:.3f}",
                    f"Core match: {core_status}",
                    f"Term check: {term_result}",
                ]
            )
        )
        qa_rows.append(
            {
                "id": chunk_id,
                "similarity": similarity,
                "core": core_status,
                "terms": term_result,
                "term_misses": term_misses,
                "status": status,
            }
        )

    ASR_OUTPUT.write_text("\n\n".join(transcript_sections) + "\n", encoding="utf-8")

    gate_status = "Pass" if not review_chunks else "Review Required"
    lines = [
        "# ASR QA",
        "",
        f"Slug: `{SLUG}`",
        "",
        "## Gate Status",
        "",
        "- Stage: `ASR QA`",
        f"- Status: `{gate_status}`",
        "- Pause required: `yes`",
        "- Provider: `openai`",
        f"- Model: `{MODEL}`",
        "- Selected audio: `chunks-qwen/c01.wav` through `chunks-qwen/c14.wav`",
        "- Transcript evidence: `asr.txt`",
        f"- Review chunks: `{', '.join(review_chunks) if review_chunks else 'none'}`",
        "- Next approved stage: `voice manifest`" if not review_chunks else "- Next approved stage: `regenerate or listening review failed chunks`",
        "- Not approved yet: `scene graph`, `visual production`, `render`",
        "",
        "## Decision",
        "",
    ]
    if review_chunks:
        lines.extend(
            [
                "ASR found chunks requiring review before the voice manifest can be locked.",
                "Regenerate or manually approve only the failed chunks, then rerun ASR QA.",
            ]
        )
    else:
        lines.extend(
            [
                "All selected Qwen takes pass ASR core-match and required-term checks.",
                "Proceed to voice manifest creation using the selected chunk audio and measured durations.",
            ]
        )

    lines.extend(
        [
            "",
            "## Chunk Results",
            "",
            "| Chunk | Similarity | Core | Terms | Status | Notes |",
            "|---|---:|---|---|---|---|",
        ]
    )
    for row in qa_rows:
        notes = "missing " + ", ".join(row["term_misses"]) if row["term_misses"] else ""
        lines.append(
            f"| `{row['id']}` | {row['similarity']:.3f} | `{row['core']}` | "
            f"`{row['terms']}` | `{row['status']}` | {notes} |"
        )

    lines.extend(
        [
            "",
            "## QA Notes",
            "",
            "- This gate validates transcript fidelity and required terms by ASR.",
            "- Final listening QA is still required before render because ASR cannot judge tone or fatigue by itself.",
            "",
        ]
    )
    QA_OUTPUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"asr={ASR_OUTPUT}")
    print(f"qa={QA_OUTPUT}")
    print(f"status={gate_status}")
    print(f"review_chunks={','.join(review_chunks) if review_chunks else 'none'}")


if __name__ == "__main__":
    main()
