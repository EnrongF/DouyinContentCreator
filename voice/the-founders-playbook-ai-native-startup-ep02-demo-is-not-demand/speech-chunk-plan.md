# Speech Chunk Plan

Slug: `the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand`

## Gate Status

- Stage: `speech chunk plan`
- Status: `completed; ready for TTS approval`
- Pause required: `yes`
- Prior gate: `voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/script.md`
- Pronunciation lock: `voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/pronunciation.md`
- Target duration: `60-75 seconds`
- Estimated draft duration: `63-70 seconds`
- Next approved stage: `TTS production`
- Not approved yet: `TTS`, `ASR`, `voice manifest`, `scene graph`, `render`, `Douyin package`

## Chunk Rules Applied

- One chunk carries one performable spoken unit.
- Target chunk duration: `2-8 seconds`.
- Long ideas are split before TTS.
- Subtitle text is compact and may be shorter than spoken text.
- Final timing must follow measured audio later.

## Chunks

| Chunk | Paragraph | Est. sec | Spoken Text | TTS Input Note | Subtitle | Pause / Emphasis | Focus Phrase | Expected Visual Focus |
|---|---|---:|---|---|---|---|---|---|
| c01 | p01 | 3.0 | AI 让你很快做出 Demo。 | `A I` if needed | AI 很快做出 Demo。 | clean hook | 很快做出 Demo | idea turns into Demo |
| c02 | p01 | 5.0 | 但最危险的地方也在这里：演示版一出来，你很容易以为问题已经被验证了。 | use `演示版` for ASR clarity | Demo 一出来，很容易以为问题已验证。 | pause after `这里` | 问题已经被验证了 | evidence panel remains empty |
| c03 | p02 | 3.0 | 其实，Demo 不是没用。它很有用。 | keep `Demo` | Demo 不是没用，它很有用。 | reassure, not dismissive | 很有用 | Demo stays visible |
| c04 | p02 | 5.5 | 但它不是用来证明你对了，而是用来帮你问清楚：这个问题到底是不是真的存在。 | slight pause before contrast | 它不是证明你对了，而是帮你问清楚。 | contrast emphasis | 问清楚 | Demo shifts to question tool |
| c05 | p03 | 4.2 | 在想法阶段，真正要过的不是“能不能做出来”，而是三件事。 | avoid `Idea` in speech | 想法阶段，真正要过的是三件事。 | measured setup | 三件事 | validation gate appears |
| c06 | p03 | 3.8 | 第一，问题是不是真实、具体，而且经常发生。 | none | 问题是否真实、具体、经常发生。 | list rhythm | 真实、具体、经常发生 | check one highlights |
| c07 | p03 | 4.8 | 第二，你的方案是不是解决了用户真正的问题，而不是你一开始想象的问题。 | none | 方案是否解决了真正的问题。 | emphasize `真正` | 用户真正的问题 | check two highlights |
| c08 | p03 | 3.8 | 第三，信号够不够支持你开始做 MVP。 | `M V P` if needed | 信号是否足够支持开始做 MVP。 | firm | 开始做 MVP | check three highlights |
| c09 | p04 | 3.2 | 所以，别只问用户：“你会不会用？” | quoted question clear | 别只问：“你会不会用？” | slight skepticism | 你会不会用 | weak question dims |
| c10 | p04 | 5.5 | 更好的问题是：你上一次遇到这个问题是什么时候？现在怎么解决？为什么还不换？ | question cadence | 上次什么时候遇到？现在怎么解决？为什么还不换？ | three question rhythm | 上一次 / 现在 / 为什么 | evidence questions appear |
| c11 | p05 | 3.5 | 如果用户只是在夸 Demo，你还没有答案。 | keep `Demo` | 只是在夸 Demo，还没有答案。 | firm | 没有答案 | praise lane dims |
| c12 | p05 | 5.2 | 如果他开始暴露真实痛点，甚至指出你的 Demo 哪里没解决问题，那才是更有价值的信号。 | keep `Demo` | 暴露真实痛点，才是更有价值的信号。 | slow on `真实痛点` | 真实痛点 | pain / contradiction chips highlight |
| c13 | p05 | 4.2 | 这一集的判断是：Demo 可以帮你问问题，但不能替你证明有人要。 | keep `Demo` | Demo 可以帮你问问题，不能证明有人要。 | takeaway emphasis | 不能替你证明有人要 | final decision card |
| c14 | p05 | 4.5 | 下一集，我们看确定要做以后，为什么要先定边界，再让 AI 写。 | `A I` if needed | 下一集：先定边界，再让 AI 写。 | bridge, lighter tone | 先定边界 | Episode 3 gate preview |

## Pronunciation Flags

| Chunk | Term | Handling |
|---|---|---|
| c01, c14 | `AI` | TTS input may use `A I`; subtitle and visual text use `AI`. |
| c01, c03-c04, c11-c13 | `Demo` | Keep as `Demo`; switch to `演示版` if TTS mispronounces. |
| c02 | `Demo` | Spoken as `演示版` after ASR misread; subtitle stays `Demo`. |
| c08 | `MVP` | TTS input may use `M V P`; subtitle and visual text use `MVP`. |

## Chunk QA

Pass:
- No chunk is expected to exceed 8 seconds.
- Each chunk has one focus phrase.
- Subtitle text is shorter or simpler than spoken text.
- The episode stays on Idea-stage validation, not PMF.
- The EP03 bridge points to boundary/context without teaching it here.

Open risks before TTS:
- c02 is the densest chunk; split after `这里` if TTS sounds rushed.
- c10 has three questions; keep it only if the generated cadence is natural.
- c12 may need a slightly slower take to make `真实痛点` land.

## Next Milestone

Run TTS only after approval.

That milestone should:
- generate Qwen `Ethan` chunk takes;
- measure durations;
- run ASR QA;
- build `voice-manifest.json`;
- stop before scene graph unless voice manifest passes.
