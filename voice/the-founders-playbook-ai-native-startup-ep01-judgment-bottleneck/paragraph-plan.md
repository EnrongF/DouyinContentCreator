# The Founder's Playbook EP01 - Voice Design

Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`

## Gate Status

- Stage: `voice manifest`
- Status: `Pass; manifest created`
- Pause required: `yes`
- Prior gate: `compression/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.md`
- Working title: `AI 创业，真正卡的是判断`
- Target duration: `60-75 seconds`
- Expression gate: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/native-chinese-expression-gate.md`
- Expression status: `Pass with fixes`
- Script draft: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/script-draft.md`
- Script review: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/script-review.md`
- Locked script: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/script.md`
- Speech chunk plan: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/speech-chunk-plan.md`
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

## Voice Design Objective

Design a spoken structure that explains one mental upgrade:

```text
AI accelerates execution, so founder judgment becomes the exposed bottleneck.
```

Chinese working claim:

```text
AI 不是让创业不需要执行，而是把执行变快以后，让创始人的判断更快暴露出来。
```

Compression model to test in voice:

```text
AI 是加速器，不是方向盘。
```

This is still **not final script**. The next gate must check whether the metaphor and wording sound natural in Mandarin voiceover.

## Paragraph Plan

| Paragraph | Target | Core Idea | Speaking Intention | Tone | Pace | Primary Visual Focus | Source Value |
|---|---:|---|---|---|---|---|---|
| p01 | 0-8s | Old fear vs new fear. | Hook the viewer with a native contrast. | Direct, slightly urgent | Fast opening, clean pause after contrast | old bottleneck vs new bottleneck | execution compression |
| p02 | 8-22s | AI speeds up execution work. | Ground the claim in concrete work types. | Calm, explanatory | Medium | research / code / docs / ops lanes accelerating | AI compresses research, coding, documents, operations |
| p03 | 22-38s | Speed exposes judgment. | State the mental upgrade without overclaiming. | Firm, reflective | Slightly slower | fast lanes converge at founder decision gate | founder role shifts upward |
| p04 | 38-60s | Four lifecycle gates test four judgments. | Preserve source taxonomy while previewing later episodes. | Structured, measured | List rhythm, short pauses | Idea / MVP / Launch / Scale gates | source lifecycle |
| p05 | 60-75s | Takeaway and series bridge. | Leave the viewer with one decision question. | Settled, forward-looking | Slow final beat | highlighted decision question | same job, new rules |

## Paragraph Voice Candidates

These are expression candidates, not final narration.

### p01 Hook Contrast

Preferred:

```text
以前创业，最怕东西做不出来。现在更怕做得太快，方向却错了。
```

Backup:

```text
以前创业卡在执行。现在有了 AI，很多时候是判断先出问题。
```

Avoid:

```text
AI 让创业的执行瓶颈消失了。
```

Reason: overclaims and implies execution no longer matters.

### p02 Execution Acceleration

Candidate:

```text
调研、写代码、写文档、做运营，这些事都可以被 AI 推快。
```

Backup:

```text
AI 能把很多原本很慢的工作压缩掉：调研更快，代码更快，文档和运营也更快。
```

Avoid:

```text
AI 原生创业全面压缩执行链路。
```

Reason: sounds written and abstract.

### p03 Judgment Bottleneck

Preferred:

```text
但速度上来以后，真正暴露出来的，是创始人有没有判断清楚。
```

Backup:

```text
做得快不是问题，问题是你是不是在把错误方向越做越快。
```

Metaphor candidate:

```text
AI 更像加速器，不是方向盘。
```

Voice risk:
- This metaphor is memorable, but it may sound slogan-like if repeated. Use once at most.

### p04 Lifecycle Preview

Candidate:

```text
Idea 阶段，判断值不值得做。MVP 阶段，判断边界清不清楚。Launch 以后，判断能不能不靠创始人硬接。Scale 阶段，判断有没有沉淀别人拿不走的业务细节。
```

Shorter backup:

```text
从想法，到 MVP，到上线，再到规模化。
每个阶段，考的判断都不一样。
```

Voice risk:
- Full version may be too dense. If it pushes pacing, use the shorter backup and let visuals carry the four labels.

### p05 Takeaway

Preferred:

```text
所以，用 AI 创业之前，先别急着问怎么更快。先问一句：现在缺的是速度，还是判断？
```

Backup:

```text
下一集，我们先看第一个判断：有 Demo，为什么还不代表有人要。
```

## Speaking Intention By Paragraph

### p01

- Intention: create the tension without sounding sensational.
- Emotion: alert but controlled.
- Breath: one clear pause after `方向却错了`.
- Blocker: if it sounds like "AI makes startups dangerous" rather than "speed amplifies judgment", rewrite.

### p02

- Intention: make the AI-native shift concrete.
- Emotion: practical.
- Breath: list rhythm for `调研、写代码、写文档、做运营`.
- Blocker: if it becomes an AI tool promo, rewrite.

### p03

- Intention: land the mental upgrade.
- Emotion: serious but not dramatic.
- Breath: slow slightly on `判断清楚`.
- Blocker: if `加速器 / 方向盘` feels too slogan-like, remove the metaphor.

### p04

- Intention: preview the series and protect source taxonomy.
- Emotion: structured.
- Breath: short pause after each lifecycle label.
- Blocker: if it becomes four lessons instead of four gates, shorten.

### p05

- Intention: turn the episode into a usable question.
- Emotion: settled, useful.
- Breath: pause before the final question.
- Blocker: if the bridge feels like marketing, keep only the decision question.

## Native Chinese Risks

- `执行压缩` is acceptable as an internal concept, but should not dominate spoken copy.
- `判断瓶颈` is understandable but abstract. Prefer `真正卡的是判断` or `有没有判断清楚`.
- `AI-native` should usually be spoken as `AI 原生` or avoided in the sentence.
- `Launch` and `Scale` can be visual labels; spoken Chinese should explain them naturally when needed.
- Avoid long noun stacks such as `AI-native 创业执行压缩后的判断瓶颈迁移`.

## Voice Design Decision

Pass to **Native Chinese Expression Gate**.

Gate questions for next stage:
- Does `AI 是加速器，不是方向盘` sound native enough, or should it stay only as a visual metaphor?
- Should p04 use the full four-gate sentence or the shorter lifecycle preview?
- Does the final question `现在缺的是速度，还是判断？` preserve the source claim without sounding too abstract?
