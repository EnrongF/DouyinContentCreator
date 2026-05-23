import json
from pathlib import Path

from generate_qwen_tts import CHUNKS, MODEL, OUTPUT_DIR, SLUG, VOICE, VOICE_ROOT, audio_duration

VOICE_MANIFEST = VOICE_ROOT / "voice-manifest.json"
QA_OUTPUT = VOICE_ROOT / "qa.md"

CHUNK_META = {
    "c01": {
        "sectionLabel": "速度风险",
        "intent": "hook with fast AI coding",
        "tone": "direct",
        "pacing": "clean hook",
        "pauseAfterMs": 280,
        "emphasis": ["写代码很快"],
        "focusPhrase": "写代码很快",
        "visualFocus": "code stream appears",
    },
    "c02": {
        "sectionLabel": "速度风险",
        "intent": "show product scatter when boundaries are unclear",
        "tone": "slightly urgent",
        "pacing": "pause after setup",
        "pauseAfterMs": 420,
        "emphasis": ["边界不清楚", "写散"],
        "focusPhrase": "产品写散",
        "visualFocus": "feature nodes spill outside boundary",
    },
    "c03": {
        "sectionLabel": "MVP 关口",
        "intent": "correct the impulse to build a full product",
        "tone": "corrective",
        "pacing": "measured",
        "pauseAfterMs": 320,
        "emphasis": ["不是马上", "做满"],
        "focusPhrase": "不是马上把功能做满",
        "visualFocus": "full-product button dims",
    },
    "c04": {
        "sectionLabel": "MVP 关口",
        "intent": "preserve MVP as evidence gathering",
        "tone": "grounded",
        "pacing": "list rhythm",
        "pauseAfterMs": 460,
        "emphasis": ["收集证据", "回来", "付费", "推荐"],
        "focusPhrase": "回来、付费、推荐",
        "visualFocus": "focused MVP evidence gate",
    },
    "c05": {
        "sectionLabel": "范围边界",
        "intent": "reject feature accumulation as the main MVP job",
        "tone": "structured",
        "pacing": "measured setup",
        "pauseAfterMs": 260,
        "emphasis": ["不是", "还能加什么"],
        "focusPhrase": "还能加什么",
        "visualFocus": "add-feature card dims",
    },
    "c06": {
        "sectionLabel": "范围边界",
        "intent": "define the three-part scope boundary",
        "tone": "clear",
        "pacing": "three-part rhythm",
        "pauseAfterMs": 460,
        "emphasis": ["解决什么", "不解决什么", "什么证据"],
        "focusPhrase": "三件事",
        "visualFocus": "scope document appears",
    },
    "c07": {
        "sectionLabel": "上下文漂移",
        "intent": "name context reset as a hidden AI build risk",
        "tone": "firm",
        "pacing": "slightly slower",
        "pauseAfterMs": 320,
        "emphasis": ["重新猜", "产品边界"],
        "focusPhrase": "重新猜一遍产品边界",
        "visualFocus": "context reset loop",
    },
    "c08": {
        "sectionLabel": "范围失形",
        "intent": "show zero-friction scope creep",
        "tone": "cumulative",
        "pacing": "three-step accumulation",
        "pauseAfterMs": 360,
        "emphasis": ["边缘场景", "酷功能", "失去形状"],
        "focusPhrase": "失去形状",
        "visualFocus": "product box deforms",
    },
    "c09": {
        "sectionLabel": "AI 技术债",
        "intent": "define hidden AI technical debt",
        "tone": "technical",
        "pacing": "slow on concept",
        "pauseAfterMs": 460,
        "emphasis": ["技术债", "边界", "架构上下文", "漂移"],
        "focusPhrase": "边界和架构上下文",
        "visualFocus": "drift warning",
    },
    "c10": {
        "sectionLabel": "可读上下文",
        "intent": "turn the idea into an operating rule",
        "tone": "practical",
        "pacing": "decisive",
        "pauseAfterMs": 360,
        "emphasis": ["边界", "上下文", "读到"],
        "focusPhrase": "放到它能读到的地方",
        "visualFocus": "readable context document",
    },
    "c11": {
        "sectionLabel": "本集判断",
        "intent": "deliver takeaway",
        "tone": "settled",
        "pacing": "takeaway emphasis",
        "pauseAfterMs": 420,
        "emphasis": ["先写边界", "再写代码"],
        "focusPhrase": "先写边界",
        "visualFocus": "boundary before code card",
    },
    "c12": {
        "sectionLabel": "下一集",
        "intent": "bridge to founder-as-router episode",
        "tone": "forward-looking",
        "pacing": "lighter handoff",
        "pauseAfterMs": 0,
        "emphasis": ["创始人", "中转站"],
        "focusPhrase": "创始人不能继续当中转站",
        "visualFocus": "episode four router preview",
    },
}

