# Agent Commands

**Category:** Autonomous Agent Invocation Commands
**Status:** Active

---

## Overview

Agent commands invoke KENDRAH's specialized autonomous agents for complex, multi-step, goal-directed tasks. Unlike single-skill commands, agent commands orchestrate multi-phase workflows that plan, execute, monitor, and deliver results end-to-end.

---

## Core Agent Commands

| Command                               | Agent Activated       | Description                                                |
|---------------------------------------|-----------------------|------------------------------------------------------------|
| `/agent code [goal]`                  | CodeAgent             | End-to-end software development from goal to working code |
| `/agent research [topic]`             | ResearchAgent         | Deep research, synthesis, and structured reporting         |
| `/agent security [target]`            | SecurityAgent         | Full security assessment and vulnerability report          |
| `/agent data [task]`                  | DataAgent             | Data ingestion, analysis, and visualization pipeline       |
| `/agent build [target]`               | BuildAgent            | Full project build, test, and deployment                   |
| `/agent monitor [target]`             | MonitorAgent          | Continuous monitoring with alerting                        |
| `/agent self-improve`                 | SelfImproveAgent      | Analyze and propose improvements to KENDRAH's config       |
| `/agent plan [goal]`                  | PlannerAgent          | Strategic multi-phase planning for any domain goal         |
| `/agent decide [question]`            | DecisionAgent         | Structured decision analysis and recommendation            |
| `/agent architect [system]`           | ArchitectAgent        | System or solution design and architecture planning        |

---

## Agent Flags

| Flag                    | Effect                                                             |
|-------------------------|--------------------------------------------------------------------|
| `--plan-only`           | Show the execution plan without running it                        |
| `--dry-run`             | Simulate execution without making real changes                    |
| `--verbose`             | Print detailed step-by-step output during execution               |
| `--confirm-each`        | Pause and ask for user confirmation before each major step        |
| `--spec [file]`         | Read task specification from a file instead of inline             |
| `--output [path]`       | Write agent results to a specific file or directory               |
| `--log`                 | Force logging of all agent actions to project history             |
| `--max-steps [n]`       | Limit the agent to a maximum of `n` execution steps               |

---

## CodeAgent Commands

| Command                                          | Description                                                   |
|--------------------------------------------------|---------------------------------------------------------------|
| `/agent code "build [app description]"`          | Generate a complete application                              |
| `/agent code --spec requirements.md`             | Build from a requirements file                               |
| `/agent code --task "add feature X to Y"`        | Add a specific feature to an existing project                |
| `/agent code --fix "bug description"`            | Find and fix a described bug across the codebase             |

---

## ResearchAgent Commands

| Command                                          | Description                                                   |
|--------------------------------------------------|---------------------------------------------------------------|
| `/agent research "[topic]"`                      | Full research on any topic with synthesized report           |
| `/agent research --depth [quick|deep|exhaustive]`| Set depth of research                                        |
| `/agent research --output report.md`             | Save research output to a file                               |
| `/agent research --compare "[A] vs [B]"`         | Comparative analysis of two subjects                         |

---

## SecurityAgent Commands

| Command                                          | Description                                                   |
|--------------------------------------------------|---------------------------------------------------------------|
| `/agent security --scan [target]`                | Full vulnerability scan of a target system or codebase       |
| `/agent security --report`                       | Generate a formatted security assessment report              |
| `/agent security --audit [directory]`            | Audit source code for security anti-patterns                 |
| `/agent security --monitor`                      | Start continuous security monitoring                         |

---

## MonitorAgent Commands

| Command                                          | Description                                                   |
|--------------------------------------------------|---------------------------------------------------------------|
| `/agent monitor --system`                        | Monitor OS-level metrics (CPU, RAM, disk, network)           |
| `/agent monitor --logs [service]`                | Tail and analyze logs from a service                         |
| `/agent monitor --url [endpoint]`                | Monitor an HTTP endpoint for uptime and response time        |
| `/agent monitor --alert [condition]`             | Set a custom alert condition                                  |
| `/agent monitor --stop`                          | Stop all active monitoring agents                            |

---

## SelfImproveAgent Commands

| Command                                          | Description                                                   |
|--------------------------------------------------|---------------------------------------------------------------|
| `/agent self-improve --analyze`                  | Analyze current skills, rules, and commands for gaps         |
| `/agent self-improve --propose`                  | Propose specific improvements (user approves before applying)|
| `/agent self-improve --apply [proposal-id]`      | Apply a previously proposed improvement                       |
| `/agent self-improve --history`                  | Show history of past self-improvements                       |

---

## Agent Status & Control

| Command                    | Description                                              |
|----------------------------|----------------------------------------------------------|
| `/agent status`            | Show all currently running agents and their progress    |
| `/agent stop [agent-name]` | Stop a specific running agent                           |
| `/agent stop all`          | Stop all running agents                                 |
| `/agent history`           | Show history of past agent runs and their outcomes      |
| `/agent retry [id]`        | Retry a previously failed agent run                     |
