from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CaptureResult:
    source_url: str
    media_path: Path
    metadata_path: Path


def require_binary(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise RuntimeError(f"{name} is required but was not found on PATH")
    return path


def capture_media(url: str, output_dir: Path) -> CaptureResult:
    """Download permitted public media with yt-dlp and preserve source metadata."""
    require_binary("yt-dlp")
    output_dir.mkdir(parents=True, exist_ok=True)
    template = str(output_dir / "source.%(ext)s")
    cmd = [
        "yt-dlp", "--no-playlist", "--write-info-json",
        "--output", template, url,
    ]
    subprocess.run(cmd, check=True)

    candidates = [
        p for p in output_dir.glob("source.*")
        if p.suffix not in {".json", ".part", ".ytdl"}
    ]
    if not candidates:
        raise RuntimeError("Media capture completed but no media file was found")

    media_path = candidates[0]
    metadata_path = output_dir / "source.info.json"
    if not metadata_path.exists():
        metadata_path.write_text(
            json.dumps({"webpage_url": url}, indent=2), encoding="utf-8"
        )
    return CaptureResult(url, media_path, metadata_path)
