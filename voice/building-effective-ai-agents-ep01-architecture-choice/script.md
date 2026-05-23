# Voice Script

Slug: `building-effective-ai-agents-ep01-architecture-choice`

Voice direction: calm executive documentary, natural Mandarin, measured but not slow. Keep English terms clear: Agent, Multi-Agent, Workflow, Single Agent, Token.

## Script

做 Agent 最容易犯的错，是从技术名词开始。

这份 Anthropic PDF 真正给出的，不是一个固定答案，而是一组架构选择。

先不要把概念混在一起。原文先讲 Single Agent，再讲 Multi-Agent 的协调概念，最后讲 Agentic Workflows。

Agentic Workflow 讲的是结构：任务如何排序、交接、并行和评估。它支撑架构，但不等于 Multi-Agent 的协调概念。

Single Agent 是一个 Agent 负责目标，用工具、技能和记忆推进任务。它可以调用流程，但核心仍是一个 Agent 的动态决策。

所以，目标清楚、路径需要动态选择，但还不需要多个专家一起处理时，先从 Single Agent 开始。

Multi-Agent 的核心不是顺序或并行，而是协调。原文先分集中式和去中心化：集中式里才有 hierarchical pattern。

但代价也很真实。PDF 提醒，Multi-Agent 可能消耗单 Agent 大约十到十五倍 Token。

所以架构选择，主要看五件事：控制要求、领域复杂度、资源预算、上线时间，以及需不需要领域专家参与。

一旦进入真实业务系统，还要能观察和治理：提示链、模型决策、检索上下文、Token 消耗，都要看得见。

第一集的结论是：先选最小可用架构，再保留演进空间。

下一集讲：怎么从一个窄而稳的 Agent 开始。
