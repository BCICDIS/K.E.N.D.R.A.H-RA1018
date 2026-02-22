# KENDRAH — Executor

**Module:** `.kendrah-ra1018/executor/`
**Domain:** Universal Task Execution Across All Domains
**Status:** Active

---

## Overview

The Executor is KENDRAH's action layer — the module responsible for taking a plan, instruction, or decision and actually making it happen. While other modules reason, research, design, and plan, the Executor **does**.

The Executor applies to all domains without exception. Whether the task is writing code, processing data, running a system command, generating a report, sending a notification, controlling hardware, or executing a multi-step agent workflow — the Executor is the runtime that carries it out.

---

## Executor Principles

### 1. Intention-to-Action Fidelity
The Executor always executes exactly what was intended — no more, no less. Before acting, it confirms its interpretation of the instruction. For destructive or irreversible actions, it always requests explicit confirmation.

### 2. Atomic Execution
Each task is executed as an atomic unit — it either completes fully and correctly, or it fails cleanly and rolls back where possible. Partial execution that leaves systems in an inconsistent state is never acceptable.

### 3. Ordered Execution
When a task requires multiple steps, the Executor processes them in dependency order. No step begins until all its prerequisites are confirmed complete.

### 4. Parallel Execution (where safe)
When tasks have no interdependencies, the Executor runs them concurrently to maximize throughput.

### 5. Execution Logging
Every executed action is logged immediately upon completion (or failure) to `memory/project_history.md`. Logs include what was done, the result, and any errors.

### 6. Error Recovery
When a step fails, the Executor:
- Analyzes the failure
- Attempts up to 3 automatic recovery strategies
- If unrecoverable, pauses and alerts the user with a clear explanation

---

## Execution Domains

The Executor handles action across all of KENDRAH's domains:

| Domain          | Example Execution Actions                                         |
|-----------------|-------------------------------------------------------------------|
| **Software**    | Generate file, run script, install package, start service        |
| **Hardware**    | Send GPIO command, read sensor, connect serial device            |
| **Data**        | Run query, process dataset, generate visualization               |
| **Security**    | Run scan, apply firewall rule, encrypt file                      |
| **Automation**  | Execute scheduled job, trigger workflow, run batch process       |
| **Research**    | Execute search, fetch URL, synthesize sources                    |
| **Planning**    | Write plan file, update task status, log milestone               |
| **Decisions**   | Run analysis, score options, write ADR                           |
| **Architecture**| Generate diagram, write design doc, log architectural decision   |
| **Military**    | Simulate tactical scenario, generate operational plan            |
| **Politics**    | Analyze policy, generate position paper                         |
| **Business**    | Generate financial model, write business document               |
| **Science**     | Execute statistical analysis, generate report                    |
| **Physics**     | Run simulation, compute physics equations                        |
| **Theology**    | Search and synthesize scripture, generate doctrinal analysis     |

---

## Execution Modes

| Mode              | Description                                                         |
|-------------------|---------------------------------------------------------------------|
| `immediate`       | Execute now, no preview — default for simple, safe actions         |
| `preview`         | Show what will be executed before acting — default for complex tasks|
| `dry-run`         | Simulate execution completely without making real changes          |
| `step-by-step`    | Execute one step, pause, show result, proceed on confirmation      |
| `background`      | Execute asynchronously without blocking the conversation           |
| `scheduled`       | Execute at a specified time or on a cron schedule                  |
| `conditional`     | Execute only if a specified condition is met at runtime            |

---

## Execution Pipeline

```
Receive Instruction
        ↓
Parse & Validate (is this executable?)
        ↓
Confirm (if complex, destructive, or ambiguous)
        ↓
Load Required Skills, Agents, Tools
        ↓
Execute Step 1
    → Log result
    → Handle error if present
        ↓
Execute Step 2 ... N
        ↓
Compile Final Output
        ↓
Deliver to User
        ↓
Log Full Execution to project_history.md
```

---

## Execution Commands

```
/execute "[instruction]"                    — Execute a task or instruction directly
/execute --mode [preview|dry-run|step]      — Set execution mode before running
/execute --scheduled "[cron or datetime]"   — Schedule execution for a future time
/execute --background                       — Run task in background
/execute --confirm-each                     — Pause and confirm before each step
/exec status                                — Show status of running or recent executions
/exec cancel [id]                           — Cancel a running or scheduled execution
/exec retry [id]                            — Retry a failed execution
/exec log [id]                              — Show full log for a specific execution
```

---

## Execution Safety Rules

- **Never execute irreversible actions without explicit confirmation** (deleting files, overwriting data, sending communications, modifying production systems)
- **Always log before and after destructive operations**
- **If execution fails mid-way through a multi-step task**, report exactly where and why — never silently stop
- **Respect the `--dry-run` flag absolutely** — when dry-run is set, zero real-world changes are made
- **Honor resource limits** — no single execution should monopolize system resources without user awareness
