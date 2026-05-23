# Voice

Store voice scripts, pronunciation notes, TTS chunks, timing manifests, and voice QA.

Root contract: `../VOICE_SYSTEM.md`.

Pattern:

```text
voice/<slug>/
  script.md
  paragraph-plan.md
  pronunciation.md
  voice-manifest.json
  chunks/*.mp3
  voiceover.final.mp3
  asr.txt
  qa.md
```

Rules:
- Design voice by paragraph before TTS.
- Use `speech-chunk-plan.md` for performable chunk boundaries.
- Use Qwen `qwen3-tts-instruct-flash` with voice `Ethan` as the default Chinese voice maker.
- Keep OpenAI `gpt-4o-mini-tts` with `marin` as a fallback and comparison baseline.
- Use `voice-manifest.json` to drive Remotion timing.
- Burn subtitles into final video from the same manifest.
- Follow `../VOICE_SYSTEM.md` for native Chinese, TTS, ASR, and sync gates.
