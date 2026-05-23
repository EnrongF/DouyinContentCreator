# Harness Engineering QA

## Source Gate
- Status: Pass
- Source count: top source bundle was narrowed by Source Scout and Source Qualifier.
- Source quality: mostly first-party Harness docs, source repos, and technical blogs from 2025-2026.
- Risk: Harness claims are first-party positioning; do not present as independent market validation.

## Content Gate
- Status: Pass
- One main idea: AI delivery agents need a governed delivery harness.
- Hook: strong risk-based opening.
- Source fidelity: preserves inner-loop vs outer-loop distinction, harness control-plane framing, knowledge graph, governed tools, verification, and audit evidence.
- No overclaim: avoids saying Harness is the only solution.

## Douyin Gate
- Status: Pass
- First 3 seconds: direct risk hook.
- Mobile readability: designed for 9:16 with large text.
- Simplicity: one core metaphor, "model is brain, harness is control plane."
- Works without sound: subtitles are included in storyboard/video frames.

## Visual Gate
- Status: Pass
- Visual direction updated from generic AI slide style to an Anthropic-like editorial technical note style.
- Uses warm paper background, ink typography, restrained clay/ochre/moss accents, thin rules, numbered notes, structured diagrams, and generous whitespace.
- Avoids neon gradients, purple bias, glass cards, noisy grid backgrounds, and decorative icons.
- Manual visual QA checked cover and the most complex diagram frame; one overflow issue in scene 7 was corrected before final render.

## V2 Information Density Gate
- Status: Pass for storyboard and silent preview; voiced final video pending TTS approval.
- V2 expands from 8 simple scenes to 14 source-backed scenes.
- Added important details: concrete failure modes, knowledge graph vs RAG, live context, Delegate execution boundary, secret handling, evidence chain, and MCP/Skills quantitative artifacts.
- V2 silent preview: `video.v2.silent.mp4`.
- Blocker: OpenAI TTS regeneration for the expanded script was not approved, so `video.mp4` was not overwritten with mismatched audio.

## Render Gate
- Status: Pass
- `video.mp4` regenerated with `voiceover.final.mp3` at 1080x1920, 30 fps, 00:01:31.83, with AAC audio.
- `render_video.py` now prefers `voiceover.final.mp3`, then `voiceover.openai.mp3`, then the old `voiceover.aiff` fallback.
- OpenAI TTS target: `gpt-4o-mini-tts`, natural conversational Mandarin, short-video technology explainer tone.
- `cover.png`, `storyboard.html`, `storyboard.gif`, voiceover files, and frame PNGs are included.
- Note: video rendering used a temporary bundled `imageio-ffmpeg` encoder because system `ffmpeg` was not installed.

## Voice Gate
- Status: Pass automated transcription check
- `voiceover.final.mp3` was generated with OpenAI TTS voice `marin`.
- `voiceover.transcript.txt` confirms the key English terms survived transcription: AI, Coding Agent, Delivery Agent, Harness engineering, delivery harness, feature flag, scorecard, rollback, audit log, API key.
- Remaining risk: final taste check should still be done by human listening before publishing, because transcription cannot judge vocal warmth perfectly.
- Disclosure: caption/package should state the narration is AI-generated when publishing.
