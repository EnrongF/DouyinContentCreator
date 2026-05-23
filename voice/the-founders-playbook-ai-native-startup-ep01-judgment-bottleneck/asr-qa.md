# ASR QA

Slug: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`

## Gate Status

- Stage: `ASR QA`
- Status: `Pass`
- Pause required: `yes`
- Provider: `openai`
- Model: `gpt-4o-mini-transcribe`
- Selected audio: `chunks-qwen/c01.wav` through `chunks-qwen/c19.wav`
- Transcript evidence: `asr.txt`
- Review chunks: `none`
- Voice manifest: `voice-manifest.json`
- Voice QA: `qa.md`
- Next approved stage: `scene graph`
- Not approved yet: `visual production`, `render`

## Decision

All selected Qwen takes pass ASR core-match and required-term checks.
The voice manifest has been created from the selected chunk audio and measured durations.

## Chunk Results

| Chunk | Similarity | Core | Terms | Status | Notes |
|---|---:|---|---|---|---|
| `c01` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c02` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c03` | 1.000 | `pass` | `pass` | `pass` |  |
| `c04` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c05` | 1.000 | `pass` | `pass` | `pass` |  |
| `c06` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c07` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c08` | 1.000 | `pass` | `pass` | `pass` |  |
| `c09` | 1.000 | `pass` | `pass` | `pass` |  |
| `c10` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c11` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c12` | 0.974 | `pass` | `pass` | `pass` |  |
| `c13` | 1.000 | `pass` | `pass` | `pass` |  |
| `c14` | 1.000 | `pass` | `pass` | `pass` |  |
| `c15` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c16` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c17` | 1.000 | `pass` | `pass` | `pass` |  |
| `c18` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c19` | 0.962 | `pass` | `pass` | `pass` |  |

## QA Notes

- This gate validates transcript fidelity and required terms by ASR.
- Retakes were made for c05, c08, c09, and c14 before this pass.
- Final listening QA is still required before render because ASR cannot judge tone or fatigue by itself.
- `voice-manifest.json` is intentionally not created by this script; it is the next milestone artifact after this gate passes.
