import {Composition, Still} from 'remotion';
import rawSceneGraph from '../../scene-graphs/building-effective-ai-agents.json';
import rawEpisode01SceneGraph from '../../scene-graphs/building-effective-ai-agents-ep01-architecture-choice.json';
import rawEpisode02SceneGraph from '../../scene-graphs/building-effective-ai-agents-ep02-start-simple-scale-intelligently.json';
import rawEpisode03SceneGraph from '../../scene-graphs/building-effective-ai-agents-ep03-single-vs-multi-agent-coordination.json';
import rawEpisode04SceneGraph from '../../scene-graphs/building-effective-ai-agents-ep04-agentic-workflows-are-structure.json';
import rawEpisode05SceneGraph from '../../scene-graphs/building-effective-ai-agents-ep05-production-readiness.json';
import rawEpisode06SceneGraph from '../../scene-graphs/building-effective-ai-agents-ep06-hybrid-emerging-patterns.json';
import rawFounderPlaybookEp01SceneGraph from '../../scene-graphs/the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck.json';
import rawFounderPlaybookEp02SceneGraph from '../../scene-graphs/the-founders-playbook-ai-native-startup-ep02-demo-is-not-demand.json';
import rawFounderPlaybookEp03SceneGraph from '../../scene-graphs/the-founders-playbook-ai-native-startup-ep03-boundaries-before-ai-code.json';
import rawFounderPlaybookEp04SceneGraph from '../../scene-graphs/the-founders-playbook-ai-native-startup-ep04-founder-not-router.json';
import rawFounderPlaybookEp05SceneGraph from '../../scene-graphs/the-founders-playbook-ai-native-startup-ep05-workflow-moat.json';
import {BusinessAgentGuide} from './compositions/BusinessAgentGuide';
import {Cover, CoverGrid, CoverVertical} from './compositions/Cover';
import {FounderPlaybookCover} from './compositions/FounderPlaybookCover';
import {FounderPlaybookEpisode, founderDurationInFrames} from './compositions/FounderPlaybookEpisode';
import {VoiceMixPreview} from './compositions/VoiceMixPreview';
import type {FounderSceneGraph} from './components/founder-playbook/types';
import type {SceneGraph} from './types';

const sceneGraph = rawSceneGraph as SceneGraph;
const episode01SceneGraph = rawEpisode01SceneGraph as SceneGraph;
const founderPlaybookEp01SceneGraph = rawFounderPlaybookEp01SceneGraph as FounderSceneGraph;
const founderPlaybookEp02SceneGraph = rawFounderPlaybookEp02SceneGraph as FounderSceneGraph;
const founderPlaybookEp03SceneGraph = rawFounderPlaybookEp03SceneGraph as FounderSceneGraph;
const founderPlaybookEp04SceneGraph = rawFounderPlaybookEp04SceneGraph as FounderSceneGraph;
const founderPlaybookEp05SceneGraph = rawFounderPlaybookEp05SceneGraph as FounderSceneGraph;
const episodePlaybackRate = 1.2;
const playbackRateFor = (graph: SceneGraph) =>
  graph.slug === 'building-effective-ai-agents-ep06-hybrid-emerging-patterns' ? 1 : episodePlaybackRate;
const episode01SourceCoverSceneGraph = {
  ...episode01SceneGraph,
  cover: {
    ...episode01SceneGraph.cover,
    headline: 'Agent架构怎么选?',
    subhead: '架构、协调、工作流，是三件不同的事',
    artifact: 'source-architecture-choice',
    badge: 'EP01 / 架构选择',
    proofChips: ['Source Diagrams', 'Coordination', 'Workflow'],
    sourceMark: 'Source: Anthropic PDF / Building Effective AI Agents',
    sourceVisualRule: 'Source diagrams are visual anchors; labels preserve the PDF taxonomy.',
  },
} as SceneGraph;
const episodeGraphs = [
  episode01SceneGraph,
  rawEpisode02SceneGraph as SceneGraph,
  rawEpisode03SceneGraph as SceneGraph,
  rawEpisode04SceneGraph as SceneGraph,
  rawEpisode05SceneGraph as SceneGraph,
  rawEpisode06SceneGraph as SceneGraph,
];
const founderPlaybookGraphs = [
  founderPlaybookEp01SceneGraph,
  founderPlaybookEp02SceneGraph,
  founderPlaybookEp03SceneGraph,
  founderPlaybookEp04SceneGraph,
  founderPlaybookEp05SceneGraph,
];

