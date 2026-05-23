from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import html
import json
import math

ROOT = Path(__file__).resolve().parent
FRAMES = ROOT / "frames"
FRAMES.mkdir(exist_ok=True)
FRAME_MANIFEST = ROOT / "frame_durations.json"
AUDIO_MANIFEST = ROOT / "beat_audio_manifest.json"

W, H = 1920, 1080
PHASES_PER_BEAT = 8
PHASE_DURATION_WEIGHTS = (0.10, 0.10, 0.11, 0.12, 0.12, 0.13, 0.14, 0.18)

BG = (11, 12, 12)
BG_2 = (16, 17, 16)
PANEL = (24, 25, 23)
PANEL_2 = (31, 32, 29)
INK = (246, 242, 232)
MUTED = (163, 158, 146)
SOFT = (88, 88, 79)
FAINT = (55, 55, 49)
CYAN = (118, 203, 214)
CLAY = (220, 124, 91)
OLIVE = (136, 158, 116)
GOLD = (222, 178, 96)
BLUE = (126, 157, 199)
RED = (224, 91, 82)

LEFT_X = 92
LEFT_W = 650
RIGHT_X = 820
RIGHT_Y = 116
RIGHT_W = 1010
RIGHT_H = 810
TITLE_BOX = (LEFT_X, 224, LEFT_X + LEFT_W, 520)

SANS = "/System/Library/Fonts/SFNS.ttf"
SANS_CN = "/System/Library/Fonts/Hiragino Sans GB.ttc"
SERIF_CN = "/System/Library/Fonts/Supplemental/Songti.ttc"
MONO = "/System/Library/Fonts/SFNSMono.ttf"
NY = "/System/Library/Fonts/NewYork.ttf"
FALLBACK = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"


def font(path, size, index=0):
    selected = path if Path(path).exists() else FALLBACK
    return ImageFont.truetype(selected, size=size, index=index)


F_META = font(MONO, 18)
F_META_L = font(MONO, 24)
F_KICKER = font(MONO, 26)
F_HEAD = font(SERIF_CN, 76)
F_HEAD_SM = font(SERIF_CN, 64)
F_SUB = font(SANS_CN, 31)
F_BODY = font(SANS_CN, 28)
F_BODY_SM = font(SANS_CN, 23)
F_BODY_XS = font(SANS_CN, 20)
F_BODY_BOLD = font(SANS_CN, 34)
F_LABEL = font(SANS_CN, 24)
F_STAT = font(NY, 90)
F_STAT_SM = font(NY, 70)
F_NUM = font(SANS, 102)


def duration_hint(beat):
    if "audio_duration" in beat:
        return float(beat["audio_duration"])
    if "duration_hint" in beat:
        return float(beat["duration_hint"])
    return max(1.2, min(5.2, len(beat["caption"]) / 7.5 + 0.8))


def blend_color(a, b, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw, text, fnt, max_width):
    lines = []
    for para in str(text).split("\n"):
        if not para:
            lines.append("")
            continue
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


def draw_wrapped(draw, xy, text, fnt, fill, max_width, line_gap=10):
    x, y = xy
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += text_size(draw, line, fnt)[1] + line_gap
    return y


def glow(img, center, radius, color, alpha=45, blur=120):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x, y = center
    d.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))


