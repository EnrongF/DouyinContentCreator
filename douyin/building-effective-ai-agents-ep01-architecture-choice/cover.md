# Cover

## Title

Agent架构怎么选?

## Subtitle

架构、协调、工作流，是三件不同的事

## Visual

Use original PDF diagrams as the main visual, grouped by the pattern names that match the diagrams:

```text
Single Agent
Multi-Agent Coordination
Agentic Workflows
```

Follow the series cover family:
- Same Douyin-first vertical layout: `1080x1920`.
- 16:9 covers may be kept as secondary previews, but the publish cover is vertical.
- Same badge pattern: `EPxx / Episode Decision`.
- Same source attribution mark: `Source: Anthropic PDF / Building Effective AI Agents`.
- One original PDF diagram or diagram montage as the proof artifact; it should support the headline, not compete with it.
- Chinese headline large enough for phone-feed reading; English source labels may remain inside diagrams.
- Reference-inspired hierarchy: very large value headline, compact source/episode strapline, and small proof chips.
- Our style adjustment: keep the dark technical-documentary system and source diagrams; do not copy the reference's comic sticker lettering or exaggerated thumbnail effects.
- Feed readability rule: first read is the value claim, second read is the decision subtitle, third read is the source proof.
- Series consistency rule: keep the `EPxx` square badge, proof chips, dark source-board layout, and source diagram evidence across episodes.
- Thumbnail style rule: use strong shadow, dense contrast, and a compact proof strip; avoid slide-like explanatory headers.

## Logic

- The cover promise is audience-facing: avoid choosing a more expensive architecture just because it sounds more advanced.
- The cover can borrow the reference pattern of a strong claim plus proof tags, but the proof tags must be source-grounded.
- Every cover card points to the source layer it represents.
- `Hierarchical` is not a peer of `sequential` or `parallel`; it belongs under multi-agent centralized coordination.
- `Sequential`, `parallel`, and `evaluator-optimizer` belong under agentic workflow structures.
- The source taxonomy is proof, not the headline. Do not use source-analysis process language as cover value.
- Source logo / VI can be referenced as source attribution, but must not make the video look officially endorsed by the source publisher.

## Source-Logic Cover

The ladder cover is rejected for Episode 1 because it implies an upgrade path. The source-logic cover is the production cover.

`Production Controls` moves out of the cover and stays as a production caveat inside the episode.

Render target:

```bash
cd remotion
npm run still:building-effective-ai-agents-ep01-vertical-cover
npm run still:building-effective-ai-agents-ep01-source-cover
```
