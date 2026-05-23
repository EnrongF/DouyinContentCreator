import json
from pathlib import Path

from generate_qwen_tts import CHUNKS, MODEL, OUTPUT_DIR, SLUG, VOICE, VOICE_ROOT, audio_duration

VOICE_MANIFEST = VOICE_ROOT / "voice-manifest.json"
QA_OUTPUT = VOICE_ROOT / "qa.md"

CHUNK_META = {
    "c01": {
        "sectionLabel": "快速 Demo",
        "intent": "hook with AI-era speed",
        "tone": "direct",
        "pacing": "clean hook",
        "pauseAfterMs": 280,
        "emphasis": ["很快", "Demo"],
        "focusPhrase": "很快做出 Demo",
        "visualFocus": "idea turns into Demo",
    },
    "c02": {
        "sectionLabel": "错误确定感",
        "intent": "name the false-validation risk",
        "tone": "slightly urgent",
        "pacing": "pause after setup",
        "pauseAfterMs": 420,
        "emphasis": ["问题已经被验证了"],
        "focusPhrase": "问题已经被验证了",
        "visualFocus": "evidence panel remains empty",
    },
    "c03": {
        "sectionLabel": "Demo 的用处",
        "intent": "avoid dismissing demos",
        "tone": "reassuring",
        "pacing": "short corrective",
        "pauseAfterMs": 220,
        "emphasis": ["很有用"],
        "focusPhrase": "很有用",
        "visualFocus": "Demo stays visible",
    },
    "c04": {
        "sectionLabel": "Demo 的用处",
        "intent": "reframe Demo as question tool",
        "tone": "grounded",
        "pacing": "contrast emphasis",
        "pauseAfterMs": 460,
        "emphasis": ["不是用来证明", "问清楚"],
        "focusPhrase": "问清楚",
        "visualFocus": "Demo shifts to question tool",
    },
    "c05": {
        "sectionLabel": "想法阶段",
        "intent": "set up the three validation checks",
        "tone": "structured",
        "pacing": "measured setup",
        "pauseAfterMs": 260,
        "emphasis": ["不是能不能做出来", "三件事"],
        "focusPhrase": "三件事",
        "visualFocus": "validation gate appears",
    },
    "c06": {
        "sectionLabel": "验证检查",
        "intent": "first validation check",
        "tone": "clear",
        "pacing": "list rhythm",
        "pauseAfterMs": 220,
        "emphasis": ["真实", "具体", "经常发生"],
        "focusPhrase": "真实、具体、经常发生",
        "visualFocus": "check one highlights",
    },
    "c07": {
        "sectionLabel": "验证检查",
        "intent": "second validation check",
        "tone": "clear",
        "pacing": "slightly slower",
        "pauseAfterMs": 220,
        "emphasis": ["用户真正的问题"],
        "focusPhrase": "用户真正的问题",
        "visualFocus": "check two highlights",
    },
    "c08": {
        "sectionLabel": "验证检查",
        "intent": "third validation check",
        "tone": "firm",
        "pacing": "short",
        "pauseAfterMs": 420,
        "emphasis": ["信号", "MVP"],
        "focusPhrase": "开始做 MVP",
        "visualFocus": "check three highlights",
    },
    "c09": {
        "sectionLabel": "问法切换",
        "intent": "reject weak future-facing question",
        "tone": "practical",
        "pacing": "slight skepticism",
        "pauseAfterMs": 260,
        "emphasis": ["你会不会用"],
        "focusPhrase": "你会不会用",
        "visualFocus": "weak question dims",
    },
    "c10": {
        "sectionLabel": "问法切换",
        "intent": "give better evidence questions",
        "tone": "practical",
        "pacing": "three question rhythm",
        "pauseAfterMs": 500,
        "emphasis": ["上一次", "现在", "为什么"],
        "focusPhrase": "上一次 / 现在 / 为什么",
        "visualFocus": "evidence questions appear",
    },
    "c11": {
        "sectionLabel": "证据判断",
        "intent": "separate praise from answer",
        "tone": "firm",
        "pacing": "short",
        "pauseAfterMs": 260,
        "emphasis": ["夸 Demo", "没有答案"],
        "focusPhrase": "没有答案",
        "visualFocus": "praise lane dims",
    },
    "c12": {
        "sectionLabel": "证据判断",
        "intent": "name the stronger signal",
        "tone": "decisive",
        "pacing": "slow on pain",
        "pauseAfterMs": 420,
        "emphasis": ["真实痛点", "更有价值的信号"],
        "focusPhrase": "真实痛点",
        "visualFocus": "pain and contradiction chips highlight",
    },
    "c13": {
        "sectionLabel": "本集判断",
        "intent": "deliver takeaway",
        "tone": "settled",
        "pacing": "takeaway emphasis",
        "pauseAfterMs": 420,
        "emphasis": ["帮你问问题", "不能替你证明有人要"],
        "focusPhrase": "不能替你证明有人要",
        "visualFocus": "final decision card",
    },
    "c14": {
        "sectionLabel": "下一集",
        "intent": "bridge to boundaries episode",
        "tone": "forward-looking",
        "pacing": "lighter handoff",
        "pauseAfterMs": 0,
        "emphasis": ["先定边界"],
        "focusPhrase": "先定边界",
        "visualFocus": "episode three gate preview",
    },
}

PARAGRAPHS = [
    {
        "id": "p01",
        "chunkIds": ["c01", "c02"],
        "coreIdea": "AI makes Demo fast, but fast Demo creates false certainty.",
        "visualFocus": "fast Demo before evidence",
    },
    {
        "id": "p02",
        "chunkIds": ["c03", "c04"],
        "coreIdea": "Demo is useful as a question tool, not proof.",
        "visualFocus": "Demo shifts from proof to conversation tool",
    },
    {
        "id": "p03",
        "chunkIds": ["c05", "c06", "c07", "c08"],
        "coreIdea": "Idea-stage gate is problem-solution fit.",
        "visualFocus": "three validation checks",
    },
    {
        "id": "p04",
        "chunkIds": ["c09", "c10"],
        "coreIdea": "Better customer discovery asks about past behavior and current workaround.",
        "visualFocus": "weak question vs evidence questions",
    },
    {
        "id": "p05",
        "chunkIds": ["c11", "c12", "c13", "c14"],
        "coreIdea": "Praise is not enough; pain and contradiction are better signals.",
        "visualFocus": "praise vs pain decision card and EP03 bridge",
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
            "number": 2,
            "title": "有 Demo，不代表有人要",
            "workingEnglishTitle": "Demo Is Not Demand",
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
