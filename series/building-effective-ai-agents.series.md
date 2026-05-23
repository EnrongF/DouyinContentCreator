# Building Effective AI Agents Series Map

## Topic Promise

Help business and technical leaders choose the right AI-agent architecture without overbuilding.

## Audience

Business leaders, product owners, operations teams, and technical decision makers evaluating enterprise AI-agent implementations.

## Series Type

Full series. The PDF is too dense for one balanced short video.

## Source Value Inventory Summary

Non-cuttable source values:
- Agent vs automation distinction.
- Start simple, scale intelligently.
- Model choice as capability/speed/cost tradeoff.
- Observability for opaque agent decisions.
- Single-agent vs multi-agent use and avoid rules.
- Source taxonomy: single-agent systems, multi-agent coordination concepts, and agentic workflow structures are separate layers.
- Multi-agent coordination concepts: centralized/hierarchical and decentralized/collaborative.
- Agentic workflow structures: sequential, parallel, evaluator-optimizer.
- Decision axes: control, domain complexity, resource constraints, time-to-market, and domain expertise.
- Multi-agent token-cost caveat: roughly 10-15x more tokens than single agents.
- Original architecture/workflow diagrams from pages 12, 16, 17, 19, 20, and 22.

Moved values:
- Skills and modular capability packages.
- Customer example metrics.
- Single-agent research walkthrough.
- Multi-agent coordination concepts.
- Agentic workflow structure details.
- Context management mechanics.
- Emerging dynamic and network patterns.
- Hybrid production evolution paths.

## Episode List

| Episode | Working Title | Mental Upgrade | Keep | Move / Defer |
|---|---|---|---|---|
| 1 | Agent架构怎么选? | Do not flatten the PDF: Single Agent, Multi-Agent coordination, and Agentic Workflows are different layers. | Source taxonomy, agent vs automation, decision axes, 10-15x cost caveat, start simple. | Skills, detailed workflow patterns, production observability mechanics. |
| 2 | Agent从小做起 | A narrow, modular agent is usually the right first step. | Model choice, modular design, Skills as capability packages. | Multi-agent coordination details. |
| 3 | 多智能体一定更好么? | Multi-agent only pays off when single agents hit specific limits and coordination is justified. | Single-agent loop, multi-agent use rules, centralized/hierarchical vs decentralized/collaborative, 90.2% caveated signal, cost/observability risks. | Agentic workflow taxonomy. |
| 4 | Workflow到底是什么? | Sequential, parallel, and evaluator workflows define structured orchestration; they are not peers of hierarchical coordination. | Sequential, parallel, evaluator-optimizer, use/avoid rules. | Emerging patterns. |
| 5 | Agent上线前看什么? | The hard part is observing, governing, and evolving agent behavior. | Observability, context management, memory, pagination/filtering/truncation, success metrics. | Advanced hybrid strategy. |
| 6 | 什么时候用混合架构? | Advanced agent systems are combinations that evolve from simpler systems. | Dynamic generation, network systems, hybrid escalation, e-commerce evolution path. | Full implementation tutorial. |

## Diagram Assignments

| Episode | Diagram Assets |
|---|---|
| 1 | Optional taxonomy montage only: `p12-single-agent-architecture.png`, `p16-multi-agent-hierarchical-workflow.png`, `p19-multi-agent-sequential-workflow.png` |
| 2 | `p12-single-agent-architecture.png`; optional `p12-single-agent-research-workflow.png` with source-context warning |
| 3 | `p16-multi-agent-hierarchical-workflow.png`, `p17-multi-agent-collaborative-workflow.png` |
| 4 | `p19-multi-agent-sequential-workflow.png`, `p20-multi-agent-parallel-workflow.png`, `p22-multi-agent-evaluator-workflow.png` |
| 5 | Reuse source diagrams only as anchors; add observability/context overlays |
| 6 | Use diagram comparisons from earlier episodes plus adapted evolution ladder |

## Series Cover System

All episode covers should look like one source-faithful family, not six unrelated thumbnails.

Shared cover rules:
- Use one consistent Douyin-first vertical cover layout at `1080x1920`. Keep 16:9 covers only as secondary preview artifacts when needed.
- Use the same badge grammar: `EPxx / <episode decision>`.
- Use a large audience-value Chinese headline plus a compact source/taxonomy subtitle. The headline should sell the decision value, not describe how we analyzed the source.
- Use thumb-first hierarchy: the headline must still be readable in a small phone grid, with the source/episode strapline secondary and proof chips tertiary.
- Use one strong contrast pair per episode, but keep it inside our restrained technical palette. Borrow the reference's clarity, not its comic sticker/stroke style.
- Add one to three compact proof chips when useful, such as `10-15x Token`, `Single Agent`, `Coordination`, or `Workflow`; chips must point to source-backed ideas rather than decoration.
- Use source VI only as reference and attribution. Do not present the source logo as channel branding or imply endorsement.
- Use at least one original source diagram, source basic graph, or source-derived taxonomy artifact as the dominant visual anchor.
- Preserve source category boundaries in cover labels; cover visuals must pass the Source Logic / Taxonomy Gate.
- Keep the source attribution mark visible: `Source: Anthropic PDF / Building Effective AI Agents`.
- Avoid production-method headlines. Use value-language such as `Agent架构怎么选?` or `不是越复杂就越高级`.
- Avoid low-trust thumbnail tactics: fake urgency, misleading VS framing, excessive outlined lettering, and labels that are only there to game attention.

Episode cover anchors:

| Episode | Cover Headline | Proof Chips | Cover Anchor | Cover Logic |
|---|---|---|---|---|
| 1 | `Agent架构怎么选?` | `Source Diagrams`, `Coordination`, `Workflow` | Source taxonomy montage: single-agent, multi-agent coordination, agentic workflow | Prevent the audience from treating Multi-Agent as a simple upgrade path. |
| 2 | `Agent从小做起` | `Single Agent`, `Context`, `Tools` | `p12-single-agent-architecture.png` | Start with a narrow adaptive agent before scaling architecture. |
| 3 | `多智能体一定更好么?` | `Hierarchical`, `Collaborative`, `Handoff` | `p16` hierarchical plus `p17` collaborative | Compare multi-agent coordination concepts, not workflow structures. |
| 4 | `Workflow到底是什么?` | `Sequential`, `Parallel`, `Evaluator` | `p19`, `p20`, `p22` workflow diagrams | Treat workflows as orchestration structure. |
| 5 | `Agent上线前看什么?` | `Tracing`, `Eval`, `Control` | Source diagram with observability/context overlays | Shift from architecture choice to production control. |
| 6 | `什么时候用混合架构?` | `Evolution`, `Hybrid`, `Tradeoff` | Recombined source diagrams plus evolution path | Show hybrid systems as later combinations, not the starting point. |

## Episode 1 Bridge

End Episode 1 with:

```text
Once you know the problem really needs autonomy, the next question is how narrow the first agent should be.
```

## Source Logic Guardrail

This series must preserve the PDF's category boundaries:

```text
Single-agent systems
Multi-agent coordination concepts
  -> centralized / hierarchical
  -> decentralized / collaborative
Agentic workflow structures
  -> sequential
  -> parallel
  -> evaluator-optimizer
```

Do not present `hierarchical`, `sequential`, and `parallel` as peer categories. If a later episode uses a simplified ladder, label it as synthesis and state which source layers were combined.

## Compression Guardrail

If an episode needs more than one mental upgrade, split it. Do not use a faster voiceover to carry more source material.
