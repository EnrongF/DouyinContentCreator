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
    "c01": ["护城河", "模型"],
    "c02": ["规模化", "模型", "护城河"],
    "c03": ["业务流程", "沉淀", "细节"],
    "c04": ["行业", "用户"],
    "c05": ["流程", "工具", "协作"],
    "c06": ["提示词", "模型", "复制"],
    "c07": ["上下文", "数据", "集成", "习惯", "切换成本"],
    "c08": ["AI"],
    "c09": ["系统", "业务细节"],
    "c10": ["AI", "规模化", "护城河"],
}

NORMALIZE_REPLACEMENTS = {
    "ＭＶＰ": "MVP",
    "M V P": "MVP",
    "M.V.P.": "MVP",
    "LAUNCH": "Launch",
    "launch": "Launch",
    "Lunch": "Launch",
    "lunch": "Launch",
    "Bug": "bug",
    "BUG": "bug",
    "中轉站": "中转站",
    "創始人": "创始人",
    "業務": "业务",
    "證明": "证明",
    "增長": "增长",
    "問題": "问题",
    "發生": "发生",
    "風險": "风险",
    "判斷": "判断",
    "護城河": "护城河",
    "業務流程": "业务流程",
    "規模化": "规模化",
    "權限": "权限",
    "數據": "数据",
    "習慣": "习惯",
    "切換成本": "切换成本",
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
        "- Selected audio: `chunks-qwen/c01.wav` through `chunks-qwen/c12.wav`",
        "- Transcript evidence: `asr.txt`",
        f"- Review chunks: `{', '.join(review_chunks) if review_chunks else 'none'}`",
        "- Next approved stage: `render QA`" if not review_chunks else "- Next approved stage: `regenerate or listening review failed chunks`",
        "",
        "## Decision",
        "",
    ]
    if review_chunks:
        lines.extend(
            [
                "ASR found chunks requiring review before publish.",
                "Regenerate or manually approve failed chunks, then rerun ASR QA.",
            ]
        )
    else:
        lines.extend(
            [
                "All selected Qwen takes pass ASR core-match and required-term checks.",
                "Proceed with render QA and package verification.",
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
    lines.append("")
    QA_OUTPUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"asr={ASR_OUTPUT}")
    print(f"qa={QA_OUTPUT}")
    print(f"status={gate_status}")
    print(f"review_chunks={','.join(review_chunks) if review_chunks else 'none'}")


if __name__ == "__main__":
    main()
