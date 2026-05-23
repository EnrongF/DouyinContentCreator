import {interpolate, useCurrentFrame} from 'remotion';
import {FounderArtifact} from './FounderArtifacts';
import {founderTheme, symbolForArtifact} from './founderTheme';
import {FounderSymbol} from './FounderSymbols';
import type {FounderScene, FounderSceneGraph} from './types';

type FounderFrameProps = {
  sceneGraph: FounderSceneGraph;
  scene: FounderScene;
  sceneIndex: number;
  totalScenes: number;
  progress: number;
  isContinuingContext?: boolean;
  willContinueContext?: boolean;
};

const c = founderTheme.colors;
const fonts = founderTheme.fonts;

const chipsForScene = (scene: FounderScene) => {
  const type = scene.artifact.type;
  if (type.includes('demo')) return ['Prototype', 'Void', 'Signal'];
  if (type.includes('validation')) return ['Reality', 'Fit', 'Threshold'];
  if (type.includes('question')) return ['Vector', 'Behavior', 'Evidence'];
  if (type.includes('praise') || type.includes('pain')) return ['Surface', 'Signal', 'Threshold'];
  if (type.includes('code-speed') || type.includes('before-code')) return ['Boundary', 'Context', 'Code'];
  if (type.includes('router')) return ['Requests', 'Founder', 'Bottleneck'];
  if (type.includes('launch')) return ['MVP', 'Launch', 'Repeatable'];
  if (type.includes('model-access')) return ['Model', 'Access', 'Not Moat'];
  if (type.includes('specificity') || type.includes('workflow')) return ['Workflow', 'Context', 'Moat'];
  if (type.includes('copy-gap') || type.includes('switching-cost')) return ['Context', 'Integration', 'Lock-in'];
  if (type.includes('scale-lifecycle')) return ['Idea', 'Launch', 'Scale'];
  if (type.includes('audit')) return ['Automate', 'Delegate', 'Judgment'];
  if (type.includes('sprawl') || type.includes('creep') || type.includes('shape-loss')) return ['Scope', 'Features', 'Drift'];
  if (type.includes('mvp-evidence')) return ['MVP', 'Evidence', 'Gate'];
  if (type.includes('context') || type.includes('technical-debt')) return ['Boundary', 'Context', 'Drift'];
  if (type.includes('boundary')) return ['Signal', 'Boundary', 'Execution'];
  if (type.includes('execution-lane')) return ['Research', 'Code', 'Ops'];
  if (type.includes('removed')) return ['Caveat', 'Execution', 'Still matters'];
  if (type.includes('early')) return ['Execution', 'Evidence', 'Judgment'];
  if (type.includes('steering') || type.includes('accelerator')) return ['AI Speed', 'Founder Direction'];
  if (type.includes('later-gates')) return ['Boundary', 'System', 'Moat'];
  if (type.includes('lifecycle') || type.includes('idea') || type.includes('later')) return ['Idea', 'MVP', 'Launch'];
  if (type.includes('decision') || type.includes('question')) return ['Speed', 'Judgment'];
  if (type.includes('next')) return ['Demo', 'Validation', 'Demand'];
  if (type.includes('bottleneck')) return ['Idea', 'Build', 'Ship'];
  return ['Fast', 'Direction', 'Risk'];
};

const explainerForScene = (scene: FounderScene) => {
  const focus = scene.focusPhrase?.replace(/\s+/g, ' ').trim();
  if (focus) return focus;
  return scene.artifact.highlight ?? scene.focusCue ?? '';
};

const headlineSize = (text: string) => {
  if (text.length > 25) return 50;
  if (text.length > 18) return 55;
  if (text.length > 13) return 58;
  return 68;
};

