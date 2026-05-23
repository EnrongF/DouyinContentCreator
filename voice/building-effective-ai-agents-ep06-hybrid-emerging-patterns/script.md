# Episode 6 Script

Slug: `building-effective-ai-agents-ep06-hybrid-emerging-patterns`

## Narration

很多团队做 Agent，最后都会问一句：那我们是不是该上混合架构了？

但 Anthropic 这份报告里，混合架构不是起点。它更像是系统长大以后，才出现的组合形态。

比较稳的路线，是先做一个边界清楚的单 Agent。等任务类型开始分叉，再加 routing，让不同请求走不同路径。

如果问题真的跨了多个专业领域，再把能力拆成 specialist agents，让 supervisor 负责分派、汇总和兜底。

再往后，才是把 workflow 结构接进来。独立分析可以并行跑；质量标准清楚的任务，可以加 evaluator 做反复优化。

注意，这些不是同一层级的模式。hierarchical 是多智能体协调方式，parallel 和 evaluator 是工作流结构。混在一起用时，要标成 synthesis。

报告还提到 dynamic agent generation 和 peer-to-peer network，但它们属于 emerging patterns。适合探索，不适合一上来就当生产默认方案。

所以判断要不要 hybrid，看四个信号：单 Agent 已经有明确瓶颈；任务能自然拆开；质量和升级规则说得清；还有，团队扛得住 10 到 15 倍 token 成本、延迟和观测复杂度。

一句话：混合架构不是高级感。它是证据逼出来的下一步。
