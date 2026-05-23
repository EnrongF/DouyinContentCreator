import {AbsoluteFill} from 'remotion';
import {founderTheme} from '../components/founder-playbook/founderTheme';
import type {FounderSceneGraph} from '../components/founder-playbook/types';

type FounderPlaybookCoverProps = {
  sceneGraph: FounderSceneGraph;
  variant?: 'vertical' | 'grid';
};

const c = founderTheme.colors;
const fonts = founderTheme.fonts;

export const FounderPlaybookCover = ({sceneGraph, variant = 'vertical'}: FounderPlaybookCoverProps) => {
  const isGrid = variant === 'grid';
  const topPad = isGrid ? 92 : 132;
  const titleSize = isGrid ? 76 : 88;
  const visualTop = isGrid ? 660 : 760;
  const episodeLabel = `EP${String(sceneGraph.episode).padStart(2, '0')}`;
  const coverTitle =
    sceneGraph.episode === 5
      ? '护城河，\n藏在业务流程里'
      : sceneGraph.episode === 4
      ? '创始人，\n别当中转站'
      : sceneGraph.episode === 3
      ? '先写边界，\n再写代码'
      : sceneGraph.episode === 2
        ? '有 Demo，\n不代表有人要'
        : 'AI 创业，\n真正卡的是判断';
  const subhead =
    sceneGraph.episode === 5
      ? '模型能接入，流程细节才会沉淀。'
      : sceneGraph.episode === 4
      ? '上线后，重复发生的问题要变成系统。'
      : sceneGraph.episode === 3
      ? 'AI 写得越快，越要先锁住产品范围。'
      : sceneGraph.episode === 2
        ? 'Demo 是提问工具，不是需求证据。'
        : '速度不是答案，先判断什么值得做。';
  const chips =
    sceneGraph.episode === 5
      ? ['Scale', 'Workflow', 'Moat']
      : sceneGraph.episode === 4
      ? ['Launch', 'System', 'Judgment']
      : sceneGraph.episode === 3
      ? ['Boundary', 'Context', 'Code']
      : sceneGraph.episode === 2
        ? ['Prototype', 'Void', 'Signal']
        : ['Speed', 'Judgment', 'Idea Gate'];
  const decisionCards =
    sceneGraph.episode === 5
      ? [
          ['模型', 'Access'],
          ['流程', 'Workflow'],
        ]
      : sceneGraph.episode === 4
      ? [
          ['中转站', 'Router'],
          ['系统', 'System'],
        ]
      : sceneGraph.episode === 2
      ? [
          ['夸 Demo', 'Praise'],
          ['真痛点', 'Pain'],
        ]
      : [
          ['速度', 'Speed'],
          ['判断', 'Judgment'],
        ];
  const lifecycle = sceneGraph.episode === 2
    ? [
        ['Idea', '验证'],
        ['Demo', '道具'],
        ['Evidence', '证据'],
        ['MVP', '下一关'],
      ]
    : [
        ['Idea', '该不该做'],
      ['MVP', '边界'],
      ['Launch', '系统'],
      ['Scale', '护城河'],
    ];
  const activeLifecycleIndex = sceneGraph.episode === 5 ? 3 : sceneGraph.episode === 4 ? 2 : 0;

  return (
    <AbsoluteFill
      style={{
        overflow: 'hidden',
        background: c.page,
        color: c.ink,
        fontFamily: fonts.cn,
      }}
    >
      <CoverField />
      <main
        style={{
          position: 'relative',
          zIndex: 2,
          height: '100%',
          padding: `${topPad}px 86px 64px`,
          display: 'grid',
          gridTemplateRows: `${isGrid ? 500 : 590}px 1fr ${isGrid ? 96 : 134}px`,
        }}
      >
        <section>
          <div style={{display: 'flex', alignItems: 'center', gap: 16}}>
            <div
              style={{
                width: 76,
                height: 76,
                borderRadius: 8,
                display: 'grid',
                placeItems: 'center',
                background: c.amber,
                color: '#101214',
                fontFamily: fonts.ui,
                fontSize: 26,
                fontWeight: 950,
                boxShadow: `0 0 32px ${c.amber}55`,
              }}
            >
              {episodeLabel}
            </div>
            <div style={{display: 'grid', gap: 8}}>
              <div style={{fontFamily: fonts.mono, color: c.cyan, fontSize: 18, fontWeight: 900}}>
                THE FOUNDER&apos;S PLAYBOOK
              </div>
              <div style={{fontFamily: fonts.ui, color: c.muted, fontSize: 20, fontWeight: 850}}>
                AI-Native Startup
              </div>
            </div>
          </div>

          <h1
            style={{
              margin: '78px 0 0',
              maxWidth: 880,
              fontSize: titleSize,
              lineHeight: 1.08,
              letterSpacing: 0,
              fontWeight: 950,
              whiteSpace: 'pre-line',
              textShadow: '0 0 26px rgba(255,248,234,0.24), 0 2px 18px rgba(0,0,0,0.46)',
            }}
          >
            {coverTitle}
          </h1>

          <p
            style={{
              margin: '30px 0 0',
              maxWidth: 850,
              color: c.soft,
              fontSize: isGrid ? 34 : 38,
              lineHeight: 1.28,
              fontWeight: 900,
            }}
          >
            {subhead}
          </p>

          <div style={{display: 'flex', gap: 12, marginTop: 28}}>
            {chips.map((chip, index) => (
              <span
                key={chip}
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: 9,
                  minHeight: 38,
                  padding: '8px 16px',
                  border: '1px solid rgba(255,248,234,0.26)',
                  borderRadius: 999,
                  background: 'rgba(255,248,234,0.085)',
                  color: c.ink,
                  fontFamily: fonts.ui,
                  fontSize: 18,
                  fontWeight: 900,
                }}
              >
                <i
                  style={{
                    width: 12,
                    height: 12,
                    borderRadius: 99,
                    background: index === 1 ? c.cyan : index === 2 ? c.amber : c.orange,
                  }}
                />
                {chip}
              </span>
            ))}
          </div>
        </section>

        <section style={{position: 'relative'}}>
          {sceneGraph.episode === 3 ? (
            <Ep03CoverVisual isGrid={isGrid} visualTop={visualTop} />
          ) : sceneGraph.episode === 2 ? (
            <Ep02CoverVisual isGrid={isGrid} visualTop={visualTop} />
          ) : (
            <>
              <div
                style={{
                  position: 'absolute',
                  left: 0,
                  right: 0,
                  top: visualTop - (isGrid ? 630 : 720),
                  display: 'grid',
                  gridTemplateColumns: '1fr 1fr',
                  gap: 24,
                }}
              >
                <DecisionCard label={decisionCards[0][0]} sublabel={decisionCards[0][1]} active={false} />
                <DecisionCard label={decisionCards[1][0]} sublabel={decisionCards[1][1]} active />
              </div>
              <div
                style={{
                  position: 'absolute',
                  left: 18,
                  right: 18,
                  top: visualTop - (isGrid ? 320 : 386),
                  display: 'grid',
                  gridTemplateColumns: 'repeat(4, 1fr)',
                  gap: 12,
                  opacity: 0.92,
                }}
              >
                {lifecycle.map(([stage, label], index) => (
                  <div
                    key={stage}
                    style={{
                      minHeight: isGrid ? 118 : 142,
                      display: 'grid',
                      placeItems: 'center',
                      alignContent: 'center',
                      gap: 8,
                      borderRadius: 8,
                      border: `1px solid ${index === activeLifecycleIndex ? c.amber : 'rgba(255,248,234,0.18)'}`,
                      background: index === activeLifecycleIndex ? `${c.amber}24` : 'rgba(255,248,234,0.045)',
                      color: index === activeLifecycleIndex ? c.ink : c.muted,
                      fontFamily: fonts.ui,
                      fontSize: 19,
                      fontWeight: 950,
                      textAlign: 'center',
                    }}
                  >
                    {stage}
                    <small style={{fontFamily: fonts.cn, fontSize: 16, fontWeight: 850}}>{label}</small>
                  </div>
                ))}
              </div>
            </>
          )}
        </section>

        <footer
          style={{
            display: 'flex',
            alignItems: 'end',
            justifyContent: 'space-between',
            gap: 24,
            color: 'rgba(255,248,234,0.5)',
            fontFamily: fonts.ui,
            fontSize: 16,
          }}
        >
          <span>Source: The Founder&apos;s Playbook / Building an AI-Native Startup</span>
          <span>{episodeLabel}</span>
        </footer>
      </main>
    </AbsoluteFill>
  );
};

