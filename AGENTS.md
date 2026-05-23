# Codex Agent Guide

This is the entry point for agents working in this repository. Keep it short.
Load deeper contracts only when the task needs them.

## Read First

1. `PROJECT_CHARTER.md` - product charter, principles, concept model, roles, and directory map.
2. `PRODUCTION_PIPELINE.md` - production workflow, gates, artifacts, and render contracts.
3. `VOICE_SYSTEM.md` - voice, Chinese expression, TTS, ASR, subtitle, and timing rules.
4. `VISUAL_SYSTEM.md` - visual, HTML preview, Remotion, and cover rules.
5. `visual-templates/templates.json` - style candidate pool for visual exploration.
6. The `README.md` for any directory you edit.

## Objective

Produce AI cognition compression: source-faithful mental models, scripts,
visuals, voice, videos, covers, captions, and distribution packages for frontier
AI systems knowledge.

The work is not generic AI content. It must preserve source truth, compress
complexity, and create high-trust artifacts for builders, operators, and
decision-makers.

## Operating Principles

- Source fidelity first: do not invent claims, taxonomies, diagrams, metrics, or
  caveats.
- Compression is a value budget, not just shorter wording.
- One artifact teaches one mental upgrade. Split into a series before
  over-compressing.
- Shared state lives in files, not chat.
- Scene graphs and voice manifests are the production source of truth for video.
- Visuals and motion must explain the idea, not decorate it.
- Publishable Douyin videos require burned-in subtitles, source-faithful visuals,
  cover, caption, manifest, and QA notes.

## Default Workflow

Use the full workflow for new publishable video work. For narrower tasks, run
only the relevant slice.

```text
Research
-> Source Value Inventory
-> Source Logic / Taxonomy Gate
-> Series / Episode Scope Gate
-> Episode Strategy
-> Value Budget
-> Compression
-> Voice Design
-> Native Chinese / Voice Naturalness Gates
-> Scene Graph
-> Voice Production
-> Motion / Focus Sync
-> Remotion Rendering
-> QA
-> Douyin Distribution
```

## Platform Rules

- Prefer primary, recent, professional sources; use at most three sources by
  default.
- For AI-agent topics, check Anthropic primary sources first when relevant.
- Do not ship one video with multiple unrelated mental upgrades.
- Do not rely on `.srt` for Douyin; subtitles must be burned into the MP4.
- Covers must be readable in a phone feed and must not imply source publisher
  endorsement.
- New or revised video work uses scene graphs plus Remotion, not ad-hoc render
  scripts.
- Visual redesigns require preview approval before touching scene graphs,
  Remotion components, covers, or final videos unless the user explicitly says to
  implement directly.

## Directory Routing

- `sources/`: source bundles, links, provenance, and source notes.
- `extraction/`: source maps, claims, artifacts, source value inventory.
- `synthesis/`: durable briefs and candidate mental upgrades.
- `series/`: episode maps when a topic has multiple mental upgrades.
- `compression/`: selected episode value budget and mental model.
- `voice/`: script, paragraph plan, speech chunks, TTS, ASR, voice manifest, QA.
- `scene-graphs/`: render source of truth for scenes, claims, subtitles, focus,
  artifacts, source refs, and timing intent.
- `remotion/`: React/Remotion implementation for videos, covers, stills, and
  contact sheets.
- `presentation/`: HTML previews, decks, and memo-style artifacts.
- `douyin/`: publishable package: video, cover, caption, manifest, QA.
- `review/`: fidelity, clarity, taxonomy, expression, and verification findings.
- `final/`: shipped artifact index.

## Role Model

Use roles as responsibilities, not bureaucracy. One agent may hold several roles
on a small task.

- Lead: scope, sequencing, file ownership, conflict resolution, integration.
- Knowledge: source search, qualification, extraction, synthesis, AI engineering analysis, series decision, value budget, compression.
- Voice: script, Chinese expression, speech chunks, TTS, ASR, timing manifest.
- Visual Production: visual system, previews, HTML prototypes, optional brand/source visual extraction for style setting, source artifact treatment, scene graph mapping, Remotion rendering, subtitles, cover.
- Quality: source fidelity, taxonomy, clarity, expression, voice-frame sync, visual QA, release verification.
- Douyin Platform: publishing plan, metadata experiments, performance metrics, follower conversion, engagement feedback.

## Edit Discipline

- Keep edits scoped to the requested artifact or pipeline layer.
- Do not rewrite historical packages just to match the current stack.
- If revising an old video topic, migrate by creating a scene graph and Remotion
  composition instead of patching old frame scripts.
- Update `qa.md`, `manifest.md`, or review notes whenever a publishable artifact
  changes.
