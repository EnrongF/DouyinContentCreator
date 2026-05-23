from __future__ import annotations

import html
import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
FRAMES = ROOT / "frames"
W, H = 1920, 1080

FONT_SANS = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_SERIF = "/System/Library/Fonts/Supplemental/Songti.ttc"

BG = (7, 9, 10)
INK = (245, 240, 230)
MUTED = (168, 160, 145)
QUIET = (104, 111, 112)
CYAN = (122, 212, 223)
GOLD = (221, 182, 95)
RED = (225, 92, 82)
BLUE = (142, 178, 224)
PANEL = (24, 28, 29)
PANEL_2 = (34, 39, 40)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


SANS_22 = font(FONT_SANS, 22)
SANS_28 = font(FONT_SANS, 28)
SANS_34 = font(FONT_SANS, 34)
SANS_40 = font(FONT_SANS, 40)
SANS_48 = font(FONT_SANS, 48)
SANS_58 = font(FONT_SANS, 58)
SANS_72 = font(FONT_SANS, 72)
SERIF_80 = font(FONT_SERIF, 80)
SERIF_96 = font(FONT_SERIF, 96)


SCENES = [
    {
        "kicker": "WRONG FIRST QUESTION",
        "headline": "别先问\n能不能做多智能体",
        "note": "业务用户真正该问：这个问题到底需不需要 Agent？",
        "subtitle": "很多企业做 Agent，第一步就问错了：他们先问能不能做多智能体。",
        "artifact": "wrong_question",
        "duration": 8.0,
    },
    {
        "kicker": "AGENTIC FIT",
        "headline": "Agent 适合\n路径不固定的问题",
        "note": "开放目标、工具使用、动态决策、反馈迭代，才是 Agent 的核心特征。",
        "subtitle": "Agent 真正适合的是：路径不固定，需要调用工具，需要根据反馈调整，还要持续推进目标。",
        "artifact": "traits",
        "duration": 11.0,
    },
    {
        "kicker": "DO NOT OVERBUILD",
        "headline": "流程清楚\n就别急着上 Agent",
        "note": "固定格式抽取、普通问答、标准报表，通常用增强型 LLM 或 Workflow 更稳。",
        "subtitle": "如果流程很清楚，规则也稳定，你需要的可能只是自动化，或者一个 Workflow。",
        "artifact": "low_risk",
        "duration": 10.0,
    },
    {
        "kicker": "CONTROLLED PROCESS",
        "headline": "步骤清楚\n但需要控制",
        "note": "审批、合规检查、内容发布链路，更适合 Sequential Workflow。",
        "subtitle": "步骤清楚但需要控制时，适合 Sequential Workflow，因为你知道每一步，也需要留下过程。",
        "artifact": "workflow",
        "duration": 10.0,
    },
    {
        "kicker": "SINGLE AGENT",
        "headline": "目标清楚\n路径不清楚",
        "note": "客户问题排查、市场研究、代码库理解、数据分析，可以从 Single Agent 开始。",
        "subtitle": "目标清楚但路径不清楚时，可以用 Single Agent：它计划、调用工具、观察结果，再继续调整。",
        "artifact": "single_agent",
        "duration": 12.0,
    },
    {
        "kicker": "MULTI-DOMAIN WORK",
        "headline": "跨多个领域\n才考虑 Multi-Agent",
        "note": "贷款风险评估要看信用、市场、运营、合规，这时不同 Agent 的专业视角有价值。",
        "subtitle": "问题跨多个领域时，Multi-Agent 才有意义：不同 Agent 负责不同专业视角，最后再汇总。",
        "artifact": "multi_agent",
        "duration": 13.0,
    },
    {
        "kicker": "REAL COST",
        "headline": "多 Agent\n不是默认选项",
        "note": "成本更高、延迟更长、调试更难。复杂度必须由业务价值证明。",
        "subtitle": "多 Agent 的代价很真实：成本更高、延迟更长、调试更难。它不是默认选项。",
        "artifact": "costs",
        "duration": 10.0,
    },
    {
        "kicker": "PRODUCTION HARNESS",
        "headline": "碰真实系统\n必须加 Harness",
        "note": "CRM、订单、支付、审批、数据库，都需要权限、日志、评估、回滚和人工接管。",
        "subtitle": "当 Agent 要碰真实业务系统，重点不再是 Agent 本身，而是权限、日志、评估、回滚和人工接管。",
        "artifact": "harness",
        "duration": 13.0,
    },
    {
        "kicker": "DECISION MATRIX",
        "headline": "业务选型\n看四个变量",
        "note": "流程是否固定、风险是否可控、是否跨领域、成本和治理能力是否足够。",
        "subtitle": "给业务团队的选择框架很简单：流程是否固定，风险是否可控，是否跨领域，治理能力是否足够。",
        "artifact": "matrix",
        "duration": 12.0,
    },
    {
        "kicker": "ARCHITECTURE LADDER",
        "headline": "从小架构\n逐级加复杂度",
        "note": "Automation → Workflow → Single Agent → Multi-Agent → Harnessed System。",
        "subtitle": "先用最小架构解决真实业务问题，再逐步从 Workflow 到 Single Agent，再到 Multi-Agent 和 Harness。",
        "artifact": "ladder",
        "duration": 12.0,
    },
    {
        "kicker": "FINAL PRINCIPLE",
        "headline": "成熟系统\n不是更复杂",
        "note": "而是复杂度刚好够用。",
        "subtitle": "真正成熟的 Agent 项目，不是更复杂，而是复杂度刚好够用。",
        "artifact": "final",
        "duration": 8.0,
    },
]