const DecisionCard = ({label, sublabel, active}: {label: string; sublabel: string; active?: boolean}) => (
  <div
    style={{
      minHeight: 246,
      display: 'grid',
      placeItems: 'center',
      alignContent: 'center',
      gap: 14,
      borderRadius: 8,
      border: `1px solid ${active ? c.amber : 'rgba(255,248,234,0.18)'}`,
      background: active ? `${c.amber}22` : 'rgba(255,248,234,0.055)',
      color: active ? c.ink : c.muted,
      fontFamily: fonts.cn,
      fontSize: 48,
      fontWeight: 950,
      boxShadow: active ? `0 0 36px ${c.amber}2c` : 'none',
    }}
  >
    {label}
    <small style={{fontFamily: fonts.ui, fontSize: 22, color: active ? c.amber : c.muted}}>{sublabel}</small>
  </div>
);

const Ep02CoverVisual = ({isGrid, visualTop}: {isGrid: boolean; visualTop: number}) => {
  const upperTop = visualTop - (isGrid ? 620 : 706);
  const lowerTop = visualTop - (isGrid ? 312 : 380);
  return (
    <>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: upperTop,
          display: 'grid',
          gridTemplateColumns: '0.95fr 72px 1.25fr',
          gap: 14,
          alignItems: 'center',
        }}
      >
        <CoverNode label="原型态" sublabel="Demo" tone={c.orange} concept="build" />
        <CoverArrow />
        <CoverNode label="提问向量" sublabel="正确用法" tone={c.cyan} active concept="question" />
      </div>
      <div
        style={{
          position: 'absolute',
          left: 18,
          right: 18,
          top: lowerTop,
          display: 'grid',
          gridTemplateColumns: '1fr 1.14fr',
          gap: 18,
          alignItems: 'end',
        }}
      >
        <SignalCard label="表层反馈" sublabel="夸 Demo" active={false} concept="void" />
        <SignalCard label="痛点信号" sublabel="更像证据" active concept="signal" />
      </div>
      <div
        style={{
          position: 'absolute',
          left: 24,
          right: 24,
          top: lowerTop + (isGrid ? 228 : 266),
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: 12,
        }}
      >
        {['问题真实?', '方案匹配?', '信号足够?'].map((label, index) => (
          <div
            key={label}
            style={{
              minHeight: isGrid ? 70 : 82,
              display: 'grid',
              placeItems: 'center',
              borderRadius: 8,
              border: `1px solid ${index === 2 ? c.amber : 'rgba(255,248,234,0.18)'}`,
              background: index === 2 ? `${c.amber}20` : 'rgba(255,248,234,0.045)',
              color: index === 2 ? c.ink : c.muted,
              fontFamily: fonts.cn,
              fontSize: isGrid ? 18 : 20,
              fontWeight: 950,
              textAlign: 'center',
            }}
          >
            {label}
          </div>
        ))}
      </div>
    </>
  );
};

