import {AbsoluteFill, Img, staticFile} from 'remotion';
import {Background} from '../components/Background';
import {fonts, theme} from '../styles/theme';
import type {SceneGraph} from '../types';

type CoverProps = {
  sceneGraph: SceneGraph;
};

const coverMeta = (sceneGraph: SceneGraph) => ({
  isSourceLogicCover: sceneGraph.cover.artifact === 'source-architecture-choice',
  proofChips: sceneGraph.cover.proofChips ?? ['Architecture', 'Coordination', 'Workflow'],
  episodeTag: sceneGraph.cover.badge.match(/EP\d+/i)?.[0] ?? 'SERIES',
});

const mesh = {
  black: '#0f0f10',
  ink: '#1d1d1f',
  cream: '#fefef7',
  paper: '#f7f3ee',
  muted: '#868f97',
  orange: '#fb7232',
  gold: '#f7b500',
  blue: '#32c5ff',
  pink: '#fd86c7',
};

const meshFonts = {
  cn:
    '"Resource Han Rounded CN", "GenSenRounded TW", "GenSenRounded2 TW", "GenJyuuGothic", "Source Han Sans SC", "Noto Sans CJK SC", "Noto Sans SC", "Sarasa UI SC", "PingFang SC", sans-serif',
  ui: '"Avenir Next", "Helvetica Neue", "Inter", "PingFang SC", system-ui, sans-serif',
  mono: fonts.mono,
};

export const Cover = ({sceneGraph}: CoverProps) => {
  const {isSourceLogicCover, proofChips, episodeTag} = coverMeta(sceneGraph);

  return (
    <AbsoluteFill style={{color: theme.text}}>
      <Background />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'radial-gradient(circle at 72% 42%, rgba(97,216,255,0.18), transparent 34%), linear-gradient(90deg, rgba(3,7,10,0.5) 0%, rgba(3,7,10,0.15) 45%, rgba(3,7,10,0.62) 100%)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          padding: '72px 92px 72px',
          display: 'grid',
          gridTemplateColumns: '1.02fr 0.98fr',
          columnGap: 42,
        }}
      >
        <section style={{display: 'flex', flexDirection: 'column', justifyContent: 'space-between'}}>
          <div>
            <div style={{display: 'flex', alignItems: 'center', gap: 18}}>
              <div
                style={{
                  width: 76,
                  height: 76,
                  borderRadius: 16,
                  background: theme.amber,
                  color: '#0b0f12',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontFamily: fonts.display,
                  fontSize: 30,
                  fontWeight: 900,
                  boxShadow: `0 0 34px ${theme.amber}55`,
                }}
              >
                {episodeTag}
              </div>
              <div
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  border: `1px solid ${theme.line}`,
                  borderRadius: 999,
                  padding: '12px 20px',
                  color: theme.cyan,
                  fontFamily: fonts.mono,
                  fontSize: 22,
                  letterSpacing: 0,
                  textTransform: 'uppercase',
                  background: 'rgba(17,24,32,0.72)',
                }}
              >
                {sceneGraph.cover.badge}
              </div>
            </div>
            <h1
              style={{
                margin: '58px 0 0',
                fontFamily: fonts.display,
                fontSize: 126,
                lineHeight: 0.98,
                letterSpacing: 0,
                fontWeight: 900,
                textShadow: '0 10px 0 rgba(0,0,0,0.34), 0 0 34px rgba(97,216,255,0.15)',
                WebkitTextStroke: '1px rgba(255,255,255,0.18)',
              }}
            >
              <HeadlineText text={sceneGraph.cover.headline} />
            </h1>
            <p
              style={{
                margin: '34px 0 0',
                fontFamily: fonts.sans,
                color: theme.text,
                fontSize: 43,
                lineHeight: 1.28,
                maxWidth: 780,
                fontWeight: 800,
                textShadow: '0 6px 18px rgba(0,0,0,0.5)',
              }}
            >
              {sceneGraph.cover.subhead}
            </p>
            <div style={{display: 'flex', gap: 14, flexWrap: 'wrap', marginTop: 36}}>
              {proofChips.map((chip, index) => (
                <div
                  key={chip}
                  style={{
                    height: 50,
                    borderRadius: 12,
                    border: `1px solid ${index === 0 ? theme.amber : theme.line}`,
                    background:
                      index === 0 ? 'rgba(240,180,76,0.2)' : 'rgba(17,24,32,0.9)',
                    color: index === 0 ? theme.amber : theme.cyan,
                    display: 'flex',
                    alignItems: 'center',
                    padding: '0 20px',
                    fontFamily: fonts.mono,
                    fontSize: 18,
                    letterSpacing: 0,
                    textTransform: 'uppercase',
                    fontWeight: 800,
                  }}
                >
                  {chip}
                </div>
              ))}
            </div>
          </div>
          <div
            style={{
              fontFamily: fonts.mono,
              fontSize: 20,
              color: theme.muted,
              letterSpacing: 0,
              lineHeight: 1.2,
              maxWidth: 720,
            }}
          >
            {sceneGraph.cover.sourceMark ?? 'Executive Technical Documentary / 16:9'}
          </div>
        </section>
        <section
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          {isSourceLogicCover ? (
            <SourceArchitectureChoice />
          ) : sceneGraph.cover.visuals?.length ? (
            <GenericCoverProof visuals={sceneGraph.cover.visuals} />
          ) : (
            <DecisionLadder />
          )}
        </section>
      </div>
    </AbsoluteFill>
  );
};

