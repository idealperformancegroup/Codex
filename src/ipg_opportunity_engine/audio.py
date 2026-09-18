from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def extract_audio(media_path: Path, output_path: Path) -> Path:
    """Create a mono 16 kHz WAV suitable for transcription."""
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required but was not found on PATH")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "ffmpeg", "-y", "-i", str(media_path),
        "-vn", "-ac", "1", "-ar", "16000", str(output_path)
    ], check=True)
    return output_path
