# Final Render QA

Slug: `the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand`

## Gate Status

- Stage: `final render QA`
- Status: `technical pass - rebuilt content-fitted visual system`
- Pause required: `yes`
- Final video: `douyin/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/video.mp4`
- Sample stills: `review/the-founders-playbook-ai-native-startup-ep02-content-fit-samples/`
- Next approved stage: `Douyin package`
- Not approved yet: `publish/upload`

## Render Evidence

- Render command completed through Remotion.
- Composition: `the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand`
- Frames rendered: `1955`
- Format: `1080x1920`, `30 fps`
- MP4 file size: `13,213,162 bytes`
- Audio: `aac`, `48000 Hz`, `2 channels`
- Audio duration from `afinfo`: `65.216 seconds`
- Sound effects: six sparse concept cues mixed under the voice.
- Burned-in subtitles: yes, rendered in Remotion from scene graph subtitles.

## Visual QA

Sample stills reviewed:

- `c02-false-validation.png`
- `c05-validation-gate.png`
- `c10-evidence-questions.png`
- `c13-takeaway.png`

Pass:
- EP badge correctly shows `EP02`.
- Subtitle area is clear and does not collide with central artifacts.
- Core visual distinction is preserved: Demo / evidence / demand.
- Validation gate stays inside the Idea-stage logic and does not introduce PMF mechanics.
- Final takeaway frame uses the corrected headline `Demo 能提问，不能证明有人要`.

Content-fit pass:
- Demo speed uses a path diagram.
- False validation uses a split Demo/evidence panel.
- Validation checks use stacked rows fitted to the three checks.
- Customer discovery questions use a vertical question stack plus evidence column.
- Praise versus pain uses a threshold diagram.
- Final decision uses a two-sided question/proof distinction.
- Cover visual uses Demo -> question tool and praise/pain evidence structure.

Concept-symbol pass:
- EP02 no longer relies mainly on direct object-expression symbols.
- Added abstract concept glyphs for void evidence, signal, threshold, mismatch,
  question vector, proof rejection, and boundary.
- Direct labels remain only as secondary anchors for fast mobile comprehension.

Symbol/motion principle pass:
- Complies with the locked Founder Playbook VI.
- Fits symbols and motions to the content concept instead of using decoration.
- Keeps marks understandable at phone size.
- Uses common diagram grammar before custom invention.
- Preserves an abstract style and avoids literal product/person/object icons.

SFX pass:
- Effects are declared in the scene graph with concept and rationale.
- They mark only major actions: Demo path, empty evidence, evidence gate,
  threshold filter, final decision lock, and next boundary.
- Routine motion and minor reveals remain silent.

Known limitations:
- `ffprobe` is not available globally in this environment; video stream metadata is inferred from Remotion composition settings and render output.
- Final listening QA should still be done before upload because ASR checks transcript fidelity, not tone fatigue.

## Source Fidelity QA

Pass:
- Does not use the unverified `42%` statistic.
- Does not use Sean Ellis or PMF measurement details.
- Does not present Claude product surfaces as universal startup law.
- Keeps the source claim: prototype is useful as a pressure-testing prop, not proof of validation.

## Decision

Technical render QA passes. Proceed to Douyin package.