export const CoverVertical = ({sceneGraph}: CoverProps) => {
  const {isSourceLogicCover, proofChips, episodeTag} = coverMeta(sceneGraph);

  return (
    <AbsoluteFill style={{color: theme.text, background: theme.graphite}}>
      <Background />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'radial-gradient(circle at 64% 55%, rgba(97,216,255,0.2), transparent 34%), linear-gradient(180deg, rgba(3,7,10,0.16) 0%, rgba(3,7,10,0.66) 72%, rgba(3,7,10,0.92) 100%)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          padding: '82px 70px 86px',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'flex-start',
        }}
      >
        <div>
          <div style={{display: 'flex', alignItems: 'center', gap: 18}}>
            <div
              style={{
                width: 96,
                height: 96,
                borderRadius: 18,
                background: theme.amber,
                color: '#0b0f12',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontFamily: fonts.display,
                fontSize: 36,
                fontWeight: 900,
                boxShadow: `0 0 42px ${theme.amber}55`,
              }}
            >
              {episodeTag}
            </div>
            <div
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                border: `1px solid ${theme.line}`,
                borderRadius: 999,
                padding: '14px 22px',
                color: theme.cyan,
                fontFamily: fonts.mono,
                fontSize: 25,
                letterSpacing: 0,
                textTransform: 'uppercase',
                background: 'rgba(17,24,32,0.78)',
              }}
            >
              {sceneGraph.cover.badge}
            </div>
          </div>
          <h1
            style={{
              margin: '76px 0 0',
              fontFamily: fonts.display,
              fontSize: 134,
              lineHeight: 0.98,
              letterSpacing: 0,
              fontWeight: 900,
              textShadow: '0 12px 0 rgba(0,0,0,0.38), 0 0 42px rgba(97,216,255,0.2)',
              WebkitTextStroke: '1px rgba(255,255,255,0.18)',
            }}
          >
            <HeadlineText text={sceneGraph.cover.headline} />
          </h1>
          <p
            style={{
              margin: '42px 0 0',
              fontFamily: fonts.sans,
              color: theme.text,
              fontSize: 45,
              lineHeight: 1.28,
              maxWidth: 900,
              fontWeight: 900,
              textShadow: '0 6px 20px rgba(0,0,0,0.52)',
            }}
          >
            {sceneGraph.cover.subhead}
          </p>
          <div style={{display: 'flex', gap: 14, flexWrap: 'wrap', marginTop: 36}}>
            {proofChips.map((chip, index) => (
              <div
                key={chip}
                style={{
                  height: 54,
                  borderRadius: 12,
                  border: `1px solid ${index === 0 ? theme.amber : theme.line}`,
                  background: index === 0 ? 'rgba(240,180,76,0.22)' : 'rgba(17,24,32,0.92)',
                  color: index === 0 ? theme.amber : theme.cyan,
                  display: 'flex',
                  alignItems: 'center',
                  padding: '0 20px',
                  fontFamily: fonts.mono,
                  fontSize: 19,
                  letterSpacing: 0,
                  textTransform: 'uppercase',
                  fontWeight: 800,
                }}
              >
                {chip}
              </div>
            ))}
          </div>
        </div>
        <div style={{marginTop: 182}}>
          {isSourceLogicCover ? (
            <SourceArchitectureChoiceVertical />
          ) : sceneGraph.cover.visuals?.length ? (
            <GenericCoverProofVertical visuals={sceneGraph.cover.visuals} />
          ) : (
            <DecisionLadder />
          )}
          <div
            style={{
              marginTop: 40,
              fontFamily: fonts.mono,
              fontSize: 21,
              color: theme.muted,
              letterSpacing: 0,
              lineHeight: 1.25,
            }}
          >
            {sceneGraph.cover.sourceMark ?? 'Executive Technical Documentary / Douyin Vertical'}
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const CoverGrid = ({sceneGraph}: CoverProps) => {
  const {isSourceLogicCover, proofChips, episodeTag} = coverMeta(sceneGraph);
  const visuals = sceneGraph.cover.visuals;
  const headlineLines = gridHeadlineLines(sceneGraph.cover.headline);

  return (
    <AbsoluteFill style={{color: mesh.cream, background: mesh.black}}>
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'radial-gradient(42% 36% at 73% 3%, rgba(255,237,144,0.66), rgba(255,219,103,0.22) 48%, transparent 82%), radial-gradient(44% 40% at 58% 10%, rgba(255,255,241,0.72), rgba(255,153,130,0.46) 34%, transparent 78%), radial-gradient(36% 26% at 21% 4%, rgba(252,187,0,0.54), rgba(238,161,0,0.18) 58%, transparent 82%), radial-gradient(40% 25% at 74% 28%, rgba(253,134,199,0.34), rgba(171,64,125,0.12) 60%, transparent 82%), linear-gradient(180deg, rgba(15,15,16,0.1) 0%, rgba(15,15,16,0.72) 38%, rgba(15,15,16,0.96) 100%)',
          filter: 'saturate(1.08)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: '-18%',
          right: '-18%',
          bottom: '-18%',
          height: 520,
          background:
            'radial-gradient(50% 42% at 50% 44%, rgba(250,250,247,0.44), rgba(248,242,231,0.18) 68%, transparent 100%), radial-gradient(32% 26% at 31% 28%, rgba(255,216,108,0.42), rgba(255,178,104,0.12) 62%, transparent 100%)',
          filter: 'blur(18px)',
          opacity: 0.8,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: -250,
          top: 465,
          width: 1520,
          height: 900,
          borderRadius: '50%',
          border: '1px solid rgba(255,255,255,0.14)',
          transform: 'rotate(-12deg)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: -150,
          top: 548,
          width: 1280,
          height: 700,
          borderRadius: '50%',
          border: '1px solid rgba(255,255,255,0.1)',
          transform: 'rotate(8deg)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          padding: '78px 70px 52px',
          display: 'flex',
          flexDirection: 'column',
        }}
      >
        <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 12}}>
          <div
            style={{
              width: 56,
              height: 56,
              borderRadius: 12,
              background: mesh.gold,
              color: mesh.ink,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontFamily: meshFonts.ui,
              fontSize: 19,
              fontWeight: 900,
              boxShadow: `0 0 30px ${mesh.gold}66`,
            }}
          >
            {episodeTag}
          </div>
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              border: 'none',
              borderRadius: 999,
              padding: 0,
              color: mesh.muted,
              fontFamily: meshFonts.ui,
              fontSize: 20,
              letterSpacing: 0,
              background: 'transparent',
            }}
          >
            {sceneGraph.cover.badge}
          </div>
        </div>

        <h1
          style={{
            margin: '44px auto 0',
            fontFamily: meshFonts.cn,
            fontSize: gridHeadlineSize(sceneGraph.cover.headline),
            lineHeight: 1.06,
            letterSpacing: 0,
            fontWeight: 800,
            maxWidth: 930,
            textAlign: 'center',
            textShadow: `0 0 8px rgba(255,255,255,0.48), 0 16px 48px ${mesh.orange}33`,
          }}
        >
          {headlineLines.map((line) => (
            <span key={line} style={{display: 'block', transform: line.length >= 6 ? 'scaleX(0.97)' : undefined}}>
              {line}
            </span>
          ))}
        </h1>

        <p
          style={{
            margin: '24px auto 0',
            fontFamily: meshFonts.cn,
            color: 'rgba(254,254,247,0.74)',
            fontSize: 34,
            lineHeight: 1.36,
            maxWidth: 860,
            fontWeight: 430,
            textAlign: 'center',
            textShadow: '0 6px 18px rgba(0,0,0,0.5)',
          }}
        >
          {sceneGraph.cover.subhead}
        </p>

        <div style={{display: 'flex', justifyContent: 'center', gap: 10, flexWrap: 'wrap', marginTop: 24}}>
          {proofChips.slice(0, 3).map((chip, index) => (
            <div
              key={chip}
              style={{
                height: 40,
                borderRadius: 12,
                border: '1px solid rgba(255,255,255,0.42)',
                background: 'rgba(255,255,255,0.08)',
                color: mesh.cream,
                display: 'flex',
                alignItems: 'center',
                gap: 7,
                padding: '0 13px',
                fontFamily: meshFonts.ui,
                fontSize: 15,
                letterSpacing: 0,
                fontWeight: 700,
                boxShadow: 'inset 0 0 0 1px rgba(255,255,255,0.08)',
              }}
            >
              <span
                style={{
                  width: 18,
                  height: 18,
                  borderRadius: '50%',
                  background: index === 0 ? mesh.orange : index === 1 ? mesh.blue : mesh.gold,
                  boxShadow: `0 0 18px ${index === 0 ? mesh.orange : index === 1 ? mesh.blue : mesh.gold}`,
                }}
              />
              {chip}
            </div>
          ))}
        </div>

        <div style={{height: 58}} />

        {isSourceLogicCover ? (
          <SourceArchitectureChoiceGrid />
        ) : visuals?.length ? (
          <GenericCoverProofGrid visuals={visuals} />
        ) : (
          <DecisionLadder />
        )}

        <div
          style={{
            marginTop: 'auto',
            fontFamily: meshFonts.ui,
            fontSize: 15,
            color: 'rgba(255,255,255,0.5)',
            letterSpacing: 0,
            lineHeight: 1.25,
            textAlign: 'center',
          }}
        >
          {sceneGraph.cover.sourceMark ?? 'Douyin grid cover / 3:4'}
        </div>
      </div>
    </AbsoluteFill>
  );
};

