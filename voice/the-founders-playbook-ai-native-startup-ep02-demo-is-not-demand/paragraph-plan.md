# Paragraph Plan

Slug: `the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand`

## Gate Status

- Stage: `Voice Design`
- Status: `paragraph plan completed`
- Pause required: `yes`
- Prior gate: `compression/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand.md`
- Target duration: `60-75 seconds`
- Next approved stage: `script draft / native Chinese expression gate`
- Not approved yet: `TTS`, `ASR`, `voice manifest`, `scene graph`, `render`

## Episode Voice Promise

Turn the EP02 mental model into a natural spoken Mandarin episode:

```text
Demo 可以帮你问问题，但不能替你证明有人要。
```

## Voice Constraints

- Keep one idea per paragraph.
- Do not use the unverified `42%` statistic.
- Do not mention Claude product surfaces unless used as source attribution; this episode should not sound like product training.
- Keep `Demo` if it remains natural; otherwise switch spoken form to `演示版` while visual text may keep `Demo`.
- Avoid `PMF` in narration. This is Idea-stage problem-solution fit, not MVP / PMF mechanics.
- Preserve the source distinction: prototype is a conversation prop, not validation.

## Paragraph Map

| Paragraph | Target | Core Idea | Speaking Intention | Tone | Pace | Primary Visual Focus | Source Value |
|---|---:|---|---|---|---|---|---|
| p01 | 0-9s | AI makes Demo creation fast, but false certainty is the risk. | Hook with a clean AI-era contrast. | Direct, slightly urgent | Fast opening, firm pause after contrast | fast Demo appears, evidence panel still empty | AI collapses idea-to-prototype distance |
| p02 | 9-24s | A Demo is not validation by itself. | Correct the most dangerous misunderstanding. | Grounded, corrective | Moderate, emphasize `不是证据` | Demo stamped as tool, not proof | prototype is not validation |
| p03 | 24-40s | Idea-stage exit is problem-solution fit. | Define what actually counts before MVP. | Clear, practical | Structured list rhythm | validation gate with three checks | problem real / solution fits / enough signal |
| p04 | 40-58s | User conversations create evidence when they reveal behavior and contradiction. | Give a usable interview rule without becoming a tutorial. | Practical, founder-to-founder | Slightly slower, examples breathe | evidence chips from conversation | customer discovery, disconfirming evidence |
| p05 | 58-72s | Use the Demo to expose pain, not collect compliments. | Land the takeaway and bridge to EP03. | Decisive, lighter bridge | Final question, then preview | split card: praise vs pain; next gate: scope | Demo as pressure-testing prop; bridge to MVP boundary |

## Paragraph Draft Intent

### p01

Function:
- Open from the EP01 bridge.
- Establish that AI speed is useful but dangerous when it creates false certainty.

Voice direction:

```text
AI 让你很快做出 Demo。真正危险的是，Demo 一出来，你就以为问题已经被验证了。
```

Visual focus:
- Idea card turns into Demo surface.
- Evidence panel remains empty.

### p02

Function:
- State the core correction: Demo is not evidence.
- Keep the language practical, not dismissive.

Voice direction:

```text
Demo 不是没用。它很有用，但它的用处不是证明你对了，而是帮你把问题问清楚。
```

Visual focus:
- Demo moves from `proof` lane to `conversation tool` lane.

### p03

Function:
- Preserve source exit criteria.
- Make problem-solution fit concrete without saying `PMF`.

Voice direction:

```text
这一关要判断三件事：问题是不是真实、具体、经常发生；你的方案是不是解决了真实问题；信号够不够支持你进入 MVP。
```

Visual focus:
- Three gate checks reveal.

### p04

Function:
- Turn evidence into user conversation behavior.
- Include disconfirming evidence without over-teaching.

Voice direction:

```text
所以别只问“你会不会用”。要问他上一次什么时候遇到，今天怎么解决，哪里还是不愿意换。
```

Visual focus:
- Weak question fades; evidence questions appear.

### p05

Function:
- Land practical takeaway.
- Bridge to Episode 3.

Voice direction:

```text
如果用户只是在夸 Demo，你还没有答案。如果他开始暴露真实痛点，才值得继续。下一集再看：确定要做以后，为什么要先定边界，再让 AI 写。
```

Visual focus:
- `夸 Demo` dims; `暴露痛点` highlights; next gate preview `边界`.

## Source Fidelity Notes

Pass:
- Keeps Idea stage separate from MVP and Launch.
- Uses problem-solution fit without overloading with PMF.
- Treats Demo as useful but not proof.
- Preserves disconfirming evidence as a source-backed guardrail.

Risk:
- `Demo 是道具` may sound dismissive in full narration. Prefer softer lines: `Demo 是用来问问题的`.
- p03 can become too list-heavy. Let visuals carry the three checks if voice feels dense.

## Next Milestone

Create `script-draft.md`, run the native Chinese expression gate, then lock `script.md` if the draft passes with fixes.
