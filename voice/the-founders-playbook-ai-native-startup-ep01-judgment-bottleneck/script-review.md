# Script Review / Lock

Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`

## Gate Status

- Stage: `Script Review / Lock`
- Status: `Pass, locked with edits`
- Pause required: `yes`
- Prior gate: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/script-draft.md`
- Locked script: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/script.md`
- Next approved stage: `Speech Chunk Plan`
- Not approved yet: `TTS`, `ASR`, `voice manifest`, `scene graph`, `visual production`, `render`

## Review Decisions

### 1. `油门 / 方向盘` metaphor

Decision: **keep, but clarify once**.

Reason:
- Native enough for spoken Chinese.
- More natural than `加速器 / 方向盘`.
- Must not become the whole explanation.

Locked handling:

```text
AI 这个工具，更像油门，不是方向盘。
它能让你跑得更快，但不能帮你决定往哪走。
```

### 2. Source attribution in narration

Decision: **remove spoken `这份创业 playbook` from the locked narration**.

Reason:
- It feels slightly unnatural in voice.
- Episode 1 does not need source attribution inside narration.
- Source attribution can be handled visually later without interrupting the spoken flow.

### 3. Lifecycle preview

Decision: **keep the short lifecycle preview**.

Reason:
- It preserves source taxonomy.
- It avoids turning Episode 1 into four mini-lessons.

Locked handling:

```text
从想法，到 M V P，到上线，再到规模化。
每个阶段，考的判断都不一样。
```

### 4. Episode 2 bridge

Decision: **keep the bridge, with natural phrasing**.

Locked handling:

```text
下一集，我们先看第一关：有了 Demo，为什么还不代表有人要。
```

## Checks

Native Chinese: `Pass`
- No translation-shaped noun stacks remain.
- English terms are minimized.
- `M V P` is retained because it is common and useful.

Source fidelity: `Pass`
- Execution still matters.
- AI accelerates execution.
- Judgment becomes exposed.
- Source lifecycle remains ordered.
- No unverified statistics, product claims, founder examples, PMF mechanics, technical debt details, launch system details, or moat mechanics were added.

Pacing: `Pass`
- Estimated target remains `60-75 seconds`.
- Paragraphs map cleanly to one idea and one visual focus each.

Open risk:
- TTS may make `M V P` sound too letter-by-letter mechanical. If so, speech chunk planning can choose `最小可用产品` for spoken voice while keeping `MVP` on screen.

## Lock Decision

Script is locked for **Speech Chunk Plan**.

Do not start TTS until:
- speech chunks are created;
- pronunciation is rechecked;
- chunk lengths are checked against the 2-8 second target where feasible.