const gridHeadlineSize = (headline: string) => {
  if (headline.length >= 13) {
    return 78;
  }
  if (headline.length >= 10) {
    return 88;
  }
  return 98;
};

const gridHeadlineLines = (headline: string) => {
  const normalized = headline.replace('?', '？');

  if (normalized.includes('混合架构')) {
    return ['什么时候用', '混合架构？'];
  }
  if (normalized.includes('Workflow')) {
    return ['Workflow到底', '是什么？'];
  }
  if (normalized.includes('上线前')) {
    return ['Agent上线前看', '什么？'];
  }
  if (normalized.includes('从小做起')) {
    return ['Agent从小做起'];
  }
  if (normalized.includes('多智能体')) {
    return ['多智能体一定更', '好么？'];
  }
  if (normalized.includes('Agent架构')) {
    return ['Agent架构怎么', '选？'];
  }

  return [normalized];
};

const HeadlineText = ({text}: {text: string}) => {
  if (text === '别把 Multi-Agent 当升级版') {
    return (
      <>
        别把
        <br />
        <span
          style={{
            color: theme.cyan,
            textShadow: `0 0 30px ${theme.cyan}55`,
            whiteSpace: 'nowrap',
          }}
        >
          Multi-Agent
        </span>
        <br />
        当升级版
      </>
    );
  }

  if (!text.includes('Multi-Agent')) {
    return <>{text}</>;
  }

  const [before, after] = text.split('Multi-Agent');

  return (
    <>
      {before}
      <span
        style={{
          color: theme.cyan,
          textShadow: `0 0 30px ${theme.cyan}55`,
          whiteSpace: 'nowrap',
        }}
      >
        Multi-Agent
      </span>
      {after}
    </>
  );
};

