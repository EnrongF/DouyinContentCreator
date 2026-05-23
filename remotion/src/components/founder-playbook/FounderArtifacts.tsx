import type React from 'react';
import {interpolate, useCurrentFrame} from 'remotion';
import {FounderSymbol} from './FounderSymbols';
import {founderTheme, symbolForArtifact, toneForArtifact} from './founderTheme';
import type {FounderScene} from './types';

type FounderArtifactProps = {
  scene: FounderScene;
  progress: number;
  isContinuingContext?: boolean;
};

const c = founderTheme.colors;
const fonts = founderTheme.fonts;

const clamp = (value: number, min = 0, max = 1) => Math.min(max, Math.max(min, value));

const reveal = (progress: number, start: number, end: number) =>
  interpolate(progress, [start, end], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

const ModuleShell = ({
  scene,
  progress,
  title,
  meta,
  children,
  stableContent,
}: {
  scene: FounderScene;
  progress: number;
  title: string;
  meta: string;
  children: React.ReactNode;
  stableContent?: boolean;
}) => {
  const tone = toneForArtifact(scene.artifact.type);
  const symbol = symbolForArtifact(scene.artifact.type);

  return (
    <div
      style={{
        position: 'relative',
        height: '100%',
        overflow: 'hidden',
        borderTop: `2px solid ${c.cyan}80`,
        paddingTop: 28,
      }}
    >
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: '42px minmax(0, 1fr) auto',
          alignItems: 'center',
          gap: 14,
          color: c.muted,
          fontFamily: fonts.mono,
          fontSize: 18,
          fontWeight: 900,
          letterSpacing: 0.7,
          textTransform: 'uppercase',
        }}
      >
        <FounderSymbol kind={symbol} size={38} />
        <span style={{color: c.cyan}}>{title}</span>
        <span>{meta}</span>
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 92,
          bottom: 0,
          opacity: stableContent ? 1 : reveal(progress, 0.02, 0.16),
          transform: stableContent ? 'none' : `translateY(${(1 - reveal(progress, 0.02, 0.16)) * 22}px)`,
          filter: `drop-shadow(0 0 30px ${tone}1f)`,
        }}
      >
        {children}
      </div>
    </div>
  );
};

const Track = ({
  label,
  endLabel,
  active,
  offset,
}: {
  label: string;
  endLabel: string;
  active: number;
  offset: number;
}) => {
  const width = `${Math.round(clamp(active) * 100)}%`;
  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: offset,
        height: 58,
        display: 'grid',
        gridTemplateColumns: '92px 1fr 86px',
        alignItems: 'center',
        gap: 18,
        color: c.soft,
        fontFamily: fonts.cn,
        fontSize: 24,
        fontWeight: 900,
      }}
    >
      <b
        style={{
          height: 42,
          display: 'grid',
          placeItems: 'center',
          borderRadius: 8,
          color: active > 0.75 ? '#111416' : c.ink,
          background: active > 0.75 ? c.amber : c.panel,
          border: `1px solid ${active > 0.75 ? 'transparent' : c.line}`,
        }}
      >
        {label}
      </b>
      <span
        style={{
          height: 7,
          borderRadius: 999,
          background: 'rgba(255,248,234,0.1)',
          overflow: 'hidden',
        }}
      >
        <i
          style={{
            display: 'block',
            width,
            height: '100%',
            borderRadius: 999,
            background: `linear-gradient(90deg, ${c.orange}, ${c.cyan})`,
            boxShadow: `0 0 22px ${c.cyan}55`,
          }}
        />
      </span>
      <span style={{fontSize: 20, color: active > 0.75 ? c.ink : c.muted}}>{endLabel}</span>
    </div>
  );
};

const BottleneckMap = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="bottleneck map" meta="blocked lane">
    <Track label="Idea" endLabel="清楚" active={reveal(progress, 0.05, 0.25)} offset={18} />
    <Track label="Build" endLabel="卡住" active={reveal(progress, 0.2, 0.55)} offset={102} />
    <Track label="Ship" endLabel="变慢" active={reveal(progress, 0.45, 0.82)} offset={186} />
  </ModuleShell>
);

const WrongDirectionPath = ({scene, progress}: FounderArtifactProps) => {
  const draw = reveal(progress, 0.1, 0.62);
  const isRisk = scene.artifact.type.includes('wrong');
  return (
    <ModuleShell scene={scene} progress={progress} title="wrong path" meta={isRisk ? 'risk' : 'path'}>
      <svg viewBox="0 0 760 360" style={{position: 'absolute', inset: 0, width: '100%', height: '100%'}}>
        <path
          d="M52 244 C188 170 318 128 616 98"
          fill="none"
          stroke="rgba(50,200,232,0.22)"
          strokeWidth="7"
          strokeDasharray="16 16"
        />
        <path
          d="M52 244 C190 190 290 240 660 286"
          fill="none"
          stroke={c.orange}
          strokeWidth="9"
          strokeLinecap="round"
          strokeDasharray={720}
          strokeDashoffset={720 - 720 * draw}
        />
      </svg>
      <LabelCard right={18} top={34} color={c.cyan} text="Target" />
      <LabelCard right={48} bottom={34} color={c.rose} text="Wrong Direction" />
    </ModuleShell>
  );
};

const LabelCard = ({
  text,
  color,
  top,
  right,
  bottom,
}: {
  text: string;
  color: string;
  top?: number;
  right?: number;
  bottom?: number;
}) => (
  <div
    style={{
      position: 'absolute',
      top,
      right,
      bottom,
      width: 156,
      height: 72,
      display: 'grid',
      placeItems: 'center',
      borderRadius: 8,
      border: `1px solid ${color}80`,
      background: `${color}1f`,
      color,
      fontFamily: fonts.ui,
      fontSize: 22,
      fontWeight: 950,
      textAlign: 'center',
    }}
  >
    {text}
  </div>
);

const ExecutionLanes = ({scene, progress}: FounderArtifactProps) => {
  const labels = scene.artifact.nodes.length >= 4 ? scene.artifact.nodes : ['调研', '代码', '文档', '运营'];
  return (
    <ModuleShell scene={scene} progress={progress} title="lane activation" meta="parallel">
      <div style={{position: 'absolute', inset: '18px 0 0', display: 'grid', gap: 28, alignContent: 'center'}}>
        {labels.slice(0, 4).map((label, index) => {
          const active = reveal(progress, 0.12 + index * 0.12, 0.36 + index * 0.12);
          return (
            <div
              key={label}
              style={{
                display: 'grid',
                gridTemplateColumns: '86px 1fr 66px',
                alignItems: 'center',
                gap: 18,
                color: c.soft,
                fontFamily: fonts.cn,
                fontSize: 25,
                fontWeight: 900,
              }}
            >
              <span>{label}</span>
              <span style={{height: 7, borderRadius: 999, background: 'rgba(255,248,234,0.08)', overflow: 'hidden'}}>
                <i
                  style={{
                    display: 'block',
                    width: `${Math.round(active * 100)}%`,
                    height: '100%',
                    borderRadius: 999,
                    background: c.cyan,
                    boxShadow: `0 0 22px ${c.cyan}66`,
                  }}
                />
              </span>
              <b
                style={{
                  height: 48,
                  display: 'grid',
                  placeItems: 'center',
                  borderRadius: 999,
                  color: '#111416',
                  background: c.amber,
                  fontFamily: fonts.ui,
                  fontSize: 20,
                  opacity: 0.5 + active * 0.5,
                }}
              >
                AI
              </b>
            </div>
          );
        })}
      </div>
    </ModuleShell>
  );
};

const RetainedExecutionLayer = ({scene, progress}: FounderArtifactProps) => {
  const layers = [
    ['AI', '辅助与加速'],
    ['执行', '仍然存在'],
    ['判断', '更早暴露'],
  ];
  return (
    <ModuleShell scene={scene} progress={progress} title="retained layer" meta="guardrail">
      {layers.map(([label, body], index) => {
        const active = index === 1 || progress > index * 0.2;
        return (
          <div
            key={label}
            style={{
              position: 'absolute',
              left: 20,
              right: 20,
              top: 24 + index * 88,
              minHeight: 66,
              display: 'grid',
              gridTemplateColumns: '112px 1fr',
              alignItems: 'center',
              gap: 18,
              border: `1px solid ${active ? c.amber : c.line}`,
              borderRadius: 8,
              padding: '13px 18px',
              background: active ? `${c.amber}20` : c.panel,
              color: c.soft,
              fontFamily: fonts.cn,
              fontSize: 23,
              fontWeight: 900,
            }}
          >
            <b style={{color: c.ink}}>{label}</b>
            <span>{body}</span>
          </div>
        );
      })}
    </ModuleShell>
  );
};

const EarlyDecisionGate = ({scene, progress}: FounderArtifactProps) => {
  const gateX = interpolate(progress, [0, 0.74], [468, 214], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <ModuleShell scene={scene} progress={progress} title="early gate" meta="time shift">
      <div style={{position: 'absolute', left: 16, right: 16, top: 156, height: 7, borderRadius: 999, background: `linear-gradient(90deg, ${c.orange}, ${c.cyan}, rgba(255,248,234,0.12))`}} />
      <GateCard left={480} top={110} muted text={'原来\n更晚判断'} />
      <GateCard left={gateX} top={106} text={'现在\n更早暴露'} />
    </ModuleShell>
  );
};

const GateCard = ({left, top, text, muted}: {left: number; top: number; text: string; muted?: boolean}) => (
  <div
    style={{
      position: 'absolute',
      left,
      top,
      width: 136,
      height: 104,
      display: 'grid',
      placeItems: 'center',
      borderRadius: 8,
      border: `1px solid ${muted ? c.line : c.amber}`,
      background: muted ? c.panel : `${c.amber}24`,
      color: muted ? c.muted : c.ink,
      fontFamily: fonts.cn,
      fontSize: 22,
      fontWeight: 950,
      textAlign: 'center',
      whiteSpace: 'pre-line',
      boxShadow: muted ? 'none' : `0 0 28px ${c.amber}30`,
    }}
  >
    {text}
  </div>
);

const SpeedNeutralMarker = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="speed marker" meta="neutral">
    <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 22, position: 'absolute', inset: '54px 0 0'}}>
      <DecisionTile label="速度" active progress={progress} tone={c.cyan} detail="不是问题" />
      <DecisionTile label="方向" progress={progress} tone={c.amber} detail="仍需判断" />
    </div>
  </ModuleShell>
);