def draw_text(draw: ImageDraw.ImageDraw, xy, text, fnt, fill=INK, spacing=12, anchor=None):
    draw.multiline_text(xy, text, font=fnt, fill=fill, spacing=spacing, anchor=anchor)


def text_box(draw, xy, text, fnt, fill=INK, width=18, line_spacing=8, anchor=None):
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=width) or [""])
    draw.multiline_text(xy, "\n".join(lines), font=fnt, fill=fill, spacing=line_spacing, anchor=anchor)


def rounded(draw, box, fill, outline=(255, 255, 255, 36), radius=28, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def base(scene_idx: int, scene: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-260, -120, 780, 720), fill=(*CYAN, 28))
    gd.ellipse((1320, 520, 2220, 1320), fill=(*GOLD, 20))
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    img = Image.alpha_composite(img.convert("RGBA"), glow)
    draw = ImageDraw.Draw(img, "RGBA")

    draw.rectangle((92, 150, 1828, 151), fill=(245, 240, 230, 34))
    draw.text((92, 66), "AI COGNITION COMPRESSION", font=SANS_22, fill=(*MUTED, 230))
    draw.text((92, 102), "Building Effective AI Agents", font=SANS_28, fill=(*INK, 230))
    draw.text((820, 76), f"{scene_idx:02d}/{len(SCENES):02d}", font=SANS_34, fill=(*CYAN, 245))
    draw.text((930, 84), "BUSINESS IMPLEMENTATION GUIDE", font=SANS_22, fill=(*MUTED, 220))

    draw.text((92, 216), scene["kicker"], font=SANS_28, fill=(*CYAN, 245))
    draw.rectangle((92, 264, 232, 267), fill=(*CYAN, 240))
    draw_text(draw, (92, 316), scene["headline"], SERIF_96, fill=INK, spacing=2)
    text_box(draw, (92, 585), scene["note"], SANS_40, fill=MUTED, width=17, line_spacing=14)

    rounded(draw, (820, 116, 1830, 870), fill=(*PANEL, 238), outline=(*INK, 34), radius=34)
    draw.text((865, 160), "ARCHITECTURE ARTIFACT", font=SANS_22, fill=(*CYAN, 230))

    # Burned-in subtitle.
    rounded(draw, (360, 900, 1560, 1000), fill=(4, 6, 7, 190), outline=(*INK, 40), radius=24)
    text_box(draw, (960, 928), scene["subtitle"], SANS_40, fill=(255, 249, 235), width=31, line_spacing=6, anchor="ma")
    return img.convert("RGB")


def card(draw, box, title, body="", accent=CYAN):
    rounded(draw, box, fill=(*PANEL_2, 245), outline=(*accent, 150), radius=24)
    x1, y1, x2, y2 = box
    draw.text((x1 + 24, y1 + 22), title, font=SANS_34, fill=(*accent, 245))
    if body:
        text_box(draw, (x1 + 24, y1 + 74), body, SANS_28, fill=MUTED, width=14, line_spacing=8)