const sourceArchitectureCards = [
  {
    title: 'Single Agent',
    label: '架构层',
    image: 'building-effective-ai-agents-ep01-architecture-choice/diagrams/p12-single-agent-architecture.png',
  },
  {
    title: 'Multi-Agent',
    label: '协调模式',
    image: 'building-effective-ai-agents-ep01-architecture-choice/diagrams/p16-multi-agent-hierarchical-workflow.png',
  },
  {
    title: 'Workflows',
    label: '工作流结构',
    image: 'building-effective-ai-agents-ep01-architecture-choice/diagrams/p19-multi-agent-sequential-workflow.png',
  },
];

const SourceArchitectureChoice = () => {
  return (
    <div
      style={{
        width: 864,
        height: 724,
        position: 'relative',
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 14,
          top: 20,
          height: 76,
          borderTop: `3px solid ${theme.cyan}`,
          borderBottom: `1px solid rgba(97,216,255,0.24)`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '0 22px',
          background: 'linear-gradient(90deg, rgba(8,12,16,0.94), rgba(8,12,16,0.48))',
          boxShadow: `0 0 54px ${theme.cyan}16`,
        }}
      >
        <div
          style={{
            fontFamily: fonts.mono,
            color: theme.cyan,
            fontSize: 18,
            letterSpacing: 0,
            textTransform: 'uppercase',
            fontWeight: 800,
          }}
        >
          Source diagrams
        </div>
        <div
          style={{
            fontFamily: fonts.mono,
            color: theme.muted,
            fontSize: 16,
            letterSpacing: 0,
            textTransform: 'uppercase',
          }}
        >
          original PDF retained
        </div>
      </div>
      <div
        style={{
          position: 'absolute',
          left: 8,
          top: 124,
          width: 798,
          height: 468,
          borderRadius: 20,
          border: `1px solid rgba(97,216,255,0.22)`,
          background: 'rgba(5, 9, 12, 0.58)',
          boxShadow: `0 0 110px rgba(97,216,255,0.16)`,
        }}
      />
      <div
        style={{
          position: 'absolute',
          right: 4,
          bottom: 54,
          width: 384,
          height: 88,
          borderRadius: 14,
          border: `1px solid ${theme.amber}`,
          background: 'rgba(44,31,16,0.96)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: theme.amber,
          fontFamily: fonts.sans,
          fontSize: 32,
          fontWeight: 900,
          boxShadow: `0 0 38px ${theme.amber}24`,
        }}
      >
        不是越复杂越高级
      </div>
      <div
        style={{
          position: 'absolute',
          left: 48,
          top: 154,
          right: 34,
          bottom: 152,
          display: 'grid',
          gridTemplateColumns: '1fr 1fr 1fr',
          gap: 16,
        }}
      >
        {sourceArchitectureCards.map((card, index) => (
          <div
            key={card.title}
            style={{
              position: 'relative',
              borderRadius: 16,
              border: `1px solid ${index === 1 ? theme.amber : theme.cyan}`,
              background: '#f5f1e8',
              overflow: 'hidden',
              transform: `translateY(${index === 1 ? -24 : index === 2 ? 20 : 0}px) rotate(${index === 0 ? -2 : index === 2 ? 2 : 0}deg)`,
              boxShadow: index === 1 ? `0 0 34px ${theme.amber}32` : `0 0 28px ${theme.cyan}22`,
            }}
          >
            <div
              style={{
                position: 'absolute',
                top: 12,
                left: 12,
                zIndex: 2,
                borderRadius: 999,
                background: index === 1 ? theme.amber : theme.cyan,
                color: '#071014',
                fontFamily: fonts.mono,
                fontSize: 15,
                letterSpacing: 0,
                textTransform: 'uppercase',
                padding: '7px 11px',
                fontWeight: 900,
              }}
            >
              {card.label}
            </div>
            <div
              style={{
                position: 'absolute',
                inset: '52px 12px 86px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              <Img
                src={staticFile(card.image)}
                style={{
                  maxWidth: '100%',
                  maxHeight: '100%',
                  objectFit: 'contain',
                }}
              />
            </div>
            <div
              style={{
                position: 'absolute',
                left: 0,
                right: 0,
                bottom: 0,
                height: 82,
                background: 'rgba(9,14,18,0.95)',
                borderTop: `1px solid ${theme.line}`,
                padding: '13px 16px',
              }}
            >
              <div
                style={{
                  fontFamily: fonts.sans,
                  fontSize: 28,
                  lineHeight: 1.1,
                  fontWeight: 900,
                  color: theme.text,
                }}
              >
                {card.title}
              </div>
              <div
                style={{
                  marginTop: 7,
                  fontFamily: fonts.mono,
                  fontSize: 12,
                  letterSpacing: 0,
                  color: theme.muted,
                  textTransform: 'uppercase',
                }}
              >
                PDF visual anchor
              </div>
            </div>
          </div>
        ))}
      </div>
      <div
        style={{
          position: 'absolute',
          left: 50,
          bottom: 62,
          width: 364,
          height: 62,
          borderRadius: 14,
          background: 'rgba(17,24,32,0.92)',
          border: `1px solid ${theme.line}`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: theme.text,
          fontFamily: fonts.sans,
          fontSize: 27,
          fontWeight: 900,
        }}
      >
        先选最小可用架构
      </div>
    </div>
  );
};

const SourceArchitectureChoiceVertical = () => {
  return (
    <div
      style={{
        width: 940,
        height: 620,
        position: 'relative',
        margin: '0 auto',
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: 4,
          right: 4,
          top: 0,
          height: 70,
          borderTop: `3px solid ${theme.cyan}`,
          borderBottom: `1px solid rgba(97,216,255,0.22)`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '0 22px',
          background: 'linear-gradient(90deg, rgba(8,12,16,0.95), rgba(8,12,16,0.5))',
          boxShadow: `0 0 54px ${theme.cyan}16`,
        }}
      >
        <div
          style={{
            fontFamily: fonts.mono,
            color: theme.cyan,
            fontSize: 20,
            letterSpacing: 0,
            textTransform: 'uppercase',
            fontWeight: 800,
          }}
        >
          Source diagrams
        </div>
        <div
          style={{
            fontFamily: fonts.mono,
            color: theme.muted,
            fontSize: 17,
            letterSpacing: 0,
            textTransform: 'uppercase',
          }}
        >
          original PDF retained
        </div>
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          top: 96,
          width: 940,
          height: 394,
          borderRadius: 22,
          border: `1px solid rgba(97,216,255,0.22)`,
          background: 'rgba(5, 9, 12, 0.64)',
          boxShadow: `0 0 110px rgba(97,216,255,0.16)`,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 34,
          top: 124,
          right: 34,
          height: 314,
          display: 'grid',
          gridTemplateColumns: '1fr 1fr 1fr',
          gap: 16,
        }}
      >
        {sourceArchitectureCards.map((card, index) => (
          <div
            key={card.title}
            style={{
              position: 'relative',
              borderRadius: 16,
              border: `1px solid ${index === 1 ? theme.amber : theme.cyan}`,
              background: '#f5f1e8',
              overflow: 'hidden',
              transform: `translateY(${index === 1 ? -20 : index === 2 ? 16 : 0}px) rotate(${index === 0 ? -2 : index === 2 ? 2 : 0}deg)`,
              boxShadow: index === 1 ? `0 0 34px ${theme.amber}32` : `0 0 28px ${theme.cyan}22`,
            }}
          >
            <div
              style={{
                position: 'absolute',
                top: 10,
                left: 10,
                zIndex: 2,
                borderRadius: 999,
                background: index === 1 ? theme.amber : theme.cyan,
                color: '#071014',
                fontFamily: fonts.mono,
                fontSize: 16,
                letterSpacing: 0,
                textTransform: 'uppercase',
                padding: '8px 12px',
                fontWeight: 900,
              }}
            >
              {card.label}
            </div>
            <div
              style={{
                position: 'absolute',
                inset: '54px 12px 80px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              <Img
                src={staticFile(card.image)}
                style={{
                  maxWidth: '100%',
                  maxHeight: '100%',
                  objectFit: 'contain',
                }}
              />
            </div>
            <div
              style={{
                position: 'absolute',
                left: 0,
                right: 0,
                bottom: 0,
                height: 78,
                background: 'rgba(9,14,18,0.96)',
                borderTop: `1px solid ${theme.line}`,
                padding: '12px 14px',
              }}
            >
              <div
                style={{
                  fontFamily: fonts.sans,
                  fontSize: 27,
                  lineHeight: 1.05,
                  fontWeight: 900,
                  color: theme.text,
                }}
              >
                {card.title}
              </div>
              <div
                style={{
                  marginTop: 7,
                  fontFamily: fonts.mono,
                  fontSize: 12,
                  letterSpacing: 0,
                  color: theme.muted,
                  textTransform: 'uppercase',
                }}
              >
                PDF visual anchor
              </div>
            </div>
          </div>
        ))}
      </div>
      <div
        style={{
          position: 'absolute',
          left: 68,
          bottom: 42,
          width: 386,
          height: 64,
          borderRadius: 14,
          background: 'rgba(17,24,32,0.94)',
          border: `1px solid ${theme.line}`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: theme.text,
          fontFamily: fonts.sans,
          fontSize: 28,
          fontWeight: 900,
        }}
      >
        先选最小可用架构
      </div>
      <div
        style={{
          position: 'absolute',
          right: 42,
          bottom: 34,
          width: 410,
          height: 82,
          borderRadius: 14,
          border: `1px solid ${theme.amber}`,
          background: 'rgba(44,31,16,0.96)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: theme.amber,
          fontFamily: fonts.sans,
          fontSize: 30,
          fontWeight: 900,
          boxShadow: `0 0 38px ${theme.amber}24`,
        }}
      >
        不是越复杂越高级
      </div>
    </div>
  );
};

const SourceArchitectureChoiceGrid = () => {
  return <MeshProofGrid items={sourceArchitectureCards} label="Source diagrams" />;
};

const MeshProofGrid = ({
  items,
  label,
}: {
  items: Array<{title: string; label: string; image: string}>;
  label: string;
}) => {
  return (
    <div
      style={{
        width: 940,
        height: 360,
        position: 'relative',
        margin: '0 auto',
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: 0,
          top: 0,
          color: mesh.muted,
          fontFamily: meshFonts.ui,
          fontSize: 15,
          fontWeight: 800,
          letterSpacing: 1.2,
          textTransform: 'uppercase',
        }}
      >
        {label}
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 42,
          height: 230,
          display: 'grid',
          gridTemplateColumns: `repeat(${Math.max(1, items.length)}, 1fr)`,
          gap: 18,
        }}
      >
        {items.map((card, index) => (
          <GridProofCard key={card.title} item={card} index={index} />
        ))}
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 8,
          height: 1,
          background: 'linear-gradient(90deg, rgba(50,197,255,0.72), rgba(255,255,255,0.05))',
          boxShadow: `0 0 20px ${mesh.blue}55`,
        }}
      />
    </div>
  );
};

