---
name: codex-knowledge-extraction
purpose: AI cognition compression for frontier AI systems
status: active
---

# Project Charter

This repository turns frontier AI systems knowledge into source-faithful mental
models and publishable artifacts. The target audience is serious builders,
technical operators, founders, enterprise AI leaders, consultants, and systems
thinkers.

Douyin is a distribution surface. The product is AI cognition compression.

## Objectives

- Compress dense AI research, engineering practice, and operator knowledge into
  high-trust mental models.
- Preserve source truth while making the structure easier to understand.
- Convert qualified knowledge into scripts, voice, visuals, Remotion videos,
  covers, captions, and final distribution packages.
- Build a maintained knowledge library where newer frontier sources update or
  supersede older claims instead of creating duplicate truths.

## Concept Model

Use these stable concepts across the project:

```text
source value
-> topic
-> series
-> episode
-> section
-> voice paragraph
-> speech chunk
-> visual focus moment
-> scene graph beat
-> rendered frame
-> distribution package
```

Meaning:
- Source value: original claims, terms, diagrams, metrics, examples, caveats,
  workflows, and practical implications.
- Topic: the larger knowledge area.
- Series: a planned split when the topic has more than one mental upgrade.
- Episode: one standalone mental upgrade.
- Section: one part of the episode argument.
- Voice paragraph: one idea, one speaking intention, one pacing direction, one
  primary visual focus.
- Speech chunk: a performable spoken unit for TTS, timing, and ASR QA.
- Visual focus moment: the visible highlight that matches the spoken focus.
- Scene graph beat: structured render data for one timed visual/narration beat.
- Distribution package: final Douyin-ready files and QA records.

## Principles

- Fidelity: preserve source-defined taxonomy, category boundaries, causal logic,
  diagrams, tables, metrics, caveats, and source terminology when they matter.
- Compression: reduce cognitive load without flattening truth. Split before
  over-compressing.
- Value budgeting: declare retained value, moved value, omitted value, and
  non-cuttable source material.
- Modality alignment: research, script, voice, visuals, motion, subtitles, cover,
  and caption must express the same episode logic.
- Determinism: publishable videos render from scene graphs and measured voice
  manifests, not hidden hand timing.
- Native expression: Chinese narration, subtitles, labels, captions, and covers
  must sound natural, not translation-shaped.
- Operational clarity: directory ownership and artifact contracts matter more
  than chat history.

## Source Standard

Default to at most three sources unless the task needs broader coverage.

Preferred sources:
- Primary or first-party engineering posts.
- Official docs, specs, standards, release notes, and datasets.
- Research papers, conference talks, direct transcripts, and source diagrams.
- Credible expert analysis when clearly labeled as secondary.

For AI agents, Claude, tool use, evaluation, context engineering, or multi-agent
systems, check Anthropic primary sources first when relevant.

Avoid SEO summaries, content farms, reposts without evidence, outdated tutorials,
and unclear provenance.

## Platform Rules

Douyin artifacts must be:
- Attractive: strong opening contrast and clear visual rhythm.
- Compressed: one mental upgrade per artifact.
- Understandable: concrete examples, diagrams, short claims, and plain language.
- Accurate: no viral simplification that breaks source truth.
- Actionable: end with a decision frame, checklist, operating principle, or next
  step.
- High-trust: institutional intelligence, not generic AI-tool content.

Publishable video package requirements:
- `video.mp4` with burned-in subtitles.
- `cover.png` and `cover.md`.
- `caption.md`.
- `manifest.md`.
- `qa.md`.
- `platform.md` after publish when performance data is available.
- Voice manifest and source references preserved upstream.

## Roles

Roles describe responsibilities. Use only the roles needed for the task.

| Role | Owns |
|---|---|
| Lead | Scope, sequencing, file ownership, conflict resolution, final integration. |
| Knowledge | Source scouting, qualification, extraction, synthesis, AI engineering analysis, series decision, value budget, compression. |
| Voice | Script, paragraph plan, speech chunks, natural Chinese, TTS, ASR, voice manifest. |
| Visual Production | Visual system, previews, HTML prototypes, optional brand/source visual extraction for style setting, diagrams, scene graph mapping, Remotion rendering, timing sync, subtitles, covers, contact sheets. |
| Quality | Fidelity, taxonomy, over-compression, expression, visual quality, voice-frame sync, package verification, manifests, final index. |
| Douyin Platform | Publishing plan, title/caption/tag experiments, performance metrics, follower conversion, engagement analysis, iteration feedback. |

## Capabilities

Capabilities are task modes used inside roles. They are not separate owners and
should not compete with the canonical role model.

- Knowledge capabilities: source search, qualification, recency checks, extraction, synthesis, mental model, value budget, episode scope.
- Voice capabilities: spoken Mandarin, speech chunks, pronunciation, duration, ASR.
- Visual Production capabilities: visual system, diagrams, focus states, HTML previews, Remotion video, subtitles, covers, stills, contact sheets. Optional style-setting capability: brand/source visual extraction.
- Quality capabilities: source fidelity, taxonomy, expression, voice-frame sync, platform clarity, manifest, QA package, final index.
- Douyin Platform capabilities: publish timing, metadata experiments, views, followers, engagement, retention, iteration notes.

## Directory Map

```text
sources/        source bundles and provenance
extraction/     source maps and source value inventory
synthesis/      briefs and candidate mental upgrades
series/         series and episode maps
compression/    selected episode mental model and value budget
voice/          scripts, speech chunks, audio, ASR, voice manifests
scene-graphs/   render source of truth
remotion/       React/Remotion renderer
presentation/   HTML previews, decks, and memo artifacts
douyin/         publishable distribution packages
review/         review and verification findings
final/          shipped artifact index
prompts/        role prompts and reusable agent instructions
resources/      source assets and supporting materials
```

## Deliverable Contracts

Common file patterns:

```text
sources/<slug>.sources.md
extraction/<slug>.source-map.md
synthesis/<slug>.brief.md
series/<slug>.series.md
compression/<slug>.md
scene-graphs/<slug>.json
voice/<slug>/script.md
voice/<slug>/paragraph-plan.md
voice/<slug>/speech-chunk-plan.md
voice/<slug>/voice-manifest.json
douyin/<slug>/video.mp4
douyin/<slug>/cover.png
douyin/<slug>/cover.md
douyin/<slug>/caption.md
douyin/<slug>/manifest.md
douyin/<slug>/qa.md
douyin/<slug>/platform.md
review/<slug>.findings.md
review/<slug>.source-visual-inventory.md  # optional when visual style needs source/brand extraction
```

## Working Rules

- Read the relevant directory `README.md` before changing files there.
- One owner per file set.
- Worker and reviewer do not edit the same artifact in the same pass.
- Extraction starts only after sources are qualified.
- Run the Source Logic / Taxonomy Gate before compression, scripting, cover, or
  render decisions.
- For visual-production work, optionally run Brand / Source Visual Extraction
  before visual template selection when the source has meaningful visual
  identity, diagrams, product UI, screenshots, logos, or endorsement risk.
- Run the Series / Episode Scope Gate before scripting.
- Run the Native Chinese Expression Gate before TTS, subtitles, cover final, or
  render.
- Run Voice Naturalness and ASR QA before locking the voice manifest.
- Use measured voice durations for final Remotion timing.
- Final output ships only after fidelity, clarity, subtitle, cover, packaging,
  and verification checks pass.
