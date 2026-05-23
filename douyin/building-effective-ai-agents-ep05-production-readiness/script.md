# Script

Voice direction: calm executive documentary, natural Mandarin, measured but not slow. Keep English terms clear.

Agent 的风险不只是答错，而是你不知道它为什么这样做、用了什么上下文、调用了哪些工具。

AI 应用要看 prompt chains、model decision paths、retrieval context、Token consumption，以及整个 reasoning workflow。

多轮工具调用、检索结果、Agent 交接都会让上下文膨胀。上下文失控，Agent 的行为就会变得不可控。

原文提到 context editing、memory tools、pagination、filtering、truncation 和 token caps。这些不是优化项，是上线条件。

传统软件的错误路径通常可复现，但 Agent 的决策可能每次不同。生产系统必须记录、评估、限制和回滚。

不要只看模型分数。要看节省时间、错误率、人工接管率、客户体验和成本，指标必须能说明业务价值。

第一个门：任务边界清楚。第二个门：工具权限可控。第三个门：上下文可管理。第四个门：失败能被发现和接管。

第五集的结论是：生产级 Agent 不是先追求更聪明，而是先做到可见、可控、可接管。
