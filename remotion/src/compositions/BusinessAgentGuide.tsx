import {
  AbsoluteFill,
  Audio,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {Artifact} from '../components/Artifact';
import {Background} from '../components/Background';
import {fonts, theme} from '../styles/theme';
import type {Scene, SceneGraph} from '../types';

type BusinessAgentGuideProps = {
  sceneGraph: SceneGraph;
  playbackRate?: number;
};

type SceneRange = {
  scene: Scene;
  start: number;
  end: number;
};

const nonAudienceStageLabels = new Set([
  'hook',
  'intro',
  'opening',
  'setup',
  'bridge',
  'next',
  'outro',
  'cta',
]);

const audienceStageLabel = (scene: Scene) => {
  const label = scene.sectionLabel?.trim();
  if (!label || nonAudienceStageLabels.has(label.toLowerCase())) {
    return null;
  }

  return label;
};

const buildRanges = (sceneGraph: SceneGraph, fps: number, playbackRate: number): SceneRange[] => {
  let cursor = 0;
  return sceneGraph.scenes.map((scene) => {
    const duration = Math.round((scene.durationSeconds * fps) / playbackRate);
    const range = {scene, start: cursor, end: cursor + duration};
    cursor += duration;
    return range;
  });
};

const activeRange = (ranges: SceneRange[], frame: number) => {
  const fallback = ranges[ranges.length - 1];
  if (!fallback) {
    throw new Error('Scene graph must contain at least one scene.');
  }

  return ranges.find((range) => frame >= range.start && frame < range.end) ?? fallback;
};

export const BusinessAgentGuide = ({sceneGraph, playbackRate = 1}: BusinessAgentGuideProps) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const ranges = buildRanges(sceneGraph, fps, playbackRate);
  const range = activeRange(ranges, frame);
  const sceneFrame = frame - range.start;
  const sceneDuration = Math.max(1, range.end - range.start);
  const progress = sceneFrame / sceneDuration;
  const sceneIndex = sceneGraph.scenes.findIndex((scene) => scene.id === range.scene.id);
  const enter = interpolate(sceneFrame, [0, 18], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{color: theme.text}}>
      <Background />
      <AbsoluteFill
        style={{
          padding: '78px 92px 64px',
          display: 'grid',
          gridTemplateColumns: '0.84fr 1.16fr',
          columnGap: 58,
        }}
      >
        <section
          style={{
            opacity: enter,
            transform: `translateY(${(1 - enter) * 26}px)`,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            minWidth: 0,
          }}
        >
          <div>
            <div
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: 14,
                border: `1px solid ${theme.line}`,
                borderRadius: 999,
                padding: '10px 18px',
                color: theme.muted,
                fontFamily: fonts.mono,
                fontSize: 19,
                letterSpacing: 1.4,
                textTransform: 'uppercase',
                background: 'rgba(17,24,32,0.58)',
              }}
              >
                <span
                style={{
                  width: 8,
                  height: 8,
                  borderRadius: 999,
                  background: theme.cyan,
                  boxShadow: `0 0 16px ${theme.cyan}`,
                }}
                />
              {audienceStageLabel(range.scene) ?? 'Architecture Choice'}
            </div>
            <h1
              style={{
                margin: '62px 0 0',
                fontFamily: fonts.display,
                fontSize: 74,
                lineHeight: 1.08,
                letterSpacing: -1.4,
                fontWeight: 900,
                maxWidth: 690,
              }}
            >
              {range.scene.claim}
            </h1>
            <p
              style={{
                margin: '34px 0 0',
                fontFamily: fonts.sans,
                color: theme.muted,
                fontSize: 28,
                lineHeight: 1.48,
                maxWidth: 610,
              }}
            >
              {range.scene.focus}
            </p>
          </div>
          <div
            style={{
              fontFamily: fonts.mono,
              color: theme.muted,
              fontSize: 20,
              letterSpacing: 1,
            }}
          >
            {String(sceneIndex + 1).padStart(2, '0')} /{' '}
            {String(sceneGraph.scenes.length).padStart(2, '0')}
          </div>
        </section>
        <section
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            opacity: enter,
            transform: `scale(${0.982 + enter * 0.018})`,
          }}
        >
          <Artifact scene={range.scene} progress={progress} />
        </section>
      </AbsoluteFill>
      <Subtitle text={range.scene.subtitle} progress={progress} />
      <ProgressRail ranges={ranges} activeSceneId={range.scene.id} frame={frame} />
      <SceneAudio ranges={ranges} playbackRate={playbackRate} />
    </AbsoluteFill>
  );
};

