import json
from pathlib import Path

from generate_qwen_tts import CHUNKS, MODEL, OUTPUT_DIR, VOICE, VOICE_ROOT, audio_duration

SLUG = "the-founders-playbook-ai-native-startup-ep01-judgment-bottleneck"
VOICE_MANIFEST = VOICE_ROOT / "voice-manifest.json"
QA_OUTPUT = VOICE_ROOT / "qa.md"

CHUNK_META = {
    "c01": {
        "sectionLabel": "旧约束",
        "intent": "hook with old bottleneck",
        "tone": "direct",
        "pacing": "fast opening",
        "pauseAfterMs": 240,
        "emphasis": ["做不出来"],
        "focusPhrase": "做不出来",
        "visualFocus": "blocked work lane",
    },
    "c02": {
        "sectionLabel": "新风险",
        "intent": "name the new failure mode",
        "tone": "slightly urgent",
        "pacing": "pause after contrast",
        "pauseAfterMs": 480,
        "emphasis": ["方向错了"],
        "focusPhrase": "方向错了",
        "visualFocus": "speed lane veers wrong",
    },
    "c03": {
        "sectionLabel": "执行提速",
        "intent": "ground AI acceleration in concrete work",
        "tone": "practical",
        "pacing": "list rhythm",
        "pauseAfterMs": 260,
        "emphasis": ["AI 都能帮你提速"],
        "focusPhrase": "AI 都能帮你提速",
        "visualFocus": "research, code, docs, ops lanes accelerate",
    },
    "c04": {
        "sectionLabel": "执行提速",
        "intent": "prevent wrong interpretation",
        "tone": "firm",
        "pacing": "short emphasis",
        "pauseAfterMs": 180,
        "emphasis": ["不是替你省掉执行"],
        "focusPhrase": "不是替你省掉执行",
        "visualFocus": "execution lane stays visible",
    },
    "c05": {
        "sectionLabel": "判断提前",
        "intent": "show speed exposing judgment",
        "tone": "explanatory",
        "pacing": "slower on judgment",
        "pauseAfterMs": 480,
        "emphasis": ["执行变快", "判断更早露出来"],
        "focusPhrase": "判断更早露出来",
        "visualFocus": "decision gate appears earlier",
    },
    "c06": {
        "sectionLabel": "判断瓶颈",
        "intent": "separate speed from the real problem",
        "tone": "firm",
        "pacing": "short",
        "pauseAfterMs": 240,
        "emphasis": ["不是问题"],
        "focusPhrase": "不是问题",
        "visualFocus": "fast lane stays neutral",
    },
    "c07": {
        "sectionLabel": "判断瓶颈",
        "intent": "state wrong-direction acceleration",
        "tone": "firm",
        "pacing": "medium",
        "pauseAfterMs": 280,
        "emphasis": ["错得更快"],
        "focusPhrase": "错得更快",
        "visualFocus": "wrong path accelerates",
    },
    "c08": {
        "sectionLabel": "判断瓶颈",
        "intent": "land the metaphor",
        "tone": "memorable but restrained",
        "pacing": "contrast emphasis",
        "pauseAfterMs": 320,
        "emphasis": ["油门", "方向盘"],
        "focusPhrase": "油门，不是方向盘",
        "visualFocus": "accelerator vs steering visual",
    },
    "c09": {
        "sectionLabel": "判断瓶颈",
        "intent": "clarify founder responsibility",
        "tone": "plain",
        "pacing": "pause after faster",
        "pauseAfterMs": 280,
        "emphasis": ["不能帮你决定"],
        "focusPhrase": "决定往哪走",
        "visualFocus": "steering remains with founder",
    },
    "c10": {
        "sectionLabel": "创始人判断",
        "intent": "name the actual bottleneck",
        "tone": "reflective",
        "pacing": "slower",
        "pauseAfterMs": 200,
        "emphasis": ["想清楚"],
        "focusPhrase": "想清楚",
        "visualFocus": "founder decision gate",
    },
    "c11": {
        "sectionLabel": "创始人判断",
        "intent": "turn judgment into two choices",
        "tone": "balanced",
        "pacing": "paired cadence",
        "pauseAfterMs": 520,
        "emphasis": ["值得做", "先停"],
        "focusPhrase": "值得做 / 先停",
        "visualFocus": "go and stop decision cards",
    },
    "c12": {
        "sectionLabel": "阶段判断",
        "intent": "reframe AI startup from tools to judgments",
        "tone": "structured",
        "pacing": "measured",
        "pauseAfterMs": 280,
        "emphasis": ["不是工具", "一连串判断"],
        "focusPhrase": "一连串判断",
        "visualFocus": "gate sequence appears",
    },
    "c13": {
        "sectionLabel": "阶段判断",
        "intent": "preview lifecycle gates",
        "tone": "structured",
        "pacing": "list rhythm",
        "pauseAfterMs": 280,
        "emphasis": ["想法", "MVP", "上线", "规模化"],
        "focusPhrase": "想法 / MVP / 上线 / 规模化",
        "visualFocus": "four lifecycle gates reveal",
    },
    "c14": {
        "sectionLabel": "阶段判断",
        "intent": "avoid compressing all gates into one lesson",
        "tone": "measured",
        "pacing": "medium",
        "pauseAfterMs": 280,
        "emphasis": ["每个阶段", "判断都不一样"],
        "focusPhrase": "判断都不一样",
        "visualFocus": "different icons on each gate",
    },
    "c15": {
        "sectionLabel": "第一关",
        "intent": "highlight the next episode gate",
        "tone": "direct",
        "pacing": "slight setup pause",
        "pauseAfterMs": 300,
        "emphasis": ["该不该做"],
        "focusPhrase": "该不该做",
        "visualFocus": "first gate highlights",
    },
    "c16": {
        "sectionLabel": "后续关卡",
        "intent": "defer later episodes",
        "tone": "compact",
        "pacing": "compact list",
        "pauseAfterMs": 520,
        "emphasis": ["边界", "系统", "护城河"],
        "focusPhrase": "边界 / 系统 / 护城河",
        "visualFocus": "later gates dimmed",
    },
    "c17": {
        "sectionLabel": "决策问题",
        "intent": "slow the viewer before asking the decision question",
        "tone": "settled",
        "pacing": "slow final beat",
        "pauseAfterMs": 300,
        "emphasis": ["别急着问怎么更快"],
        "focusPhrase": "别急着问怎么更快",
        "visualFocus": "speed question card dims",
    },
    "c18": {
        "sectionLabel": "决策问题",
        "intent": "deliver the final diagnostic question",
        "tone": "settled",
        "pacing": "question emphasis",
        "pauseAfterMs": 420,
        "emphasis": ["速度", "判断"],
        "focusPhrase": "速度，还是判断",
        "visualFocus": "final decision card",
    },
    "c19": {
        "sectionLabel": "下一集",
        "intent": "bridge to episode two",
        "tone": "forward-looking",
        "pacing": "lighter handoff",
        "pauseAfterMs": 0,
        "emphasis": ["不代表有人要"],
        "focusPhrase": "不代表有人要",
        "visualFocus": "episode two gate preview",
    },
}

