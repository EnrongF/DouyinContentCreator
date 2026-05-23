# Remotion Visual QA - EP01 Judgment Bottleneck

## Gate Status

- Stage: `Remotion visual QA / sample still approval`
- Status: `sample stills rendered; pass after text-fit fix; awaiting final render approval`
- Composition: `the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck`
- Frame size: `1080x1920`
- Duration: `2019 frames / 67.30s`
- Visual direction: `A2 Balanced VI + Content Fit`
- Pause required: `yes`
- Next gate if accepted: `final render`
- Not approved yet: `final render`, `Douyin package`

## Samples

Directory:

```text
review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.remotion-samples/
```

Rendered samples:

- `c01-bottleneck.png` at frame `41`
- `c03-lanes.png` at frame `278`
- `c05-early-gate.png` at frame `459`
- `c08-control.png` at frame `707`
- `c10-judgment-node.png` at frame `923`
- `c13-lifecycle.png` at frame `1283`
- `c18-final-decision.png` at frame `1808`
- `c19-demo-gate.png` at frame `1941`

## Findings

### Fixed

- Several longer Chinese headlines produced one-character orphan lines in stills, especially `c05`, `c18`, and `c19`.
- Fix applied in `remotion/src/components/founder-playbook/FounderFrame.tsx`:
  - reduced headline size for medium and long claims;
  - added balanced text wrapping for headline layout.

### Pass

- The approved A2 identity is visible: warm black field, cream headline, amber EP badge, cyan/orange/amber semantic accents, and integrated subtitle without a rectangle.
- Content-specific modules are distinguishable across scenes: bottleneck board, execution lanes, early gate, control split, judgment node, lifecycle gates, decision hold, and demo-demand gate.
- Burned-in subtitle region remains readable and does not collide with central artifacts in the checked frames.
- Source mark is present but quiet; it does not imply source publisher endorsement.

## Verification

Commands run:

```text
npm exec tsc -- --noEmit
npm exec remotion -- still src/index.ts the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck ../review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.remotion-samples/c01-bottleneck.png --frame=41
npm exec remotion -- still src/index.ts the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck ../review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.remotion-samples/c03-lanes.png --frame=278
npm exec remotion -- still src/index.ts the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck ../review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.remotion-samples/c05-early-gate.png --frame=459
npm exec remotion -- still src/index.ts the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck ../review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.remotion-samples/c08-control.png --frame=707
npm exec remotion -- still src/index.ts the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck ../review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.remotion-samples/c10-judgment-node.png --frame=923
npm exec remotion -- still src/index.ts the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck ../review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.remotion-samples/c13-lifecycle.png --frame=1283
npm exec remotion -- still src/index.ts the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck ../review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.remotion-samples/c18-final-decision.png --frame=1808
npm exec remotion -- still src/index.ts the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck ../review/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.remotion-samples/c19-demo-gate.png --frame=1941
```

Result:

```text
TypeScript passed.
All eight selected stills rendered.
Visual QA passes for the sample-still gate after headline fitting fix.
```

## Recommendation

Approve the next milestone: `final render`.

Do not start the `Douyin package` until the final MP4 passes render QA.
