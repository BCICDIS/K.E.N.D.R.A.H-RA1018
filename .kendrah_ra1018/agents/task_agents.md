# Task Agents

**Module:** Agents → Task Agents
**Status:** Active

---

## Overview

Task Agents are KENDRAH's specialized autonomous execution units. Each agent is purpose-built for a specific problem domain. When invoked, an agent takes a high-level goal, decomposes it into ordered steps, executes each step autonomously, monitors its own progress, handles errors, and delivers a final output — all with minimal user intervention.

Task agents are the most powerful mode of KENDRAH operation: they represent KENDRAH acting not just as a tool, but as an autonomous collaborator.

---

## Agent Registry

| Agent Name           | Trigger Command            | Domain                                            |
|----------------------|----------------------------|---------------------------------------------------|
| `CodeAgent`          | `/agent code`              | End-to-end software development                  |
| `ResearchAgent`      | `/agent research`          | Multi-source research and intelligence synthesis  |
| `SecurityAgent`      | `/agent security`          | Vulnerability assessment and threat analysis      |
| `DataAgent`          | `/agent data`              | Data ingestion, analysis, and visualization       |
| `BuildAgent`         | `/agent build`             | Project build, test, and deployment pipeline      |
| `MonitorAgent`       | `/agent monitor`           | Continuous system and log monitoring              |
| `PlannerAgent`       | `/agent plan`              | Strategic and operational planning                |
| `DecisionAgent`      | `/agent decide`            | Structured decision support and analysis          |
| `ArchitectAgent`     | `/agent architect`         | System and solution design                        |
| `ResearcherAgent`    | `/agent researcher`        | Broad knowledge research across any domain        |
| `SelfImproveAgent`   | `/agent self-improve`      | KENDRAH self-analysis and capability improvement  |
| `WriterAgent`        | `/agent write`             | Long-form writing, reports, and documentation     |
| `ScientistAgent`     | `/agent scientist`         | Hypothesis-driven analysis and scientific inquiry |

---

## Agent Lifecycle Detail

Every task agent follows this lifecycle:

```
1. RECEIVE GOAL
   ↓ Parse the user's intent, constraints, and success criteria

2. LOAD CONTEXT
   ↓ Read session memory, project history, applicable skills and rules

3. DECOMPOSE
   ↓ Break the goal into an ordered list of concrete sub-tasks

4. PLAN (optional user review with --plan-only)
   ↓ Present the plan: steps, expected outputs, estimated complexity

5. EXECUTE
   ↓ Run each sub-task sequentially (or in parallel where safe)
   ↓ Use the appropriate skills for each step
   ↓ Log each completed step to project_history.md

6. MONITOR & RECOVER
   ↓ If a step fails, analyze the error
   ↓ Attempt auto-recovery (up to 3 retries)
   ↓ If unrecoverable, alert the user and pause

7. COMPILE OUTPUT
   ↓ Aggregate results from all steps into a final, coherent output

8. DELIVER
   ↓ Present the output to the user (file, report, message, or summary)

9. LOG
   ↓ Record the full agent run in project_history.md as AGENT_RUN event
```

---

## CodeAgent — Detail

**Purpose:** Complete software feature and application development.

**What it does:**
1. Parses the feature or application request
2. Plans the file structure and component breakdown
3. Generates all source files in dependency order
4. Writes tests for every generated module
5. Runs the test suite and fixes failures
6. Commits the completed work with a descriptive Git message

**Example:**
```
/agent code "Build a user registration system with email verification"

→ Plan:
  1. Create User model (src/models/user.py)
  2. Create users API routes (src/api/users.py)
  3. Create email service (src/services/email.py)
  4. Create registration flow with token generation
  5. Write tests (tests/test_users.py, tests/test_email.py)
  6. Run tests → fix failures
  7. Git commit: "feat: add user registration with email verification"
```

---

## ResearchAgent — Detail

**Purpose:** Deep, multi-source research synthesis on any topic.

**What it does:**
1. Breaks the research topic into key sub-questions
2. Queries available sources: web, local documents, databases, APIs
3. Synthesizes findings across sources, resolving conflicts
4. Structures the output as a formatted research report
5. Highlights key conclusions, evidence, and uncertainties

**Domains:** Technology, science, history, law, business, medicine, policy — any domain.

**Example:**
```
/agent research "The impact of quantum computing on modern cryptography"

→ Output: Structured research report with:
  - Executive summary
  - Current state of quantum computing
  - Vulnerable cryptographic algorithms
  - Post-quantum cryptography standards (NIST)
  - Timeline and risk assessment
  - Recommended actions
```

---

## PlannerAgent — Detail

**Purpose:** Strategic and operational planning for any goal.

**What it does:**
1. Clarifies the goal and constraints
2. Identifies key milestones and phases
3. Decomposes into actionable tasks with dependencies
4. Assigns effort estimates and priorities
5. Outputs a structured plan document (Markdown or task list)

**Domains:** Project management, product development, personal goals, operations, campaigns — any domain.

---

## DecisionAgent — Detail

**Purpose:** Structured analysis of a decision or choice.

**What it does:**
1. Identifies the options and decision criteria
2. Evaluates each option against the criteria
3. Applies frameworks: pros/cons, cost-benefit, risk analysis, SWOT
4. Presents a clear recommendation with rationale
5. Documents the decision in project history

**Domains:** Technology choices, business strategy, resource allocation, policy, personal decisions.

---

## ArchitectAgent — Detail

**Purpose:** Design systems, solutions, and technical architectures.

**What it does:**
1. Understands the requirements and constraints
2. Proposes architecture options with trade-offs
3. Produces system diagrams (as Markdown/ASCII or image)
4. Defines component boundaries, interfaces, and data flows
5. Outputs an architecture design document

**Domains:** Software systems, infrastructure, organizational design, data pipelines, network topology.

---

## ScientistAgent — Detail

**Purpose:** Apply scientific reasoning to any domain of inquiry.

**What it does:**
1. Frames the question as a hypothesis
2. Identifies available data or literature
3. Designs an analysis or experiment plan
4. Executes analysis (data processing, statistical testing, modeling)
5. Draws evidence-based conclusions with confidence levels
6. Outputs a structured scientific report

**Domains:** Physical sciences, biology, social sciences, engineering, data science, medicine.

---

## WriterAgent — Detail

**Purpose:** Long-form writing, structured documents, and content generation.

**What it does:**
1. Understands the subject, audience, tone, and format
2. Produces an outline for user review (if `--plan-only`)
3. Writes section by section with consistent voice and structure
4. Self-edits for clarity, coherence, and style
5. Outputs a complete document in the requested format

**Domains:** Technical reports, academic papers, business proposals, articles, books, documentation, scripts.
