import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const remotionRoot = process.cwd();
const repoRoot = path.resolve(remotionRoot, '..');
const sceneGraphDir = path.join(repoRoot, 'scene-graphs');
const publicDir = path.join(remotionRoot, 'public');

const sceneGraphFiles = fs
  .readdirSync(sceneGraphDir)
  .filter((file) => file.endsWith('.json'))
  .sort();

const missingImages = [];
const emptyArtifacts = [];
const generatedFallbacks = [];

for (const file of sceneGraphFiles) {
  const graphPath = path.join(sceneGraphDir, file);
  const graph = JSON.parse(fs.readFileSync(graphPath, 'utf8'));

  for (const scene of graph.scenes ?? []) {
    const artifact = scene.artifact ?? {};
    const imagePaths = artifact.imagePaths ?? (artifact.imagePath ? [artifact.imagePath] : []);
    const hasImages = imagePaths.length > 0;
    const hasNodes = Boolean(artifact.nodes?.length);
    const hasGroups = Boolean(artifact.groups?.length);

    for (const imagePath of imagePaths) {
      if (!fs.existsSync(path.join(publicDir, imagePath))) {
        missingImages.push(`${file} / ${scene.id}: ${imagePath}`);
      }
    }

    if (!hasImages && !hasNodes && !hasGroups) {
      emptyArtifacts.push(`${file} / ${scene.id}: ${artifact.type ?? 'unknown'}`);
    }

    if (artifact.type === 'architecture-hierarchy' && !hasGroups && hasNodes && artifact.fallback === 'generated') {
      generatedFallbacks.push(`${file} / ${scene.id}: generated hierarchy from nodes`);
    }

    if (
      (artifact.type === 'source-diagram' || artifact.type === 'diagram-montage') &&
      !hasImages &&
      artifact.fallback === 'generated'
    ) {
      generatedFallbacks.push(`${file} / ${scene.id}: generated source diagram from scene`);
    }
  }
}

if (generatedFallbacks.length > 0) {
  console.log('Generated visual fallbacks:');
  for (const item of generatedFallbacks) {
    console.log(`- ${item}`);
  }
}

if (missingImages.length > 0) {
  console.warn('\nMissing original source diagram files; renderer fallback will remain visible:');
  for (const item of missingImages) {
    console.warn(`- ${item}`);
  }
}

if (emptyArtifacts.length > 0) {
  console.error('\nScenes with no renderable visual data:');
  for (const item of emptyArtifacts) {
    console.error(`- ${item}`);
  }
  process.exit(1);
}

console.log('\nVisual asset audit passed.');
