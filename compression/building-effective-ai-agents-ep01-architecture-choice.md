# Building Effective AI Agents EP01 - Architecture Choice

## Core Claim

Agent architecture is not a technology ladder. It is a source-taxonomy and fit decision.

The first question is not:

```text
Can we build a multi-agent system?
```

The first question is:

```text
Which source layer are we choosing: single-agent system, multi-agent coordination concept, or agentic workflow structure?
```

## Compression Level

- Level: deep technical, 90-120 seconds.
- Reason: Episode 1 must preserve the source taxonomy, the architecture decision axes, and the multi-agent cost caveat.
- Artifact type: first episode of a series, not a complete compression of the PDF.

## Value Budget

### Non-Cuttable

- Agents fit problems where the path cannot be fully scripted.
- Source taxonomy separates single-agent systems, multi-agent coordination concepts, and agentic workflow structures.
- Single Agent has one agent responsible for the goal, supported by tools, Skills, memory, and possible workflows.
- Multi-Agent coordination concepts are centralized vs decentralized; hierarchical belongs under centralized coordination.
- Agentic workflow patterns define structured orchestration such as sequential, parallel, and evaluator-optimizer. They should not be treated as peer coordination concepts with hierarchical/collaborative multi-agent patterns.
- Start simple, scale intelligently.
- Fixed steps and clear handoffs should usually use agentic workflow structure.
- Single Agent fits a clear goal where the path must be dynamically selected.
- Multi-Agent fits multiple specialist roles that require coordination.
- Multi-Agent can cost roughly 10-15x more tokens than a single agent.
- Production systems need observability and governance because agent behavior is dynamic and opaque.

### Original Diagrams To Preserve

- `p12-single-agent-architecture.png`
- `p19-multi-agent-sequential-workflow.png`
- `p20-multi-agent-parallel-workflow.png`
- Optional montage: `p16-multi-agent-hierarchical-workflow.png`

English labels are acceptable because these are source artifacts.

### Move To Later Episodes

- Skills and modular agent capabilities.
- Detailed single-agent research workflow.
- Hierarchical vs collaborative multi-agent comparison.
- Sequential / parallel / evaluator workflow deep dive.
- Context management mechanics.
- Hybrid and emerging patterns.

## Episode Spine

1. Wrong first question.
2. Source proof: the PDF contains multiple architecture diagrams.
3. Source taxonomy: single-agent systems, multi-agent coordination, agentic workflows.
4. Workflow structure: sequential/parallel/evaluator are predefined orchestration patterns.
5. Single Agent: one dynamic agent can still use tools, Skills, memory, and workflows.
6. Multi-Agent: coordination first, with hierarchical under centralized and collaborative under decentralized.
7. Cost caveat: Multi-Agent may use 10-15x tokens.
8. Decision axes: control requirements, complexity, resources, time-to-market, expertise.
9. Production caveat: observability and governance.
10. Takeaway: use the smallest architecture that works and can evolve.
