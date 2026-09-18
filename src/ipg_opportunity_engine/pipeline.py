from __future__ import annotations

import json
from pathlib import Path

from .audio import extract_audio
from .capture import capture_media
from .social_intelligence import create_signal_report
from .storyboard import extract_storyboard
from .transcription import normalize_transcript, transcribe


def run_social_pipeline(url: str, run_dir: Path, whisper_model: str = "small") -> Path:
    """URL -> capture -> audio -> transcript -> storyboard -> machine-readable report."""
    run_dir.mkdir(parents=True, exist_ok=True)
    capture = capture_media(url, run_dir / "capture")
    audio = extract_audio(capture.media_path, run_dir / "audio" / "speech.wav")
    transcript_path = transcribe(audio, run_dir / "transcript", whisper_model)
    transcript = normalize_transcript(transcript_path)
    frames = extract_storyboard(capture.media_path, run_dir / "frames")

    report = create_signal_report(url).model_dump(mode="json")
    report["transcript"] = transcript
    report["visual_analysis"] = {
        "status": "frames_extracted_pending_model_analysis",
        "frame_count": len(frames),
        "frames": [str(p) for p in frames],
    }
    report["artifacts"] = {
        "media": str(capture.media_path),
        "metadata": str(capture.metadata_path),
        "audio": str(audio),
        "transcript": str(transcript_path),
    }

    output = run_dir / "social-intelligence-report.json"
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return output
