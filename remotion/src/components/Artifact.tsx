import {Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import React from 'react';
import {theme, fonts} from '../styles/theme';
import type {Scene} from '../types';

type ArtifactProps = {
  scene: Scene;
  progress: number;
};

const activeTone = (type: string) => {
  if (type === 'cost-triangle') {
    return theme.amber;
  }

  if (type === 'wrong-question') {
    return theme.red;
  }

  return theme.cyan;
};

const successTone = '#7bd88f';

export const Artifact = ({scene, progress}: ArtifactProps) => {
  if (scene.artifact.type === 'ep06-threshold-board') {
    return <Ep06ThresholdBoard scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-evidence-ladder') {
    return <Ep06EvidenceLadder scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-composition-board') {
    return <Ep06CompositionBoard scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-routing-ledger') {
    return <Ep06RoutingLedger scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-escalation-gate') {
    return <Ep06EscalationGate scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-emerging-lab') {
    return <Ep06EmergingLab scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-decision-panel') {
    return <Ep06DecisionPanel scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-final-stack') {
    return <Ep06FinalStack scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-question-gate') {
    return <QuestionGate scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-evolution-lane') {
    return <EvolutionLane scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-hybrid-composer') {
    return <HybridComposer scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-routing-escalator') {
    return <RoutingEscalator scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-decision-radar') {
    return <DecisionRadar scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'ep06-takeaway-stack') {
    return <TakeawayStack scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'source-diagram' || scene.artifact.type === 'diagram-montage') {
    return <SourceDiagram scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'cost-triangle') {
    return <CostTriangle scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'harness') {
    return <Harness scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'selection-matrix') {
    return <SelectionMatrix scene={scene} progress={progress} />;
  }

  if (scene.artifact.type === 'architecture-hierarchy') {
    return <ArchitectureHierarchy scene={scene} progress={progress} />;
  }

  return <NodePath scene={scene} progress={progress} />;
};

const ArtifactShell = ({
  scene,
  tone,
  label,
  children,
  width = 880,
  height = 560,
}: {
  scene: Scene;
  tone: string;
  label: string;
  children: React.ReactNode;
  width?: number;
  height?: number;
}) => {
  return (
    <div
      style={{
        width,
        height,
        position: 'relative',
        border: `1px solid ${theme.line}`,
        borderRadius: 34,
        background:
          'linear-gradient(135deg, rgba(9, 14, 18, 0.82), rgba(12, 24, 30, 0.7))',
        boxShadow: `0 0 80px ${tone}14, inset 0 0 60px rgba(97, 216, 255, 0.03)`,
        overflow: 'hidden',
      }}
    >
      <div
        style={{
          position: 'absolute',
          inset: 0,
          opacity: 0.22,
          backgroundImage:
            'linear-gradient(rgba(255,255,255,0.08) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px)',
          backgroundSize: '48px 48px',
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 36,
          top: 28,
          zIndex: 3,
          fontFamily: fonts.mono,
          fontSize: 17,
          letterSpacing: 1.4,
          textTransform: 'uppercase',
          color: tone,
        }}
      >
        {label}
      </div>
      <div style={{position: 'absolute', inset: '72px 36px 66px', zIndex: 2}}>
        {children}
      </div>
      <ArtifactLabel scene={scene} tone={tone} />
    </div>
  );
};

const Ep06ThresholdBoard = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;
  const activeIndex = Math.min(nodes.length - 1, Math.floor(progress * nodes.length));

  return (
    <ArtifactShell scene={scene} tone={theme.cyan} label="evidence threshold" width={920}>
      <div style={{height: '100%', display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 18}}>
        {nodes.map((node, index) => {
          const active = index <= activeIndex;
          const tone = index === 0 ? theme.red : index === 1 ? theme.cyan : theme.amber;

          return (
            <div
              key={node}
              style={{
                borderRadius: 22,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}14` : 'rgba(17,24,32,0.72)',
                boxShadow: active ? `0 0 38px ${tone}24` : 'none',
                padding: 24,
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                color: active ? theme.text : theme.muted,
              }}
            >
              <div style={{fontFamily: fonts.mono, fontSize: 16, color: tone}}>
                {index === 0 ? 'premature' : index === 1 ? 'required' : 'locked'}
              </div>
              <div style={{fontFamily: fonts.sans, fontSize: 38, lineHeight: 1.06, fontWeight: 900}}>
                {node}
              </div>
              <div style={{height: 10, borderRadius: 999, background: theme.line, overflow: 'hidden'}}>
                <div
                  style={{
                    width: `${active ? 100 : 20}%`,
                    height: '100%',
                    background: tone,
                    boxShadow: `0 0 24px ${tone}`,
                  }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const Ep06EvidenceLadder = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes.slice(0, 7);
  const activeIndex = Math.min(nodes.length - 1, Math.floor(progress * nodes.length));

  return (
    <ArtifactShell scene={scene} tone={theme.cyan} label="evidence ladder">
      <div style={{height: '100%', position: 'relative'}}>
        <div style={{position: 'absolute', left: 54, top: 54, bottom: 32, width: 4, background: theme.line}}>
          <div
            style={{
              width: '100%',
              height: `${Math.min(100, progress * 108)}%`,
              background: theme.cyan,
              boxShadow: `0 0 26px ${theme.cyan}`,
            }}
          />
        </div>
        {nodes.map((node, index) => {
          const active = index <= activeIndex;
          const tone = index <= 2 ? theme.cyan : index <= 4 ? theme.amber : successTone;
          return (
            <div
              key={node}
              style={{
                position: 'absolute',
                left: 88 + (index % 2) * 308,
                top: 18 + index * 54,
                width: 300,
                height: 48,
                borderRadius: 14,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}14` : 'rgba(17,24,32,0.72)',
                color: active ? theme.text : theme.muted,
                display: 'flex',
                alignItems: 'center',
                padding: '0 18px',
                fontFamily: fonts.sans,
                fontSize: 24,
                fontWeight: 900,
                boxShadow: active ? `0 0 24px ${tone}20` : 'none',
              }}
            >
              <span style={{fontFamily: fonts.mono, fontSize: 16, color: tone, marginRight: 14}}>
                {String(index + 1).padStart(2, '0')}
              </span>
              {node}
            </div>
          );
        })}
        <div
          style={{
            position: 'absolute',
            right: 4,
            bottom: 0,
            width: 300,
            color: theme.muted,
            fontFamily: fonts.sans,
            fontSize: 24,
            lineHeight: 1.2,
          }}
        >
          {scene.focus}
        </div>
      </div>
    </ArtifactShell>
  );
};