const GenericCoverProof = ({
  visuals,
}: {
  visuals: NonNullable<SceneGraph['cover']['visuals']>;
}) => {
  const items = visuals.slice(0, 3);

  return (
    <div
      style={{
        width: 864,
        height: 724,
        position: 'relative',
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 14,
          top: 20,
          height: 76,
          borderTop: `3px solid ${theme.cyan}`,
          borderBottom: `1px solid rgba(97,216,255,0.24)`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '0 22px',
          background: 'linear-gradient(90deg, rgba(8,12,16,0.94), rgba(8,12,16,0.48))',
          boxShadow: `0 0 54px ${theme.cyan}16`,
        }}
      >
        <div style={{fontFamily: fonts.mono, color: theme.cyan, fontSize: 18, fontWeight: 800}}>
          Source proof
        </div>
        <div style={{fontFamily: fonts.mono, color: theme.muted, fontSize: 16}}>
          original PDF retained
        </div>
      </div>
      <div
        style={{
          position: 'absolute',
          left: 8,
          top: 124,
          width: 798,
          height: 468,
          borderRadius: 20,
          border: `1px solid rgba(97,216,255,0.22)`,
          background: 'rgba(5, 9, 12, 0.58)',
          boxShadow: `0 0 110px rgba(97,216,255,0.16)`,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 48,
          top: 154,
          right: 34,
          bottom: 112,
          display: 'grid',
          gridTemplateColumns: `repeat(${Math.max(1, items.length)}, 1fr)`,
          gap: 16,
        }}
      >
        {items.map((item, index) => (
          <CoverProofCard key={item.title} item={item} index={index} />
        ))}
      </div>
    </div>
  );
};