const Ep03CoverVisual = ({isGrid, visualTop}: {isGrid: boolean; visualTop: number}) => {
  const upperTop = visualTop - (isGrid ? 624 : 710);
  const lowerTop = visualTop - (isGrid ? 312 : 382);
  return (
    <>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: upperTop,
          display: 'grid',
          gridTemplateColumns: '1fr 74px 1fr',
          gap: 14,
          alignItems: 'center',
        }}
      >
        <CoverNode label="边界" sublabel="scope" tone={c.amber} active concept="boundary" />
        <CoverArrow />
        <CoverNode label="代码" sublabel="execution" tone={c.orange} concept="build" />
      </div>
      <div
        style={{
          position: 'absolute',
          left: 18,
          right: 18,
          top: lowerTop,
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: 14,
        }}
      >
        {[
          ['解决什么', 'does', 'boundary'],
          ['不解决什么', 'not now', 'void'],
          ['证据能加', 'threshold', 'signal'],
        ].map(([label, sublabel, concept], index) => (
          <SignalCard
            key={label}
            label={label}
            sublabel={sublabel}
            active={index === 0 || index === 2}
            concept={concept as CoverConcept}
          />
        ))}
      </div>
      <div
        style={{
          position: 'absolute',
          left: 36,
          right: 36,
          top: lowerTop + (isGrid ? 226 : 266),
          minHeight: isGrid ? 78 : 92,
          display: 'grid',
          gridTemplateColumns: '1fr 76px 1fr',
          gap: 12,
          alignItems: 'center',
          color: c.muted,
          fontFamily: fonts.cn,
          fontSize: isGrid ? 21 : 24,
          fontWeight: 950,
        }}
      >
        <span style={{textAlign: 'right'}}>上下文</span>
        <CoverConceptGlyph concept="mismatch" tone={c.rose} />
        <span>不漂移</span>
      </div>
    </>
  );
};

