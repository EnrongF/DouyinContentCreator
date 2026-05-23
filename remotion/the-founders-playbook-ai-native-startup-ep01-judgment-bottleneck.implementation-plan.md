# The Founder's Playbook EP01 Remotion Implementation Plan

Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`

## Gate Status

- Stage: `Remotion implementation`
- Status: `implemented; awaiting visual QA / sample still approval`
- Pause required: `yes`
- Locked visual system: `A2 Balanced VI + Content Fit`
- Chosen preview: `presentation/.visual-previews/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/style-a-v2-warm-founder-gate.html`
- Scene graph: `scene-graphs/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.json`
- Voice manifest: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/voice-manifest.json`
- Total duration: `67.300s`
- Frame count: `2019` at `30fps`
- Implementation result: `complete`
- Next approved stage after implementation: `Remotion visual QA / sample still approval`
- Not approved yet: `final render`, `Douyin package`

## Implementation Strategy

Use a separate Founder Playbook Remotion composition instead of extending the
existing `BusinessAgentGuide` composition directly.

Reason:
- Existing `BusinessAgentGuide` is built for the older `Building Effective AI
  Agents` schema and primarily `16:9` layouts.
- This episode is `9:16`, uses the locked A2 visual system, and carries
  different scene graph fields such as `focusPhrase`, `focusCue`, and
  `audioSource`.
- A separate composition avoids destabilizing the completed AI Agents series.

## Planned Files

Add:
- `remotion/src/compositions/FounderPlaybookEpisode.tsx`
- `remotion/src/components/founder-playbook/FounderFrame.tsx`
- `remotion/src/components/founder-playbook/FounderArtifacts.tsx`
- `remotion/src/components/founder-playbook/FounderSymbols.tsx`
- `remotion/src/components/founder-playbook/founderTheme.ts`
- `remotion/public/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/audio/c01.wav` through `c19.wav`

Modify:
- `remotion/src/Root.tsx`
- `remotion/package.json`

Avoid unless necessary:
- broad edits to `BusinessAgentGuide.tsx`;
- broad edits to existing AI Agents cover components;
- changing prior rendered package outputs.

## Composition Contract

Register:

```text
id: the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck
width: 1080
height: 1920
fps: 30
durationInFrames: 2019
```

The composition should:
- import the locked scene graph;
- derive scene ranges from `durationSeconds`;
- sequence audio chunks by scene id;
- render burned-in subtitles from `scene.subtitle`;
- render top metadata from `episode`, `sectionLabel`, and scene index;
- render one central artifact per scene from `scene.artifact.type`;
- preserve the A2 visual system without treating it as a fixed page template.

## Audio Plan

Copy selected Qwen chunks from:

```text
voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/chunks-qwen/
```

To:

```text
remotion/public/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/audio/
```

Use `staticFile()` paths:

```text
the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/audio/c01.wav
...
the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/audio/c19.wav
```

Do not retime audio. Scene duration follows the existing scene graph and voice
manifest.

## Visual System Implementation

Shared VI layer:
- warm black field;
- cream Chinese headline;
- amber episode badge;
- orange / cyan / amber semantic chips;
- rose only for wrong-direction or blocked-demand risk;
- quiet source mark;
- rounded / humanist Chinese font stack.

Layout regions:
- top: episode badge, section label, scene index;
- upper-middle: claim and short explanatory line;
- center: content-specific artifact module;
- bottom: integrated subtitle text with no rectangle.

Subtitle treatment:
- no boxed subtitle background;
- left aligned or optically centered depending on line length;
- thin amber/cyan accent cue;
- shadow for readability;
- must not collide with central artifact.

## Artifact Mapping

