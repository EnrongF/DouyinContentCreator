import os
import re
from pathlib import Path
from subprocess import PIPE, run

from openai import OpenAI

VOICE_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = VOICE_ROOT / "chunks-openai"
REPORT = VOICE_ROOT / "tts-takes.md"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

MODEL = os.environ.get("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
VOICE = os.environ.get("OPENAI_TTS_VOICE", "marin")
SPEED = float(os.environ.get("OPENAI_TTS_SPEED", "1.0"))

INSTRUCTIONS = """
用自然、口语化的标准普通话朗读，像一个冷静的播客型技术顾问在解释判断。
不要播音腔，不要新闻腔，不要网红语气。
每个输入都是一个短 speech chunk，只表达一个意思。
遇到逗号短停；遇到冒号，停一下再解释；问句轻微上扬。
关键词可以稍微加重，但不要夸张。整体温和、可信、略带思考感。
英文或字母缩写自然读清楚，不要突然切换成夸张英文口音。
""".strip()

CHUNKS = [
    ("c01", "p01", "以前创业，最怕的是做不出来。", "以前最怕做不出来。"),
    ("c02", "p01", "现在更怕的是，做得很快，但方向错了。", "做得很快，但方向错了。"),
    ("c03", "p02", "调研、写代码、写文档、做运营，A I 都能帮你提速。", "调研、代码、文档、运营，AI 都能提速。"),
    ("c04", "p02", "但它不是替你省掉执行。", "AI 不是省掉执行。"),
    ("c05", "p02", "而是把执行推快，让判断更早露出来。", "它把执行推快，让判断更早露出来。"),
    ("c06", "p03", "做得快不是问题。", "做得快不是问题。"),
    ("c07", "p03", "问题是方向错了以后，你会错得更快。", "方向错了以后，会错得更快。"),
    ("c08", "p03", "A I 更像油门，不是方向盘。", "AI 更像油门，不是方向盘。"),
    ("c09", "p03", "它能让你跑得更快，但不能替你决定往哪走。", "它能让你更快，但不能替你决定往哪走。"),
    ("c10", "p03", "真正卡住人的，是创始人有没有想清楚。", "真正卡住人的，是有没有想清楚。"),
    ("c11", "p03", "什么值得做，什么应该先停。", "什么值得做，什么应该先停。"),
    ("c12", "p04", "所以用 A I 创业，起点不是工具，而是一连串判断。", "用 AI 创业，起点不是工具，是一连串判断。"),
    ("c13", "p04", "从想法，到 M V P，到上线，再到规模化。", "从想法，到 MVP，到上线，再到规模化。"),
    ("c14", "p04", "每一关考的都不是同一种判断。", "每一关，考的判断都不一样。"),
    ("c15", "p04", "第一关，是你到底该不该做。", "第一关：到底该不该做。"),
    ("c16", "p04", "后面才轮到边界、系统和护城河。", "后面才轮到边界、系统和护城河。"),
    ("c17", "p05", "所以，用 A I 创业之前，先别急着问怎么更快。", "用 AI 创业，先别急着问怎么更快。"),
    ("c18", "p05", "先问一句：现在缺的是速度，还是判断？", "现在缺的是速度，还是判断？"),
    ("c19", "p05", "下一集，我们先看第一关：有了 Demo，为什么还不代表有人要。", "下一集：有 Demo，为什么还不代表有人要。"),
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


def audio_duration(path: Path) -> float:
    result = run(["afinfo", str(path)], check=True, text=True, stdout=PIPE, stderr=PIPE)
    match = re.search(r"estimated duration:\s*([0-9.]+)\s*sec", result.stdout)
    if not match:
        raise RuntimeError(f"Could not measure audio duration for {path}")
    return float(match.group(1))


def write_report(rows: list[dict]) -> None:
    total = sum(row["duration"] for row in rows)
    lines = [
        "# TTS Takes",
        "",
        "Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`",
        "",
        "## Gate Status",
        "",
        "- Stage: `TTS Takes`",
        "- Status: `generated`",
        "- Pause required: `yes`",
        "- First-choice provider: `qwen-dashscope`",
        "- First-choice status: `blocked after API call; audio download host returned network policy HTML`",
        "- Fallback provider: `openai`",
        f"- Model: `{MODEL}`",
        f"- Voice: `{VOICE}`",
        f"- Speed: `{SPEED}`",
        f"- Measured speech duration: `{total:.3f} seconds`",
        "- Next approved stage: `TTS Take QA / Selection`",
        "- Not approved yet: `ASR`, `voice manifest`, `scene graph`, `visual production`, `render`",
        "",
        "## Generated Chunks",
        "",
        "| Chunk | Paragraph | Duration | Audio | TTS Input | Subtitle |",
        "|---|---|---:|---|---|---|",
    ]
    for row in rows:
        rel = row["path"].relative_to(VOICE_ROOT)
        lines.append(
            f"| `{row['id']}` | `{row['paragraph']}` | {row['duration']:.3f}s | `{rel}` | "
            f"{row['tts']} | {row['subtitle']} |"
        )
    lines.extend(
        [
            "",
            "## QA Notes",
            "",
            "- Audio has been generated and measured only.",
            "- Manual/listening QA is still required before ASR and voice manifest lock.",
            "- Pay special attention to `M V P` in c13 and `Demo` in c19.",
            "- Final timing must be measured again after selected takes are accepted.",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    load_env_file(DEFAULT_ENV)
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is missing.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    client = OpenAI(timeout=90.0, max_retries=2)
    rows = []
    for chunk_id, paragraph, text, subtitle in CHUNKS:
        output = OUTPUT_DIR / f"{chunk_id}.mp3"
        if not (output.exists() and output.stat().st_size > 2048):
            print(f"openai tts {chunk_id}", flush=True)
            with client.audio.speech.with_streaming_response.create(
                model=MODEL,
                voice=VOICE,
                input=text,
                instructions=INSTRUCTIONS,
                response_format="mp3",
                speed=SPEED,
            ) as response:
                response.stream_to_file(output)

        if output.stat().st_size < 2048:
            raise RuntimeError(f"TTS output too small: {output}")
        duration = audio_duration(output)
        rows.append(
            {
                "id": chunk_id,
                "paragraph": paragraph,
                "tts": text,
                "subtitle": subtitle,
                "duration": duration,
                "path": output,
            }
        )
        print(f"{chunk_id}\t{duration:.3f}s\t{output}", flush=True)
    write_report(rows)
    print(REPORT)


if __name__ == "__main__":
    main()
