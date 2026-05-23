# ASR QA

Slug: `the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code`

## Gate Status

- Stage: `ASR QA`
- Status: `Pass`
- Pause required: `yes`
- Provider: `openai`
- Model: `gpt-4o-mini-transcribe`
- Selected audio: `chunks-qwen/c01.wav` through `chunks-qwen/c12.wav`
- Transcript evidence: `asr.txt`
- Review chunks: `none`
- Next approved stage: `voice manifest`
- Not approved yet: `scene graph`, `visual production`, `render`

## Decision

All selected Qwen takes pass ASR core-match and required-term checks.
Proceed to voice manifest creation using the selected chunk audio and measured durations.

## Chunk Results

| Chunk | Similarity | Core | Terms | Status | Notes |
|---|---:|---|---|---|---|
| `c01` | 1.000 | `pass` | `pass` | `pass` |  |
| `c02` | 0.950 | `pass` | `pass` | `pass` |  |
| `c03` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c04` | 1.000 | `pass` | `pass` | `pass` |  |
| `c05` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c06` | 0.971 | `pass` | `pass` | `pass` |  |
| `c07` | 1.000 | `pass` | `pass` | `pass` |  |
| `c08` | 1.000 | `pass` | `not_applicable` | `pass` |  |
| `c09` | 1.000 | `pass` | `pass` | `pass` |  |
| `c10` | 0.980 | `pass` | `pass` | `pass` |  |
| `c11` | 1.000 | `pass` | `pass` | `pass` |  |
| `c12` | 0.968 | `pass` | `pass` | `pass` |  |

## QA Notes

- This gate validates transcript fidelity and required terms by ASR.
- Final listening QA is still required before render because ASR cannot judge tone or fatigue by itself.
