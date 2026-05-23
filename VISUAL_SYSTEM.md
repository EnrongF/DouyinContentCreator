# Visual System

This file defines visual exploration, HTML preview, Remotion, cover, and motion
rules for this repository.

## Core Rule

Use broad comparison before implementation:

```text
diagnose
-> compare broadly
-> choose deliberately
-> enforce source fidelity
-> implement deterministically
```

For visual redesigns, stop after previews and wait for user approval before
editing scene graphs, Remotion components, covers, or final videos unless the
user explicitly says to implement directly.

## Visual Principles

### Content-Fitted Design

Every page, frame, diagram, and animation must be shaped by the content it
explains. Do not force content into a preset composition, chart shape, motion
pattern, or decorative system.

- Visuals explain source logic; they do not decorate around it.
- Preserve source diagrams, labels, and taxonomy when they are evidence.
- One frame should carry one primary idea.
- Choose layout, hierarchy, diagram structure, motion type, and pacing from the
  actual concept, audience, format, and voice timing.
- Prefer concept-type symbols over direct object-expression symbols: use
  abstract marks for signal, gate, threshold, void, mismatch, boundary, and
  evidence state before using literal product/UI icons.
- Use stable layout regions so subtitles, labels, diagrams, and progress
  metadata cannot collide.
- If content feels squeezed, sparse, over-labeled, rushed, or artificially
  symmetrical, change the visual structure before finalizing.

### Diagram Fit

- Diagrams must fit the content they explain: choose structure, scale, spacing,
  label density, orientation, and grouping from the actual concept.
- Prefer content-fitted diagrams over decorative symmetry.
- Expand, simplify, split, rotate, stack, or paginate the diagram when the
  content would otherwise feel squeezed or artificially sparse.
- Diagram labels must be readable without tiny corrective explanations.
- Source diagrams may be simplified or annotated only when the source taxonomy
  remains intact and the adaptation is clear.

### Animation Fit

- Motion must be semantic: reveal, highlight, path activation, state change,
  outline, zoom, or timing emphasis.
- Animation must fit the content it explains: choose motion type, order, speed,
  hold time, and emphasis from the idea and measured voice timing.
- Prefer content-fitted animation over decorative movement.
- Slow down, simplify, reorder, hold, or remove motion when it no longer
  clarifies the idea being spoken.
- Do not let voiceover run over unchanged visuals for long stretches unless the
  hold is an intentional comprehension pause.
- Ambient background motion is allowed when it is slow, low-contrast,
  non-directional, and continuous enough to feel like scene atmosphere rather
  than a repeated concept animation. It must never become the primary motion,
  imply source logic, or compete with subtitles, labels, diagrams, or focus
  states.

### Symbol And Motion Principles

- Identify the section key message before designing any symbol. The symbol must
  encode the section's primary takeaway, not merely its topic label or a
  decorative object associated with the words.
- Comply with the locked VI: symbols and motion must feel like part of the
  current visual identity, not a separate icon pack or animation style. This is
  the first priority; outside references such as iOS icon discipline are
  secondary inputs, never a replacement for the episode or series VI.
- Fit the content and concept: choose marks, paths, thresholds, gates, and motion
  timing from the idea being explained.
- Stay easy to understand: abstract symbols still need obvious meaning at phone
  size, with short labels when needed.
- Prefer common-use visual grammar: gates, thresholds, signals, paths, nodes,
  voids, mismatch lines, and boundaries should use familiar shapes before novel
  invention.
- Keep an abstract style: avoid literal product, person, UI, mascot, or
  decorative object icons when a concept mark can explain the idea.
- Learn from iOS icon design only as discipline: strong silhouette, one concept
  per mark, familiar metaphor, optical balance, and small-size legibility. Adapt
  those lessons into the locked VI palette, geometry, stroke weight, surface
  treatment, and motion language.

### Distinctiveness And Taste

- Show, do not tell: when taste or direction is uncertain, generate visible
  options instead of asking for abstract aesthetic descriptions.
- Distinctive design is required. Avoid default template composition, repeated
  centered cards, predictable grids, and generic "AI presentation" output.
- Avoid generic AI aesthetics: neon gradients, purple bias, glass-card
  decoration, noisy grids, decorative icons, and fake dashboards.

## Visual Diagnosis

Before creating or changing visuals, identify:
- Artifact type: HTML preview, deck, Remotion video, cover, contact sheet, or
  Douyin package.
- Audience: technical leader, builder, operator, consultant, founder, or general
  Douyin viewer.
- Source constraints: diagrams, taxonomy, labels, metrics, original terms,
  non-cuttable claims.
- Visual job: system, comparison, sequence, hierarchy, failure mode, decision
  frame, or evidence display.
