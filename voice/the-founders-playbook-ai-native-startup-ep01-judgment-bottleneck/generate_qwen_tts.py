import json
import os
import re
import time
import urllib.error
import urllib.request
import urllib.parse
from pathlib import Path
from subprocess import PIPE, run

ROOT = Path(__file__).resolve().parents[2]
VOICE_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = VOICE_ROOT / "chunks-qwen"
REPORT = VOICE_ROOT / "tts-takes.md"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

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
        "tts": "以前创业，最怕的是做不出来。",
        "subtitle": "以前最怕做不出来。",
    },
    {
        "id": "c02",
        "paragraph": "p01",
        "tts": "现在更怕的是，做得很快，但方向错了。",
        "subtitle": "做得很快，但方向错了。",
    },
    {
        "id": "c03",
        "paragraph": "p02",
        "tts": "调研、写代码、写文档、做运营，A I 都能帮你提速。",
        "subtitle": "调研、代码、文档、运营，AI 都能提速。",
    },
    {
        "id": "c04",
        "paragraph": "p02",
        "tts": "但它不是替你省掉执行。",
        "subtitle": "AI 不是省掉执行。",
    },
    {
        "id": "c05",
        "paragraph": "p02",
        "tts": "而是让执行变快，让判断更早露出来。",
        "subtitle": "它让执行变快，让判断更早露出来。",
    },
    {
        "id": "c06",
        "paragraph": "p03",
        "tts": "做得快不是问题。",
        "subtitle": "做得快不是问题。",
    },
    {
        "id": "c07",
        "paragraph": "p03",
        "tts": "问题是方向错了以后，你会错得更快。",
        "subtitle": "方向错了以后，会错得更快。",
    },
    {
        "id": "c08",
        "paragraph": "p03",
        "tts": "A I 这个工具，更像油门，不是方向盘。",
        "subtitle": "AI 更像油门，不是方向盘。",
    },
    {
        "id": "c09",
        "paragraph": "p03",
        "tts": "它能让你跑得更快，但不能帮你决定往哪走。",
        "subtitle": "它能让你更快，但不能帮你决定往哪走。",
    },
    {
        "id": "c10",
        "paragraph": "p03",
        "tts": "真正卡住人的，是创始人有没有想清楚。",
        "subtitle": "真正卡住人的，是有没有想清楚。",
    },
    {
        "id": "c11",
        "paragraph": "p03",
        "tts": "什么值得做，什么应该先停。",
        "subtitle": "什么值得做，什么应该先停。",
    },
    {
        "id": "c12",
        "paragraph": "p04",
        "tts": "所以用 A I 创业，起点不是工具，而是一连串判断。",
        "subtitle": "用 AI 创业，起点不是工具，是一连串判断。",
    },
    {
        "id": "c13",
        "paragraph": "p04",
        "tts": "从想法，到 M V P，到上线，再到规模化。",
        "subtitle": "从想法，到 MVP，到上线，再到规模化。",
    },
    {
        "id": "c14",
        "paragraph": "p04",
        "tts": "每个阶段，考的判断都不一样。",
        "subtitle": "每个阶段，判断都不一样。",
    },
    {
        "id": "c15",
        "paragraph": "p04",
        "tts": "第一关，是你到底该不该做。",
        "subtitle": "第一关：到底该不该做。",
    },
    {
        "id": "c16",
        "paragraph": "p04",
        "tts": "后面才轮到边界、系统和护城河。",
        "subtitle": "后面才轮到边界、系统和护城河。",
    },
    {
        "id": "c17",
        "paragraph": "p05",
        "tts": "所以，用 A I 创业之前，先别急着问怎么更快。",
        "subtitle": "用 AI 创业，先别急着问怎么更快。",
    },
    {
        "id": "c18",
        "paragraph": "p05",
        "tts": "先问一句：现在缺的是速度，还是判断？",
        "subtitle": "现在缺的是速度，还是判断？",
    },
    {
        "id": "c19",
        "paragraph": "p05",
        "tts": "下一集，我们先看第一关：有了 Demo，为什么还不代表有人要。",
        "subtitle": "下一集：有 Demo，为什么还不代表有人要。",
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
        "Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`",
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
        rows.append(
            {
                **chunk,
                "duration": duration,
                "path": output,
                "endpoint": endpoint,
            }
        )
        print(f"{chunk['id']}\t{duration:.3f}s\t{output}", flush=True)
    write_report(rows)
    print(REPORT)


if __name__ == "__main__":
    main()