| Scene | Artifact type | Component module | Symbol | Motion |
|---|---|---|---|---|
| `c01` | `bottleneck-shift-board` | `BottleneckMap` | bottleneck | blocked build lane reveal |
| `c02` | `wrong-direction-speed-path` | `WrongDirectionPath` | path | target path dim, wrong path draws |
| `c03` | `execution-lane-accelerator` | `ExecutionLanes` | lanes | four lanes activate in sequence |
| `c04` | `execution-not-removed` | `RetainedExecutionLayer` | layer | execution layer remains highlighted |
| `c05` | `early-decision-gate` | `EarlyDecisionGate` | gate | gate shifts earlier on timeline |
| `c06` | `speed-neutral-marker` | `SpeedNeutralMarker` | path | speed stays neutral while direction waits |
| `c07` | `wrong-direction-acceleration` | `WrongDirectionPath` | path | wrong path accelerates with error trail |
| `c08` | `accelerator-steering-metaphor` | `ControlSplit` | control | accelerator pulses; steering stays separate |
| `c09` | `founder-steering-control` | `FounderSteeringControl` | control | direction selector locks to founder side |
| `c10` | `founder-decision-gate` | `FounderJudgmentNode` | node | judgment node becomes the bottleneck |
| `c11` | `go-stop-decision-cards` | `GoStopDecisionCards` | binary | go/stop cards split from one gate |
| `c12` | `judgment-sequence` | `JudgmentGateSequence` | gate | tool layer dims, judgment gates reveal |
| `c13` | `source-lifecycle-gates` | `LifecycleGates` | lifecycle | Idea -> MVP -> Launch -> Scale reveal |
| `c14` | `different-judgment-icons` | `StageJudgmentIcons` | lifecycle | each gate receives distinct decision mark |
| `c15` | `idea-stage-gate` | `IdeaGateZoom` | gate | Idea gate enlarges, later gates dim |
| `c16` | `later-gates-deferred` | `DeferredLaterGates` | lifecycle | later gates recede as future episodes |
| `c17` | `speed-question-dim` | `SpeedQuestionDim` | binary | speed prompt dims, decision prompt rises |
| `c18` | `final-decision-card` | `FinalDecisionCard` | binary | judgment receives final highlight |
| `c19` | `next-episode-gate-preview` | `DemoDemandGate` | demo/demand | Demo approaches but does not unlock demand |

## Component Design

`FounderPlaybookEpisode.tsx`:
- computes ranges;
- selects active scene;
- sequences audio;
- renders `FounderFrame`;
- renders subtitle and progress rail.

`FounderFrame.tsx`:
- owns vertical layout;
- applies VI layer;
- renders badge, claim, chips, artifact, subtitle, source mark.

`FounderArtifacts.tsx`:
- maps `artifact.type` to local modules;
- reuses shared primitives for paths, gates, lanes, lifecycle, and decision cards;
- does not invent text beyond scene graph labels and approved preview labels.

`FounderSymbols.tsx`:
- exposes the 10 approved symbols:
  `bottleneck`, `path`, `lanes`, `gate`, `control`, `lifecycle`, `layer`,
  `node`, `binary`, `demo/demand`.

`founderTheme.ts`:
- locks A2 palette, typography stack, layout constants, safe areas, subtitle style,
  and animation timing helpers.

## Package Scripts

Add after implementation starts:

```json
"render:the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck": "remotion render src/index.ts the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck ../douyin/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/video.mp4"
```

Still/contact-sheet scripts should be added only after the video composition
exists and a cover/contact-sheet contract is drafted.

## Verification Plan

Before render approval:
- TypeScript compile succeeds.
- Composition is registered and inspectable through Remotion.
- All `c01` through `c19` audio files exist in `remotion/public/.../audio/`.
- Total frames equal `2019`.
- Subtitle treatment has no rectangle and does not collide with artifacts.
- Visual focus matches `focusPhrase` and `focusCue`.
- `Idea -> MVP -> Launch -> Scale` order is preserved.
- Sample stills/contact sheet are reviewed before final render.

## Risks

- `remotion/src/types.ts` currently models the older AI Agents scene graph. Use a
  local Founder Playbook type or safely extend the shared type without breaking
  existing compositions.
- Chinese subtitle lines may need per-scene fitting once rendered at `1080x1920`.
- The central artifact area must stay content-specific; do not regress into a
  repeated source-proof shelf.
- Audio paths must move into `remotion/public` before Remotion can load them with
  `staticFile()`.

## Pause

Implementation has been completed and verified at registration level. Stop here
until visual QA or sample still generation is approved.

## Implementation Result

Implemented files:
- `remotion/src/compositions/FounderPlaybookEpisode.tsx`
- `remotion/src/components/founder-playbook/FounderFrame.tsx`
- `remotion/src/components/founder-playbook/FounderArtifacts.tsx`
- `remotion/src/components/founder-playbook/FounderSymbols.tsx`
- `remotion/src/components/founder-playbook/founderTheme.ts`
- `remotion/src/components/founder-playbook/types.ts`

Modified files:
- `remotion/src/Root.tsx`
- `remotion/package.json`

Copied assets:
- `remotion/public/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/audio/c01.wav` through `c19.wav`

Verification:
- TypeScript: `npm exec tsc -- --noEmit` passed.
- Audio assets: exact selected `c01.wav` through `c19.wav` set present.
- Remotion composition registry: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`, `1080x1920`, `2019` frames, `67.30s`.
