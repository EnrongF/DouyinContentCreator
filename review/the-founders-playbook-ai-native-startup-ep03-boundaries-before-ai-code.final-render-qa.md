# Final Render QA

Slug: `the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code`

## Gate Status

- Stage: `final render QA`
- Status: `technical pass`
- Pause required: `yes`
- Final video: `douyin/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code/video.mp4`
- Sample stills: `review/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code.samples/`
- Next approved stage: `Douyin package`
- Not approved yet: `publish/upload`

## Render Evidence

- Render command completed through Remotion.
- Composition: `the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code`
- Frames rendered: `1900`
- Format: `1080x1920`, `30 fps`
- MP4 file size: `12,368,744 bytes`
- Audio: `aac`, `48000 Hz`, `2 channels`
- Audio duration from `afinfo`: `63.381 seconds`
- Burned-in subtitles: yes, rendered in Remotion from scene graph subtitles.
- Sound effects: five sparse concept cues mixed under the voice.

## Visual QA

Sample stills reviewed:

- `c02-sprawl.png`
- `c01-boundary-first.png`
- `c05-not-add-more.png`
- `c10-readable-refined.png`
- `c06-scope.png`
- `c11-decision.png`

Pass:
- EP badge correctly shows `EP03`.
- Subtitle area is clear and does not collide with central artifacts.
- Core visual distinction is preserved: boundary / context / code.
- Scope document scene uses a three-row boundary model.
- Final takeaway frame locks `先写边界` before `再写代码`.

Concept-symbol pass:
- Symbols comply with the locked Founder Playbook VI first.
- Symbol design starts from the section key message, then chooses the abstract mark.
- iOS icon lessons are used only as discipline: strong silhouette, one concept per mark, small-size legibility.
- Core marks are abstract: boundary frame, execution stack, evidence bars, void state, mismatch paths.
- `c01` was rebuilt so speed is visually contained by a boundary-first frame.
- `c05` was rebuilt so the wrong add-more question dims before scope is written.
- `AI 可读取` mark was refined from a generic signal/path into a three-step symbol: written context -> read gate -> AI-readable execution path.

SFX pass:
- Effects are declared in the scene graph with concept and rationale.
- They mark only major actions: code speed, boundary sprawl, scope lock, context drift, and next router gate.
- Routine motion and minor reveals remain silent.

Known limitations:
- `ffprobe` is not available globally in this environment; video stream metadata is inferred from Remotion composition settings and render output.
- Final listening QA should still be done before upload because ASR checks transcript fidelity, not tone fatigue.

## Source Fidelity QA

Pass:
- Keeps MVP as evidence-gathering, not full-product construction.
- Avoids Sean Ellis and product availability claims.
- Treats `CLAUDE.md`/persistent context as a general source example, not a universal product law.
- Keeps security/compliance and launch hardening out of this episode.
- Bridges to Episode 4 without teaching launch systems here.

## Decision

Technical render QA passes. Proceed to Douyin package.
