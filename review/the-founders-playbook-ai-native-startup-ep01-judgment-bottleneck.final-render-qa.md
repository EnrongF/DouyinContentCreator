# Final Render QA - EP01 Judgment Bottleneck

## Gate Status

- Stage: `final render`
- Status: `rerendered with C16 visual correction; technical QA passed; awaiting Douyin package approval`
- Output: `douyin/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck/video.mp4`
- Pause required: `yes`
- Next gate if accepted: `Douyin package`
- Not approved yet: `Douyin package`

## Render Command

```text
npm run render:the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck
```

First attempt failed because Chromium launch was blocked by macOS sandbox permissions:

```text
bootstrap_check_in org.chromium.Chromium.MachPortRendezvousServer: Permission denied
```

The render was rerun with approved browser-launch permissions and completed successfully.

Revision note:

```text
The in-video top progress bar was removed because Douyin can create progress UI automatically.
The small scene count in the header remains as content orientation, not a video progress bar.
```

C16 correction:

```text
The C16 visual was changed from the generic lifecycle gate module to a dedicated deferred-gates module.
It now pairs with the voice line "后面才轮到边界、系统和护城河" by showing only MVP/边界, Launch/系统, and Scale/护城河 as later gates.
```

## Output Metadata

Measured with `@remotion/media-parser`:

```text
container: mp4
video codec: h264
audio codec: aac
dimensions: 1080x1920
fps: 30
frames: 2019
duration: 67.35s
audio sample rate: 48000
audio channels: 2
file size: 11,566,292 bytes
estimated video bitrate: 1,048,416 bps
estimated audio bitrate: 317,374 bps
```

## Checks

- MP4 exists at the expected Douyin episode path.
- Output is vertical 9:16 at `1080x1920`.
- Duration matches the Remotion composition and voice-manifest timing tolerance.
- Video and audio streams are present.
- Codec choices are platform-compatible: H.264 video and AAC audio.
- Subtitles are burned into the Remotion composition by design.
- In-video top progress bar has been removed.
- C16 visual now matches the voice/script: later gates only, not the first Idea gate.

## Limitations

- `ffmpeg` and `ffprobe` are not installed in this environment.
- I could not extract frames from the encoded MP4 with local tools. The visual frame gate was covered by the prior Remotion sample-still QA using the same composition and frame numbers.

## Recommendation

Approve the next milestone: `Douyin package`.

The next package gate should produce or update:

- `cover.png`
- `cover.md`
- `caption.md`
- `manifest.md`
- `qa.md`
