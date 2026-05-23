# Pronunciation And Term Handling

Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`

## Status

- Stage: `Pronunciation / Symbol Rewrite`
- Status: `locked into voice manifest`
- Prior gate: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/speech-chunk-plan.md`
- Next approved stage: `scene graph`
- TTS and ASR have passed using the current rewrite table.

## Term Handling

| Visual term | Preferred spoken form | Notes |
|---|---|---|
| `AI-native` | avoid in Episode 1, or `AI 原生` if required | Use sparingly. Prefer natural Chinese sentences over repeated mixed-language terms. |
| `The Founder's Playbook` | avoid in narration | Source attribution should be handled visually later if needed. |
| `Idea` | `想法` | Visual label can stay `Idea`; spoken line should prefer Chinese. |
| `MVP` | `M V P` | Spell letters clearly in TTS input. Subtitle and visuals stay `MVP`. |
| `Launch` | `上线` or `上线以后` | Prefer Chinese-first voice. |
| `Scale` | `规模化` or `规模化阶段` | Prefer Chinese-first voice. |
| `Claude` | avoid in Episode 1 | Do not mention unless source attribution becomes necessary. |
| `Claude Code` | avoid in Episode 1 | Product tutorial content is out of scope. |
| `PMF` | avoid in Episode 1 | Belongs to later validation / MVP episodes. |
| `Demo` | `Demo` | Common enough for this audience. If TTS mispronounces it, switch spoken form to `演示版` while keeping `Demo` in subtitles if needed. |

## Symbol And Label Handling

- `Idea -> MVP -> Launch -> Scale` should be visible as a visual sequence.
- Spoken form should not read the arrow symbol.
- Preferred spoken sequence:

```text
从想法，到 MVP，到上线，再到规模化。
```

Visual labels may still show `Idea`, `MVP`, `Launch`, `Scale`.

## TTS Input Rewrite

Use this table when generating audio. `Spoken text` and `subtitle text` may differ.

| Chunk | Locked script text | TTS input text | Subtitle text |
|---|---|---|---|
| c03 | `调研、写代码、写文档、做运营，AI 都能帮你提速。` | `调研、写代码、写文档、做运营，A I 都能帮你提速。` | `调研、代码、文档、运营，AI 都能提速。` |
| c08 | `AI 这个工具，更像油门，不是方向盘。` | `A I 这个工具，更像油门，不是方向盘。` | `AI 更像油门，不是方向盘。` |
| c12 | `所以用 AI 创业，起点不是工具，而是一连串判断。` | `所以用 A I 创业，起点不是工具，而是一连串判断。` | `用 AI 创业，起点不是工具，是一连串判断。` |
| c13 | `从想法，到 M V P，到上线，再到规模化。` | `从想法，到 M V P，到上线，再到规模化。` | `从想法，到 MVP，到上线，再到规模化。` |
| c17 | `所以，用 AI 创业之前，先别急着问怎么更快。` | `所以，用 A I 创业之前，先别急着问怎么更快。` | `用 AI 创业，先别急着问怎么更快。` |
| c19 | `下一集，我们先看第一关：有了 Demo，为什么还不代表有人要。` | `下一集，我们先看第一关：有了 Demo，为什么还不代表有人要。` | `下一集：有 Demo，为什么还不代表有人要。` |

## Punctuation For TTS

- Keep Chinese commas after `所以` and `但` to force a small breath.
- Keep the colon in c18 and c19 to create a setup pause.
- Do not read arrows such as `->`; convert to `到` in speech.
- Do not speak slash labels such as `油门 / 方向盘`; use the full sentence `油门，不是方向盘`.
- Keep `M V P` spaced in TTS input. Do not use `MVP` in the spoken input unless a voice test proves it reads naturally.

## Risk Terms

Avoid in voice unless rewritten:

```text
执行压缩
判断瓶颈迁移
创始人作为智能体编排者
AI-native 创业执行链路
```

Prefer:

```text
AI 把执行变快
真正卡的是判断
创始人要决定什么值得做
用 AI 创业
```

## Lock Decision

Pronunciation and symbol rewrite are locked in **voice-manifest.json**.

Scene graph work must use:
- chunk boundaries from `speech-chunk-plan.md`;
- TTS input rewrites from this file;
- subtitle text from `speech-chunk-plan.md`;
- selected Qwen `Ethan` audio chunks from `chunks-qwen/`;
- timing from `voice-manifest.json`.

If later listening QA finds awkward pronunciation for `M V P` or `Demo`, update this file and rerun only the affected chunks before render.
