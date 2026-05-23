# Voice QA

Status: pass.

## Final Voice Build

- TTS generated 12 scene-level chunks from `script.md`.
- Model: `gpt-4o-mini-tts`.
- Voice: `marin`.
- Total measured duration: 103.656 seconds.
- Scene graph timings were updated from measured audio.
- Audio chunks were copied to `remotion/public/building-effective-ai-agents/audio/`.
- Final Remotion render uses sequence-level audio, not a sidecar subtitle workflow.

## ASR QA

- Status: pass.
- Transcript saved to `asr.txt`.
- Review chunks: none.

## Pronunciation Fixes Applied

- `Sequential Workflow` was rewritten as `顺序工作流` for natural Mandarin delivery.
- The control-list line was rewritten as `权限控制、日志记录、监控、评估、回滚、人工接管` to avoid unclear pronunciation.

## Remaining Risk

ASR passed, but final publication still needs one manual full watch/listen pass because ASR can normalize English technical terms differently from human perception.
