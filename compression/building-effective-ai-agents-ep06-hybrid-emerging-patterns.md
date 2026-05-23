# Episode 6 Compression

## Core Claim

Hybrid agent architecture is not the advanced template you start with. It is a
later composition that becomes justified only after a simpler agent hits measured
limits.

## Target Audience

Builders, operators, founders, and enterprise AI leaders who already understand
the basic single-agent, multi-agent, and workflow distinctions and now need an
upgrade path.

## Compression Level

Standard: 75-95 seconds.

This episode should be direct and decision-oriented. It should not become a full
implementation tutorial.

## Source Basis

- Primary source: Anthropic PDF `Building Effective AI Agents`.
- Source refs:
  - `pdf:p22-p23`: dynamic agent generation and peer-to-peer network systems as emerging patterns.
  - `pdf:p23-p24`: decision framework and resource constraints.
  - `pdf:p23`: multi-agent systems can use roughly 10-15x more tokens than single agents.
  - `pdf:p24-p25`: evolution path from single agent to routing, specialist agents, multi-agent coordination, and evaluator agents.
  - `pdf:p25`: hybrid strategies combine supervisors, parallel processing, dynamic routing, and multi-agent escalation.

## Value Budget

### Retained Value

- Hybrid means composition, not a single source category.
- The source's evolution path starts with a single agent, then adds routing,
  specialists, coordination, and evaluators as needed.
- Routing is often the first hybrid move.
- Specialist agents make sense when domains separate cleanly.
- Parallel and evaluator workflows are composable workflow structures, not peers
  of hierarchical multi-agent coordination.
- Dynamic generation and peer-to-peer networks are emerging patterns, not
  default production advice.
- The 10-15x token-cost caveat stays visible.

### Moved Value

- Full implementation tutorial for hybrid production systems.
- Detailed context management mechanics.
- Full dynamic-agent-generation design.
- Full peer-to-peer network architecture.
- Long enterprise examples and vendor-supplied metrics.

### Omitted Value

- Customer proof examples that do not change the EP06 decision.
- All old creative wording, script structure, and visual treatment from the
  previous EP06 package.

## Mental Model

Use this ladder:

```text
single agent
-> router
-> specialist agents
-> multi-agent coordination
-> evaluator / optimizer loop
-> hybrid architecture
```

But explain that the ladder is synthesis. It recombines source concepts into an
operating path. It must not imply that every system should climb every step.

## Decision Frame

Use hybrid architecture only when four conditions are true:

1. A simpler agent has a measured bottleneck.
2. The work separates into different task types or specialist domains.
3. Quality criteria, escalation rules, or review loops are clear.
4. The team can afford the added token cost, latency, observability, and
   governance overhead.

If these are not true, stay with a narrower single agent or a structured
workflow.

## Non-Cuttable Caveats

- Hybrid is a composition of simpler patterns, not a source-defined standalone
  category.
- Dynamic agent generation and peer-to-peer networks are emerging patterns.
- Multi-agent systems can cost roughly 10-15x more tokens than single-agent
  systems.
- Do not present `hierarchical`, `sequential`, and `parallel` as peer categories.
- Any recombined ladder or architecture map must be labeled as synthesis.

## Suggested Scene Spine

1. Hook: the mistake is starting with the most complex architecture.
2. Source ladder: single agent -> routing -> specialists -> coordination -> evaluator.
3. First hybrid move: routing by task type.
4. Specialist move: supervisor plus domain agents.
5. Workflow pieces: parallel and evaluator loops as structured additions.
6. Emerging caveat: dynamic and peer-to-peer patterns are experimental.
7. Decision gate: four conditions before hybrid.
8. Takeaway: hybrid is earned by evidence, not chosen for status.