- Format: `16:9`, `9:16`, static HTML, or preview-only prototype.
- Risk: overflow, too many claims, generic design, wrong taxonomy, weak
  voice-sync, unreadable mobile text.
- Mode:
  - New visual artifact: diagnose content, source constraints, audience, and
    format before style selection.
  - Existing HTML enhancement: count elements, check density, preserve working
    navigation, and split slides before adding content that would overflow.
- Source-asset adaptation: inspect available diagrams/images before outlining
  visual structure.

## Brand / Source Visual Extraction

This is an optional style-setting task inside Visual Production. It is not
required for all project work.

Run it before template selection only when visual style is undecided and a
source PDF, website, screenshot, UI, logo, or report identity is visually
important.

Owner: Visual Production.

Prompt: `prompts/brand-source-extractor.md`.

Output:

```text
review/<slug>.source-visual-inventory.md
```

Use this step to extract:
- actual colors, typography clues, surfaces, shape language, diagram treatment,
  and layout grammar;
- source assets that should anchor the frame;
- attribution and endorsement constraints;
- template-fit notes for `visual-templates/templates.json`.

This step does not approve a final style and does not edit scene graphs,
Remotion components, covers, or final videos. It feeds the visual template
comparison step.

## Style Discovery

Read `visual-templates/templates.json` when choosing a new visual direction.
Read `review/<slug>.source-visual-inventory.md` first when it exists and the
current task is visual style selection or visual redesign.

Use three preview directions by default:
- `codex-native`: Executive Technical Documentary / Minimal Cinematic Systems
  Intelligence.
- `source-native`: a treatment that preserves the source publisher's artifact
  style without implying endorsement.
- `contrast`: a meaningfully different professional direction from the template
  pool.

Expand beyond three when the user asks for broader comparison or the project is
defining a reusable series system.

When the user provides images, diagrams, screenshots, or logos, evaluate them
before planning slides:
- what each asset shows;
- whether it is usable;
- what source value or concept it carries;
- dominant colors and visual identity;
- whether it should anchor a frame, support a frame, or stay as review evidence.

Design the outline around usable source assets instead of planning the deck
first and inserting images later.

Save previews under:

```text
presentation/.visual-previews/<slug>/
  style-a.html
  style-b.html
  style-c.html
  style-comparison.md
  notes.md
```

Each preview should show one representative moment:
- Title or hook state.
- One source artifact or diagram treatment.
- One motion or focus state.
- One subtitle or label treatment.
- One proof chip, progress label, or source attribution mark when relevant.

Use real text from the script or scene graph, not placeholder text.

Previews should be self-contained HTML and intentionally different in
typography, palette, layout grammar, artifact treatment, motion, and emotional
stance. A comparison set that only changes colors is not sufficient.

## Approval Checkpoint

Default behavior:
- Produce visual diagnosis, shortlist, previews, and tradeoff notes.
- Recommend one direction.
- Wait for approval before production edits.

Allowed exceptions:
- The user explicitly says to implement directly.
- The task is a narrow bug fix in an already locked visual system.
- The task only updates documentation or QA notes.

## Visual System Lock

After approval, record:

```text
Visual System:
- Style name:
- Chosen preview:
- Audience feeling:
- Typography:
- Palette:
- Layout grammar:
- Artifact treatment:
- Motion principles:
- Source fidelity guardrails:
- Frame fitting constraints:
```

For publishable videos, reflect this in the scene graph `visualSystem` field or
the relevant `douyin/<slug>/qa.md`.

## Confirmed Series Cover Brand

Status: approved on 2026-05-21.

Use this style for the `Building Effective AI Agents` Douyin episode cover
system unless a later visual lock supersedes it.

Visual System:
- Style name: Mesh-inspired warm cognition cover.
- Reference source: `https://me.sh` visual extraction plus OSFCC-style
  open-source Chinese font selection.
- Audience feeling: premium, warm, humanist, relationship-memory inspired, but
  still source-faithful and technical.
- Typography:
  - Chinese display / headline: rounded or humanist open-source Chinese sans.
  - Preferred stack: `Resource Han Rounded CN`, `GenSenRounded TW`,
    `GenSenRounded2 TW`, `GenJyuuGothic`, `Source Han Sans SC`,
    `Noto Sans CJK SC`, `Noto Sans SC`, `Sarasa UI SC`, `PingFang SC`.
  - UI metadata: `Avenir Next`, `Helvetica Neue`, `Inter`, `PingFang SC`,
    system sans.
  - Avoid serif subtitles for this cover system; they read too literary for the
    Douyin technical brand.
- Palette:
  - Base: warm black / near-black.
  - Text: cream white.
  - Accents: warm orange, amber, soft cyan, occasional pink glow.
