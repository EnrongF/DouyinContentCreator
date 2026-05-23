# Remotion

Target home for the React + Remotion rendering stack.

Expected structure:

```text
remotion/
  package.json
  src/
    Root.tsx
    compositions/
    components/
    scene-graphs/
    styles/
```

Responsibilities:
- Render `video.mp4` with burned-in subtitles.
- Render `cover.png`.
- Render contact sheets or stills for QA.
- Support native `16:9` first and optional `9:16` adaptation later.

Historical Python/Swift render scripts are not the target stack for new topics.

## Current Composition

- `building-effective-ai-agents`: 1920 x 1080 video composition driven by `../scene-graphs/building-effective-ai-agents.json`.
- `building-effective-ai-agents-cover`: matching cover still.

## Commands

Install dependencies first:

```bash
npm install
```

Render:

```bash
npm run still:building-effective-ai-agents-cover
npm run render:building-effective-ai-agents
```

The current scene graph uses draft target durations. Final render should happen only after voice chunks are generated, measured, and synced in `../voice/building-effective-ai-agents/voice-manifest.json`.
