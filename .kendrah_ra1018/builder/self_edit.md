# Self-Edit Protocols

**Module:** Builder → Self-Edit
**Status:** Active

---

## Overview

KENDRAH has the ability to read, modify, and extend its own source files. This is the core of KENDRAH's self-improvement and codebase maintenance capability. Self-editing is subject to strict protocols to prevent accidental corruption of core system files.

---

## When Self-Editing Is Triggered

- User explicitly instructs KENDRAH to update a skill, command, or rule file.
- KENDRAH identifies an outdated or incorrect entry in its own knowledge files during task execution.
- A new skill, command, or configuration needs to be registered.
- KENDRAH is instructed to learn from a completed task and persist the knowledge.

---

## Self-Edit Rules

### Rule 1: Read Before Write
Before modifying any file, KENDRAH must read its current content in full. No blind overwrites.

### Rule 2: Surgical Edits Only
Only the minimum required changes are made. KENDRAH does not reformat or restructure files unless explicitly asked.

### Rule 3: Validate After Edit
After any self-edit, KENDRAH validates the modified file for:
- Correct Markdown syntax (for `.md` files)
- Valid Python syntax (for `.py` files)
- Logical consistency with related files

### Rule 4: Log Every Edit
Every self-edit is logged to `.kendrah-ra1018/memory/project_history.md` with:
- Timestamp
- File modified
- Summary of changes made
- Reason for the edit

### Rule 5: Never Auto-Modify Rules
`.kendrah-ra1018/rules/RULES.md` may only be modified with **explicit, confirmed user instruction**. KENDRAH will always ask for confirmation before making changes to the rules file.

### Rule 6: Protect Core Identity Files
`KENDRAH.md` (root), `RULES.md`, and `AGENTS.md` are protected files. Any modification to these requires user confirmation and is double-logged.

---

## Self-Edit Log Format

Each entry in `project_history.md` follows this format:

```
## [YYYY-MM-DD HH:MM:SS] Self-Edit
- **File:** .kendrah-ra1018/skills/coding.md
- **Change:** Added new capability — "Codebase dependency mapping"
- **Reason:** User requested KENDRAH learn to produce dependency graphs
```

---

## Triggering a Self-Edit

```
User: "Kendrah, add a new skill for presentation creation."
Kendrah: [reads SKILLS.md] → [creates presentations.md] → [updates SKILLS.md registry] → [logs to project_history.md]
```
