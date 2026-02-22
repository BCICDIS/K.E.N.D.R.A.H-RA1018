# KENDRAH Agent System

**Location:** `.kendrah-ra1018/agents/`
**Status:** Active

---

## Overview

KENDRAH operates a modular agent system — a collection of specialized autonomous sub-agents that handle specific domains of complex, multi-step tasks. Agents can be invoked manually by the user or automatically triggered by KENDRAH when a task requires sustained, multi-phase execution.

Agents differ from skills in that they are **autonomous workflows**, not just capability definitions. An agent takes a goal, plans how to achieve it, executes across multiple steps, monitors its own progress, and delivers a final result.

---

## Available Agents

| Agent              | Trigger               | Domain                                                |
|--------------------|-----------------------|-------------------------------------------------------|
| `CodeAgent`        | `/agent code`         | End-to-end code generation, refactoring, and testing |
| `ResearchAgent`    | `/agent research`     | Information gathering, analysis, and reporting       |
| `SecurityAgent`    | `/agent security`     | Vulnerability scanning and security assessment       |
| `DataAgent`        | `/agent data`         | Data ingestion, analysis, and visualization pipeline |
| `BuildAgent`       | `/agent build`        | Full project build, test, and deployment pipeline    |
| `MonitorAgent`     | `/agent monitor`      | Continuous system or log monitoring with alerts      |
| `SelfImproveAgent` | `/agent self-improve` | Analyze and improve KENDRAH's own configuration      |

---

## Agent Lifecycle

```
User Command (goal statement)
        ↓
Goal Parsing & Task Decomposition
        ↓
Sub-task Planning (ordered steps)
        ↓
Sequential/Parallel Execution
        ↓
Progress Monitoring & Error Recovery
        ↓
Result Compilation & Delivery
        ↓
Memory Logging
```

---

## CodeAgent

The CodeAgent handles complete software development workflows end-to-end.

**Capabilities:**
- Parse a feature request and decompose it into files, functions, and modules to create.
- Generate the full implementation across multiple files.
- Write tests for all generated code.
- Run tests, capture failures, and auto-fix issues.
- Commit the completed feature with a descriptive commit message.

**Example Invocation:**
```
User: "Kendrah, build me a user authentication system with email and password login."
→ CodeAgent activates → plans files → generates code → writes tests → runs tests → commits.
```

---

## SelfImproveAgent

The SelfImproveAgent allows KENDRAH to evaluate and enhance its own configuration files, skill definitions, and rules based on operational patterns.

**Capabilities:**
- Review skill files for accuracy and completeness.
- Propose new skills or commands based on frequently requested tasks not covered by existing skills.
- Identify rules that conflict or are redundant and suggest consolidation.
- Present improvement proposals to the user for approval before applying.

**Safety:** SelfImproveAgent never applies changes without explicit user approval.

---

## Invoking Agents

Agents can be triggered by natural language or structured command:

```
Natural language: "Kendrah, build the entire backend for my app."
Structured:       /agent build --target backend --spec requirements.md
```

Agents accept a `--plan-only` flag to show the planned steps without executing:
```
/agent code --task "add pagination to user list API" --plan-only
```