const GenericCoverProofVertical = ({
  visuals,
}: {
  visuals: NonNullable<SceneGraph['cover']['visuals']>;
}) => {
  const items = visuals.slice(0, 3);

  return (
    <div
      style={{
        width: 940,
        height: 620,
        position: 'relative',
        margin: '0 auto',
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: 4,
          right: 4,
          top: 0,
          height: 70,
          borderTop: `3px solid ${theme.cyan}`,
          borderBottom: `1px solid rgba(97,216,255,0.22)`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '0 22px',
          background: 'linear-gradient(90deg, rgba(8,12,16,0.95), rgba(8,12,16,0.5))',
          boxShadow: `0 0 54px ${theme.cyan}16`,
        }}
      >
        <div style={{fontFamily: fonts.mono, color: theme.cyan, fontSize: 20, fontWeight: 800}}>
          Source proof
        </div>
        <div style={{fontFamily: fonts.mono, color: theme.muted, fontSize: 17}}>
          original PDF retained
        </div>
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          top: 96,
          width: 940,
          height: 394,
          borderRadius: 22,
          border: `1px solid rgba(97,216,255,0.22)`,
          background: 'rgba(5, 9, 12, 0.64)',
          boxShadow: `0 0 110px rgba(97,216,255,0.16)`,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 34,
          top: 124,
          right: 34,
          height: 314,
          display: 'grid',
          gridTemplateColumns: `repeat(${Math.max(1, items.length)}, 1fr)`,
          gap: 16,
        }}
      >
        {items.map((item, index) => (
          <CoverProofCard key={item.title} item={item} index={index} />
        ))}
      </div>
    </div>
  );
};

