# Manifest

## Package

- Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`
- Series: `The Founder's Playbook - Building an AI-Native Startup`
- Episode: `EP01 AI 创业，真正卡的是判断`
- Package date: 2026-05-21
- Package mode: scene graph + Remotion render + Qwen voiceover.

## Primary Artifacts

- `../../compression/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.md`
- `../../scene-graphs/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.json`
- `../../voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/script.md`
- `../../voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/speech-chunk-plan.md`
- `../../voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/voice-manifest.json`
- `../../voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/asr-qa.md`
- `../../review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.final-render-qa.md`
- `video.mp4`
- `cover.png`
- `cover.vertical.png`
- `cover.grid.png`
- `caption.md`
- `cover.md`
- `brief.md`
- `script.md`
- `qa.md`

## Render Commands

```bash
cd remotion
npm run render:the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck
npm run still:the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck-vertical-cover
npm run still:the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck-grid-cover
```

## Voice Commands

```bash
python3 voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/generate_qwen_tts.py
python3 voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/validate_openai_asr.py
```

## Status

- Script: locked.
- Scene graph: locked and rendered through Remotion.
- Visual system: A2 Balanced VI + Content Fit.
- TTS: Qwen / Ethan, chunks `c01` through `c19`.
- ASR QA: pass.
- Voice duration: `61.440s` measured speech.
- Total video duration: `67.35s`.
- Video: rendered to `video.mp4`.
- Video size: approximately `12 MB`.
- Vertical cover: rendered to `cover.vertical.png`.
- Douyin profile-grid cover: rendered to `cover.grid.png` and copied to `cover.png`.
- Cover size: approximately `1.2 MB` for grid, `2.5 MB` for vertical.

## Checksums

- Scene graph: `f41b533c6911294cc567675b731e367574f5712d8fb5cc2ddac727c8075a243f`
- Voice manifest: `830e01ccb3f29639b1c2d3417e2a2215b1ddebaee7c3728a644fa5870349613e`
- Video: `b1b59f832ed6553a86dd20a26b2284950d9fb636207c902d6d251fab501b980a`
- Vertical cover: `822df4a58a7784e7410a5a7d565390e29cc88d79ab4ce94dfb98637485037186`
- Grid cover: `33b38eb71265820d0f91212cbe3700ed278e7e2495490fdba292836a1681addc`
- Cover alias: `33b38eb71265820d0f91212cbe3700ed278e7e2495490fdba292836a1681addc`
