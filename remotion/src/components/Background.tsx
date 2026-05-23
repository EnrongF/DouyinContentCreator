import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {theme} from '../styles/theme';

export const Background = () => {
  const frame = useCurrentFrame();
  const drift = interpolate(frame % 240, [0, 240], [0, 1]);

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(circle at ${24 + drift * 22}% 20%, rgba(97, 216, 255, 0.18), transparent 34%), linear-gradient(135deg, ${theme.graphite}, #07090b 68%, #0d1418)`,
      }}
    >
      <AbsoluteFill
        style={{
          opacity: 0.14,
          backgroundImage:
            'linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px)',
          backgroundSize: '64px 64px',
          maskImage:
            'linear-gradient(90deg, transparent, black 16%, black 84%, transparent)',
        }}
      />
      <AbsoluteFill
        style={{
          opacity: 0.08,
          backgroundImage:
            'radial-gradient(circle, rgba(255,255,255,0.75) 0.7px, transparent 0.8px)',
          backgroundSize: '7px 7px',
        }}
      />
    </AbsoluteFill>
  );
};

