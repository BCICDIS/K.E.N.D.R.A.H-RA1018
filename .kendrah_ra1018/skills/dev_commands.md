# Dev Commands

**Category:** Software Development Commands
**Status:** Active

---

## Overview

Development commands trigger KENDRAH's code generation, editing, testing, review, and deployment capabilities. These are the most frequently used command types for software engineering workflows.

---

## Code Generation Commands

| Command                             | Description                                                  |
|-------------------------------------|--------------------------------------------------------------|
| `/create [description]`             | Generate a new file, script, module, or application          |
| `/generate function [description]`  | Generate a specific function from a natural language prompt  |
| `/generate class [description]`     | Generate a class definition with methods                     |
| `/generate api [description]`       | Scaffold a REST API based on requirements                    |
| `/generate tests [file]`            | Generate unit tests for a given file                         |
| `/generate docs [file]`             | Generate documentation for a given file                      |
| `/scaffold [app-type]`              | Scaffold a full project structure                            |

---

## Code Editing Commands

| Command                             | Description                                                  |
|-------------------------------------|--------------------------------------------------------------|
| `/edit [file] [instruction]`        | Edit a specific file based on an instruction                 |
| `/refactor [file]`                  | Refactor and optimize the specified file                     |
| `/fix [file] [error]`               | Apply a targeted fix to a bug or error                       |
| `/cleanup [file or directory]`      | Remove dead code, unused imports, and redundancies           |
| `/rename [old] [new]`               | Rename variables, functions, or classes project-wide         |

---

## Testing Commands

| Command                             | Description                                                  |
|-------------------------------------|--------------------------------------------------------------|
| `/run tests`                        | Execute the full test suite                                  |
| `/run tests --file [file]`          | Run tests for a specific file                                |
| `/coverage`                         | Report test coverage across the codebase                     |
| `/test [function or class]`         | Generate and run a test for a specific unit                  |

---

## Review & Analysis Commands

| Command                             | Description                                                  |
|-------------------------------------|--------------------------------------------------------------|
| `/review [file]`                    | Perform an automated code review on a file                   |
| `/analyze codebase`                 | Deep analysis of the entire project structure                |
| `/lint [file]`                      | Run linter and report style violations                       |
| `/security-scan [file or dir]`      | Scan code for common security vulnerabilities                |
| `/complexity [file]`                | Report cyclomatic complexity and suggest simplifications     |

---

## Version Control Commands

| Command                             | Description                                                  |
|-------------------------------------|--------------------------------------------------------------|
| `/git status`                       | Show current Git status                                      |
| `/git commit --auto-message`        | Commit staged changes with an AI-generated commit message    |
| `/git push`                         | Push to the configured remote branch                         |
| `/git diff [file]`                  | Show changes since last commit                               |
| `/git log [n]`                      | Show last `n` commits with summaries                         |
| `/git branch [name]`                | Create a new branch                                          |
| `/git merge [branch]`               | Merge a branch with conflict assistance                      |

---

## Deployment Commands

| Command                             | Description                                                  |
|-------------------------------------|--------------------------------------------------------------|
| `/deploy [environment]`             | Deploy the application to the specified environment          |
| `/docker build`                     | Build a Docker image for the current project                 |
| `/docker run`                       | Run the Docker container locally                             |
| `/env setup [platform]`             | Generate environment configuration for a target platform     |
