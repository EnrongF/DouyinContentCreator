const $ = (selector) => document.querySelector(selector);

function params() {
  const query = new URLSearchParams(location.search);
  return {
    beat: Number(query.get("beat") || 1),
    phase: Number(query.get("phase") || 7),
    exportMode: query.get("export") === "1"
  };
}

function el(tag, className, attrs = {}, children = []) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  for (const [key, value] of Object.entries(attrs)) {
    if (key === "text") node.textContent = value;
    else if (key === "html") node.innerHTML = value;
    else if (key === "style") Object.assign(node.style, value);
    else if (key === "dataId") node.dataset.id = value;
    else node.setAttribute(key, value);
  }
  for (const child of children) node.append(child);
  return node;
}

function position(node, x, y, w, h) {
  Object.assign(node.style, {
    left: `${x}px`,
    top: `${y}px`,
    width: `${w}px`,
    height: `${h}px`
  });
  return node;
}

function card(id, x, y, w, h, title, body = "", cls = "card") {
  const node = position(el("article", cls, { dataId: id }), x, y, w, h);
  node.append(el("h2", "", { text: title }));
  if (body) node.append(el("p", "", { html: body.replace(/\n/g, "<br>") }));
  return node;
}

function node(id, x, y, w, h, title, body = "") {
  const n = position(el("article", "node", { dataId: id }), x, y, w, h);
  n.append(el("h3", "", { text: title }));
  if (body) n.append(el("p", "", { html: body.replace(/\n/g, "<br>") }));
  return n;
}

function stat(id, x, y, w, h, value, label) {
  const s = position(el("article", "stat", { dataId: id }), x, y, w, h);
  s.append(el("strong", "", { text: value }));
  s.append(el("span", "", { html: label.replace(/\n/g, "<br>") }));
  return s;
}

function arrow(x, y, w, id = "") {
  return position(el("div", "arrow", id ? { dataId: id } : {}), x, y, w, 3);
}

function pill(id, x, y, text) {
  return position(el("div", "pill", { dataId: id, text }), x, y, Math.max(136, text.length * 12 + 34), 42);
}

function pathSvg(cls, d) {
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("class", cls);
  svg.setAttribute("viewBox", "0 0 1010 810");
  const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
  path.setAttribute("d", d);
  svg.append(path);
  return svg;
}

