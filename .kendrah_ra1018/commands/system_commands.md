# System Commands

**Category:** Operating System & Infrastructure Commands
**Status:** Active

---

## Overview

System commands give KENDRAH direct control over the operating system, hardware, processes, file system, and network infrastructure. These commands are the lowest-level interface KENDRAH exposes — operating beneath the application layer to interact with the machine itself.

---

## Process & Service Commands

| Command                              | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| `/process list`                      | List all running processes with PID, CPU, and memory usage   |
| `/process kill [name or PID]`        | Terminate a process by name or PID                           |
| `/process top [n]`                   | Show top `n` processes by CPU or memory usage                |
| `/process start [command]`           | Start a process or service in the background                 |
| `/service status [name]`             | Check the status of a system service                         |
| `/service restart [name]`            | Restart a named system service                               |
| `/service enable [name]`             | Enable a service to start on boot                            |
| `/service disable [name]`            | Disable a service from starting on boot                      |

---

## File System Commands

| Command                              | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| `/fs list [path]`                    | List directory contents with metadata                        |
| `/fs tree [path]`                    | Display directory structure as a tree                        |
| `/fs find [pattern] [path]`          | Search for files matching a pattern                          |
| `/fs copy [src] [dst]`               | Copy file or directory                                       |
| `/fs move [src] [dst]`               | Move file or directory                                       |
| `/fs delete [path]`                  | Delete file or directory (prompts confirmation)              |
| `/fs mkdir [path]`                   | Create directory and all parents                             |
| `/fs watch [path]`                   | Watch a directory for changes and log events                 |
| `/fs permissions [path] [mode]`      | Set file or directory permissions                            |
| `/fs checksum [file]`                | Compute MD5 and SHA-256 checksum for a file                  |
| `/fs compress [path] [output]`       | Compress a file or directory to `.zip` or `.tar.gz`          |
| `/fs extract [archive] [dest]`       | Extract a compressed archive                                 |

---

## Storage & Drive Commands

| Command                              | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| `/disk list`                         | List all mounted drives with capacity and usage              |
| `/disk usage [path]`                 | Show disk usage for a path                                   |
| `/disk health [drive]`               | Run S.M.A.R.T. diagnostics on a drive                        |
| `/disk mount [device] [mountpoint]`  | Mount a storage device                                       |
| `/disk unmount [mountpoint]`         | Unmount a storage device                                     |

---

## Network Commands

| Command                              | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| `/net status`                        | Show network interfaces, IPs, and connection status          |
| `/net ping [host]`                   | Ping a host and report latency                               |
| `/net scan [target]`                 | Scan a host or subnet for open ports and services            |
| `/net connections`                   | List active TCP/UDP connections and associated processes      |
| `/net dns [domain]`                  | Resolve a domain name and show DNS records                   |
| `/net trace [host]`                  | Run a traceroute to a host                                   |
| `/net firewall list`                 | List active firewall rules                                   |
| `/net firewall add [rule]`           | Add a firewall rule                                          |
| `/net firewall remove [rule]`        | Remove a firewall rule                                       |

---

## System Monitoring Commands

| Command                              | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| `/sys status`                        | Full system health snapshot (CPU, RAM, disk, network)        |
| `/sys cpu`                           | Current CPU usage per core                                   |
| `/sys memory`                        | RAM usage, available, and swap status                        |
| `/sys temperature`                   | Hardware temperature readings (CPU, GPU, drives)             |
| `/sys uptime`                        | System uptime and boot time                                  |
| `/sys logs [service]`                | Tail system or service logs                                  |
| `/sys events [n]`                    | Show last `n` system events                                  |

---

## Scheduler & Automation Commands

| Command                              | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| `/schedule add [task] [cron]`        | Schedule a task with a cron expression                       |
| `/schedule list`                     | List all scheduled tasks                                     |
| `/schedule remove [id]`              | Remove a scheduled task by ID                                |
| `/schedule run [id]`                 | Manually trigger a scheduled task immediately                |

---

## Environment Commands

| Command                              | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| `/env get [key]`                     | Get the value of an environment variable                     |
| `/env set [key] [value]`             | Set an environment variable for the current session          |
| `/env list`                          | List all environment variables                               |
| `/env export [file]`                 | Export environment variables to a `.env` file                |