type CoverConcept = 'build' | 'question' | 'signal' | 'void' | 'boundary' | 'mismatch';

const CoverConceptGlyph = ({concept, tone}: {concept: CoverConcept; tone: string}) => (
  <svg width="82" height="82" viewBox="0 0 100 100" aria-hidden="true">
    <rect x="13" y="13" width="74" height="74" rx="8" fill="rgba(255,248,234,0.035)" stroke="rgba(255,248,234,0.16)" strokeWidth="2" />
    {concept === 'build' && (
      <>
        <rect x="27" y="30" width="46" height="10" rx="5" fill={tone} opacity="0.72" />
        <rect x="27" y="47" width="46" height="10" rx="5" fill={c.amber} opacity="0.82" />
        <rect x="27" y="64" width="46" height="10" rx="5" fill={c.cyan} opacity="0.54" />
      </>
    )}
    {concept === 'question' && (
      <>
        <circle cx="28" cy="64" r="7" fill={c.amber} />
        <circle cx="50" cy="46" r="7" fill={c.cyan} />
        <circle cx="73" cy="30" r="7" fill={c.cyan} opacity="0.76" />
        <path d="M28 64L50 46L73 30" fill="none" stroke={c.cyan} strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" />
      </>
    )}
    {concept === 'signal' && (
      <>
        <path d="M24 72H76" fill="none" stroke="rgba(255,248,234,0.2)" strokeWidth="5" strokeLinecap="round" />
        <rect x="30" y="52" width="9" height="20" rx="4.5" fill={c.rose} opacity="0.62" />
        <rect x="46" y="39" width="9" height="33" rx="4.5" fill={c.amber} opacity="0.82" />
        <rect x="62" y="25" width="9" height="47" rx="4.5" fill={c.cyan} />
      </>
    )}
    {concept === 'void' && (
      <>
        <rect x="30" y="30" width="40" height="40" rx="8" fill="none" stroke={c.rose} strokeWidth="6" strokeDasharray="8 8" />
        <path d="M42 50H58" fill="none" stroke="rgba(255,248,234,0.28)" strokeWidth="5" strokeLinecap="round" />
      </>
    )}
    {concept === 'boundary' && (
      <>
        <rect x="25" y="24" width="50" height="52" rx="7" fill="none" stroke={tone} strokeWidth="6" />
        <path d="M40 25V75M60 25V75" fill="none" stroke="rgba(255,248,234,0.24)" strokeWidth="4" strokeLinecap="round" />
        <path d="M25 50H75" fill="none" stroke={c.cyan} strokeWidth="6" strokeLinecap="round" />
      </>
    )}
    {concept === 'mismatch' && (
      <>
        <path d="M18 34H40C61 34 58 66 82 66" fill="none" stroke={c.rose} strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" />
        <path d="M18 66H42C60 66 58 34 82 34" fill="none" stroke={c.cyan} strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" />
        <circle cx="50" cy="50" r="8" fill={c.amber} />
      </>
    )}
  </svg>
);