PARAGRAPHS = [
    {
        "id": "p01",
        "chunkIds": ["c01", "c02"],
        "coreIdea": "AI coding speed scatters an unclear product.",
        "visualFocus": "feature sprawl outside boundary",
    },
    {
        "id": "p02",
        "chunkIds": ["c03", "c04"],
        "coreIdea": "MVP is still evidence-gathering, not full-product construction.",
        "visualFocus": "focused MVP evidence gate",
    },
    {
        "id": "p03",
        "chunkIds": ["c05", "c06"],
        "coreIdea": "Scope is a three-part boundary.",
        "visualFocus": "does / does not / evidence to add",
    },
    {
        "id": "p04",
        "chunkIds": ["c07", "c08", "c09"],
        "coreIdea": "AI technical debt is boundary and context drift.",
        "visualFocus": "context drift and product sprawl",
    },
    {
        "id": "p05",
        "chunkIds": ["c10", "c11", "c12"],
        "coreIdea": "Let AI execute decisions already made.",
        "visualFocus": "boundary before code and EP04 bridge",
    },
]


def display_text(tts_text: str) -> str:
    return tts_text.replace("A I", "AI").replace("M V P", "MVP")


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
            "number": 3,
            "title": "先定边界，再让 AI 写",
            "workingEnglishTitle": "Boundaries Before AI Code",
        },
        "language": "zh-CN",
        "status": "voice_manifest_ready",
        "pauseRequired": True,
        "nextApprovedStage": "scene graph",
        "notApprovedYet": ["visual production", "render", "Douyin package"],
        "voiceDirection": "natural Mandarin, calm technical host, direct and trustworthy, no news or influencer tone",
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
            "status": "pass",
            "transcript": "asr.txt",
            "qa": "asr-qa.md",
            "reviewChunks": [],
        },
        "subtitlePolicy": {
            "source": "chunks[].subtitle",
            "burnIntoFinalVideo": True,
            "standaloneSrtRequired": False,
        },
        "paragraphs": PARAGRAPHS,
        "chunks": chunks,
    }

    VOICE_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    QA_OUTPUT.write_text(
        "\n".join(
            [
                "# Voice QA",
                "",
                f"Slug: `{SLUG}`",
                "",
                "## Gate Status",
                "",
                "- Stage: `voice manifest`",
                "- Status: `Pass; manifest created`",
                "- Pause required: `yes`",
                "- Voice manifest: `voice-manifest.json`",
                "- ASR QA: `asr-qa.md`",
                "- Selected provider: `qwen-dashscope`",
                f"- Selected model: `{MODEL}`",
                f"- Selected voice: `{VOICE}`",
                f"- Total measured speech: `{manifest['totalMeasuredSpeechSeconds']:.3f} seconds`",
                f"- Total timed duration with pauses: `{manifest['totalDurationSeconds']:.3f} seconds`",
                "- Next approved stage: `scene graph`",
                "- Not approved yet: `visual production`, `render`, `Douyin package`",
                "",
                "## Decision",
                "",
                "The selected Qwen chunks are locked into a timing manifest for scene graph work.",
                "",
                "## Remaining Voice Risk",
                "",
                "- Final listening QA is still required before render because ASR cannot judge tone, fatigue, or emotional continuity.",
                "- Subtitle line breaks are not final; they should be checked against the scene graph and Douyin safe area before render.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(f"manifest={VOICE_MANIFEST}")
    print(f"qa={QA_OUTPUT}")
    print(f"total_speech={manifest['totalMeasuredSpeechSeconds']:.3f}")
    print(f"total_duration={manifest['totalDurationSeconds']:.3f}")


if __name__ == "__main__":
    main()
