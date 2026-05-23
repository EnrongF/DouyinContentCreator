export type FounderArtifact = {
  type: string;
  state?: string;
  nodes: string[];
  highlight?: string;
  keyMessage?: string;
  symbolMeaning?: string;
};

export type FounderScene = {
  id: string;
  startSeconds?: number;
  durationSeconds: number;
  speechEndSeconds?: number;
  sectionLabel?: string;
  paragraphId?: string;
  claim: string;
  narration: string;
  subtitle: string;
  artifact: FounderArtifact;
  focusPhrase?: string;
  focusCue?: string;
  motion?: string;
  sources: string[];
  sourceLogic?: string;
  audioSource?: string;
};

export type FounderSoundEffect = {
  id: string;
  file: string;
  sceneId: string;
  atSeconds: number;
  durationSeconds?: number;
  volume?: number;
  concept: string;
  rationale: string;
};

export type FounderSceneGraph = {
  schemaVersion: string;
  slug: string;
  title: string;
  series: string;
  episode: number;
  status: string;
  mission: string;
  audience: string;
  format: {
    primary: string;
    width: number;
    height: number;
    fps: number;
    coverGrid?: {
      width: number;
      height: number;
      note?: string;
    };
  };
  timing: {
    totalDurationSeconds: number;
    totalMeasuredSpeechSeconds: number;
    audioStrategy: string;
  };
  visualSystem: unknown;
  soundEffects?: FounderSoundEffect[];
  scenes: FounderScene[];
};
