# Timing Map

This rerun uses `frame_durations.json` as the timing authority. The visual sequence is not equal-duration still slides.

## Sync Model

- Beat count: 59 narration-aligned beats.
- TTS chunk count: 24 phrase-level chunks.
- Phase count: 8 dynamic frames per beat.
- Phased frames: 472.
- Source timing hint total: superseded by measured scene audio durations and weighted beat allocation.
- Final scaling: `render_video.py` preserves per-beat durations when `timing_source=beat_audio_manifest`; it does not globally stretch beat timing.
- Final video duration: 00:03:24.23.
- Voiceover duration: 00:03:24.14.
- Voice profile: OpenAI TTS `alloy`, conversational Mandarin, speed `1.2`; longest derived beat 5.09 seconds.
- Timing authority: `scene_audio_manifest.json` -> `beat_audio_manifest.json` -> `frame_durations.json`.

## Beat Sequence

The table below preserves the storyboard beat order and original planning hints. Exact production timing is now in `beat_audio_manifest.json`; each row there contains the spoken text, scene audio file, weighted allocation, and derived duration used by the final render.

| Beat | Start | End | Hint | Focus |
|---:|---:|---:|---:|---|
| 01 | 000.0 | 003.0 | 03.0 | 别只看那一百万行代码 |
| 02 | 003.0 | 007.0 | 04.0 | 关键：软件工程变成智能体生产环境 |
| 03 | 007.0 | 011.0 | 04.0 | Harness Engineering：可见、可控、可验证 |
| 04 | 011.0 | 013.2 | 02.2 | 这不是 demo：从真实产品开始 |
| 05 | 013.2 | 015.8 | 02.6 | 0 行人工手写代码 |
| 06 | 015.8 | 019.3 | 03.5 | 5 个月：约 1M 行代码，约 1,500 PR |
| 07 | 019.3 | 022.3 | 03.0 | OpenAI 估计：约 1/10 手写时间 |
| 08 | 022.3 | 025.7 | 03.4 | 3 位工程师：每人每天 3.5 个 PR |
| 09 | 025.7 | 029.7 | 04.0 | 7 位工程师后吞吐继续上升，还有真实用户 |
| 10 | 029.7 | 032.3 | 02.6 | 关键不是代码量，而是角色变了 |
| 11 | 032.3 | 034.6 | 02.3 | 人类掌舵，智能体执行 |
| 12 | 034.6 | 037.2 | 02.6 | 第一层：仓库先被智能体塑形 |
| 13 | 037.2 | 040.2 | 03.0 | Codex CLI + GPT-5 生成初始 scaffold |
| 14 | 040.2 | 044.2 | 04.0 | 结构、CI、格式化、包管理、应用框架 |
| 15 | 044.2 | 046.7 | 02.5 | 甚至 AGENTS.md 也由 Codex 写 |
| 16 | 046.7 | 049.1 | 02.4 | 第二层：让应用对智能体可见 |
| 17 | 049.1 | 051.5 | 02.4 | 每个 git worktree 启动独立应用 |
| 18 | 051.5 | 055.3 | 03.8 | DevTools：截图、读页面、导航 |
| 19 | 055.3 | 057.8 | 02.5 | 复现问题，再验证修复 |
| 20 | 057.8 | 060.0 | 02.2 | 界面变成智能体工作台 |
| 21 | 060.0 | 062.0 | 02.0 | 第三层：让运行信号可见 |
| 22 | 062.0 | 064.7 | 02.7 | 每个 worktree 有临时本地观测栈 |
| 23 | 064.7 | 067.7 | 03.0 | Vector 汇入日志、指标、链路追踪 |
| 24 | 067.7 | 070.5 | 02.8 | Codex 用 LogQL、PromQL、TraceQL 查询 |
| 25 | 070.5 | 074.5 | 04.0 | 性能目标变成可执行任务 |
| 26 | 074.5 | 076.7 | 02.2 | 有些 Codex 任务可连续工作 6 小时以上 |
| 27 | 076.7 | 079.1 | 02.4 | 第四层：把组织知识写进仓库 |
| 28 | 079.1 | 082.1 | 03.0 | 巨大的 AGENTS.md 会浪费上下文 |
| 29 | 082.1 | 084.7 | 02.6 | AGENTS.md 只做约 100 行地图 |
| 30 | 084.7 | 088.9 | 04.2 | docs/ 才是版本化系统记录 |
| 31 | 088.9 | 092.1 | 03.2 | CI、链接检查、文档维护 agent 保持新鲜 |
| 32 | 092.1 | 095.3 | 03.2 | 智能体看不见的知识，几乎等于不存在 |
| 33 | 095.3 | 098.3 | 03.0 | 外部文档、聊天、隐性经验必须进入仓库 |
| 34 | 098.3 | 100.8 | 02.5 | 第五层：把工程品味机械化 |
| 35 | 100.8 | 103.3 | 02.5 | 业务域只能沿固定顺序依赖 |
| 36 | 103.3 | 105.7 | 02.4 | 跨领域能力必须通过 Providers |
| 37 | 105.7 | 109.7 | 04.0 | 边界解析、结构化日志、命名和文件大小都能检查 |
| 38 | 109.7 | 112.2 | 02.5 | lint 错误会把修复指导注入上下文 |
| 39 | 112.2 | 115.6 | 03.4 | 约束不是减速器，是防止速度变混乱的加速器 |
| 40 | 115.6 | 118.0 | 02.4 | 第六层：吞吐量改变合并策略 |
| 41 | 118.0 | 122.0 | 04.0 | 短生命周期 PR，更少阻塞式 gate，flaky 后续修 |
| 42 | 122.0 | 125.5 | 03.5 | 高吞吐下修正便宜、等待昂贵；低吞吐别照搬 |
| 43 | 125.5 | 128.3 | 02.8 | Agent-generated 不只是业务代码 |
| 44 | 128.3 | 131.5 | 03.2 | 代码、测试、工具、CI、文档、评审都进入系统 |
| 45 | 131.5 | 133.5 | 02.0 | 最后形成端到端闭环 |
| 46 | 133.5 | 136.5 | 03.0 | 验证状态、复现 bug、录制失败视频 |
| 47 | 136.5 | 140.5 | 04.0 | 修复、驱动应用验证、录制修复视频、提交代码合并请求 |
| 48 | 140.5 | 144.3 | 03.8 | 回应反馈、修构建、判断时升级给人类、合并 |
| 49 | 144.3 | 146.9 | 02.6 | 这依赖工具和结构，不能直接复制 |
| 50 | 146.9 | 149.1 | 02.2 | 而熵也要被治理 |
| 51 | 149.1 | 152.1 | 03.0 | 旧办法：每周五 20% 时间清理 AI 垃圾代码 |
| 52 | 152.1 | 156.3 | 04.2 | golden principles：共享工具，不猜数据 |
| 53 | 156.3 | 159.9 | 03.6 | 后台 Codex 扫描偏差、更新质量分、开小型重构请求 |
| 54 | 159.9 | 161.9 | 02.0 | 这就像垃圾回收 |
| 55 | 161.9 | 164.7 | 02.8 | 这不是 AI 写代码，而是 Harness Engineering |
| 56 | 164.7 | 167.5 | 02.8 | 模型负责生成，Harness 负责治理 |
| 57 | 167.5 | 170.3 | 02.8 | 让生成结果可见、可控、可验证、可维护 |
| 58 | 170.3 | 173.9 | 03.6 | OpenAI 仍在学习长期一致性和人类判断位置 |
| 59 | 173.9 | 176.4 | 02.5 | 企业智能体真正需要的是基础设施 |

## Dynamic Focus Rule

Each beat is rendered as 8 phase frames:

- soft glow and corner brackets emphasize the focused element;
- pulse halo expands and settles;
- subtle underline progress marks the active focused box;
- no bottom subtitle/focus-caption card is rendered; platform subtitles should be generated from the voice track;
- long source-heavy sections are split into micro-beats instead of one static hold.
