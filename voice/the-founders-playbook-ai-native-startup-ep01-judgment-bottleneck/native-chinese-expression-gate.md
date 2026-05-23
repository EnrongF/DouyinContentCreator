# Native Chinese Expression Gate

Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`

## Gate Status

- Stage: `Native Chinese Expression Gate`
- Status: `Pass with fixes`
- Pause required: `yes`
- Prior gate: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/paragraph-plan.md`
- Next approved stage: `Script Draft`
- Not approved yet: `speech chunk plan`, `TTS`, `ASR`, `voice manifest`, `scene graph`, `visual production`, `render`

## Verdict

The voice structure passes, but several expressions need fixes before script drafting.

Main decision:

```text
Use spoken Chinese first.
Keep English lifecycle labels mostly visual.
Avoid abstract internal terms in narration.
```

## Line-Level Decisions

| Item | Current / candidate | Verdict | Fix |
|---|---|---|---|
| Title | `AI 创业，真正卡的是判断` | Pass | Usable as title. In narration, prefer `真正卡住人的，是判断`. |
| Core claim | `AI 不是让创业不需要执行，而是把执行变快以后，让创始人的判断更快暴露出来。` | Fix | `AI 不是替你省掉执行，而是让执行变快，让判断更早露出来。` |
| Mental model | `AI 是加速器，不是方向盘。` | Fix | `AI 这个工具，更像油门，不是方向盘。` Use once at most. |
| p01 | `以前创业，最怕东西做不出来。现在更怕做得太快，方向却错了。` | Fix | `以前创业，最怕的是做不出来。现在更怕的是，做得很快，但方向错了。` |
| p02 | `调研、写代码、写文档、做运营，这些事都可以被 AI 推快。` | Fix | `调研、写代码、写文档、做运营，AI 都能帮你提速。` |
| p03 | `但速度上来以后，真正暴露出来的，是创始人有没有判断清楚。` | Fix | `但速度一上来，创始人到底有没有想清楚，会被放大得更明显。` |
| p03 backup | `做得快不是问题，问题是你是不是在把错误方向越做越快。` | Pass with minor fix | `做得快不是问题，问题是方向错了以后，你会错得更快。` |
| p04 full | `Idea 阶段，判断值不值得做...` | Fix | Too dense for voice. Use shorter spoken version and let visuals carry the labels. |
| p04 short | `从 Idea 到 MVP，再到 Launch 和 Scale，每一关考的都不是同一种判断。` | Fix | `从想法，到 MVP，到上线，再到规模化。每个阶段，考的判断都不一样。` |
| p05 | `所以，用 AI 创业之前，先别急着问怎么更快。先问一句：现在缺的是速度，还是判断？` | Pass | Good final question. Keep. |

## Approved Voice Inputs For Script Draft

These lines are approved as script inputs, not final locked narration.

### p01 Hook

```text
以前创业，最怕的是做不出来。
现在更怕的是，做得很快，但方向错了。
```

### p02 Execution Acceleration

```text
调研、写代码、写文档、做运营，AI 都能帮你提速。
```

### p03 Judgment Shift

```text
但速度一上来，创始人到底有没有想清楚，会被放大得更明显。
```

Optional metaphor:

```text
AI 这个工具，更像油门，不是方向盘。
```

Use once at most. If it makes the narration feel like a slogan, remove it.

### p04 Lifecycle Preview

Preferred spoken form:

```text
从想法，到 MVP，到上线，再到规模化。
每个阶段，考的判断都不一样。
```

Visual labels may still show:

```text
Idea
MVP
Launch
Scale
```

Do not force all English labels into voice.

### p05 Takeaway

```text
所以，用 AI 创业之前，先别急着问怎么更快。
先问一句：现在缺的是速度，还是判断？
```

## Expression Guardrails For Script Draft

Avoid:

```text
执行压缩
判断瓶颈迁移
AI-native 创业执行链路
创始人作为智能体编排者
更容易把错东西做得很完整
```

Prefer:

```text
AI 把执行变快
真正卡住人的，是判断
创始人要决定什么值得做
方向错了以后，会错得更快
用 AI 创业
```

## Pronunciation Decision

- `AI`: speak as `A I`.
- `MVP`: speak as `M V P`; if the sentence is too mixed, use `最小可用产品`.
- `Idea`: prefer `想法`; keep `Idea` visual if useful.
- `Launch`: prefer `上线`.
- `Scale`: prefer `规模化`.
- `AI-native`: avoid in Episode 1 narration unless source framing requires it.
- `Claude`, `Claude Code`, `PMF`: avoid in Episode 1 narration.

## Gate Notes

Pass conditions for script draft:
- The script may use the approved inputs above.
- The script must stay under one mental model.
- The lifecycle preview must not become four mini-lessons.
- No unverified statistics, product claims, or startup examples may be added.

Blocking conditions:
- If final script reintroduces stiff translated terms, rerun this gate.
- If English labels dominate the voice, rerun this gate.
- If `油门 / 方向盘` becomes the whole explanation rather than a supporting metaphor, simplify.
