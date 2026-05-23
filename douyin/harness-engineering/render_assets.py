from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math

ROOT = Path(__file__).resolve().parent
FRAMES = ROOT / "frames"
FRAMES.mkdir(exist_ok=True)

W, H = 1080, 1920

# Executive Technical Documentary: dark base, high-trust typography,
# restrained cyan accent, cinematic depth, system diagrams.
BG = (7, 10, 14)
GRAPHITE = (15, 20, 27)
PANEL = (18, 25, 34)
PANEL_2 = (23, 31, 42)
INK = (238, 244, 247)
MUTED = (135, 148, 158)
FAINT = (43, 55, 68)
CYAN = (61, 213, 235)
BLUE = (74, 132, 255)
GREEN = (83, 220, 162)
AMBER = (225, 168, 76)
RED = (242, 91, 91)

SANS = "/System/Library/Fonts/SFNS.ttf"
SANS_CN = "/System/Library/Fonts/Hiragino Sans GB.ttc"
MONO = "/System/Library/Fonts/SFNSMono.ttf"
FALLBACK = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"


def font(path, size, index=0):
    selected = path if Path(path).exists() else FALLBACK
    return ImageFont.truetype(selected, size=size, index=index)


F_META = font(MONO, 24)
F_KICKER = font(MONO, 28)
F_HEAD = font(SANS_CN, 78)
F_HEAD_SMALL = font(SANS_CN, 64)
F_SUB = font(SANS_CN, 36)
F_BODY = font(SANS_CN, 30)
F_BODY_SM = font(SANS_CN, 25)
F_BODY_BOLD = font(SANS_CN, 34)
F_NUM = font(SANS, 108)
F_STAT = font(SANS, 96)


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw, text, fnt, max_width):
    lines = []
    for para in text.split("\n"):
        current = ""
        for ch in para:
            test = current + ch
            if text_size(draw, test, fnt)[0] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = ch
        if current:
            lines.append(current)
    return lines


def draw_wrapped(draw, xy, text, fnt, fill, max_width, line_gap=14):
    x, y = xy
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += text_size(draw, line, fnt)[1] + line_gap
    return y


def glow_circle(img, center, radius, color, alpha=80, blur=80):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x, y = center
    d.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    img.alpha_composite(layer)


def base(idx, label, accent=CYAN):
    img = Image.new("RGBA", (W, H), (*BG, 255))
    glow_circle(img, (210, 430), 270, (20, 104, 130), 62, 110)
    glow_circle(img, (880, 1220), 330, (28, 72, 160), 40, 150)
    glow_circle(img, (680, 320), 210, accent, 24, 130)
    draw = ImageDraw.Draw(img)

    # Subtle architectural grid: visible enough to imply systems, not decoration.
    for x in range(72, W - 72, 72):
        draw.line((x, 210, x, H - 210), fill=(18, 27, 36, 120), width=1)
    for y in range(240, H - 220, 72):
        draw.line((72, y, W - 72, y), fill=(18, 27, 36, 120), width=1)

    draw.rectangle((0, 0, W, H), outline=(255, 255, 255, 12), width=2)
    draw.line((72, 162, W - 72, 162), fill=FAINT, width=1)
    draw.line((72, H - 178, W - 72, H - 178), fill=FAINT, width=1)
    draw.text((72, 72), "AI SYSTEMS INTELLIGENCE", font=F_META, fill=MUTED)
    draw.text((72, 112), label.upper(), font=F_META, fill=accent)
    draw.text((W - 180, 62), f"{idx:02d}", font=F_NUM, fill=(34, 47, 60))
    return img, draw


def footer(draw, idx, label):
    draw.text((72, H - 128), f"{idx:02d} / {label}", font=F_BODY_SM, fill=MUTED)
    draw.text((W - 360, H - 128), "Harness Engineering", font=F_BODY_SM, fill=MUTED)


def small_caps(draw, xy, text, accent=CYAN):
    x, y = xy
    draw.text((x, y), text.upper(), font=F_KICKER, fill=accent)
    draw.line((x, y + 50, x + 150, y + 50), fill=accent, width=3)


def headline(draw, y, lines, accent_line=None, accent=CYAN, size="large"):
    fnt = F_HEAD if size == "large" else F_HEAD_SMALL
    for i, line in enumerate(lines):
        color = accent if accent_line == i else INK
        y = draw_wrapped(draw, (72, y), line, fnt, color, W - 144, 16)
        y += 2
    return y