def panel(draw, box, fill=PANEL, outline=FAINT, radius=26, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def base(idx, label, accent=CYAN):
    img = Image.new("RGBA", (W, H), (*BG, 255))
    glow(img, (260, 210), 420, accent, 34, 170)
    glow(img, (1530, 710), 520, blend_color(accent, OLIVE, 0.55), 28, 190)
    glow(img, (980, 120), 320, CLAY, 12, 180)
    draw = ImageDraw.Draw(img)

    # Minimal documentary chrome: source identity without decorative clutter.
    draw.text((LEFT_X, 66), "AI COGNITION COMPRESSION", font=F_META, fill=MUTED)
    draw.text((LEFT_X, 96), "OpenAI Harness Engineering", font=F_BODY_SM, fill=INK)
    draw.text((RIGHT_X, 70), f"{idx:02d}/14", font=F_META_L, fill=accent)
    draw.text((RIGHT_X + 82, 73), label.upper(), font=F_META, fill=MUTED)
    draw.line((LEFT_X, 152, W - 92, 152), fill=(70, 70, 63, 105), width=1)
    draw.line((LEFT_X, 972, W - 92, 972), fill=(70, 70, 63, 80), width=1)
    draw.text((LEFT_X, 1004), "source: openai.com/index/harness-engineering", font=F_BODY_XS, fill=(120, 116, 105))
    draw.text((W - 410, 1004), "native 16:9 systems documentary", font=F_BODY_XS, fill=(120, 116, 105))
    return img, draw


def left_claim(draw, kicker, lines, accent=CYAN, note=None, small=False):
    draw.text((LEFT_X, 192), kicker.upper(), font=F_KICKER, fill=accent)
    draw.line((LEFT_X, 236, LEFT_X + 138, 236), fill=accent, width=3)
    y = 278
    fnt = F_HEAD_SM if small else F_HEAD
    for line in lines:
        y = draw_wrapped(draw, (LEFT_X, y), line, fnt, INK, LEFT_W, 13)
    if note:
        y += 22
        draw_wrapped(draw, (LEFT_X + 4, y), note, F_SUB, MUTED, LEFT_W - 28, 13)
    return y


def stage(draw, title=None, accent=CYAN):
    box = (RIGHT_X, RIGHT_Y, RIGHT_X + RIGHT_W, RIGHT_Y + RIGHT_H)
    panel(draw, box, fill=(17, 18, 17), outline=(52, 53, 47), radius=34, width=1)
    if title:
        draw.text((RIGHT_X + 42, RIGHT_Y + 36), title, font=F_META_L, fill=accent)
    return box


def card(draw, box, title, body="", accent=CYAN, fill=PANEL, title_font=None, body_font=None):
    panel(draw, box, fill=fill, outline=blend_color(accent, FAINT, 0.62), radius=24, width=1)
    x1, y1, x2, y2 = box
    draw.text((x1 + 28, y1 + 24), title, font=title_font or F_BODY_BOLD, fill=accent)
    if body:
        draw_wrapped(draw, (x1 + 28, y1 + 78), body, body_font or F_BODY_SM, MUTED, x2 - x1 - 56, 9)


def stat_card(draw, box, stat, label, accent=CYAN):
    panel(draw, box, fill=PANEL_2, outline=blend_color(accent, FAINT, 0.45), radius=24, width=1)
    x1, y1, x2, _ = box
    draw.text((x1 + 28, y1 + 22), stat, font=F_STAT, fill=accent)
    draw_wrapped(draw, (x1 + 30, y1 + 118), label, F_BODY_SM, INK, x2 - x1 - 60, 8)


def node(draw, box, title, body="", accent=CYAN, active=True, compact=False):
    fill = PANEL_2 if active else (20, 21, 19)
    outline = blend_color(accent, FAINT, 0.48 if active else 0.72)
    panel(draw, box, fill=fill, outline=outline, radius=22, width=1)
    x1, y1, x2, _ = box
    draw.text((x1 + 24, y1 + 22), title, font=F_LABEL if compact else F_BODY_BOLD, fill=accent if active else MUTED)
    if body:
        draw_wrapped(draw, (x1 + 24, y1 + (62 if compact else 78)), body, F_BODY_XS if compact else F_BODY_SM, INK if active else MUTED, x2 - x1 - 48, 7)


def arrow(draw, start, end, accent=CYAN, width=3, alpha=220):
    color = (*accent, alpha)
    draw.line((start[0], start[1], end[0], end[1]), fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    size = 15
    p1 = (end[0] - size * math.cos(angle - 0.48), end[1] - size * math.sin(angle - 0.48))
    p2 = (end[0] - size * math.cos(angle + 0.48), end[1] - size * math.sin(angle + 0.48))
    draw.polygon([end, p1, p2], fill=color)


def connector(draw, points, accent=CYAN, width=3):
    for a, b in zip(points, points[1:]):
        draw.line((a[0], a[1], b[0], b[1]), fill=(*accent, 180), width=width)


def pill(draw, xy, text, accent=CYAN):
    x, y = xy
    tw, th = text_size(draw, text, F_BODY_XS)
    box = (x, y, x + tw + 34, y + th + 20)
    panel(draw, box, fill=(25, 27, 25), outline=blend_color(accent, FAINT, 0.45), radius=999)
    draw.text((x + 17, y + 10), text, font=F_BODY_XS, fill=INK)
    return box


def focus_overlay(image, caption, boxes=None, accent=CYAN, beat=None, phase=0.0, phase_idx=0):
    """Soft animated focus: dim inactive content, glow the active element, no hard rectangle."""
    img = image.convert("RGBA")
    boxes = boxes or []
    pulse = 0.5 + 0.5 * math.sin((phase * math.tau) - math.pi / 2)
    sweep = max(0.0, min(1.0, phase))
    color_shift = 0.5 + 0.5 * math.sin(phase * math.tau)
    active = blend_color(accent, INK, color_shift * 0.28)

    shade = Image.new("RGBA", img.size, (0, 0, 0, int(14 + 10 * pulse)))
    img.alpha_composite(shade)

    glow_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    line_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    ld = ImageDraw.Draw(line_layer)
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = box
        primary = i == 0
        strength = 1.0 if primary else 0.58
        pad = int(18 + 16 * pulse)
        glow_box = (x1 - pad, y1 - pad, x2 + pad, y2 + pad)
        gd.rounded_rectangle(
            glow_box,
            radius=34,
            fill=(*active, int((34 + 22 * pulse) * strength)),
        )
        for step in range(5):
            inset = step * 3
            alpha = int((120 - step * 18 + 35 * pulse) * strength)
            ld.rounded_rectangle(
                (x1 - inset, y1 - inset, x2 + inset, y2 + inset),
                radius=28 + step,
                outline=(*active, max(18, alpha)),
                width=1,
            )
        if primary:
            sx = int(x1 + (x2 - x1) * sweep)
            ld.line((sx, y1 + 8, sx, y2 - 8), fill=(*INK, 76), width=2)
            ld.line((x1 + 28, y2 + 12, x1 + 28 + int((x2 - x1 - 56) * sweep), y2 + 12), fill=(*active, 180), width=3)

    img.alpha_composite(glow_layer.filter(ImageFilter.GaussianBlur(16)))
    img.alpha_composite(line_layer)
    return img.convert("RGB")


def scene_01():
    img, draw = base(1, "official source", CYAN)
    left_claim(
        draw,
        "openai engineering",
        ["别只看", "一百万行代码"],
        CYAN,
        "真正的变化：软件工程被改造成 Codex 能执行、能检查的环境。",
    )
    stage(draw, "SOURCE ARTIFACT", CYAN)
    card(
        draw,
        (900, 255, 1750, 520),
        "Harness engineering",
        "Leveraging Codex in an agent-first world\nOpenAI Engineering · Ryan Lopopolo · 2026-02-11",
        CYAN,
        fill=(22, 26, 28),
    )
    draw.text((940, 600), "核心压缩", font=F_META_L, fill=MUTED)
    card(draw, (940, 650, 1230, 800), "可见", "应用和运行信号能被看到", OLIVE)
    card(draw, (1260, 650, 1510, 800), "可控", "规则和流程能约束生成", GOLD)
    card(draw, (1540, 650, 1790, 800), "可验证", "结果能被测试和复现", CYAN)
    return img.convert("RGB")


def scene_02():
    img, draw = base(2, "source numbers", BLUE)
    left_claim(draw, "original numbers", ["先看", "原始数字"], BLUE, "这些数字来自 OpenAI 原文，不是二次转述。")
    stage(draw, "SOURCE METRICS", BLUE)
    cards = [
        ((870, 210, 1088, 390), "0", "manually-written code", BLUE),
        ((1115, 210, 1333, 390), "5", "months", CYAN),
        ((1360, 210, 1578, 390), "1M", "lines of code", OLIVE),
        ((1605, 210, 1805, 390), "1.5K", "PRs", GOLD),
        ((870, 455, 1088, 635), "1/10", "hand-coding time", RED),
        ((1115, 455, 1333, 635), "3.5", "PRs / engineer / day", CYAN),
        ((1360, 455, 1578, 635), "7", "engineers later", BLUE),
        ((1605, 455, 1805, 635), "100s", "users + testers", OLIVE),
    ]
    for box, stat, label, color in cards:
        stat_card(draw, box, stat, label, color)
    draw.text((900, 754), "数字不是结论，数字说明：研发系统的吞吐结构变了。", font=F_BODY, fill=INK)
    return img.convert("RGB")


def scene_03():
    img, draw = base(3, "role inversion", CYAN)
    left_claim(draw, "human attention", ["人类掌舵", "Codex 执行"], CYAN, "核心不是代码更多，而是人的工作重心被上移。")
    stage(draw, "ROLE INVERSION", CYAN)
    card(draw, (900, 310, 1210, 620), "过去", "人写代码\n工具辅助\n评审靠人补救", MUTED, fill=(21, 22, 20))
    card(draw, (1450, 310, 1760, 620), "现在", "人设方向\nAgent 执行\n系统负责反馈", CYAN, fill=(22, 27, 28))
    arrow(draw, (1235, 465), (1425, 465), CYAN, 5)
    draw.text((1015, 730), "Human: intent / judgment / boundaries", font=F_BODY_SM, fill=MUTED)
    draw.text((1375, 780), "Agent: implementation / iteration / verification", font=F_BODY_SM, fill=CYAN)
    return img.convert("RGB")


def scene_04():
    img, draw = base(4, "agent-shaped repo", GOLD)
    left_claim(draw, "empty repository", ["仓库先被", "Agent 塑形"], GOLD, "不是先写完系统，再让 AI 适配。")
    stage(draw, "FIRST COMMIT: LATE AUGUST 2025", GOLD)
    nodes = [
        ((880, 438, 1060, 610), "Scaffold", "Codex + GPT-5"),
        ((1135, 438, 1315, 610), "Repo", "structure\npackages"),
        ((1390, 438, 1570, 610), "CI", "tests\nformat"),
        ((1645, 438, 1815, 610), "AGENTS.md", "agent rules"),
    ]
    for idx, (box, title, body) in enumerate(nodes):
        node(draw, box, title, body, GOLD, compact=True)
        if idx < len(nodes) - 1:
            arrow(draw, (box[2] + 12, 524), (nodes[idx + 1][0][0] - 14, 524), GOLD, 4)
    card(draw, (965, 720, 1730, 835), "结果", "仓库从第一天就面向 Agent 工作流设计", GOLD, fill=(30, 27, 20))
    return img.convert("RGB")


def scene_05():
    img, draw = base(5, "application legibility", CYAN)
    left_claim(draw, "chrome devtools mcp", ["让应用本身", "对 Codex 可见"], CYAN, "页面、DOM、导航和修复验证，都进入工具链。", small=True)
    stage(draw, "APP AS WORKBENCH", CYAN)
    panel(draw, (880, 245, 1320, 735), fill=(238, 236, 226), outline=(74, 74, 66), radius=26)
    draw.text((920, 285), "App UI", font=F_BODY_BOLD, fill=BG)
    draw.rounded_rectangle((920, 365, 1268, 420), radius=14, fill=(214, 218, 209))
    draw.rounded_rectangle((920, 455, 1180, 510), radius=14, fill=(214, 218, 209))
    draw.rounded_rectangle((920, 560, 1270, 650), radius=18, outline=CYAN, width=4)
    card(draw, (1435, 290, 1780, 675), "DevTools MCP", "screenshot()\nDOM snapshot\nnavigate()\nruntime events", CYAN, fill=(23, 28, 29))
    arrow(draw, (1328, 500), (1420, 500), CYAN, 5)
    card(draw, (1040, 790, 1640, 885), "Observe → Reproduce → Patch → Validate", "", OLIVE, fill=(24, 28, 24))
    return img.convert("RGB")


def scene_06():
    img, draw = base(6, "observability", OLIVE)
    left_claim(draw, "logs metrics traces", ["运行信号", "变成 Agent 工具"], OLIVE, "日志、指标、链路追踪，不只是给人看的仪表盘。")
    stage(draw, "TEMP LOCAL OBSERVABILITY STACK", OLIVE)
    node(draw, (870, 470, 1040, 615), "Worktree", "isolated app", OLIVE, compact=True)
    node(draw, (1110, 470, 1275, 615), "Vector", "fan-out", OLIVE, compact=True)
    node(draw, (1360, 278, 1528, 410), "Logs", "LogQL", OLIVE, compact=True)
    node(draw, (1360, 470, 1528, 602), "Metrics", "PromQL", OLIVE, compact=True)
    node(draw, (1360, 662, 1528, 794), "Traces", "TraceQL", OLIVE, compact=True)
    node(draw, (1638, 446, 1810, 640), "Codex", "query\nsignals", OLIVE, compact=True)
    arrow(draw, (1044, 542), (1098, 542), OLIVE, 4)
    arrow(draw, (1280, 542), (1348, 344), OLIVE, 3)
    arrow(draw, (1280, 542), (1348, 536), OLIVE, 3)
    arrow(draw, (1280, 542), (1348, 728), OLIVE, 3)
    arrow(draw, (1535, 344), (1625, 505), OLIVE, 3)
    arrow(draw, (1535, 536), (1625, 536), OLIVE, 3)
    arrow(draw, (1535, 728), (1625, 575), OLIVE, 3)
    draw.text((945, 850), "performance targets become executable tasks", font=F_BODY_SM, fill=MUTED)
    return img.convert("RGB")


def scene_07():
    img, draw = base(7, "repository knowledge", GOLD)
    left_claim(draw, "map not manual", ["AGENTS.md 是地图", "docs/ 是系统记录"], GOLD, "约一百行地图，指向版本化、可维护的知识库。", small=True)
    stage(draw, "KNOWLEDGE LAYOUT", GOLD)
    card(draw, (890, 360, 1150, 650), "AGENTS.md", "~100 lines\nnavigation map\nnot a giant manual", GOLD, fill=(30, 27, 20))
    arrow(draw, (1162, 505), (1250, 505), GOLD, 4)
    panel(draw, (1265, 240, 1795, 795), fill=(19, 21, 20), outline=blend_color(GOLD, FAINT, 0.42), radius=28)
    draw.text((1305, 282), "docs/", font=F_BODY_BOLD, fill=GOLD)
    rows = [
        ("Architecture", "ARCHITECTURE"),
        ("Plans", "PLANS / exec"),
        ("Product", "PRODUCT"),
        ("Quality", "QUALITY / SECURITY"),
        ("Design", "DESIGN / UI"),
    ]
    for idx, (name, body) in enumerate(rows):
        y = 350 + idx * 78
        panel(draw, (1308, y, 1752, y + 54), fill=(28, 29, 26), outline=(74, 68, 48), radius=14)
        draw.text((1330, y + 13), name, font=F_BODY_XS, fill=INK)
        draw.text((1495, y + 13), body, font=F_BODY_XS, fill=MUTED)
    card(draw, (1020, 840, 1700, 900), "CI + link checks + doc-gardening agent keep it fresh", "", GOLD, fill=(25, 25, 22), body_font=F_BODY_XS)
    return img.convert("RGB")


def scene_08():
    img, draw = base(8, "agent legibility", RED)
    left_claim(draw, "what cannot be seen", ["看不见的知识", "几乎等于不存在"], RED, "隐性知识必须进入仓库，才会稳定进入 Agent 上下文。", small=True)
    stage(draw, "VISIBLE KNOWLEDGE BOUNDARY", RED)
    card(draw, (1180, 410, 1490, 610), "Codex Context", "repo-local\nversioned\nverifiable", CYAN, fill=(23, 29, 30))
    sources = [
        ((890, 265, 1130, 410), "外部文档"),
        ((1540, 265, 1780, 410), "聊天讨论"),
        ((890, 675, 1130, 820), "隐性经验"),
        ((1540, 675, 1780, 820), "临时决策"),
    ]
    for box, title in sources:
        card(draw, box, title, "must enter repo", RED, fill=(30, 22, 22), title_font=F_LABEL)
        arrow(draw, ((box[0] + box[2]) // 2, (box[1] + box[3]) // 2), (1335, 510), RED, 3)
    return img.convert("RGB")


def scene_09():
    img, draw = base(9, "architecture invariants", CYAN)
    left_claim(draw, "enforce taste mechanically", ["工程品味", "要被机械化"], CYAN, "好的架构不能只靠口头提醒，要变成 lint、边界和错误信息。")
    stage(draw, "ARCHITECTURE INVARIANTS", CYAN)
    layers = ["Types", "Config", "Repo", "Service", "Runtime", "UI"]
    x = 885
    for idx, name in enumerate(layers):
        box = (x + idx * 148, 355, x + idx * 148 + 116, 485)
        node(draw, box, name, "", CYAN, compact=True)
        if idx < len(layers) - 1:
            arrow(draw, (box[2] + 8, 420), (x + (idx + 1) * 148 - 10, 420), CYAN, 3)
    card(draw, (905, 610, 1165, 770), "Blocked shortcut", "no direct cross-domain leap", RED, fill=(31, 22, 22), title_font=F_LABEL)
    card(draw, (1280, 610, 1760, 770), "Providers Boundary", "auth / connectors / telemetry / feature flags", BLUE, fill=(22, 25, 30), title_font=F_LABEL)
    draw.line((1040, 600, 1515, 492), fill=(*RED, 190), width=5)
    draw.text((950, 840), "lint messages carry remediation back into agent context", font=F_BODY_SM, fill=MUTED)
    return img.convert("RGB")


def scene_10():
    img, draw = base(10, "merge philosophy", BLUE)
    left_claim(draw, "throughput changes process", ["修正成本变低", "等待成本变高"], BLUE, "高吞吐会改变合并策略，但低吞吐团队不能照搬。")
    stage(draw, "MERGE STRATEGY SHIFT", BLUE)
    card(draw, (900, 285, 1210, 520), "Fix Cost", "cheaper with\nfast agents", OLIVE, fill=(22, 29, 23))
    card(draw, (1450, 285, 1760, 520), "Waiting Cost", "expensive when flow stalls", RED, fill=(31, 22, 22))
    arrow(draw, (1225, 405), (1428, 405), BLUE, 5)
    for x, text in [(940, "short-lived PRs"), (1205, "fewer blocking gates"), (1510, "flaky fixed later")]:
        pill(draw, (x, 660), text, BLUE)
    card(draw, (980, 790, 1680, 880), "Caveat: high throughput required.", "", GOLD, fill=(29, 27, 21))
    return img.convert("RGB")


def scene_11():
    img, draw = base(11, "agent-generated scope", OLIVE)
    left_claim(draw, "everything in the repo", ["Agent-generated", "不只是业务代码"], OLIVE, "测试、工具、CI、文档、评审，也会成为生成对象。", small=True)
    stage(draw, "GENERATION SURFACE AREA", OLIVE)
    items = [
        ((900, 255, 1265, 390), "代码 / 测试", "business logic · evaluations"),
        ((1360, 255, 1725, 390), "工具 / CI", "release tooling · scripts"),
        ((900, 525, 1265, 660), "文档 / 评审", "design history · review comments"),
        ((1360, 525, 1725, 660), "仪表盘 / 管理", "dashboards · repo management"),
    ]
    for box, title, body in items:
        card(draw, box, title, body, OLIVE, fill=(23, 28, 23))
    draw.text((1000, 805), "The whole development system becomes generatable.", font=F_BODY_SM, fill=MUTED)
    return img.convert("RGB")


def scene_12():
    img, draw = base(12, "autonomy loop", CYAN)
    left_claim(draw, "one prompt to merged change", ["自治不是魔法", "是闭环"], CYAN, "工具、验证、反馈和升级路径，共同组成端到端工作流。")
    stage(draw, "END-TO-END AUTONOMY LOOP", CYAN)
    center = (1340, 525)
    positions = [
        (1050, 260, "Check", "state"),
        (1320, 230, "Bug", "video"),
        (1585, 300, "Patch", "fix"),
        (1640, 520, "Test", "app"),
        (1510, 735, "PR", "change"),
        (1245, 765, "Feedback", "build"),
        (980, 690, "Escalate", "human"),
        (930, 470, "Merge", "land"),
    ]
    boxes = []
    for x, y, title, body in positions:
        box = (x, y, x + 166, y + 132)
        boxes.append(box)
        node(draw, box, title, body, CYAN, compact=True)
    for a, b in zip(boxes, boxes[1:] + boxes[:1]):
        arrow(draw, ((a[0] + a[2]) // 2, (a[1] + a[3]) // 2), ((b[0] + b[2]) // 2, (b[1] + b[3]) // 2), CYAN, 2, 155)
    panel(draw, (1240, 445, 1460, 600), fill=(22, 28, 29), outline=CYAN, radius=999)
    draw.text((1290, 490), "loop", font=F_STAT_SM, fill=CYAN)
    return img.convert("RGB")


def scene_13():
    img, draw = base(13, "entropy control", GOLD)
    left_claim(draw, "garbage collection", ["熵也要", "被治理"], GOLD, "Agent 会放大模式，好坏都会放大。")
    stage(draw, "ENTROPY MANAGEMENT", GOLD)
    card(draw, (900, 295, 1215, 540), "旧办法", "Friday cleanup\n20% time\nAI slop removal", RED, fill=(31, 22, 22))
    card(draw, (1460, 295, 1775, 540), "新办法", "golden principles\nbackground Codex\nsmall refactor PRs", GOLD, fill=(30, 27, 20))
    arrow(draw, (1230, 417), (1445, 417), GOLD, 5)
    principles = [
        "shared utilities > hand-rolled helpers",
        "no YOLO data probing",
        "typed SDKs and validated boundaries",
        "scan deviations → quality grades → refactor PRs",
    ]
    panel(draw, (940, 655, 1735, 855), fill=(22, 23, 21), outline=blend_color(GOLD, FAINT, 0.45), radius=24)
    for idx, item in enumerate(principles):
        y = 692 + idx * 40
        draw.text((980, y), f"{idx + 1:02d}", font=F_META, fill=GOLD)
        draw.text((1035, y - 4), item, font=F_BODY_XS, fill=INK)
    return img.convert("RGB")


def scene_14():
    img, draw = base(14, "final compression", CYAN)
    left_claim(draw, "the real lesson", ["模型负责生成", "Harness 负责治理"], CYAN, "企业真正需要的不是更炫的 demo，而是 AI 基础设施。")
    stage(draw, "FINAL MODEL", CYAN)
    card(draw, (900, 360, 1210, 610), "Model", "generates code\nand artifacts", OLIVE, fill=(22, 29, 23))
    card(draw, (1450, 360, 1760, 610), "Harness", "visibility\ncontrol\nverification\nmaintenance", CYAN, fill=(22, 28, 29))
    arrow(draw, (1225, 485), (1428, 485), CYAN, 5)
    for x, text, color in [(930, "可见", OLIVE), (1110, "可控", GOLD), (1290, "可验证", CYAN), (1505, "可维护", BLUE)]:
        pill(draw, (x, 755), text, color)
    card(draw, (970, 855, 1705, 915), "Still learning: consistency.", "", GOLD, fill=(28, 27, 23))
    return img.convert("RGB")


SCENES = [
    scene_01,
    scene_02,
    scene_03,
    scene_04,
    scene_05,
    scene_06,
    scene_07,
    scene_08,
    scene_09,
    scene_10,
    scene_11,
    scene_12,
    scene_13,
    scene_14,
]

BEATS = [
    {"scene": scene_01, "caption": "别只看那一百万行代码", "boxes": [(92, 270, 720, 468)], "accent": CYAN, "duration_hint": 3.0},
    {"scene": scene_01, "caption": "关键：软件工程变成智能体生产环境", "boxes": [(900, 255, 1750, 520)], "accent": CYAN, "duration_hint": 4.0},
    {"scene": scene_01, "caption": "Harness Engineering：可见、可控、可验证", "boxes": [(940, 650, 1790, 800)], "accent": OLIVE, "duration_hint": 4.0},
    {"scene": scene_02, "caption": "这不是 demo：从真实产品开始", "boxes": [(92, 278, 720, 486), (1360, 455, 1805, 635)], "accent": OLIVE, "duration_hint": 2.2},
    {"scene": scene_02, "caption": "0 行人工手写代码", "boxes": [(870, 210, 1088, 390)], "accent": BLUE, "duration_hint": 2.6},
    {"scene": scene_02, "caption": "5 个月：约 1M 行代码，约 1,500 PR", "boxes": [(1115, 210, 1578, 390), (1605, 210, 1805, 390)], "accent": OLIVE, "duration_hint": 3.5},
    {"scene": scene_02, "caption": "OpenAI 估计：约 1/10 手写时间", "boxes": [(870, 455, 1088, 635)], "accent": RED, "duration_hint": 3.0},
    {"scene": scene_02, "caption": "3 位工程师：每人每天 3.5 个 PR", "boxes": [(1115, 455, 1333, 635)], "accent": CYAN, "duration_hint": 3.4},
    {"scene": scene_02, "caption": "7 位工程师后吞吐继续上升，还有真实用户", "boxes": [(1360, 455, 1805, 635)], "accent": BLUE, "duration_hint": 4.0},
    {"scene": scene_03, "caption": "关键不是代码量，而是角色变了", "boxes": [(92, 278, 720, 470)], "accent": CYAN, "duration_hint": 2.6},
    {"scene": scene_03, "caption": "人类掌舵，智能体执行", "boxes": [(900, 310, 1760, 620)], "accent": CYAN, "duration_hint": 2.3},
    {"scene": scene_04, "caption": "第一层：仓库先被智能体塑形", "boxes": [(92, 278, 720, 470)], "accent": GOLD, "duration_hint": 2.6},
    {"scene": scene_04, "caption": "Codex CLI + GPT-5 生成初始 scaffold", "boxes": [(880, 438, 1060, 610)], "accent": GOLD, "duration_hint": 3.0},
    {"scene": scene_04, "caption": "结构、CI、格式化、包管理、应用框架", "boxes": [(1135, 438, 1570, 610)], "accent": GOLD, "duration_hint": 4.0},
    {"scene": scene_04, "caption": "甚至 AGENTS.md 也由 Codex 写", "boxes": [(1645, 438, 1815, 610)], "accent": GOLD, "duration_hint": 2.5},
    {"scene": scene_05, "caption": "第二层：让应用对智能体可见", "boxes": [(92, 278, 720, 470)], "accent": CYAN, "duration_hint": 2.4},
    {"scene": scene_05, "caption": "每个 git worktree 启动独立应用", "boxes": [(880, 245, 1320, 735)], "accent": CYAN, "duration_hint": 2.4},
    {"scene": scene_05, "caption": "DevTools：截图、读页面、导航", "boxes": [(1435, 290, 1780, 675)], "accent": CYAN, "duration_hint": 3.8},
    {"scene": scene_05, "caption": "复现问题，再验证修复", "boxes": [(1040, 790, 1640, 885)], "accent": OLIVE, "duration_hint": 2.5},
    {"scene": scene_05, "caption": "界面变成智能体工作台", "boxes": [(880, 245, 1780, 885)], "accent": CYAN, "duration_hint": 2.2},
    {"scene": scene_06, "caption": "第三层：让运行信号可见", "boxes": [(92, 278, 720, 470)], "accent": OLIVE, "duration_hint": 2.0},
    {"scene": scene_06, "caption": "每个 worktree 有临时本地观测栈", "boxes": [(870, 470, 1040, 615)], "accent": OLIVE, "duration_hint": 2.7},
    {"scene": scene_06, "caption": "Vector 汇入日志、指标、链路追踪", "boxes": [(1110, 278, 1528, 794)], "accent": OLIVE, "duration_hint": 3.0},
    {"scene": scene_06, "caption": "Codex 用 LogQL、PromQL、TraceQL 查询", "boxes": [(1638, 446, 1810, 640)], "accent": OLIVE, "duration_hint": 2.8},
    {"scene": scene_06, "caption": "性能目标变成可执行任务", "boxes": [(930, 832, 1630, 885)], "accent": OLIVE, "duration_hint": 4.0},
    {"scene": scene_06, "caption": "有些 Codex 任务可连续工作 6 小时以上", "boxes": [(1638, 446, 1810, 640)], "accent": GOLD, "duration_hint": 2.2},
    {"scene": scene_07, "caption": "第四层：把组织知识写进仓库", "boxes": [(92, 278, 742, 500)], "accent": GOLD, "duration_hint": 2.4},
    {"scene": scene_07, "caption": "巨大的 AGENTS.md 会浪费上下文", "boxes": [(890, 360, 1150, 650)], "accent": RED, "duration_hint": 3.0},
    {"scene": scene_07, "caption": "AGENTS.md 只做约 100 行地图", "boxes": [(890, 360, 1150, 650)], "accent": GOLD, "duration_hint": 2.6},
    {"scene": scene_07, "caption": "docs/ 才是版本化系统记录", "boxes": [(1265, 240, 1795, 795)], "accent": GOLD, "duration_hint": 4.2},
    {"scene": scene_07, "caption": "CI、链接检查、文档维护 agent 保持新鲜", "boxes": [(1020, 840, 1700, 900)], "accent": GOLD, "duration_hint": 3.2},
    {"scene": scene_08, "caption": "智能体看不见的知识，几乎等于不存在", "boxes": [(92, 278, 742, 500)], "accent": RED, "duration_hint": 3.2},
    {"scene": scene_08, "caption": "外部文档、聊天、隐性经验必须进入仓库", "boxes": [(890, 265, 1780, 820)], "accent": RED, "duration_hint": 3.0},
    {"scene": scene_09, "caption": "第五层：把工程品味机械化", "boxes": [(92, 278, 720, 470)], "accent": CYAN, "duration_hint": 2.5},
    {"scene": scene_09, "caption": "业务域只能沿固定顺序依赖", "boxes": [(885, 355, 1741, 485)], "accent": CYAN, "duration_hint": 2.5},
    {"scene": scene_09, "caption": "跨领域能力必须通过 Providers", "boxes": [(1280, 610, 1760, 770)], "accent": BLUE, "duration_hint": 2.4},
    {"scene": scene_09, "caption": "边界解析、结构化日志、命名和文件大小都能检查", "boxes": [(885, 355, 1760, 770)], "accent": CYAN, "duration_hint": 4.0},
    {"scene": scene_09, "caption": "lint 错误会把修复指导注入上下文", "boxes": [(905, 610, 1760, 850)], "accent": RED, "duration_hint": 2.5},
    {"scene": scene_10, "caption": "约束不是减速器，是防止速度变混乱的加速器", "boxes": [(92, 278, 720, 500)], "accent": BLUE, "duration_hint": 3.4},
    {"scene": scene_10, "caption": "第六层：吞吐量改变合并策略", "boxes": [(92, 278, 720, 470)], "accent": BLUE, "duration_hint": 2.4},
    {"scene": scene_10, "caption": "短生命周期 PR，更少阻塞式 gate，flaky 后续修", "boxes": [(920, 645, 1760, 725)], "accent": BLUE, "duration_hint": 4.0},
    {"scene": scene_10, "caption": "高吞吐下修正便宜、等待昂贵；低吞吐别照搬", "boxes": [(900, 285, 1760, 880)], "accent": GOLD, "duration_hint": 3.5},
    {"scene": scene_11, "caption": "Agent-generated 不只是业务代码", "boxes": [(92, 278, 742, 500)], "accent": OLIVE, "duration_hint": 2.8},
    {"scene": scene_11, "caption": "代码、测试、工具、CI、文档、评审都进入系统", "boxes": [(900, 255, 1725, 660)], "accent": OLIVE, "duration_hint": 3.2},
    {"scene": scene_12, "caption": "最后形成端到端闭环", "boxes": [(92, 278, 720, 470)], "accent": CYAN, "duration_hint": 2.0},
    {"scene": scene_12, "caption": "验证状态、复现 bug、录制失败视频", "boxes": [(1050, 230, 1486, 392)], "accent": CYAN, "duration_hint": 3.0},
    {"scene": scene_12, "caption": "修复、验证、录制修复视频、提交代码合并请求", "boxes": [(1510, 300, 1806, 867)], "accent": OLIVE, "duration_hint": 4.0},
    {"scene": scene_12, "caption": "回应反馈、修构建、判断时升级给人类、合并", "boxes": [(930, 470, 1411, 897)], "accent": CYAN, "duration_hint": 3.8},
    {"scene": scene_12, "caption": "这依赖工具和结构，不能直接复制", "boxes": [(930, 230, 1806, 897)], "accent": RED, "duration_hint": 2.6},
    {"scene": scene_13, "caption": "而熵也要被治理", "boxes": [(92, 278, 720, 470)], "accent": GOLD, "duration_hint": 2.2},
    {"scene": scene_13, "caption": "旧办法：每周五 20% 时间清理 AI 垃圾代码", "boxes": [(900, 295, 1215, 540)], "accent": RED, "duration_hint": 3.0},
    {"scene": scene_13, "caption": "golden principles：共享工具，不猜数据", "boxes": [(940, 655, 1735, 815)], "accent": GOLD, "duration_hint": 4.2},
    {"scene": scene_13, "caption": "后台 Codex 扫描偏差、更新质量分、开小型重构请求", "boxes": [(1460, 295, 1775, 855)], "accent": OLIVE, "duration_hint": 3.6},
    {"scene": scene_13, "caption": "这就像垃圾回收", "boxes": [(1460, 295, 1775, 540)], "accent": GOLD, "duration_hint": 2.0},
    {"scene": scene_14, "caption": "这不是 AI 写代码，而是 Harness Engineering", "boxes": [(92, 278, 720, 500)], "accent": CYAN, "duration_hint": 2.8},
    {"scene": scene_14, "caption": "模型负责生成，Harness 负责治理", "boxes": [(900, 360, 1760, 610)], "accent": CYAN, "duration_hint": 2.8},
    {"scene": scene_14, "caption": "让生成结果可见、可控、可验证、可维护", "boxes": [(900, 735, 1655, 810)], "accent": OLIVE, "duration_hint": 2.8},
    {"scene": scene_14, "caption": "OpenAI 仍在学习长期一致性和人类判断位置", "boxes": [(970, 855, 1705, 915)], "accent": GOLD, "duration_hint": 3.6},
    {"scene": scene_14, "caption": "企业智能体真正需要的是基础设施", "boxes": [(900, 360, 1760, 915)], "accent": CYAN, "duration_hint": 2.5},
]

BEAT_VOICE_TEXTS = [
    "别只盯着那一百万行代码。",
    "关键是，研发流程变成 Codex 能执行、能检查的环境。",
    "这就是 Harness Engineering：让 AI 做事，也让结果可检查。",
    "它不是演示，而是从零开始的内部产品。",
    "这些代码不是一行一行手写出来的。",
    "项目做了五个月，产出大约一百万行代码，一千五百个代码合并请求。",
    "OpenAI 说，速度大约是手写方式的十倍。",
    "最早只有三位工程师，平均每人每天三点五个代码合并请求。",
    "后来团队变成七个人，使用的人也越来越多。",
    "重点不是代码更多，而是分工变了。",
    "人类决定方向，Codex 负责执行。",
    "第一步，先让仓库适合 AI。",
    "最开始的脚手架，是 Codex 和 GPT-5 生成的。",
    "目录结构、持续集成、格式化和包管理，先一起搭好。",
    "AGENTS.md 这种说明文件，也由 Codex 写。",
    "第二步，让应用对 AI 可见。",
    "每个独立工作区，都能跑一个应用。",
    "接入 Chrome DevTools 之后，Codex 能看到页面。",
    "它能复现问题，也能验证修复。",
    "这时，界面就是 AI 的工作台。",
    "第三步，让运行状态可见。",
    "每个独立工作区，都有临时观测系统。",
    "日志、指标、链路追踪，都会进入系统。",
    "Codex 可以自己查询这些信号。",
    "启动时间、慢链路，都能变成任务。",
    "有些任务，Codex 可以连续做六小时以上。",
    "第四步，把组织知识放进仓库。",
    "说明文件太大，会浪费上下文。",
    "所以它只保留一百行左右的地图。",
    "详细知识放进文档目录。",
    "检查、持续集成和维护智能体，负责保持更新。",
    "AI 看不见的知识，基本就用不上。",
    "聊天、经验、外部文档，都要进入仓库。",
    "第五步，把工程品味变成规则。",
    "业务模块，按照固定顺序依赖。",
    "跨领域能力，统一通过 Providers。",
    "边界要验证，日志要结构化。",
    "错误信息会告诉智能体怎么修。",
    "规则不是刹车，是防止速度失控。",
    "第六步，合并策略也要改变。",
    "代码合并请求更短，门禁更少，反馈更快。",
    "高吞吐团队可以快修；低吞吐团队不能照搬。",
    "AI 生成的范围，不止业务代码。",
    "测试、工具、持续集成、文档、评审，也能生成。",
    "最后，它形成一个闭环。",
    "Codex 先确认状态，再复现问题。",
    "然后修复、验证、录视频、提交代码合并请求。",
    "反馈和构建失败，它先处理；需要判断，再找人。",
    "但这依赖工具和结构，不能直接复制。",
    "系统混乱，也必须被治理。",
    "旧办法，是每周五拿出百分之二十时间，清理 AI 垃圾代码。",
    "新办法，叫 golden principles，也就是一组黄金原则。",
    "后台 Codex 会扫描问题，开小型重构请求。",
    "这就像一套垃圾回收系统。",
    "所以重点不是 AI 写代码，而是 Harness Engineering。",
    "模型负责生成，Harness 负责治理。",
    "结果要看得见、管得住、能验证、能维护。",
    "OpenAI 也还在学习，长期问题怎么处理。",
    "企业真正需要的，其实是这种 AI 基础设施。",
]

if len(BEATS) != len(BEAT_VOICE_TEXTS):
    raise RuntimeError(f"BEATS count {len(BEATS)} != voice text count {len(BEAT_VOICE_TEXTS)}")

for beat, voice_text in zip(BEATS, BEAT_VOICE_TEXTS):
    beat["voice"] = voice_text


def write_storyboard(frame_paths, beats=None):
    cards = []
    for i, path in enumerate(frame_paths, start=1):
        rel = path.relative_to(ROOT)
        caption = beats[i - 1]["caption"] if beats and i - 1 < len(beats) else f"Scene {i:02d}"
        cards.append(
            f'<figure><img src="{html.escape(str(rel))}" alt="beat {i:02d}"><figcaption>{html.escape(caption)}</figcaption></figure>'
        )
    doc = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>OpenAI Codex Harness Engineering Storyboard</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #0b0c0c;
      --panel: #181917;
      --ink: #f6f2e8;
      --muted: #a39e92;
      --accent: #76cbd6;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: radial-gradient(circle at 18% 8%, rgba(118,203,214,.14), transparent 30%), var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Hiragino Sans GB", sans-serif;
    }}
    header {{
      max-width: 1320px;
      margin: 0 auto;
      padding: 56px 28px 28px;
    }}
    .eyebrow {{ color: var(--accent); font-size: 13px; letter-spacing: .18em; text-transform: uppercase; font-family: ui-monospace, monospace; }}
    h1 {{ margin: 14px 0 12px; font-family: Georgia, "Songti SC", serif; font-size: clamp(34px, 5vw, 72px); line-height: .96; font-weight: 500; }}
    p {{ color: var(--muted); max-width: 880px; font-size: 18px; line-height: 1.6; }}
    main {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 22px;
      max-width: 1320px;
      margin: 0 auto;
      padding: 20px 28px 72px;
    }}
    figure {{
      margin: 0;
      padding: 12px;
      background: linear-gradient(180deg, rgba(255,255,255,.055), rgba(255,255,255,.018));
      border: 1px solid rgba(255,255,255,.08);
      border-radius: 22px;
    }}
    img {{ width: 100%; display: block; border-radius: 15px; }}
    figcaption {{ padding: 10px 4px 2px; color: var(--muted); font-size: 13px; }}
  </style>
</head>
<body>
  <header>
    <div class="eyebrow">native 16:9 · executive technical documentary</div>
    <h1>OpenAI Codex Harness Engineering</h1>
    <p>Widescreen storyboard rebuilt from the source article and existing timing. Each beat keeps the same voice text while the active visual element is highlighted with a soft dynamic focus.</p>
  </header>
  <main>
    {''.join(cards)}
  </main>
</body>
</html>
"""
    (ROOT / "storyboard.html").write_text(doc, encoding="utf-8")


def write_frame_manifest(entries):
    FRAME_MANIFEST.write_text(
        json.dumps(
            {
                "phase_count": PHASES_PER_BEAT,
                "timing_source": "beat_audio_manifest" if AUDIO_MANIFEST.exists() else "duration_hint",
                "frames": entries,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def load_audio_durations():
    if not AUDIO_MANIFEST.exists():
        return {}
    manifest = json.loads(AUDIO_MANIFEST.read_text(encoding="utf-8"))
    return {int(item["beat"]): float(item["audio_duration"]) for item in manifest.get("beats", [])}


def main():
    for old_frame in FRAMES.glob("scene_*.png"):
        old_frame.unlink()
    if FRAME_MANIFEST.exists():
        FRAME_MANIFEST.unlink()

    paths = []
    key_paths = []
    manifest_entries = []
    audio_durations = load_audio_durations()
    for i, beat in enumerate(BEATS, start=1):
        base_image = beat["scene"]()
        focus_boxes = beat.get("boxes", [])
        if i in audio_durations:
            beat["audio_duration"] = audio_durations[i]
        beat_duration = duration_hint(beat)
        for phase_idx in range(PHASES_PER_BEAT):
            phase = phase_idx / max(1, PHASES_PER_BEAT - 1)
            image = focus_overlay(
                base_image.copy(),
                beat["caption"],
                boxes=focus_boxes,
                accent=beat.get("accent", CYAN),
                beat=i,
                phase=phase,
                phase_idx=phase_idx,
            )
            path = FRAMES / f"scene_{i:02d}_{phase_idx:02d}.png"
            image.save(path, quality=94)
            paths.append(path)
            if phase_idx == PHASES_PER_BEAT - 1:
                key_paths.append(path)
            manifest_entries.append(
                {
                    "file": str(path.relative_to(ROOT)),
                    "beat": i,
                    "phase": phase_idx + 1,
                    "caption": beat["caption"],
                    "voice": beat["voice"],
                    "duration_hint": beat_duration * PHASE_DURATION_WEIGHTS[phase_idx],
                }
            )
    Image.open(key_paths[0]).save(ROOT / "cover.png", quality=94)
    preview_frames = [Image.open(path).resize((640, 360), Image.Resampling.LANCZOS) for path in key_paths]
    preview_frames[0].save(
        ROOT / "storyboard.gif",
        save_all=True,
        append_images=preview_frames[1:],
        duration=900,
        loop=0,
    )
    write_frame_manifest(manifest_entries)
    write_storyboard(key_paths, BEATS)
    print(f"wrote {len(paths)} native 16:9 phased frames, {len(key_paths)} storyboard beats, cover, timing manifest")


if __name__ == "__main__":
    main()
