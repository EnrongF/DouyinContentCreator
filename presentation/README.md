# Presentation

Store the final HTML, slides, or memo here.

Root visual contract: `../VISUAL_SYSTEM.md`.

## Naming
Use descriptive article slugs so multiple research decks can coexist.

Pattern:
- `<source-or-topic-slug>.html`

Current deck:
- `anthropic-multi-agent-research-system.html`
- `anthropic-multi-agent-research-system.zh-cn.html`
- `harness-engineering.html`

## Sharing
The decks use local images from:
- `assets/anthropic-multi-agent-research-system/`

When sending a deck to someone else, include the `assets/` folder next to the HTML file.

## HTML Quality Rules

- Prefer self-contained, zero-dependency HTML for previews and shareable decks.
- Every slide must fit the viewport with no scrolling inside slides.
- Use viewport-relative or `clamp()` sizing for type and spacing.
- Include keyboard navigation and progress state for deck-like artifacts.
- Respect `prefers-reduced-motion`.
- Split dense content instead of shrinking text until it becomes unreadable.
