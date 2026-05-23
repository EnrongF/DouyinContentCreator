# Source Map

## Source
- Article: [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- Publisher: Anthropic
- Published: 2025-06-13

## Core Thesis
Anthropic argues that multi-agent systems are most valuable for open-ended research tasks that require breadth, parallel exploration, and more tokens than a single context window can comfortably hold. The article ties product performance to architecture, prompting, tool design, evaluation, and production reliability.

## Key Claims
- Multi-agent systems outperform single-agent systems on breadth-first research tasks because they can search in parallel and use separate context windows.
- In Anthropic’s internal research eval, Claude Opus 4 with Sonnet 4 subagents beat single-agent Opus 4 by 90.2%.
- Token budget is a major driver of performance; their analysis says token usage explains most of the variance in BrowseComp-style browsing work.
- Upgrading to Claude Sonnet 4 gave a larger gain than doubling the token budget on Sonnet 3.7, so model quality and token budget compound.
- Multi-agent systems are expensive: agents use about 4x more tokens than chat, and multi-agent systems use about 15x more tokens than chats.
- Multi-agent systems are best suited to tasks with high value, heavy parallelization, large external information surfaces, and tool-rich workflows.

## Article Examples
- Information Technology S&P 500 board-member query:
  - Multi-agent research succeeded by decomposing broad lookup work across subagents.
  - Single-agent research failed because sequential searches were too slow.
- Architecture diagram query:
  - Find all US companies working on AI agents in 2025 with at least 100 employees.
  - Include company name, website, product, agent types, and vertical or industry.
- Semiconductor shortage delegation failure:
  - Vague instructions caused one subagent to explore the 2021 automotive chip crisis while two duplicated work on current 2025 supply chains.
  - The fix is sharper subtask boundaries and clear source/tool guidance.

## Architecture Notes
- Pattern: orchestrator-worker.
- Lead agent:
  - Analyzes the user query.
  - Creates a research plan.
  - Spawns subagents in parallel.
  - Synthesizes findings.
  - Passes results to a citation agent.
- Subagents:
  - Search independently.
  - Use interleaved thinking after tool results.
  - Return compact findings to the lead agent.
- Citation agent:
  - Locates source spans for claims.
  - Ensures attribution before final answer delivery.

## Original Visual Artifacts
- High-level architecture diagram:
  - Shows Claude.ai chat sending a user request to the multi-agent research system.
  - Shows the lead agent as orchestrator with search tools, MCP tools, memory, run_subagent, and complete_task.
  - Shows search subagents looping independently and a separate citations subagent.
- Multi-agent system process diagram:
  - Shows User, System, LeadResearcher, Subagent1, Subagent2, Memory, and CitationAgent swimlanes.
  - LeadResearcher saves the plan to Memory because context can exceed 200,000 tokens.
  - Subagents perform web_search, think/evaluate after results, and complete_task back to the lead.
  - LeadResearcher decides whether more research is needed, then sends the report and documents to CitationAgent.
- Clio embedding plot:
  - Shows common Research use clusters.
  - Top categories include developing software systems across specialized domains (10%), professional and technical content (8%), business growth and revenue generation strategies (8%), academic research and educational material development (7%), and people/place/organization verification (5%).

## Prompting Principles
1. Think like the agent by watching live simulations and identifying failure modes.
2. Teach the orchestrator to delegate with clear objectives, output formats, and boundaries.
3. Scale effort to query complexity instead of treating all tasks the same.
4. Make tool design explicit and distinct so agents choose the right capability.
5. Let agents improve prompts and tools when they encounter failures.
6. Start wide, then narrow the search as evidence accumulates.
7. Guide the thinking process with extended thinking and interleaved thinking.
8. Use parallel tool calling to cut latency and increase coverage.

## Tool And MCP Lessons
- Tool descriptions are part of the system design surface.
- MCP servers can expose agents to unseen tools with uneven descriptions.
- Agents should inspect available tools before acting.
- Tool choice should match user intent and source location; searching the web for Slack-only context is the wrong plan.
- Claude 4 models can help diagnose failures and improve prompts or tool descriptions.

## Evaluation Principles
- Start with small eval sets as soon as possible.
- Use LLM-as-judge scoring for free-form research outputs.
- Judge outputs on:
  - factual accuracy
  - citation accuracy
  - completeness
  - source quality
  - tool efficiency
- Combine automated evaluation with human review because human testers catch source bias, hallucinations, and edge cases.
- Evaluate collaboration patterns, not only individual outputs, because small lead-agent prompt changes can unpredictably change subagent behavior.

## Production Reliability Lessons
- Agent failures compound because systems are stateful and long-running.
- Durable execution and checkpointing matter because restarts are expensive.
- Tool failure messages should be visible to the model so it can adapt, alongside deterministic retries and checkpoints.
- Production tracing is necessary to understand failure causes.
- Privacy-preserving observability should focus on decision patterns, not conversation contents.
- Rainbow deployments reduce disruption when updating running agents.
- Synchronous coordination simplifies orchestration but creates bottlenecks; async execution is a likely next step.

## Appendix Ideas Worth Reusing
- End-state evaluation is often better than turn-by-turn validation for stateful agents.
- Memory systems help preserve continuity across long-horizon tasks.
- Let subagents write durable artifacts directly to a filesystem or external store to reduce “game of telephone” loss.

## Extracted Numbers
- 90.2%: internal eval improvement for multi-agent over single-agent Opus 4.
- 95%: performance variance explained by token usage, number of tool calls, and model choice in the BrowseComp analysis.
- 80%: performance variance explained by token usage alone.
- 200,000 tokens: context-window threshold referenced in the process diagram memory step.
- Up to 90%: research time reduction for complex queries.
- 4x: token usage of agents versus chat interactions.
- 15x: token usage of multi-agent systems versus chats.
- 40%: completion-time reduction from improving tool descriptions.
- 20: approximate number of real-usage queries in Anthropic's early eval set.
- 30% to 80%: example success-rate swing from early prompt changes.
- 0.0-1.0: LLM judge scoring range used alongside a pass-fail grade.

## Reusable Concepts
- Research planning as a first-class artifact.
- Parallel search as a core capability, not an optimization.
- Citation generation as a separate stage.
- Evaluation as a continuous loop, not a one-time benchmark.
- Production observability tailored to agent behavior.
