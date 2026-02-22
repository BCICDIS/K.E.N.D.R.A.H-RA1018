# Query Commands

**Category:** Data Retrieval, Search & Intelligence Commands
**Status:** Active

---

## Overview

Query commands instruct KENDRAH to retrieve, search, filter, and synthesize information from any accessible source — local files, databases, APIs, the web, logs, memory, or connected systems. KENDRAH treats all information retrieval as an intelligence task, returning structured, actionable outputs rather than raw data.

---

## Memory & Context Queries

| Command                               | Description                                                    |
|---------------------------------------|----------------------------------------------------------------|
| `/query memory`                       | Show full current session context                             |
| `/query memory --history [n]`         | Show last `n` entries in project history                      |
| `/query memory --search [keyword]`    | Search project history for a keyword or topic                 |
| `/query memory --date [date]`         | Show all memory entries from a specific date                  |
| `/query context`                      | Summarize what KENDRAH knows about the current task           |
| `/query skills`                       | List all active skills and their status                       |
| `/query rules`                        | Display all active behavioral rules                           |

---

## File & Codebase Queries

| Command                               | Description                                                    |
|---------------------------------------|----------------------------------------------------------------|
| `/query files [pattern]`              | Find files matching a name or extension pattern               |
| `/query file [path]`                  | Summarize or analyze the contents of a specific file          |
| `/query codebase`                     | Generate a high-level overview of the entire codebase         |
| `/query dependencies`                 | Map all imports and dependencies in the project               |
| `/query function [name]`              | Find and explain a specific function across the codebase      |
| `/query todos`                        | Find all `TODO`, `FIXME`, `HACK`, and `NOTE` comments         |
| `/query diff [file]`                  | Show changes to a file since last commit                      |
| `/query complexity`                   | Report code complexity metrics for the codebase               |

---

## Database Queries

| Command                               | Description                                                    |
|---------------------------------------|----------------------------------------------------------------|
| `/query db --list`                    | List all accessible databases and their tables/collections    |
| `/query db --schema [table]`          | Show the schema of a specific table                           |
| `/query db [natural language]`        | Translate a natural language question into a SQL/NoSQL query  |
| `/query db --run [query]`             | Execute a raw query and return results                        |
| `/query db --summarize [table]`       | Statistical summary of a database table                       |
| `/query db --export [table] [format]` | Export a table to CSV, JSON, or Excel                         |

---

## Log Queries

| Command                               | Description                                                    |
|---------------------------------------|----------------------------------------------------------------|
| `/query logs [service]`               | Fetch and display recent logs from a service                  |
| `/query logs --search [keyword]`      | Search logs for a keyword or pattern                          |
| `/query logs --errors`                | Filter logs to show only errors and exceptions                |
| `/query logs --date [date]`           | Show logs from a specific date range                          |
| `/query logs --summarize`             | Generate an NLP summary of recent log activity                |

---

## Web & External Information Queries

| Command                               | Description                                                    |
|---------------------------------------|----------------------------------------------------------------|
| `/query web [question or topic]`      | Search the web and return a synthesized answer                |
| `/query web --url [url]`              | Fetch, read, and summarize a specific URL                     |
| `/query web --news [topic]`           | Search for recent news articles on a topic                    |
| `/query api [endpoint]`               | Call an HTTP API endpoint and display the response            |
| `/query api --auth [method]`          | Call an authenticated API endpoint                            |

---

## Data & Analysis Queries

| Command                               | Description                                                    |
|---------------------------------------|----------------------------------------------------------------|
| `/query data [file] [question]`       | Ask a natural language question about a data file             |
| `/query data --stats [file]`          | Generate descriptive statistics for a data file               |
| `/query data --filter [conditions]`   | Filter rows from a dataset matching conditions                |
| `/query data --compare [file1] [file2]`| Compare two datasets and highlight differences               |

---

## System & Infrastructure Queries

| Command                               | Description                                                    |
|---------------------------------------|----------------------------------------------------------------|
| `/query system`                       | Full system snapshot: CPU, RAM, disk, network, uptime         |
| `/query processes`                    | List running processes with resource consumption              |
| `/query ports`                        | List all open ports and associated processes                  |
| `/query services`                     | List all running system services and their statuses           |
| `/query env`                          | Display all environment variables currently set               |

---

## Output Formatting

All query results can be formatted via flags:

| Flag              | Output Format                          |
|-------------------|----------------------------------------|
| `--json`          | Return results as JSON                 |
| `--csv`           | Return tabular results as CSV          |
| `--markdown`      | Return results formatted as Markdown   |
| `--summary`       | Return a concise natural language summary |
| `--save [file]`   | Save query results to a file           |
