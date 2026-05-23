# Script

Voice direction: calm executive documentary, natural Mandarin, measured but not slow. Keep English terms clear.

多智能体的重点不是多几个 Agent，而是任务真的需要多个专业视角一起协调。

只有当单个 Agent 遇到明显限制，比如领域太宽、上下文太长、需要并行探索，才值得考虑 Multi-Agent。

原文里的 hierarchical pattern 属于集中式多智能体协调。Supervisor 决定调用哪些子 Agent，适合需要控制和汇总的任务。

Collaborative pattern 没有一个固定中心，多个专业 Agent 直接沟通、协商角色、共享上下文。灵活性更高，治理难度也更高。

PDF 提醒，Multi-Agent 可能消耗单 Agent 大约 10 到 15 倍 Token。只有任务价值足够高，这个成本才合理。

原文提到复杂任务中多智能体可能比单智能体高 90.2%，但前提是任务需要多个独立方向。简单问题不该触发昂贵协调。

多智能体失败时，不只要看每个 Agent 做了什么，还要看它们怎么沟通、怎么交接、怎么综合结论。

第三集的结论是：先证明 Single Agent 不够，再证明协调成本值得，最后才选 hierarchical 或 collaborative。