const SceneAudio = ({ranges, playbackRate}: {ranges: SceneRange[]; playbackRate: number}) => {
  return (
    <>
      {ranges.map((range) => {
        if (!range.scene.audioFile) {
          return null;
        }

        return (
          <Sequence
            key={range.scene.id}
            from={range.start}
            durationInFrames={Math.max(1, range.end - range.start)}
          >
            <Audio src={staticFile(range.scene.audioFile)} playbackRate={playbackRate} />
          </Sequence>
        );
      })}
    </>
  );
};

const Subtitle = ({text, progress}: {text: string; progress: number}) => {
  const opacity = interpolate(progress, [0, 0.08, 0.9, 1], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'absolute',
        left: 310,
        right: 310,
        bottom: 58,
        opacity,
        padding: '18px 34px',
        borderRadius: 24,
        background: 'rgba(3, 6, 8, 0.62)',
        boxShadow: '0 18px 64px rgba(0,0,0,0.28)',
        color: theme.text,
        fontFamily: fonts.sans,
        fontSize: 40,
        lineHeight: 1.28,
        fontWeight: 800,
        textAlign: 'center',
      }}
    >
      {text}
    </div>
  );
};

const ProgressRail = ({
  ranges,
  activeSceneId,
  frame,
}: {
  ranges: SceneRange[];
  activeSceneId: string;
  frame: number;
}) => {
  const total = ranges[ranges.length - 1]?.end ?? 1;
  const width = interpolate(frame, [0, total], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const labelRanges = ranges.filter((range, index) => {
    const label = audienceStageLabel(range.scene);
    const prevLabel = index > 0 ? audienceStageLabel(ranges[index - 1].scene) : null;
    return Boolean(label) && label !== prevLabel;
  });

  return (
    <div
      style={{
        position: 'absolute',
        left: 92,
        right: 92,
        top: 30,
        height: 36,
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 18,
          height: 3,
          background: 'rgba(255,255,255,0.08)',
        }}
      >
        <div
          style={{
            width: `${width * 100}%`,
            height: '100%',
            background: theme.cyan,
            boxShadow: `0 0 18px ${theme.cyan}`,
          }}
        />
      </div>
      {ranges.map((range) => (
        <div
          key={range.scene.id}
          style={{
            position: 'absolute',
            left: `${(range.start / total) * 100}%`,
            top: 14,
            width: 11,
            height: 11,
            borderRadius: 999,
            background:
              range.scene.id === activeSceneId ? theme.cyan : 'rgba(255,255,255,0.22)',
            boxShadow:
              range.scene.id === activeSceneId ? `0 0 18px ${theme.cyan}` : 'none',
          }}
        />
      ))}
      {labelRanges.map((range, index) => {
        const label = audienceStageLabel(range.scene);
        const isActive = frame >= range.start;
        const nextRange = labelRanges[index + 1];
        const activeInSection = frame >= range.start && (!nextRange || frame < nextRange.start);

        return (
          <div
            key={`${range.scene.id}-${label}`}
            style={{
              position: 'absolute',
              left: `${(range.start / total) * 100}%`,
              top: -4,
              transform: 'translateX(-2px)',
              fontFamily: fonts.mono,
              fontSize: 14,
              letterSpacing: 0.8,
              textTransform: 'uppercase',
              color: activeInSection ? theme.text : isActive ? theme.cyan : theme.muted,
              opacity: activeInSection ? 1 : 0.58,
              whiteSpace: 'nowrap',
              maxWidth: 190,
              overflow: 'hidden',
              textOverflow: 'ellipsis',
            }}
          >
            {label}
          </div>
        );
      })}
    </div>
  );
};
