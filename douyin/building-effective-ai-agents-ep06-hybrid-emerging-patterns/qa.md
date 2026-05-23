# QA

## Scope

- Rebuild request: completed. EP06 video was rebuilt from the new production spine.
- Preserved input layer: source bundle, source map, synthesis brief, series intent, and original PDF diagram assets.
- Rebuilt production layer: compression, script, speech chunks, pronunciation notes, voice manifest, Qwen TTS audio, ASR, scene graph, video render, vertical cover, caption, QA, and manifest.

## Source Fidelity

- Episode scope: pass. Hybrid architecture is presented as evidence-driven composition, not the default starting architecture.
- Source logic: pass. The episode preserves the distinction between:
  - single-agent systems;
  - multi-agent coordination concepts;
  - agentic workflow structures.
- Taxonomy guardrail: pass. `hierarchical` is not shown as a peer of `parallel` or `evaluator`.
- Caveat retention: pass. The 10-15x token-cost boundary is present.
- Emerging-pattern caveat: pass. `dynamic agent generation` and `peer-to-peer network` are framed as emerging patterns, not production defaults.

## Voice

- TTS provider: Qwen DashScope.
- TTS model: `qwen3-tts-instruct-flash`.
- Voice: `Ethan`.
- Speech chunks: 19.
- Total voice duration: `87.870s`.
- Longest chunk: under 8 seconds after padding.
- ASR status: pass.
- ASR review chunks: none.

## Render

- Video render: pass.
- Output: `video.mp4`.
- Rendered frames: 2635 at 30 fps.
- Duration by render frames: approximately `87.83s`.
- Cover render: pass.
- Cover output: `cover.vertical.png`.
- Cover dimensions: `1080x1920`.
- Grid cover render: pass.
- Grid cover output: `cover.grid.png`.
- Grid cover dimensions: `1080x1440`.
- Confirmed cover brand style: Mesh-inspired warm cognition cover with
  Chinese-first rounded / humanist sans typography.
- Visual asset audit: pass via `npm run audit:visual-assets`.
- TypeScript check: pass via `npx tsc --noEmit`.

## Residual Risks

- `ffprobe` is not installed in this environment, so video duration was verified from Remotion frame count and the voice manifest rather than container metadata.
- This render uses the existing Remotion EP06 component grammar. It is rebuilt and source-aligned, but not a wholly new visual engine.
