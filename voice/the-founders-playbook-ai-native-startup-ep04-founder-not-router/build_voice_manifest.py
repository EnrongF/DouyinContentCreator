import json
from pathlib import Path

from generate_qwen_tts import CHUNKS, MODEL, OUTPUT_DIR, SLUG, VOICE, VOICE_ROOT, audio_duration

VOICE_MANIFEST = VOICE_ROOT / "voice-manifest.json"
QA_OUTPUT = VOICE_ROOT / "qa.md"

CHUNK_META = {
    "c01": {
        "sectionLabel": "上线瓶颈",
        "intent": "hook the founder-router bottleneck",
        "tone": "direct",
        "pacing": "firm hook",
        "pauseAfterMs": 340,
        "emphasis": ["每个问题", "创始人接住", "增长"],
        "focusPhrase": "每个问题都还要创始人接住",
        "visualFocus": "request paths converge on founder",
    },
    "c02": {
        "sectionLabel": "Launch Gate",
        "intent": "separate MVP from Launch",
        "tone": "structured",
        "pacing": "clean contrast",
        "pauseAfterMs": 360,
        "emphasis": ["MVP", "Launch", "重复增长"],
        "focusPhrase": "业务能不能重复增长",
        "visualFocus": "MVP to Launch repeatability gate",
    },
    "c03": {
        "sectionLabel": "回路反转",
        "intent": "preserve why founder-in-loop is useful early",
        "tone": "balanced",
        "pacing": "measured",
        "pauseAfterMs": 260,
        "emphasis": ["每个回路", "优势"],
        "focusPhrase": "是优势",
        "visualFocus": "active founder learning loop",
    },
    "c04": {
        "sectionLabel": "回路反转",
        "intent": "turn the early habit into launch bottleneck",
        "tone": "decisive",
        "pacing": "short turn",
        "pauseAfterMs": 420,
        "emphasis": ["同一个习惯", "瓶颈"],
        "focusPhrase": "变成瓶颈",
        "visualFocus": "loop becomes bottleneck",
    },
    "c05": {
        "sectionLabel": "瓶颈信号",
        "intent": "make delay concrete",
        "tone": "observational",
        "pacing": "slow on the time contrast",
        "pauseAfterMs": 260,
        "emphasis": ["一小时", "一周"],
        "focusPhrase": "拖成一周",
        "visualFocus": "delayed decision queue",
    },
    "c06": {
        "sectionLabel": "瓶颈信号",
        "intent": "show recurring work piling up",
        "tone": "cumulative",
        "pacing": "list rhythm",
        "pauseAfterMs": 400,
        "emphasis": ["支持消息", "Bug", "周报"],
        "focusPhrase": "都开始排队",
        "visualFocus": "support bug report queue",
    },
    "c07": {
        "sectionLabel": "错误问题",
        "intent": "reject more founder effort as the answer",
        "tone": "corrective",
        "pacing": "brief pause",
        "pauseAfterMs": 260,
        "emphasis": ["再忙一点"],
        "focusPhrase": "再忙一点",
        "visualFocus": "wrong question dims",
    },
    "c08": {
        "sectionLabel": "注意力审计",
        "intent": "open the bottleneck audit",
        "tone": "practical",
        "pacing": "setup",
        "pauseAfterMs": 260,
        "emphasis": ["列出来", "三类"],
        "focusPhrase": "分成三类",
        "visualFocus": "audit list opens",
    },
    "c09": {
        "sectionLabel": "注意力审计",
        "intent": "sort work into automation and delegation",
        "tone": "operational",
        "pacing": "two-lane rhythm",
        "pauseAfterMs": 300,
        "emphasis": ["自动化", "系统", "角色"],
        "focusPhrase": "交给系统",
        "visualFocus": "automate and delegate lanes",
    },
    "c10": {
        "sectionLabel": "创始人判断",
        "intent": "keep founder-only decisions explicit",
        "tone": "firm",
        "pacing": "slower on decision words",
        "pauseAfterMs": 420,
        "emphasis": ["方向", "取舍", "风险判断"],
        "focusPhrase": "留给创始人",
        "visualFocus": "founder judgment lane",
    },
    "c11": {
        "sectionLabel": "本集判断",
        "intent": "land the operating rule",
        "tone": "settled",
        "pacing": "takeaway emphasis",
        "pauseAfterMs": 360,
        "emphasis": ["重复发生", "系统"],
        "focusPhrase": "重复发生的问题，要变成系统",
        "visualFocus": "system replaces founder router",
    },
    "c12": {
        "sectionLabel": "下一集",
        "intent": "bridge to workflow moat",
        "tone": "forward-looking",
        "pacing": "lighter handoff",
        "pauseAfterMs": 0,
        "emphasis": ["护城河", "业务流程"],
        "focusPhrase": "业务流程里",
        "visualFocus": "EP05 workflow moat preview",
    },
}

