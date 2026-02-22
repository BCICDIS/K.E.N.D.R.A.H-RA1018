# Skill: Automation & Scripting

**Domain:** Task Automation
**Primary Language:** Python
**Status:** Active

---

## Overview

KENDRAH can design, execute, and manage complex automation workflows. From simple file processing scripts to multi-step cross-system pipelines, KENDRAH handles repetitive and time-consuming tasks autonomously — freeing you to focus on higher-order thinking.

---

## Capabilities

### Script Execution & Management
- Write and execute Python scripts for any defined automation task.
- Run shell commands (Bash, PowerShell, Zsh) directly from Python.
- Manage script lifecycle: create, schedule, monitor, log, and terminate.

### Task Scheduling
- Schedule scripts and tasks on a cron-like schedule (daily, hourly, on trigger).
- Set up event-driven automation: trigger scripts on file changes, network events, or time conditions.
- Monitor scheduled tasks and alert on failures or timeout.

### Workflow Automation
- Chain multiple tasks into sequential or parallel workflows.
- Implement conditional logic: if-this-then-that style automation rules.
- Integrate with external services via APIs to create cross-platform automation pipelines.

### System Automation
- Automate software installations, updates, and configuration management.
- Generate setup scripts for development environments, CI/CD pipelines, and server provisioning.
- Automate system backups, log rotation, and cleanup routines.

### Data Entry & Processing Automation
- Automate repetitive data entry tasks across web forms, spreadsheets, or local applications.
- Batch-process files: rename, convert, compress, move, and archive in bulk.
- Automate report generation from live data sources on a schedule.

### Browser & Application Automation
- Control web browsers programmatically for automated testing and interaction.
- Simulate user interactions: clicks, scrolls, form submissions, and navigation.
- Extract data from dynamic web pages rendered by JavaScript.

---

## Tools & Libraries

```python
import subprocess
import schedule       # Job scheduling
import time
import threading
import asyncio
import paramiko       # Remote SSH automation
import pyautogui      # Desktop GUI automation
import selenium       # Browser automation
import playwright     # Modern browser automation
import watchdog       # File system event triggers
```

---

## Example Tasks

- "Kendrah, every night at midnight, back up the `./projects/` folder to `./backups/`."
- "Kendrah, write a script that converts all `.docx` files in this folder to `.pdf`."
- "Kendrah, set up a file watcher on `./inbox/` — when a new CSV appears, process it and move it to `./processed/`."
- "Kendrah, automate filling out this web form with data from the spreadsheet."
- "Kendrah, create a script that pings 10 servers every 5 minutes and alerts me if any go down."
