# Visual Template Catalog

This directory is the local template layer for the Visual System.

It adapts the strongest transferable parts of `zarazhangrui/frontend-slides` into this project's HTML -> Remotion -> video pipeline.

Reference source:
- [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides)

## Frontend Slides Coverage

We do not vendor the upstream skill files verbatim. Instead, we absorb the
relevant production rules into this repository's visual system and adapt them to
our HTML -> scene graph -> Remotion -> Douyin pipeline.

| Upstream file | Local coverage | Status |
|---|---|---|
| `SKILL.md` | `VISUAL_SYSTEM.md`, `prompts/visual-production.md`, `prompts/visual-system-designer.md`, `prompts/visual-builder.md` | Core workflow absorbed: show-don't-tell previews, mode detection, approval checkpoint, viewport fitting, density limits, anti-generic design. |
| `STYLE_PRESETS.md` | `visual-templates/templates.json` | Style families absorbed and adapted, including dark/light/specialty presets plus Codex-native and source-native variants. |
| `viewport-base.css` | `VISUAL_SYSTEM.md` HTML Preview Rules | Mandatory viewport-fit CSS principles absorbed: `100vh`/`100dvh`, overflow lock, `clamp()`, image max-height, short-height breakpoints, reduced-motion support. |
| `html-template.md` | `VISUAL_SYSTEM.md` HTML Preview Rules and HTML Code Quality | Architecture absorbed: self-contained HTML, navigation/progress controller, semantic HTML, ARIA, optional inline editing guardrails, asset handling. |
| `animation-patterns.md` | `VISUAL_SYSTEM.md` Motion Rules and template `motion` fields | Effect-to-feeling logic absorbed and adapted to source-faithful semantic motion. |
| `scripts/extract-pptx.py` | Not currently included | Out of scope unless this repo starts converting PowerPoint files. Use the upstream script or create a local equivalent only when PPT conversion is requested. |
| `scripts/deploy.sh` | Not currently included | Out of scope; this repo produces local artifacts and Douyin packages, not Vercel-hosted slide decks by default. |
| `scripts/export-pdf.sh` | Not currently included | Out of scope unless PDF export is requested. Prefer local render/export tooling only when needed. |

When building HTML previews, the required local files are:
- `VISUAL_SYSTEM.md`
- `visual-templates/templates.json`
- `prompts/visual-production.md`
- `prompts/visual-system-designer.md` or `prompts/visual-builder.md`

## How To Use

When visual direction is undecided:

1. Read `VISUAL_SYSTEM.md`.
2. Read `visual-templates/templates.json`.
3. Select 4-8 candidate templates for comparison, not just the default house style.
4. Create compact HTML previews for the strongest contrasting candidates.
5. Score candidates on:
   - distinctiveness;
   - topic fit;
   - source handling;
   - readability;
   - motion potential;
   - reusability;
   - Remotion production cost.
6. Run the HTML parity checklist: viewport fit, density limits, distinctive
   typography, purposeful motion, keyboard navigation, reduced-motion support,
   and anti-generic design.
7. Lock one visual system.
8. Apply the source-fidelity gate before Remotion implementation.

## Template Types

- `codex-native`: Designed for this repository's source-faithful AI cognition compression work.
- `frontend-slides-adapted`: Adapted from the public `frontend-slides` template philosophy and style families.
- `source-native`: Derived from the visual identity of the source material itself.

## Rule

Templates are starting points, not final designs.

Do not copy a template blindly. Use it to generate professional options, then adapt typography, color, artifact treatment, motion, density, and source constraints to the actual episode.
