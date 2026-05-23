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

SLUG = "the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code"
MODEL = os.environ.get("QWEN_TTS_MODEL", "qwen3-tts-instruct-flash")
VOICE = os.environ.get("QWEN_TTS_VOICE", "Ethan")
ENDPOINTS = [
    "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
    "https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
]

INSTRUCTION = (
    "自然口语化的标准普通话。像冷静的技术播客主持人，直接、可信、略带判断感。"
    "不要播音腔，不要新闻腔，不要网红语气。短句之间保留自然停顿；"
    "问句轻微上扬，关键判断稍微放慢。"
)

CHUNKS = [
    {
        "id": "c01",
        "paragraph": "p01",
        "tts": "A I 写代码很快。",
        "subtitle": "AI 写代码很快。",
    },
    {
        "id": "c02",
        "paragraph": "p01",
        "tts": "但如果产品边界不清楚，它也会很快把产品写散。",
        "subtitle": "边界不清楚，产品会被写散。",
    },
    {
        "id": "c03",
        "paragraph": "p02",
        "tts": "有了验证信号以后，下一关不是马上把功能做满。",
        "subtitle": "有了验证信号，不是马上做满功能。",
    },
    {
        "id": "c04",
        "paragraph": "p02",
        "tts": "M V P 阶段，本质上还是在收集证据：一小群真实用户，会不会回来、付费，或者愿意推荐。",
        "subtitle": "MVP 阶段，还是在收集证据。",
    },
    {
        "id": "c05",
        "paragraph": "p03",
        "tts": "所以，最小可用产品，最重要的不是“还能加什么”。",
        "subtitle": "最重要的不是“还能加什么”。",
    },
    {
        "id": "c06",
        "paragraph": "p03",
        "tts": "而是先写清楚三件事：它现在解决什么，暂时不解决什么，什么证据才允许你加新功能。",
        "subtitle": "先写清楚：解决什么、不解决什么、什么证据能加。",
    },
    {
        "id": "c07",
        "paragraph": "p04",
        "tts": "不然，每次让 A I 开工，它都会重新猜一遍产品边界。",
        "subtitle": "每次让 AI 开工，它都会重新猜边界。",
    },
    {
        "id": "c08",
        "paragraph": "p03",
        "tts": "今天加一个边缘场景，明天补一个酷功能，后天整个产品就开始失去形状。",
        "subtitle": "一个又一个功能，产品开始失去形状。",
    },
    {
        "id": "c09",
        "paragraph": "p04",
        "tts": "这就是 A I 时代更隐蔽的技术债：代码可能能跑，但产品边界和架构上下文已经开始漂移。",
        "subtitle": "AI 技术债：边界和上下文开始漂移。",
    },
    {
        "id": "c10",
        "paragraph": "p04",
        "tts": "所以，让 A I 写之前，先把边界和上下文放到它能读到的地方。",
        "subtitle": "让 AI 写之前，先放好边界和上下文。",
    },
    {
        "id": "c11",
        "paragraph": "p05",
        "tts": "这一集的判断是：先写边界，再写代码。",
        "subtitle": "先写边界，再写代码。",
    },
    {
        "id": "c12",
        "paragraph": "p05",
        "tts": "下一集，我们看产品上线以后，创始人为什么不能继续做所有事情的中转站。",
        "subtitle": "下一集：创始人别当中转站。",
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
    result = run(
        ["afinfo", str(path)],
        check=True,
        text=True,
        stdout=PIPE,
        stderr=PIPE,
    )
    match = re.search(r"estimated duration:\s*([0-9.]+)\s*sec", result.stdout)
    if not match:
        raise RuntimeError(f"Could not measure audio duration for {path}")
    return float(match.group(1))


def post_json(url: str, api_key: str, payload: dict) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
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
            "- Pay special attention to `A I`, `M V P`, `边界`, and `架构上下文` pronunciation.",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    load_env_file(DEFAULT_ENV)
    api_key = os.environ.get("DASHSCOPE_API_KEY") or os.environ.get("QWEN_API_KEY")
    if not api_key:
        raise SystemExit("DASHSCOPE_API_KEY or QWEN_API_KEY is missing.")

    force_ids = {
        value.strip()
        for value in os.environ.get("QWEN_TTS_REGENERATE", "").split(",")
        if value.strip()
    }
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
