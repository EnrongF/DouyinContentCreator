# Manifest

## Package

- Job: OpenAI Codex Harness Engineering
- Source: https://openai.com/index/harness-engineering/
- Output folder: `douyin/openai-codex-harness-engineering/`
- Distribution target: horizontal wide technical documentary

## Primary Artifacts

- `video.mp4`: final narrated horizontal wide video.
- `video.silent.mp4`: silent render from frames.
- `voiceover.final.mp3`: final OpenAI TTS Mandarin voiceover.
- `storyboard.html`: review storyboard.
- `storyboard.gif`: animated storyboard preview.
- `native-wide-contact-sheet.jpg`: sampled key-frame QA sheet.
- `cover.png`: cover frame.
- `frames/scene_*.png`: source frames.
- `frame_durations.json`: per-frame timing manifest used for voice-frame sync.
- `beat_audio_manifest.json`: per-beat spoken text, audio chunk path, and measured audio duration.
- `scene_audio_manifest.json`: phrase-level TTS chunks and the source for weighted beat timing.
- `timing-map.md`: voice-frame sync and dynamic focus beat map.
- `html-renderer/`: browser-native visual renderer and Playwright frame exporter.
- `narration.txt`: final spoken script.
- `caption.md`: caption draft.
- `qa.md`: quality-gate notes.

## Render Commands

```bash
python3 douyin/openai-codex-harness-engineering/render_assets.py
python3 douyin/openai-codex-harness-engineering/html-renderer/render_frames.py
python3 douyin/openai-codex-harness-engineering/generate_openai_tts.py
python3 douyin/openai-codex-harness-engineering/render_video.py
python3 douyin/openai-codex-harness-engineering/validate_voiceover.py
```

## Final Metadata

- Resolution: 1920 x 1080
- Frame rate: 30 fps
- Duration: 00:03:42.30
- Beat frames: 59
- Phased frames: 472
- Video codec: H.264 High, yuv420p
- Audio: AAC mono, 24 kHz
- Voiceover duration: 00:03:42.22
- Frame renderer: html-native-playwright

## Checksums

```text
255feb5890fb95c78477f4d3a3e0dbbba845a31fd09e637a6319bc76d6384b57  video.mp4
2ad9928c426e9c95080e7bd177198ea8401bc17e59cb114915c87f13908bdf5a  video.silent.mp4
182898a95fe10a313ac1d064b1920a7207728e62ef522c6b71c2529d75b8d1f3  voiceover.final.mp3
69da04e2d55729e93f7ad1dd80e8913671f200e6e6ca171c65dc23636608bae5  storyboard.html
bfc243fc93323f9f481e200f19f711dea10c79ca20234d420502aae56be0b30d  storyboard.gif
3ff25035f7b1179753f5af3815fe653c35d66ef359777796fbbe627ff51e0f86  cover.png
b7c4d6ef3c24dbcc77d1be4917fd53d2b06953969b019c3ad9f5e0ed3a60c045  frame_durations.json
814e54fb8351d6f9cdc6437ae4ea6354cf56ffb5f70fa92696ea8880aca59109  beat_audio_manifest.json
0f73f182caa53e2641b2b7ef13d5f302645ccb5aec461ace7ca6ee678f2ad46f  scene_audio_manifest.json
4027e7d87c8097387d220eadc2ccdace7eccb09b13fe66530894205919f4bbad  native-wide-contact-sheet.jpg
b90ccfb8e674343481ddf1110a1979f1a2373ad60353055b44f68a8a3c6897d7  html-renderer/index.html
62f2af0ba839caa44b2d80f36207c500e6e3c04859d74fd33f7efd2bba0ec289  html-renderer/styles.css
225cf01517ac4ad905ecc7896ba4e5cc114eaa88e7e9926742bc5fb79707521c  html-renderer/scene-data.js
18b9ccbc59a24bc70ae6be638762bf32421d8d12c96439ad14b5d8cd2a0848c5  html-renderer/timeline.js
14455d7495ffa52d2615da34de21e88b463f353ee69de1fb972247107b0ada8c  html-renderer/render_frames.py
e5228141deb89735b660665ba74dc9576591f7b52b20bfe723c4dc178fd464d1  render_assets.py
7dd46e3ec44158598741eab6ad3171c29b0139e6a2384b7635a3af79e3235558  generate_openai_tts.py
8e7634beb7f60803b7ed0dfef2e96260cf12bf651c694fcb7c8b08e7d61f62ff  validate_voiceover.py
```

## Production Notes

- `__pycache__/` is generated locally and should not be included in any external handoff package.
- `render_video.py` uses `imageio_ffmpeg` when available and falls back to system `ffmpeg`.
- The spoken narration is simplified Mandarin-first text, generated as 24 phrase-level TTS chunks using OpenAI TTS voice `alloy` at speed `1.2`.
- Pronunciation QA rewrites brittle spoken tokens such as `PR`, `CI`, `worktree`, lowercase `agent`, `bug`, and `docs 目录` into natural Mandarin while keeping the visual terminology intact.
- Beat timing is derived from phrase-level audio with weighted allocation, then written back to `beat_audio_manifest.json` for visual sync.
- The longest derived spoken beat is 5.39 seconds; no beat exceeds the 6-second QA ceiling.
- Bottom subtitle/focus-caption card is intentionally removed because platform subtitles can be generated from the voice track.
- Background grids and internal dev chrome were removed. The visual system now uses a native 16:9 composition: narrative compression on the left, horizontal content stage on the right.
- `render_assets.py` no longer uses portrait-to-wide transform helpers such as `wide_frame`, `transform_box`, `NARRATIVE_SRC`, or `CONTENT_SRC`.
- Publishable render now uses `html-renderer/render_frames.py`, which captures deterministic browser states like `index.html?beat=42&phase=7&export=1`.
- Publishable render uses a 59-beat / 472-phase HTML screenshot sequence with dynamic focus overlays; the old 14-frame static slide sequence should be treated as superseded.
- `render_video.py` reads `frame_durations.json`. When `timing_source=beat_audio_manifest`, it preserves per-beat durations instead of globally stretching the sequence.
- Latest design-review pass rebuilt the visual system toward cleaner executive technical documentary: no grid texture, stronger contrast, softer metadata, legible dim states, full-stage diagram coordinates, and repaired DevTools process-label layout.
