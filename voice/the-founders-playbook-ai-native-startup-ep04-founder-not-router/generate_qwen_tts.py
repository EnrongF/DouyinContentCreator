import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from subprocess import PIPE, run

VOICE_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = VOICE_ROOT / "chunks-qwen"
REPORT = VOICE_ROOT / "tts-takes.md"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

SLUG = "the-founders-playbook-ai-native-startup-ep04-founder-not-router"
MODEL = os.environ.get("QWEN_TTS_MODEL", "qwen3-tts-instruct-flash")
VOICE = os.environ.get("QWEN_TTS_VOICE", "Ethan")
ENDPOINTS = [
    "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
    "https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
]

INSTRUCTION = (
    "自然口语化的标准普通话。像冷静的技术播客主持人，直接、可信、有一点创始人判断感。"
    "不要播音腔，不要新闻腔，不要网红语气。整体比短视频快嘴稍慢，保留思考停顿；"
    "关键判断稍微放慢，列表项保持清楚节奏。"
)

CHUNKS = [
    {
        "id": "c01",
        "paragraph": "p01",
        "tts": "产品上线后，如果每个问题都还要创始人接住，公司就没有真正进入增长。",
        "subtitle": "每个问题都等创始人，公司就还没进入增长。",
    },
    {
        "id": "c02",
        "paragraph": "p01",
        "tts": "M V P 证明产品值得存在；Launch 证明业务能不能重复增长。",
        "subtitle": "MVP 证明产品；Launch 证明增长能不能重复。",
    },
    {
        "id": "c03",
        "paragraph": "p02",
        "tts": "早期，创始人在每个回路里，是优势：学得快，判断也快。",
        "subtitle": "早期，创始人在回路里，是优势。",
    },
    {
        "id": "c04",
        "paragraph": "p02",
        "tts": "但上线以后，同一个习惯会变成瓶颈。",
        "subtitle": "上线以后，同一个习惯会变成瓶颈。",
    },
    {
        "id": "c05",
        "paragraph": "p03",
        "tts": "一个一小时能决定的问题，因为等你，拖成一周。",
        "subtitle": "一小时的决定，因为等你，拖成一周。",
    },
    {
        "id": "c06",
        "paragraph": "p03",
        "tts": "支持消息堆起来，Bug 分流没人接，周报只在你想起来时才发生。",
        "subtitle": "支持、Bug、周报，都开始排队。",
    },
    {
        "id": "c07",
        "paragraph": "p04",
        "tts": "这时不要问自己：“我怎么再忙一点？”",
        "subtitle": "不要问：我怎么再忙一点？",
    },
    {
        "id": "c08",
        "paragraph": "p04",
        "tts": "要把亲手处理的事情列出来，分成三类。",
        "subtitle": "把亲手处理的事，分成三类。",
    },
    {
        "id": "c09",
        "paragraph": "p04",
        "tts": "能自动化的，交给系统；能交给别人的，交给角色。",
        "subtitle": "能自动化的交给系统，能交给别人的交给角色。",
    },
    {
        "id": "c10",
        "paragraph": "p04",
        "tts": "只把真正需要方向、取舍和风险判断的事，留给创始人。",
        "subtitle": "只把方向、取舍、风险判断留给创始人。",
    },
    {
        "id": "c11",
        "paragraph": "p05",
        "tts": "这一集的判断是：重复发生的问题，要变成系统。",
        "subtitle": "重复发生的问题，要变成系统。",
    },
    {
        "id": "c12",
        "paragraph": "p05",
        "tts": "下一集，我们看护城河为什么不只在模型里，而在业务流程里。",
        "subtitle": "下一集：护城河藏在业务流程里。",
    },
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


def post_json(url: str, api_key: str, payload: dict) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        return json.loads(response.read().decode("utf-8"))


def find_audio_url(response: dict) -> str | None:
    candidates = [
        response.get("output", {}).get("audio", {}).get("url"),
        response.get("output", {}).get("url"),
        response.get("audio", {}).get("url"),
    ]
    for value in candidates:
        if isinstance(value, str) and value.startswith("http"):
            return value
    return None


def download(url: str, path: Path) -> None:
    with urllib.request.urlopen(url, timeout=90) as response:
        payload = response.read()
    trimmed = payload.lstrip()[:64].lower()
    if trimmed.startswith(b"<!doctype html") or trimmed.startswith(b"<html"):
        raise RuntimeError("Audio download returned HTML instead of audio.")
    path.write_bytes(payload)


def synthesize(api_key: str, text: str, output: Path) -> str:
    payload = {
        "model": MODEL,
        "input": {
            "text": text,
            "voice": VOICE,
            "language_type": "Chinese",
            "instruction": INSTRUCTION,
            "optimize_instructions": True,
        },
    }
    last_error = None
    for endpoint in ENDPOINTS:
        try:
            response = post_json(endpoint, api_key, payload)
            audio_url = find_audio_url(response)
            if not audio_url:
                raise RuntimeError(f"No audio URL in response: {json.dumps(response, ensure_ascii=False)[:500]}")
            print(f"audio_url_host={urllib.parse.urlparse(audio_url).netloc}", flush=True)
            download(audio_url, output)
            return endpoint
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            last_error = exc
            time.sleep(0.25)
    raise RuntimeError(f"Qwen TTS failed: {last_error}")


def write_report(rows: list[dict]) -> None:
    total = sum(row["duration"] for row in rows)
    lines = [
        "# TTS Takes",
        "",
        f"Slug: `{SLUG}`",
        "",
        "## Gate Status",
        "",
        "- Stage: `TTS Takes`",
        "- Status: `generated`",
        "- Pause required: `yes`",
        "- Provider: `qwen-dashscope`",
        f"- Model: `{MODEL}`",
        f"- Voice: `{VOICE}`",
        f"- Measured speech duration: `{total:.3f} seconds`",
        "- Next approved stage: `ASR QA`",
        "- Not approved yet: `voice manifest`, `scene graph`, `visual production`, `render`",
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
            "- ASR QA is required before voice manifest lock.",
            "- Pay special attention to `MVP`, `Launch`, `Bug`, `取舍`, and `护城河` pronunciation.",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    load_env_file(DEFAULT_ENV)
    api_key = os.environ.get("DASHSCOPE_API_KEY") or os.environ.get("QWEN_API_KEY")
    if not api_key:
        raise SystemExit("DASHSCOPE_API_KEY or QWEN_API_KEY is missing.")

    force_ids = {value.strip() for value in os.environ.get("QWEN_TTS_REGENERATE", "").split(",") if value.strip()}
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for chunk in CHUNKS:
        output = OUTPUT_DIR / f"{chunk['id']}.wav"
        if chunk["id"] in force_ids or not (output.exists() and output.stat().st_size > 2048):
            print(f"qwen tts {chunk['id']}", flush=True)
            endpoint = synthesize(api_key, chunk["tts"], output)
        else:
            endpoint = "reused"
        if output.stat().st_size < 2048:
            raise RuntimeError(f"TTS output too small: {output}")
        duration = audio_duration(output)
        rows.append({**chunk, "duration": duration, "path": output, "endpoint": endpoint})
        print(f"{chunk['id']}\t{duration:.3f}s\t{output}", flush=True)
    write_report(rows)
    print(REPORT)


if __name__ == "__main__":
    main()
