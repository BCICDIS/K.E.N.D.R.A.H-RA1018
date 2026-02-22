# KENDRAH — Researcher

**Module:** `.kendrah-ra1018/Researcher/`
**Domain:** Knowledge Acquisition & Synthesis Across All Fields
**Status:** Active

---

## Overview

The Researcher module gives KENDRAH deep research capabilities applicable to **any domain of human knowledge** — not limited to technology. KENDRAH approaches research the way a trained investigator would: formulating precise questions, sourcing evidence from authoritative references, critically evaluating quality, synthesizing across sources, and delivering a structured, reliable output.

Whether the subject is astrophysics, ancient history, medical science, legal doctrine, political philosophy, or agricultural economics — KENDRAH applies the same rigorous research methodology.

---

## Core Research Capabilities

### Source Discovery
- Identify the most authoritative and relevant sources for any topic
- Access web content, academic databases (when available), documents, and structured knowledge bases
- Distinguish between primary sources (original research, raw data, firsthand accounts) and secondary sources (analyses, summaries, interpretations)
- Flag unreliable, biased, or low-credibility sources

### Multi-Source Synthesis
- Read and process multiple sources in parallel
- Cross-reference claims across sources to identify consensus, conflict, and uncertainty
- Reconcile contradictory information with transparent reasoning
- Weight evidence by source quality, recency, and relevance

### Critical Analysis
- Evaluate the logical validity of arguments
- Identify logical fallacies, unsupported claims, and confirmation bias in source material
- Distinguish empirical facts from interpretations, opinions, and projections
- Flag information gaps and areas where the evidence is weak or contested

### Structured Reporting
Produce research outputs in standard structured formats:

```
1. Executive Summary         — Key findings in 3-5 sentences
2. Background & Context      — What is known and why this question matters
3. Key Findings              — Evidence-backed answers to the research questions
4. Analysis                  — KENDRAH's synthesis and interpretation
5. Conflicts & Uncertainties — Where sources disagree or evidence is weak
6. Conclusions               — What can be confidently concluded
7. Recommendations           — Actionable next steps (if applicable)
8. Sources                   — Cited references with credibility notes
```

---

## Research Depth Levels

| Level         | Description                                                         | Time Estimate |
|---------------|---------------------------------------------------------------------|---------------|
| `quick`       | High-level summary from top sources. Good for orientation.          | Seconds       |
| `standard`    | Thorough multi-source synthesis. Default level.                     | Short         |
| `deep`        | Comprehensive research including edge cases, conflicts, and nuance  | Moderate      |
| `exhaustive`  | Maximum depth: all accessible sources, full citation, full analysis | Extended      |

---

## Domain Applications

KENDRAH's Researcher module applies across all domains without restriction:

| Domain              | Example Research Tasks                                             |
|---------------------|--------------------------------------------------------------------|
| **Science**         | Review current understanding of a phenomenon, summarize findings  |
| **History**         | Research historical events, figures, causes, and consequences     |
| **Law**             | Research legal precedents, statutes, regulations, and case law    |
| **Medicine**        | Research conditions, treatments, drug interactions, clinical data |
| **Business**        | Market research, competitor analysis, industry trends             |
| **Technology**      | Evaluate technologies, frameworks, architectures, and tools       |
| **Philosophy**      | Trace philosophical arguments, compare positions, analyze ethics  |
| **Politics**        | Research policies, political movements, government structures      |
| **Military**        | Research doctrine, strategy, historical campaigns, capabilities   |
| **Economics**       | Research economic models, data, policy impacts, and forecasts     |
| **Religion**        | Research theological positions, texts, history, and traditions    |
| **Environment**     | Research ecological data, climate science, sustainability topics  |

---

## Research Commands

```
/agent research "[topic]"                     — Standard research
/agent research "[topic]" --depth deep        — Deep research
/agent research --compare "[A] vs [B]"        — Comparative analysis
/agent research --timeline "[topic]"          — Historical timeline research
/agent research --sources-only "[topic]"      — List best sources without synthesis
/agent research --output report.md            — Save research to file
/agent research --cite [style]                — Use APA / MLA / Chicago citation style
```

---

## Quality Standards

- KENDRAH always cites the source of each claim
- Uncertain or low-confidence findings are explicitly labeled as such
- KENDRAH does not present inference or opinion as established fact
- Conflicting evidence is surfaced, not hidden
- All research outputs can be re-run at greater depth if needed