const GenericCoverProofGrid = ({
  visuals,
}: {
  visuals: NonNullable<SceneGraph['cover']['visuals']>;
}) => {
  const items = visuals.slice(0, 3);
  return <MeshProofGrid items={items} label="Source proof" />;
};

const GridProofCard = ({
  item,
  index,
}: {
  item: NonNullable<SceneGraph['cover']['visuals']>[number];
  index: number;
}) => {
  return (
    <div
      style={{
        position: 'relative',
        borderRadius: 22,
        border: '1px solid rgba(255,255,255,0.76)',
        background: mesh.paper,
        overflow: 'hidden',
        transform: `translateY(${index === 1 ? -14 : index === 2 ? 12 : 0}px) rotate(${index === 0 ? -2.4 : index === 2 ? 2.4 : 0}deg)`,
        boxShadow: '0 24px 58px rgba(0,0,0,0.34), inset 0 -10px 24px rgba(255,255,255,0.42)',
      }}
    >
      <div
        style={{
          position: 'absolute',
          top: 12,
          left: 12,
          zIndex: 2,
          borderRadius: 999,
          background: mesh.ink,
          color: mesh.cream,
          fontFamily: meshFonts.cn,
          fontSize: 14,
          padding: '7px 10px',
          fontWeight: 900,
        }}
      >
        {item.label}
      </div>
      <div
        style={{
          position: 'absolute',
          inset: '46px 12px 48px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Img
          src={staticFile(item.image)}
          style={{
            maxWidth: '100%',
            maxHeight: '100%',
            objectFit: 'contain',
          }}
        />
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 0,
          height: 46,
          background: 'transparent',
          padding: '8px 12px',
        }}
      >
        <div
          style={{
            fontFamily: meshFonts.ui,
            fontSize: 18,
            lineHeight: 1.05,
            fontWeight: 900,
            color: 'rgba(29,29,31,0.78)',
            whiteSpace: 'nowrap',
            overflow: 'hidden',
            textOverflow: 'ellipsis',
          }}
        >
          {item.title}
        </div>
      </div>
    </div>
  );
};

