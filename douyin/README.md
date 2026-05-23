# Douyin Outputs

Store Douyin-ready scripts, captions, hooks, thumbnail notes, short-form content plans, and visual artifacts for the project's mission: AI cognition compression.

## Mission Fit
- Douyin is the distribution format.
- The project mission is AI cognition compression: frontier AI knowledge compressed into source-faithful, high-trust mental models.
- Outputs should feel like institutional-grade intelligence condensed for a mobile audience.

## Naming
Use descriptive source or topic slugs.

Pattern:
- `<source-or-topic-slug>/video.mp4`
- `<source-or-topic-slug>/caption.md`
- `<source-or-topic-slug>/cover.png`
- `<source-or-topic-slug>/cover.md`
- `<source-or-topic-slug>/manifest.md`
- `<source-or-topic-slug>/qa.md`
- `<source-or-topic-slug>/platform.md` after publishing or performance review

## Quality Standard
- One main idea per artifact.
- One larger topic may become a series; do not force multiple mental upgrades into one short video.
- Use the hierarchy: source value -> topic -> series -> episode -> section -> voice paragraph -> visual focus moment.
- Strong first 3 seconds.
- Plain-language explanation.
- Concrete example or visual metaphor.
- Accurate to the source.
- Memorable mental upgrade.
- Compact framework, ladder, or decision model.
- Source-faithful compression without low-trust simplification.
- Explicit value budget: every artifact should know what it keeps, moves to another episode, and omits.
- Non-cuttable source material must remain visible in script, visuals, or source fidelity notes.
- Paragraph-designed voice: each paragraph should have one idea, one emotion, one pacing direction, and one primary focus.
- Voice-frame sync: every narration beat should correspond to a visible frame, callout, or focus state; avoid long voiceover over unrelated or unchanged visuals.
- Dynamic focus: highlight the active element as it is discussed through reveal, glow, outline, pointer, zoom, color shift, or motion; static slide sequences are not production-ready by default.
- Burned-in subtitles: every publishable video must render subtitles directly into `video.mp4`, synced to the final voiceover. Do not rely on a standalone `.srt`, because Douyin does not support uploading it with the video.
- Cover: every publishable video must ship with `cover.png` plus `cover.md`. The cover should share the video's typography, palette, and visual metaphor, and remain readable on a phone feed.
- Series covers: multi-episode series must define one cover family and reuse it across episodes. Source VI, logos, and basic graphs may be referenced for attribution and visual context, but the cover must not imply official endorsement by the source publisher.
- Cover hierarchy should be thumb-first: one large viewer-value headline, one compact source/episode strapline, one dominant proof artifact, and optional proof chips. Avoid cover text that describes production method instead of audience value.
- Source-driven rendering: publishable videos should be rendered from a scene graph and voice manifest, not hand-timed frame scripts.

## Visual Standard
- Default to Executive Technical Documentary / Minimal Cinematic Systems Intelligence for frontier AI infrastructure topics.
- Use dark graphite, off-white, muted gray, and one restrained cyan/blue accent.
- Use large clean sans-serif hierarchy, architectural diagrams, UI overlays, node graphs, and restrained cinematic depth.
- Anthropic-like editorial technical style remains acceptable for research-note artifacts, but publishable Douyin videos should prefer the executive technical documentary style.
- Avoid generic AI visuals: neon gradients, purple bias, glass cards, noisy grids, excessive rounded rectangles, and decorative icons that do not explain the idea.
- The video should feel like AI cognition compression, not a template slide deck or AI-tool recommendation clip.
- Motion must be semantic: use progressive reveals, focus highlights, flow paths, and state changes to explain the system rather than decorative transitions.
- Covers should follow the same executive technical documentary system: one large claim, one architecture artifact, high contrast, no small dense text.
- Covers based on a source PDF should prefer original diagrams or source-derived basic graphs as the visual anchor, with taxonomy labels checked against the source before rendering.

## Production Stack
- Research and extraction live in `sources/`, `extraction/`, and `synthesis/`.
- Compression lives in `compression/<slug>.md`.
- Series maps live in `series/<slug>.series.md` when a topic needs multiple episodes.
- Scene sequencing lives in `scene-graphs/<slug>.json`.
- Voice timing lives in `voice/<slug>/voice-manifest.json`.
- Motion implementation lives in `remotion/`.
- Douyin packages contain only distribution artifacts and QA outputs.
- Post-publish performance notes live in `platform.md`: publish metadata,
  experiment hypothesis, views, engagement, follower conversion, diagnosis, and
  recommended iteration.

## Benchmark-Derived Content Standard
- Do not stop at one metaphor; include a compact framework or ladder.
- Prefer `not X, but Y` positioning to create contrast.
- Relate frontier terms to concepts the audience already knows before introducing the new term.
- For AI engineering topics, explain why model choice alone is insufficient and what external system makes the difference.
- Each publishable artifact should contain at least one concrete framework with 4-7 named parts.
- For emerging terms, lead with social proof and knowledge gap before definition.
- Produce two preview modes when possible: clean standalone video and Douyin-native phone preview with app-like UI/social proof.
- Use successful Douyin references as benchmark notes under `douyin/benchmarks/`.
