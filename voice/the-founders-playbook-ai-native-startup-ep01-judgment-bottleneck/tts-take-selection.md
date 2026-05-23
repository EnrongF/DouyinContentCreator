# TTS Take QA / Selection

Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`

## Gate Status

- Stage: `TTS Take QA / Selection`
- Status: `Pass; ASR passed`
- Pause required: `yes`
- Prior gate: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/tts-takes.md`
- Selected provider: `qwen-dashscope`
- Selected model: `qwen3-tts-instruct-flash`
- Selected voice: `Ethan`
- Selected chunks: `c01-c19`
- Measured speech duration: `61.440 seconds`
- ASR QA: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/asr-qa.md`
- Voice manifest: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/voice-manifest.json`
- Voice QA: `voice/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/qa.md`
- Total timed duration with pauses: `67.300 seconds`
- Next approved stage: `scene graph`
- Not approved yet: `visual production`, `render`

## Selection Decision

Select all generated Qwen takes:

```text
chunks-qwen/c01.wav
...
chunks-qwen/c19.wav
```

Reason:
- All 19 expected WAV files exist.
- Files are valid mono PCM WAV audio.
- Measured total speech duration is within the target `60-75 seconds`.
- No chunk exceeds the 8-second planning target.
- Short chunks c04 and c06 are acceptable because they are deliberate emphasis lines.
- c05, c08, c09, and c14 were regenerated so ASR preserves the intended meaning and required terms.

## Technical QA

| Check | Result |
|---|---|
| Expected chunk count | `19` |
| Actual chunk count | `19` |
| Audio format | `WAVE`, mono, `24000 Hz`, `16-bit PCM` |
| Measured speech duration | `61.440 seconds` |
| Longest chunk | `c19`, `5.200 seconds` |
| Shortest chunk | `c06`, `1.360 seconds` |
| Chunk duration gate | `Pass` |
| File-size sanity | `Pass` |

## ASR Attention Results

| Chunk | Concern | Required ASR check |
|---|---|---|
| `c05` | `执行变快` phrase | Passed after retake replacing `把执行推快`. |
| `c03` | `A I` spoken form | Confirm ASR does not distort the sentence meaning. |
| `c08` | `A I` + `油门 / 方向盘` metaphor | Passed after retake with `A I 这个工具`. |
| `c09` | `帮你决定往哪走` phrase | Passed after retake replacing `替你决定`. |
| `c13` | `M V P` spoken form | Confirm ASR recognizes or acceptably represents the acronym. |
| `c14` | `每个阶段` phrase | Passed after retake replacing `每一关`. |
| `c17` | `A I` spoken form | Confirm rhythm stays natural. |
| `c19` | `Demo` spoken form | Confirm ASR recognizes `Demo` or produces an acceptable equivalent. |

## Selection Notes

- Rejected retakes are preserved in `chunks-qwen/` with `.asr-review-*` suffixes.
- If later listening review finds pronunciation problems, regenerate only the affected chunks.
- `voice-manifest.json` has been created from the selected chunks and ASR report.

## Next Milestone

Create the **scene graph**.

The scene graph should:
- use `voice-manifest.json` as timing authority;
- map chunk-level focus phrases to visual states;
- keep subtitles from the manifest;
- avoid Remotion implementation or render work until the scene graph is accepted.