const ControlSplit = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="control split" meta="distinction">
    <div style={{position: 'absolute', inset: '28px 0 0', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 22, alignItems: 'center'}}>
      <ControlPanel label="油门" detail="AI 加速" kind="dial" progress={progress} />
      <ControlPanel label="方向盘" detail="创始人判断" kind="wheel" progress={progress} />
    </div>
  </ModuleShell>
);

const ControlPanel = ({label, detail, kind, progress}: {label: string; detail: string; kind: 'dial' | 'wheel'; progress: number}) => (
  <div
    style={{
      minHeight: 216,
      display: 'grid',
      placeItems: 'center',
      alignContent: 'center',
      gap: 18,
      border: `1px solid ${c.line}`,
      borderRadius: 8,
      background: c.panel,
      color: c.soft,
      fontFamily: fonts.cn,
      fontSize: 24,
      fontWeight: 950,
      textAlign: 'center',
    }}
  >
    <span
      style={{
        width: kind === 'dial' ? 82 : 92,
        height: kind === 'dial' ? 82 : 92,
        borderRadius: 999,
        border: `${kind === 'dial' ? 12 : 9}px solid ${kind === 'dial' ? 'rgba(255,248,234,0.16)' : c.cyan}`,
        borderTopColor: kind === 'dial' ? c.orange : c.cyan,
        transform: kind === 'dial' ? `rotate(${-20 + progress * 78}deg)` : `rotate(${-6 + progress * 12}deg)`,
        boxShadow: kind === 'wheel' ? `inset 0 0 0 20px ${c.cyan}18` : 'none',
      }}
    />
    <span>
      {label}
      <br />
      <small style={{color: c.muted, fontFamily: fonts.ui, fontSize: 18}}>{detail}</small>
    </span>
  </div>
);

const FounderJudgmentNode = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="judgment node" meta="bottleneck">
    <div style={{position: 'absolute', inset: 0}}>
      {['问题', '证据', '做', '停'].map((label, index) => {
        const positions = [
          {left: 28, top: 44},
          {right: 28, top: 44},
          {left: 28, bottom: 44},
          {right: 28, bottom: 44},
        ];
        return <Spoke key={label} label={label} style={positions[index]} />;
      })}
      <div
        style={{
          position: 'absolute',
          left: '50%',
          top: '45%',
          width: 178,
          height: 128,
          transform: `translate(-50%, -50%) scale(${0.92 + reveal(progress, 0.1, 0.55) * 0.08})`,
          display: 'grid',
          placeItems: 'center',
          border: `1px solid ${c.amber}`,
          borderRadius: 8,
          background: `${c.amber}26`,
          color: c.ink,
          fontFamily: fonts.cn,
          fontSize: 26,
          fontWeight: 950,
          textAlign: 'center',
          boxShadow: `0 0 34px ${c.amber}2e`,
        }}
      >
        创始人
        <br />
        判断
      </div>
    </div>
  </ModuleShell>
);

const Spoke = ({label, style}: {label: string; style: React.CSSProperties}) => (
  <div
    style={{
      position: 'absolute',
      width: 116,
      height: 58,
      display: 'grid',
      placeItems: 'center',
      border: `1px solid ${c.line}`,
      borderRadius: 8,
      background: c.panel,
      color: c.soft,
      fontFamily: fonts.cn,
      fontSize: 22,
      fontWeight: 900,
      ...style,
    }}
  >
    {label}
  </div>
);

const GoStopDecisionCards = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="go / stop" meta="split decision">
    <div style={{position: 'absolute', inset: '54px 0 0', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 22}}>
      <DecisionTile label="值得做" detail="Go" active={progress > 0.22} progress={progress} tone={c.cyan} />
      <DecisionTile label="先停" detail="Stop" active={progress > 0.42} progress={progress} tone={c.amber} />
    </div>
  </ModuleShell>
);

const DecisionTile = ({
  label,
  detail,
  active,
  progress,
  tone,
}: {
  label: string;
  detail: string;
  active?: boolean;
  progress: number;
  tone: string;
}) => (
  <div
    style={{
      minHeight: 186,
      display: 'grid',
      placeItems: 'center',
      alignContent: 'center',
      gap: 12,
      border: `1px solid ${active ? tone : c.line}`,
      borderRadius: 8,
      background: active ? `${tone}22` : c.panel,
      color: active ? c.ink : c.muted,
      fontFamily: fonts.cn,
      fontSize: 36,
      fontWeight: 950,
      transform: `translateY(${(1 - reveal(progress, 0.08, 0.45)) * 12}px)`,
      boxShadow: active ? `0 0 28px ${tone}26` : 'none',
    }}
  >
    {label}
    <small style={{fontFamily: fonts.ui, fontSize: 20, color: active ? tone : c.muted}}>{detail}</small>
  </div>
);

const JudgmentGateSequence = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="judgment chain" meta="tools recede">
    <div style={{position: 'absolute', inset: '48px 0 0', display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 12}}>
      {['工具', '证据', '判断', '行动'].map((label, index) => (
        <GateStep key={label} label={label} active={progress > index * 0.16} primary={index === 2} />
      ))}
    </div>
  </ModuleShell>
);

const GateStep = ({label, active, primary}: {label: string; active: boolean; primary?: boolean}) => (
  <div
    style={{
      minHeight: 174,
      alignSelf: 'center',
      display: 'grid',
      placeItems: 'center',
      border: `1px solid ${primary ? c.amber : active ? c.cyan : c.line}`,
      borderRadius: 8,
      background: primary ? `${c.amber}24` : active ? `${c.cyan}14` : c.panel,
      color: active ? c.ink : c.muted,
      fontFamily: fonts.cn,
      fontSize: 26,
      fontWeight: 950,
    }}
  >
    {label}
  </div>
);

const LifecycleGates = ({scene, progress}: FounderArtifactProps) => {
  const defaults = ['Idea', 'MVP', 'Launch', 'Scale'];
  const labels = scene.artifact.nodes.length >= 4 ? scene.artifact.nodes.slice(0, 4) : defaults;
  const sublabels =
    scene.artifact.type === 'different-judgment-icons'
      ? ['该不该做', '边界清不清', '能否脱手', '是否可防守']
      : ['该不该做', '边界', '系统', '护城河'];
  return (
    <ModuleShell scene={scene} progress={progress} title="lifecycle gates" meta="source order">
      <div style={{position: 'absolute', inset: '62px 0 0', display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 12}}>
        {labels.map((label, index) => {
          const active = progress > index * 0.13;
          const primary = scene.artifact.type === 'idea-stage-gate' ? index === 0 : active;
          return (
            <div
              key={`${label}-${index}`}
              style={{
                minHeight: primary ? 190 : 156,
                alignSelf: primary ? 'start' : 'center',
                display: 'grid',
                placeItems: 'center',
                alignContent: 'center',
                gap: 10,
                border: `1px solid ${primary ? c.amber : active ? c.cyan : c.line}`,
                borderRadius: 8,
                background: primary ? c.amber : active ? `${c.cyan}14` : c.panel,
                color: primary ? '#111416' : active ? c.ink : c.muted,
                fontFamily: fonts.ui,
                fontSize: 23,
                fontWeight: 950,
                textAlign: 'center',
                opacity: scene.artifact.type === 'later-gates-deferred' && index > 0 ? 0.58 : 1,
              }}
            >
              {label}
              <small style={{fontFamily: fonts.cn, fontSize: 16, color: primary ? '#25302f' : c.muted}}>
                {sublabels[index]}
              </small>
            </div>
          );
        })}
      </div>
    </ModuleShell>
  );
};

const LaterGatesDeferred = ({scene, progress}: FounderArtifactProps) => {
  const gates = [
    {stage: 'MVP', label: '边界', detail: '先定清楚'},
    {stage: 'Launch', label: '系统', detail: '以后再脱手'},
    {stage: 'Scale', label: '护城河', detail: '最后才积累'},
  ];

  return (
    <ModuleShell scene={scene} progress={progress} title="deferred gates" meta="later episodes">
      <div
        style={{
          position: 'absolute',
          inset: '48px 0 0',
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: 16,
          alignItems: 'center',
        }}
      >
        {gates.map((gate, index) => {
          const active = reveal(progress, 0.12 + index * 0.12, 0.34 + index * 0.12);
          return (
            <div
              key={gate.stage}
              style={{
                minHeight: 206,
                display: 'grid',
                placeItems: 'center',
                alignContent: 'center',
                gap: 12,
                border: `1px solid rgba(255,248,234,${0.16 + active * 0.12})`,
                borderRadius: 8,
                background: `linear-gradient(180deg, rgba(255,248,234,${0.05 + active * 0.05}), rgba(255,248,234,0.025))`,
                color: c.ink,
                fontFamily: fonts.cn,
                textAlign: 'center',
                opacity: 0.52 + active * 0.36,
                transform: `translateY(${(1 - active) * 18}px)`,
              }}
            >
              <span style={{fontFamily: fonts.ui, color: c.muted, fontSize: 18, fontWeight: 900}}>{gate.stage}</span>
              <b style={{fontSize: 34, fontWeight: 950}}>{gate.label}</b>
              <small style={{fontSize: 17, color: c.muted, fontWeight: 850}}>{gate.detail}</small>
            </div>
          );
        })}
      </div>
      <div
        style={{
          position: 'absolute',
          left: 22,
          right: 22,
          bottom: 26,
          height: 6,
          borderRadius: 999,
          background: 'rgba(255,248,234,0.1)',
          overflow: 'hidden',
        }}
      >
        <span
          style={{
            display: 'block',
            width: `${Math.round(reveal(progress, 0.08, 0.72) * 100)}%`,
            height: '100%',
            borderRadius: 999,
            background: `linear-gradient(90deg, ${c.cyan}, ${c.amber})`,
            opacity: 0.62,
          }}
        />
      </div>
    </ModuleShell>
  );
};

const FinalQuestion = ({scene, progress}: FounderArtifactProps) => {
  const activeJudgment = scene.artifact.type !== 'speed-question-dim';
  return (
    <ModuleShell scene={scene} progress={progress} title="decision hold" meta="takeaway">
      <div style={{position: 'absolute', inset: '52px 0 0', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 22}}>
        <DecisionTile label="速度" detail="Speed" active={!activeJudgment && progress < 0.45} progress={progress} tone={c.cyan} />
        <DecisionTile label="判断" detail="Judgment" active={activeJudgment || progress >= 0.45} progress={progress} tone={c.amber} />
      </div>
    </ModuleShell>
  );
};

