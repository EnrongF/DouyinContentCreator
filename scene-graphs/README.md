# Scene Graphs

Store structured render plans consumed by Remotion.

Pattern:
- `<slug>.json`

Scene graphs are the source of truth for:
- Source value references retained in the episode.
- Series, episode, section, paragraph, and beat hierarchy.
- Scene order.
- Beat text.
- Burned-in subtitles.
- Source references.
- Visual artifacts.
- Focus states.
- Timing intent before measured voice durations.

React/Remotion components must render from the scene graph and should not invent new claims.

Each voice paragraph should map to one primary visual focus. Beats can add focus phrases and cue details, but they should not overload a paragraph with unrelated visual targets.

If a scene carries a non-cuttable source value, keep the related source reference and focus cue explicit so review can verify it was not lost during visual compression.
