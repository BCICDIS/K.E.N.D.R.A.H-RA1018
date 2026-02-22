# Skill: Operating System Management

**Domain:** System Control & Automation
**Primary Language:** Python
**Status:** Active

---

## Overview

KENDRAH has deep OS-level control across Windows, macOS, and Linux environments. This skill enables KENDRAH to operate as an autonomous system manager — controlling processes, managing hardware, handling environment configurations, and automating system-level tasks without requiring manual intervention.

---

## Capabilities

### System Control
- Start, stop, and manage running processes and services.
- Control system settings: display, audio, network, power, and peripherals.
- Monitor hardware performance: CPU, RAM, GPU, disk I/O, temperature, and uptime.
- Schedule and execute tasks via cron jobs or system task schedulers.
- Manage environment variables and system-wide configurations.

### Storage & Drive Management
- Access and manage Hard Drives and SSDs.
- Create, format, partition, mount, and unmount storage volumes.
- Perform disk health checks and diagnostics (S.M.A.R.T. data).
- Monitor available storage and trigger alerts on low disk space.

### Directory & File System Navigation
- Traverse and map the entire file system structure.
- Create, rename, move, copy, and delete directories at any depth.
- Set and modify file/folder permissions, ownership, and ACLs.
- Search for files by name, extension, content, date, or metadata.

### Process & Resource Management
- List, prioritize, and kill processes by name, PID, or resource usage.
- Set CPU and memory limits on specific processes.
- Run background processes and monitor them autonomously.

### Multi-OS Support
- **Windows:** Win32 API access, registry management, PowerShell integration.
- **macOS:** AppleScript, Homebrew toolchain, macOS system APIs.
- **Linux:** Shell scripting, systemd/init.d services, package managers (apt, yum, pacman).

---

## Tools & Libraries

```python
import os
import shutil
import subprocess
import psutil           # Process & system monitoring
import platform         # OS detection
import pathlib          # Path management
import ctypes           # Windows low-level access
import signal           # Process signal management
```

---

## Example Tasks

- "Kendrah, check which process is consuming the most CPU."
- "Kendrah, create a backup directory at `/mnt/backup` and move all `.log` files there."
- "Kendrah, restart the web server service."
- "Kendrah, list all mounted drives and their available space."
