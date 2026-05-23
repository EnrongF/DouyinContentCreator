# QA

## Gate Status

- Stage: `final render`
- Status: `pass`
- Voice ASR: `pass`
- Render: `pass`

## Checks Completed

- Rendered vertical cover, grid cover, and `cover.png` alias.
- Rendered MP4 with burned-in subtitles.
- Sampled frames across model access, workflow stack, specificity layers, switching cost, audit question, and final lifecycle close.
- Confirmed no right-edge clipping on workflow cards in sampled frames.
- Confirmed semantic context groups use one forward pass instead of repeated in/out loops.
- Confirmed focus highlight is visible on active entities or connections.

## QA Notes

- c07 headline was tightened after first render because the original long claim split `习惯` awkwardly. Final render uses `最后会变成切换成本。`.
- Background light remains slow and secondary; it gives motion without competing with the content focus.
