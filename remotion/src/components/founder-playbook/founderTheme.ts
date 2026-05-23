export const founderTheme = {
  colors: {
    page: '#050708',
    field: '#080b0c',
    ink: '#fff8ea',
    soft: '#d8c7b0',
    muted: '#9ca6a8',
    dim: 'rgba(255, 248, 234, 0.42)',
    line: 'rgba(255, 248, 234, 0.16)',
    panel: 'rgba(255, 248, 234, 0.07)',
    orange: '#ff7a38',
    amber: '#ffc21a',
    cyan: '#32c8e8',
    rose: '#f16b84',
  },
  fonts: {
    cn: '"Resource Han Rounded CN", "GenSenRounded2 TW", "GenSenRounded TW", "GenJyuuGothic", "Source Han Sans SC", "Noto Sans CJK SC", "Noto Sans SC", "Sarasa UI SC", "PingFang SC", "Microsoft YaHei", sans-serif',
    ui: '"Avenir Next", Inter, "Helvetica Neue", Arial, "PingFang SC", sans-serif',
    mono: '"SF Mono", "JetBrains Mono", Menlo, monospace',
  },
  layout: {
    width: 1080,
    height: 1920,
    padX: 86,
    padTop: 96,
    padBottom: 86,
  },
} as const;

export type FounderSymbolKind =
  | 'bottleneck'
  | 'path'
  | 'lanes'
  | 'gate'
  | 'control'
  | 'lifecycle'
  | 'layer'
  | 'node'
  | 'binary'
  | 'demo'
  | 'signal'
  | 'threshold'
  | 'void'
  | 'mismatch'
  | 'question'
  | 'boundary';

export const symbolForArtifact = (type: string): FounderSymbolKind => {
  if (type.includes('bottleneck')) return 'bottleneck';
  if (type.includes('router')) return 'bottleneck';
  if (type.includes('audit')) return 'lanes';
  if (type.includes('launch')) return 'gate';
  if (type.includes('lane') || type.includes('accelerator')) return 'lanes';
  if (type.includes('false')) return 'void';
  if (type.includes('signal') || type.includes('pain') || type.includes('praise')) return 'signal';
  if (type.includes('solution-fit')) return 'mismatch';
  if (type.includes('enough-signal')) return 'threshold';
  if (type.includes('question')) return 'question';
  if (type.includes('boundary')) return 'boundary';
  if (type.includes('gate') || type.includes('sequence')) return 'gate';
  if (type.includes('steering') || type.includes('control')) return 'control';
  if (type.includes('lifecycle') || type.includes('stage') || type.includes('later')) return 'lifecycle';
  if (type.includes('removed') || type.includes('execution-not')) return 'layer';
  if (type.includes('founder-decision')) return 'node';
  if (type.includes('decision-card') || type.includes('go-stop')) return 'binary';
  if (type.includes('next-episode')) return 'demo';
  return 'path';
};

export const toneForArtifact = (type: string) => {
  if (type.includes('wrong') || type.includes('demo')) return founderTheme.colors.rose;
  if (type.includes('lifecycle') || type.includes('idea') || type.includes('gate')) {
    return founderTheme.colors.amber;
  }
  if (type.includes('execution') || type.includes('lane')) return founderTheme.colors.cyan;
  return founderTheme.colors.orange;
};
