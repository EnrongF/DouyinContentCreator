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

SLUG = "the-founders-playbook-ai-native-startup-ep05-workflow-moat"
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
        "tts": "很多人讲 A I 创业的护城河，第一反应是：我用了哪个模型。",
        "subtitle": "讲护城河，别只看用了哪个模型。",
    },
    {
        "id": "c02",
        "paragraph": "p01",
        "tts": "但到规模化阶段，模型权限本身很难成为护城河。别人也能接入相似的能力。",
        "subtitle": "模型权限本身，很难成为护城河。",
    },
    {
        "id": "c03",
        "paragraph": "p02",
        "tts": "真正开始拉开差距的，是业务流程里一层一层沉淀下来的细节。",
        "subtitle": "差距来自业务流程里沉淀的细节。",
    },
    {
        "id": "c04",
        "paragraph": "p03",
        "tts": "比如，你知道这个行业的例外情况；你的系统接住了真实用户的行为。",
        "subtitle": "行业例外、用户行为，开始进入系统。",
    },
    {
        "id": "c05",
        "paragraph": "p03",
        "tts": "你的流程连上了客户原来的工具，也留下了真实协作的痕迹。",
        "subtitle": "流程接入工具，也留下协作痕迹。",
    },
    {
        "id": "c06",
        "paragraph": "p04",
        "tts": "这些东西不是一句提示词，也不是换一个模型就能复制。",
        "subtitle": "这些不是换个模型就能复制。",
    },
    {
        "id": "c07",
        "paragraph": "p04",
        "tts": "它们会变成上下文、数据、集成、习惯，最后变成切换成本。",
        "subtitle": "上下文、数据、集成、习惯，会变成切换成本。",
    },
    {
        "id": "c08",
        "paragraph": "p05",
        "tts": "所以，这一集不要问：我们是不是用了 A I？",
        "subtitle": "不要只问：我们是不是用了 AI？",
    },
    {
        "id": "c09",
        "paragraph": "p05",
        "tts": "要问：我们的 A I 系统里，沉淀了哪些只有我们才有的业务细节？",
        "subtitle": "要问：系统里沉淀了哪些独特业务细节？",
    },
    {
        "id": "c10",
        "paragraph": "p05",
        "tts": "这才是 A I native 公司在规模化以后，可能长出护城河的地方。",
        "subtitle": "工作流里，才可能长出护城河。",
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
