# KAIZEN Digital Product Intelligence & Creation Stack

**Created:** 2026-09-20

## Objective

Create a repeatable system that discovers proven digital-product demand, identifies unresolved customer complaints and market gaps, defines a materially improved original product, and then assists with or automates production, testing, and iteration.

This is not a cloning system. The operating rule is:

**Find demonstrated demand -> identify unmet needs -> create a materially better original solution -> test -> learn -> improve.**

## Target Loop

1. **Discover Winners**
   - Find digital products, SaaS, templates, courses, tools, apps, calculators, memberships, guides, or other digital assets with demonstrated demand.
   - Evidence may include reviews, revenue signals, rankings, advertising activity, app-store performance, marketplace traction, community discussion, or other credible signals.

2. **Mine Customer Pain**
   - Collect low-star reviews, support complaints, Reddit discussions, "alternative to" searches, feature requests, GitHub issues, app-store reviews, G2/Capterra/TrustRadius feedback, and other user language.
   - Cluster repeated complaints and separate isolated anecdotes from persistent gaps.

3. **Gap Analysis**
   - Compare what customers want with what leading products currently deliver.
   - Identify missing features, usability friction, weak delivery mechanisms, poor pricing structures, underserved segments, bad onboarding, support gaps, complexity, or other improvement opportunities.

4. **Underwrite**
   - Determine whether the opportunity deserves test capital.
   - Assess demonstrated demand, competition, gap strength, production difficulty, distribution access, monetization depth, legal/IP risk, support burden, and expected portfolio value.
   - Status: TEST / WATCH / PASS.

5. **Define Product 2.0 Thesis**
   - One precise sentence explaining why the proposed product deserves to exist and what meaningful gap it solves better than current alternatives.

6. **Design Product + Delivery Mechanism**
   - Choose the simplest format that best delivers the desired outcome: workbook, spreadsheet, assessment, interactive web tool, app, template pack, AI-guided tool, course, membership, hybrid, etc.
   - Do not copy protected expression, source code, proprietary datasets, branding, or content.

7. **Build**
   - Generate the minimum sellable asset and supporting funnel components.
   - Human review and QA remain gates before release.

8. **Test**
   - Run a bounded demand/distribution test.
   - Measure the evidence chain from attention through purchase, usage, refund/retention, and follow-on behavior.

9. **Learn + Improve**
   - Feed customer behavior, reviews, survey responses, support tickets, ad results, and purchase history back into future product selection and product revisions.

---

## Candidate Repository Stack

### 1. GPT Researcher
**Repository:** https://github.com/assafelovic/gpt-researcher  
**Role:** General research engine

Observed capabilities:
- planner + execution-agent architecture;
- web and local research;
- source tracking and aggregation;
- customizable/domain-specific research agents;
- JavaScript-enabled scraping;
- memory/context during research;
- report export;
- MCP support/topic.

**KAIZEN use:** foundation research engine underneath specialized digital-product research workflows.

**Status:** DEEP REVIEW / TEST CANDIDATE

### 2. Deep Market Research
**Repository:** https://github.com/RohitWaghire/Deep-Market-Reasearch  
**Role:** Demand + pain + competitor-gap research logic

Observed workflow:
- mines Reddit, Quora, X, Hacker News for pain;
- quantifies demand signals;
- identifies competitors;
- mines 1-star reviews and "alternative to" searches;
- analyzes monetization and distribution;
- produces validation verdicts and test plans.

**KAIZEN use:** excellent reference logic for our opportunity-research and underwriting layer.

**Caution:** very small/new repository; use the methodology as reference before trusting the implementation.

**Status:** METHODOLOGY CANDIDATE

### 3. GapHunter
**Repository:** https://github.com/debba/gaphunter-skill  
**Role:** Complaint mining + competitive gap extraction

Observed workflow:
- searches G2, Capterra, TrustRadius, Reddit, GitHub Issues, Hacker News;
- clusters semantically similar complaints;
- tags frequency, trend, priority, and effort;
- compares gaps against an existing codebase;
- creates structured gap reports and implementation plans.

**KAIZEN use:** this is extremely close to the "find what customers dislike and turn it into the roadmap" part of our target system.

