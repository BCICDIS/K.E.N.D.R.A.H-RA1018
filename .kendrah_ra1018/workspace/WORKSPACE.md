# KENDRAH — Workspace

**Module:** `.kendrah-ra1018/workspace/`
**Domain:** Project Management, Organization & Location Tracking
**Status:** Active

---

## Overview

The Workspace module is KENDRAH's project management layer. It tracks all active and archived projects, their locations on disk, their status, tech stacks, associated files, and key metadata. The Workspace is the control center through which KENDRAH knows what you are building, where it lives, and where things stand.

Think of Workspace as your project registry — every project KENDRAH has touched or been told about is registered here, with enough context to pick up where things left off at any time.

---

## Workspace Structure

```
workspace/
├── WORKSPACE.md              ← This file — registry and overview
├── active/                   ← Active projects
│   ├── project_name.md       ← One file per active project
│   └── ...
├── archived/                 ← Completed or paused projects
│   └── ...
└── templates/
    └── project_template.md   ← Template for new project entries
```

---

## Project Registry

All projects KENDRAH manages are registered in this workspace. Each entry is a Markdown file in `active/` or `archived/`.

### Active Projects

| Project Name | Location | Status | Domain | Last Updated |
|---|---|---|---|---|
| *(No active projects — register one below)* | | | | |

---

## Project Entry Format

Each project file (`active/project_name.md`) follows this structure:

```markdown
# Project: [Project Name]

## Identity
- **Name:** [Project Name]
- **ID:** proj-[unique-id]
- **Domain:** software | research | data | operations | other
- **Status:** planning | active | paused | complete | archived
- **Owner:** [User name or team]
- **Created:** [YYYY-MM-DD]
- **Last Activity:** [YYYY-MM-DD]

## Location
- **Root Directory:** /path/to/project/root
- **Repository:** [Git URL or local path]
- **Branch:** main
- **Deployment:** [URL or environment name, if deployed]

## Description
[What this project is and what it aims to accomplish]

## Tech Stack
- Language: Python
- Framework: FastAPI
- Database: PostgreSQL
- Frontend: React
- Deployment: Docker + DigitalOcean

## Current Milestone
**Milestone:** [Name]
**Target:** [Date]
**Deliverable:** [What needs to be done]
**Status:** In Progress

## Active Tasks
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

## Completed Milestones
- [x] Project initialized
- [x] Database schema designed

## Key Decisions
- [Date] — Used FastAPI over Flask (performance + async support)
- [Date] — PostgreSQL over MongoDB (relational data model)

## Files & Directories
| Path | Description |
|---|---|
| `src/api/` | API route handlers |
| `src/models/` | SQLAlchemy models |
| `tests/` | Unit and integration tests |

## Notes & Context
[Any additional context KENDRAH needs to work effectively on this project]
```

---

## Workspace Commands

### Project Management
```
/workspace list                          — List all active and archived projects
/workspace status                        — Summary status of all active projects
/workspace new "[project name]"          — Register a new project in the workspace
/workspace open "[project name]"         — Set a project as the active context
/workspace archive "[project name]"      — Move a project to archived
/workspace delete "[project name]"       — Remove a project from the registry (prompts confirmation)
```

### Navigation & Location
```
/workspace locate "[project name]"       — Show the file system location of a project
/workspace cd "[project name]"           — Navigate KENDRAH's context to a project directory
/workspace files "[project name]"        — List all key files in a project
/workspace open-file "[path]"            — Open and contextualize a specific file
```

### Status & Progress
```
/workspace progress "[project name]"     — Show milestone and task completion status
/workspace update-status "[name]" "[status]" — Update a project's status
/workspace add-task "[project]" "[task]" — Add a task to a project's active list
/workspace complete-task "[task]"        — Mark a task as complete
/workspace milestone "[project]" "[milestone]" — Record a completed milestone
```

### Context Switching
```
/workspace switch "[project name]"       — Switch KENDRAH's full context to another project
/workspace context                       — Show the currently active project context
```

---

## Multi-Project Management

KENDRAH can manage multiple projects simultaneously. When switching between projects with `/workspace switch`, KENDRAH:
1. Saves the current session context to the outgoing project's file
2. Loads the incoming project's context, history, and file locations
3. Confirms the switch with a brief project status summary

---

## Project Templates

The `templates/` directory contains starter structures for common project types:
- `python_api_project.md` — FastAPI backend project template
- `fullstack_web_project.md` — Full-stack Python + JS web app
- `data_science_project.md` — Data analysis and ML project
- `research_project.md` — Research and documentation project
- `general_project.md` — Generic project for any domain
