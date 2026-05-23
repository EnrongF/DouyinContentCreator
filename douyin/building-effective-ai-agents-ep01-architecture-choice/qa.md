# QA

## Source Gate

- Status: Pass for pre-render package.
- Source: `/Users/fuenrong/Downloads/Building Effective AI Agents- Architecture Patterns and Implementation Frameworks.pdf`.
- Original PDF diagrams are preserved in the scene graph through source-diagram and diagram-montage artifacts.

## Source Logic / Taxonomy Gate

- Status: Pass after correction.
- Required source taxonomy:
  - `Single-agent systems`: one agent handles the task with tools, Skills, memory, and feedback.
  - `Multi-agent coordination concepts`: centralized/hierarchical and decentralized/collaborative coordination among multiple agents.
  - `Agentic workflows`: predefined structures such as sequential, parallel, and evaluator-optimizer.
- Blocking rule: do not present `hierarchical`, `sequential`, and `parallel` as peer patterns. `Hierarchical` belongs under multi-agent coordination; `sequential` and `parallel` belong under agentic workflows.
- Blocking rule: cover labels must identify the source layer represented by each diagram, not only the literal diagram title.

## Compression Gate

- Status: Pass.
- Episode only covers architecture choice.
- Moved values are documented for later episodes: Skills, workflow deep dive, context management, hybrid/emerging patterns.
- Multi-Agent 10-15x token caveat is present.

## Voice Gate

- Status: Pass.
- TTS generated as 12 paragraph-level chunks using `gpt-4o-mini-tts`, voice `marin`.
- Measured total duration: 117.96 seconds.
- Scene graph durations and `audioFile` paths are locked from `voice-manifest.json`.
- ASR QA status: pass.
- Pronunciation QA fix applied: `第一集的结论：先选最小可用架构，再留出演进路径。` was rewritten as `第一集的结论是：先选最小可用架构，再保留演进空间。` after ASR misheard `留出演进路径`.

## Native Chinese Expression Gate

- Status: Pass with fixes.
- Scope: title options, spoken script, subtitles, cover copy, caption, and top progress labels.
- Blocking rule: flag translation-shaped Chinese such as `架构不是升级梯`; replace with native expressions such as `架构选择，不是从低级到高级`, `不要把 Multi-Agent 当成升级版`, or `不是越复杂就越高级`.
- This gate is separate from pronunciation QA: good TTS pronunciation does not fix unnatural wording.
- Fixes applied before final render: `领域专家度` became `专家参与`; `多个专家协同` became `多个专家一起处理`; `留出演进路径` became `保留演进空间`.

## Render Gate

- Status: Pass.
- Scene graph exists at `scene-graphs/building-effective-ai-agents-ep01-architecture-choice.json`.
- Remotion composition is registered as `building-effective-ai-agents-ep01-architecture-choice`.
- Scene graph includes abstract `sectionLabel` values and internal `paragraphLabel` metadata.
- Remotion layout includes a top dynamic progress bar with audience-value major stage labels only; generic labels such as `Hook` and `Next` are hidden from the progress UI.
- Cover preview exists at `douyin/building-effective-ai-agents-ep01-architecture-choice/cover.preview.png`.
- Alternative source-logic cover exists at `douyin/building-effective-ai-agents-ep01-architecture-choice/cover.source-logic.png`.
- Series cover consistency: pass. The source-logic cover uses the approved episode badge, source attribution mark, and original PDF diagram montage.
- Cover value framing: pass. The headline now asks the audience-facing decision question, `Agent架构怎么选?`, instead of describing our source-analysis process.
- Source VI handling: pass. Anthropic/source identity appears only as attribution, not as channel branding or implied endorsement.
- Final video exists at `douyin/building-effective-ai-agents-ep01-architecture-choice/video.mp4`.
- Contact sheet exists at `douyin/building-effective-ai-agents-ep01-architecture-choice/contact-sheet.jpg`.
- Render output: native 1920 x 1080 Remotion MP4, 3538 frames at 30 fps, about 117.93 seconds, 32 MB.
