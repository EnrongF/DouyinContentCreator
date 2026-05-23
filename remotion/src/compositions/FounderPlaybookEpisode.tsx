import {AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {FounderFrame} from '../components/founder-playbook/FounderFrame';
import type {FounderScene, FounderSceneGraph, FounderSoundEffect} from '../components/founder-playbook/types';

type FounderPlaybookEpisodeProps = {
  sceneGraph: FounderSceneGraph;
};

type SceneRange = {
  scene: FounderScene;
  start: number;
  end: number;
};

export const founderDurationInFrames = (sceneGraph: FounderSceneGraph) =>
  sceneGraph.scenes.reduce(
    (total, scene) => total + Math.max(1, Math.round(scene.durationSeconds * sceneGraph.format.fps)),
    0,
  );

const buildRanges = (sceneGraph: FounderSceneGraph, fps: number): SceneRange[] => {
  let cursor = 0;
  return sceneGraph.scenes.map((scene) => {
    const duration = Math.max(1, Math.round(scene.durationSeconds * fps));
    const range = {scene, start: cursor, end: cursor + duration};
    cursor += duration;
    return range;
  });
};

const activeRange = (ranges: SceneRange[], frame: number) => {
  const fallback = ranges[ranges.length - 1];
  if (!fallback) {
    throw new Error('Founder Playbook scene graph must contain at least one scene.');
  }

  return ranges.find((range) => frame >= range.start && frame < range.end) ?? fallback;
};

const visualContextKeyFor = (scene: FounderScene) => {
  if (scene.artifact.type === 'attention-audit-lanes') return 'attention-audit-lanes';
  if (scene.artifact.type === 'founder-router-bottleneck') return 'founder-router-bottleneck';
  if (scene.artifact.type === 'model-access-not-moat') return 'model-access-not-moat';
  if (scene.artifact.type === 'workflow-specificity-stack') return 'workflow-specificity-stack';
  if (scene.artifact.type === 'specificity-layer-stack') return 'specificity-layer-stack';
  if (scene.artifact.type === 'copy-gap-barrier' || scene.artifact.type === 'switching-cost-chain') {
    return 'copy-gap-to-switching-cost';
  }
  if (scene.artifact.type === 'workflow-moat-audit') return 'workflow-moat-audit';
  return `${scene.id}:${scene.artifact.type}`;
};

const audioPathFor = (sceneGraph: FounderSceneGraph, scene: FounderScene) =>
  `${sceneGraph.slug}/audio/${scene.id}.wav`;

const sfxFrameFor = (ranges: SceneRange[], effect: FounderSoundEffect, fps: number) => {
  const sceneRange = ranges.find((range) => range.scene.id === effect.sceneId);
  if (!sceneRange) {
    return null;
  }

  return sceneRange.start + Math.max(0, Math.round(effect.atSeconds * fps));
};

export const FounderPlaybookEpisode = ({sceneGraph}: FounderPlaybookEpisodeProps) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const ranges = buildRanges(sceneGraph, fps);
  const range = activeRange(ranges, frame);
  const sceneFrame = frame - range.start;
  const sceneDuration = Math.max(1, range.end - range.start);
  const sceneProgress = sceneFrame / sceneDuration;
  const sceneIndex = sceneGraph.scenes.findIndex((scene) => scene.id === range.scene.id);
  const previousScene = sceneIndex > 0 ? sceneGraph.scenes[sceneIndex - 1] : null;
  const nextScene = sceneIndex >= 0 && sceneIndex < sceneGraph.scenes.length - 1 ? sceneGraph.scenes[sceneIndex + 1] : null;
  const contextKey = visualContextKeyFor(range.scene);
  const isContinuingContext = previousScene ? visualContextKeyFor(previousScene) === contextKey : false;
  const willContinueContext = nextScene ? visualContextKeyFor(nextScene) === contextKey : false;

  return (
    <AbsoluteFill>
      <FounderFrame
        sceneGraph={sceneGraph}
        scene={range.scene}
        sceneIndex={sceneIndex}
        totalScenes={sceneGraph.scenes.length}
        progress={sceneProgress}
        isContinuingContext={isContinuingContext}
        willContinueContext={willContinueContext}
      />
      {ranges.map((sceneRange) => (
        <Sequence
          key={sceneRange.scene.id}
          from={sceneRange.start}
          durationInFrames={Math.max(1, sceneRange.end - sceneRange.start)}
        >
          <Audio src={staticFile(audioPathFor(sceneGraph, sceneRange.scene))} />
        </Sequence>
      ))}
      {(sceneGraph.soundEffects ?? []).map((effect) => {
        const startFrame = sfxFrameFor(ranges, effect, fps);
        if (startFrame === null) {
          return null;
        }

        return (
          <Sequence
            key={effect.id}
            from={startFrame}
            durationInFrames={Math.max(1, Math.round((effect.durationSeconds ?? 0.5) * fps))}
          >
            <Audio src={staticFile(effect.file)} volume={effect.volume ?? 0.14} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
