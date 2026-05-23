# Pronunciation

Slug: `the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand`

## Gate Status

- Stage: `pronunciation lock`
- Status: `draft completed for TTS preparation`
- Pause required: `yes`
- Prior gate: `voice/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand/script.md`
- Next approved stage: `TTS only after approval`
- Not approved yet: `TTS`, `ASR`, `voice manifest`, `scene graph`, `render`

## Term Handling

| Term | Spoken handling | Subtitle / visual handling | Note |
|---|---|---|---|
| `AI` | `A I` in TTS input if needed | `AI` | Same handling as EP01. |
| `Demo` | `Demo` | `Demo` | Common enough for target audience; switch to `演示版` only if TTS sounds awkward. |
| `MVP` | `M V P` in TTS input | `MVP` | Spell letters clearly if generated voice misreads it. |
| `Idea` | `想法阶段` | optional `Idea / 想法` | Prefer Chinese in speech. |
| `PMF` | avoid | avoid | Belongs to later MVP / measurement work. |

## TTS Input Notes

Potential replacements for generated TTS:

| Chunk | Script text | TTS input candidate | Subtitle |
|---|---|---|---|
| c01 | `AI 让你很快做出 Demo。` | `A I 让你很快做出 Demo。` | `AI 让你很快做出 Demo。` |
| c02 | `Demo 一出来` | `演示版一出来` | `Demo 一出来，很容易以为问题已验证。` |
| c08 | `第三，信号够不够支持你开始做 MVP。` | `第三，信号够不够支持你开始做 M V P。` | `信号够不够支持你开始做 MVP。` |
| c14 | `下一集，我们看确定要做以后，为什么要先定边界，再让 AI 写。` | `下一集，我们看确定要做以后，为什么要先定边界，再让 A I 写。` | `下一集：先定边界，再让 AI 写。` |

## Pause / Breath Notes

- Pause after the opening `Demo` hook so the contrast lands.
- Slight pause before `不是用来证明你对了`.
- Give each of the three validation checks its own breath.
- Slow down on `真实痛点`.
- Keep the final bridge lighter than the main takeaway.

## QA

Pass:
- No hard-to-pronounce product names.
- No `PMF`.
- `Demo`, `AI`, and `MVP` have explicit fallback handling.

Open risk:
- c02 uses `演示版` after ASR misread `Demo`; other Demo chunks remain acceptable if ASR passes.
