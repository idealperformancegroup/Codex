from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def extract_storyboard(media_path: Path, frames_dir: Path, every_seconds: int = 3) -> list[Path]:
    """Sample frames for later visual/UI/offer analysis."""
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required but was not found on PATH")
    frames_dir.mkdir(parents=True, exist_ok=True)
    pattern = frames_dir / "frame-%04d.jpg"
    subprocess.run([
        "ffmpeg", "-y", "-i", str(media_path),
        "-vf", f"fps=1/{every_seconds}", "-q:v", "3", str(pattern)
    ], check=True)
    return sorted(frames_dir.glob("frame-*.jpg"))
