# QA

## Source Gate

- Status: Pass for existing rendered package; PDF-only value-budget redo completed separately.
- Primary source for the latest value-budget redo is the provided Anthropic PDF: `/Users/fuenrong/Downloads/Building Effective AI Agents- Architecture Patterns and Implementation Frameworks.pdf`.
- Latest source map, synthesis, compression, and series map now treat the PDF as the source of truth and mark supporting sources as out of scope unless explicitly added back.
- Existing rendered video and TTS audio were not regenerated in the PDF-only redo and may still contain earlier supporting-source terminology.
- Original PDF diagrams were extracted into `resources/building-effective-ai-agents/diagrams/`, but the existing rendered video has not yet been updated to include them.
- Vendor-supplied examples are treated as examples, not independent market proof.

## Audience Gate

- Status: Pass.
- The package is aimed at business users interested in agent implementation decisions.
- The script focuses on when to use and avoid each architecture pattern, not only on technical taxonomy.

## Subtitle Gate

- Status: Pass for final render.
- Subtitles are burned directly into every rendered frame.
- No `.srt` sidecar is produced, matching Douyin upload constraints.
- Remotion subtitle border removed; subtitles now use a soft transparent backing only.

## Cover Gate

- Status: Pass.
- `cover.png` uses the same graphite/cyan executive technical documentary style as the video.
- Cover title: `别急着上 Agent`.
- Cover visual: business decision matrix.
- `cover.remotion.png` rendered successfully at 1920 x 1080 from the Remotion stack.

## Render Gate

- Status: Pass for voice-synced final render.
- `video.mp4` exists and is readable as an MP4 container.
- `video.remotion.mp4` rendered successfully from the native 16:9 Remotion scene graph with scene-synced audio.
- Remotion output duration target: 103.733 seconds, 3112 frames at 30 fps.
- Timing consistency QA: pass. Composition duration now uses the same per-scene frame rounding as scene playback and audio sequencing.
- QA stills rendered from mid-scene frames:
  - `qa-stills/frame-0060.png`
  - `qa-stills/frame-1050.png`
  - `qa-stills/frame-2050.png`
- Connector QA: pass. Architecture connector lines now stop outside node/card edges and no longer cut through visual elements.
- Title scale QA: pass. Scene titles and cover title were reduced slightly to leave more room for the visual artifact.

## Voice Gate

- Status: Pass for existing rendered package; stale for latest PDF-only scene/script edits.
- TTS generated 12 measured scene chunks with model `gpt-4o-mini-tts`, voice `marin`.
- Final measured duration: 103.656 seconds.
- Container audio check: AAC stereo 48 kHz, estimated duration 103.787 seconds including codec/container padding.
- ASR QA status: pass.
- Pronunciation QA fix applied before final render:
  - `Sequential Workflow` changed to `顺序工作流`.
  - `权限` line changed to `权限控制、日志记录、监控、评估、回滚、人工接管`.
- Remaining QA: manual full watch/listen pass is still recommended before Douyin upload.
- Latest PDF-only script replaces earlier `Harness` wording with production-control and observability wording. TTS must be regenerated before this script can be treated as final media.

## Remotion Checksums

- `video.remotion.mp4`: `0facfa69849665cbb25113815dbb7b824d62b38152db8c8e752c1abbcbe5aeb9`
- `cover.remotion.png`: `af1e24a022120b3233513a2df71be23684d99b4b216157c4d1e293dda01483d6`
