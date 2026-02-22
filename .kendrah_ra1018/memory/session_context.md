# Session Context

**File:** `.kendrah-ra1018/memory/session_context.md`
**Scope:** Current Session Only
**Auto-cleared on:** `/reset` or new session start
**Last Updated:** [auto-populated by KENDRAH]

---

## Purpose

This file is the live working memory for the current KENDRAH session. It tracks what is happening right now — the active task, open files, recent commands, decisions made, and any intermediate state needed to continue work seamlessly without repeating context.

KENDRAH reads this file at the start of every response within a session. It is updated continuously as the session progresses.

---

## Active Session State

```yaml
session_id: ""
started_at: ""
active_task: ""
task_status: idle  # idle | planning | executing | reviewing | complete
current_domain: ""  # software | research | security | data | planning | etc.
```

---

## Current Task

```
Task: [KENDRAH will populate this when a task begins]
Status: Not started
Priority: Normal
Assigned Agent: None
```

---

## Active Files

Files currently open, being edited, or referenced in this session:

```
[No active files — session not started]
```

---

## Recent Commands

The last 10 commands issued this session:

```
[No commands yet]
```

---

## Decisions Made This Session

Key decisions, choices, or preferences established during this session:

```
[No decisions recorded yet]
```

**Examples of what gets recorded here:**
- "User chose FastAPI over Flask for this project."
- "Database: PostgreSQL with SQLAlchemy ORM."
- "Authentication: JWT with 24-hour token expiry."
- "Deploy target: Docker + DigitalOcean."

---

## Pending Items

Tasks or follow-ups that are planned but not yet executed:

```
[None]
```

---

## User Preferences (This Session)

Preferences expressed or inferred during this session:

```
Output verbosity: Normal
Code style: [detected from existing project or user instruction]
Confirmation mode: Default (only for destructive actions)
Language override: None (defaulting to Python)
```

---

## Notes

Free-form notes KENDRAH or the user has added during the session:

```
[No notes]
```

---

## Session Context Format Reference

When KENDRAH populates this file during a real session, a typical entry looks like this:

```markdown
## Active Session State
session_id: "ks-20240315-001"
started_at: "2024-03-15 09:14:22"
active_task: "Build REST API for task management app"
task_status: executing
current_domain: software

## Current Task
Task: Build a FastAPI-based REST API for a task management application
Status: In progress — generated models and routes, writing tests next
Priority: High
Assigned Agent: CodeAgent

## Active Files
- src/api/tasks.py (created — CRUD routes)
- src/models/task.py (created — SQLAlchemy model)
- tests/test_tasks.py (in progress)

## Decisions Made This Session
- Framework: FastAPI
- Database: PostgreSQL via SQLAlchemy
- Auth: JWT (to be added in next session)
- Deployment target: Docker

## Pending Items
- Write unit tests for task routes
- Add authentication middleware
- Generate Dockerfile
```
