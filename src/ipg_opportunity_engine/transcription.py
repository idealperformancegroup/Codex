from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


def transcribe(audio_path: Path, output_dir: Path, model: str = "small") -> Path:
    """Transcribe locally with the Whisper CLI when installed."""
    if not shutil.which("whisper"):
        raise RuntimeError(
            "Whisper CLI is not installed. Install openai-whisper or configure another adapter."
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "whisper", str(audio_path), "--model", model,
        "--output_dir", str(output_dir), "--output_format", "json"
    ], check=True)
    transcript = output_dir / f"{audio_path.stem}.json"
    if not transcript.exists():
        raise RuntimeError("Whisper completed but transcript JSON was not found")
    return transcript


def normalize_transcript(path: Path) -> dict:
    raw = json.loads(path.read_text(encoding="utf-8"))
    segments = [
        {
            "start": item.get("start"),
            "end": item.get("end"),
            "text": (item.get("text") or "").strip(),
        }
        for item in raw.get("segments", [])
    ]
    return {"text": (raw.get("text") or "").strip(), "segments": segments}
