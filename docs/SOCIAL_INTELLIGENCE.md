# Social Intelligence Engine v1

## Goal
Convert a permitted public social-media URL into machine-readable evidence for opportunity research.

## Pipeline
URL -> yt-dlp capture -> ffmpeg audio -> Whisper transcript -> sampled storyboard frames -> JSON report.

Supported URL classification currently includes Instagram, Facebook, TikTok, YouTube, and X. Actual capture depends on what yt-dlp can access lawfully and technically at runtime.

## Requirements
- Python 3.11+
- yt-dlp
- ffmpeg
- Whisper CLI (openai-whisper)

## Current boundary
v1 extracts frames but does not yet make AI claims about their contents. Visual model analysis is the next adapter. Market validation, competitor research, reviews, economics, and opportunity scoring are separate downstream modules.

## Usage
```bash
ipg-opportunity analyze-social "https://example.com/video" --run-dir runs/example
```

The output is `social-intelligence-report.json`.

## Evidence rule
Capture/transcription is source evidence. Interpretation and profitability remain unproven until downstream research is completed.
