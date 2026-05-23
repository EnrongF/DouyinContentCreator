# Speech Chunk Plan

Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`

## Gate Status

- Stage: `voice manifest`
- Status: `Pass; manifest created`
- Pause required: `yes`
- Prior gate: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/script.md`
- Target duration: `60-75 seconds`
- Estimated draft duration: `70-73 seconds`
- Pronunciation lock: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/pronunciation.md`
- TTS takes report: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/tts-takes.md`
- TTS provider: `qwen-dashscope`
- TTS voice: `Ethan`
- Measured speech duration: `61.440 seconds`
- TTS take selection: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/tts-take-selection.md`
- ASR QA: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/asr-qa.md`
- Voice manifest: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/voice-manifest.json`
- Voice QA: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/qa.md`
- Total timed duration with pauses: `67.300 seconds`
- Next approved stage: `scene graph`
- Not started yet: `visual production`, `render`

## Chunk Rules Applied

- One chunk carries one performable spoken unit.
- Target chunk duration: `2-8 seconds`.
- Long ideas are split before TTS.
- Subtitle text is compact and may be shorter than spoken text.
- Visual focus is planned, but final timing must follow measured audio later.

## Chunks

| Chunk | Paragraph | Est. sec | Spoken Text | Subtitle | Pause / Emphasis | Focus Phrase | Expected Visual Focus |
|---|---|---:|---|---|---|---|---|
| c01 | p01 | 3.0 | 以前创业，最怕的是做不出来。 | 以前最怕做不出来。 | small pause after `创业` | 做不出来 | blocked work lane |
| c02 | p01 | 4.0 | 现在更怕的是，做得很快，但方向错了。 | 做得很快，但方向错了。 | pause after `更怕的是` | 方向错了 | speed lane veers wrong |
| c03 | p02 | 5.5 | 调研、写代码、写文档、做运营，AI 都能帮你提速。 | 调研、代码、文档、运营，AI 都能提速。 | list rhythm | AI 都能帮你提速 | four execution lanes accelerate |
| c04 | p02 | 2.8 | 但它不是替你省掉执行。 | AI 不是省掉执行。 | emphasize `不是` | 不是省掉执行 | execution lane stays visible |
| c05 | p02 | 4.2 | 而是让执行变快，让判断更早露出来。 | 它让执行变快，让判断更早露出来。 | slow slightly on `判断` | 执行变快 / 判断更早露出来 | decision gate appears earlier |
| c06 | p03 | 2.0 | 做得快不是问题。 | 做得快不是问题。 | short, firm | 不是问题 | fast lane stays neutral |
| c07 | p03 | 3.8 | 问题是方向错了以后，你会错得更快。 | 方向错了以后，会错得更快。 | emphasize `错得更快` | 错得更快 | wrong path accelerates |
| c08 | p03 | 3.0 | AI 这个工具，更像油门，不是方向盘。 | AI 更像油门，不是方向盘。 | contrast emphasis | 油门 / 方向盘 | accelerator vs steering visual |
| c09 | p03 | 4.5 | 它能让你跑得更快，但不能帮你决定往哪走。 | 它能让你更快，但不能帮你决定往哪走。 | pause after `更快` | 帮你决定往哪走 | steering remains with founder |
| c10 | p03 | 4.2 | 真正卡住人的，是创始人有没有想清楚。 | 真正卡住人的，是有没有想清楚。 | slow on `想清楚` | 想清楚 | founder decision gate |
| c11 | p03 | 3.0 | 什么值得做，什么应该先停。 | 什么值得做，什么应该先停。 | balanced pair | 值得做 / 先停 | go / stop decision cards |
| c12 | p04 | 5.2 | 所以用 AI 创业，起点不是工具，而是一连串判断。 | 用 AI 创业，起点不是工具，是一连串判断。 | emphasize `不是工具` | 一连串判断 | gate sequence appears |
| c13 | p04 | 4.6 | 从想法，到 M V P，到上线，再到规模化。 | 从想法，到 MVP，到上线，再到规模化。 | spell `M V P` clearly | 想法 / MVP / 上线 / 规模化 | four lifecycle gates reveal |
| c14 | p04 | 3.2 | 每个阶段，考的判断都不一样。 | 每个阶段，判断都不一样。 | measured | 判断都不一样 | gates receive different icons |
| c15 | p04 | 2.8 | 第一关，是你到底该不该做。 | 第一关：到底该不该做。 | slight pause after `第一关` | 该不该做 | first gate highlights |
| c16 | p04 | 3.2 | 后面才轮到边界、系统和护城河。 | 后面才轮到边界、系统和护城河。 | compact list | 边界 / 系统 / 护城河 | later gates dimmed |
| c17 | p05 | 4.5 | 所以，用 AI 创业之前，先别急着问怎么更快。 | 用 AI 创业，先别急着问怎么更快。 | pause after `所以` | 别急着问怎么更快 | speed question card dims |
| c18 | p05 | 4.0 | 先问一句：现在缺的是速度，还是判断？ | 现在缺的是速度，还是判断？ | final question emphasis | 速度，还是判断 | final decision card |
| c19 | p05 | 5.0 | 下一集，我们先看第一关：有了 Demo，为什么还不代表有人要。 | 下一集：有 Demo，为什么还不代表有人要。 | bridge, lighter tone | 不代表有人要 | Episode 2 gate preview |

## Pronunciation Flags

| Chunk | Term | Handling |
|---|---|---|
| c03, c08, c12, c17 | `AI` | TTS input uses `A I`; subtitle and visual text use `AI`. |
| c13 | `M V P` | TTS input keeps spaced letters; subtitle and visual text use `MVP`. |
| c19 | `Demo` | Keep as `Demo`; if TTS mispronounces it, switch spoken form to `演示版` before ASR. |

## Chunk QA

Pass:
- No chunk is expected to exceed 8 seconds.
- Each chunk has one focus phrase.
- Subtitle text is shorter or equal in complexity to spoken text.
- The `油门 / 方向盘` metaphor is contained in two chunks and does not dominate the whole script.
- The lifecycle preview remains a preview, not four mini-lessons.

Open risks before TTS:
- c13 may sound awkward if `M V P` is over-enunciated.
- c19 may sound slightly mixed-language with `Demo`; test with TTS or replace with `原型` if needed.
- Estimated duration must be replaced by measured audio duration in `voice-manifest.json`.

## Next Milestone

Create the **scene graph**.

That milestone should:
- use `voice-manifest.json` as timing authority;
- map each chunk to visual focus states;
- preserve subtitle text and safe-area intent;
- keep source claims faithful;
- not start Remotion implementation or render work.
