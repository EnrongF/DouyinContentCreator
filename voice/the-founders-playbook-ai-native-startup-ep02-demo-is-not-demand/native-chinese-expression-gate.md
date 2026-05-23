# Native Chinese Expression Gate

Slug: `the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand`

## Gate Status

- Stage: `Native Chinese Expression Gate`
- Status: `Pass with fixes`
- Pause required: `yes`
- Prior gate: `voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/script-draft.md`
- Next approved stage: `locked script / speech chunk plan`
- Not approved yet: `TTS`, `ASR`, `voice manifest`, `scene graph`, `render`

## Verdict

`Pass with fixes`.

The draft is source-faithful and mostly natural, but needs small口播 fixes:

| Draft line | Decision | Reason / Fix |
|---|---|---|
| `在 Idea 阶段` | Fix | Say `在想法阶段`; keep `Idea` as optional visual label. |
| `第三，信号够不够支持你进入 MVP。` | Fix | For speech, use `进入 M V P` or `开始做 MVP`. Keep visual label `MVP`. |
| `哪里还是不愿意换？` | Fix | Slightly unclear by itself. Use `现在的办法哪里让他不愿意换？` or `为什么还不换？`. |
| `证明有人要` | Pass | Native, compact, and matches title. |
| `Demo 可以帮你问问题` | Pass | Softer than `Demo 是道具`; good for voice. |

## Locked Expression Choices

- Spoken `Idea`: `想法阶段`.
- Spoken `MVP`: `M V P` in TTS input if needed; subtitle and visual text use `MVP`.
- Spoken `Demo`: keep as `Demo`; if TTS is awkward later, switch spoken form to `演示版` while subtitles may keep `Demo`.
- Avoid `PMF` in this episode.
- Do not say `用户调研` repeatedly; use concrete phrases like `问用户`, `真实痛点`, `现在怎么解决`.

## Revised Voice Lines

Use these fixes in the locked script:

```text
在想法阶段，真正要过的不是“能不能做出来”，而是三件事。
```

```text
第三，信号够不够支持你开始做 MVP。
```

```text
现在怎么解决？为什么还不换？
```

## QA

Pass:
- Natural Chinese口播.
- No translation-shaped noun stacks.
- No stiff product vocabulary.
- English terms are limited and useful.
- Source meaning preserved.

Open risk for TTS:
- `Demo` and `MVP` pronunciation should be tested; regenerate only affected chunks if awkward.

## Next Milestone

Lock `script.md`, then create `speech-chunk-plan.md` and `pronunciation.md`.
