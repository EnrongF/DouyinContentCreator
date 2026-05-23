import json
import shutil
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HTML_ROOT = Path(__file__).resolve().parent
FRAMES = ROOT / "frames"
FRAME_MANIFEST = ROOT / "frame_durations.json"
AUDIO_MANIFEST = ROOT / "beat_audio_manifest.json"

PHASES_PER_BEAT = 8
PHASE_DURATION_WEIGHTS = (0.10, 0.10, 0.11, 0.12, 0.12, 0.13, 0.14, 0.18)


def write_beats_data(beats):
    payload = {
        "generated_from": str(AUDIO_MANIFEST.name),
        "beats": [
            {
                "beat": int(item["beat"]),
                "scene": int(item["scene"]),
                "caption": item["caption"],
                "voice": item["voice"],
                "audio_duration": float(item["audio_duration"]),
            }
            for item in beats
        ],
    }
    (HTML_ROOT / "beats-data.js").write_text(
        "window.BEATS = " + json.dumps(payload["beats"], ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )


def write_frame_manifest(entries):
    FRAME_MANIFEST.write_text(
        json.dumps(
            {
                "phase_count": PHASES_PER_BEAT,
                "timing_source": "beat_audio_manifest",
                "renderer": "html-native-playwright",
                "frames": entries,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def write_storyboard(key_paths, beats):
    cards = []
    for path, beat in zip(key_paths, beats):
        rel = path.relative_to(ROOT)
        cards.append(
            f'<figure><img src="{rel}" alt="beat {beat["beat"]:02d}"><figcaption>{beat["beat"]:02d} · {beat["caption"]}</figcaption></figure>'
        )
    doc = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>HTML Native Storyboard · OpenAI Codex Harness Engineering</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #080909;
      --ink: #f5f0e6;
      --muted: #a39d8f;
      --accent: #7ad4df;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: radial-gradient(circle at 18% 8%, rgba(122,212,223,.16), transparent 30%), var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Hiragino Sans GB", sans-serif;
    }}
    header {{ max-width: 1320px; margin: 0 auto; padding: 56px 28px 28px; }}
    .eyebrow {{ color: var(--accent); font-size: 13px; letter-spacing: .18em; text-transform: uppercase; font-family: ui-monospace, monospace; }}
    h1 {{ margin: 14px 0 12px; font-family: Georgia, "Songti SC", serif; font-size: clamp(34px, 5vw, 72px); line-height: .96; font-weight: 500; }}
    p {{ color: var(--muted); max-width: 880px; font-size: 18px; line-height: 1.6; }}
    main {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 22px; max-width: 1320px; margin: 0 auto; padding: 20px 28px 72px; }}
    figure {{ margin: 0; padding: 12px; background: linear-gradient(180deg, rgba(255,255,255,.055), rgba(255,255,255,.018)); border: 1px solid rgba(255,255,255,.08); border-radius: 22px; }}
    img {{ width: 100%; display: block; border-radius: 15px; }}
    figcaption {{ padding: 10px 4px 2px; color: var(--muted); font-size: 13px; }}
  </style>
</head>
<body>
  <header>
    <div class="eyebrow">html-native 16:9 · browser rendered frames</div>
    <h1>OpenAI Codex Harness Engineering</h1>
    <p>Storyboard generated from browser screenshots. Voice and beat timing are preserved from the existing OpenAI TTS manifest.</p>
  </header>
  <main>{''.join(cards)}</main>
</body>
</html>
"""
    (ROOT / "storyboard.html").write_text(doc, encoding="utf-8")


def main():
    manifest = json.loads(AUDIO_MANIFEST.read_text(encoding="utf-8"))
    beats = manifest["beats"]
    if len(beats) != 59:
        raise SystemExit(f"Expected 59 beats, got {len(beats)}")
    write_beats_data(beats)

    for old_frame in FRAMES.glob("scene_*.png"):
        old_frame.unlink()
    FRAMES.mkdir(exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        raise SystemExit(f"Playwright Python package is required: {exc}") from exc

    frame_entries = []
    key_paths = []
    url = (HTML_ROOT / "index.html").resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        for beat in beats:
            beat_no = int(beat["beat"])
            beat_duration = float(beat["audio_duration"])
            for phase_idx in range(PHASES_PER_BEAT):
                target = f"{url}?beat={beat_no}&phase={phase_idx}&export=1"
                page.goto(target, wait_until="networkidle")
                page.evaluate("document.fonts && document.fonts.ready")
                path = FRAMES / f"scene_{beat_no:02d}_{phase_idx:02d}.png"
                page.screenshot(path=str(path), full_page=False)
                frame_entries.append(
                    {
                        "file": str(path.relative_to(ROOT)),
                        "beat": beat_no,
                        "phase": phase_idx + 1,
                        "caption": beat["caption"],
                        "voice": beat["voice"],
                        "duration_hint": beat_duration * PHASE_DURATION_WEIGHTS[phase_idx],
                    }
                )
                if phase_idx == PHASES_PER_BEAT - 1:
                    key_paths.append(path)
        browser.close()

    Image.open(key_paths[0]).save(ROOT / "cover.png", quality=94)
    preview_frames = [Image.open(path).resize((640, 360), Image.Resampling.LANCZOS) for path in key_paths]
    preview_frames[0].save(
        ROOT / "storyboard.gif",
        save_all=True,
        append_images=preview_frames[1:],
        duration=900,
        loop=0,
    )
    write_frame_manifest(frame_entries)
    write_storyboard(key_paths, beats)

    # Rebuild contact sheet for visual QA.
    sample_beats = [1, 2, 4, 5, 6, 7, 9, 10, 12, 13, 14, 20, 24, 30, 38, 42, 49, 54, 59]
    thumbs = []
    for beat in sample_beats:
        thumb = Image.open(FRAMES / f"scene_{beat:02d}_07.png").resize((384, 216), Image.Resampling.LANCZOS)
        thumbs.append(thumb.convert("RGB"))
    cols = 4
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 384, rows * 216), (8, 9, 9))
    for idx, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((idx % cols) * 384, (idx // cols) * 216))
    sheet.save(ROOT / "native-wide-contact-sheet.jpg", quality=92)

    print(f"wrote {len(frame_entries)} html-native frames from {len(beats)} beats")


if __name__ == "__main__":
    main()
