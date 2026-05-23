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

SLUG = "the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand"
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
        "tts": "A I 让你很快做出 Demo。",
        "subtitle": "AI 很快做出 Demo。",
    },
    {
        "id": "c02",
        "paragraph": "p01",
        "tts": "但最危险的地方也在这里：演示版一出来，你很容易以为问题已经被验证了。",
        "subtitle": "Demo 一出来，很容易以为问题已验证。",
    },
    {
        "id": "c03",
        "paragraph": "p02",
        "tts": "其实，Demo 不是没用。它很有用。",
        "subtitle": "Demo 不是没用，它很有用。",
    },
    {
        "id": "c04",
        "paragraph": "p02",
        "tts": "但它不是用来证明你对了，而是用来帮你问清楚：这个问题到底是不是真的存在。",
        "subtitle": "它不是证明你对了，而是帮你问清楚。",
    },
    {
        "id": "c05",
        "paragraph": "p03",
        "tts": "在想法阶段，真正要过的不是“能不能做出来”，而是三件事。",
        "subtitle": "想法阶段，真正要过的是三件事。",
    },
    {
        "id": "c06",
        "paragraph": "p03",
        "tts": "第一，问题是不是真实、具体，而且经常发生。",
        "subtitle": "问题是否真实、具体、经常发生。",
    },
    {
        "id": "c07",
        "paragraph": "p03",
        "tts": "第二，你的方案是不是解决了用户真正的问题，而不是你一开始想象的问题。",
        "subtitle": "方案是否解决了真正的问题。",
    },
    {
        "id": "c08",
        "paragraph": "p03",
        "tts": "第三，信号够不够支持你开始做 M V P。",
        "subtitle": "信号是否足够支持开始做 MVP。",
    },
    {
        "id": "c09",
        "paragraph": "p04",
        "tts": "所以，别只问用户：“你会不会用？”",
        "subtitle": "别只问：“你会不会用？”",
    },
    {
        "id": "c10",
        "paragraph": "p04",
        "tts": "更好的问题是：你上一次遇到这个问题是什么时候？现在怎么解决？为什么还不换？",
        "subtitle": "上次什么时候遇到？现在怎么解决？为什么还不换？",
    },
    {
        "id": "c11",
        "paragraph": "p05",
        "tts": "如果用户只是在夸 Demo，你还没有答案。",
        "subtitle": "只是在夸 Demo，还没有答案。",
    },
    {
        "id": "c12",
        "paragraph": "p05",
        "tts": "如果他开始暴露真实痛点，甚至指出你的 Demo 哪里没解决问题，那才是更有价值的信号。",
        "subtitle": "暴露真实痛点，才是更有价值的信号。",
    },
    {
        "id": "c13",
        "paragraph": "p05",
        "tts": "这一集的判断是：Demo 可以帮你问问题，但不能替你证明有人要。",
        "subtitle": "Demo 可以帮你问问题，不能证明有人要。",
    },
    {
        "id": "c14",
        "paragraph": "p05",
        "tts": "下一集，我们看确定要做以后，为什么要先定边界，再让 A I 写。",
        "subtitle": "下一集：先定边界，再让 AI 写。",
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
            "- Pay special attention to `Demo`, `M V P`, and `A I` pronunciation.",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    load_env_file(DEFAULT_ENV)
    api_key = os.environ.get("DASHSCOPE_API_KEY") or os.environ.get("QWEN_API_KEY")
    if not api_key:
        raise SystemExit("DASHSCOPE_API_KEY or QWEN_API_KEY is missing.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for chunk in CHUNKS:
        output = OUTPUT_DIR / f"{chunk['id']}.wav"
        if not (output.exists() and output.stat().st_size > 2048):
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