PARAGRAPHS = [
    {
        "id": "p01",
        "chunkIds": ["c01", "c02"],
        "coreIdea": "Old execution bottleneck vs new wrong-direction speed risk.",
        "visualFocus": "old bottleneck vs wrong-direction speed",
    },
    {
        "id": "p02",
        "chunkIds": ["c03", "c04", "c05"],
        "coreIdea": "AI speeds up execution instead of removing it.",
        "visualFocus": "execution lanes and earlier decision gate",
    },
    {
        "id": "p03",
        "chunkIds": ["c06", "c07", "c08", "c09", "c10", "c11"],
        "coreIdea": "Speed exposes founder judgment.",
        "visualFocus": "accelerator, steering, and founder decision gate",
    },
    {
        "id": "p04",
        "chunkIds": ["c12", "c13", "c14", "c15", "c16"],
        "coreIdea": "AI startup stages test different judgments.",
        "visualFocus": "Idea, MVP, Launch, Scale gates",
    },
    {
        "id": "p05",
        "chunkIds": ["c17", "c18", "c19"],
        "coreIdea": "Ask whether the current bottleneck is speed or judgment.",
        "visualFocus": "final decision question and next episode preview",
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
            "number": 1,
            "title": "AI 创业，真正卡的是判断",
            "workingEnglishTitle": "Judgment Bottleneck",
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
            "retakeChunks": ["c05", "c08", "c09", "c14"],
        },
        "subtitlePolicy": {
            "source": "chunks[].subtitle",
            "burnIntoFinalVideo": True,
            "standaloneSrtRequired": False,
        },
        "paragraphs": PARAGRAPHS,
        "chunks": chunks,
    }

    VOICE_MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

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
                "The selected Qwen chunks are now locked into a timing manifest for scene graph work.",
                "",
                "ASR passed after retakes for `c05`, `c08`, `c09`, and `c14`.",
                "",
                "## Remaining Voice Risk",
                "",
                "- Final listening QA is still required before render because ASR cannot judge tone, fatigue, or emotional continuity.",
                "- Subtitle line breaks are not final; they should be checked against the scene graph and Douyin safe area before render.",
                "- No scene graph, visual production, render, or Douyin package was started in this gate.",
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
