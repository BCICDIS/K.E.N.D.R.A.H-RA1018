# KENDRAH Commands Registry

**Location:** `.kendrah-ra1018/commands/`
**Status:** Active

---

## Overview

This registry documents all command categories available to KENDRAH. Commands can be issued via natural language or structured command syntax. KENDRAH interprets both and maps them to the appropriate skill or agent.

---

## Command Categories

| File                    | Category                          |
|-------------------------|-----------------------------------|
| `system_commands.md`    | OS, file system, process control  |
| `dev_commands.md`       | Code generation, editing, testing |
| `agent_commands.md`     | Autonomous agent invocation       |
| `query_commands.md`     | Data retrieval, search, analysis  |

---

## Command Syntax

KENDRAH accepts commands in plain natural language. For precision tasks, structured syntax is also supported:

```
/command [target] [--option value]
```

### Examples

| Natural Language                                           | Structured Syntax                                    |
|------------------------------------------------------------|------------------------------------------------------|
| "Kendrah, create a Python script to rename all files"       | `/create script --lang python --task file-rename`   |
| "Kendrah, run the test suite"                              | `/run tests --coverage`                              |
| "Kendrah, git commit with a meaningful message"            | `/git commit --auto-message`                         |
| "Kendrah, scan for open ports on localhost"                | `/scan network --target localhost --type ports`      |
| "Kendrah, summarize today's logs"                          | `/query logs --date today --action summarize`        |

---

## Global Command Flags

| Flag          | Description                                           |
|---------------|-------------------------------------------------------|
| `--verbose`   | Show detailed output and reasoning                    |
| `--dry-run`   | Simulate the action without executing changes         |
| `--log`       | Force logging of the result to project history        |
| `--confirm`   | Require explicit confirmation before executing        |
| `--silent`    | Suppress output, execute quietly                      |

---

## Built-In Shorthand Commands

| Shorthand     | Action                                                |
|---------------|-------------------------------------------------------|
| `/status`     | Report KENDRAH's current state and loaded context     |
| `/memory`     | Show current session context and recent history       |
| `/skills`     | List all active skills                                |
| `/rules`      | Display current behavioral rules                      |
| `/reset`      | Clear session context (not persistent memory)         |
| `/help`       | Display command help and available options            |
