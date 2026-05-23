# Episode Brief

## Episode

EP01: Agent架构怎么选?

## Promise

Help business teams avoid overbuilding by choosing the simplest AI-agent architecture that matches the problem.

## Mental Upgrade

Agent architecture is not a ladder from simple to advanced. It is a source-taxonomy and fit decision.

## Scope

This episode covers only the first decision:

```text
Which source layer are we choosing: single-agent system, multi-agent coordination concept, or agentic workflow structure?
```

Important clarification: do not mix the source levels. Hierarchical is a multi-agent coordination pattern under centralized systems. Sequential and parallel are agentic workflow structures.

## Hierarchy

- Single Agent: one agent responsible for the goal, supported by tools, Skills, memory, and possible workflows.
- Multi-Agent coordination: centralized/hierarchical or decentralized/collaborative coordination among multiple agents.
- Agentic workflows: predefined structures such as sequential, parallel, and evaluator-optimizer.

## Source Diagrams Used

- `p12-single-agent-architecture.png`
- `p16-multi-agent-hierarchical-workflow.png`
- `p19-multi-agent-sequential-workflow.png`
- `p20-multi-agent-parallel-workflow.png`

## Moved To Later Episodes

- Skills and modular design.
- Full single-agent implementation walkthrough.
- Hierarchical vs collaborative multi-agent deep dive.
- Workflow pattern deep dive.
- Context management.
- Emerging and hybrid patterns.
