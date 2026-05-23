export type SceneArtifact = {
  type: string;
  nodes: string[];
  groups?: Array<{
    title: string;
    items: string[];
  }>;
  imagePath?: string;
  imagePaths?: string[];
  caption?: string;
  fallback?: 'generated';
};

export type Scene = {
  id: string;
  durationSeconds: number;
  paragraphLabel?: string;
  sectionLabel?: string;
  claim: string;
  narration: string;
  subtitle: string;
  audioFile?: string;
  artifact: SceneArtifact;
  focus: string;
  sources: string[];
  sourceDiagramRefs?: string[];
};

export type SourceDiagram = {
  id: string;
  sourceRef: string;
  path: string;
  useInEpisodes: string[];
  preservation: string;
};

export type SceneGraph = {
  schemaVersion: string;
  slug: string;
  title: string;
  mission: string;
  audience: string;
  format: {
    aspectRatio: string;
    width: number;
    height: number;
    fps: number;
  };
  visualSystem: {
    name: string;
    background: string;
    typography: string;
    palette: Record<string, string>;
    motionPrinciples: string[];
  };
  cover: {
    headline: string;
    subhead: string;
    artifact: string;
    badge: string;
    proofChips?: string[];
    visuals?: Array<{
      title: string;
      label: string;
      image: string;
    }>;
    sourceMark?: string;
    sourceVisualRule?: string;
  };
  sourceDiagrams?: SourceDiagram[];
  scenes: Scene[];
};
