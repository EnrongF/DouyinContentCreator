# QA

## Status

- Build status: `rendered`
- Publish status: `package ready`
- Video: `video.mp4`
- Cover: `cover.png`

## Render Verification

- Remotion render completed successfully.
- Video output: `video.mp4`, reported by Remotion as `9.1 MB`.
- Composition: `the-founders-playbook-ai-native-startup-ep04-founder-not-router`
- Timeline: `1626 frames`, `30fps`, target duration `54.2s`.
- Format from scene graph: `1080x1920`.
- Subtitles are burned into the frame by `FounderFrame`.
- Cover dimensions verified with `sips`:
  - `cover.png`: `1080x1440`
  - `cover.grid.png`: `1080x1440`
  - `cover.vertical.png`: `1080x1920`

## QA Stills

- `contact-sheet.jpg`
- `qa-frame-0000.png`
- `qa-frame-0060.png`
- `qa-frame-0300.png`
- `qa-frame-0430.png`
- `qa-frame-0560.png`
- `qa-frame-0650.png`
- `qa-frame-1100.png`
- `qa-frame-1260.png`
- `qa-frame-1500.png`

Visual checks:
- Cover headline and subhead are readable in grid format.
- Top progress labels and bottom subtitles stay in reserved regions.
- Launch gate and attention audit visuals are readable at phone size.
- No sampled subtitle overlaps the central artifact.
- Router connector lines dock at the founder node boundary and do not cross the
  founder label.
- Reused router and audit artifacts now use state-specific hold/highlight
  behavior instead of replaying the same foreground reveal every chunk.
- Reused semantic contexts keep the full element group visible; focus moves by
  highlighting the active entity or connection instead of hiding the surrounding
  context.
- Background light now uses slow warm/cool drift and breathing movement as
  ambient identity motion; it does not imply foreground source logic or compete
  with subtitles.
- Router and audit contexts now use a conservative one-in / forward-motion /
  one-out treatment across adjacent scenes instead of re-entering the same
  visual group repeatedly.
- Attention audit lane cards keep right-side breathing room so focus outlines,
  glows, and labels are not clipped.

## Fidelity Checks

Pass:
- Launch is kept separate from MVP and Scale.
- Founder attention is redirected, not removed.
- The audit preserves the three categories: automation, delegation, founder judgment.
- Security, compliance, enterprise readiness, and detailed growth metrics remain out of scope.

## Remaining Gate

ASR QA passed after normalizing the common `Launch` / `Lunch` ASR variant. Evidence:
- `voice/the-founders-playbook-ai-native-startup-ep04-founder-not-router/asr-qa.md`
- `voice/the-founders-playbook-ai-native-startup-ep04-founder-not-router/asr.txt`