- Layout grammar:
  - Covers must work as Douyin profile-grid tiles.
  - Primary grid cover artifact is `1080x1440` (`3:4`), saved as
    `cover.grid.png`.
  - Keep the click-driving headline, subtitle, source proof, and decision cue
    inside the `3:4` grid composition.
  - Preserve `1080x1920` `cover.vertical.png` as the full vertical artifact when
    needed, but do not judge grid readability from the vertical cover alone.
- Artifact treatment:
  - Keep source diagrams as proof inserts when they provide trust value.
  - Do not expect tiny source diagram details to carry the cover message.
  - Use labels, chips, and title hierarchy for readable meaning.
- Motion principles:
  - For animated derivatives, use soft orbit, memory-field, glow, and reveal
    motion. Avoid hard dashboard motion unless the episode itself is operational.
- Source fidelity guardrails:
  - Source diagrams are attribution/proof, not publisher endorsement.
  - Do not redraw Anthropic taxonomies into misleading new hierarchies.
  - Do not make workflow structures and coordination structures look like the
    same category.
- Frame fitting constraints:
  - Douyin grid cover: `1080x1440`.
  - Full vertical cover/video frame: `1080x1920`.
  - Avoid critical text in vertical-only bottom regions that disappear in grid.

## Source Fidelity Gate

Before Remotion implementation, verify:
- The chosen style preserves source taxonomy and evidence.
- Parent/child concepts are not made to look like peers.
- Non-cuttable source material remains visible or explicitly accounted for.
- Source diagrams are not forced into a misleading shape.
- Labels are readable without tiny corrective explanations.
- Motion clarifies the source logic.

If the style fails this gate, adapt it or choose another preview.

## Default Style Families

### Executive Technical Documentary

Default for frontier AI systems.

- Graphite or near-black background.
- Strong Chinese headline, clean sans metadata, mono labels.
- Restrained cyan/blue accent with occasional amber/red for decisions or risks.
- Architecture maps, source diagrams, workflow paths, harness shells, eval loops.
- Motion: reveal, outline, path activation, state change.

### Source Editorial Technical

Use when the source has a strong paper, report, or research identity.

- Ivory or paper-like background, ink rules, margin notes.
- Editorial headline with clean sans body.
- Annotated diagrams, figure labels, source evidence cards.
- Motion: subtle stagger, highlight, page-like transitions.

### Systems Control Room

Use for operations, evaluation, monitoring, reliability, or production readiness.

- Dark operational UI.
- Dense but legible sans and mono text.
- Green/cyan for healthy flow, amber/red for risk.
- Dashboards, queues, traces, routing diagrams, eval gates.
- Never invent fake metrics.

### Decision Matrix

Use for choices, tradeoffs, gates, and operating principles.

- Quiet dark or clean editorial background.
- Large claim with compact labels.
- One decision color and one warning color.
- Matrices, ladders, gates, tradeoff triangles.
- Do not imply a strict ranking when the source says context-dependent.

## HTML Preview Rules

- Use semantic sections and clear frame containers.
- Keep previews self-contained unless testing a reusable stylesheet.
- Use direct local image paths for assets.
- Include keyboard navigation for deck-like previews. For full HTML decks,
  support arrow keys, space/page navigation, touch/swipe when practical,
  progress state, and visible slide position.
- Include `prefers-reduced-motion` support.
- Use viewport-relative or `clamp()` sizing for typography, spacing, and
  repeated UI elements. Avoid fixed sizes that can overflow at short heights.
- Never use invalid negative CSS functions such as `-clamp(...)`, `-min(...)`,
  or `-max(...)`; use `calc(-1 * clamp(...))` or equivalent.
- Verify 16:9 previews at 1280 x 720 and 1920 x 1080.
- Verify 9:16 previews at 390 x 844 and 1080 x 1920.

Minimum CSS:

```css
html,
body {
  height: 100%;
  overflow-x: hidden;
}

.slide {
  width: 100vw;
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  scroll-snap-align: start;
  position: relative;
}

.slide-content {
  max-height: 100%;
  overflow: hidden;
}

:root {
  --title-size: clamp(1.5rem, 5vw, 4rem);
  --h2-size: clamp(1.25rem, 3.5vw, 2.5rem);
  --body-size: clamp(0.75rem, 1.5vw, 1.125rem);
  --slide-padding: clamp(1rem, 4vw, 4rem);
  --content-gap: clamp(0.5rem, 2vw, 2rem);
}

img,
.image-container {
  max-width: 100%;
  max-height: min(50vh, 400px);
  object-fit: contain;
}

@media (max-height: 700px) {
  :root {
    --slide-padding: clamp(0.75rem, 3vw, 2rem);
    --title-size: clamp(1.25rem, 4.5vw, 2.5rem);
  }
}

@media (max-height: 600px) {
  :root {
    --slide-padding: clamp(0.5rem, 2.5vw, 1.5rem);
    --body-size: clamp(0.7rem, 1.2vw, 0.95rem);
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.2s !important;
  }
}
```

