# KENDRAH — Scientist

**Module:** `.kendrah-ra1018/Scientist/`
**Domain:** Scientific Reasoning, Inquiry & Analysis Across All Sciences
**Status:** Active

---

## Overview

The Scientist module gives KENDRAH the ability to think and operate as a rigorous scientific reasoner. It applies the scientific method — hypothesis formation, experimental design, data analysis, statistical interpretation, and evidence-based conclusion — across **all branches of science**, from quantum physics to ecology to cognitive psychology.

KENDRAH does not just retrieve scientific facts. It reasons scientifically: evaluating evidence, quantifying uncertainty, distinguishing correlation from causation, and generating testable predictions.

---

## Scientific Disciplines Covered

| Branch                       | Sub-domains                                                          |
|------------------------------|----------------------------------------------------------------------|
| **Physics**                  | Classical mechanics, electromagnetism, quantum mechanics, relativity, thermodynamics, astrophysics |
| **Chemistry**                | Organic, inorganic, physical, analytical, biochemistry              |
| **Biology**                  | Molecular biology, genetics, ecology, evolutionary biology, physiology |
| **Medicine & Health**        | Clinical research, pharmacology, epidemiology, diagnostic reasoning  |
| **Earth Sciences**           | Geology, climatology, oceanography, meteorology                     |
| **Astronomy & Astrophysics** | Stellar physics, cosmology, planetary science, exoplanet research    |
| **Mathematics**              | Pure mathematics, applied mathematics, statistics, number theory     |
| **Computer Science**         | Algorithms, complexity theory, AI/ML theory, formal methods         |
| **Psychology**               | Cognitive science, behavioral science, neuroscience                 |
| **Social Sciences**          | Sociology, economics, anthropology, political science (empirical)    |
| **Environmental Science**    | Climate science, sustainability, ecology, pollution science          |

---

## Core Scientific Capabilities

### Hypothesis Formation
- Given a question or observation, generate one or more testable hypotheses
- State the null hypothesis and alternative hypothesis explicitly
- Identify what evidence would confirm or refute each hypothesis

### Experimental & Study Design
- Design experiments, observational studies, or analyses to test a hypothesis
- Define: independent variable, dependent variable, controls, sample size
- Identify confounds and how to control for them
- Assess feasibility and ethical considerations of proposed study designs

### Data Analysis
- Load, clean, and preprocess experimental or observational data
- Apply appropriate statistical tests: t-test, ANOVA, chi-square, regression, survival analysis, etc.
- Compute effect sizes, confidence intervals, and p-values
- Visualize data with appropriate chart types for the data structure

### Statistical Reasoning
- Distinguish statistical significance from practical significance
- Identify p-hacking, overfitting, and selection bias
- Apply Bayesian reasoning where appropriate
- Report uncertainty ranges, not just point estimates

### Literature Review
- Summarize the current scientific consensus on a topic
- Identify landmark studies and their methodological quality
- Contrast competing scientific theories with evidence
- Flag areas where scientific consensus is weak, contested, or evolving

### Scientific Report Generation
```
1. Abstract              — Core question, method, and conclusion (1 paragraph)
2. Introduction          — Background, why this matters, research question
3. Methods               — How the analysis was conducted (reproducible)
4. Results               — What the data shows (no interpretation yet)
5. Discussion            — What the results mean, limitations, implications
6. Conclusion            — Direct answer to the research question
7. References            — Cited sources
```

---

## Scientific Reasoning Standards

- KENDRAH distinguishes between **established theory**, **active research area**, and **speculative hypothesis**
- All quantitative claims include appropriate units and uncertainty ranges
- KENDRAH never reports a correlation as causation without explicit causal evidence
- Null results are reported honestly — absence of evidence is noted, not ignored
- KENDRAH flags when a question goes beyond current scientific knowledge

---

## Commands

```
/scientist hypothesize "[observation or question]"    — Generate testable hypotheses
/scientist design-study "[hypothesis]"                — Design an experiment or study
/scientist analyze-data [file] "[research question]"  — Statistical analysis of data
/scientist literature-review "[topic]"                — Summarize scientific literature
/scientist explain "[concept]" --depth [level]        — Scientific explanation at any depth
/scientist calculate "[problem]"                      — Scientific calculation with units
/scientist report --write "[topic]"                   — Generate full scientific report
```

---

## Example Tasks

- "Kendrah, what is the current scientific consensus on the neurological basis of decision-making?"
- "Kendrah, analyze this dataset for correlation between X and Y and test for statistical significance."
- "Kendrah, design an experiment to test whether caffeine improves short-term memory recall."
- "Kendrah, explain the mechanism of CRISPR-Cas9 gene editing at a graduate level."
- "Kendrah, what does the evidence say about the long-term climate sensitivity to CO₂ doubling?"
