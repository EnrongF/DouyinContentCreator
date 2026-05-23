# Codex Knowledge Extraction

AI cognition compression for frontier AI systems.

This repository turns high-quality sources into source-faithful mental models,
Chinese voice scripts, structured scene graphs, Remotion videos, covers,
captions, and Douyin-ready distribution packages.

## Stable Docs

- `AGENTS.md`: Codex agent entry point.
- `PROJECT_CHARTER.md`: project charter, principles, concepts, roles, directories.
- `PRODUCTION_PIPELINE.md`: workflow, gates, scene graph, voice, Remotion contracts.
- `VOICE_SYSTEM.md`: voice design, Chinese expression, TTS, ASR, subtitles, timing.
- `VISUAL_SYSTEM.md`: visual exploration, HTML previews, motion, covers.

## Core Workflow

```text
Research
-> Source Value Inventory
-> Source Logic / Taxonomy Gate
-> Series / Episode Scope Gate
-> Value Budget
-> Compression
-> Voice Design
-> Scene Graph
-> Voice Production
-> Remotion Rendering
-> QA
-> Douyin Distribution
```

## Directory Map

- `sources/`: source bundles and provenance.
- `extraction/`: source maps and value inventory.
- `synthesis/`: briefs and candidate mental upgrades.
- `series/`: series and episode maps.
- `compression/`: mental models and value budgets.
- `voice/`: scripts, speech chunks, audio, ASR, voice manifests.
- `scene-graphs/`: render source of truth.
- `remotion/`: React/Remotion renderer.
- `presentation/`: HTML previews, decks, memo artifacts.
- `douyin/`: final distribution packages.
- `review/`: review and verification findings.
- `final/`: shipped artifact index.

## Non-Negotiables

- Do not invent claims.
- Preserve source taxonomy and important original artifacts.
- Split into a series before over-compressing.
- Use natural Chinese for voice, subtitles, labels, captions, and covers.
- Render publishable videos from scene graphs and measured voice manifests.
- Burn subtitles into final MP4 files.

## Douyin Authorization Helper

Create a local `.env` from `.env.example`, then set `DOUYIN_CLIENT_KEY`,
`DOUYIN_REDIRECT_URI`, and the requested `DOUYIN_SCOPE`.

```bash
python3 scripts/douyin_get_permission_code.py --save
```

The script opens the Douyin authorization page. After authorization, paste the
final redirect URL or raw `code`; it prints the authorization code and, with
`--save`, stores it as `DOUYIN_CODE` in `.env`.

Token and share-result helper:

```bash
python3 scripts/douyin_api.py --get-access-token --get-client-token --save
python3 scripts/douyin_api.py --create-share-id --save
```