const DemoDemandGate = ({scene, progress}: FounderArtifactProps) => {
  const move = interpolate(progress, [0.08, 0.62], [0, 58], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <ModuleShell scene={scene} progress={progress} title="blocked demand gate" meta="next episode">
      <div style={{position: 'absolute', inset: '56px 0 0'}}>
        <div style={{position: 'absolute', left: 18 + move, top: 76, width: 150, height: 112, ...cardStyle(c.ink)}}>
          Demo
          <br />
          做出来
        </div>
        <div
          style={{
            position: 'absolute',
            left: 252,
            right: 210,
            top: 130,
            height: 7,
            borderRadius: 999,
            background: `linear-gradient(90deg, ${c.cyan}, ${c.rose})`,
            opacity: reveal(progress, 0.2, 0.58),
          }}
        />
        <div style={{position: 'absolute', right: 18, top: 72, width: 160, height: 120, ...cardStyle(c.rose)}}>
          需求
          <br />
          未解锁
        </div>
      </div>
    </ModuleShell>
  );
};

const fittedFontSize = (text: string, large = 32, medium = 27, small = 22) => {
  if (text.length > 11) return small;
  if (text.length > 6) return medium;
  return large;
};

type ConceptKind = 'build' | 'signal' | 'threshold' | 'void' | 'mismatch' | 'question' | 'boundary' | 'proof' | 'evidence';

const ConceptGlyph = ({kind, tone, active = 1, size = 74}: {kind: ConceptKind; tone: string; active?: number; size?: number}) => {
  const common = {
    fill: 'none',
    strokeLinecap: 'round' as const,
    strokeLinejoin: 'round' as const,
  };
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" aria-hidden="true" style={{opacity: 0.45 + active * 0.55}}>
      <rect x="13" y="13" width="74" height="74" rx="8" fill="rgba(255,248,234,0.035)" stroke="rgba(255,248,234,0.14)" strokeWidth="2" />
      {kind === 'build' && (
        <>
          <rect x="27" y="30" width="46" height="10" rx="5" fill={tone} opacity="0.72" />
          <rect x="27" y="47" width="46" height="10" rx="5" fill={c.amber} opacity="0.82" />
          <rect x="27" y="64" width="46" height="10" rx="5" fill={c.cyan} opacity="0.54" />
        </>
      )}
      {kind === 'signal' && (
        <>
          <path d="M24 72H76" {...common} stroke="rgba(255,248,234,0.2)" strokeWidth="5" />
          <rect x="30" y="52" width="9" height="20" rx="4.5" fill={c.rose} opacity="0.62" />
          <rect x="46" y="39" width="9" height="33" rx="4.5" fill={c.amber} opacity="0.82" />
          <rect x="62" y="25" width="9" height="47" rx="4.5" fill={c.cyan} />
        </>
      )}
      {kind === 'threshold' && (
        <>
          <path d="M18 66H82" {...common} stroke="rgba(255,248,234,0.22)" strokeWidth="6" />
          <path d="M18 66C31 66 34 45 47 45C60 45 62 27 82 27" {...common} stroke={c.cyan} strokeWidth="7" />
          <path d="M61 18V82" {...common} stroke={c.amber} strokeWidth="5" />
        </>
      )}
      {kind === 'void' && (
        <>
          <rect x="30" y="30" width="40" height="40" rx="8" {...common} stroke={c.rose} strokeWidth="6" strokeDasharray="8 8" />
          <path d="M42 50H58" {...common} stroke="rgba(255,248,234,0.28)" strokeWidth="5" />
        </>
      )}
      {kind === 'mismatch' && (
        <>
          <path d="M18 34H40C61 34 58 66 82 66" {...common} stroke={c.rose} strokeWidth="6" />
          <path d="M18 66H42C60 66 58 34 82 34" {...common} stroke={c.cyan} strokeWidth="6" />
          <circle cx="50" cy="50" r="8" fill={c.amber} />
        </>
      )}
      {kind === 'question' && (
        <>
          <circle cx="28" cy="64" r="7" fill={c.amber} />
          <circle cx="50" cy="46" r="7" fill={c.cyan} />
          <circle cx="73" cy="30" r="7" fill={c.cyan} opacity="0.76" />
          <path d="M28 64L50 46L73 30" {...common} stroke={c.cyan} strokeWidth="6" />
        </>
      )}
      {kind === 'boundary' && (
        <>
          <rect x="25" y="24" width="50" height="52" rx="7" {...common} stroke={c.amber} strokeWidth="6" />
          <path d="M40 25V75M60 25V75" {...common} stroke="rgba(255,248,234,0.24)" strokeWidth="4" />
          <path d="M25 50H75" {...common} stroke={c.cyan} strokeWidth="6" />
        </>
      )}
      {kind === 'proof' && (
        <>
          <path d="M26 52L43 68L76 30" {...common} stroke={tone} strokeWidth="8" opacity="0.46" />
          <path d="M27 28L75 76M75 28L27 76" {...common} stroke={c.rose} strokeWidth="5" />
        </>
      )}
      {kind === 'evidence' && (
        <>
          <path d="M24 70H76" {...common} stroke="rgba(255,248,234,0.2)" strokeWidth="5" />
          <rect x="30" y="44" width="10" height="26" rx="5" fill={c.rose} opacity="0.6" />
          <rect x="46" y="31" width="10" height="39" rx="5" fill={c.amber} opacity="0.82" />
          <rect x="62" y="20" width="10" height="50" rx="5" fill={c.cyan} />
        </>
      )}
    </svg>
  );
};

const FlowCard = ({
  label,
  detail,
  tone,
  active,
  concept,
  style,
}: {
  label: string;
  detail?: string;
  tone: string;
  active: number;
  concept?: ConceptKind;
  style?: React.CSSProperties;
}) => (
  <div
    style={{
      minHeight: 132,
      display: 'grid',
      placeItems: 'center',
      alignContent: 'center',
      gap: 10,
      padding: '18px 16px',
      borderRadius: 8,
      border: `1px solid ${active > 0.5 ? tone : c.line}`,
      background: active > 0.5 ? `${tone}22` : c.panel,
      color: active > 0.5 ? c.ink : c.muted,
      fontFamily: fonts.cn,
      fontSize: fittedFontSize(label),
      fontWeight: 950,
      textAlign: 'center',
      lineHeight: 1.15,
      opacity: 0.42 + active * 0.58,
      transform: `translateY(${(1 - active) * 16}px)`,
      boxShadow: active > 0.65 ? `0 0 28px ${tone}28` : 'none',
      ...style,
    }}
  >
    {concept && <ConceptGlyph kind={concept} tone={tone} active={active} />}
    {label}
    {detail && <small style={{fontFamily: fonts.ui, color: tone, fontSize: 17, fontWeight: 900}}>{detail}</small>}
  </div>
);

const Arrow = ({active, tone = c.cyan, vertical}: {active: number; tone?: string; vertical?: boolean}) => (
  <div
    style={{
      width: vertical ? 7 : '100%',
      height: vertical ? '100%' : 7,
      minHeight: vertical ? 54 : 7,
      justifySelf: 'center',
      alignSelf: 'center',
      borderRadius: 999,
      background: 'rgba(255,248,234,0.1)',
      overflow: 'hidden',
      position: 'relative',
    }}
  >
    <span
      style={{
        display: 'block',
        width: vertical ? '100%' : `${Math.round(active * 100)}%`,
        height: vertical ? `${Math.round(active * 100)}%` : '100%',
        borderRadius: 999,
        background: tone,
        boxShadow: `0 0 20px ${tone}66`,
      }}
    />
  </div>
);

const DemoFastBuild = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="demo build path" meta="fast, not evidence">
    <div
      style={{
        position: 'absolute',
        inset: '58px 0 0',
        display: 'grid',
        gridTemplateColumns: '1fr 82px 1fr 82px 1.2fr',
        alignItems: 'center',
        gap: 10,
      }}
    >
      <FlowCard label="想法" detail="Idea" tone={c.soft} active={reveal(progress, 0.02, 0.18)} concept="build" />
      <Arrow active={reveal(progress, 0.14, 0.34)} tone={c.orange} />
      <FlowCard label="AI" detail="加速" tone={c.orange} active={reveal(progress, 0.22, 0.42)} concept="threshold" />
      <Arrow active={reveal(progress, 0.36, 0.58)} tone={c.orange} />
      <FlowCard label="原型态" detail="Demo" tone={c.amber} active={reveal(progress, 0.48, 0.76)} concept="build" style={{minHeight: 214}} />
    </div>
  </ModuleShell>
);

const DemoFalseValidation = ({scene, progress}: FounderArtifactProps) => {
  const stamp = reveal(progress, 0.2, 0.5);
  const empty = reveal(progress, 0.45, 0.82);
  return (
    <ModuleShell scene={scene} progress={progress} title="false validation" meta="empty evidence">
      <div style={{position: 'absolute', inset: '34px 0 0', display: 'grid', gridTemplateColumns: '1fr 1.05fr', gap: 28}}>
        <div style={{position: 'relative', display: 'grid', alignContent: 'center'}}>
          <FlowCard label="完成感" detail="Demo" tone={c.orange} active={reveal(progress, 0.08, 0.28)} concept="proof" style={{minHeight: 274}} />
          <div
            style={{
              position: 'absolute',
              right: 28,
              top: 88,
              width: 150,
              height: 68,
              display: 'grid',
              placeItems: 'center',
              border: `2px solid ${c.rose}`,
              borderRadius: 8,
              color: c.rose,
              fontFamily: fonts.ui,
              fontSize: 22,
              fontWeight: 950,
              transform: `rotate(-10deg) scale(${0.72 + stamp * 0.28})`,
              opacity: stamp * 0.82,
            }}
          >
            PROOF?
          </div>
        </div>
        <div
          style={{
            minHeight: 244,
            alignSelf: 'center',
            display: 'grid',
            alignContent: 'center',
            gap: 18,
            padding: 24,
            borderRadius: 8,
            border: `1px solid ${empty > 0.5 ? c.rose : c.line}`,
            background: 'rgba(255,248,234,0.035)',
            color: c.muted,
            fontFamily: fonts.cn,
            fontWeight: 950,
          }}
        >
          <span style={{fontFamily: fonts.ui, color: c.muted, fontSize: 19}}>Evidence Panel</span>
          <span style={{height: 2, background: 'rgba(255,248,234,0.16)'}} />
          <ConceptGlyph kind="void" tone={c.rose} active={empty} size={94} />
          <span style={{fontSize: 36, color: empty > 0.5 ? c.rose : c.muted}}>证据为空</span>
        </div>
      </div>
    </ModuleShell>
  );
};

