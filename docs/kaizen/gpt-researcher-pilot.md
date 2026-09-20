# GPT Researcher - KAIZEN Deep Review & Pilot Plan

**Date:** 2026-09-20  
**Upstream:** https://github.com/assafelovic/gpt-researcher  
**KAIZEN status:** TEST CANDIDATE - do not make a production dependency until benchmarked.

## Why this is being tested

KAIZEN needs a reusable research substrate capable of decomposing a broad research mandate into subquestions, searching multiple sources in parallel, scraping and curating evidence, retaining context, tracking sources, and producing structured outputs.

GPT Researcher appears to provide much of that machinery while allowing KAIZEN to retain its own underwriting and decision rules.

## Code-level findings

Inspection of the current upstream code confirms:

1. **Research planning is explicit.** `ResearchConductor.plan_research()` performs an initial search and then calls `plan_research_outline()` to generate a research strategy/subqueries.
2. **Subqueries are parallelized.** Web/vector research paths use `asyncio.gather()` across planned subqueries.
3. **Source modes are flexible.** Current conductor code supports web, local documents, hybrid, Azure, LangChain documents, LangChain vector stores, provided URLs, and optional complementary web research.
4. **MCP is built into retrieval.** The conductor detects MCP retrievers and supports `disabled`, `fast`, and `deep` strategies, including caching to reduce redundant calls.
5. **Multiple retrievers exist.** Current upstream includes Tavily, Exa, Google, Bing, Brave, DuckDuckGo, SerpAPI, Serper, Searx, arXiv, OpenAlex, Semantic Scholar, PubMed Central, MCP, custom retrieval and others.
6. **Source curation exists.** After collection, the conductor can run a source-curation step before downstream report generation.
7. **Cost/context telemetry exists.** The workflow logs research costs and context size, which is useful for a KAIZEN benchmark.

## Strategic fit

GPT Researcher should be treated as a **research worker**, not as the KAIZEN decision maker.

Proposed boundary:

```
KAIZEN mandate
  -> KAIZEN query/template
  -> GPT Researcher collection + synthesis
  -> normalized evidence packet
  -> KAIZEN gap analysis + underwriting
  -> TEST / WATCH / PASS
```

## Pilot: Digital Product Scout

### Research mandate

> Identify digital-product categories with demonstrated buyer demand where repeated, source-backed customer complaints reveal a tractable opportunity for a materially better original product. Do not copy protected content, branding, source code, proprietary datasets, or distinctive expression.

### Required evidence packet

For every candidate:
- product/category;
- leading products/competitors;
- evidence of demand and date of evidence;
- pricing/business model where observable;
- review/community sources;
- repeated complaint themes;
- frequency/confidence of each gap;
- what current products already solve;
- unresolved need;
- proposed Product 2.0 thesis;
- possible delivery mechanisms;
- estimated build complexity;
- plausible distribution channels;
- material legal/IP/platform/privacy risks;
- sources and evidence quality.

### Research source priorities

Prioritize sources according to the product category:
- product marketplaces and rankings;
- G2 / Capterra / TrustRadius where applicable;
- Apple / Google app-store reviews;
- Reddit and relevant communities;
- GitHub Issues for software/open-source competitors;
- public customer reviews and support forums;
- search-demand and advertising/distribution evidence;
- creator/course/template marketplaces when accessible and lawful.

Do not treat stars, likes, isolated comments, or unsupported revenue claims as proof of product-market fit.

## Benchmark design

Run the same narrow product-discovery mandate through:
A. normal KAIZEN research; and
B. GPT Researcher.

Compare:

| Dimension | Measure |
|---|---|
| Source breadth | unique credible sources and source classes |
| Traceability | claims with inspectable supporting sources |
| Complaint quality | repeated customer problems found vs generic feature ideas |
| Gap specificity | actionable, non-generic unmet needs |
| Demand evidence | independent evidence supporting existing spend/usage |
| Noise | irrelevant, duplicated, weak or promotional evidence |
| Research time | elapsed workflow time |
| API/search cost | measured external cost where available |
| Decision usefulness | whether evidence supports TEST/WATCH/PASS |
| Reproducibility | whether another run can reconstruct the evidence trail |

### Adoption gate

Adopt or adapt GPT Researcher only if it materially improves at least one high-value dimension without unacceptable degradation in reliability, cost, security, or operational complexity.

Possible outcomes:
- **ADOPT** - use upstream package/service largely as designed.
- **ADAPT** - borrow/fork selected research-conductor patterns.
- **REFERENCE** - retain architecture/methodology only.
- **REJECT** - no meaningful delta over existing capabilities.

## Security / operational gates before local integration

- Pin a reviewed version/commit rather than tracking upstream blindly.
- Never commit API keys or credentials.
- Review scraper/retriever network behavior.
- Use least-privilege API credentials.
- Separate research data from secrets/customer private data.
- Do not give autonomous research code write/deploy/payment permissions.
- Treat retrieved web content as untrusted input.
- Preserve citations/source URLs in normalized outputs.
- Track external API cost and rate limits.
- Run new upstream updates through review before adoption.

## First implementation target

Create a thin **KAIZEN Digital Product Scout adapter** rather than importing the entire upstream project into Codex immediately.

The adapter should eventually:
1. accept a KAIZEN research mandate;
2. invoke the selected research backend;
3. normalize results to the KAIZEN evidence schema;
4. pass the evidence packet to the Digital Asset Portfolio Engine;
5. write the resulting opportunity record into the KAIZEN registry;
6. preserve source provenance and benchmark metrics.

## Current decision

**Proceed to controlled pilot. Do not yet install as a permanent production dependency.**
