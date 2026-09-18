from __future__ import annotations

import json
from pathlib import Path

from .audio import extract_audio
from .business_intelligence import build_business_intelligence
from .capture import capture_media
from .research_plan import build_research_plan
from .social_intelligence import create_signal_report
from .storyboard import extract_storyboard
from .transcription import normalize_transcript, transcribe


def run_social_pipeline(url: str, run_dir: Path, whisper_model: str = "small") -> Path:
    """URL -> source evidence -> business signals -> downstream research plan."""
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
    business_intelligence = build_business_intelligence(
        transcript, report["visual_analysis"]
    )
    report["business_intelligence"] = business_intelligence
    report["research_plan"] = build_research_plan(business_intelligence)
    report["artifacts"] = {
        "media": str(capture.media_path),
        "metadata": str(capture.metadata_path),
        "audio": str(audio),
        "transcript": str(transcript_path),
    }

    output = run_dir / "social-intelligence-report.json"
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return output