const DemoToolShift = ({scene, progress}: FounderArtifactProps) => {
  const isQuestionTool = scene.artifact.type === 'demo-question-tool';
  const questionActive = reveal(progress, isQuestionTool ? 0.34 : 0.18, isQuestionTool ? 0.72 : 0.5);
  return (
    <ModuleShell scene={scene} progress={progress} title="demo as tool" meta={isQuestionTool ? 'question lane' : 'keep the tool'}>
      <div style={{position: 'absolute', inset: '36px 0 0', display: 'grid', gridTemplateColumns: '1fr 70px 1fr', gap: 12}}>
        <FlowCard
          label="证明我对了"
          detail={isQuestionTool ? '不是这条路' : '先别删掉'}
          tone={isQuestionTool ? c.rose : c.orange}
          active={isQuestionTool ? 0.35 : reveal(progress, 0.1, 0.36)}
          concept={isQuestionTool ? 'proof' : 'build'}
          style={{minHeight: isQuestionTool ? 152 : 218, opacity: isQuestionTool ? 0.42 : undefined}}
        />
        <Arrow active={questionActive} tone={c.cyan} />
        <FlowCard
          label={isQuestionTool ? '问清楚问题' : '对话道具'}
          detail={isQuestionTool ? '问题是否存在' : '有用'}
          tone={c.cyan}
          active={questionActive}
          concept="question"
          style={{minHeight: isQuestionTool ? 242 : 218}}
        />
      </div>
    </ModuleShell>
  );
};

const ValidationGate = ({scene, progress}: FounderArtifactProps) => {
  const details: Record<string, Array<[string, string, string]>> = {
    'idea-validation-gate': [
      ['1', '问题真实?', '不是能不能做'],
      ['2', '方案匹配?', '解决真实问题'],
      ['3', '信号足够?', '支持 MVP'],
    ],
    'validation-check-real-problem': [
      ['真实', '不是假设', '用户确实遇到'],
      ['具体', '不是泛泛痛点', '场景能说清'],
      ['经常发生', '不是偶发', '频率足够'],
    ],
    'validation-check-solution-fit': [
      ['想象的问题', '先降权', '创始人假设'],
      ['真实的问题', '主焦点', '用户现场'],
      ['方案匹配', '再判断', '是否解决它'],
    ],
    'validation-check-enough-signal': [
      ['访谈', '过去行为', '不是礼貌表态'],
      ['信号阈值', '够就前进', '不是确定性'],
      ['MVP', '下一关', '开始最小验证'],
    ],
  };
  const rows = details[scene.artifact.type] ?? details['idea-validation-gate'];
  return (
    <ModuleShell scene={scene} progress={progress} title="validation gate" meta="content-fitted checks">
      <div style={{position: 'absolute', inset: '24px 0 0', display: 'grid', gridTemplateColumns: '1fr', gap: 14}}>
        {rows.map(([label, title, detail], index) => {
          const active = reveal(progress, 0.08 + index * 0.13, 0.32 + index * 0.13);
          const isFocus = scene.focusPhrase?.includes(title.replace('?', '')) || scene.artifact.highlight?.includes(title.replace('?', ''));
          return (
            <div
              key={title}
              style={{
                minHeight: isFocus ? 118 : 98,
                display: 'grid',
                gridTemplateColumns: '74px 1fr 180px',
                alignItems: 'center',
                gap: 18,
                padding: '16px 20px',
                borderRadius: 8,
                border: `1px solid ${isFocus ? c.amber : active > 0.5 ? c.cyan : c.line}`,
                background: isFocus ? `${c.amber}22` : active > 0.5 ? 'rgba(50,200,232,0.1)' : c.panel,
                color: active > 0.5 || isFocus ? c.ink : c.muted,
                fontFamily: fonts.cn,
                fontWeight: 950,
                transform: `translateX(${(1 - active) * -18}px)`,
                opacity: 0.45 + active * 0.55,
                boxShadow: isFocus ? `0 0 28px ${c.amber}24` : 'none',
              }}
            >
              <div style={{display: 'grid', placeItems: 'center', gap: 4}}>
                <ConceptGlyph
                  kind={
                    scene.artifact.type === 'validation-check-solution-fit'
                      ? index === 0
                        ? 'void'
                        : index === 1
                          ? 'signal'
                          : 'mismatch'
                      : scene.artifact.type === 'validation-check-enough-signal'
                        ? index === 1
                          ? 'threshold'
                          : index === 2
                            ? 'boundary'
                            : 'question'
                        : index === 0
                          ? 'signal'
                          : index === 1
                            ? 'evidence'
                            : 'threshold'
                  }
                  tone={isFocus ? c.amber : c.cyan}
                  active={active}
                  size={58}
                />
                <b style={{fontFamily: fonts.ui, fontSize: 19, color: isFocus ? c.amber : c.cyan}}>{label}</b>
              </div>
              <span style={{fontSize: 32}}>{title}</span>
              <small style={{fontSize: 18, color: c.muted, lineHeight: 1.25}}>{detail}</small>
            </div>
          );
        })}
      </div>
    </ModuleShell>
  );
};

const QuestionEvidence = ({scene, progress}: FounderArtifactProps) => {
  const weak = scene.artifact.type === 'weak-future-question';
  const questions = weak ? ['你会不会用?'] : ['上一次什么时候?', '现在怎么解决?', '为什么还不换?'];
  return (
    <ModuleShell scene={scene} progress={progress} title={weak ? 'weak question' : 'evidence questions'} meta={weak ? 'future intent' : 'past behavior'}>
      <div style={{position: 'absolute', inset: '30px 0 0', display: 'grid', gridTemplateColumns: weak ? '1fr 1fr' : '1.2fr 0.8fr', gap: 22}}>
        <div style={{display: 'grid', gap: 14, alignContent: 'center'}}>
          {questions.map((question, index) => (
            <FlowCard
              key={question}
              label={question}
              detail={weak ? '礼貌回答' : ['过去行为', '当前替代', '转换阻力'][index]}
              tone={weak ? c.rose : c.cyan}
              active={reveal(progress, 0.08 + index * 0.12, 0.34 + index * 0.12)}
              concept={weak ? 'void' : 'question'}
              style={{minHeight: weak ? 190 : 96}}
            />
          ))}
        </div>
        <div style={{display: 'grid', alignContent: 'center', gap: 16}}>
          <FlowCard
            label={weak ? '弱信号' : '证据列'}
            detail={weak ? '不能直接当需求' : '能追问、能反证'}
            tone={weak ? c.rose : c.amber}
            active={reveal(progress, weak ? 0.42 : 0.52, 0.82)}
            concept={weak ? 'void' : 'evidence'}
            style={{minHeight: weak ? 190 : 276}}
          />
        </div>
      </div>
    </ModuleShell>
  );
};

const SignalFilter = ({scene, progress}: FounderArtifactProps) => {
  const praiseOnly = scene.artifact.type === 'praise-not-evidence';
  const praise = reveal(progress, 0.08, 0.34);
  const pain = reveal(progress, 0.34, 0.72);
  return (
    <ModuleShell scene={scene} progress={progress} title="signal filter" meta={praiseOnly ? 'not enough' : 'stronger evidence'}>
      <div style={{position: 'absolute', inset: '40px 0 0'}}>
        <div style={{position: 'absolute', left: 0, right: 0, top: 162, height: 3, background: `${c.amber}80`}} />
        <div style={{position: 'absolute', right: 12, top: 132, color: c.amber, fontFamily: fonts.ui, fontSize: 17, fontWeight: 900}}>
          evidence threshold
        </div>
        <div style={{position: 'absolute', left: 0, width: '46%', top: praiseOnly ? 186 : 194}}>
          <FlowCard label="表层正反馈" detail="夸 Demo" tone={c.rose} active={praise} concept="void" style={{minHeight: 156, opacity: 0.55 + praise * 0.24}} />
        </div>
        <div style={{position: 'absolute', right: 0, width: '50%', top: praiseOnly ? 66 : 46}}>
          <FlowCard
            label={praiseOnly ? '答案未解锁' : '痛点信号'}
            detail={praiseOnly ? '还要追问' : '真实痛点 + 没解决'}
            tone={praiseOnly ? c.rose : c.cyan}
            active={praiseOnly ? reveal(progress, 0.44, 0.76) : pain}
            concept={praiseOnly ? 'void' : 'signal'}
            style={{minHeight: praiseOnly ? 162 : 226}}
          />
        </div>
      </div>
    </ModuleShell>
  );
};

const FinalDemoDecision = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="final decision" meta="question, not proof">
    <div style={{position: 'absolute', inset: '42px 0 0', display: 'grid', gridTemplateColumns: '1fr 78px 1fr', gap: 12}}>
      <FlowCard label="提问向量" detail="Demo 的正确用法" tone={c.cyan} active={reveal(progress, 0.08, 0.36)} concept="question" style={{minHeight: 264}} />
      <div style={{display: 'grid', placeItems: 'center', color: c.muted, fontFamily: fonts.ui, fontSize: 30, fontWeight: 950}}>≠</div>
      <FlowCard label="需求证明" detail="不能替你完成" tone={c.rose} active={reveal(progress, 0.38, 0.74)} concept="proof" style={{minHeight: 264}} />
    </div>
  </ModuleShell>
);

const NextBoundaryGate = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="next boundary gate" meta="episode 03">
    <div style={{position: 'absolute', inset: '58px 0 0', display: 'grid', gridTemplateColumns: '1fr 70px 1fr 70px 1fr', alignItems: 'center', gap: 10}}>
      <FlowCard label="信号足够" detail="值得做" tone={c.cyan} active={reveal(progress, 0.06, 0.28)} concept="threshold" />
      <Arrow active={reveal(progress, 0.2, 0.44)} tone={c.amber} />
      <FlowCard label="边界框" detail="下一关" tone={c.amber} active={reveal(progress, 0.34, 0.62)} concept="boundary" style={{minHeight: 212}} />
      <Arrow active={reveal(progress, 0.54, 0.78)} tone={c.orange} />
      <FlowCard label="生成执行" detail="EP03" tone={c.orange} active={reveal(progress, 0.66, 0.88)} concept="build" />
    </div>
  </ModuleShell>
);

