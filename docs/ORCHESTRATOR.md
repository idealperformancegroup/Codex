# Opportunity Engine Orchestrator v1

The orchestrator connects the existing modules into one command.

## End-to-end flow

```
URL
  -> Social capture
  -> Audio + transcript
  -> Storyboard frames
  -> Business-signal extraction
  -> Research-plan generation
  -> Automated evidence collection
  -> Opportunity research score
  -> Final JSON opportunity report
```

## Command

```bash
ipg-opportunity run "https://example.com/video" --run-dir runs/example
```

Use `--no-research` when a search-provider credential is unavailable. The local source-analysis stages will still run.

## Important boundary

The orchestrator produces a research report, not a guarantee of profitability. It preserves the engine's separation between verified facts, observed signals, assumptions, hypotheses, and financial scenarios.

Capital deployment remains a human decision.
