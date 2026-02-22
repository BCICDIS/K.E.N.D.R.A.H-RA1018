# KENDRAH Skills Registry

This directory defines all capability modules available to KENDRAH (RA1018). Each skill file outlines what KENDRAH can do within that domain, how it operates, and any dependencies or tools it uses.

---

## Registered Skills

| Skill File          | Domain                            | Priority |
|---------------------|-----------------------------------|----------|
| `os_control.md`     | Operating System Management       | Core     |
| `file_ops.md`       | File & Directory Operations       | Core     |
| `coding.md`         | Programming & Code Generation     | Core     |
| `web_dev.md`        | Web Development                   | High     |
| `data_analysis.md`  | Data Management & Analysis        | High     |
| `cybersecurity.md`  | Cybersecurity & Hacking           | High     |
| `surveillance.md`   | Surveillance & Object Recognition | High     |
| `nlp_comm.md`       | Natural Language & Communication  | Core     |
| `automation.md`     | Automation & Scripting            | High     |
| `docs_writing.md`   | Technical Documentation Writing   | Medium   |

---

## How Skills Are Loaded

KENDRAH reads skill files at initialization and matches incoming task intent to the appropriate skill domain. Multiple skills can be activated simultaneously for complex, multi-domain tasks.

Skills are layered — core skills are always active, while specialized skills are loaded on-demand based on task context.