**Status:** HIGH-PRIORITY METHODOLOGY / POSSIBLE ADAPTER

### 4. BigIdeasDB
**Repository / project:** https://github.com/bigideas-db/.github  
**Role:** External market-intelligence/data source

Project claims:
- analyzes large volumes of complaints across Reddit, G2, Capterra, Upwork, App Stores and other sources;
- combines pain-point data with revenue, acquisition, funding, and company intelligence;
- exposes MCP tools.

**KAIZEN use:** potentially valuable data feed rather than core open-source engine.

**Caution:** verify accessible data, pricing, source rights, coverage, and reproducibility before dependency.

**Status:** DATA-SOURCE EVALUATION

### 5. Open Product Researcher
**Repository:** https://github.com/lhstorm/open-product-researcher  
**Role:** Structured product research + go/no-go + PRD

Observed workflow:
- structured 7-step product research methodology;
- competitive, technical, and commercial research;
- kill/pivot/continue logic;
- traceable research artifacts;
- multi-model + multiple search providers;
- MCP extensibility;
- final strategic synthesis / PRD.

**KAIZEN use:** strong reference architecture for turning raw research into an investment/build decision.

**Caution:** repository describes itself as a proof of concept and has little community adoption. Treat architecture as inspiration until tested.

**Status:** ARCHITECTURE CANDIDATE

### 6. AI-Factory (AICOM)
**Repository:** https://github.com/alexar76/aicom  
**Role:** Autonomous build pipeline

Observed workflow:
- "idea -> shippable web product";
- multi-agent pipeline spanning research, PM, architecture, design, development, QA, security, deployment, marketing, and sales;
- self-hosted;
- testing and QA gates;
- storefront / publishing capabilities.

**KAIZEN use:** potential build/execution layer after product thesis and specification are approved.

**Caution:** broad and complex system with low public adoption signal at present. Needs isolated technical/security review before integration.

**Status:** BUILD-LAYER TEST CANDIDATE

---

## Recommended KAIZEN Architecture

Rather than betting on one repository, assemble the capability:

```
MARKET SOURCES
Reddit / G2 / Capterra / App Stores / marketplaces / ads / search / communities
        |
        v
GPT RESEARCHER
broad research, sourcing, parallel exploration
        |
        v
DIGITAL PRODUCT SCOUT
identify products/categories with demonstrated demand
        |
        v
GAP MINER
GapHunter-style complaint clustering and missing-feature analysis
        |
        v
UNDERWRITER
Deep-Market-Research + KAIZEN portfolio rules
TEST / WATCH / PASS
        |
        v
PRODUCT 2.0 THESIS
material improvement + target segment + delivery mechanism
        |
        v
BUILD SPEC
content / UX / modules / features / funnel / tracking
        |
        v
AUTONOMOUS BUILD LAYER
AI-Factory-style execution or appropriate artifact-specific tools
        |
        v
QA + HUMAN GATE
        |
        v
BOUNDED MARKET TEST
        |
        v
DATA -> ITERATE / SCALE / KILL / HOLD
```

## Important Design Rule

**GPT Researcher is the research substrate, not the investment brain.**

The KAIZEN Digital Asset Portfolio Engine remains the decision system. External repositories provide specialized machinery, data collection, research patterns, and production capability. They do not replace our underwriting rules.

## First Prototype Goal

Build a KAIZEN "Digital Product Scout" workflow that accepts a broad mandate such as:

> Find digital products with demonstrated demand where repeated customer complaints reveal a tractable opportunity for a materially better original product.

Expected output for each candidate:
- category / product type;
- evidence of demand;
- leading competitors;
- price / business model;
- review and complaint sources;
- repeated pain themes;
- gap frequency/confidence;
- proposed improvement thesis;
- plausible delivery mechanism;
- build complexity;
- distribution options;
- legal/IP/platform risks;
- TEST / WATCH / PASS;
- smallest market test.

## Next Technical Test

Use GPT Researcher on one narrow product category and compare its source breadth, traceability, complaint retrieval, and synthesis quality against a normal KAIZEN web-research pass. Do not integrate it permanently until the measured delta justifies it.