For full HTML decks, use a presentation controller pattern:
- keyboard navigation;
- touch/swipe navigation when useful;
- progress indicator or slide dots;
- intersection-observer or equivalent state to trigger reveal animations;
- optional inline editing only when explicitly requested.

If inline editing is included, export/save behavior must strip edit state before
capturing the final HTML so the saved file does not reopen with editing UI
visible.

## Density Limits

Use these as hard limits for HTML decks and strong guidance for Remotion frames.
If content exceeds them, split the slide, scene, or episode.

| Slide / Frame Type | Maximum Content |
|---|---|
| Title / hook | 1 heading + 1 subtitle + optional source strapline |
| Standard content | 1 heading + 4-6 bullets OR 1 heading + 2 short paragraphs |
| Framework / grid | 1 heading + 6 cards maximum |
| Code / terminal | 1 heading + 8-10 lines of code |
| Quote / source proof | 1 quote up to 3 lines + attribution |
| Image / diagram | 1 heading + 1 image/diagram with readable annotation |
| Cover | 1 large claim + compact strapline + 1 dominant proof artifact |

Never preserve a slide count by cramming. Preserve quality by splitting.

## Asset Handling

- Inspect source images before deciding the visual outline.
- Use direct local paths for local HTML previews; do not base64 large images by
  default.
- Never overwrite original assets.
- Resize oversized images for preview performance only when needed and write
  processed copies with a suffix such as `_processed`.
- Do not repeat the same source image across multiple frames unless it is a logo
  used only for source attribution or a deliberate series identity mark.
- When a source diagram is evidence, frame it as evidence and add explanatory
  overlays rather than redrawing it into a different taxonomy.

## HTML Code Quality

- Prefer single-file, zero-dependency HTML for previews and shareable static
  decks.
- Use structured CSS variables for palette, typography, spacing, and motion.
- Use semantic HTML, ARIA labels for controls, and keyboard-operable navigation.
- Comments should explain editable sections or non-obvious visual mechanisms.
- Avoid adding npm/build dependencies for preview work unless the task
  explicitly requires them.

## Remotion Rules

- Scene graph remains the source of truth.
- Components render claims, labels, subtitles, source refs, artifacts, and focus
  states from scene data.
- Add a new artifact component only when existing components cannot express the
  visual job.
- Keep layout regions stable across scenes unless the scene graph explicitly
  changes mode.
- Use source diagrams from `remotion/public/<slug>/diagrams/` or equivalent
  static assets.
- For new or revised scenes, use `artifact.fallback: "generated"` only when a
  content-derived backup is required.
- Covers reuse the same visual family as the video.

## Frame Fitting

- One screen carries one primary idea.
- A normal content screen has one headline and either 2-5 support points, one
  diagram, or one compact framework.
- If a frame needs more than six visual objects, split the beat.
- Reserve a bottom subtitle band and top progress/stage band.
- Do not place important text in subtitle-safe or cover-safe areas.
- Test dense Chinese labels early.

## Motion Rules

- Motion should land on or slightly before the spoken focus phrase.
- Prefer transform and opacity.
- Do not animate every element.
- Do not let decorative animation distract from source diagrams or subtitles.
- Separate ambient motion from semantic motion. Background light can drift
  slowly across the whole scene as visual identity; foreground diagrams should
  use one-shot reveal, state change, accumulation, hold, or explicit cycle based
  on the spoken concept.
- Loop foreground motion only when the concept itself is cyclic, such as
  monitoring, repeated queue arrival, a feedback loop, or heartbeat. For gates,
  audits, bottlenecks, routing, and decisions, prefer reveal -> state change ->
  hold; repeated replay usually reads as decorative.
- When repeated scenes share one semantic context, keep the complete visual
  group present. Change focus by highlighting the active entity, connection,
  label, or state, not by hiding the rest of the group or replaying the whole
  diagram as if it were a new context.
- If the semantic boundary is uncertain, default to the simplest treatment:
  bring the visual group in once, play the foreground motion forward once, hold
  the complete context while focus changes, and take the group out once at the
  end of that context.
- Connectors must dock at node boundaries or explicit ports. They must not cross
  labels, central nodes, subtitles, or other semantic objects.
- Respect reduced-motion behavior in HTML previews.

## QA Checklist

Before finalizing visual work:
- Source taxonomy and evidence are preserved.
- There is one primary idea per frame.
- Subtitles, labels, claims, and diagrams are readable.
- No text overflows or crowds safe areas.
- Active visual focus matches the voice.
- Motion is semantic.
- The artifact avoids generic AI aesthetics.
- The cover communicates the main value within one second.
- Source diagrams are clearly framed as evidence.
- Local image and audio paths are valid.
