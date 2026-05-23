# Harness Engineering Shotlist V2

## Format
- 9:16 vertical video.
- Target duration: about 110-130 seconds after OpenAI TTS generation.
- Anthropic-like editorial style: warm paper, ink typography, clay/ochre/moss accents, thin rules, structured diagrams.
- Works without sound because each scene carries the main message visually.

## Scene Plan
| Scene | Visual | Spoken Purpose | On-Screen Text |
|---:|---|---|---|
| 01 | Editorial warning cover | Hook the production-risk problem | AI 最大风险不是写错代码，是错代码上线 |
| 02 | Inner-loop diagram | Define Coding Agent scope | Coding Agent = 写 / 改 / 测 |
| 03 | Outer-loop diagram | Define Delivery Agent scope | Delivery Agent = 构建 / 扫描 / 审批 / 部署 / 回滚 / 审计 |
| 04 | API-key anti-pattern | Explain why permission alone is not governance | 不能只给 AI 一个 API key |
| 05 | Failure-mode cards | Add concrete risk details | prompt injection / wrong action / looping damage |
| 06 | Brain vs harness | Establish mental model | 模型是大脑，Harness 是控制系统 |
| 07 | Knowledge graph | Explain memory layer beyond RAG | 不是普通 RAG，而是 Knowledge Graph |
| 08 | Live-state cards | Explain runtime context | incident / freeze / scan / on-call |
| 09 | Model → Harness → Delegate | Explain governed tools | 工具可以强大，但不能裸调 |
| 10 | Secret boundary | Explain enterprise execution boundary | 密钥不进模型，不进 prompt |
| 11 | Evidence chain | Explain validation and accountability | policy gate / scorecard / rollback / audit log |
| 12 | MCP + Skills stats | Preserve important source artifacts | 11 tools / 168 resources / 31 toolsets |
| 13 | Governed path | Summarize safe execution | AI 不绕过流程，它通过流程 |
| 14 | Takeaway | Final memory point | Delivery Harness 是安全上线控制平面 |

## Improvements Over V1
- Adds source-backed implementation details instead of only metaphor.
- Adds concrete failure modes.
- Adds MCP Server quantitative artifacts.
- Adds Delegate/secrets boundary.
- Adds evidence chain and live-context requirements.
- Fixes scene 07/13 block overflow risk with shorter labels and larger block spacing.