const BoundaryFastCode = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="speed needs boundary" meta="section message first">
    <div style={{position: 'absolute', inset: '38px 0 0'}}>
      <div
        style={{
          position: 'absolute',
          left: 124,
          top: 32,
          width: 650,
          height: 284,
          borderRadius: 8,
          border: `3px solid ${c.amber}`,
          background: 'rgba(255,194,26,0.08)',
          boxShadow: `0 0 34px ${c.amber}22`,
          opacity: reveal(progress, 0.2, 0.58),
        }}
      />
      <div style={{position: 'absolute', left: 58, top: 78, width: 300}}>
        <FlowCard label="AI 写代码" detail="speed" tone={c.orange} active={reveal(progress, 0.06, 0.3)} concept="build" style={{minHeight: 194}} />
      </div>
      <div style={{position: 'absolute', left: 390, top: 64, width: 330}}>
        <FlowCard label="边界先行" detail="scope before execution" tone={c.amber} active={reveal(progress, 0.34, 0.74)} concept="boundary" style={{minHeight: 222}} />
      </div>
      <div style={{position: 'absolute', left: 324, top: 168, width: 76}}>
        <Arrow active={reveal(progress, 0.28, 0.52)} tone={c.amber} />
      </div>
    </div>
  </ModuleShell>
);

const BoundarySprawl = ({scene, progress}: FounderArtifactProps) => {
  const spread = reveal(progress, 0.28, 0.78);
  const nodes = [
    {label: '边缘场景', x: 72, y: 54, tone: c.rose},
    {label: '酷功能', x: 538, y: 44, tone: c.orange},
    {label: '临时补丁', x: 608, y: 252, tone: c.rose},
    {label: '用户证据', x: 112, y: 282, tone: c.cyan},
  ];
  return (
    <ModuleShell scene={scene} progress={progress} title="product boundary" meta="sprawl risk">
      <div style={{position: 'absolute', inset: '24px 0 0'}}>
        <div
          style={{
            position: 'absolute',
            left: 154 - spread * 42,
            top: 70 - spread * 18,
            width: 520 + spread * 76,
            height: 250 + spread * 38,
            borderRadius: 8,
            border: `3px solid ${spread > 0.5 ? c.rose : c.amber}`,
            background: 'rgba(255,248,234,0.035)',
            boxShadow: spread > 0.5 ? `0 0 34px ${c.rose}28` : `0 0 24px ${c.amber}20`,
          }}
        />
        {nodes.map((node, index) => {
          const active = reveal(progress, 0.1 + index * 0.12, 0.34 + index * 0.12);
          const out = index === 1 || index === 2 ? spread : 0;
          return (
            <div
              key={node.label}
              style={{
                position: 'absolute',
                left: node.x + (index === 1 ? out * 92 : index === 2 ? out * 122 : 0),
                top: node.y + (index === 2 ? out * 36 : 0),
                width: 210,
                height: 82,
                display: 'grid',
                placeItems: 'center',
                borderRadius: 8,
                border: `1px solid ${node.tone}`,
                background: `${node.tone}1f`,
                color: c.ink,
                fontFamily: fonts.cn,
                fontSize: 24,
                fontWeight: 950,
                opacity: 0.35 + active * 0.65,
                transform: `scale(${0.92 + active * 0.08})`,
              }}
            >
              {node.label}
            </div>
          );
        })}
        <div style={{position: 'absolute', left: 340, top: 160, display: 'grid', placeItems: 'center'}}>
          <ConceptGlyph kind={spread > 0.5 ? 'mismatch' : 'boundary'} tone={spread > 0.5 ? c.rose : c.amber} active={0.7 + spread * 0.3} size={112} />
        </div>
      </div>
    </ModuleShell>
  );
};

const MvpEvidenceGate = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="mvp evidence gate" meta="not full product">
    <div style={{position: 'absolute', inset: '42px 0 0', display: 'grid', gridTemplateColumns: '1fr 72px 1.1fr', gap: 12, alignItems: 'center'}}>
      <FlowCard label="做满功能" detail="dim this" tone={c.rose} active={0.34 + reveal(progress, 0.05, 0.2) * 0.24} concept="void" style={{minHeight: 210, opacity: 0.48}} />
      <Arrow active={reveal(progress, 0.26, 0.54)} tone={c.cyan} />
      <FlowCard label="收集证据" detail="回来 / 付费 / 推荐" tone={c.cyan} active={reveal(progress, 0.36, 0.76)} concept="evidence" style={{minHeight: 250}} />
    </div>
  </ModuleShell>
);

const ScopeBoundaryDoc = ({scene, progress}: FounderArtifactProps) => {
  if (scene.artifact.state === 'add-feature-option-dimmed') {
    return (
      <ModuleShell scene={scene} progress={progress} title="scope before features" meta="not add-more">
        <div style={{position: 'absolute', inset: '42px 0 0', display: 'grid', gridTemplateColumns: '1fr 72px 1.1fr', gap: 12, alignItems: 'center'}}>
          <FlowCard label="还能加什么" detail="wrong question" tone={c.rose} active={0.42 + reveal(progress, 0.06, 0.28) * 0.18} concept="void" style={{minHeight: 212, opacity: 0.52}} />
          <Arrow active={reveal(progress, 0.3, 0.58)} tone={c.amber} />
          <FlowCard label="先写范围" detail="solve / not / evidence" tone={c.amber} active={reveal(progress, 0.48, 0.84)} concept="boundary" style={{minHeight: 248}} />
        </div>
      </ModuleShell>
    );
  }

  const rows = [
    ['现在解决什么', 'does', c.cyan],
    ['暂时不解决什么', 'does not', c.rose],
    ['什么证据能加', 'evidence', c.amber],
  ] as const;
  return (
    <ModuleShell scene={scene} progress={progress} title="scope boundary" meta="three-part rule">
      <div style={{position: 'absolute', inset: '22px 0 0', display: 'grid', gridTemplateColumns: '1fr', gap: 14}}>
        {rows.map(([label, detail, tone], index) => {
          const active = reveal(progress, 0.08 + index * 0.14, 0.34 + index * 0.14);
          return (
            <div
              key={label}
              style={{
                minHeight: 104,
                display: 'grid',
                gridTemplateColumns: '82px 1fr 150px',
                alignItems: 'center',
                gap: 18,
                padding: '14px 20px',
                borderRadius: 8,
                border: `1px solid ${active > 0.5 ? tone : c.line}`,
                background: active > 0.5 ? `${tone}1f` : c.panel,
                color: c.ink,
                fontFamily: fonts.cn,
                fontWeight: 950,
                opacity: 0.38 + active * 0.62,
              }}
            >
              <ConceptGlyph kind={index === 0 ? 'boundary' : index === 1 ? 'void' : 'threshold'} tone={tone} active={active} size={62} />
              <span style={{fontSize: 32}}>{label}</span>
              <small style={{fontFamily: fonts.ui, fontSize: 18, color: tone, fontWeight: 900}}>{detail}</small>
            </div>
          );
        })}
      </div>
    </ModuleShell>
  );
};

const ContextDrift = ({scene, progress}: FounderArtifactProps) => {
  const drift = reveal(progress, 0.28, 0.82);
  return (
    <ModuleShell scene={scene} progress={progress} title="context drift" meta="hidden technical debt">
      <div style={{position: 'absolute', inset: '42px 0 0', display: 'grid', gridTemplateColumns: '1fr 70px 1fr', alignItems: 'center', gap: 14}}>
        <FlowCard label="边界 / 架构 / 上下文" detail="written context" tone={c.cyan} active={reveal(progress, 0.08, 0.36)} concept="boundary" style={{minHeight: 238}} />
        <Arrow active={drift} tone={c.rose} />
        <FlowCard label={scene.artifact.type === 'context-readable-before-code' ? 'AI 可读取' : '重新猜一遍'} detail={scene.artifact.type === 'context-readable-before-code' ? 'before coding' : 'session reset'} tone={scene.artifact.type === 'context-readable-before-code' ? c.amber : c.rose} active={reveal(progress, 0.34, 0.76)} concept={scene.artifact.type === 'context-readable-before-code' ? 'question' : 'mismatch'} style={{minHeight: 238}} />
      </div>
    </ModuleShell>
  );
};

