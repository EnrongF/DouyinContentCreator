# Speech Chunk Plan

Slug: `the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code`

## Gate Status

- Stage: `speech chunk plan`
- Status: `completed; ready for TTS`
- Pause required: `yes`
- Prior gate: `voice/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code/script.md`
- Pronunciation lock: `voice/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code/pronunciation.md`
- Target duration: `60-75 seconds`
- Estimated draft duration: `64-72 seconds`
- Next approved stage: `TTS production`
- Not approved yet: `TTS`, `ASR`, `voice manifest`, `scene graph`, `render`, `Douyin package`

## Chunks

| Chunk | Paragraph | Est. sec | Spoken Text | TTS Input Note | Subtitle | Pause / Emphasis | Focus Phrase | Expected Visual Focus |
|---|---|---:|---|---|---|---|---|---|
| c01 | p01 | 2.4 | AI 写代码很快。 | `A I` if needed | AI 写代码很快。 | short hook | 写代码很快 | code stream appears |
| c02 | p01 | 4.4 | 但如果产品边界不清楚，它也会很快把产品写散。 | none | 边界不清楚，产品会被写散。 | pause after contrast | 产品写散 | feature nodes spill out |
| c03 | p02 | 3.8 | 有了验证信号以后，下一关不是马上把功能做满。 | none | 有了验证信号，不是马上做满功能。 | corrective | 不是马上把功能做满 | full-product button dims |
| c04 | p02 | 6.0 | MVP 阶段，本质上还是在收集证据：一小群真实用户，会不会回来、付费，或者愿意推荐。 | `M V P` if needed | MVP 阶段，还是在收集证据。 | list rhythm | 回来 / 付费 / 推荐 | evidence chips appear |
| c05 | p03 | 4.2 | 所以，最小可用产品，最重要的不是“还能加什么”。 | none | 最重要的不是“还能加什么”。 | emphasize `不是` | 还能加什么 | add-feature card dims |
| c06 | p03 | 6.0 | 而是先写清楚三件事：它现在解决什么，暂时不解决什么，什么证据才允许你加新功能。 | none | 先写清楚：解决什么、不解决什么、什么证据能加。 | three-part rhythm | 三件事 | scope document appears |
| c07 | p04 | 4.5 | 不然，每次让 AI 开工，它都会重新猜一遍产品边界。 | `A I` if needed | 每次让 AI 开工，它都会重新猜边界。 | slow on `重新猜` | 重新猜一遍产品边界 | context reset loop |
| c08 | p04 | 5.0 | 今天加一个边缘场景，明天补一个酷功能，后天整个产品就开始失去形状。 | none | 一个又一个功能，产品开始失去形状。 | cumulative rhythm | 失去形状 | product box deforms |
| c09 | p04 | 6.0 | 这就是 AI 时代更隐蔽的技术债：代码可能能跑，但产品边界和架构上下文已经开始漂移。 | `A I` if needed | AI 技术债：边界和上下文开始漂移。 | slow, technical | 边界和架构上下文 | drift warning |
| c10 | p05 | 5.0 | 所以，让 AI 写之前，先把边界和上下文放到它能读到的地方。 | `A I` if needed | 让 AI 写之前，先放好边界和上下文。 | decisive | 放到它能读到的地方 | readable context doc |
| c11 | p05 | 3.5 | 这一集的判断是：先写边界，再写代码。 | none | 先写边界，再写代码。 | takeaway | 先写边界 | boundary before code card |
| c12 | p05 | 5.0 | 下一集，我们看产品上线以后，创始人为什么不能继续做所有事情的中转站。 | none | 下一集：创始人别当中转站。 | bridge | 创始人不能继续当中转站 | EP04 router preview |

## Pronunciation Flags

| Chunk | Term | Handling |
|---|---|---|
| c01, c07, c09, c10 | `AI` | TTS input may use `A I`; subtitle and visual text use `AI`. |
| c04 | `MVP` | TTS input may use `M V P`; subtitle and visual text use `MVP`. |

## Chunk QA

Pass:
- No chunk expected to exceed 8 seconds.
- Each chunk has one focus phrase.
- No unverified metrics or product availability claims.
- No full Claude Code tutorial.

Open risks before TTS:
- c04 and c09 are dense; retake or split if generated voice sounds rushed.
- `架构上下文` needs clear pronunciation.

## Next Milestone

Run TTS production, ASR QA, and voice manifest lock.