const Ep06CompositionBoard = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;
  const imagePaths = scene.artifact.imagePaths ?? [];

  return (
    <ArtifactShell scene={scene} tone={theme.amber} label="composition proof" width={940}>
      <div style={{height: '100%', display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 16}}>
        {nodes.map((node, index) => {
          const reveal = progress > index * 0.18;
          const tone = index === 0 ? theme.cyan : index === 1 ? successTone : theme.amber;
          return (
            <div
              key={node}
              style={{
                borderRadius: 18,
                border: `1px solid ${reveal ? tone : theme.line}`,
                background: '#f6f4ef',
                overflow: 'hidden',
                position: 'relative',
                opacity: reveal ? 1 : 0.42,
                boxShadow: reveal ? `0 0 28px ${tone}26` : 'none',
              }}
            >
              <div
                style={{
                  position: 'absolute',
                  top: 12,
                  left: 12,
                  zIndex: 4,
                  borderRadius: 999,
                  background: tone,
                  color: '#061015',
                  fontFamily: fonts.mono,
                  fontSize: 12,
                  fontWeight: 900,
                  padding: '7px 10px',
                  textTransform: 'uppercase',
                }}
              >
                {node}
              </div>
              {imagePaths[index] ? (
                <Img
                  src={staticFile(imagePaths[index])}
                  style={{
                    position: 'absolute',
                    inset: '52px 12px 14px',
                    maxWidth: 'calc(100% - 24px)',
                    maxHeight: 'calc(100% - 66px)',
                    objectFit: 'contain',
                    margin: 'auto',
                  }}
                />
              ) : null}
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const Ep06RoutingLedger = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;
  const activeIndex = Math.min(nodes.length - 1, Math.floor(progress * nodes.length));

  return (
    <ArtifactShell scene={scene} tone={theme.amber} label="cost routing ledger">
      <div style={{height: '100%', display: 'grid', gap: 16, alignContent: 'center'}}>
        {nodes.map((node, index) => {
          const active = index <= activeIndex;
          const isCost = /10|15|Token|Heavy|Complex/.test(node);
          const tone = isCost ? theme.amber : theme.cyan;
          return (
            <div
              key={`${node}-${index}`}
              style={{
                height: 66,
                marginLeft: index % 2 === 0 ? 0 : 70,
                borderRadius: 16,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}14` : 'rgba(17,24,32,0.72)',
                color: active ? theme.text : theme.muted,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '0 24px',
                fontFamily: fonts.sans,
                fontSize: 30,
                fontWeight: 900,
                boxShadow: active ? `0 0 26px ${tone}20` : 'none',
              }}
            >
              <span>{node}</span>
              <span style={{fontFamily: fonts.mono, color: tone, fontSize: 16}}>
                {isCost ? 'COST GATE' : 'DEFAULT'}
              </span>
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const Ep06EscalationGate = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;
  const activeIndex = Math.min(nodes.length - 1, Math.floor(progress * nodes.length));

  return (
    <ArtifactShell scene={scene} tone={successTone} label="escalation gate">
      <div style={{height: '100%', position: 'relative'}}>
        <div style={{position: 'absolute', left: 58, right: 58, top: 176, height: 5, background: theme.line}}>
          <div style={{height: '100%', width: `${progress * 100}%`, background: successTone}} />
        </div>
        {nodes.map((node, index) => {
          const active = index <= activeIndex;
          const tone = index < 2 ? theme.cyan : index === nodes.length - 1 ? theme.red : theme.amber;
          const x = 60 + (index / Math.max(1, nodes.length - 1)) * 680;
          return (
            <div
              key={node}
              style={{
                position: 'absolute',
                left: x - 78,
                top: index % 2 === 0 ? 72 : 220,
                width: 158,
                minHeight: 92,
                borderRadius: 18,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}15` : 'rgba(17,24,32,0.78)',
                color: active ? theme.text : theme.muted,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                textAlign: 'center',
                padding: 12,
                fontFamily: fonts.sans,
                fontSize: 23,
                lineHeight: 1.08,
                fontWeight: 900,
                boxShadow: active ? `0 0 24px ${tone}24` : 'none',
              }}
            >
              {node}
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const Ep06EmergingLab = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;
  return (
    <ArtifactShell scene={scene} tone={theme.red} label="experimental zone">
      <div style={{height: '100%', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20}}>
        {nodes.map((node, index) => {
          const active = progress > index * 0.15;
          const tone = index < 2 ? theme.amber : index === 2 ? successTone : theme.red;
          return (
            <div
              key={node}
              style={{
                borderRadius: 20,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}13` : 'rgba(17,24,32,0.74)',
                color: active ? theme.text : theme.muted,
                padding: 22,
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                boxShadow: active ? `0 0 30px ${tone}22` : 'none',
              }}
            >
              <div style={{fontFamily: fonts.mono, color: tone, fontSize: 16}}>
                {index < 2 ? 'emerging pattern' : index === 2 ? 'upside' : 'risk'}
              </div>
              <div style={{fontFamily: fonts.sans, fontSize: 34, lineHeight: 1.05, fontWeight: 900}}>
                {node}
              </div>
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const Ep06DecisionPanel = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;
  return (
    <ArtifactShell scene={scene} tone={theme.cyan} label="decision axes">
      <div style={{height: '100%', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 18}}>
        {nodes.map((node, index) => {
          const active = progress > index * 0.12;
          const tone = index % 2 === 0 ? theme.cyan : theme.amber;
          return (
            <div
              key={node}
              style={{
                borderRadius: 16,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}12` : 'rgba(17,24,32,0.72)',
                color: active ? theme.text : theme.muted,
                display: 'flex',
                alignItems: 'center',
                padding: '0 22px',
                fontFamily: fonts.sans,
                fontSize: 30,
                fontWeight: 900,
                boxShadow: active ? `0 0 24px ${tone}20` : 'none',
              }}
            >
              <span style={{fontFamily: fonts.mono, color: tone, fontSize: 18, marginRight: 16}}>
                AXIS {index + 1}
              </span>
              {node}
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const Ep06FinalStack = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;
  return (
    <ArtifactShell scene={scene} tone={theme.cyan} label="operating principle">
      <div style={{height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center'}}>
        {nodes.map((node, index) => {
          const active = progress > index * 0.16;
          const tone = index === nodes.length - 1 ? theme.amber : theme.cyan;
          return (
            <div
              key={node}
              style={{
                height: 76,
                marginBottom: 15,
                marginLeft: index * 34,
                borderRadius: 16,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}12` : 'rgba(17,24,32,0.72)',
                color: active ? theme.text : theme.muted,
                display: 'flex',
                alignItems: 'center',
                padding: '0 26px',
                fontFamily: fonts.sans,
                fontSize: 33,
                fontWeight: 900,
                boxShadow: active ? `0 0 28px ${tone}22` : 'none',
              }}
            >
              <span style={{fontFamily: fonts.mono, color: tone, fontSize: 19, marginRight: 18}}>
                {String(index + 1).padStart(2, '0')}
              </span>
              {node}
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const QuestionGate = ({scene, progress}: ArtifactProps) => {
  const [wrong = '一次做全', right = '逐步演进'] = scene.artifact.nodes;
  const rightActive = progress > 0.38;

  return (
    <ArtifactShell scene={scene} tone={theme.red} label="question gate">
      <div style={{height: '100%', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24}}>
        {[wrong, right].map((node, index) => {
          const isRight = index === 1;
          const active = isRight ? rightActive : !rightActive;
          const tone = isRight ? theme.cyan : theme.red;

          return (
            <div
              key={node}
              style={{
                borderRadius: 26,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}18` : 'rgba(17,24,32,0.74)',
                boxShadow: active ? `0 0 42px ${tone}26` : 'none',
                padding: 30,
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
              }}
            >
              <div
                style={{
                  fontFamily: fonts.mono,
                  color: active ? tone : theme.muted,
                  fontSize: 18,
                  letterSpacing: 1.2,
                  textTransform: 'uppercase',
                }}
              >
                {isRight ? 'better question' : 'too early'}
              </div>
              <div
                style={{
                  color: active ? theme.text : theme.muted,
                  fontFamily: fonts.sans,
                  fontSize: 52,
                  lineHeight: 1.05,
                  fontWeight: 900,
                }}
              >
                {node}
              </div>
              <div
                style={{
                  height: 9,
                  borderRadius: 999,
                  background: theme.line,
                  overflow: 'hidden',
                }}
              >
                <div
                  style={{
                    width: `${active ? 100 : 34}%`,
                    height: '100%',
                    background: tone,
                    boxShadow: `0 0 26px ${tone}`,
                  }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const EvolutionLane = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;

  return (
    <ArtifactShell scene={scene} tone={theme.cyan} label="evolution lane">
      <div style={{height: '100%', position: 'relative'}}>
        <div
          style={{
            position: 'absolute',
            left: 34,
            right: 34,
            top: 192,
            height: 4,
            background: theme.line,
          }}
        >
          <div
            style={{
              height: '100%',
              width: `${Math.min(100, progress * 112)}%`,
              background: theme.cyan,
              boxShadow: `0 0 28px ${theme.cyan}`,
            }}
          />
        </div>
        {nodes.map((node, index) => {
          const x = 38 + (index / Math.max(1, nodes.length - 1)) * 724;
          const active = progress >= index / Math.max(1, nodes.length);
          const isDecision = index >= 3;
          const tone = isDecision ? theme.amber : theme.cyan;

          return (
            <div
              key={node}
              style={{
                position: 'absolute',
                left: x - 72,
                top: index % 2 === 0 ? 78 : 226,
                width: 148,
                minHeight: 112,
                borderRadius: 20,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}16` : 'rgba(17,24,32,0.86)',
                boxShadow: active ? `0 0 32px ${tone}26` : 'none',
                color: active ? theme.text : theme.muted,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                textAlign: 'center',
                padding: 14,
                fontFamily: fonts.sans,
                fontSize: 23,
                lineHeight: 1.12,
                fontWeight: 900,
              }}
            >
              {node}
            </div>
          );
        })}
        <div
          style={{
            position: 'absolute',
            left: 42,
            right: 42,
            bottom: 14,
            color: theme.muted,
            fontFamily: fonts.sans,
            fontSize: 25,
            lineHeight: 1.24,
          }}
        >
          {scene.focus}
        </div>
      </div>
    </ArtifactShell>
  );
};

const HybridComposer = ({scene, progress}: ArtifactProps) => {
  const imagePaths = scene.artifact.imagePaths ?? [];
  const labels = ['Single Agent', 'Workflow', 'Multi-Agent'];

  return (
    <ArtifactShell scene={scene} tone={theme.amber} label="hybrid composer" width={920}>
      <div
        style={{
          height: '100%',
          display: 'grid',
          gridTemplateColumns: '1fr 92px 1fr 92px 1fr',
          gap: 12,
          alignItems: 'center',
        }}
      >
        {labels.map((label, index) => {
          const reveal = progress > index * 0.18;
          return (
            <React.Fragment key={label}>
              <div
                style={{
                  height: 330,
                  borderRadius: 18,
                  border: `1px solid ${reveal ? theme.amber : theme.line}`,
                  background: '#f6f4ef',
                  position: 'relative',
                  overflow: 'hidden',
                  opacity: reveal ? 1 : 0.38,
                  boxShadow: reveal ? `0 0 30px ${theme.amber}22` : 'none',
                }}
              >
                <div
                  style={{
                    position: 'absolute',
                    top: 12,
                    left: 12,
                    zIndex: 3,
                    borderRadius: 999,
                    background: index === 1 ? theme.amber : theme.cyan,
                    color: '#071014',
                    fontFamily: fonts.mono,
                    fontSize: 12,
                    fontWeight: 900,
                    padding: '6px 9px',
                    textTransform: 'uppercase',
                  }}
                >
                  {label}
                </div>
                {imagePaths[index] ? (
                  <Img
                    src={staticFile(imagePaths[index])}
                    style={{
                      position: 'absolute',
                      inset: '46px 10px 12px',
                      maxWidth: 'calc(100% - 20px)',
                      maxHeight: 'calc(100% - 58px)',
                      objectFit: 'contain',
                      margin: 'auto',
                    }}
                  />
                ) : null}
              </div>
              {index < labels.length - 1 ? (
                <div
                  style={{
                    color: progress > 0.38 + index * 0.16 ? theme.amber : theme.line,
                    fontFamily: fonts.display,
                    fontSize: 64,
                    fontWeight: 900,
                    textAlign: 'center',
                    textShadow:
                      progress > 0.38 + index * 0.16 ? `0 0 24px ${theme.amber}44` : 'none',
                  }}
                >
                  +
                </div>
              ) : null}
            </React.Fragment>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const RoutingEscalator = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;
  const activeIndex = Math.min(nodes.length - 1, Math.floor(progress * nodes.length));

  return (
    <ArtifactShell scene={scene} tone={theme.cyan} label="routing escalator">
      <div style={{height: '100%', display: 'grid', gap: 18}}>
        {nodes.map((node, index) => {
          const active = index <= activeIndex;
          const isEscalation = index >= 2;
          const tone = isEscalation ? theme.amber : theme.cyan;
          return (
            <div
              key={node}
              style={{
                height: 74,
                marginLeft: index * 46,
                marginRight: (nodes.length - index - 1) * 34,
                borderRadius: 18,
                border: `1px solid ${active ? tone : theme.line}`,
                background: active ? `${tone}14` : 'rgba(17,24,32,0.72)',
                boxShadow: active ? `0 0 26px ${tone}22` : 'none',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '0 24px',
                color: active ? theme.text : theme.muted,
                fontFamily: fonts.sans,
                fontSize: 31,
                fontWeight: 900,
              }}
            >
              <span>{node}</span>
              <span style={{fontFamily: fonts.mono, color: tone, fontSize: 18}}>
                {isEscalation ? 'ESCALATE' : 'ROUTE'}
              </span>
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const DecisionRadar = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes.slice(0, 5);
  const center = 250;
  const radius = 172;
  const points = nodes.map((node, index) => {
    const angle = -Math.PI / 2 + (index / nodes.length) * Math.PI * 2;
    return {
      node,
      x: center + Math.cos(angle) * radius,
      y: center + Math.sin(angle) * radius,
      active: progress > index * 0.14,
    };
  });

  return (
    <ArtifactShell scene={scene} tone={theme.cyan} label="decision radar">
      <div style={{height: '100%', display: 'grid', gridTemplateColumns: '520px 1fr', gap: 28}}>
        <svg width="520" height="420" viewBox="0 0 520 420" style={{overflow: 'visible'}}>
          {[70, 120, 172].map((r) => (
            <circle
              key={r}
              cx={center}
              cy={210}
              r={r}
              fill="none"
              stroke={theme.line}
              strokeWidth="1.5"
              opacity={0.75}
            />
          ))}
          {points.map((point) => (
            <line
              key={`${point.node}-line`}
              x1={center}
              y1={210}
              x2={point.x}
              y2={point.y - 40}
              stroke={point.active ? theme.cyan : theme.line}
              strokeWidth="2"
              opacity={point.active ? 0.95 : 0.35}
            />
          ))}
          <circle cx={center} cy={210} r="34" fill={`${theme.cyan}22`} stroke={theme.cyan} />
          {points.map((point, index) => (
            <g key={point.node}>
              <circle
                cx={point.x}
                cy={point.y - 40}
                r={point.active ? 15 : 10}
                fill={point.active ? theme.cyan : theme.graphite2}
                stroke={point.active ? theme.cyan : theme.line}
              />
              <text
                x={point.x}
                y={point.y + (index === 0 ? -72 : -12)}
                fill={point.active ? theme.text : theme.muted}
                fontFamily={fonts.sans}
                fontSize="22"
                fontWeight="800"
                textAnchor="middle"
              >
                {point.node}
              </text>
            </g>
          ))}
        </svg>
        <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 14}}>
          {nodes.map((node, index) => {
            const active = progress > index * 0.14;
            return (
              <div
                key={node}
                style={{
                  borderRadius: 14,
                  border: `1px solid ${active ? theme.cyan : theme.line}`,
                  background: active ? 'rgba(97,216,255,0.11)' : 'rgba(17,24,32,0.62)',
                  color: active ? theme.text : theme.muted,
                  fontFamily: fonts.sans,
                  fontSize: 25,
                  fontWeight: 900,
                  padding: '12px 16px',
                }}
              >
                {node}
              </div>
            );
          })}
        </div>
      </div>
    </ArtifactShell>
  );
};

const TakeawayStack = ({scene, progress}: ArtifactProps) => {
  const nodes = scene.artifact.nodes;
  return (
    <ArtifactShell scene={scene} tone={theme.cyan} label="season principle">
      <div style={{height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center'}}>
        {nodes.map((node, index) => {
          const active = progress > index * 0.16;
          return (
            <div
              key={node}
              style={{
                height: 78,
                marginBottom: 16,
                marginLeft: index * 34,
                borderRadius: 16,
                border: `1px solid ${active ? theme.cyan : theme.line}`,
                background: active ? 'rgba(97,216,255,0.12)' : 'rgba(17,24,32,0.72)',
                boxShadow: active ? `0 0 30px ${theme.cyan}24` : 'none',
                color: active ? theme.text : theme.muted,
                display: 'flex',
                alignItems: 'center',
                padding: '0 26px',
                fontFamily: fonts.sans,
                fontSize: 34,
                fontWeight: 900,
              }}
            >
              <span
                style={{
                  color: active ? theme.cyan : theme.dim,
                  fontFamily: fonts.mono,
                  fontSize: 20,
                  marginRight: 20,
                }}
              >
                {String(index + 1).padStart(2, '0')}
              </span>
              {node}
            </div>
          );
        })}
      </div>
    </ArtifactShell>
  );
};

const ArchitectureHierarchy = ({scene, progress}: ArtifactProps) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const groups = scene.artifact.groups ?? [];
  const shouldGenerateFallback = scene.artifact.fallback === 'generated';
  const fallbackGroups =
    groups.length > 0 || !shouldGenerateFallback
      ? groups
      : [
          {
            title: scene.claim,
            items:
              scene.artifact.nodes.length > 0
                ? scene.artifact.nodes
                : [scene.focus, ...(scene.sources ?? [])].filter(Boolean),
          },
        ];

  return (
    <div
      style={{
        width: 900,
        height: 560,
        position: 'relative',
        border: `1px solid ${theme.line}`,
        borderRadius: 34,
        background: 'rgba(9, 14, 18, 0.72)',
        boxShadow: `0 0 80px rgba(97, 216, 255, 0.08), inset 0 0 60px rgba(97, 216, 255, 0.03)`,
        overflow: 'hidden',
        padding: 38,
      }}
    >
      <div
        style={{
          fontFamily: fonts.mono,
          fontSize: 18,
          letterSpacing: 1.2,
          textTransform: 'uppercase',
          color: theme.cyan,
          marginBottom: 30,
        }}
      >
        Source taxonomy
      </div>
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: `repeat(${Math.max(1, fallbackGroups.length)}, 1fr)`,
          gap: 22,
          height: 420,
        }}
      >
        {fallbackGroups.map((group, groupIndex) => {
          const reveal = spring({
            frame: frame - groupIndex * 11,
            fps,
            config: {damping: 18, stiffness: 86},
          });
          const tone = groupIndex === 0 ? theme.cyan : groupIndex === 1 ? theme.amber : theme.red;

          return (
            <div
              key={group.title}
              style={{
                opacity: reveal,
                transform: `translateY(${(1 - reveal) * 20}px)`,
                borderRadius: 24,
                border: `1px solid ${tone}`,
                background: groupIndex === 1 ? 'rgba(42,31,14,0.55)' : 'rgba(15,31,39,0.56)',
                boxShadow: `0 0 30px ${tone}24`,
                padding: 22,
                display: 'flex',
                flexDirection: 'column',
              }}
            >
              <div
                style={{
                  fontFamily: fonts.sans,
                  fontSize: 30,
                  lineHeight: 1.1,
                  fontWeight: 900,
                  color: theme.text,
                  minHeight: 70,
                  display: 'flex',
                  alignItems: 'center',
                }}
              >
                {group.title}
              </div>
              <div
                style={{
                  marginTop: 16,
                  display: 'grid',
                  gap: 13,
                }}
              >
                {group.items.map((item, itemIndex) => {
                  const itemReveal = interpolate(
                    progress,
                    [0.12 + (groupIndex + itemIndex) * 0.08, 0.26 + (groupIndex + itemIndex) * 0.08],
                    [0, 1],
                    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
                  );

                  return (
                    <div
                      key={item}
                      style={{
                        borderRadius: 16,
                        border: `1px solid ${itemReveal > 0.75 ? tone : theme.line}`,
                        background: 'rgba(9,14,18,0.72)',
                        color: theme.text,
                        fontFamily: fonts.sans,
                        fontSize: 21,
                        lineHeight: 1.18,
                        fontWeight: 700,
                        minHeight: 54,
                        display: 'flex',
                        alignItems: 'center',
                        padding: '9px 13px',
                        opacity: 0.42 + itemReveal * 0.58,
                      }}
                    >
                      {item}
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
      <ArtifactLabel scene={scene} tone={theme.cyan} />
    </div>
  );
};

const SourceDiagram = ({scene, progress}: ArtifactProps) => {
  const imagePaths =
    scene.artifact.imagePaths ??
    (scene.artifact.imagePath ? [scene.artifact.imagePath] : []);
  const tone = activeTone(scene.artifact.type);
  const isMontage = imagePaths.length > 1;
  const shouldGenerateFallback = scene.artifact.fallback === 'generated';
  const slots =
    imagePaths.length > 0
      ? imagePaths
      : shouldGenerateFallback
        ? buildGeneratedDiagramSlots(scene).map((slot) => slot.id)
        : [];
  const generatedSlots = shouldGenerateFallback ? buildGeneratedDiagramSlots(scene) : [];

  return (
    <div
      style={{
        width: 900,
        height: 560,
        position: 'relative',
        border: `1px solid ${theme.line}`,
        borderRadius: 34,
        background: 'rgba(9, 14, 18, 0.76)',
        boxShadow: `0 0 80px rgba(97, 216, 255, 0.08), inset 0 0 60px rgba(97, 216, 255, 0.03)`,
        overflow: 'hidden',
        padding: 32,
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: 32,
          top: 24,
          zIndex: 3,
          fontFamily: fonts.mono,
          fontSize: 18,
          letterSpacing: 1.3,
          textTransform: 'uppercase',
          color: tone,
        }}
      >
        Original PDF diagram
      </div>
      <div
        style={{
          position: 'absolute',
          inset: '66px 34px 74px',
          display: 'grid',
          gridTemplateColumns: isMontage ? `repeat(${Math.min(3, slots.length)}, 1fr)` : '1fr',
          gap: 22,
          alignItems: 'center',
        }}
      >
        {slots.map((path, index) => {
          const reveal = interpolate(
            progress,
            [index * 0.18, index * 0.18 + 0.22],
            [0, 1],
            {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
          );

          return (
            <div
              key={path}
              style={{
                height: '100%',
                borderRadius: 20,
                background: '#f6f4ef',
                border: `1px solid ${reveal > 0.8 ? tone : 'rgba(255,255,255,0.18)'}`,
                boxShadow: reveal > 0.8 ? `0 0 34px ${tone}33` : 'none',
                opacity: 0.35 + reveal * 0.65,
                transform: `translateY(${(1 - reveal) * 14}px)`,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                overflow: 'hidden',
                padding: isMontage ? 8 : 12,
                position: 'relative',
              }}
            >
              {shouldGenerateFallback ? (
                <GeneratedSourceDiagram
                  scene={scene}
                  slot={generatedSlots[index] ?? generatedSlots[0]}
                  index={index}
                  tone={tone}
                  compact={isMontage}
                />
              ) : null}
              {imagePaths[index] ? (
                <Img
                  src={staticFile(imagePaths[index])}
                  style={{
                    position: 'absolute',
                    inset: isMontage ? 8 : 12,
                    maxWidth: `calc(100% - ${isMontage ? 16 : 24}px)`,
                    maxHeight: `calc(100% - ${isMontage ? 16 : 24}px)`,
                    objectFit: 'contain',
                    margin: 'auto',
                    zIndex: 2,
                  }}
                />
              ) : null}
            </div>
          );
        })}
      </div>
      <div
        style={{
          position: 'absolute',
          left: 36,
          right: 36,
          bottom: 24,
          color: theme.muted,
          fontFamily: fonts.sans,
          fontSize: 22,
          lineHeight: 1.25,
        }}
      >
        {scene.artifact.caption ?? 'English labels are preserved as source material.'}
      </div>
    </div>
  );
};

const buildGeneratedDiagramSlots = (scene: Scene) => {
  const refs =
    scene.sourceDiagramRefs && scene.sourceDiagramRefs.length > 0
      ? scene.sourceDiagramRefs
      : scene.sources && scene.sources.length > 0
        ? scene.sources
        : [scene.artifact.type];
  const nodes =
    scene.artifact.nodes.length > 0
      ? scene.artifact.nodes
      : [scene.claim, scene.focus].filter(Boolean);

  return refs.slice(0, 3).map((ref, index) => ({
    id: `${scene.id}-generated-${index}`,
    ref,
    title: readableDiagramTitle(ref, scene, index),
    nodes,
  }));
};

const readableDiagramTitle = (ref: string, scene: Scene, index: number) => {
  const title = ref
    .replace(/^pdf:/, 'PDF ')
    .replace(/[-_]/g, ' ')
    .replace(/\b\w/g, (char) => char.toUpperCase());

  if (title && title !== scene.artifact.type) {
    return title;
  }

  return index === 0 ? scene.claim : `${scene.claim} ${index + 1}`;
};

const GeneratedSourceDiagram = ({
  scene,
  slot,
  index,
  tone,
  compact,
}: {
  scene: Scene;
  slot?: ReturnType<typeof buildGeneratedDiagramSlots>[number];
  index: number;
  tone: string;
  compact: boolean;
}) => {
  const nodes = (slot?.nodes ?? [scene.claim, scene.focus]).slice(0, compact ? 3 : 5);
  const title = slot?.title ?? scene.claim;

  return (
    <div
      style={{
        position: 'absolute',
        inset: compact ? 8 : 12,
        zIndex: 1,
        borderRadius: compact ? 14 : 18,
        background:
          'linear-gradient(135deg, rgba(246,244,239,0.98), rgba(224,233,235,0.96))',
        color: '#132029',
        fontFamily: fonts.sans,
        padding: compact ? 13 : 22,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
      }}
    >
      <div>
        <div
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            borderRadius: 999,
            background: tone,
            color: '#061015',
            fontFamily: fonts.mono,
            fontSize: compact ? 10 : 13,
            fontWeight: 900,
            letterSpacing: 0.4,
            textTransform: 'uppercase',
            padding: compact ? '5px 8px' : '7px 11px',
          }}
        >
          Generated from scene
        </div>
        <div
          style={{
            marginTop: compact ? 10 : 18,
            fontSize: compact ? 18 : 30,
            lineHeight: 1.08,
            fontWeight: 900,
          }}
        >
          {title}
        </div>
      </div>
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: compact ? '1fr' : `repeat(${Math.min(3, nodes.length)}, 1fr)`,
          gap: compact ? 8 : 12,
          alignItems: 'center',
        }}
      >
        {nodes.map((node, nodeIndex) => (
          <div
            key={`${node}-${nodeIndex}`}
            style={{
              minHeight: compact ? 34 : 58,
              borderRadius: compact ? 10 : 14,
              border: `1px solid ${nodeIndex === index % Math.max(1, nodes.length) ? tone : 'rgba(19,32,41,0.24)'}`,
              background:
                nodeIndex === index % Math.max(1, nodes.length)
                  ? 'rgba(97,216,255,0.16)'
                  : 'rgba(255,255,255,0.62)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              textAlign: 'center',
              padding: compact ? '5px 7px' : '9px 10px',
              fontSize: compact ? 12 : 18,
              lineHeight: 1.12,
              fontWeight: 800,
            }}
          >
            {node}
          </div>
        ))}
      </div>
      <div
        style={{
          fontFamily: fonts.mono,
          color: 'rgba(19,32,41,0.62)',
          fontSize: compact ? 9 : 12,
          letterSpacing: 0.4,
          textTransform: 'uppercase',
        }}
      >
        {slot?.ref ?? scene.sources?.[0] ?? 'source-derived'} / fallback {index + 1}
      </div>
    </div>
  );
};

const NodePath = ({scene, progress}: ArtifactProps) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const tone = activeTone(scene.artifact.type);
  const nodes = scene.artifact.nodes;
  const nodeWidth = 164;
  const nodeRadius = nodeWidth / 2;
  const railLeft = 88;
  const railWidth = 644;
  const nodeX = (index: number) =>
    railLeft + (nodes.length === 1 ? 0 : (railWidth / (nodes.length - 1)) * index);

  return (
    <div
      style={{
        width: 820,
        height: 520,
        position: 'relative',
        border: `1px solid ${theme.line}`,
        borderRadius: 34,
        background: 'rgba(9, 14, 18, 0.66)',
        boxShadow: `0 0 80px rgba(97, 216, 255, 0.08), inset 0 0 60px rgba(97, 216, 255, 0.03)`,
        overflow: 'hidden',
      }}
    >
      {nodes.slice(0, -1).map((node, index) => {
        const from = nodeX(index) + nodeRadius + 18;
        const to = nodeX(index + 1) - nodeRadius - 18;
        const segmentWidth = Math.max(12, to - from);
        const segmentStart = 0.08 + index * (0.78 / Math.max(1, nodes.length - 1));
        const segmentEnd = segmentStart + 0.22;
        const activation = interpolate(progress, [segmentStart, segmentEnd], [0, 1], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });

        return (
          <div
            key={`${node}-${nodes[index + 1]}`}
            style={{
              position: 'absolute',
              left: from,
              top: 258,
              width: segmentWidth,
              height: 3,
              background: theme.line,
              zIndex: 1,
            }}
          >
            <div
              style={{
                width: `${activation * 100}%`,
                height: '100%',
                background: tone,
                boxShadow: activation > 0 ? `0 0 28px ${tone}` : 'none',
              }}
            />
          </div>
        );
      })}
      {nodes.map((node, index) => {
        const x = nodeX(index);
        const reveal = spring({
          frame: frame - index * 9,
          fps,
          config: {damping: 16, stiffness: 90},
        });
        const isActive = progress > index / Math.max(1, nodes.length);

        return (
          <div
            key={node}
            style={{
              position: 'absolute',
              left: x - 82,
              top: 190 + (index % 2 === 0 ? -18 : 22),
              width: 164,
              minHeight: 124,
              zIndex: 2,
              opacity: reveal,
              transform: `translateY(${(1 - reveal) * 22}px)`,
              borderRadius: 24,
              border: `1px solid ${isActive ? tone : theme.line}`,
              background: isActive
                ? `linear-gradient(180deg, rgba(23,46,57,0.98), rgba(15,24,31,0.98))`
                : 'rgba(17,24,32,0.98)',
              boxShadow: isActive ? `0 0 34px ${tone}33` : 'none',
              color: theme.text,
              fontFamily: fonts.sans,
              fontSize: 28,
              fontWeight: 700,
              lineHeight: 1.18,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              textAlign: 'center',
              padding: 18,
            }}
          >
            {node}
          </div>
        );
      })}
      <ArtifactLabel scene={scene} tone={tone} />
    </div>
  );
};

const CostTriangle = ({scene, progress}: ArtifactProps) => {
  const tone = theme.amber;
  const nodes = scene.artifact.nodes;

  return (
    <div
      style={{
        width: 760,
        height: 520,
        position: 'relative',
        borderRadius: 34,
        background: 'rgba(12, 13, 12, 0.72)',
        border: `1px solid ${theme.line}`,
        overflow: 'hidden',
      }}
    >
      <svg
        width="760"
        height="520"
        style={{position: 'absolute', inset: 0, opacity: 0.75, zIndex: 1}}
      >
        <path
          d="M380 206 L209 314 M380 206 L555 314 M209 314 L555 314"
          stroke={tone}
          strokeWidth="3"
          strokeDasharray="12 16"
          strokeLinecap="round"
          opacity={interpolate(progress, [0.2, 0.9], [0.15, 0.9])}
        />
      </svg>
      {nodes.map((node, index) => {
        const positions = [
          {left: 298, top: 88},
          {left: 126, top: 314},
          {left: 472, top: 314},
        ];
        const position = positions[index] ?? positions[0];
        const reveal = progress > index * 0.22 ? 1 : 0.25;

        return (
          <div
            key={node}
            style={{
              position: 'absolute',
              ...position,
              zIndex: 2,
              width: 166,
              height: 118,
              borderRadius: 24,
              border: `1px solid ${tone}`,
              color: theme.text,
              background:
                reveal > 0.5 ? 'rgba(44, 31, 16, 0.98)' : 'rgba(17, 24, 32, 0.98)',
              boxShadow: reveal > 0.5 ? `0 0 34px ${tone}44` : 'none',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontFamily: fonts.sans,
              fontSize: 32,
              fontWeight: 800,
            }}
          >
            {node}
          </div>
        );
      })}
      <ArtifactLabel scene={scene} tone={tone} />
    </div>
  );
};

const Harness = ({scene, progress}: ArtifactProps) => {
  const controls = scene.artifact.nodes;
  const visibleCount = Math.ceil(progress * controls.length);

  return (
    <div
      style={{
        width: 820,
        height: 520,
        position: 'relative',
        borderRadius: 34,
        border: `1px solid ${theme.line}`,
        background: 'rgba(9, 14, 18, 0.72)',
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: 280,
          top: 188,
          width: 260,
          height: 132,
          borderRadius: 28,
          border: `1px solid ${theme.cyan}`,
          boxShadow: `0 0 44px ${theme.cyan}33`,
          color: theme.text,
          fontFamily: fonts.sans,
          fontSize: 34,
          fontWeight: 900,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          background: 'rgba(97,216,255,0.11)',
        }}
      >
        Agent
      </div>
      {controls.map((control, index) => {
        const angle = (-150 + index * 60) * (Math.PI / 180);
        const x = 410 + Math.cos(angle) * 296;
        const y = 254 + Math.sin(angle) * 186;
        const active = index < visibleCount;

        return (
          <div
            key={control}
            style={{
              position: 'absolute',
              left: x - 78,
              top: y - 45,
              width: 156,
              height: 90,
              borderRadius: 22,
              border: `1px solid ${active ? theme.cyan : theme.line}`,
              color: active ? theme.text : theme.muted,
              background: active ? 'rgba(97,216,255,0.1)' : 'rgba(17,24,32,0.62)',
              fontFamily: fonts.sans,
              fontSize: 28,
              fontWeight: 800,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: active ? `0 0 24px ${theme.cyan}2e` : 'none',
            }}
          >
            {control}
          </div>
        );
      })}
      <ArtifactLabel scene={scene} tone={theme.cyan} />
    </div>
  );
};

const SelectionMatrix = ({scene, progress}: ArtifactProps) => {
  return (
    <div
      style={{
        width: 820,
        height: 520,
        borderRadius: 34,
        border: `1px solid ${theme.line}`,
        background: 'rgba(9, 14, 18, 0.72)',
        padding: 54,
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: 22,
        position: 'relative',
      }}
    >
      {scene.artifact.nodes.map((node, index) => {
        const active = progress > index * 0.14;
        return (
          <div
            key={node}
            style={{
              borderRadius: 24,
              border: `1px solid ${active ? theme.cyan : theme.line}`,
              background: active ? 'rgba(97,216,255,0.11)' : 'rgba(17,24,32,0.65)',
              color: active ? theme.text : theme.muted,
              fontFamily: fonts.sans,
              fontSize: 34,
              fontWeight: 900,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            {node}
          </div>
        );
      })}
      <ArtifactLabel scene={scene} tone={theme.cyan} />
    </div>
  );
};

const ArtifactLabel = ({scene, tone}: {scene: Scene; tone: string}) => {
  return (
    <div
      style={{
        position: 'absolute',
        left: 36,
        bottom: 28,
        right: 36,
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        color: theme.muted,
        fontFamily: fonts.mono,
        fontSize: 17,
        letterSpacing: 1.2,
        textTransform: 'uppercase',
      }}
    >
      <span>{scene.artifact.type}</span>
      <span style={{color: tone}}>focus / active</span>
    </div>
  );
};
