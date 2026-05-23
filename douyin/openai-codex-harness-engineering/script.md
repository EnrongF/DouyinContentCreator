# Script

## Hook

别只看那一百万行代码。OpenAI 真正做的不是让 Codex 多写代码，而是把软件工程改造成智能体可以执行、验证、维护的生产环境。

## Structure

1. Thesis: this is Harness Engineering, not just Prompt Engineering.
2. Evidence: 0 manually-written code, five months, about one million LOC, roughly 1,500 PRs, about 1/10th hand-written time, 3.5 PRs per engineer per day, seven engineers later, hundreds of internal users.
3. Scaffold: Codex CLI + GPT-5 generated repo structure, CI, formatting, package manager setup, app framework, and AGENTS.md.
4. Application legibility: per-worktree app instance, Chrome DevTools, screenshots, DOM/page reading, navigation, bug reproduction, fix validation.
5. Runtime legibility: ephemeral local observability system, Vector, logs, metrics, traces, query interfaces, 800ms startup, no span over two seconds, six-hour Codex runs.
6. Repository knowledge: short AGENTS.md as map, docs/ as source of truth, versioned architecture/specs/plans/security/quality docs, CI/linter/link checks, doc-gardening agent.
7. Mechanical taste: fixed dependency order, Providers boundary, boundary parsing, structured logs, naming/file-size/reliability lints, remediation instructions injected into agent context.
8. Merge philosophy: short-lived PRs, fewer blocking gates, flaky tests fixed by follow-up agent runs, correction cheap and waiting expensive, not safe to copy into low-throughput teams.
9. Autonomy loop: validate state, reproduce bug, record failure video, fix, validate by driving app, record resolution video, merge request, feedback, build remediation, human escalation for judgment, merge.
10. Entropy loop: Friday 20% AI slop cleanup failed; golden principles and background Codex cleanup tasks act as garbage collection.
11. Caveat: OpenAI is still learning long-term coherence, where human judgment compounds, and how this evolves as models improve.

## Final Line

模型负责生成，Harness 负责治理：让生成结果可见、可控、可验证、也可维护。
