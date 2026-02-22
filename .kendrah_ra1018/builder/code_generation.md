# Code Generation Pipeline

**Module:** Builder → Code Generation
**Primary Language:** Python
**Status:** Active

---

## Overview

This document defines how KENDRAH transforms a user's intent — whether typed, spoken, or inferred — into production-quality code. The pipeline is the backbone of KENDRAH's software development capability, covering the full journey from a natural language prompt to a validated, written file on disk.

---

## Pipeline Stages

### Stage 1: Intent Parsing
KENDRAH receives the user's instruction and identifies:
- **Action type:** Create, modify, extend, refactor, fix, generate
- **Target artifact:** Script, function, class, module, full app, API, CLI tool, etc.
- **Language:** Defaults to Python unless specified or inferred from project context
- **Scope:** Single function, single file, multi-file feature, or full application

### Stage 2: Context Loading
Before writing a single line of code, KENDRAH loads:
- Current session context from `memory/session_context.md`
- Relevant project history from `memory/project_history.md`
- Existing files in the target directory (if modifying or extending)
- Active rules from `rules/RULES.md`
- Applicable skills from `skills/`

This step ensures all generated code is consistent with the existing codebase, naming conventions, architecture, and project rules.

### Stage 3: Planning
KENDRAH decomposes the request into a concrete implementation plan:
- Files to create or modify
- Functions, classes, and modules to define
- Dependencies and imports required
- Order of implementation (dependencies first)
- Test coverage plan

For complex requests, KENDRAH surfaces the plan to the user before executing (`--plan-only` flag).

### Stage 4: Code Generation
KENDRAH writes code according to the plan:
- Generates idiomatic, well-documented Python (or specified language)
- Includes type annotations, docstrings, and inline comments where needed
- Produces clean code aligned to `rules/RULES.md` coding standards
- Handles edge cases and error conditions explicitly

### Stage 5: Validation
Before writing to disk, generated code is validated:

```python
import ast

def validate_python(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except SyntaxError as e:
        return False
```

For other languages, appropriate validators or linters are invoked. If validation fails, KENDRAH auto-corrects and re-validates.

### Stage 6: Test Generation (Optional, Auto-triggered)
If the generated code is a function, class, or API endpoint, KENDRAH automatically offers to generate corresponding tests. See `test_generation.md` for the full test pipeline.

### Stage 7: File Write
Validated code is written to the target file:
- New files are created in the correct location.
- Existing files are edited surgically (see `self_edit.md`).
- File paths and names follow project conventions.

### Stage 8: Memory Logging
The completed generation event is logged:
```
## [TIMESTAMP] Code Generation
- Action: Created `src/api/users.py`
- Description: Full CRUD API for user management using FastAPI
- Language: Python
- Files Created: src/api/users.py, src/models/user.py
- Tests Generated: tests/test_users.py
```

---

## Natural Language to Code Examples

| User Instruction                                          | KENDRAH Output                                             |
|-----------------------------------------------------------|------------------------------------------------------------|
| "Create a function to paginate a list"                    | `paginate(data: list, page: int, size: int) -> list`       |
| "Build a REST API for task management"                    | FastAPI app with routes: GET/POST/PUT/DELETE `/tasks`      |
| "Write a script to rename all files in a folder"         | Python script using `pathlib` and user-defined pattern    |
| "Create a class for a bank account with deposits"        | `BankAccount` class with `deposit`, `withdraw`, `balance` |
| "Build a CLI tool to compress images in a directory"     | Python `argparse`-based CLI using `Pillow`                |

---

## Code Generation Modes

| Mode           | Trigger                        | Behavior                                             |
|----------------|--------------------------------|------------------------------------------------------|
| `interactive`  | Default                        | Generates, shows output, asks for feedback           |
| `silent`       | `--silent`                     | Generates and writes to disk without preview         |
| `plan-only`    | `--plan-only`                  | Shows implementation plan without generating code    |
| `dry-run`      | `--dry-run`                    | Generates code but does not write to disk            |
| `batch`        | Multiple files in one command  | Processes all files sequentially, logs each          |

---

## Supported Output Types

- Python scripts (`.py`)
- Python packages (directory with `__init__.py`)
- FastAPI / Flask / Django applications
- CLI tools (argparse, click, typer)
- HTML / CSS / JavaScript files
- Configuration files (`.yaml`, `.toml`, `.json`, `.env`)
- Dockerfiles and `docker-compose.yml`
- Shell scripts (`.sh`, `.ps1`)
- Markdown documentation
- Test files (`test_*.py`, `*_test.py`)
