# Voice System

This file defines the voice, Chinese expression, TTS, ASR, subtitle, and timing
contract for publishable artifacts.

Voice is not a late production step. In this project, voice is the timing layer
that Remotion follows.

## Core Rule

Design spoken structure before generating audio:

```text
episode promise
-> paragraph voice design
-> speech chunk plan
-> native Chinese expression gate
-> pronunciation and symbol rewrite
-> TTS takes
-> best-take selection
-> duration measurement
-> ASR QA
-> voice-manifest.json
-> Remotion timing lock
```

## Voice Principles

- One voice paragraph carries one idea, one speaking intention, one pacing
  direction, and one primary visual focus.
- One speech chunk is a performable spoken unit, usually 1-3 short sentences.
- Voice should sound like natural spoken Mandarin, not translated written
  English.
- English technical terms may remain visible, but spoken delivery should be
  comfortable and understandable.
- Timing is evidence: final visuals must follow measured audio durations, not
  draft estimates.
- Subtitles come from the same locked voice manifest used for render timing.

## Voice Directory Contract

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

Required files for publishable video:
- `script.md`: final narration text.
- `paragraph-plan.md`: paragraph intention, pacing, emotion, visual focus.
- `speech-chunk-plan.md`: chunk boundaries, spoken text, pauses, emphasis.
- `pronunciation.md`: English terms, numbers, symbols, names, and replacements.
- `voice-manifest.json`: locked audio, chunk durations, subtitle text, timing.
- `asr.txt`: transcript from generated audio.
- `qa.md`: voice naturalness, ASR, subtitle, and sync notes.

## Paragraph Design

Each paragraph should declare:
- `paragraphId`
- Core idea
- Speaking intention
- Emotional tone
- Pacing direction
- Primary visual focus
- Source value carried by the paragraph

Block a paragraph if:
- It contains two unrelated ideas.
- It needs more than one primary visual focus.
- It uses formal written structure that sounds unnatural when spoken.
- It depends on a source claim that is not captured upstream.

## Speech Chunk Design

Chunk rules:
- Target 2-8 seconds per chunk for Mandarin.
- Avoid chunks over 15 seconds unless source fidelity requires it.
- Keep punctuation as acoustic control: short pauses, emphasis, and clean
  breath points.
- Split long technical sentences before TTS.
- Keep related emotional tone together; do not over-split so every sentence
  sounds like a new take.

Each chunk should include:
- `chunkId`
- `paragraphId`
- Spoken text
- Subtitle text
- Intended pause or emphasis
- Focus phrase
- Expected visual focus

## Native Chinese Expression Gate

Run before TTS, subtitle lock, cover finalization, captions, or render.

Check:
- Narration sounds like natural Mandarin口播.
- Subtitles read naturally while staying compact.
- Cover text and stage labels do not sound translated.
- English source terms are retained only where useful.
- Numbers, symbols, abbreviations, and product names are spoken naturally.
- Technical phrasing is precise without becoming stiff.

Avoid:
- Literal compounds that native speakers would not use.
- English grammar mapped into Chinese.
- Long noun stacks.
- Empty dramatic phrases that weaken source trust.
- Multiple metaphors in one paragraph.

Status: `Pass`, `Pass with fixes`, or `Fail`.

Any `Fail` blocks TTS, subtitle lock, cover rendering, and final video rendering.

## Pronunciation And Symbol Rewrite

Before TTS, normalize:
- English model, product, and framework names.
- Numbers, percentages, versions, file names, and code terms.
- Acronyms and mixed Chinese-English phrases.
- Symbols such as `/`, `->`, `+`, `#`, and file extensions.

Keep the visual term accurate even when the spoken form is adapted for clarity.

## TTS Production

Default Chinese voice maker:
- Provider: Qwen / DashScope.
- Model: `qwen3-tts-instruct-flash`.
- Voice: `Ethan`.
- API key env: use `DASHSCOPE_API_KEY` when present, otherwise `QWEN_API_KEY`.

OpenAI `gpt-4o-mini-tts` with `marin` remains the fallback path and comparison
baseline, but new Chinese narration should start with Qwen `Ethan` unless a
listening test shows it does not fit the episode.

Default to speech-chunk generation for publishable Chinese narration. Split
or merge chunks based on naturalness, pronunciation isolation, and focus timing.

Production rules:
- Generate more than one take for important or difficult paragraphs.
- Select best takes based on naturalness, pacing, pronunciation, and emotional
  continuity.
- Regenerate weak paragraphs rather than accepting the first usable output.
- Avoid stitching so finely that tone, volume, or emotion resets too often.
- Preserve consistent voice identity across the full artifact.

## ASR And Voice QA

Run ASR after final take selection.

Check:
- ASR transcript matches intended narration closely enough for subtitle timing.
- Required terms are recognized or have acceptable ASR variants.
- No chunk has distracting mispronunciation.
- Pace leaves enough room for the visual focus to land.
- Listener fatigue is low: rhythm, pauses, and emphasis vary naturally.

## Voice Manifest Contract

`voice-manifest.json` is the timing authority for Remotion.

It should include:
- Slug and episode metadata.
- Audio file paths.
- Paragraph and chunk IDs.
- Final spoken text.
- Subtitle text.
- Start time, end time, and duration.
- Focus phrase or focus cue references.
- ASR or QA status when useful.

Render code should use the manifest for:
- Composition duration.
- Subtitle timing.
- Focus timing.
- Audio placement.

## Subtitle Rules

- Subtitles must be burned into final `video.mp4`.
- Do not rely on a standalone `.srt` for Douyin publishing.
- Subtitle text should come from locked chunk text or manifest text.
- Subtitle line breaks must fit the target format and safe area.
- Subtitles should not compete with source diagrams or stage labels.

## Voice-Frame Sync

Every spoken focus phrase should have a corresponding visual state:
- Reveal
- Highlight
- Outline
- Zoom
- Path activation
- State change
- Pointer or label emphasis

The focus should land on or slightly before the spoken phrase and hold long
enough to read.
