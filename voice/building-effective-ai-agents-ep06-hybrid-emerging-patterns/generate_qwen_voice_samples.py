import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOICE_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = VOICE_ROOT / "voice-tests" / "qwen"
DEFAULT_ENV = Path("/Users/fuenrong/Documents/Learn/.env")

MODEL = "qwen3-tts-instruct-flash"
VOICES = ["Ethan", "Kai", "Neil", "Elias"]
ENDPOINTS = [
    "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
    "https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
]

TEXT = """一上来就问：要不要混合架构？

这个问题，其实有点早。

混合架构不是起点。
它更像系统跑起来之后，慢慢长出来的形态。"""

INSTRUCTION = (
    "自然口语化的标准普通话。像冷静的技术播客主持人，略带挑战感，"
    "不要播音腔，不要新闻腔。第一句直接，问句后停顿；"
    "“有点早”放慢并带判断感。后两句转为稳定解释。"
)


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
    result = subprocess.run(
        ["afinfo", str(path)],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    match = re.search(r"estimated duration:\s*([0-9.]+)\s*sec", result.stdout)
    if not match:
        return 0.0
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
        path.write_bytes(response.read())


def synthesize_voice(api_key: str, voice: str) -> tuple[Path, str]:
    payload = {
        "model": MODEL,
        "input": {
            "text": TEXT,
            "voice": voice,
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
            output = OUTPUT_DIR / f"ep06-opening-qwen-{voice}.wav"
            download(audio_url, output)
            return output, endpoint
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            last_error = exc
            time.sleep(0.2)
    raise RuntimeError(f"{voice} failed: {last_error}")


def main() -> None:
    load_env_file(DEFAULT_ENV)
    api_key = os.environ.get("DASHSCOPE_API_KEY") or os.environ.get("QWEN_API_KEY")
    if not api_key:
        raise SystemExit("QWEN_API_KEY or DASHSCOPE_API_KEY is missing.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for voice in VOICES:
        output, endpoint = synthesize_voice(api_key, voice)
        print(f"{voice}\t{audio_duration(output):.3f}s\t{output}\t{endpoint}")


if __name__ == "__main__":
    main()
