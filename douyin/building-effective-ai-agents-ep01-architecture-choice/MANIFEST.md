# Manifest

## Package

- Slug: `building-effective-ai-agents-ep01-architecture-choice`
- Series: `Building Effective AI Agents`
- Episode: `EP01 Agent架构怎么选?`
- Source: Anthropic PDF provided by user.

## Primary Artifacts

- `../../scene-graphs/building-effective-ai-agents-ep01-architecture-choice.json`
- `../../compression/building-effective-ai-agents-ep01-architecture-choice.md`
- `../../voice/building-effective-ai-agents-ep01-architecture-choice/script.md`
- `../../voice/building-effective-ai-agents-ep01-architecture-choice/paragraph-plan.md`
- `../../voice/building-effective-ai-agents-ep01-architecture-choice/voice-manifest.json`
- `../../voice/building-effective-ai-agents-ep01-architecture-choice/asr.txt`
- `../../resources/building-effective-ai-agents/diagrams/`
- `video.mp4`
- `cover.preview.png`
- `cover.source-logic.png`
- `cover.vertical.png`
- `contact-sheet.jpg`

## Render Commands

```bash
cd remotion
npm run still:building-effective-ai-agents-ep01-cover
npm run still:building-effective-ai-agents-ep01-source-cover
npm run still:building-effective-ai-agents-ep01-vertical-cover
npm run render:building-effective-ai-agents-ep01
```

Note: the EP01 Remotion composition renders at `1.2x` playback rate. Scene graph durations remain measured at original voice length; the render layer shortens visual ranges and speeds audio together.

## Status

- Script: final for Episode 1.
- Scene graph: final with measured voice durations.
- Original diagrams: preserved and wired into Remotion public assets.
- Cover preview: rendered.
- Alternative source-logic cover: rendered.
- Douyin vertical cover: rendered to `cover.vertical.png`.
- TTS: generated with `gpt-4o-mini-tts`, voice `marin`.
- ASR QA: pass after regenerating the conclusion line.
- Final video: rendered to `video.mp4` at `1.2x` playback speed.
- Contact sheet: rendered.

## Checksums

```text
dd74f65871dd372a5614b1b93d70995d5201f58a88ccb03dbe6b8af7115b3ee8  video.mp4
ff495c469b4dc3bf5790e0970cd847b9b151db11fb86efc77b7fbc8856cb331b  contact-sheet.jpg
1953d18b1a4db2b1511d562ad8086b77e360f4e50a0f8e749489a41f6389150e  cover.source-logic.png
9727419e619355ba11d31940a482d7c72fec1052d7523df6d79f655b211c4497  cover.vertical.png
f6530bd2c20a9fcda73fbc83fa8f1959beb0169b96d9fa8a5e21a592e9cb6fcb  voice-manifest.json
6fe492f9c6670625b7ba9dd1b36f1666d5713c7ad3d8088879a4c5a0f83113ee  scene graph
```