const ReadGateMark = ({active}: {active: number}) => (
  <svg width="116" height="116" viewBox="0 0 120 120" aria-hidden="true" style={{opacity: 0.42 + active * 0.58}}>
    <rect x="18" y="18" width="84" height="84" rx="8" fill="rgba(255,248,234,0.035)" stroke={active > 0.5 ? c.amber : 'rgba(255,248,234,0.16)'} strokeWidth="2" />
    <path d="M36 42H62" stroke={c.cyan} strokeWidth="7" strokeLinecap="round" />
    <path d="M36 60H72" stroke={c.cyan} strokeWidth="7" strokeLinecap="round" opacity="0.72" />
    <path d="M36 78H56" stroke={c.cyan} strokeWidth="7" strokeLinecap="round" opacity="0.46" />
    <path d="M77 36V84" stroke={c.amber} strokeWidth="6" strokeLinecap="round" />
    <path d="M68 52L78 42L88 52" fill="none" stroke={c.amber} strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" />
    <path d="M68 68L78 78L88 68" fill="none" stroke={c.amber} strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

const ExecutionStackMark = ({active}: {active: number}) => (
  <svg width="116" height="116" viewBox="0 0 120 120" aria-hidden="true" style={{opacity: 0.42 + active * 0.58}}>
    <rect x="18" y="18" width="84" height="84" rx="8" fill="rgba(255,248,234,0.035)" stroke="rgba(255,248,234,0.16)" strokeWidth="2" />
    <rect x="34" y="34" width="52" height="12" rx="6" fill={c.orange} opacity="0.88" />
    <rect x="34" y="54" width="52" height="12" rx="6" fill={c.amber} opacity="0.72" />
    <rect x="34" y="74" width="52" height="12" rx="6" fill={c.cyan} opacity="0.56" />
  </svg>
);

const ContextReadableBeforeCode = ({scene, progress}: FounderArtifactProps) => {
  const sourceActive = reveal(progress, 0.08, 0.3);
  const gateActive = reveal(progress, 0.3, 0.58);
  const execActive = reveal(progress, 0.56, 0.86);
  return (
    <ModuleShell scene={scene} progress={progress} title="context loaded" meta="before coding">
      <div
        style={{
          position: 'absolute',
          inset: '34px 0 0',
          display: 'grid',
          gridTemplateColumns: '1fr 56px 0.82fr 56px 1fr',
          alignItems: 'center',
          gap: 10,
        }}
      >
        <FlowCard label="边界 / 架构 / 上下文" detail="written context" tone={c.cyan} active={sourceActive} concept="boundary" style={{minHeight: 230}} />
        <Arrow active={gateActive} tone={c.cyan} />
        <div
          style={{
            minHeight: 230,
            display: 'grid',
            placeItems: 'center',
            alignContent: 'center',
            gap: 10,
            padding: '18px 12px',
            borderRadius: 8,
            border: `1px solid ${gateActive > 0.5 ? c.amber : c.line}`,
            background: gateActive > 0.5 ? `${c.amber}1f` : c.panel,
            color: gateActive > 0.5 ? c.ink : c.muted,
            fontFamily: fonts.cn,
            fontSize: 27,
            fontWeight: 950,
            textAlign: 'center',
            opacity: 0.4 + gateActive * 0.6,
            boxShadow: gateActive > 0.65 ? `0 0 28px ${c.amber}24` : 'none',
          }}
        >
          <ReadGateMark active={gateActive} />
          读取门
          <small style={{fontFamily: fonts.ui, color: c.amber, fontSize: 16, fontWeight: 900}}>loaded first</small>
        </div>
        <Arrow active={execActive} tone={c.orange} />
        <div
          style={{
            minHeight: 230,
            display: 'grid',
            placeItems: 'center',
            alignContent: 'center',
            gap: 10,
            padding: '18px 12px',
            borderRadius: 8,
            border: `1px solid ${execActive > 0.5 ? c.orange : c.line}`,
            background: execActive > 0.5 ? `${c.orange}20` : c.panel,
            color: execActive > 0.5 ? c.ink : c.muted,
            fontFamily: fonts.cn,
            fontSize: 29,
            fontWeight: 950,
            textAlign: 'center',
            opacity: 0.4 + execActive * 0.6,
            boxShadow: execActive > 0.65 ? `0 0 28px ${c.orange}24` : 'none',
          }}
        >
          <ExecutionStackMark active={execActive} />
          AI 可读取
          <small style={{fontFamily: fonts.ui, color: c.orange, fontSize: 16, fontWeight: 900}}>before code</small>
        </div>
      </div>
    </ModuleShell>
  );
};

const FinalBoundaryDecision = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="final rule" meta="decision lock">
    <div style={{position: 'absolute', inset: '54px 0 0', display: 'grid', gridTemplateColumns: '1.1fr 76px 1fr', gap: 14, alignItems: 'center'}}>
      <FlowCard label="先写边界" detail="scope + context" tone={c.amber} active={reveal(progress, 0.08, 0.38)} concept="boundary" style={{minHeight: 260}} />
      <Arrow active={reveal(progress, 0.34, 0.62)} tone={c.orange} />
      <FlowCard label="再写代码" detail="execution" tone={c.orange} active={reveal(progress, 0.54, 0.86)} concept="build" style={{minHeight: 220}} />
    </div>
  </ModuleShell>
);

const NextRouterPreview = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="next operating gate" meta="episode 04">
    <div style={{position: 'absolute', inset: '54px 0 0', display: 'grid', gridTemplateColumns: '1fr 72px 1fr', gap: 14, alignItems: 'center'}}>
      <FlowCard label="上线后" detail="real users" tone={c.cyan} active={reveal(progress, 0.08, 0.32)} concept="signal" style={{minHeight: 220}} />
      <Arrow active={reveal(progress, 0.3, 0.58)} tone={c.amber} />
      <FlowCard label="别当中转站" detail="EP04" tone={c.amber} active={reveal(progress, 0.48, 0.82)} concept="mismatch" style={{minHeight: 244}} />
    </div>
  </ModuleShell>
);

const FounderRouterBottleneck = ({scene, progress, isContinuingContext}: FounderArtifactProps) => {
  const frame = useCurrentFrame();
  const pulse = 0.5 + Math.sin(frame / 18) * 0.5;
  const labels = scene.artifact.nodes.length >= 4 ? scene.artifact.nodes.slice(0, 4) : ['Support', 'Bug', 'Decision', 'Report'];
  const state = scene.artifact.state ?? 'requests-converge';
  const isFirstReveal = state === 'requests-converge';
  const isLearningLoop = state === 'learning-loop-advantage';
  const isWarning =
    state === 'overload-flip' ||
    state === 'decision-delay' ||
    state === 'recurring-work-queue' ||
    state === 'requests-converge';
  const center = isFirstReveal ? reveal(progress, 0.22, 0.58) : 1;
  const overload = isWarning
    ? state === 'requests-converge'
      ? reveal(progress, 0.58, 0.86)
      : state === 'overload-flip'
        ? reveal(progress, 0.12, 0.52)
        : 1
    : 0;
  const pathFocus = (index: number) => {
    if (state === 'decision-delay') return index < 2;
    if (state === 'overload-flip') return false;
    return true;
  };
  const pathActive = (index: number) => {
    if (isFirstReveal) return reveal(progress, 0.08 + index * 0.08, 0.36 + index * 0.08);
    return 1;
  };
  const pathOpacity = (index: number) => {
    const active = pathActive(index);
    if (active < 1) return active * 0.84;
    if (pathFocus(index)) return 0.84 + pulse * 0.12;
    return 0.58;
  };
  const nodeFocus = (index: number) => {
    if (isFirstReveal || isLearningLoop || state === 'recurring-work-queue') return true;
    if (state === 'decision-delay') return index < 2;
    return false;
  };
  const positions = [
    {left: 40, top: 48},
    {right: 40, top: 48},
    {left: 40, bottom: 58},
    {right: 40, bottom: 58},
  ];

  return (
    <ModuleShell scene={scene} progress={progress} title="founder router" meta="launch bottleneck" stableContent={isContinuingContext}>
      <div style={{position: 'absolute', inset: '36px 0 0'}}>
        <svg viewBox="0 0 908 430" style={{position: 'absolute', inset: 0, width: '100%', height: '100%'}}>
          {[
            'M184 92 C286 122 328 150 358 174',
            'M724 92 C622 122 580 150 550 174',
            'M184 338 C286 308 328 278 358 254',
            'M724 338 C622 308 580 278 550 254',
          ].map((d, index) => (
            <path
              key={d}
              d={d}
              fill="none"
              stroke={index < 2 ? c.cyan : c.orange}
              strokeWidth={pathFocus(index) ? 7.5 + pulse * 1.7 : 5.6}
              strokeLinecap="round"
              strokeDasharray={430}
              strokeDashoffset={430 - 430 * pathActive(index)}
              opacity={pathOpacity(index)}
              style={{filter: pathFocus(index) ? `drop-shadow(0 0 ${8 + pulse * 8}px ${index < 2 ? c.cyan : c.orange}66)` : 'none'}}
            />
          ))}
        </svg>
        {labels.map((label, index) => (
          <div
            key={label}
            style={{
              position: 'absolute',
              width: 176,
              height: 88,
              display: 'grid',
              placeItems: 'center',
              borderRadius: 8,
              border: `1px solid ${index < 2 ? c.cyan : c.orange}${nodeFocus(index) ? 'cc' : '7a'}`,
              background: `${index < 2 ? c.cyan : c.orange}${nodeFocus(index) ? '22' : '14'}`,
              color: c.ink,
              fontFamily: fonts.ui,
              fontSize: 22,
              fontWeight: 950,
              opacity: isFirstReveal ? reveal(progress, 0.04 + index * 0.07, 0.22 + index * 0.07) : nodeFocus(index) ? 1 : 0.78,
              boxShadow: nodeFocus(index) ? `0 0 ${18 + pulse * 10}px ${index < 2 ? c.cyan : c.orange}22` : 'none',
              ...positions[index],
            }}
          >
            {label}
          </div>
        ))}
        <div
          style={{
            position: 'absolute',
            left: '50%',
            top: '50%',
            width: 238,
            height: 238,
            transform: `translate(-50%, -50%) scale(${0.92 + overload * 0.06})`,
            display: 'grid',
            placeItems: 'center',
            alignContent: 'center',
            gap: 10,
            borderRadius: '50%',
            border: `2px solid ${overload > 0.45 ? c.rose : c.amber}`,
            background: isLearningLoop ? `${c.cyan}16` : overload > 0.45 ? `${c.rose}1f` : `${c.amber}1d`,
            color: c.ink,
            fontFamily: fonts.cn,
            fontSize: 34,
            fontWeight: 950,
            opacity: 0.45 + center * 0.55,
            boxShadow: isLearningLoop
              ? `0 0 ${30 + pulse * 12}px ${c.cyan}24`
              : overload > 0.45
                ? `0 0 ${38 + pulse * 14}px ${c.rose}3a`
                : `0 0 ${30 + pulse * 10}px ${c.amber}2c`,
          }}
        >
          创始人
          <small style={{fontFamily: fonts.ui, color: isLearningLoop ? c.cyan : overload > 0.45 ? c.rose : c.amber, fontSize: 17, fontWeight: 900}}>
            {isLearningLoop ? 'learning loop' : state === 'decision-delay' ? 'waiting point' : 'default router'}
          </small>
        </div>
      </div>
    </ModuleShell>
  );
};

const LaunchRepeatabilityGate = ({scene, progress}: FounderArtifactProps) => (
  <ModuleShell scene={scene} progress={progress} title="launch gate" meta="repeatability">
    <div style={{position: 'absolute', inset: '62px 0 0', display: 'grid', gridTemplateColumns: '1fr 70px 1fr 70px 1fr', gap: 12, alignItems: 'center'}}>
      <FlowCard label="MVP" detail="product exists" tone={c.cyan} active={reveal(progress, 0.05, 0.24)} concept="proof" style={{minHeight: 210}} />
      <Arrow active={reveal(progress, 0.22, 0.42)} tone={c.cyan} />
      <FlowCard label="Launch" detail="business test" tone={c.amber} active={reveal(progress, 0.36, 0.58)} concept="threshold" style={{minHeight: 260}} />
      <Arrow active={reveal(progress, 0.56, 0.76)} tone={c.amber} />
      <FlowCard label="重复增长" detail="repeatable" tone={c.orange} active={reveal(progress, 0.68, 0.9)} concept="signal" style={{minHeight: 220}} />
    </div>
  </ModuleShell>
);

