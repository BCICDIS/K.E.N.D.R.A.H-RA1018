# KENDRAH Memory System

**Location:** `.kendrah-ra1018/memory/`
**Status:** Active

---

## Overview

KENDRAH maintains a persistent memory system that stores session context, project history, and long-term knowledge. Memory allows KENDRAH to reduce repetitive input, build on past work intelligently, and maintain continuity across multiple sessions.

---

## Memory Files

| File                    | Scope       | Description                                        |
|-------------------------|-------------|----------------------------------------------------|
| `session_context.md`    | Session     | Active conversation context, current task state    |
| `project_history.md`    | Persistent  | All decisions, edits, builds, and key milestones  |

---

## How Memory Works

### Session Context
- Loaded at the start of each KENDRAH session.
- Tracks: current task, recent commands, active files, and intermediate results.
- Cleared when the user issues `/reset` or starts a new session.
- Updated continuously as tasks progress.

### Project History
- Persists across all sessions indefinitely.
- Contains: self-edit logs, build records, notable decisions, and project milestones.
- Can be queried: "Kendrah, what changes did we make to the API last week?"
- Never auto-cleared — can only be archived or pruned by user command.

---

## Memory Query Examples

```
User: "Kendrah, what were we working on yesterday?"
→ KENDRAH reads project_history.md and returns a summary of recent activity.

User: "Kendrah, what did you change in the authentication module?"
→ KENDRAH filters history by file reference and returns relevant edit logs.

User: "Kendrah, remind me what tech stack we decided on."
→ KENDRAH retrieves the stored tech stack decision from session or project history.
```

---

## Memory Storage Format

### session_context.md
```markdown
## Active Session — [YYYY-MM-DD]
- **Current Task:** Building REST API for user management
- **Active Files:** src/api/users.py, src/models/user.py
- **Last Command:** /generate function — create_user endpoint
- **Notes:** Using FastAPI + PostgreSQL. JWT auth decided.
```

### project_history.md
```markdown
## [YYYY-MM-DD HH:MM] Build Event
- **Action:** Generated `src/api/users.py`
- **Description:** Created full CRUD API for user management
- **Files Modified:** src/api/users.py (created), src/models/user.py (created)

## [YYYY-MM-DD HH:MM] Self-Edit
- **File:** .kendrah-ra1018/skills/coding.md
- **Change:** Added dependency graph generation capability
- **Reason:** User instruction
```

---

## Clearing Memory

| Command                     | Effect                                           |
|-----------------------------|--------------------------------------------------|
| `/reset`                    | Clears session context only                      |
| `/memory clear session`     | Same as `/reset`                                 |
| `/memory archive history`   | Archives project history to a dated backup file  |
| `/memory clear all`         | Clears both session and history (irreversible)   |
