# KENDRAH — Decision

**Module:** `.kendrah-ra1018/Decision/`
**Domain:** Structured Decision Analysis & Recommendation Across All Domains
**Status:** Active

---

## Overview

The Decision module gives KENDRAH the ability to support, structure, and analyze decisions of any kind — from technical choices to strategic business decisions, personal life decisions, military command decisions, policy choices, or ethical dilemmas.

KENDRAH does not make decisions for you — it provides structured analysis that makes the decision clearer, more informed, and less susceptible to cognitive bias. The final decision always belongs to the user.

---

## Decision Types Supported

| Decision Type              | Example                                                         |
|----------------------------|-----------------------------------------------------------------|
| **Technical**              | Choose between two frameworks, architectures, or tools         |
| **Strategic**              | Determine the best market entry strategy                        |
| **Operational**            | Select the best process for a recurring workflow               |
| **Resource Allocation**    | How to allocate budget, time, or personnel across projects      |
| **Risk-Based**             | Whether to proceed given identified risks                       |
| **Ethical**                | Analyze the ethical dimensions of an action or policy          |
| **Political**              | Policy trade-off analysis, stakeholder impact assessment        |
| **Military**               | Tactical and strategic option analysis                          |
| **Personal**               | Career choices, major life decisions, priority setting          |
| **Scientific**             | Hypothesis selection, methodology choice                        |

---

## Decision Analysis Frameworks

KENDRAH applies the most appropriate framework for the decision type:

### 1. Pros/Cons Analysis
Simple enumeration of advantages and disadvantages for each option.
Best for: Quick, low-stakes decisions.

### 2. Weighted Criteria Matrix
Options are scored against weighted criteria. Produces a numerical ranking.
Best for: Multi-option decisions with clear, comparable criteria.

```
Criteria         Weight   Option A   Option B   Option C
Performance      30%      8          6          9
Cost             25%      9          7          5
Ease of Use      20%      7          9          6
Scalability      25%      6          5          9
---
Weighted Score            7.45       6.50       7.25
```

### 3. Cost-Benefit Analysis
Quantifies the expected costs and benefits of each option over a defined time horizon.
Best for: Financial decisions, investment choices, policy evaluation.

### 4. Risk Analysis
Identifies risks for each option, assesses likelihood and impact, and computes an expected risk score.
Best for: High-stakes decisions under uncertainty.

```
Risk                        Likelihood   Impact   Score
Data breach on cloud         Medium       High     High
Vendor lock-in               High         Medium   High
Performance degradation      Low          High     Medium
```

### 5. SWOT Analysis
Strengths, Weaknesses, Opportunities, Threats for each option or course of action.
Best for: Strategic decisions, organizational choices.

### 6. Decision Tree
Maps out decision branches and outcomes, including probabilities and expected values.
Best for: Sequential decisions under uncertainty with quantifiable outcomes.

### 7. Ethical Framework Analysis
Evaluates a decision through multiple ethical lenses:
- **Consequentialist:** What produces the best outcomes?
- **Deontological:** What duties or rules apply?
- **Virtue Ethics:** What would a person of good character do?
- **Justice/Fairness:** Who is affected and how fairly?

---

## Decision Output Format

```markdown
## Decision Analysis: [Decision Title]

### Context
[What situation requires this decision and why it matters]

### Options
- Option A: [Description]
- Option B: [Description]
- Option C: [Description]

### Criteria & Weights
[Criteria with justification for weighting]

### Analysis
[Framework applied — scored matrix, risk table, etc.]

### Recommendation
**Recommended Option: [X]**
Rationale: [Why this option scores best against the criteria, given the constraints]

### Risks of Recommended Option
[Key risks and how to mitigate them]

### Conditions That Would Change This Recommendation
[If X changes, Option Y becomes preferable because...]
```

---

## Commands

```
/decide "[decision question]"                      — Full structured decision analysis
/decide --options "[A], [B], [C]"                  — Analyze specified options
/decide --framework [pros-cons|matrix|risk|swot]   — Use a specific framework
/decide --ethical "[action or policy]"             — Ethical dimension analysis
/decide --recommend "[situation]"                  — Direct recommendation with rationale
/decide --adr "[decision]"                         — Save as Architecture Decision Record
```

---

## Example Tasks

- "Kendrah, help me decide whether to build this feature in-house or use a third-party API."
- "Kendrah, analyze the strategic trade-offs between entering the Asian market now versus waiting 18 months."
- "Kendrah, what are the ethical considerations of implementing mandatory biometric employee tracking?"
- "Kendrah, given these three cloud providers, which best fits our requirements? Apply a weighted matrix."
- "Kendrah, we need to cut 20% of the project budget. Help me decide what to deprioritize."