PARAGRAPHS = [
    {
        "id": "p01",
        "chunkIds": ["c01", "c02"],
        "coreIdea": "Launch is a repeatability gate, not just a product launch.",
        "visualFocus": "founder router bottleneck and launch gate",
    },
    {
        "id": "p02",
        "chunkIds": ["c03", "c04"],
        "coreIdea": "Founder-in-the-loop shifts from advantage to bottleneck.",
        "visualFocus": "loop advantage flips into bottleneck",
    },
    {
        "id": "p03",
        "chunkIds": ["c05", "c06"],
        "coreIdea": "Bottleneck warning signs are delayed decisions and recurring queues.",
        "visualFocus": "decision support bug report queue",
    },
    {
        "id": "p04",
        "chunkIds": ["c07", "c08", "c09", "c10"],
        "coreIdea": "Audit founder-handled work into automation, delegation, and founder judgment.",
        "visualFocus": "three-lane attention audit",
    },
    {
        "id": "p05",
        "chunkIds": ["c11", "c12"],
        "coreIdea": "Repeated problems should become systems; Scale shifts to workflow moat.",
        "visualFocus": "system router and EP05 bridge",
    },
]


def display_text(tts_text: str) -> str:
    return tts_text.replace("M V P", "MVP")


def main() -> None:
    current = 0.0
    chunks = []
    total_speech = 0.0
    for chunk in CHUNKS:
        chunk_id = chunk["id"]
        audio_path = OUTPUT_DIR / f"{chunk_id}.wav"
        if not audio_path.exists():
            raise SystemExit(f"Missing selected audio chunk: {audio_path}")
        measured = round(audio_duration(audio_path), 3)
        total_speech += measured
        meta = CHUNK_META[chunk_id]
        padding = round(meta["pauseAfterMs"] / 1000, 3)
        start = round(current, 3)
        speech_end = round(start + measured, 3)
        end = round(speech_end + padding, 3)
        chunks.append(
            {
                "id": chunk_id,
                "paragraphId": chunk["paragraph"],
                "sectionLabel": meta["sectionLabel"],
                "intent": meta["intent"],
                "tone": meta["tone"],
                "pacing": meta["pacing"],
                "text": display_text(chunk["tts"]),
                "ttsInputText": chunk["tts"],
                "subtitle": chunk["subtitle"],
                "focusPhrase": meta["focusPhrase"],
                "focusCue": "reveal-highlight",
                "focus": [meta["visualFocus"]],
                "emphasis": meta["emphasis"],
                "audioFile": f"chunks-qwen/{chunk_id}.wav",
                "ttsProvider": "qwen-dashscope",
                "ttsModel": MODEL,
                "ttsVoice": VOICE,
                "startSeconds": start,
                "speechEndSeconds": speech_end,
                "endSeconds": end,
                "measuredSpeechSeconds": measured,
                "pauseAfterMs": meta["pauseAfterMs"],
                "paddingSeconds": padding,
                "actualDurationSeconds": round(measured + padding, 3),
            }
        )
        current = end

    manifest = {
        "schemaVersion": "1.2",
        "slug": SLUG,
        "series": "The Founder's Playbook - Building an AI-Native Startup",
        "episode": {
            "number": 4,
            "title": "上线后，创始人别当中转站",
            "workingEnglishTitle": "Founder Not Router",
        },
        "language": "zh-CN",
        "status": "voice_manifest_ready",
        "pauseRequired": True,
        "nextApprovedStage": "scene graph",
        "notApprovedYet": ["visual production", "render", "Douyin package"],
        "voiceDirection": "natural Mandarin, calm technical host, direct founder-operating judgment, no news or influencer tone",
        "defaultVoiceMaker": {
            "provider": "qwen-dashscope",
            "model": MODEL,
            "voice": VOICE,
        },
        "audioStrategy": "chunk_sequence",
        "finalAudio": "selected_qwen_chunks",
        "totalMeasuredSpeechSeconds": round(total_speech, 3),
        "totalDurationSeconds": round(current, 3),
        "asr": {
            "status": "pending",
            "transcriptPath": "asr.txt",
            "qaPath": "qa.md",
        },
        "paragraphs": PARAGRAPHS,
        "chunks": chunks,
    }
    VOICE_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    qa_lines = [
        "# Voice QA",
        "",
        f"Slug: `{SLUG}`",
        "",
        "## Gate Status",
        "",
        "- Stage: `voice manifest`",
        "- Status: `manifest built from measured Qwen chunks; ASR pending`",
        "- Provider: `qwen-dashscope`",
        f"- Model: `{MODEL}`",
        f"- Voice: `{VOICE}`",
        f"- Measured speech duration: `{total_speech:.3f} seconds`",
        f"- Total duration with pauses: `{current:.3f} seconds`",
        "- Next approved stage: `scene graph / render smoke test`",
        "",
        "## Native Chinese Expression Gate",
        "",
        "Pass with caveat: script is natural Mandarin and keeps the founder-attention caveat. Final ASR should still verify `MVP`, `Launch`, `Bug`, `取舍`, and `护城河`.",
        "",
        "## ASR Status",
        "",
        "- Pending. Do not treat this as final publish QA until ASR is run.",
        "",
    ]
    QA_OUTPUT.write_text("\n".join(qa_lines), encoding="utf-8")
    print(VOICE_MANIFEST)
    print(QA_OUTPUT)


if __name__ == "__main__":
    main()
