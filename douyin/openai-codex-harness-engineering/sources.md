# Source

- Title: Harness engineering: leveraging Codex in an agent-first world
- Publisher: OpenAI Engineering
- Author: Ryan Lopopolo, Member of the Technical Staff
- Date: 2026-02-11
- URL: https://openai.com/index/harness-engineering/

## Source Quality

- Latest/frontier: 2026 OpenAI Engineering article about agent-first software development.
- Original/professional: first-party OpenAI engineering account, written by an engineer on the project.
- Scope: one-source job by request. Search role intentionally skipped.

## Original Materials To Preserve

- 0 manually-written code constraint.
- Five-month experiment from empty repository to internal beta product.
- Rough scale: about one million lines of code, roughly 1,500 merged PRs, three engineers initially driving Codex, 3.5 PRs per engineer per day, team later seven engineers.
- Estimated acceleration: OpenAI estimates roughly 1/10th the time it would have taken to write the code by hand.
- Product adoption: internal daily users, external alpha testers, hundreds of internal users, including daily internal power users.
- Role shift: humans steer; agents execute.
- First commit landed in late August 2025; Codex CLI with GPT-5 generated initial scaffold and AGENTS.md.
- Initial scaffold: repository structure, CI configuration, formatting rules, package manager setup, application framework, AGENTS.md.
- Chrome DevTools MCP application-legibility loop: screenshots, DOM/page state, navigation, bug reproduction, fix validation.
- Local ephemeral per-worktree observability stack: logs, metrics, traces, Vector, LogQL, PromQL, TraceQL.
- Codex runs can work on a single task for upwards of six hours.
- Repository knowledge as system of record: short AGENTS.md as map, structured docs/ as source of truth.
- AGENTS.md is roughly 100 lines and points to deeper docs.
- Agent legibility principle: what Codex cannot access in context effectively does not exist.
- Repository knowledge examples: design docs with verification status, execution plans with progress and decision logs, quality docs grading domains and layers.
- Layered domain architecture: Types, Config, Repo, Service, Runtime, UI, Providers boundary, Utils, App Wiring + UI.
- Mechanical enforcement: custom linters, structural tests, structured logging, naming conventions, file size limits, reliability requirements, remediation instructions in lint messages.
- Minimal blocking merge philosophy under high agent throughput: short-lived PRs, flaky tests handled by follow-up runs, correction cheap and waiting expensive.
- Agent-generated means product code, tests, CI, tools, docs, evaluation harnesses, review comments, scripts, dashboards.
- End-to-end autonomy checklist from validating current state to merging the change.
- Entropy management: 20% Friday cleanup did not scale; golden principles and recurring cleanup tasks became garbage collection.
- Golden principle examples: prefer shared utility packages over hand-rolled helpers; do not probe data YOLO-style; validate boundaries or rely on typed SDKs.
- Background Codex cleanup tasks scan deviations, update quality grades, open targeted refactoring PRs, and many can be reviewed quickly or automerged.
- Caveats: long-term architectural coherence is still unknown; OpenAI is still learning where human judgment adds leverage and how model improvements change the system.