const CoverNode = ({
  label,
  sublabel,
  tone,
  active,
  concept,
}: {
  label: string;
  sublabel: string;
  tone: string;
  active?: boolean;
  concept: CoverConcept;
}) => (
  <div
    style={{
      minHeight: 204,
      display: 'grid',
      placeItems: 'center',
      alignContent: 'center',
      gap: 12,
      borderRadius: 8,
      border: `1px solid ${active ? tone : 'rgba(255,248,234,0.18)'}`,
      background: active ? `${tone}22` : 'rgba(255,248,234,0.055)',
      color: active ? c.ink : c.muted,
      fontFamily: fonts.cn,
      fontSize: 44,
      fontWeight: 950,
      textAlign: 'center',
      boxShadow: active ? `0 0 34px ${tone}24` : 'none',
    }}
  >
    <CoverConceptGlyph concept={concept} tone={tone} />
    {label}
    <small style={{fontFamily: fonts.ui, fontSize: 21, color: tone, fontWeight: 900}}>{sublabel}</small>
  </div>
);

const CoverArrow = () => (
  <div
    style={{
      height: 8,
      borderRadius: 999,
      background: `linear-gradient(90deg, ${c.orange}, ${c.cyan})`,
      boxShadow: `0 0 22px ${c.cyan}55`,
    }}
  />
);

const SignalCard = ({label, sublabel, active, concept}: {label: string; sublabel: string; active?: boolean; concept: CoverConcept}) => (
  <div
    style={{
      minHeight: active ? 180 : 140,
      display: 'grid',
      placeItems: 'center',
      alignContent: 'center',
      gap: 10,
      borderRadius: 8,
      border: `1px solid ${active ? c.amber : 'rgba(255,248,234,0.16)'}`,
      background: active ? `${c.amber}22` : 'rgba(255,248,234,0.045)',
      color: active ? c.ink : c.muted,
      fontFamily: fonts.cn,
      fontSize: active ? 40 : 34,
      fontWeight: 950,
      textAlign: 'center',
      boxShadow: active ? `0 0 34px ${c.amber}24` : 'none',
    }}
  >
    <CoverConceptGlyph concept={concept} tone={active ? c.amber : c.rose} />
    {label}
    <small style={{fontFamily: fonts.ui, fontSize: 19, color: active ? c.amber : c.muted, fontWeight: 900}}>{sublabel}</small>
  </div>
);

const CoverField = () => (
  <>
    <div
      style={{
        position: 'absolute',
        inset: 0,
        background:
          'linear-gradient(132deg, rgba(255,194,26,0.34), rgba(255,122,56,0.14) 26%, transparent 47%), linear-gradient(312deg, rgba(50,200,232,0.15), transparent 40%), linear-gradient(180deg, rgba(255,248,234,0.025), transparent 42%, rgba(255,248,234,0.045))',
      }}
    />
    <div
      style={{
        position: 'absolute',
        inset: 0,
        background:
          'linear-gradient(175deg, transparent 0 41%, rgba(0,0,0,0.48) 68%, rgba(0,0,0,0.18)), repeating-linear-gradient(0deg, transparent 0 122px, rgba(255,248,234,0.034) 123px, transparent 125px)',
      }}
    />
    <div
      style={{
        position: 'absolute',
        left: '-34%',
        right: '-34%',
        top: '34%',
        height: '54%',
        border: '1px solid rgba(255,248,234,0.12)',
        borderRadius: '50%',
        transform: 'rotate(-8deg)',
      }}
    />
  </>
);
