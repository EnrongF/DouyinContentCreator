# Manifest

- Slug: `the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code`
- Episode: `EP03 先定边界，再让 AI 写`
- Package mode: scene graph + content-fitted Remotion render + Qwen voiceover.
- Publish/upload: skipped for now while privileges are applying.

## Source Artifacts

- Scene graph: `../../scene-graphs/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code.json`
- Compression: `../../compression/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code.md`
- Voice manifest: `../../voice/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code/voice-manifest.json`
- ASR QA: `../../voice/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code/asr-qa.md`
- Final render QA: `../../review/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code.final-render-qa.md`

## Package Artifacts

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
npx remotion render src/index.ts the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code ../douyin/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code/video.mp4
npx remotion still src/index.ts the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code-vertical-cover ../douyin/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code/cover.vertical.png
npx remotion still src/index.ts the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code-grid-cover ../douyin/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code/cover.grid.png
```

## Status

- Script: locked.
- Voice manifest: locked.
- ASR QA: pass.
- Scene graph: rendered through Remotion.
- Visual rebuild: complete; EP03 uses content-fitted boundary/context/code diagrams.
- Symbol rebuild: complete; each scene artifact records `keyMessage` and `symbolMeaning`.
- Symbol refinement: complete; `AI 可读取` uses written context -> read gate -> AI-readable execution path.
- Symbol/motion principles: VI compliance first, concept fit, phone-size clarity, common grammar, abstract style.
- Sound effects: complete; five quiet concept cues only on major action notifications.
- Cover: rendered.
- Publish/upload: skipped for now while privileges are applying.