const AttentionAuditLanes = ({scene, progress, isContinuingContext}: FounderArtifactProps) => {
  const frame = useCurrentFrame();
  const pulse = 0.5 + Math.sin(frame / 20) * 0.5;
  const state = scene.artifact.state ?? 'audit-list-open';
  const lanes = [
    {label: '自动化', detail: 'automate', tone: c.cyan, concept: 'signal' as const},
    {label: '交给别人', detail: 'delegate', tone: c.amber, concept: 'boundary' as const},
    {label: '创始人判断', detail: 'founder-only', tone: c.orange, concept: 'question' as const},
  ];
  const sourceActive = state === 'wrong-question-dimmed' ? 0.86 : state === 'audit-list-open' ? reveal(progress, 0.06, 0.28) : 0.82;
  const arrowActive = state === 'wrong-question-dimmed' ? 0.62 : state === 'audit-list-open' ? reveal(progress, 0.26, 0.5) : 0.82;
  const laneFocusWeight = (index: number) => {
    if (state === 'automate-delegate') {
      if (index === 0) {
        return interpolate(progress, [0, 0.32, 0.68, 1], [1, 1, 0.68, 0.62], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
      }
      if (index === 1) {
        return interpolate(progress, [0, 0.36, 0.62, 1], [0.58, 0.58, 1, 1], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
      }
      return 0.44;
    }
    if (state === 'founder-only-judgment') return index === 2 ? 1 : 0.5;
    if (state === 'system-replaces-router') return index === 0 ? 1 : index === 1 ? 0.66 : 0.46;
    if (state === 'wrong-question-dimmed') return 0.32;
    return 0.86;
  };
  const laneActive = (index: number) => {
    if (state === 'wrong-question-dimmed') return 0.58;
    if (state === 'audit-list-open') return reveal(progress, 0.38 + index * 0.13, 0.62 + index * 0.13);
    return 0.58 + laneFocusWeight(index) * 0.42;
  };

  return (
    <ModuleShell scene={scene} progress={progress} title="attention audit" meta="system lanes" stableContent={isContinuingContext}>
      <div style={{position: 'absolute', inset: '42px 28px 0 0', display: 'grid', gridTemplateColumns: '220px 70px minmax(0, 1fr)', alignItems: 'center', gap: 16}}>
        <FlowCard
          label={state === 'wrong-question-dimmed' ? '更忙一点' : '重复问题'}
          detail={state === 'wrong-question-dimmed' ? 'wrong question' : 'recurring work'}
          tone={c.rose}
          active={sourceActive}
          concept="mismatch"
          style={{
            minHeight: 238,
            boxShadow: state === 'wrong-question-dimmed' ? `0 0 ${24 + pulse * 12}px ${c.rose}2e` : undefined,
          }}
        />
        <Arrow active={arrowActive} tone={c.amber} />
        <div style={{display: 'grid', gap: 18}}>
          {lanes.map((lane, index) => {
            const focus = laneFocusWeight(index);
            const active = laneActive(index);
            const isFocus = focus > 0.82;
            return (
              <FlowCard
                key={lane.label}
                label={lane.label}
                detail={lane.detail}
                tone={lane.tone}
                active={active}
                concept={lane.concept}
                style={{
                  minHeight: 126,
                  gridTemplateColumns: '70px 1fr',
                  gridAutoFlow: 'column',
                  justifyContent: 'start',
                  outline: isFocus ? `3px solid ${lane.tone}cc` : 'none',
                  outlineOffset: 3,
                  transform: `translateY(${(1 - active) * 10}px) scale(${1 + focus * 0.012})`,
                  boxShadow: isFocus ? `0 0 ${28 + pulse * 16}px ${lane.tone}38` : `0 0 12px ${lane.tone}12`,
                  filter: isFocus ? 'saturate(1.18)' : 'saturate(0.82)',
                }}
              />
            );
          })}
        </div>
      </div>
    </ModuleShell>
  );
};

const WorkflowMoatModule = ({scene, progress, isContinuingContext}: FounderArtifactProps) => {
  const state = scene.artifact.state ?? '';
  const frame = useCurrentFrame();
  const pulse = 0.5 + Math.sin(frame / 14) * 0.5;
  const isModel = scene.artifact.type === 'model-access-not-moat';
  const isStack = scene.artifact.type === 'workflow-specificity-stack' || scene.artifact.type === 'specificity-layer-stack';
  const isCopyGap = scene.artifact.type === 'copy-gap-barrier';
  const isCost = scene.artifact.type === 'switching-cost-chain';
  const isAudit = scene.artifact.type === 'workflow-moat-audit';
  const isScale = scene.artifact.type === 'scale-lifecycle-close';
  const stable = isContinuingContext;

  if (isModel) {
    const leftActive = 0.78;
    const modelActive = reveal(progress, stable ? 0 : 0.08, stable ? 0.01 : 0.28);
    const rightActive = reveal(progress, state === 'same-access-no-gap' ? 0.18 : 0.38, state === 'same-access-no-gap' ? 0.52 : 0.76);
    return (
      <ModuleShell scene={scene} progress={progress} title="model access" meta="not defensibility" stableContent={stable}>
        <div style={{position: 'absolute', inset: '48px 18px 0', display: 'grid', gridTemplateColumns: '1fr 76px 1fr 76px 1fr', alignItems: 'center', gap: 10}}>
          <FlowCard label="我们" detail="builder" tone={c.cyan} active={leftActive} concept="question" style={{minHeight: 210}} />
          <Arrow active={modelActive} tone={c.cyan} />
          <FlowCard
            label="模型权限"
            detail={state === 'wrong-model-focus' ? 'looks important' : 'shared access'}
            tone={state === 'wrong-model-focus' ? c.amber : c.orange}
            active={0.8 + modelActive * 0.2}
            concept="threshold"
            style={{
              minHeight: 248,
              outline: state === 'wrong-model-focus' ? `3px solid ${c.amber}cc` : undefined,
              outlineOffset: 3,
              boxShadow: state === 'wrong-model-focus' ? `0 0 ${28 + pulse * 14}px ${c.amber}34` : undefined,
            }}
          />
          <Arrow active={rightActive} tone={c.orange} />
          <FlowCard
            label={state === 'same-access-no-gap' ? '别人也能接入' : '护城河?'}
            detail={state === 'same-access-no-gap' ? 'no gap' : 'not enough'}
            tone={c.rose}
            active={rightActive}
            concept="void"
            style={{
              minHeight: 210,
              outline: state === 'same-access-no-gap' ? `3px solid ${c.rose}bb` : undefined,
              outlineOffset: 3,
            }}
          />
        </div>
      </ModuleShell>
    );
  }

  if (isStack) {
    const layers: Array<[string, string, string, ConceptKind]> =
      scene.artifact.type === 'workflow-specificity-stack'
        ? [
            ['业务流程', 'workflow spine', c.amber, 'boundary' as const],
            ['沉淀细节', 'specificity', c.cyan, 'signal' as const],
            ['系统记忆', 'accumulates', c.orange, 'evidence' as const],
          ]
        : [
            ['行业例外', 'domain exceptions', c.amber, 'boundary' as const],
            ['用户行为', 'behavior data', c.cyan, 'signal' as const],
            ['工具集成', 'integrations', c.orange, 'threshold' as const],
            ['协作痕迹', 'collaboration traces', c.rose, 'evidence' as const],
          ];
    const focusedIndex = state === 'domain-behavior' ? 0 : state === 'integration-collaboration' ? 2 : 0;
    return (
      <ModuleShell scene={scene} progress={progress} title="workflow specificity" meta="accumulated layers" stableContent={stable}>
        <div style={{position: 'absolute', inset: '30px 20px 0', display: 'grid', alignContent: 'center', gap: 15}}>
          {layers.map(([label, detail, tone, concept], index) => {
            const active = stable ? 0.76 + index * 0.04 : reveal(progress, 0.08 + index * 0.11, 0.32 + index * 0.11);
            const isFocus =
              scene.artifact.type === 'workflow-specificity-stack'
                ? index === 0
                : state === 'domain-behavior'
                  ? index <= 1
                  : index >= focusedIndex;
            return (
              <FlowCard
                key={label}
                label={label}
                detail={detail}
                tone={tone}
                active={active}
                concept={concept}
                style={{
                  minHeight: 96,
                  gridTemplateColumns: '64px 1fr',
                  gridAutoFlow: 'column',
                  justifyContent: 'start',
                  outline: isFocus ? `3px solid ${tone}cc` : 'none',
                  outlineOffset: 3,
                  opacity: isFocus ? 0.96 : 0.54,
                  boxShadow: isFocus ? `0 0 ${24 + pulse * 12}px ${tone}30` : undefined,
                }}
              />
            );
          })}
        </div>
      </ModuleShell>
    );
  }

  if (isCopyGap || isCost) {
    if (isCopyGap) {
      return (
        <ModuleShell scene={scene} progress={progress} title="copy gap" meta="access vs memory" stableContent={stable}>
          <div style={{position: 'absolute', inset: '52px 18px 0', display: 'grid', gridTemplateColumns: '1fr 70px 1.1fr', alignItems: 'center', gap: 14}}>
            <div style={{display: 'grid', gap: 16}}>
              <FlowCard label="提示词" detail="copyable" tone={c.rose} active={0.56} concept="void" style={{minHeight: 108, opacity: 0.58}} />
              <FlowCard label="换模型" detail="copyable" tone={c.rose} active={0.56} concept="threshold" style={{minHeight: 108, opacity: 0.58}} />
            </div>
            <Arrow active={reveal(progress, 0.22, 0.52)} tone={c.rose} />
            <FlowCard
              label="业务记忆"
              detail="not a simple copy"
              tone={c.amber}
              active={reveal(progress, stable ? 0 : 0.32, stable ? 0.01 : 0.74)}
              concept="evidence"
              style={{minHeight: 260, outline: `3px solid ${c.amber}cc`, outlineOffset: 3}}
            />
          </div>
        </ModuleShell>
      );
    }

    const nodes = ['上下文', '数据', '集成', '习惯', '切换成本'];
    return (
      <ModuleShell scene={scene} progress={progress} title="switching cost" meta="conditional moat" stableContent={stable}>
        <div style={{position: 'absolute', inset: '78px 8px 0', display: 'grid', gridTemplateColumns: '1fr 38px 1fr 38px 1fr 38px 1fr 38px 1.18fr', alignItems: 'center', gap: 8}}>
          {nodes.map((node, index) => {
            const active = reveal(progress, 0.06 + index * 0.1, 0.28 + index * 0.1);
            const focus = index === nodes.length - 1;
            return (
              <div key={node} style={{display: 'contents'}}>
                <FlowCard
                  label={node}
                  detail={focus ? 'lock-in' : ['context', 'data', 'integrate', 'habit'][index]}
                  tone={focus ? c.amber : index % 2 === 0 ? c.cyan : c.orange}
                  active={focus ? Math.max(active, reveal(progress, 0.56, 0.84)) : active}
                  concept={focus ? 'threshold' : index === 1 ? 'signal' : 'boundary'}
                  style={{
                    minHeight: focus ? 182 : 152,
                    fontSize: focus ? 28 : undefined,
                    outline: focus && progress > 0.58 ? `3px solid ${c.amber}cc` : undefined,
                    outlineOffset: 3,
                  }}
                />
                {index < nodes.length - 1 && <Arrow active={reveal(progress, 0.14 + index * 0.1, 0.38 + index * 0.1)} tone={index > 2 ? c.amber : c.cyan} />}
              </div>
            );
          })}
        </div>
      </ModuleShell>
    );
  }

  if (isAudit) {
    const rightQuestion = state === 'right-question-highlight';
    return (
      <ModuleShell scene={scene} progress={progress} title="workflow moat audit" meta="founder question" stableContent={stable}>
        <div style={{position: 'absolute', inset: '44px 24px 0', display: 'grid', gridTemplateRows: '1fr 1fr', gap: 20}}>
          <FlowCard
            label="是不是用了 AI?"
            detail="wrong question"
            tone={c.rose}
            active={rightQuestion ? 0.34 : reveal(progress, stable ? 0 : 0.08, stable ? 0.01 : 0.34)}
            concept="void"
            style={{
              minHeight: 132,
              opacity: rightQuestion ? 0.48 : undefined,
              outline: !rightQuestion ? `3px solid ${c.rose}aa` : undefined,
              outlineOffset: 3,
            }}
          />
          <FlowCard
            label="沉淀了什么独特业务细节?"
            detail="right question"
            tone={c.amber}
            active={rightQuestion ? reveal(progress, 0.08, 0.46) : 0.28}
            concept="question"
            style={{
              minHeight: 164,
              outline: rightQuestion ? `3px solid ${c.amber}cc` : undefined,
              outlineOffset: 3,
              boxShadow: rightQuestion ? `0 0 ${28 + pulse * 16}px ${c.amber}36` : undefined,
            }}
          />
        </div>
      </ModuleShell>
    );
  }

  if (isScale) {
    const labels = ['Idea', 'MVP', 'Launch', 'Scale'];
    const sublabels = ['判断', '边界', '系统', '护城河'];
    return (
      <ModuleShell scene={scene} progress={progress} title="scale close" meta="possible moat">
        <div style={{position: 'absolute', inset: '72px 16px 0', display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 12, alignItems: 'center'}}>
          {labels.map((label, index) => {
            const active = reveal(progress, 0.08 + index * 0.1, 0.3 + index * 0.1);
            const focus = index === 3;
            return (
              <FlowCard
                key={label}
                label={label}
                detail={sublabels[index]}
                tone={focus ? c.amber : c.cyan}
                active={focus ? Math.max(active, reveal(progress, 0.48, 0.86)) : active}
                concept={focus ? 'threshold' : 'boundary'}
                style={{
                  minHeight: focus ? 230 : 176,
                  outline: focus ? `3px solid ${c.amber}cc` : undefined,
                  outlineOffset: 3,
                  boxShadow: focus ? `0 0 ${28 + pulse * 16}px ${c.amber}36` : undefined,
                }}
              />
            );
          })}
        </div>
      </ModuleShell>
    );
  }

  return <LifecycleGates scene={scene} progress={progress} />;
};

const BoundaryCodeModule = ({scene, progress, isContinuingContext}: FounderArtifactProps) => {
  switch (scene.artifact.type) {
    case 'ai-code-speed':
      return <BoundaryFastCode scene={scene} progress={progress} />;
    case 'product-boundary-sprawl':
    case 'scope-creep-shape-loss':
      return <BoundarySprawl scene={scene} progress={progress} />;
    case 'mvp-evidence-gate':
      return <MvpEvidenceGate scene={scene} progress={progress} />;
    case 'scope-three-part-boundary':
      return <ScopeBoundaryDoc scene={scene} progress={progress} />;
    case 'context-reset-loop':
    case 'technical-debt-context-drift':
      return <ContextDrift scene={scene} progress={progress} />;
    case 'context-readable-before-code':
      return <ContextReadableBeforeCode scene={scene} progress={progress} />;
    case 'boundary-before-code-decision':
      return <FinalBoundaryDecision scene={scene} progress={progress} />;
    case 'next-founder-router-preview':
      return <NextRouterPreview scene={scene} progress={progress} />;
    case 'founder-router-bottleneck':
      return <FounderRouterBottleneck scene={scene} progress={progress} isContinuingContext={isContinuingContext} />;
    case 'launch-gate-repeatability':
      return <LaunchRepeatabilityGate scene={scene} progress={progress} />;
    case 'attention-audit-lanes':
      return <AttentionAuditLanes scene={scene} progress={progress} isContinuingContext={isContinuingContext} />;
    default:
      return <BoundaryFastCode scene={scene} progress={progress} />;
  }
};

const DemoEvidenceModule = ({scene, progress}: FounderArtifactProps) => {
  switch (scene.artifact.type) {
    case 'demo-fast-build':
      return <DemoFastBuild scene={scene} progress={progress} />;
    case 'demo-false-validation':
      return <DemoFalseValidation scene={scene} progress={progress} />;
    case 'demo-useful-tool':
    case 'demo-question-tool':
      return <DemoToolShift scene={scene} progress={progress} />;
    case 'idea-validation-gate':
    case 'validation-check-real-problem':
    case 'validation-check-solution-fit':
    case 'validation-check-enough-signal':
      return <ValidationGate scene={scene} progress={progress} />;
    case 'weak-future-question':
    case 'evidence-question-stack':
      return <QuestionEvidence scene={scene} progress={progress} />;
    case 'praise-not-evidence':
    case 'pain-signal-evidence':
      return <SignalFilter scene={scene} progress={progress} />;
    case 'demo-question-not-proof':
      return <FinalDemoDecision scene={scene} progress={progress} />;
    case 'next-boundary-gate-preview':
      return <NextBoundaryGate scene={scene} progress={progress} />;
    default:
      return <DemoFastBuild scene={scene} progress={progress} />;
  }
};

const cardStyle = (tone: string): React.CSSProperties => ({
  display: 'grid',
  placeItems: 'center',
  borderRadius: 8,
  border: `1px solid ${tone === c.ink ? c.line : `${tone}88`}`,
  background: tone === c.ink ? c.panel : `${tone}20`,
  color: tone === c.ink ? c.ink : '#ffe7e8',
  fontFamily: fonts.cn,
  fontSize: 25,
  fontWeight: 950,
  textAlign: 'center',
});

export const FounderArtifact = ({scene, progress, isContinuingContext}: FounderArtifactProps) => {
  switch (scene.artifact.type) {
    case 'bottleneck-shift-board':
      return <BottleneckMap scene={scene} progress={progress} />;
    case 'wrong-direction-speed-path':
    case 'wrong-direction-acceleration':
      return <WrongDirectionPath scene={scene} progress={progress} />;
    case 'execution-lane-accelerator':
      return <ExecutionLanes scene={scene} progress={progress} />;
    case 'execution-not-removed':
      return <RetainedExecutionLayer scene={scene} progress={progress} />;
    case 'early-decision-gate':
      return <EarlyDecisionGate scene={scene} progress={progress} />;
    case 'speed-neutral-marker':
      return <SpeedNeutralMarker scene={scene} progress={progress} />;
    case 'accelerator-steering-metaphor':
    case 'founder-steering-control':
      return <ControlSplit scene={scene} progress={progress} />;
    case 'founder-decision-gate':
      return <FounderJudgmentNode scene={scene} progress={progress} />;
    case 'go-stop-decision-cards':
      return <GoStopDecisionCards scene={scene} progress={progress} />;
    case 'judgment-sequence':
      return <JudgmentGateSequence scene={scene} progress={progress} />;
    case 'source-lifecycle-gates':
    case 'different-judgment-icons':
    case 'idea-stage-gate':
      return <LifecycleGates scene={scene} progress={progress} />;
    case 'later-gates-deferred':
      return <LaterGatesDeferred scene={scene} progress={progress} />;
    case 'speed-question-dim':
    case 'final-decision-card':
      return <FinalQuestion scene={scene} progress={progress} />;
    case 'next-episode-gate-preview':
      return <DemoDemandGate scene={scene} progress={progress} />;
    case 'demo-fast-build':
    case 'demo-false-validation':
    case 'demo-useful-tool':
    case 'demo-question-tool':
    case 'idea-validation-gate':
    case 'validation-check-real-problem':
    case 'validation-check-solution-fit':
    case 'validation-check-enough-signal':
    case 'weak-future-question':
    case 'evidence-question-stack':
    case 'praise-not-evidence':
    case 'pain-signal-evidence':
    case 'demo-question-not-proof':
    case 'next-boundary-gate-preview':
      return <DemoEvidenceModule scene={scene} progress={progress} />;
    case 'ai-code-speed':
    case 'product-boundary-sprawl':
    case 'mvp-evidence-gate':
    case 'scope-three-part-boundary':
    case 'context-reset-loop':
    case 'scope-creep-shape-loss':
    case 'technical-debt-context-drift':
    case 'context-readable-before-code':
    case 'boundary-before-code-decision':
    case 'next-founder-router-preview':
    case 'founder-router-bottleneck':
    case 'launch-gate-repeatability':
    case 'attention-audit-lanes':
      return <BoundaryCodeModule scene={scene} progress={progress} isContinuingContext={isContinuingContext} />;
    case 'model-access-not-moat':
    case 'workflow-specificity-stack':
    case 'specificity-layer-stack':
    case 'copy-gap-barrier':
    case 'switching-cost-chain':
    case 'workflow-moat-audit':
    case 'scale-lifecycle-close':
      return <WorkflowMoatModule scene={scene} progress={progress} isContinuingContext={isContinuingContext} />;
    default:
      return <WrongDirectionPath scene={scene} progress={progress} />;
  }
};