def artifact(img: Image.Image, scene: dict):
    draw = ImageDraw.Draw(img, "RGBA")
    a = scene["artifact"]
    x0, y0 = 820, 116

    if a == "wrong_question":
        card(draw, (930, 300, 1260, 500), "错误问题", "能不能做\n多智能体？", RED)
        card(draw, (1390, 300, 1720, 500), "正确问题", "业务问题\n是否需要 Agent？", CYAN)
        draw.line((1285, 400, 1360, 400), fill=(*CYAN, 230), width=5)
        draw.polygon([(1360, 400), (1338, 386), (1338, 414)], fill=(*CYAN, 230))
    elif a == "traits":
        items = [("路径开放", "不能完全预写步骤"), ("工具使用", "连接真实系统"), ("反馈调整", "观察结果再行动"), ("持续推进", "直到目标完成")]
        for i, (t, b) in enumerate(items):
            card(draw, (900 + (i % 2) * 430, 260 + (i // 2) * 220, 1250 + (i % 2) * 430, 430 + (i // 2) * 220), t, b, CYAN)
    elif a == "low_risk":
        card(draw, (900, 290, 1240, 510), "固定流程", "抽取 / 问答\n标准报表", GOLD)
        card(draw, (1370, 290, 1710, 510), "别上 Agent", "Workflow\n更稳更便宜", RED)
        draw.line((1245, 400, 1350, 400), fill=(*GOLD, 220), width=5)
    elif a == "workflow":
        labels = ["输入", "分类", "审核", "发布", "留痕"]
        for i, lab in enumerate(labels):
            bx = 890 + i * 175
            card(draw, (bx, 360, bx + 130, 480), lab, "", CYAN)
            if i < len(labels) - 1:
                draw.line((bx + 132, 420, bx + 170, 420), fill=(*CYAN, 230), width=4)
    elif a == "single_agent":
        cx, cy, r = 1325, 455, 230
        steps = [("感知", 1325, 220), ("计划", 1555, 455), ("行动", 1325, 690), ("观察", 1095, 455)]
        draw.ellipse((cx-r, cy-r, cx+r, cy+r), outline=(*CYAN, 180), width=5)
        for t, x, y in steps:
            card(draw, (x-80, y-54, x+80, y+54), t, "", CYAN)
        card(draw, (1180, 402, 1470, 510), "Single Agent", "一个循环\n持续推进", GOLD)
    elif a == "multi_agent":
        roles = [("信用", 980, 260), ("市场", 1440, 260), ("运营", 980, 570), ("合规", 1440, 570)]
        for t, x, y in roles:
            card(draw, (x-120, y-70, x+120, y+70), t, "专业视角", CYAN)
            draw.line((x, y + 78, 1325, 500), fill=(*CYAN, 120), width=3)
        card(draw, (1190, 430, 1460, 570), "汇总决策", "综合风险", GOLD)
    elif a == "costs":
        card(draw, (930, 280, 1230, 520), "收益", "复杂任务\n多视角覆盖", CYAN)
        card(draw, (1420, 230, 1720, 570), "代价", "成本↑\n延迟↑\n调试难度↑", RED)
        draw.text((1035, 655), "只有业务价值超过复杂度，才升级。", font=SANS_48, fill=(*INK, 240))
    elif a == "harness":
        card(draw, (1190, 360, 1460, 520), "Agent", "推理与行动", CYAN)
        rings = [("权限", 1040, 230), ("日志", 1520, 230), ("评估", 1040, 660), ("回滚", 1520, 660)]
        for t, x, y in rings:
            card(draw, (x-95, y-55, x+95, y+55), t, "", GOLD)
            draw.line((x, y, 1325, 440), fill=(*GOLD, 120), width=3)
        draw.ellipse((1090, 220, 1560, 690), outline=(*GOLD, 150), width=5)
    elif a == "matrix":
        left, top, size = 930, 250, 560
        draw.rectangle((left, top, left+size, top+size), outline=(*INK, 80), width=3)
        draw.line((left+size//2, top, left+size//2, top+size), fill=(*INK, 70), width=3)
        draw.line((left, top+size//2, left+size, top+size//2), fill=(*INK, 70), width=3)
        labels = [("自动化", 990, 340, GOLD), ("Workflow", 1260, 340, CYAN), ("Single Agent", 980, 610, CYAN), ("Harnessed\nAgent", 1250, 590, RED)]
        for t, x, y, c in labels:
            draw_text(draw, (x, y), t, SANS_40, fill=c, spacing=4)
        draw.text((left+190, top-55), "流程清楚 → 路径开放", font=SANS_28, fill=(*MUTED, 230))
        draw.text((left-22, top+size+22), "低风险", font=SANS_28, fill=(*MUTED, 230))
        draw.text((left+size-80, top+size+22), "高风险", font=SANS_28, fill=(*MUTED, 230))
    elif a == "ladder":
        layers = [("Automation", GOLD), ("Workflow", CYAN), ("Single Agent", CYAN), ("Multi-Agent", BLUE), ("Harnessed System", RED)]
        for i, (t, c) in enumerate(layers):
            y = 690 - i * 105
            card(draw, (920 + i * 55, y, 1710, y + 76), t, "", c)
    elif a == "final":
        card(draw, (940, 300, 1280, 520), "不是更复杂", "复杂不是目标", RED)
        card(draw, (1390, 300, 1730, 520), "刚好够用", "业务问题决定架构", CYAN)
        draw.text((1030, 650), "Smallest architecture that works.", font=SANS_48, fill=(*GOLD, 245))


def save_storyboard(paths):
    cards = []
    for idx, path in enumerate(paths, 1):
        rel = path.relative_to(ROOT)
        cards.append(f'<figure><img src="{html.escape(str(rel))}"><figcaption>{idx:02d} · {html.escape(SCENES[idx-1]["headline"].replace(chr(10), " "))}</figcaption></figure>')
    doc = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>Building Effective AI Agents Storyboard</title>
<style>
body{{margin:0;background:#07090a;color:#f5f0e6;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans GB",sans-serif}}
header{{padding:48px 64px 20px}} h1{{font-size:56px;margin:0 0 10px}} p{{color:#aaa08d;font-size:20px}}
main{{display:grid;grid-template-columns:repeat(auto-fit,minmax(420px,1fr));gap:20px;padding:28px 64px 72px}}
figure{{margin:0;background:#111516;border:1px solid rgba(255,255,255,.12);border-radius:20px;padding:12px}}
img{{width:100%;display:block;border-radius:14px}} figcaption{{padding:10px 4px 2px;color:#aaa08d}}
</style></head>
<body><header><h1>Building Effective AI Agents</h1><p>Business implementation guide · subtitles burned into frames.</p></header><main>{''.join(cards)}</main></body></html>"""
    (ROOT / "storyboard.html").write_text(doc, encoding="utf-8")


def build_cover() -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-280, -160, 760, 720), fill=(*CYAN, 34))
    gd.ellipse((1280, 400, 2240, 1300), fill=(*GOLD, 24))
    img = Image.alpha_composite(img.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(80)))
    draw = ImageDraw.Draw(img, "RGBA")
    draw.rectangle((92, 150, 1828, 151), fill=(*INK, 34))
    draw.text((92, 66), "AI COGNITION COMPRESSION", font=SANS_22, fill=(*MUTED, 230))
    draw.text((92, 102), "Business Agent Architecture Guide", font=SANS_28, fill=(*INK, 230))
    draw.text((92, 250), "别急着上", font=SERIF_96, fill=INK)
    draw.text((92, 365), "Agent", font=SERIF_96, fill=CYAN)
    draw.text((96, 520), "先判断业务问题类型", font=SANS_48, fill=(*MUTED, 245))
    draw.text((96, 610), "技术特征 × 使用边界", font=SANS_40, fill=(*GOLD, 245))
    rounded(draw, (880, 190, 1740, 820), fill=(*PANEL, 240), outline=(*INK, 44), radius=36)
    left, top, size = 1010, 305, 500
    draw.rectangle((left, top, left + size, top + size), outline=(*INK, 92), width=4)
    draw.line((left + size // 2, top, left + size // 2, top + size), fill=(*INK, 70), width=4)
    draw.line((left, top + size // 2, left + size, top + size // 2), fill=(*INK, 70), width=4)
    draw.text((left + 60, top + 88), "自动化", font=SANS_40, fill=(*GOLD, 245))
    draw.text((left + 310, top + 88), "Workflow", font=SANS_40, fill=(*CYAN, 245))
    draw.text((left + 48, top + 338), "Single\nAgent", font=SANS_40, fill=(*CYAN, 245), spacing=4)
    draw.text((left + 300, top + 325), "Harnessed\nAgent", font=SANS_40, fill=(*RED, 245), spacing=4)
    draw.text((left + 120, top - 60), "流程清楚 → 路径开放", font=SANS_28, fill=(*MUTED, 230))
    draw.text((left - 5, top + size + 28), "低风险", font=SANS_28, fill=(*MUTED, 230))
    draw.text((left + size - 95, top + size + 28), "高风险", font=SANS_28, fill=(*MUTED, 230))
    rounded(draw, (1000, 865, 1580, 948), fill=(4, 6, 7, 190), outline=(*CYAN, 80), radius=22)
    draw.text((1028, 886), "不是越复杂越先进，而是刚好够用。", font=SANS_34, fill=INK)
    return img.convert("RGB")


def main():
    FRAMES.mkdir(exist_ok=True)
    paths = []
    manifest = []
    for idx, scene in enumerate(SCENES, 1):
        img = base(idx, scene)
        artifact(img, scene)
        path = FRAMES / f"scene_{idx:02d}.png"
        img.save(path, quality=94)
        paths.append(path)
        manifest.append({"file": str(path.relative_to(ROOT)), "duration": scene["duration"], "subtitle": scene["subtitle"]})
    build_cover().save(ROOT / "cover.png", quality=94)
    save_storyboard(paths)
    (ROOT / "frame_manifest.json").write_text(json.dumps({"frames": manifest}, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "narration.txt").write_text("\n".join(scene["subtitle"] for scene in SCENES) + "\n", encoding="utf-8")
    print(f"wrote {len(paths)} frames, cover.png, storyboard.html")


if __name__ == "__main__":
    main()
