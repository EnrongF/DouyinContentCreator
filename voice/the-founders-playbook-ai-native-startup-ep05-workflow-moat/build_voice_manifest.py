import json
from pathlib import Path

from generate_qwen_tts import CHUNKS, MODEL, OUTPUT_DIR, SLUG, VOICE, VOICE_ROOT, audio_duration

VOICE_MANIFEST = VOICE_ROOT / "voice-manifest.json"
QA_OUTPUT = VOICE_ROOT / "qa.md"

CHUNK_META = {
    "c01": {
        "sectionLabel": "错误护城河",
        "intent": "open with the common wrong moat question",
        "tone": "direct",
        "pacing": "firm hook",
        "pauseAfterMs": 300,
        "emphasis": ["护城河", "哪个模型"],
        "focusPhrase": "用了哪个模型",
        "visualFocus": "model access comparison",
    },
    "c02": {
        "sectionLabel": "错误护城河",
        "intent": "separate model access from defensibility",
        "tone": "corrective",
        "pacing": "clear contrast",
        "pauseAfterMs": 360,
        "emphasis": ["规模化", "模型权限", "相似能力"],
        "focusPhrase": "模型权限本身",
        "visualFocus": "same model access does not create separation",
    },
    "c03": {
        "sectionLabel": "流程沉淀",
        "intent": "state the episode mental model",
        "tone": "settled",
        "pacing": "slow on the key phrase",
        "pauseAfterMs": 360,
        "emphasis": ["业务流程", "沉淀", "细节"],
        "focusPhrase": "业务流程里一层一层沉淀",
        "visualFocus": "workflow specificity stack begins",
    },
    "c04": {
        "sectionLabel": "细节来源",
        "intent": "show domain and behavior as sources of specificity",
        "tone": "concrete",
        "pacing": "two-example rhythm",
        "pauseAfterMs": 260,
        "emphasis": ["行业例外", "真实用户的行为"],
        "focusPhrase": "行业的例外情况",
        "visualFocus": "domain and behavior layers",
    },
    "c05": {
        "sectionLabel": "细节来源",
        "intent": "show integrations and collaboration traces",
        "tone": "concrete",
        "pacing": "measured",
        "pauseAfterMs": 360,
        "emphasis": ["客户原来的工具", "协作痕迹"],
        "focusPhrase": "连上了客户原来的工具",
        "visualFocus": "integration and collaboration layers",
    },
    "c06": {
        "sectionLabel": "复制差距",
        "intent": "make the copy gap explicit",
        "tone": "decisive",
        "pacing": "short contrast",
        "pauseAfterMs": 260,
        "emphasis": ["提示词", "模型", "复制"],
        "focusPhrase": "换一个模型就能复制",
        "visualFocus": "competitor copy path blocked",
    },
    "c07": {
        "sectionLabel": "复制差距",
        "intent": "name the accumulated assets without overclaiming",
        "tone": "structured",
        "pacing": "list rhythm",
        "pauseAfterMs": 420,
        "emphasis": ["上下文", "数据", "集成", "习惯", "切换成本"],
        "focusPhrase": "最后变成切换成本",
        "visualFocus": "specificity becomes switching cost",
    },
    "c08": {
        "sectionLabel": "本集判断",
        "intent": "reject generic AI adoption as the question",
        "tone": "corrective",
        "pacing": "brief pause",
        "pauseAfterMs": 240,
        "emphasis": ["是不是用了 AI"],
        "focusPhrase": "是不是用了 AI",
        "visualFocus": "wrong question dims",
    },
    "c09": {
        "sectionLabel": "本集判断",
        "intent": "give the practical audit question",
        "tone": "practical",
        "pacing": "slow audit question",
        "pauseAfterMs": 380,
        "emphasis": ["系统里", "只有我们才有", "业务细节"],
        "focusPhrase": "只有我们才有的业务细节",
        "visualFocus": "workflow moat audit",
    },
    "c10": {
        "sectionLabel": "系列收束",
        "intent": "close the mini-series with conditional moat language",
        "tone": "settled",
        "pacing": "final emphasis",
        "pauseAfterMs": 0,
        "emphasis": ["规模化", "可能", "护城河"],
        "focusPhrase": "可能长出护城河",
        "visualFocus": "workflow moat closes the lifecycle",
    },
}

PARAGRAPHS = [
    {
        "id": "p01",
        "chunkIds": ["c01", "c02"],
        "coreIdea": "Model access is not defensibility at Scale.",
        "visualFocus": "same model access comparison",
    },
    {
        "id": "p02",
        "chunkIds": ["c03"],
        "coreIdea": "The gap comes from workflow-specific accumulated detail.",
        "visualFocus": "workflow specificity stack",
    },
    {
        "id": "p03",
        "chunkIds": ["c04", "c05"],
        "coreIdea": "Specificity accumulates through domain exceptions, user behavior, integrations, and collaboration traces.",
        "visualFocus": "specificity layers",
    },
    {
        "id": "p04",
        "chunkIds": ["c06", "c07"],
        "coreIdea": "Competitors can copy access more easily than operational memory.",
        "visualFocus": "copy gap and switching cost",
    },
    {
        "id": "p05",
        "chunkIds": ["c08", "c09", "c10"],
        "coreIdea": "Ask what unique business detail the system is accumulating.",
        "visualFocus": "workflow moat audit and final lifecycle close",
    },
]


def display_text(tts_text: str) -> str:
    return tts_text.replace("A I native", "AI-native").replace("A I", "AI")


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
            "number": 5,
            "title": "护城河藏在业务流程里",
            "workingEnglishTitle": "Workflow Moat",
        },
        "language": "zh-CN",
        "status": "voice_manifest_ready",
        "pauseRequired": True,
        "nextApprovedStage": "scene graph",
        "notApprovedYet": ["visual production", "render", "Douyin package"],
        "voiceDirection": "natural Mandarin, calm technical host, strategic but cautious, no hype or influencer tone",
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
        "Pass with caveat: script is natural Mandarin and keeps moat claims conditional. Final ASR should still verify `AI`, `AI-native`, `护城河`, `业务流程`, and `切换成本`.",
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