const renderers = {
  source(stage) {
    stage.append(
      card("source-card", 80, 138, 820, 240, "Harness engineering", "Leveraging Codex in an agent-first world\nOpenAI Engineering · Ryan Lopopolo · 2026-02-11"),
      card("visible", 105, 520, 245, 135, "可见", "应用和运行信号能被看到"),
      card("control", 382, 520, 245, 135, "可控", "规则和流程能约束生成"),
      card("verify", 660, 520, 245, 135, "可验证", "结果能被测试和复现")
    );
  },

  metrics(stage) {
    const items = [
      ["metric-zero", 64, 120, "0", "manually-written\ncode"],
      ["metric-months", 294, 120, "5", "months"],
      ["metric-lines", 524, 120, "1M", "lines of code"],
      ["metric-prs", 754, 120, "1.5K", "PRs"],
      ["metric-time", 64, 365, "1/10", "hand-coding\ntime"],
      ["metric-rate", 294, 365, "3.5", "PRs / engineer\n/ day"],
      ["metric-engineers", 524, 365, "7", "engineers later"],
      ["metric-users", 754, 365, "100s", "users + testers"]
    ];
    for (const [id, x, y, v, label] of items) stage.append(stat(id, x, y, 190, 180, v, label));
    stage.append(card("metric-thesis", 118, 635, 770, 96, "数字说明：研发系统的吞吐结构变了。", ""));
  },

  role(stage) {
    stage.append(
      card("human", 90, 250, 315, 285, "Human", "intent\njudgment\nboundaries"),
      card("agent", 600, 250, 315, 285, "Codex", "implementation\niteration\nverification"),
      arrow(430, 390, 145, "role-arrow"),
      card("role-note", 235, 640, 540, 92, "Human steers. Agent executes. System verifies.", "")
    );
  },

  scaffold(stage) {
    stage.append(pathSvg("flow-path", "M145 405 H835"));
    stage.append(
      node("scaffold", 68, 320, 178, 150, "Scaffold", "Codex + GPT-5"),
      node("repo", 318, 320, 178, 150, "Repo", "structure\npackages"),
      node("ci", 568, 320, 178, 150, "CI", "tests\nformat"),
      node("agents", 818, 320, 150, 150, "AGENTS.md", "agent rules"),
      card("scaffold-result", 155, 590, 700, 105, "仓库从第一天就面向 Agent 工作流设计", "")
    );
  },

  devtools(stage) {
    const app = position(el("article", "browser-surface", { dataId: "app" }), 72, 132, 430, 500);
    app.innerHTML = `<div class="artifact-label">localhost:worktree/app</div><div class="ui-line wide"></div><div class="ui-line"></div><div class="ui-box"></div>`;
    stage.append(
      app,
      card("devtools", 610, 180, 330, 382, "DevTools MCP", "screenshot()\nDOM snapshot\nnavigate()\nruntime events"),
      arrow(520, 380, 70, "devtools-arrow"),
      card("validate", 124, 650, 760, 92, "Observe → Reproduce → Patch → Validate", "")
    );
  },

  observability(stage) {
    stage.append(pathSvg("flow-path", "M128 406 H300 C380 406 390 210 470 210 H592 M300 406 H592 M300 406 C390 406 390 602 470 602 H592 M702 210 C800 250 805 360 860 385 M702 406 H860 M702 602 C800 562 805 455 860 425"));
    stage.append(
      node("worktree", 64, 334, 160, 138, "Worktree", "isolated app"),
      node("vector", 288, 334, 160, 138, "Vector", "fan-out"),
      node("logs", 560, 145, 170, 122, "Logs", "LogQL"),
      node("metrics", 560, 334, 170, 122, "Metrics", "PromQL"),
      node("traces", 560, 523, 170, 122, "Traces", "TraceQL"),
      node("codex", 828, 315, 160, 178, "Codex", "query\nsignals"),
      card("target", 176, 700, 660, 74, "performance targets become executable tasks", "")
    );
  },

  knowledge(stage) {
    stage.append(
      card("agents-map", 78, 250, 255, 280, "AGENTS.md", "~100 lines\nnavigation map\nnot a giant manual"),
      arrow(360, 385, 92, "docs-arrow")
    );
    const docs = position(el("article", "docs-panel card", { dataId: "docs" }), 468, 130, 470, 540);
    docs.innerHTML = `<h2>docs/</h2>
      ${["Architecture · ARCHITECTURE", "Plans · PLANS / exec", "Product · PRODUCT", "Quality · SECURITY", "Design · UI"].map(x => `<div class="line-item">${x}</div>`).join("")}`;
    stage.append(docs, card("freshness", 185, 710, 650, 72, "CI + link checks + doc-gardening agent keep it fresh", ""));
  },

  invisible(stage) {
    stage.append(card("context", 390, 310, 260, 170, "Codex Context", "repo-local\nversioned\nverifiable"));
    const outside = [
      ["outside-doc", 70, 140, "外部文档"],
      ["chat", 710, 140, "聊天讨论"],
      ["tribal", 70, 565, "隐性经验"],
      ["decision", 710, 565, "临时决策"]
    ];
    for (const [id, x, y, title] of outside) stage.append(card(id, x, y, 230, 130, title, "must enter repo"));
    stage.append(pathSvg("flow-path", "M185 205 L455 350 M825 205 L585 350 M185 630 L455 430 M825 630 L585 430"));
  },

  architecture(stage) {
    const names = ["Types", "Config", "Repo", "Service", "Runtime", "UI"];
    names.forEach((name, i) => stage.append(node("ladder", 62 + i * 147, 238, 116, 118, name, "")));
    stage.append(
      pathSvg("flow-path", "M170 296 H248 M318 296 H396 M466 296 H544 M614 296 H692 M762 296 H840"),
      card("lint", 86, 505, 300, 142, "Blocked shortcut", "lint message carries remediation"),
      card("providers", 510, 505, 420, 142, "Providers Boundary", "auth / connectors / telemetry / feature flags"),
      pathSvg("orbit-path", "M235 495 C410 420 600 395 790 362")
    );
  },

  merge(stage) {
    stage.append(
      card("fix-cost", 80, 225, 310, 240, "Fix Cost", "cheaper with\nfast agents"),
      card("waiting-cost", 620, 225, 310, 240, "Waiting Cost", "expensive when\nflow stalls"),
      arrow(420, 345, 160, "merge-arrow"),
      pill("pr-pills", 122, 615, "short-lived PRs"),
      pill("pr-pills", 392, 615, "fewer blocking gates"),
      pill("pr-pills", 700, 615, "flaky fixed later"),
      card("merge-model", 170, 725, 660, 74, "Caveat: high throughput required.", "")
    );
  },

  scope(stage) {
    const items = [
      ["code", 110, 160, "代码 / 测试", "business logic · evaluations"],
      ["tools", 555, 160, "工具 / CI", "release tooling · scripts"],
      ["docs", 110, 430, "文档 / 评审", "design history · review comments"],
      ["dash", 555, 430, "仪表盘 / 管理", "dashboards · repo management"]
    ];
    for (const [id, x, y, title, body] of items) stage.append(card("scope-grid " + id, x, y, 345, 148, title, body));
    stage.append(card("scope-note", 206, 700, 590, 74, "The whole development system becomes generatable.", ""));
  },

  loop(stage) {
    stage.append(pathSvg("loop-path", "M500 147 C820 150 918 520 660 686 C400 850 85 610 166 326 C205 190 330 145 500 147"));
    const steps = [
      ["check", 220, 120, "Check", "state"],
      ["bug", 485, 90, "Bug", "video"],
      ["patch", 735, 190, "Patch", "fix"],
      ["test", 795, 410, "Test", "app"],
      ["pr", 650, 620, "PR", "change"],
      ["feedback", 390, 650, "Feedback", "build"],
      ["escalate", 135, 555, "Escalate", "human"],
      ["merge", 90, 335, "Merge", "land"]
    ];
    for (const [id, x, y, title, body] of steps) stage.append(node(id, x, y, 154, 122, title, body));
    stage.append(card("loop-all", 420, 345, 170, 120, "loop", ""));
  },

  entropy(stage) {
    stage.append(
      card("old", 90, 180, 315, 245, "旧办法", "Friday cleanup\n20% time\nAI slop removal"),
      card("new", 605, 180, 315, 245, "新办法", "golden principles\nbackground Codex\nsmall refactor PRs"),
      arrow(432, 300, 142, "entropy-arrow")
    );
    const principles = position(el("article", "card", { dataId: "principles" }), 130, 548, 760, 188);
    principles.innerHTML = `<h2>golden principles</h2>
      <p>01 shared utilities &gt; hand-rolled helpers<br>02 no YOLO data probing<br>03 typed SDKs + validated boundaries<br>04 scan deviations → quality grades → refactor PRs</p>`;
    stage.append(principles);
  },

  final(stage) {
    stage.append(
      card("model", 90, 245, 315, 250, "Model", "generates code\nand artifacts"),
      card("harness", 605, 245, 315, 250, "Harness", "visibility\ncontrol\nverification\nmaintenance"),
      arrow(432, 365, 142, "final-arrow"),
      pill("governance", 130, 620, "可见"),
      pill("governance", 326, 620, "可控"),
      pill("governance", 522, 620, "可验证"),
      pill("governance", 752, 620, "可维护"),
      card("caveat", 200, 735, 610, 74, "Still learning: consistency.", "")
    );
  }
};