export const FounderFrame = ({
  sceneGraph,
  scene,
  sceneIndex,
  totalScenes,
  progress,
  isContinuingContext = false,
  willContinueContext = false,
}: FounderFrameProps) => {
  const enter = isContinuingContext
    ? 1
    : interpolate(progress, [0, 0.12], [0, 1], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      });
  const exit = willContinueContext ? 1 : interpolate(progress, [0.9, 1], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const opacity = enter * exit;
  const symbol = symbolForArtifact(scene.artifact.type);
  const chips = chipsForScene(scene);

  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        overflow: 'hidden',
        background: c.page,
        color: c.ink,
        fontFamily: fonts.cn,
      }}
    >
      <BackgroundField />
      <main
        style={{
          position: 'relative',
          zIndex: 2,
          height: '100%',
          display: 'grid',
          gridTemplateRows: '104px 414px 92px minmax(0, 650px) 214px',
          padding: `${founderTheme.layout.padTop}px ${founderTheme.layout.padX}px ${founderTheme.layout.padBottom}px`,
          opacity,
          transform: `translateY(${(1 - enter) * 28}px)`,
        }}
      >
        <header style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 24}}>
          <div style={{display: 'flex', alignItems: 'center', gap: 16}}>
            <div
              style={{
                width: 72,
                height: 72,
                borderRadius: 8,
                display: 'grid',
                placeItems: 'center',
                background: c.amber,
                color: '#101214',
                fontFamily: fonts.ui,
                fontSize: 25,
                fontWeight: 950,
                boxShadow: `0 0 28px ${c.amber}4c`,
              }}
            >
              {`EP${String(sceneGraph.episode).padStart(2, '0')}`}
            </div>
            <div style={{display: 'grid', gap: 8}}>
              <div style={{color: c.muted, fontFamily: fonts.ui, fontSize: 20, fontWeight: 900}}>
                {scene.sectionLabel ?? '判断瓶颈'}
              </div>
              <div style={{color: c.dim, fontFamily: fonts.mono, fontSize: 15, letterSpacing: 0.9}}>
                {scene.id.toUpperCase()} / {sceneGraph.title}
              </div>
            </div>
          </div>
          <div style={{display: 'flex', alignItems: 'center', gap: 12, color: c.muted, fontFamily: fonts.mono, fontSize: 16, fontWeight: 900}}>
            <FounderSymbol kind={symbol} size={42} />
            <span>
              {String(sceneIndex + 1).padStart(2, '0')} / {String(totalScenes).padStart(2, '0')}
            </span>
          </div>
        </header>

        <section style={{alignSelf: 'end'}}>
          <h1
            style={{
              margin: 0,
              maxWidth: 860,
              color: c.ink,
              textShadow: '0 0 24px rgba(255,248,234,0.26), 0 2px 18px rgba(0,0,0,0.42)',
              fontSize: headlineSize(scene.claim),
              lineHeight: 1.08,
              letterSpacing: 0,
              fontWeight: 950,
              textWrap: 'balance',
            }}
          >
            {scene.claim}
          </h1>
          <p
            style={{
              margin: '22px 0 0',
              maxWidth: 790,
              color: c.soft,
              fontSize: 29,
              lineHeight: 1.36,
              fontWeight: 840,
              textShadow: '0 1px 12px rgba(0,0,0,0.36)',
            }}
          >
            {explainerForScene(scene)}
          </p>
        </section>

        <section style={{alignSelf: 'center', display: 'flex', flexWrap: 'wrap', gap: 10}}>
          {chips.map((chip, index) => (
            <Chip key={chip} label={chip} tone={index === 1 ? c.cyan : index === 2 ? c.amber : c.orange} />
          ))}
        </section>

        <section style={{minHeight: 0}}>
          <FounderArtifact scene={scene} progress={progress} isContinuingContext={isContinuingContext} />
        </section>

        <Subtitle text={scene.subtitle} progress={progress} />
      </main>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 28,
          zIndex: 3,
          color: 'rgba(255,248,234,0.46)',
          fontFamily: fonts.ui,
          fontSize: 16,
          textAlign: 'center',
        }}
      >
        Source: The Founder&apos;s Playbook / Building an AI-Native Startup
      </div>
    </div>
  );
};