const CoverProofCard = ({
  item,
  index,
}: {
  item: NonNullable<SceneGraph['cover']['visuals']>[number];
  index: number;
}) => {
  const tone = index === 1 ? theme.amber : theme.cyan;

  return (
    <div
      style={{
        position: 'relative',
        borderRadius: 16,
        border: `1px solid ${tone}`,
        background: '#f5f1e8',
        overflow: 'hidden',
        transform: `translateY(${index === 1 ? -20 : index === 2 ? 16 : 0}px) rotate(${index === 0 ? -2 : index === 2 ? 2 : 0}deg)`,
        boxShadow: index === 1 ? `0 0 34px ${theme.amber}32` : `0 0 28px ${theme.cyan}22`,
      }}
    >
      <div
        style={{
          position: 'absolute',
          top: 10,
          left: 10,
          zIndex: 2,
          borderRadius: 999,
          background: tone,
          color: '#071014',
          fontFamily: fonts.mono,
          fontSize: 16,
          padding: '8px 12px',
          fontWeight: 900,
        }}
      >
        {item.label}
      </div>
      <div
        style={{
          position: 'absolute',
          inset: '54px 12px 80px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Img
          src={staticFile(item.image)}
          style={{
            maxWidth: '100%',
            maxHeight: '100%',
            objectFit: 'contain',
          }}
        />
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 0,
          height: 78,
          background: 'rgba(9,14,18,0.96)',
          borderTop: `1px solid ${theme.line}`,
          padding: '12px 14px',
        }}
      >
        <div
          style={{
            fontFamily: fonts.sans,
            fontSize: 27,
            lineHeight: 1.05,
            fontWeight: 900,
            color: theme.text,
          }}
        >
          {item.title}
        </div>
        <div
          style={{
            marginTop: 7,
            fontFamily: fonts.mono,
            fontSize: 12,
            color: theme.muted,
            textTransform: 'uppercase',
          }}
        >
          PDF visual anchor
        </div>
      </div>
    </div>
  );
};

const DecisionLadder = () => {
  const nodes = ['Workflow', 'Single Agent', 'Multi-Agent', 'Production Controls'];
  const spineLeft = 74;

  return (
    <div
      style={{
        width: 820,
        height: 560,
        borderRadius: 38,
        border: `1px solid ${theme.line}`,
        background: 'rgba(9, 14, 18, 0.72)',
        position: 'relative',
        padding: 58,
        boxShadow: `0 0 110px rgba(97,216,255,0.12)`,
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: spineLeft,
          top: 116,
          bottom: 118,
          width: 3,
          background: theme.cyan,
          boxShadow: `0 0 28px ${theme.cyan}`,
        }}
      />
      {nodes.map((node, index) => {
        const left = 132 + index * 42;
        const top = 82 + index * 96;
        const tone = index === nodes.length - 1 ? theme.amber : theme.cyan;

        return (
          <div key={node}>
            <div
              style={{
                position: 'absolute',
                left: spineLeft + 3,
                top: top + 39,
                width: left - spineLeft - 21,
                height: 2,
                background: tone,
                boxShadow: `0 0 18px ${tone}`,
              }}
            />
            <div
              style={{
                position: 'absolute',
                left,
                top,
                width: 540,
                height: 78,
                borderRadius: 24,
                border: `1px solid ${tone}`,
                background:
                  index === nodes.length - 1
                    ? 'rgba(44,31,16,0.98)'
                    : 'rgba(15,34,43,0.98)',
                color: theme.text,
                fontFamily: fonts.sans,
                fontSize: 36,
                fontWeight: 900,
                display: 'flex',
                alignItems: 'center',
                paddingLeft: 38,
                boxShadow:
                  index === nodes.length - 1
                    ? `0 0 28px ${theme.amber}33`
                    : `0 0 24px ${theme.cyan}22`,
              }}
            >
              {node}
            </div>
          </div>
        );
      })}
      <div
        style={{
          position: 'absolute',
          right: 42,
          bottom: 34,
          fontFamily: fonts.mono,
          color: theme.muted,
          fontSize: 18,
          letterSpacing: 0,
          textTransform: 'uppercase',
        }}
      >
        smallest sufficient architecture
      </div>
    </div>
  );
};