def panel(draw, box, fill=PANEL, outline=FAINT, radius=24, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def node(draw, box, title, body, accent=CYAN, compact=False):
    panel(draw, box, fill=PANEL)
    x1, y1, x2, _ = box
    draw.text((x1 + 26, y1 + 24), title, font=F_BODY_BOLD if not compact else F_BODY, fill=accent)
    draw_wrapped(
        draw,
        (x1 + 26, y1 + (82 if not compact else 70)),
        body,
        F_BODY if not compact else F_BODY_SM,
        MUTED,
        x2 - x1 - 52,
        10,
    )


def arrow(draw, start, end, accent=CYAN):
    draw.line((start[0], start[1], end[0], end[1]), fill=accent, width=3)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    size = 15
    p1 = (end[0] - size * math.cos(angle - 0.45), end[1] - size * math.sin(angle - 0.45))
    p2 = (end[0] - size * math.cos(angle + 0.45), end[1] - size * math.sin(angle + 0.45))
    draw.polygon([end, p1, p2], fill=accent)


def subtitle(draw, y, text):
    return draw_wrapped(draw, (72, y), text, F_SUB, MUTED, W - 144, 16)


def scene_opener():
    img, draw = base(1, "trend signal", CYAN)
    small_caps(draw, (72, 270), "executive brief", CYAN)
    y = headline(draw, 390, ["Harness Engineering", "为什么突然刷屏？"], 1, CYAN)
    subtitle(draw, y + 42, "不是又一个 AI 热词，而是 Agent 从“能说”走向“能做事”的执行骨架。")
    panel(draw, (140, 1110, 940, 1338), fill=(20, 28, 39))
    draw.text((188, 1164), "SYSTEM SHIFT", font=F_META, fill=CYAN)
    draw.text((188, 1218), "Prompt → Context → Harness", font=F_BODY_BOLD, fill=INK)
    draw.text((188, 1276), "from model output to governed action", font=F_BODY_SM, fill=MUTED)
    footer(draw, 1, "Hook")
    return img.convert("RGB")


def scene_loop(idx, label, kicker, title, body, left, right, accent):
    img, draw = base(idx, label, accent)
    small_caps(draw, (72, 270), kicker, accent)
    y = headline(draw, 410, [title], 0, accent)
    subtitle(draw, y + 34, body)
    top = 1050
    node(draw, (92, top, 430, top + 230), left[0], left[1], accent)
    node(draw, (650, top, 988, top + 230), right[0], right[1], accent)
    arrow(draw, (450, top + 115), (628, top + 115), accent)
    footer(draw, idx, label)
    return img.convert("RGB")


def scene_warning():
    img, draw = base(4, "governance boundary", RED)
    small_caps(draw, (72, 270), "not an api key problem", RED)
    y = headline(draw, 390, ["不能只给 AI", "一个 API key"], 1, RED)
    subtitle(draw, y + 42, "权限不是治理。外循环连接生产系统、密钥、审批、合规和真实用户。")
    node(draw, (96, 1130, 984, 1364), "BAD EXECUTION PATH", "Model → production API → hope nothing goes wrong", RED)
    footer(draw, 4, "Permission is not governance")
    return img.convert("RGB")


def scene_failures():
    img, draw = base(5, "failure modes", RED)
    small_caps(draw, (72, 270), "blast radius", RED)
    headline(draw, 390, ["没有 Harness", "错误会被加速"], 1, RED)
    items = [
        ("Prompt injection", "PR、issue、依赖说明污染 agent 行为"),
        ("Wrong action", "错误环境、错误 manifest、错误 rollback"),
        ("Looping damage", "反复 redeploy / rollback 放大损害"),
    ]
    y = 850
    for title, body in items:
        node(draw, (96, y, 984, y + 170), title, body, RED, compact=True)
        y += 206
    footer(draw, 5, "Concrete risks")
    return img.convert("RGB")


def scene_metaphor():
    img, draw = base(6, "mental model", CYAN)
    small_caps(draw, (72, 270), "model outside the model", CYAN)
    headline(draw, 390, ["模型是大脑", "Harness 是控制平面"], 1, CYAN)
    top = 1060
    node(draw, (92, top, 390, top + 250), "MODEL", "推理\n生成计划\n判断下一步", BLUE)
    node(draw, (706, top, 1004, top + 250), "HARNESS", "约束\n执行\n证明", CYAN)
    arrow(draw, (414, top + 125), (682, top + 125), CYAN)
    draw.text((492, top + 80), "intent", font=F_META, fill=MUTED)
    draw.text((484, top + 144), "policy", font=F_META, fill=CYAN)
    footer(draw, 6, "Core analogy")
    return img.convert("RGB")


def scene_knowledge_graph():
    img, draw = base(7, "memory layer", AMBER)
    small_caps(draw, (72, 270), "relationship memory", AMBER)
    y = headline(draw, 390, ["不是普通 RAG", "而是 Knowledge Graph"], 1, AMBER)
    subtitle(draw, y + 38, "交付决策依赖关系，不只是文本：服务、团队、流水线、环境、策略、事故。")
    center = (540, 1175)
    nodes = [
        ("Service", (110, 936)),
        ("Pipeline", (660, 936)),
        ("Policy", (110, 1330)),
        ("Incident", (660, 1330)),
    ]
    for _, (x, yy) in nodes:
        draw.line((x + 155, yy + 77, center[0], center[1]), fill=(*AMBER, 88), width=2)
    panel(draw, (390, 1086, 690, 1264), fill=PANEL_2)
    draw.text((430, 1138), "Delivery KG", font=F_BODY_BOLD, fill=INK)
    for title, (x, yy) in nodes:
        node(draw, (x, yy, x + 310, yy + 154), title, "关系 + 状态", AMBER, compact=True)
    footer(draw, 7, "Relationship memory")
    return img.convert("RGB")


def scene_context():
    img, draw = base(8, "six-layer harness", CYAN)
    small_caps(draw, (72, 270), "original framework", CYAN)
    headline(draw, 390, ["Harness", "六层执行骨架"], 1, CYAN)
    items = [
        ("01 Context", "结构化上下文管理"),
        ("02 Tools", "工具系统设计"),
        ("03 Orchestration", "执行编排引擎"),
        ("04 State", "状态与记忆管理"),
        ("05 Evaluation", "独立评估和可观测性"),
        ("06 Recovery", "约束校验和恢复机制"),
    ]
    for i, (title, body) in enumerate(items):
        x = 92 + (i % 2) * 448
        y = 820 + (i // 2) * 220
        node(draw, (x, y, x + 396, y + 176), title, body, CYAN, compact=True)
    footer(draw, 8, "Six-layer harness")
    return img.convert("RGB")


def scene_tools_delegate():
    img, draw = base(9, "governed tools", GREEN)
    small_caps(draw, (72, 270), "controlled tools", GREEN)
    y = headline(draw, 390, ["工具可以强大", "但不能裸调"], 1, GREEN)
    subtitle(draw, y + 38, "部署、回滚、feature flag、扫描、审批，都要经过权限、策略和执行边界。")
    top = 1080
    boxes = [
        ("MODEL", "提出意图\n不持有密钥", 92),
        ("HARNESS", "检查策略\n记录证据", 392),
        ("DELEGATE", "企业边界内\n执行动作", 692),
    ]
    for title, body, x in boxes:
        node(draw, (x, top, x + 260, top + 250), title, body, GREEN, compact=True)
    arrow(draw, (360, top + 126), (382, top + 126), GREEN)
    arrow(draw, (660, top + 126), (682, top + 126), GREEN)
    footer(draw, 9, "Tools under policy")
    return img.convert("RGB")


def scene_secrets():
    img, draw = base(10, "secrets boundary", RED)
    small_caps(draw, (72, 270), "zero secret leakage", RED)
    y = headline(draw, 390, ["密钥不进模型", "不进 Prompt"], 1, RED)
    subtitle(draw, y + 38, "密钥在企业执行层解密，而不是进入模型上下文、供应商内存或日志。")
    node(draw, (96, 1110, 984, 1380), "CORRECT PATH", "Model intent → Harness policy → Delegate decrypts secret → Enterprise execution", RED)
    footer(draw, 10, "Keep credentials inside")
    return img.convert("RGB")


def scene_pillars():
    img, draw = base(11, "evidence chain", AMBER)
    small_caps(draw, (72, 270), "proof of action", AMBER)
    headline(draw, 390, ["每次动作", "都要留下证据"], 1, AMBER)
    items = [
        ("01", "Policy gate", "是否允许、谁批准、条件是什么"),
        ("02", "Scorecard", "服务质量、安全和发布健康度"),
        ("03", "Rollback", "失败时怎么恢复，谁触发"),
        ("04", "Audit log", "动作、证据、结果都可追踪"),
    ]
    y = 800
    for num, title, body in items:
        draw.text((96, y + 22), num, font=F_META, fill=AMBER)
        draw.text((188, y + 12), title, font=F_BODY_BOLD, fill=INK)
        draw_wrapped(draw, (188, y + 68), body, F_BODY, MUTED, W - 276, 8)
        draw.line((96, y + 158, 984, y + 158), fill=FAINT, width=1)
        y += 188
    footer(draw, 11, "Evidence chain")
    return img.convert("RGB")


def scene_mcp_skills():
    img, draw = base(12, "mcp and skills", CYAN)
    small_caps(draw, (72, 270), "operational interface", CYAN)
    headline(draw, 390, ["不是暴露所有 API", "而是收敛成工具"], 1, CYAN)
    stats = [("11", "consolidated tools"), ("168", "resource types"), ("31", "toolsets")]
    y = 880
    for number, label in stats:
        draw.text((108, y), number, font=F_STAT, fill=CYAN)
        draw.text((330, y + 34), label, font=F_BODY_BOLD, fill=INK)
        draw.line((108, y + 132, 972, y + 132), fill=FAINT, width=1)
        y += 186
    subtitle(draw, y + 30, "Skills 把人的意图翻译成正确的交付操作。")
    footer(draw, 12, "Operational interface")
    return img.convert("RGB")


def scene_gate():
    img, draw = base(13, "governed path", CYAN)
    small_caps(draw, (72, 270), "safe execution", CYAN)
    headline(draw, 390, ["AI 不绕过流程", "它通过流程"], 1, CYAN)
    top = 1000
    steps = [
        ("AI REQUEST", "部署或回滚意图"),
        ("POLICY GATE", "权限 / 审批 / 风险检查"),
        ("ENTERPRISE EXEC.", "企业系统内执行并留证据"),
    ]
    for i, (title, body) in enumerate(steps):
        x = 92 + i * 300
        node(draw, (x, top, x + 260, top + 300), title, body, CYAN, compact=True)
        if i < 2:
            arrow(draw, (x + 268, top + 150), (x + 290, top + 150), CYAN)
    footer(draw, 13, "Governed path")
    return img.convert("RGB")


def scene_takeaway():
    img, draw = base(14, "mental upgrade", CYAN)
    small_caps(draw, (72, 270), "takeaway", CYAN)
    y = headline(draw, 390, ["模型是大脑", "Delivery Harness", "是安全上线控制平面"], 1, CYAN, size="small")
    subtitle(draw, y + 46, "未来不是让 AI 直接上生产，而是让每个动作可治理、可回滚、可审计。")
    panel(draw, (120, 1180, 960, 1328), fill=PANEL_2)
    draw.text((172, 1228), "AI cognition compression", font=F_BODY_BOLD, fill=CYAN)
    draw.text((172, 1280), "frontier research → systems mental model", font=F_BODY_SM, fill=MUTED)
    footer(draw, 14, "Final memory")
    return img.convert("RGB")


for old_frame in FRAMES.glob("scene_*.png"):
    old_frame.unlink()

scenes = [
    scene_opener(),
    scene_loop(2, "Inner loop", "coding loop", "Coding Agent", "写代码、改代码、跑测试。它主要改变代码仓库。", ("Developer", "提出需求\n检查代码"), ("Repo", "代码变更\n测试结果"), BLUE),
    scene_loop(3, "Outer loop", "delivery loop", "Delivery Agent", "构建、扫描、审批、部署、回滚、审计。它会接触生产系统。", ("Code", "构建产物\n发布候选"), ("Production", "真实用户\n真实风险"), CYAN),
    scene_warning(),
    scene_failures(),
    scene_metaphor(),
    scene_knowledge_graph(),
    scene_context(),
    scene_tools_delegate(),
    scene_secrets(),
    scene_pillars(),
    scene_mcp_skills(),
    scene_gate(),
    scene_takeaway(),
]

for i, img in enumerate(scenes, 1):
    img.save(FRAMES / f"scene_{i:02d}.png", quality=95)

scenes[0].save(ROOT / "cover.png", quality=95)
print(f"wrote {len(scenes)} frames and cover")
