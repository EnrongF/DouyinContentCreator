# QA

## Gates

- Source fidelity: only uses the OpenAI Engineering source requested by the user.
- Original artifact preservation: numbers, scaffold, diagrams, repo knowledge layout, architecture layers, merge philosophy, full autonomy checklist, entropy loop, golden-principles examples, and caveats are represented as simplified source-derived visual frames.
- Style: Executive Technical Documentary refined with the HTML Effectiveness reference; charcoal/ivory editorial base, serif headlines, mono metadata, clay/olive accents, evidence cards, horizontal diagrams, and progress/checklist structures.
- Horizontal-wide fit: hook is source-specific and concrete; this rerun intentionally favors source fidelity over short duration, so it should be treated as a high-density technical documentary cut.
- Quality risk: no external source triangulation because the user explicitly skipped the search role.
- New production gate: voice must sync to the active frame/focus element.
- New production gate: focus elements must be highlighted dynamically; static slide-only output is a review cut, not the final publishable form.

## Current Status Against New Gates

- Source fidelity: pass.
- Voice QA term gate: pass.
- Duration: pass for a deep technical explainer after simplification.
- Voice-frame sync: pass for generated beat sequence. The render now uses 24 phrase-level TTS chunks, derives 59 beat timings in `beat_audio_manifest.json`, and renders 472 phased frames from `frame_durations.json`.
- Dynamic focus: pass for generated beat sequence. The hard rectangle/scanline system was replaced with soft local glow, subtle corner brackets, and color-shifting emphasis on the active element.
- Subtitle policy: pass. The generated video no longer includes the bottom subtitle/focus-caption card; platform subtitles can be added from the voice track.
- Layout policy: pass. Background grids were removed, decorative dev chrome was simplified, and frames now use a native 1920 x 1080 horizontal composition, not a portrait crop/remap.
- HTML-native renderer: pass. The final frames are browser screenshots exported from `html-renderer/index.html` using deterministic `beat` and `phase` URL state.

## Final Render

- Video: `video.mp4`
- Resolution: 1920 x 1080
- Frame rate: 30 fps
- Duration: 00:03:42.30
- Beat frames: 59
- Phased frames: 472
- Timing manifest: `frame_durations.json`
- Renderer: `html-native-playwright`
- Audio: AAC mono, 24 kHz
- Voice: OpenAI TTS `alloy`, conversational Mandarin instructions, speed `1.2`, phrase-level chunk generation
- QA sheet: `native-wide-contact-sheet.jpg`

## Voice QA

- Voice QA checked both terminology and semantic phrase integrity after the simplified Mandarin-first rewrite.
- Narration complexity was kept simple across 59 beats; 24 phrase chunks replace both previous isolated-beat and scene-level TTS to reduce robotic prosody resets while preserving focus sync.
- The longest derived beat is 5.39 seconds and no beat exceeds 6 seconds.
- Pronunciation-oriented rewrites replace brittle spoken tokens such as `PR`, `CI`, `worktree`, lowercase `agent`, `bug`, and `docs 目录` with natural Mandarin phrases: “代码合并请求”, “持续集成”, “独立工作区”, “智能体”, “问题”, and “文档目录”.
- Local script pronunciation gate now fails if brittle spoken tokens reappear or required natural phrases are missing.
- Hard-to-pronounce "AI slop" is spoken as "AI 垃圾代码" for Mandarin clarity while keeping the source concept in the package notes.
- Reviewer-found risks to listen for: Harness Engineering, AGENTS.md, Chrome DevTools, Providers, golden principles, typed SDK.
- Final transcription term gate: passed with `missing_terms=none`.
- Required terminology gate now exits nonzero when ASR misses required terms, instead of only printing the missing list.
- Term validation now normalizes whitespace/case so `Chrome DevTools` is accepted when ASR returns `chrome dev tools`; it also accepts ASR variants of `AGENTS.md` because Mandarin ASR often drops the English plural `s`.
- Required terminology gate passed after restoring the exact "Chrome DevTools" term.
- Required terminology gate passed again after restoring a speakable `AGENTS.md` mention in the naturalized script.
- Scene-level ASR spot check fixed a weak “目录” reading by changing the spoken phrase to “目录结构”.
- Remaining manual gate: watch/listen once in real time before upload, because ASR can miss subtle cadence issues.

## Multi-Role Review Fixes Applied

- Source fidelity: added `~1/10 time`, stronger product adoption context, initial scaffold details, six-hour Codex runs, roughly 100-line AGENTS.md map, expanded docs tree, merge strategy, full autonomy checklist, golden-principles examples, cleanup PR loop, and long-term caveats.
- Narrative strategy: sharpened the hook into “别只看那一百万行代码,” moved Harness Engineering earlier, and made the narration more spoken Mandarin while preserving source-critical terms.
- Visual QA: changed the design model from static slide + overlay to artifact scene + semantic state changes; fixed metric label wrapping, entropy caption overflow, and long caveat label overflow during rerender.
- Wide-format QA: replaced the previous 1080 x 1920 portrait-to-wide adaptation with native 1920 x 1080 scene functions and native focus coordinates.
- Visual frame QA: all 472 frames are valid 1920 x 1080 images; key-frame contact sheets were manually checked, and reported issues in scaffold labels, docs rows, autonomy loop labels, beat 42 focus, beat 38 warning spacing, and final caveat overflow were patched.
- Native-wide gate: `render_assets.py` no longer contains `wide_frame`, `transform_box`, `NARRATIVE_SRC`, `CONTENT_SRC`, `fit_crop`, or `OUT_W`.
- HTML renderer fixes: removed the tiny footer caption text, fixed `docs/` row overlap, added missing app surface styling, and regenerated the full 472-frame set before final mux.
- Design-review refinement: removed the remaining grid texture, raised local contrast, softened inactive dimming, reduced footer/meta noise, changed the stage to full-coordinate layout to prevent right/bottom clipping, and repaired the DevTools process label so it no longer collides with the progress rail.
- Browser capture QA: `frame_durations.json` now records `renderer=html-native-playwright`; all exported PNGs are 1920 x 1080 and the per-beat duration sums match `beat_audio_manifest.json`.
- Motion/sync QA: converted the cut into a 59-beat / 472-phase sequence with micro-beats for dense source sections and active-element highlights.
- Multi-agent refinement: Source Fidelity Analyst identified missing source artifacts; Narrative/Script Agent compressed the script for Douyin; Visual Systems Designer required artifact-specific scenes and slimmer focus captions.
- Production QA: render script now targets higher video quality for platform recompression.
- Production QA: TTS script now synthesizes phrase-level chunks with retry/reuse handling, writes `scene_audio_manifest.json`, derives beat timing into `beat_audio_manifest.json`, then concatenates the phrase chunks for final audio.
