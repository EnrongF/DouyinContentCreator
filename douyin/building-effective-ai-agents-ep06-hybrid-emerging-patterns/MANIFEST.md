# Manifest

## Package

- Slug: `building-effective-ai-agents-ep06-hybrid-emerging-patterns`
- Series: `Building Effective AI Agents`
- Episode: `EP06 什么时候用混合架构?`
- Rebuild date: 2026-05-20
- Rebuild mode: production layer rebuilt from the preserved source-information layer.

## Primary Artifacts

- `../../handoff/building-effective-ai-agents-ep06-hybrid-emerging-patterns.production-state.md`
- `../../compression/building-effective-ai-agents-ep06-hybrid-emerging-patterns.md`
- `../../scene-graphs/building-effective-ai-agents-ep06-hybrid-emerging-patterns.json`
- `../../voice/building-effective-ai-agents-ep06-hybrid-emerging-patterns/script.md`
- `../../voice/building-effective-ai-agents-ep06-hybrid-emerging-patterns/speech-chunk-plan.md`
- `../../voice/building-effective-ai-agents-ep06-hybrid-emerging-patterns/voice-manifest.json`
- `../../voice/building-effective-ai-agents-ep06-hybrid-emerging-patterns/asr.txt`
- `video.mp4`
- `cover.vertical.png`
- `cover.grid.png`
- `caption.md`
- `cover.md`
- `qa.md`

## Render Commands

```bash
cd remotion
npm run render:building-effective-ai-agents-ep06-hybrid-emerging-patterns
npm run still:building-effective-ai-agents-ep06-hybrid-emerging-patterns-vertical-cover
npm run still:building-effective-ai-agents-ep06-hybrid-emerging-patterns-grid-cover
```

## Voice Commands

```bash
python3 voice/building-effective-ai-agents-ep06-hybrid-emerging-patterns/generate_qwen_tts.py
python3 voice/building-effective-ai-agents-ep06-hybrid-emerging-patterns/validate_openai_asr.py
```

## Status

- Script: rebuilt from source facts.
- Scene graph: rebuilt in the Remotion production schema.
- Original diagrams: retained as source-proof inserts.
- TTS: regenerated for `c01` through `c19`.
- ASR QA: pass.
- Voice duration: `87.870s`.
- Video: rendered to `video.mp4`.
- Video size: approximately `27 MB`.
- Vertical cover: rendered to `cover.vertical.png`.
- Douyin profile-grid cover: rendered to `cover.grid.png` at `1080x1440`.
- Cover size: approximately `1.5 MB`.

## Checksums

- Scene graph: `e64f28753302415fc978b384fb834cc0995469873d828597a6f651da737cd170`
- Voice manifest: `54113c4b90d0087cfdc5bcb78b61becb17bb20d31ac29e8ae200e6b4191d4564`
- Video: `f63de3c9ad061a2bb8795cb637e6f9de18f1ca93c88302dc496856cc912e6d17`
- Vertical cover: `341f843616d3884fb2dc40e9cfb95061bf2df774bddd369e3cf6ad883bf2f2ed`
