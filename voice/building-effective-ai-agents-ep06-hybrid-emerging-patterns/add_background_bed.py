import math
import subprocess
import wave
from pathlib import Path

import numpy as np

VOICE_ROOT = Path(__file__).resolve().parent
TEST_DIR = VOICE_ROOT / "voice-tests"
INPUT_MP3 = TEST_DIR / "ep06-opening-retention-marin.mp3"
VOICE_WAV = TEST_DIR / "ep06-opening-retention-marin.voice.wav"
BED_WAV = TEST_DIR / "ep06-opening-retention-background-bed.wav"
MIX_WAV = TEST_DIR / "ep06-opening-retention-marin.bg.wav"
OUTPUT_MP3 = TEST_DIR / "ep06-opening-retention-marin.bg.mp3"

SAMPLE_RATE = 44100


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def read_wav(path: Path) -> tuple[np.ndarray, int]:
    with wave.open(str(path), "rb") as wav:
        channels = wav.getnchannels()
        sample_rate = wav.getframerate()
        frames = wav.readframes(wav.getnframes())
    audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
    audio = audio.reshape(-1, channels)
    return audio, sample_rate


def write_wav(path: Path, audio: np.ndarray, sample_rate: int) -> None:
    audio = np.clip(audio, -1.0, 1.0)
    pcm = (audio * 32767.0).astype(np.int16)
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(audio.shape[1])
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(pcm.tobytes())


def make_background_bed(duration_seconds: float, channels: int) -> np.ndarray:
    total = int(duration_seconds * SAMPLE_RATE)
    t = np.arange(total, dtype=np.float32) / SAMPLE_RATE

    # A quiet low-mid harmonic bed: enough warmth to reduce dry TTS,
    # but filtered by design so it does not compete with Mandarin consonants.
    base = (
        0.018 * np.sin(2 * math.pi * 92 * t)
        + 0.011 * np.sin(2 * math.pi * 138 * t)
        + 0.007 * np.sin(2 * math.pi * 184 * t)
    )
    slow_pulse = 0.82 + 0.18 * np.sin(2 * math.pi * 0.08 * t)
    bed = base * slow_pulse

    fade_len = min(total // 4, int(1.2 * SAMPLE_RATE))
    fade = np.ones(total, dtype=np.float32)
    fade[:fade_len] = np.linspace(0, 1, fade_len)
    fade[-fade_len:] = np.linspace(1, 0, fade_len)
    bed *= fade

    return np.repeat(bed[:, None], channels, axis=1)


def main() -> None:
    TEST_DIR.mkdir(parents=True, exist_ok=True)
    run(["afconvert", str(INPUT_MP3), str(VOICE_WAV), "-f", "WAVE", "-d", "LEI16@44100"])

    voice, sample_rate = read_wav(VOICE_WAV)
    if sample_rate != SAMPLE_RATE:
        raise RuntimeError(f"Expected {SAMPLE_RATE}, got {sample_rate}")

    duration = len(voice) / SAMPLE_RATE
    bed = make_background_bed(duration, voice.shape[1])
    write_wav(BED_WAV, bed, SAMPLE_RATE)

    # Gentle ducking: keep bed lower where voice energy is present.
    mono_energy = np.sqrt(np.mean(voice * voice, axis=1))
    window = max(1, int(0.08 * SAMPLE_RATE))
    kernel = np.ones(window, dtype=np.float32) / window
    smooth = np.convolve(mono_energy, kernel, mode="same")
    duck = 1.0 - np.clip(smooth * 7.0, 0, 0.55)
    bed *= duck[:, None]

    mixed = voice * 0.98 + bed
    peak = float(np.max(np.abs(mixed)))
    if peak > 0.96:
        mixed *= 0.96 / peak

    write_wav(MIX_WAV, mixed, SAMPLE_RATE)
    run(["afconvert", str(MIX_WAV), str(OUTPUT_MP3), "-f", "MPG3", "-d", "aac"])

    print(f"input={INPUT_MP3}")
    print(f"bed={BED_WAV}")
    print(f"output={OUTPUT_MP3}")


if __name__ == "__main__":
    main()
