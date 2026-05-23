# Manifest

## Package

- Job: Building Effective AI Agents
- Angle: business implementation guide, focused on technical characteristics and when to use/avoid each agent pattern.
- Output folder: `douyin/building-effective-ai-agents/`
- Distribution target: native 16:9 Douyin-ready technical documentary.

## Primary Artifacts

- `../../compression/building-effective-ai-agents.md`: cognition compression source for the episode.
- `../../scene-graphs/building-effective-ai-agents.json`: canonical 16:9 scene graph for Remotion.
- `../../voice/building-effective-ai-agents/`: voice script, pronunciation notes, voice manifest, and voice QA.
- `../../remotion/`: React + Remotion renderer scaffold for the new production stack.
- `video.mp4`: legacy silent draft MP4 with subtitles burned directly into the video frames.
- `video.remotion.mp4`: final native 16:9 Remotion MP4 with scene-synced voice audio and burned-in subtitles.
- `cover.png`: dedicated cover image.
- `cover.md`: cover copy and visual intent.
- `storyboard.html`: review storyboard.
- `contact-sheet.jpg`: visual QA sheet.
- `frames/scene_*.png`: rendered source frames with burned-in subtitles.
- `frame_manifest.json`: frame duration and subtitle manifest.
- `script.md`: full Chinese narration draft.
- `caption.md`: Douyin caption draft.
- `shotlist.md`: scene/beat plan.
- `timing-map.md`: timing and subtitle policy.
- `render_assets.py`: frame/cover/storyboard renderer.
- `render_video.swift`: macOS AVFoundation silent/video renderer.

## Render Commands

Legacy silent draft:

```bash
python3 douyin/building-effective-ai-agents/render_assets.py
swift douyin/building-effective-ai-agents/render_video.swift
```

Remotion target stack, after installing dependencies and generating final voice:

```bash
cd remotion
npm run still:building-effective-ai-agents-cover
npm run render:building-effective-ai-agents
```

## Final Metadata

- Resolution: 1920 x 1080.
- Subtitle policy: subtitles are burned into the MP4 frames; no `.srt` sidecar.
- Current audio status: final TTS voiceover included in `video.remotion.mp4`.
- Voice QA: 12 measured TTS chunks, ASR pass, total measured duration 103.656 seconds.
- Draft video checksum: `80aa63c3c36db7c842d600a9cc387f0c7d26e5cde7a19c4ec96753d6f49b9aae`
- Cover checksum: `ffd32fdd92181b9540a1961dfea491a8b9ed273359f7e9445e6c376dc2f4bb0c`
- Contact sheet checksum: `e55b97619b55e93cf1a173d8f3aa9af639de1e5426cb07239a97b47e6e3506c9`
- Remotion video checksum: `0facfa69849665cbb25113815dbb7b824d62b38152db8c8e752c1abbcbe5aeb9`
- Remotion cover checksum: `af1e24a022120b3233513a2df71be23684d99b4b216157c4d1e293dda01483d6`

## Production Notes

- The video intentionally targets business users deciding how to implement agents in real workflows.
- The central framework is technical-characteristics-based pattern selection:
  `Automation / Workflow / Single Agent / Multi-Agent / Harnessed Agent System`.
- Latest PDF-only value-budget redo treats the provided Anthropic PDF as the source of truth and maps the topic as a full series. The rendered video and TTS audio have not yet been regenerated from that PDF-only scope.
- Original PDF diagrams were extracted under `resources/building-effective-ai-agents/diagrams/` and should be used in future episode renders.
- The historical OpenAI Codex video package is untouched.
