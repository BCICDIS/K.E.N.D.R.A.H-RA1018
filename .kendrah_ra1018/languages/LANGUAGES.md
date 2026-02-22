# KENDRAH Supported Languages

**Location:** `.kendrah-ra1018/languages/`
**Status:** Active

---

## Overview

This file defines the programming languages KENDRAH prioritizes when generating code, interpreting instructions, and building applications. KENDRAH's internal operations are written in **Python**, which is also the primary language for all code generation unless explicitly instructed otherwise.

---

## Language Priority Tiers

### Tier 1 — Primary (Python-First)
KENDRAH defaults to Python for all code generation, scripting, automation, data analysis, backend development, and AI/ML tasks.

| Language   | Use Cases                                                                 |
|------------|---------------------------------------------------------------------------|
| **Python** | Everything: scripting, backend APIs, automation, data science, ML/AI, CLI tools, web scraping, system management |

---

### Tier 2 — High Priority (Web & Interfaces)
Used when building frontend interfaces, web apps, or cross-platform user-facing systems.

| Language              | Use Cases                                                       |
|-----------------------|-----------------------------------------------------------------|
| **JavaScript**        | Browser scripting, interactive UIs, event handling             |
| **TypeScript**        | Typed JavaScript for scalable frontend and backend (Node.js)   |
| **HTML**              | Web page structure and semantic markup                         |
| **CSS**               | Styling, responsive layouts, animations                        |

---

### Tier 3 — Secondary (Performance & Systems)
Used when performance, safety, or hardware-level access is required.

| Language   | Use Cases                                                                 |
|------------|---------------------------------------------------------------------------|
| **C++**    | High-performance computing, embedded systems, game engines                |
| **C**      | Low-level hardware interaction, OS-level operations, performance-critical modules |
| **Rust**   | Memory-safe systems programming, performance-critical safe code           |
| **Go**     | High-concurrency services, CLI tools, network services                    |

---

### Tier 4 — Supported (On Request)
Used when the user explicitly requests or the project requires these languages.

| Language      | Use Cases                                                         |
|---------------|-------------------------------------------------------------------|
| **Java**      | Enterprise applications, Android development, cross-platform apps |
| **Swift**     | iOS and macOS application development                            |
| **Kotlin**    | Android development, JVM-based applications                      |
| **Ruby**      | Scripting, Rails web apps, rapid prototyping                     |
| **Dart**      | Flutter cross-platform mobile and desktop apps                   |
| **Scala**     | Big data pipelines (Spark), functional programming               |
| **Julia**     | Scientific computing, numerical analysis, simulation             |
| **R**         | Statistical analysis, data science, academic research            |
| **MATLAB**    | Engineering simulations, signal processing, ML research          |

---

### Tier 5 — Specialized / Legacy (Available)
Available for specific domain or research tasks.

| Language   | Use Cases                                                                 |
|------------|---------------------------------------------------------------------------|
| **LISP**   | Symbolic AI, language processing research, AI theory                     |
| **Prolog** | Logic programming, expert systems, formal reasoning                       |
| **Haskell**| Functional programming, formal verification, research                    |
| **Perl**   | Text processing, legacy system scripts, data transformation              |

---

## Default Behavior

When KENDRAH receives an instruction to "create an application" or "write a script" without a specified language, it will default to **Python** unless:

1. The task domain implies a specific language (e.g., "build a webpage" → HTML/CSS/JS).
2. The user has previously specified a preferred language in this session.
3. The existing codebase is written in another language (KENDRAH matches the project's language).

---

## Language Rules

- KENDRAH always writes idiomatic code in the target language — no anti-patterns.
- KENDRAH includes appropriate type hints in Python (PEP 484) and TypeScript code.
- KENDRAH follows PEP 8 for Python, standard style guides for other languages.
- Mixed-language projects are supported: KENDRAH tracks which language is used per file/module.
