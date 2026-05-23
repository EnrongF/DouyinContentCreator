import type {FounderSymbolKind} from './founderTheme';
import {founderTheme} from './founderTheme';

type FounderSymbolProps = {
  kind: FounderSymbolKind;
  size?: number;
};

export const FounderSymbol = ({kind, size = 34}: FounderSymbolProps) => {
  const c = founderTheme.colors;
  const stroke = c.cyan;
  const accent = kind === 'path' || kind === 'demo' || kind === 'void' || kind === 'mismatch' ? c.rose : c.amber;

  return (
    <svg width={size} height={size} viewBox="0 0 36 36" aria-hidden="true">
      <rect
        x="1"
        y="1"
        width="34"
        height="34"
        rx="8"
        fill="rgba(255,248,234,0.07)"
        stroke="rgba(255,248,234,0.18)"
      />
      {kind === 'bottleneck' ? (
        <>
          <path d="M8 18H28" stroke={stroke} strokeWidth="3" strokeLinecap="round" />
          <path d="M18 9V27" stroke={accent} strokeWidth="5" strokeLinecap="round" />
        </>
      ) : null}
      {kind === 'path' ? (
        <>
          <path d="M7 24C14 14 20 22 28 9" stroke={accent} strokeWidth="4" fill="none" strokeLinecap="round" />
          <circle cx="28" cy="9" r="4" fill={c.rose} />
        </>
      ) : null}
      {kind === 'lanes' ? (
        <>
          <path d="M8 11H24M8 18H24M8 25H24" stroke={stroke} strokeWidth="3" strokeLinecap="round" />
          <path d="M27 9V27" stroke={accent} strokeWidth="5" strokeLinecap="round" />
        </>
      ) : null}
      {kind === 'gate' ? (
        <>
          <rect x="9" y="8" width="18" height="20" rx="4" fill="none" stroke={stroke} strokeWidth="3" />
          <path d="M10 18H26" stroke={accent} strokeWidth="3" strokeLinecap="round" />
        </>
      ) : null}
      {kind === 'control' ? (
        <>
          <circle cx="15" cy="15" r="8" fill="none" stroke="rgba(255,248,234,0.2)" strokeWidth="4" />
          <path d="M15 7A8 8 0 0 1 23 15" stroke={c.orange} strokeWidth="4" fill="none" strokeLinecap="round" />
          <circle cx="24" cy="24" r="6" fill="none" stroke={stroke} strokeWidth="3" />
        </>
      ) : null}
      {kind === 'lifecycle' ? (
        <>
          <path d="M8 18H28" stroke="rgba(255,248,234,0.28)" strokeWidth="2" />
          <circle cx="8" cy="18" r="4" fill={c.amber} />
          <circle cx="18" cy="18" r="4" fill={c.cyan} />
          <circle cx="28" cy="18" r="4" fill="rgba(255,248,234,0.42)" />
        </>
      ) : null}
      {kind === 'layer' ? (
        <>
          <rect x="9" y="9" width="18" height="5" rx="2.5" fill="rgba(255,248,234,0.28)" />
          <rect x="9" y="16" width="18" height="5" rx="2.5" fill={c.amber} opacity="0.75" />
          <rect x="9" y="23" width="18" height="5" rx="2.5" fill={c.cyan} opacity="0.5" />
        </>
      ) : null}
      {kind === 'node' ? (
        <>
          <circle cx="18" cy="18" r="11" fill="none" stroke={stroke} strokeWidth="2" opacity="0.7" />
          <circle cx="18" cy="18" r="6" fill={accent} />
        </>
      ) : null}
      {kind === 'binary' ? (
        <>
          <rect x="8" y="10" width="8" height="16" rx="4" fill="rgba(255,248,234,0.16)" />
          <rect x="19" y="10" width="10" height="16" rx="4" fill={c.amber} />
        </>
      ) : null}
      {kind === 'demo' ? (
        <>
          <rect x="8" y="13" width="9" height="9" rx="3" fill="rgba(255,248,234,0.18)" />
          <path d="M18 18H26" stroke={stroke} strokeWidth="3" strokeLinecap="round" />
          <rect x="24" y="10" width="7" height="16" rx="3" fill="none" stroke={c.rose} strokeWidth="3" />
        </>
      ) : null}
      {kind === 'signal' ? (
        <>
          <circle cx="10" cy="25" r="3" fill={c.rose} opacity="0.65" />
          <circle cx="18" cy="18" r="4" fill={c.amber} opacity="0.82" />
          <circle cx="27" cy="10" r="5" fill={c.cyan} />
          <path d="M10 25L18 18L27 10" stroke={stroke} strokeWidth="2" strokeLinecap="round" opacity="0.72" />
        </>
      ) : null}
      {kind === 'threshold' ? (
        <>
          <path d="M8 24H28" stroke="rgba(255,248,234,0.28)" strokeWidth="3" strokeLinecap="round" />
          <path d="M8 24C13 23 15 17 19 17C23 17 24 12 28 11" stroke={c.cyan} strokeWidth="4" fill="none" strokeLinecap="round" />
          <path d="M21 8V28" stroke={c.amber} strokeWidth="3" strokeLinecap="round" />
        </>
      ) : null}
      {kind === 'void' ? (
        <>
          <circle cx="18" cy="18" r="10" fill="none" stroke={c.rose} strokeWidth="3" strokeDasharray="4 4" />
          <circle cx="18" cy="18" r="3" fill="rgba(255,248,234,0.18)" />
        </>
      ) : null}
      {kind === 'mismatch' ? (
        <>
          <path d="M8 12H18C24 12 24 24 30 24" stroke={c.rose} strokeWidth="3" fill="none" strokeLinecap="round" />
          <path d="M8 24H17C22 24 23 14 29 12" stroke={c.cyan} strokeWidth="3" fill="none" strokeLinecap="round" />
          <circle cx="18" cy="18" r="3" fill={c.amber} />
        </>
      ) : null}
      {kind === 'question' ? (
        <>
          <path d="M8 21C12 10 22 11 18 19C16 23 24 21 28 13" stroke={c.cyan} strokeWidth="3" fill="none" strokeLinecap="round" />
          <circle cx="10" cy="24" r="3" fill={c.amber} />
          <circle cx="28" cy="13" r="3" fill={c.cyan} />
        </>
      ) : null}
      {kind === 'boundary' ? (
        <>
          <rect x="9" y="9" width="18" height="18" rx="3" fill="none" stroke={c.amber} strokeWidth="3" />
          <path d="M14 9V27M22 9V27" stroke="rgba(255,248,234,0.24)" strokeWidth="2" />
          <path d="M9 18H27" stroke={c.cyan} strokeWidth="3" strokeLinecap="round" />
        </>
      ) : null}
    </svg>
  );
};
