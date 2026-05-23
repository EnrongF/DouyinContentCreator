# Harness Engineering Douyin Script

## Target Audience
- AI builders, developer-tool users, software teams, and technical founders who already know coding agents but have not thought deeply about production delivery agents.

## One-Sentence Promise
AI can write code fast, but it cannot safely ship production software unless it has a delivery harness.

## Title Options
1. AI 写代码很快，但谁来安全上线？
2. Coding Agent 不是 Delivery Agent
3. 真正危险的不是 AI 写代码，是 AI 上生产
4. Agent 需要的不是更多权限，而是 Harness

## Hook Options
1. Harness Engineering 最近刷遍 AI 社群，但很多人还没弄懂，就已经开始转发、解读、甚至拿来命名项目。
2. 你以为 AI 最大的风险是写错代码？更大的风险是它把错代码上线。
3. Coding Agent 只会写代码，Delivery Agent 会碰生产、密钥和审批。
4. AI 不是不能上线生产，而是必须被一个 Harness 管住。
5. 模型是大脑，但 Harness 才是刹车、方向盘和黑匣子。

## Recommended Hook
Harness Engineering 最近刷遍 AI 社群，但很多人还没弄懂，就已经开始转发、解读、甚至拿来命名项目。

## 110-Second Spoken Script V2
你以为 AI 写错代码已经很危险？

更危险的是，它把错代码上线。

这就是 Harness engineering 的核心问题：Coding Agent 和 Delivery Agent 不是一回事。

Coding Agent 在内循环，主要做三件事：写代码、改代码、跑测试。

Delivery Agent 在外循环，碰到的是构建、扫描、审批、部署、回滚和审计。

外循环的危险在于，它连接生产系统、密钥、权限、合规和真实用户。

所以问题不是“AI 能不能部署”，而是“AI 的每一步，谁来约束和证明”。

如果只是给 AI 一个 API key，它就绕过了原来的审批、策略和审计链路。

没有 harness，常见失败会很具体：PR 描述里的 prompt injection，恶意依赖，错误的 Kubernetes 配置，反复 rollback 和 redeploy。

速度越快，错误扩散越快。

真正需要的是 delivery harness。

模型是大脑，harness 是控制平面。

第一层是记忆，不是普通 RAG，而是 software delivery knowledge graph。

它要知道服务、团队、流水线、环境、策略、事故、依赖之间的关系。

第二层是实时上下文：现在有没有故障，有没有冻结窗口，最近扫描有没有风险，谁在 on-call。

第三层是受控工具：部署、回滚、feature flag、扫描、审批，都不能让模型直接裸调接口。

执行应该发生在企业边界内，比如通过 Delegate。

密钥在 Delegate 内解密，不进模型上下文，不进模型供应商，也不进 prompt。

第四层是验证和证据。

Policy gate、scorecard、approval、rollback、audit log，都要留下可追踪证据。

Harness MCP Server 的价值在这里：它不是把所有 API 暴露给 AI。

它把复杂平台收敛成更少的受控工具和资源。

公开资料里，Harness MCP Server 已经覆盖十一类工具、一百六十八种资源类型、三十一组 toolsets。

Skills 的作用，是把人的意图翻译成正确的交付操作。

所以未来不是让 AI 直接操作生产。

而是：AI 负责推理，Harness 负责约束、执行和证明。

一句话：模型是大脑，delivery harness 是安全上线的控制平面。

## 85-Second Spoken Script V1
你以为 AI 最大的风险是写错代码？

更大的风险是：它把错代码上线。

这就是 Harness engineering 想解决的问题。

Coding Agent 负责内循环：写代码、改代码、跑测试。

但 Delivery Agent 负责外循环：构建、扫描、审批、部署、回滚、留审计证据。

外循环碰到的是生产系统、密钥、权限和合规，所以不能只是“给 AI 一个 API key”。

真正需要的是一个 delivery harness。

模型是大脑，harness 是控制系统。

它要提供四件事：

第一，记忆。比如 software delivery knowledge graph，知道服务、流水线、环境、策略和事故之间的关系。

第二，实时上下文。比如现在有没有故障、冻结窗口、风险扫描。

第三，受控工具。部署、回滚、开 feature flag，都要走权限和策略。

第四，验证和证据。审批、scorecard、rollback、audit log 都要留下。

所以未来不是“让 AI 直接操作生产”。

而是：AI 负责推理，Harness 负责约束、执行和证明。

一句话：模型是大脑，delivery harness 是安全上线的控制平面。

## 30-Second Cut
AI 写代码很快，但真正危险的是它把错代码上线。

Coding Agent 只负责写代码，这是内循环。

Delivery Agent 会碰生产、密钥、审批、部署和回滚，这是外循环。

所以它不能只有 API 权限，它需要一个 delivery harness。

模型是大脑，harness 是控制系统。

它提供记忆、实时上下文、受控工具、验证和审计证据。

未来不是让 AI 直接上生产，而是让 AI 的每个动作都经过可治理的交付控制平面。

## Claims That Must Not Be Overstated
- Do not claim Harness is the only way to do this.
- Do not claim autonomous production deployment is automatically safe.
- Do not present Harness first-party claims as independent market proof.
- Do not imply MCP alone solves governance; MCP needs permissions, policy, execution boundaries, and verification.
