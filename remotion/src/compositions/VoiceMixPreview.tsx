import {AbsoluteFill, Audio, staticFile} from 'remotion';
import {fonts, theme} from '../styles/theme';

export const VoiceMixPreview = () => {
  return (
    <AbsoluteFill
      style={{
        background: theme.graphite,
        color: theme.text,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: fonts.sans,
      }}
    >
      <div
        style={{
          border: `1px solid ${theme.line}`,
          borderRadius: 16,
          padding: '28px 34px',
          background: 'rgba(17,24,32,0.82)',
          boxShadow: '0 24px 90px rgba(0,0,0,0.36)',
          maxWidth: 780,
        }}
      >
        <div
          style={{
            fontFamily: fonts.mono,
            fontSize: 18,
            color: theme.cyan,
            letterSpacing: 0,
            marginBottom: 16,
          }}
        >
          EP06 / Voice Mix Preview
        </div>
        <div style={{fontSize: 42, fontWeight: 900, lineHeight: 1.18}}>
          Opening voice with subtle background bed
        </div>
        <div style={{fontSize: 24, color: theme.muted, marginTop: 18, lineHeight: 1.45}}>
          Voice remains primary. Background is low, slow, and ducked by design.
        </div>
      </div>
      <Audio src={staticFile('voice-tests/ep06-opening-retention-marin.mp3')} volume={1} />
      <Audio src={staticFile('voice-tests/ep06-subtle-background-bed.wav')} volume={0.13} />
    </AbsoluteFill>
  );
};
