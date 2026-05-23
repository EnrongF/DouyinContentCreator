# Production Pipeline

This file defines the production pipeline and gates. `PROJECT_CHARTER.md`
defines the product charter, `VOICE_SYSTEM.md` defines voice production, and
`VISUAL_SYSTEM.md` defines visual exploration and design rules.

## Target Stack

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
-> React Motion Components
-> Remotion Rendering
-> QA
-> Douyin Distribution
-> Release Verification
-> Platform Performance Feedback
```

Historical Python or Swift render scripts may remain as historical artifacts.
New or revised publishable video work should use scene graphs plus Remotion.

## Layer Contracts

| Layer | Primary location | Contract |
|---|---|---|
| Research | `sources/` | Source links, provenance, local assets, freshness notes. |
| Extraction | `extraction/` | Claims, terms, artifacts, caveats, source value inventory. |
| Synthesis | `synthesis/` | Candidate mental upgrades, source logic, useful narrative structure. |
| Series | `series/` | Required when one topic has multiple mental upgrades. |
| Compression | `compression/` | Selected episode promise, value budget, mental model, omissions. |
| Voice | `voice/<slug>/` | Script, paragraph plan, speech chunks, pronunciation, audio, ASR, manifest. |
| Scene graph | `scene-graphs/` | Source of truth for sequence, claims, subtitles, focus, artifacts, refs. |
| Visual preview | `presentation/` | HTML previews, style comparisons, static decks, memo artifacts. |
| Source visual inventory | `review/<slug>.source-visual-inventory.md` | Optional Visual Production style-setting artifact for extracted source colors, typography, diagram style, asset-use rules, endorsement risks, and template-fit notes. |
| Render | `remotion/` | React components, compositions, covers, stills, final MP4. |
| Distribution | `douyin/<slug>/` | Final video, cover, caption, manifest, QA. |
| Review | `review/` or package QA | Fidelity, taxonomy, expression, sync, render, and platform-fit findings. |
| Release | `final/` and package files | Package verification, manifests, final index, shipped references. |
| Platform | `douyin/<slug>/platform.md` | Post-publish metadata experiments, metrics, follower conversion, engagement, iteration notes. |

## Required Gates

### Source Value Inventory

Run after source qualification and before scope decisions.

Capture:
- Core concepts and source-defined terms.
- Diagrams, tables, metrics, examples, and artifacts.
- Process steps, failure modes, caveats, and boundaries.
- Practical implications.
- Initial tag for each value item.

Value tags:
- `non-cuttable`: required for truth or the core model.
- `episode-core`: required for the selected episode.
- `supporting`: useful if pacing allows.
- `move-to-later`: valuable but belongs in another episode.
- `omit`: redundant or low-value for the audience.

### Source Logic / Taxonomy Gate

Run after extraction and before compression, script, cover, or render decisions.

Check:
- Source-defined parent categories, child patterns, peer relationships, examples,
  implementation variants, metrics, and caveats are identified.
- Synthesis does not promote child patterns into peer categories or merge
  separate source layers.
- Visuals and cover labels match the source layer they represent.
- Intentional adaptations are labeled as synthesis.

Status: `Pass`, `Pass with caveats`, or `Fail`.

Any `Fail` blocks scripting, cover finalization, TTS, and final render.

### Optional Visual Style Step: Brand / Source Visual Extraction

This is not a universal project gate. Run it only inside Visual Production when
visual style is undecided and a source PDF, website, screenshot, product UI,
logo, or report identity materially affects trust or style.

Owner: Visual Production.

Use `prompts/brand-source-extractor.md`.

Output:

```text
review/<slug>.source-visual-inventory.md
```

Capture:
- Source or brand visual tokens: colors, typography clues, surfaces, layout
  grammar, diagram language, icon style, and annotation style.
- Source asset use: preserve, annotate, crop, montage, avoid, or review-only.
- Endorsement risks: what cannot be copied or emphasized as channel branding.
- Template fit: recommended and avoided templates from
  `visual-templates/templates.json`.

Rules:
- Extract before designing.
- Do not invent brand details.
- Do not redraw logos.
- Do not choose the final style alone.
- Feed the inventory into Visual System Designer and preview comparison.

Skip this step when:
- the task is not visual-production work;
- the visual system is already locked;
- the source has no meaningful visual identity or asset constraints;
- the change is a narrow render, copy, QA, or package fix.

### Series / Episode Scope Gate

Run before scripting.

Ship one artifact only when:
- There is one main mental upgrade.
- Two to four supporting claims are enough.
- One example or artifact can carry the idea.
- No major source value is lost.

Create a series when the topic has multiple workflow stages, decision points,
failure modes, implementation layers, or source concepts that would rush the
voice or overload the frame.

### Value Budget

Run before compression and update whenever the script feels rushed.

Each compressed episode must declare:
- Compression level: `short`, `standard`, or `deep technical`.
- Retained value.
- Moved value.
- Omitted value.
- Non-cuttable claims, terms, metrics, caveats, or artifacts.
- Expected value loss, if any.

Compression levels:
- `short` 15-30 seconds: one contrast, one source-faithful idea, one takeaway.
- `standard` 45-90 seconds: one mental model, three to five named parts, one
  example or artifact, one takeaway.
- `deep technical` 90-180 seconds: one mental upgrade with sections; use only
  when fidelity would suffer in a shorter format.

### Native Chinese Expression Gate

Run before TTS, subtitle lock, cover finalization, captions, or render. See
`VOICE_SYSTEM.md` for detailed voice and expression rules.

Check:
- Narration, subtitles, labels, cover text, and captions sound natural in
  Chinese.
- English source terms remain visible when needed and are explained naturally.
- Avoid translation-shaped noun stacks, rigid metaphors, and uncommon literal
  compounds.
- Spoken sentences are short enough for口播.

Status: `Pass`, `Pass with fixes`, or `Fail`.

Any `Fail` blocks TTS, subtitle lock, cover rendering, and final render.

### Voice Naturalness And ASR Gate

Run before locking `voice-manifest.json`. See `VOICE_SYSTEM.md` for the full
TTS, ASR, subtitle, and timing contract.

Check:
- Each paragraph has one idea, one intention, one pacing direction, one visual
  focus.
- Speech chunks are performable and not written-sounding.
- Numbers, symbols, and English terms are normalized for speech.
- Generated takes have stable tone, volume, and rhythm.
- ASR transcript matches intended narration closely enough for subtitles and
  timing.

### Render QA Gate

Run before distribution.

Check:
- Final MP4 contains burned-in subtitles.
- Voice focus matches visual focus.
- Progress labels and subtitles do not overlap important content.
- Source diagrams and labels are readable at target size.
- Cover is readable in a phone feed and uses source attribution correctly.
- Local image/audio paths exist.
- `douyin/<slug>/manifest.md` and `qa.md` reflect the final artifact.

## Scene Graph Contract

Scene graphs are the video source of truth.

Minimum shape:

```json
{
  "slug": "topic-slug",
  "seriesSlug": "optional-series-slug",
  "episode": 1,
  "format": "16:9",
  "durationTarget": 90,
  "visualSystem": "executive-technical-documentary",
  "scenes": [
    {
      "id": "scene_id",
      "sectionLabel": "Decision Frame",
      "claim": "One source-faithful claim",
      "artifact": "decision-gate",
      "paragraphId": "p01",
      "beats": [
        {
          "id": "b01",
          "voice": "Spoken narration.",
          "subtitle": "Burned-in subtitle text",
          "focus": ["focus-element"],
          "focusPhrase": "spoken focus phrase",
          "focusCue": "outline",
          "sourceRefs": ["source:p23"]
        }
      ]
    }
  ]
}
```

Rules:
- React and Remotion components render claims, labels, subtitles, artifacts, and
  source refs from scene data.
- Components must not invent new claims.
- Visible stage labels should come from `sectionLabel`, not production labels
  like `Hook`, `Intro`, `Bridge`, `CTA`, or `Outro`.
- Final timing follows measured durations from
  `voice/<slug>/voice-manifest.json`.
- Dynamic focus should land on or slightly before the spoken focus phrase.

## Voice Contract

Default structure:

```text
voice/<slug>/
  script.md
  paragraph-plan.md
  speech-chunk-plan.md
  pronunciation.md
  chunks/*.mp3
  voiceover.final.mp3
  asr.txt
  voice-manifest.json
  qa.md
```

Voice is the timing layer for final video. `VOICE_SYSTEM.md` is authoritative
for paragraph design, speech chunks, pronunciation, TTS, ASR, subtitles, and
voice-frame sync.

## Remotion Contract

Required outputs for publishable video:

```text
douyin/<slug>/video.mp4
douyin/<slug>/cover.png
douyin/<slug>/contact-sheet.jpg
douyin/<slug>/manifest.md
douyin/<slug>/qa.md
```

Post-publish output, created only when performance data exists:

```text
douyin/<slug>/platform.md
```

Render requirements:
- Burn subtitles into `video.mp4`.
- Render covers from the same visual system as the video.
- Keep top progress labels and bottom subtitles in reserved safe areas.
- Use fixed composition dimensions and stable layout bounds.
- Sample stills or contact sheets before final render.

Default formats:
- `16:9` 1920 x 1080 for current documentary direction.
- `9:16` optional Douyin-native adaptation using the same scene graph with
  format-specific layout components.

## Migration Policy

- New topics use the target stack.
- Existing ad-hoc packages do not need migration unless they are revised.
- If an old topic is revised, migrate it by creating a scene graph and Remotion
  composition rather than patching historical frame scripts.
