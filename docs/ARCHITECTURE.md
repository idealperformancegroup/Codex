# IPG Opportunity Engine Architecture

## Mission
Turn market signals into evidence-backed commercial experiments.

## System loop

```
Market
  -> Signal
  -> Capture
  -> Transcript + Visual Context
  -> Business Model Extraction
  -> Market Research
  -> Competitor Intelligence
  -> Review / Complaint Mining
  -> Opportunity Thesis
  -> Unit Economics
  -> Experiment Design
  -> Creative Brief
  -> Arcads Creative Production
  -> Meta Test
  -> Performance Data
  -> Scale / Kill
  -> Learning
```

## Module map

### 1. Social Intelligence Engine
Input: social URL.
Output: normalized signal record with transcript, visual notes, offer structure, and source metadata.

### 2. Opportunity Scoring Engine
Ranks opportunities using observable evidence and explicit assumptions.

### 3. Market & Competitor Intelligence
Collects market size proxies, pricing, offer patterns, competitors, and acquisition channels.

### 4. Review & Complaint Mining
Finds recurring customer pain, product flaws, missing features, and language customers use.

### 5. Product / Offer Architect
Converts market gaps into a differentiated product or offer specification.

### 6. Experiment Designer
Defines the smallest credible paid or organic test with budget, success criteria, and stop conditions.

### 7. Creative Brief Generator
Produces structured briefs for ad generation.

### 8. Arcads Adapter
Hands approved briefs to the upstream Arcads creative system.

### 9. Meta Deployment Adapter
Stages approved creatives as PAUSED ads for manual review.

### 10. Performance Learning Loop
Feeds first-party test results back into future scoring and creative iteration.

## Data principle
Every conclusion should point back to evidence or be labeled as an assumption.
