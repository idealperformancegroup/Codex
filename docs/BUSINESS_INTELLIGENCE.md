# Business Intelligence Layer v1

This layer converts a captured transcript into conservative business-signal candidates and a research plan.

It extracts:
- opening hook candidate
- explicit price mentions
- CTA language
- claim candidates
- problem-language candidates
- recurring keywords

It does **not** treat these as verified market facts. The output is marked `requires_market_validation`.

## Opportunity scoring
The scoring module is a transparent research-priority score. It is not a prediction of profitability.

Inputs are scored 0-10:
- demand evidence
- advertising persistence
- complaint opportunity
- margin potential
- automation advantage
- fulfillment simplicity
- competition risk
- regulatory/IP risk

Scores should only be populated after evidence is gathered.
