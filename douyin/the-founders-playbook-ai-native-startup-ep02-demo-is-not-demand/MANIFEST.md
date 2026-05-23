# Manifest

## Package

- Slug: `the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand`
- Series: `The Founder's Playbook - Building an AI-Native Startup`
- Episode: `EP02 有 Demo，不代表有人要`
- Package date: 2026-05-22
- Package mode: scene graph + content-fitted Remotion render + Qwen voiceover.

## Primary Artifacts

- `../../compression/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand.md`
- `../../scene-graphs/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand.json`
- `../../voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/script.md`
- `../../voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/speech-chunk-plan.md`
- `../../voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/voice-manifest.json`
- `../../voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/asr-qa.md`
- `../../review/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand.final-render-qa.md`
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
npx remotion render src/index.ts the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand ../douyin/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/video.mp4
npx remotion still src/index.ts the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand-vertical-cover ../douyin/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/cover.vertical.png
npx remotion still src/index.ts the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand-grid-cover ../douyin/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/cover.grid.png
```

## Voice Commands

```bash
python3 voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/generate_qwen_tts.py
python3 voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/validate_openai_asr.py
python3 voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/build_voice_manifest.py
```

## Status

- Script: locked.
- Voice manifest: locked.
- ASR QA: pass.
- Scene graph: rendered through Remotion.
- Visual rebuild: complete; EP02 uses content-fitted diagrams, abstract concept
  symbols, and animation timing for Demo/evidence logic.
- Symbol/motion rebuild: complete; the render follows the five-principle lock:
  VI compliance, concept fit, phone-size clarity, common grammar, and abstract
  style.
- Sound effect rebuild: complete; six quiet concept cues are mixed only on major
  action notifications, with no per-animation cue layer.
- Cover: rendered with content-fitted prototype / question-vector / void /
  signal structure.
- Publish/upload: skipped for now while privileges are applying.