const BackgroundField = () => {
  const frame = useCurrentFrame();
  const slow = frame / 30;
  const warmX = Math.sin(slow / 9) * 42;
  const warmY = Math.cos(slow / 11) * 24;
  const coolX = Math.cos(slow / 12) * 34;
  const coolY = Math.sin(slow / 10) * 26;
  const warmBreath = 1.04 + Math.sin(slow / 8) * 0.035;
  const coolBreath = 1.02 + Math.cos(slow / 10) * 0.028;
  const arcOpacity = 0.1 + Math.sin(slow / 13) * 0.018;

  return (
    <>
    <div
      style={{
        position: 'absolute',
        inset: 0,
        background:
          'linear-gradient(132deg, rgba(255,194,26,0.32), rgba(255,122,56,0.13) 27%, transparent 47%), linear-gradient(312deg, rgba(50,200,232,0.14), transparent 38%), linear-gradient(180deg, rgba(255,248,234,0.025), transparent 40%, rgba(255,248,234,0.045))',
      }}
    />
    <div
      style={{
        position: 'absolute',
        left: '-18%',
        top: '-10%',
        width: '76%',
        height: '38%',
        borderRadius: '50%',
        background: 'radial-gradient(circle, rgba(255,194,26,0.16), rgba(255,122,56,0.075) 42%, transparent 72%)',
        filter: 'blur(18px)',
        opacity: 0.72,
        transform: `translate3d(${warmX}px, ${warmY}px, 0) scale(${warmBreath})`,
      }}
    />
    <div
      style={{
        position: 'absolute',
        right: '-22%',
        bottom: '10%',
        width: '72%',
        height: '42%',
        borderRadius: '50%',
        background: 'radial-gradient(circle, rgba(50,200,232,0.12), rgba(50,200,232,0.055) 44%, transparent 76%)',
        filter: 'blur(20px)',
        opacity: 0.62,
        transform: `translate3d(${coolX}px, ${coolY}px, 0) scale(${coolBreath})`,
      }}
    />
    <div
      style={{
        position: 'absolute',
        inset: 0,
        background:
          'linear-gradient(175deg, transparent 0 42%, rgba(0,0,0,0.46) 68%, rgba(0,0,0,0.18)), repeating-linear-gradient(0deg, transparent 0 122px, rgba(255,248,234,0.034) 123px, transparent 125px)',
      }}
    />
    <div
      style={{
        position: 'absolute',
        left: '-36%',
        right: '-36%',
        top: '26%',
        height: '58%',
        border: '1px solid rgba(255,248,234,0.12)',
        borderRadius: '50%',
        opacity: arcOpacity,
        transform: 'rotate(-8deg)',
      }}
    />
    </>
  );
};

const Chip = ({label, tone}: {label: string; tone: string}) => (
  <div
    style={{
      display: 'inline-flex',
      alignItems: 'center',
      gap: 9,
      minHeight: 38,
      padding: '8px 16px',
      border: `1px solid rgba(255,248,234,0.26)`,
      borderRadius: 999,
      background: 'rgba(255,248,234,0.085)',
      color: c.ink,
      fontFamily: fonts.ui,
      fontSize: 18,
      fontWeight: 900,
    }}
  >
    <span style={{width: 12, height: 12, borderRadius: 99, background: tone, boxShadow: `0 0 16px ${tone}`}} />
    {label}
  </div>
);

const Subtitle = ({text, progress}: {text: string; progress: number}) => {
  const opacity = interpolate(progress, [0, 0.08, 0.92, 1], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <div
      style={{
        position: 'relative',
        alignSelf: 'end',
        minHeight: 96,
        display: 'flex',
        alignItems: 'center',
        padding: '0 8px 8px 24px',
        color: c.ink,
        fontFamily: fonts.cn,
        fontSize: text.length > 24 ? 34 : 39,
        lineHeight: 1.34,
        fontWeight: 920,
        textAlign: 'left',
        textShadow: '0 2px 16px rgba(0,0,0,0.72), 0 0 18px rgba(255,248,234,0.16)',
        opacity,
      }}
    >
      <span
        style={{
          position: 'absolute',
          left: 0,
          top: 24,
          bottom: 26,
          width: 4,
          borderRadius: 99,
          background: `linear-gradient(180deg, ${c.amber}, ${c.cyan})`,
          boxShadow: `0 0 18px ${c.cyan}40`,
        }}
      />
      {text}
    </div>
  );
};