const durationFor = (graph: SceneGraph, playbackRate = 1) =>
  graph.scenes.reduce(
    (total, scene) => total + Math.round((scene.durationSeconds * graph.format.fps) / playbackRate),
    0,
  );

const fps = sceneGraph.format.fps;
const durationInFrames = durationFor(sceneGraph);

export const RemotionRoot = () => {
  return (
    <>
      <Composition
        id="building-effective-ai-agents"
        component={BusinessAgentGuide}
        durationInFrames={durationInFrames}
        fps={fps}
        width={sceneGraph.format.width}
        height={sceneGraph.format.height}
        defaultProps={{sceneGraph}}
      />
      <Composition
        id="building-effective-ai-agents-ep06-voice-mix-preview"
        component={VoiceMixPreview}
        durationInFrames={480}
        fps={30}
        width={1920}
        height={1080}
      />
      {episodeGraphs.map((graph) => (
        <Composition
          key={graph.slug}
          id={graph.slug}
          component={BusinessAgentGuide}
          durationInFrames={durationFor(graph, playbackRateFor(graph))}
          fps={graph.format.fps}
          width={graph.format.width}
          height={graph.format.height}
          defaultProps={{sceneGraph: graph, playbackRate: playbackRateFor(graph)}}
        />
      ))}
      {founderPlaybookGraphs.map((graph) => (
        <Composition
          key={graph.slug}
          id={graph.slug}
          component={FounderPlaybookEpisode}
          durationInFrames={founderDurationInFrames(graph)}
          fps={graph.format.fps}
          width={graph.format.width}
          height={graph.format.height}
          defaultProps={{sceneGraph: graph}}
        />
      ))}
      {founderPlaybookGraphs.map((graph) => (
        <Still
          key={`${graph.slug}-vertical-cover`}
          id={`${graph.slug}-vertical-cover`}
          component={FounderPlaybookCover}
          width={1080}
          height={1920}
          defaultProps={{sceneGraph: graph, variant: 'vertical'}}
        />
      ))}
      {founderPlaybookGraphs.map((graph) => (
        <Still
          key={`${graph.slug}-grid-cover`}
          id={`${graph.slug}-grid-cover`}
          component={FounderPlaybookCover}
          width={1080}
          height={1440}
          defaultProps={{sceneGraph: graph, variant: 'grid'}}
        />
      ))}
      <Still
        id="building-effective-ai-agents-cover"
        component={Cover}
        width={sceneGraph.format.width}
        height={sceneGraph.format.height}
        defaultProps={{sceneGraph}}
      />
      <Still
        id="building-effective-ai-agents-ep01-architecture-choice-cover"
        component={Cover}
        width={episode01SceneGraph.format.width}
        height={episode01SceneGraph.format.height}
        defaultProps={{sceneGraph: episode01SceneGraph}}
      />
      <Still
        id="building-effective-ai-agents-ep01-architecture-choice-source-cover"
        component={Cover}
        width={episode01SourceCoverSceneGraph.format.width}
        height={episode01SourceCoverSceneGraph.format.height}
        defaultProps={{sceneGraph: episode01SourceCoverSceneGraph}}
      />
      <Still
        id="building-effective-ai-agents-ep01-architecture-choice-vertical-cover"
        component={CoverVertical}
        width={1080}
        height={1920}
        defaultProps={{sceneGraph: episode01SourceCoverSceneGraph}}
      />
      <Still
        id="building-effective-ai-agents-ep01-architecture-choice-grid-cover"
        component={CoverGrid}
        width={1080}
        height={1440}
        defaultProps={{sceneGraph: episode01SourceCoverSceneGraph}}
      />
      {episodeGraphs.slice(1).map((graph) => (
        <Still
          key={`${graph.slug}-vertical-cover`}
          id={`${graph.slug}-vertical-cover`}
          component={CoverVertical}
          width={1080}
          height={1920}
          defaultProps={{sceneGraph: graph}}
        />
      ))}
      {episodeGraphs.slice(1).map((graph) => (
        <Still
          key={`${graph.slug}-grid-cover`}
          id={`${graph.slug}-grid-cover`}
          component={CoverGrid}
          width={1080}
          height={1440}
          defaultProps={{sceneGraph: graph}}
        />
      ))}
    </>
  );
};
