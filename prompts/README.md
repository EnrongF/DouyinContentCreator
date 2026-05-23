# Prompt Roles

Prompt files are task-specific role instructions. Root project roles stay small;
specialized prompts can be loaded only when needed.

## Canonical Roles

| Role | Canonical prompt | Specialized prompts |
|---|---|---|
| Lead | `lead.md` | none |
| Knowledge | `knowledge.md` | `source.md`, `source-scout.md`, `source-qualifier.md`, `extraction.md`, `strategy.md`, `synthesis.md`, `ai-engineering-analyst.md`, `douyin-strategist.md` |
| Voice | `voice.md` | `script-writer.md`, `voice-director.md`, `voice-producer.md` |
| Visual Production | `visual-production.md` | `brand-source-extractor.md`, `visual.md`, `visual-system-designer.md`, `visual-builder.md`, `motion-render.md`, `remotion-renderer.md` |
| Quality | `quality.md` | `review.md`, `fidelity-reviewer.md`, `virality-clarity-reviewer.md`, `release.md`, `release-verifier.md` |
| Douyin Platform | `douyin-platform.md` | none |

## Loading Rule

Load the canonical prompt for the role first. Load specialized prompts only for
the current task slice.
