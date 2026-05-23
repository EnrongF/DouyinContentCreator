# Harness Engineering Sources

## Research Objective
Explain "Harness engineering" as agent harness engineering for software delivery: the system around AI models that controls memory, context, tools, permissions, execution, verification, and auditability when agents act in CI/CD and production delivery workflows.

## Assumption
"Harness engineering" is interpreted as Harness's software delivery platform and agent harness architecture, not electrical wiring harness engineering.

## Final Source Bundle
| Source | Date / Version | Type | Decision | Why Included |
|---|---:|---|---|---|
| [AI writes the code. Who delivers it safely?](https://www.harness.io/blog/ai-writes-the-code-who-delivers-it-safely) | Apr 30, 2026 | Primary, first-party technical essay | Include | Best framing source. Defines an agent harness as the system around the model: memory, context, tools, permissions, failure handling, governance, and verification. |
| [Harness AI DevOps Agent](https://developer.harness.io/docs/platform/harness-ai/devops-agent/) | Last updated Apr 30, 2026 | Official documentation | Include | Concrete product behavior for DevOps Agent: pipeline generation, troubleshooting, GitOps operations, OPA policy generation, privacy and data handling. |
| [Harness MCP Server](https://developer.harness.io/docs/platform/harness-ai/harness-mcp-server/) | Last updated Apr 23, 2026 | Official documentation | Include | Core architecture for AI-agent access to Harness: MCP tools, resource types, prompt templates, dynamic discovery, and transport options. |
| [harness/mcp-server](https://github.com/harness/mcp-server) | Active 2026 repo | Official source code | Include | Implementation artifact. README describes 11 consolidated tools, 168 resource types, 31 toolsets, transport modes, and registry-based dispatch. |
| [Harness Skills](https://developer.harness.io/docs/platform/harness-ai/harness-skills/) | Last updated Apr 29, 2026 | Official documentation | Include | Shows how Harness wraps MCP with agent instructions for Claude Code, Cursor, GitHub Copilot, and other assistants. |
| [harness/harness-skills](https://github.com/harness/harness-skills) | Active 2026 repo | Official source code | Include | Implementation artifact for reusable AI skills that create, operate, debug, and govern Harness workflows through natural language. |
| [Knowledge Graphs: The Backbone of AI-First Software Delivery](https://www.harness.io/blog/knowledge-graphs-for-ai-software-delivery) | Mar 17, 2026 | Primary, first-party technical blog | Include | Explains Software Delivery Knowledge Graph as context layer for AI-first delivery, guardrails, and operational reasoning. |
| [Knowledge Graph + RAG](https://www.harness.io/blog/knowledge-graph-rag) | Dec 17, 2025 | Primary, first-party technical blog | Include | Explains why RAG alone is insufficient for DevOps AI and why graph context improves grounding and automation reliability. |
| [Overview of Harness AI](https://developer.harness.io/docs/platform/harness-ai/overview/) | Last updated Apr 30, 2026 | Official documentation | Include | Taxonomy source for Harness AI features and scope. |

## Optional Support Sources
| Source | Decision | Reason |
|---|---|---|
| [Introducing Zero Trust Architecture for Software Delivery](https://www.harness.io/blog/introducing-zero-trust-architecture-for-software-delivery) | Optional | Good security/governance support, but less specific to agent harness engineering. |
| [Harness CD & GitOps Product Update](https://www.harness.io/blog/q1-2026-product-update-harness-continuous-delivery-gitops) | Optional | Useful for product freshness, but not core to harness architecture. |
| [Harness Platform Overview](https://developer.harness.io/docs/platform/get-started/overview/) | Optional | Useful background on RBAC, secrets, connectors, auditing, and notifications. |

## Rejected
| Source Type | Reason |
|---|---|
| SEO "best tools" or comparison pages | Derivative, often biased, and not original evidence. |
| Press releases | Too business-oriented for technical extraction. |
| Product pages without stable technical details | Useful for positioning only, not architecture. |
| Third-party MCP directories | Official docs and GitHub repos are available. |

## Source Risk
The source bundle is first-party-heavy. Treat claims as Harness's engineering thesis and product architecture, not independent market validation.
