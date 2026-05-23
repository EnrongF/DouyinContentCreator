# Episode 6 Speech Chunk Plan

Slug: `building-effective-ai-agents-ep06-hybrid-emerging-patterns`

## Chunks

| Chunk | Paragraph | Spoken Text | Subtitle | Pause / Emphasis | Focus Phrase | Expected Visual Focus |
|---|---|---|---|---|---|---|
| c01 | p01 | 很多团队做 Agent，最后都会问一句：那我们是不是该上混合架构了？ | 很多团队最后都会问：该上混合架构了吗？ | small pause after `Agent` | 混合架构 | title + warning badge |
| c02 | p02 | 但 Anthropic 这份报告里，混合架构不是起点。 | 但在这份报告里，混合架构不是起点。 | emphasize `不是起点` | 不是起点 | ladder reset |
| c03 | p02 | 它更像是系统长大以后，才出现的组合形态。 | 它是系统长大以后出现的组合形态。 | slight pause after `以后` | 组合形态 | synthesis label |
| c04 | p03 | 比较稳的路线，是先做一个边界清楚的单 Agent。 | 稳的路线：先做边界清楚的单 Agent。 | calm | 单 Agent | single-agent source diagram |
| c05 | p03 | 等任务类型开始分叉，再加 routing，让不同请求走不同路径。 | 任务类型分叉，再加 routing。 | emphasize `分叉` | routing | router split animation |
| c06 | p04 | 如果问题真的跨了多个专业领域，再把能力拆成 specialist agents。 | 跨多个专业领域，再拆 specialist agents。 | pause after `领域` | specialist agents | specialist nodes |
| c07 | p04 | 让 supervisor 负责分派、汇总和兜底。 | supervisor 负责分派、汇总和兜底。 | compact | supervisor | supervisor hub |
| c08 | p05 | 再往后，才是把 workflow 结构接进来。 | 再往后，才接入 workflow 结构。 | slower | workflow 结构 | workflow layer appears |
| c09 | p05 | 独立分析可以并行跑；质量标准清楚的任务，可以加 evaluator 做反复优化。 | 并行分析，或加 evaluator 做优化。 | split with semicolon pause | evaluator | parallel + evaluator cards |
| c10 | p06 | 注意，这些不是同一层级的模式。 | 注意：这些不是同一层级的模式。 | firm | 不是同一层级 | taxonomy alert |
| c11 | p06 | hierarchical 是多智能体协调方式，parallel 和 evaluator 是工作流结构。 | hierarchical 是协调方式；parallel 和 evaluator 是工作流结构。 | careful pronunciation | 协调方式 / 工作流结构 | two-layer taxonomy |
| c12 | p06 | 混在一起用时，要标成 synthesis。 | 混在一起用，要标成 synthesis。 | emphasize `synthesis` | synthesis | synthesis stamp |
| c13 | p07 | 报告还提到 dynamic agent generation 和 peer-to-peer network。 | 报告还提到 dynamic generation 和 peer-to-peer network。 | steady | emerging patterns | experimental zone |
| c14 | p07 | 但它们属于 emerging patterns。适合探索，不适合一上来就当生产默认方案。 | 它们是 emerging patterns，不是生产默认方案。 | emphasize `不是生产默认方案` | emerging patterns | dashed caution frame |
| c15 | p08 | 所以判断要不要 hybrid，看四个信号。 | 判断要不要 hybrid，看四个信号。 | transition | 四个信号 | four-gate board |
| c16 | p08 | 单 Agent 已经有明确瓶颈；任务能自然拆开；质量和升级规则说得清。 | 瓶颈明确、任务可拆、规则说得清。 | list rhythm | 瓶颈 / 可拆 / 规则 | first three gates |
| c17 | p08 | 还有，团队扛得住 10 到 15 倍 token 成本、延迟和观测复杂度。 | 还要扛得住 10 到 15 倍 token 成本。 | slow on number | 10 到 15 倍 | cost gate turns amber |
| c18 | p09 | 一句话：混合架构不是高级感。 | 混合架构不是高级感。 | pause before final | 不是高级感 | final contrast |
| c19 | p09 | 它是证据逼出来的下一步。 | 它是证据逼出来的下一步。 | final hold | 证据逼出来 | evidence -> next step |
