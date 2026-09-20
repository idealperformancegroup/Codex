# KAIZEN GitHub Capability Index

**Purpose:** Continuously discover, evaluate, test, and adopt open-source capabilities that improve IPG systems, ChatGPT/Codex workflows, websites, automation, operations, research, and other business functions.

**Operating loop:** Discover -> Classify -> Verify -> Score -> Test -> Integrate -> Measure -> Standardize -> Recheck

## Repository Types

- **Discovery Feed** - helps KAIZEN find other repositories.
- **Capability Tool** - provides a capability we may directly use or integrate.
- **Infrastructure** - connects systems or makes other capabilities accessible.
- **Reference / Learning** - useful examples, patterns, or implementation guidance.
- **Deprioritized** - superseded, archived, maintenance-only, duplicated, or currently low fit.

## Index Fields

Each repository should eventually carry:
- Repository
- Repository type
- Capability domain
- Primary use case
- Source / discovery query
- Stars / adoption signal
- Last activity
- License
- Maintainer / organization signal
- Documentation quality
- Integration difficulty
- Existing-capability overlap
- Security / dependency review
- Expected KAIZEN delta
- Evaluation status
- Test result
- Adoption decision
- Recheck date

## Seed Index - 2026-09-20

| Repository | Type | Capability Domain | What KAIZEN can use it for | Signals observed | Status | Next Action |
|---|---|---|---|---|---|---|
| [taishi-i/awesome-ChatGPT-repositories](https://github.com/taishi-i/awesome-ChatGPT-repositories) | Discovery Feed | LLM / ChatGPT / Codex discovery | Search a curated corpus of ~2,700 ChatGPT/OpenAI/Codex-related repositories; supports scored search and Codex/Claude skills | Updated Sep. 18, 2026; ~3.2K stars; CC0-1.0; Python | **Priority discovery source** | Evaluate using its bundled search skill/data as a KAIZEN ingestion source |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Discovery Feed | MCP ecosystem | Discover MCP servers that can add tools and external-system access to AI agents | Active; ~95K stars; MIT; very large ecosystem catalog | **Priority discovery source** | Mine by business capability: browser, data, CRM, marketing, finance, automation |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | Infrastructure | GitHub / AI integration | Give AI systems direct GitHub repository, file, issue, PR, workflow and code-analysis capabilities | Official GitHub project; ~33K stars; MIT; active | **High relevance** | Compare its capabilities against our current ChatGPT GitHub connector and identify gaps |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Capability Tool | Browser automation / web QA | Let LLM agents interact with websites using structured accessibility data; useful for autonomous website QA, testing and workflows | Microsoft; ~37K stars; Apache-2.0; active | **Test candidate** | Evaluate against existing browser/agent capabilities for website testing and autonomous QA |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Capability Tool / Framework | AI agents / orchestration | Build multi-agent workflows with tools, MCP, guardrails, human-in-loop, sessions, tracing, voice and sandbox agents | Official OpenAI project; active; provider-agnostic per README | **Strategic candidate** | Map components to KAIZEN autonomous research and testing workflows |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Deprioritized / Reference | Multi-agent orchestration | Historical multi-agent framework and migration reference | README states maintenance mode and directs new users to Microsoft Agent Framework | **Do not start new build here** | Evaluate successor Microsoft Agent Framework instead |

## Initial Capability Taxonomy

### AI / LLM
- Agent orchestration
- Long-term memory / context
- RAG / knowledge retrieval
- MCP / external tools
- Browser and computer use
- Voice
- Evaluation and tracing
- Prompt / skill systems
- Model routing
- Document and data workflows

### Web / Digital Product
- Website generation
- UI / component systems
- Browser testing and QA
- SEO
- Accessibility
- Analytics
- Conversion optimization
- Deployment
- Scraping / extraction
- Performance optimization

### Marketing / Growth
- Ad intelligence
- Competitor research
- Review mining
- Creative generation
- Social publishing
- Email / SMS automation
- CRM augmentation
- Attribution and analytics

### Business Operations
- Workflow automation
- Data extraction
- Reporting
- Finance / accounting
- Scheduling
- Customer service
- Sales automation
- Internal knowledge
- Logistics / dispatch

### Research / Finance / Trading
- Market data
- Backtesting
- Journaling
- Risk management
- Quantitative research
- News / sentiment
- Strategy testing

## KAIZEN Evaluation Rule

A repository is not valuable merely because it is popular. KAIZEN should prefer capabilities that produce a measurable improvement in one or more of:

1. Revenue potential
2. Cost reduction
3. Time saved
4. Error reduction
5. Quality improvement
6. Automation / autonomy
7. Decision quality
8. Scalability
9. Reliability
10. New capability unlocked

Popularity, stars, and community adoption are evidence inputs — not the final decision.

## Current Discovery Strategy

1. Query GitHub directly by capability/use case.
2. Use high-quality curated catalogs as multiplier sources.
3. Inspect README, license, update recency, maintenance status, issues, and dependency burden.
4. Add plausible candidates to this index.
5. Deep-review only the strongest candidates.
6. Test before integrating.
7. Record rejected/deprioritized repositories to avoid repeated work.
8. Recheck high-potential repositories periodically.

## KAIZEN Self-Improvement Scan 01 - 2026-09-20

First focused scan across memory, RAG/knowledge, deep research, browser/computer use, agent architecture, and evaluation.

| Repository | Domain | Observed capability | KAIZEN disposition | Why it matters / next test |
|---|---|---|---|---|
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / RAG | Portable single-file, persistent, versioned AI memory with retrieval; model-agnostic | **Deep-review candidate** | Potential durable memory layer for autonomous KAIZEN agents and project-specific knowledge. Verify benchmark claims independently and test retrieval quality, portability, write/update behavior, and operational complexity. |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | Autonomous research | Planner + execution agents; web/local research; source tracking; report generation; MCP topic; exports | **Deep-review candidate** | Closely matches KAIZEN's research mandate. Test whether its research pipeline improves breadth, sourcing, repeatability, and cost versus capabilities already available to us. |
| [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) | Browser / computer use | CLI + extension intended to let shell-capable AI agents operate a user's real logged-in browser | **Deep-review candidate - security-sensitive** | Potentially valuable for authenticated workflows. Requires strict review of permissions, credential/session exposure, action controls, and overlap with existing browser/computer-use tooling before any installation. |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | RAG / knowledge | Framework surfaced in high-adoption RAG search | **Research queue** | Evaluate specifically for KAIZEN knowledge ingestion/indexing rather than adopting a large framework by default. |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | Agent architecture | Agent design patterns / principles surfaced in RAG-agent search | **Learning/reference queue** | Mine design principles that could improve our architecture without necessarily adding another dependency. |

### Scan 01 conclusion

The strongest immediate investigation targets are **GPT Researcher**, **Memvid**, and **BrowserSkill**, but for three different reasons:

- GPT Researcher: improve the *research engine*.
- Memvid: improve the *memory/knowledge layer*.
- BrowserSkill: improve the *action/execution layer*.

These are candidates for testing, not automatic adoption. KAIZEN should compare each against capabilities already available in ChatGPT/Codex before adding infrastructure.

### Next gate

For every deep-review candidate:
1. inspect architecture and dependencies;
2. inspect license and maintenance;
3. identify exact capability gap it fills;
4. compare with our existing capability;
5. assess security/privacy risk;
6. define a small benchmark task;
7. test in isolation;
8. measure delta;
9. adopt, reject, or hold.
