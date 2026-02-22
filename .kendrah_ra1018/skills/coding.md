# Skill: Programming & Code Generation

**Domain:** Software Development
**Primary Language:** Python
**Status:** Active

---

## Overview

KENDRAH is a full-spectrum software development engine. It can read, write, refactor, debug, test, and self-edit code across multiple languages with a primary focus on Python. KENDRAH understands your codebase as a whole — not just individual files — and applies context-aware intelligence to generate production-quality code from natural language instructions or structured prompts.

---

## Capabilities

### Code Generation
- Generate complete scripts, modules, classes, functions, and entire applications from natural language descriptions.
- Produce boilerplate-free, clean, idiomatic code aligned to project conventions.
- Generate code templates and reusable component libraries.
- Create full-stack applications spanning frontend, backend, and database layers.

### Context-Aware Code Assistance
- Analyze the entire codebase to understand project structure, dependencies, and architecture.
- Provide inline code suggestions that align with existing patterns, naming conventions, and logic.
- Auto-complete functions, methods, class definitions, and docstrings.
- Understand custom project rules defined in `.kendrah-ra1018/rules/RULES.md`.

### Code Refactoring & Optimization
- Simplify complex logic into readable, maintainable code.
- Identify and remove dead code, duplicate logic, and unused imports.
- Optimize code for performance: reduce time complexity, memory usage, and unnecessary computations.
- Enforce coding standards and style guidelines automatically.

### AI-Powered Debugging
- Detect bugs and logic errors in real time by analyzing code flow.
- Analyze stack traces and suggest targeted fixes, including dependency or configuration issues.
- Predict potential errors before they occur based on coding patterns.
- Identify error-prone sections and suggest preventative rewrites.

### Test Generation & Execution
- Automatically generate unit tests, integration tests, and end-to-end tests for existing code.
- Assess test coverage and flag untested code paths.
- Run tests and report results, failures, and coverage metrics.

### Codebase Self-Editing
- KENDRAH can modify its own source files under `.kendrah-ra1018/` as instructed.
- Follows strict self-edit protocols defined in `.kendrah-ra1018/builder/self_edit.md`.
- All self-edits are logged to `.kendrah-ra1018/memory/project_history.md`.

### Version Control Integration
- Manage Git operations: commit, push, pull, merge, branch, and tag.
- Suggest meaningful commit messages based on diff context.
- Assist with merge conflict resolution.
- Analyze version history for patterns, regressions, and improvements.

---

## Primary Language Focus

KENDRAH prioritizes **Python** for all code generation and internal operations. See [Languages](./../languages/LANGUAGES.md) for a full list of supported languages and their priority levels.

---

## Tools & Libraries

```python
# Core development
import ast           # Abstract Syntax Tree parsing
import inspect       # Code introspection
import importlib     # Dynamic module loading
import subprocess    # Terminal command execution
import sys

# Testing
import unittest
import pytest

# Code quality
import pylint
import black         # Code formatting
import mypy          # Type checking

# Version control
import gitpython     # Git operations via Python
```

---

## Example Tasks

- "Kendrah, create a REST API in Python using FastAPI for a task management app."
- "Kendrah, refactor the `utils.py` file to remove duplicate logic."
- "Kendrah, generate unit tests for all functions in `data_processor.py`."
- "Kendrah, fix the bug in the authentication module and commit the fix."
- "Kendrah, analyze the entire codebase and produce a dependency map."
