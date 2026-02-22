# KENDRAH Builder System

**Location:** `.kendrah-ra1018/builder/`
**Status:** Active

---

## Overview

The Builder system governs how KENDRAH generates, edits, tests, and deploys code. It defines the pipeline from intent to execution — from a natural language command all the way to a running, tested application or updated codebase.

---

## Builder Components

| File                  | Purpose                                            |
|-----------------------|----------------------------------------------------|
| `code_generation.md`  | Pipeline for generating code from prompts          |
| `self_edit.md`        | Protocols for KENDRAH editing its own files        |
| `test_generation.md`  | Automated test creation and coverage analysis      |
| `deployment.md`       | Environment setup, containerization, and deploy    |

---

## Code Generation Pipeline

```
User Intent (Natural Language)
        ↓
Intent Parsing & Clarification
        ↓
Context Loading (codebase scan + memory)
        ↓
Code Generation (Python-first)
        ↓
Syntax & Logic Validation
        ↓
Test Generation (if applicable)
        ↓
File Write / Self-Edit
        ↓
Log to Memory
```

---

## Self-Edit Protocol Summary

KENDRAH follows strict rules when editing its own files:

1. **Never modify `RULES.md` without explicit user confirmation.**
2. All self-edits are logged immediately to `.kendrah-ra1018/memory/project_history.md`.
3. Before editing, KENDRAH reads the target file in full to understand current state.
4. Edits are surgical — only the minimum necessary changes are made.
5. After editing, KENDRAH validates the file for syntax errors and consistency.

---

## Smart Rules

KENDRAH respects project-level rules defined in `.kendrah-ra1018/rules/RULES.md`. These rules are automatically applied during all code generation and editing operations. Rules can be added, modified, or removed by the user at any time.

---

## Memory Integration

All build operations are recorded:
- **Session context** is stored in `.kendrah-ra1018/memory/session_context.md`
- **Project history** (decisions, edits, builds) is stored in `.kendrah-ra1018/memory/project_history.md`
- Memory allows KENDRAH to avoid repeating itself and to build on past work intelligently.