function setActive(stage, focusIds) {
  const focus = new Set(focusIds || []);
  const candidates = Array.from(stage.querySelectorAll("[data-id]"));
  for (const node of candidates) {
    const ids = node.dataset.id.split(/\s+/);
    const isActive = ids.some((id) => focus.has(id));
    node.classList.toggle("focus", isActive);
    node.classList.toggle("dim", focus.size > 0 && !isActive && !ids.includes("headline"));
    if (isActive) node.append(el("div", "sweep"));
  }
}

function render() {
  const { beat, phase, exportMode } = params();
  const beatData = window.BEATS.find((item) => item.beat === beat) || window.BEATS[0];
  const scene = window.SCENES[beatData.scene];
  const design = window.BEAT_DESIGN[beat] || {};
  const phaseValue = Math.max(0, Math.min(1, phase / 7));

  if (exportMode) document.documentElement.classList.add("export");
  document.documentElement.style.setProperty("--phase", phaseValue.toFixed(4));
  document.documentElement.style.setProperty("--beat-progress", String(design.progress || beat / 59));
  document.documentElement.style.setProperty("--accent", scene.accent);
  document.documentElement.style.setProperty("--accent-soft", `${scene.accent}33`);

  $("#sceneNumber").textContent = `${String(sceneIndex(beatData.scene)).padStart(2, "0")}/14`;
  $("#sceneLabel").textContent = scene.label.toUpperCase();
  $("#kicker").textContent = scene.kicker;
  $("#headline").innerHTML = scene.headline.map((line) => `<span>${line}</span>`).join("<br>");
  $("#note").textContent = scene.note;
  $("#beatLabel").textContent = `beat ${String(beat).padStart(2, "0")}`;

  const stage = $("#stage");
  stage.innerHTML = "";
  const claim = $(".left-claim");
  claim.classList.remove("focus");
  claim.querySelectorAll(".sweep").forEach((node) => node.remove());
  stage.append(el("div", "stage-title", { text: scene.title }));
  stage.append(el("div", "progress-rail"));
  const inner = el("div", "stage-inner");
  stage.append(inner);
  renderers[scene.render](inner);

  if (design.focus?.includes("headline")) {
    claim.classList.add("focus");
    claim.append(el("div", "sweep"));
  }
  setActive(inner, design.focus || []);
}

function sceneIndex(scene) {
  return Number(scene);
}

window.addEventListener("DOMContentLoaded", render);
