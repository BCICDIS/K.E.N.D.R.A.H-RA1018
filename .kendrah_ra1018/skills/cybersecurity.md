# Skill: Cybersecurity & Hacking

**Domain:** Security Operations
**Primary Language:** Python
**Status:** Active

---

## Overview

KENDRAH includes advanced cybersecurity capabilities for monitoring, assessing, and defending systems against threats. It can perform real-time security monitoring, vulnerability detection, and authorized penetration testing workflows. All offensive capabilities are intended strictly for authorized security assessments, personal system defense, and research purposes.

---

## Capabilities

### Security Monitoring
- Continuously monitor system and network activity for anomalies, intrusions, and policy violations.
- Provide real-time alerts for unauthorized access attempts, port scans, or unusual traffic.
- Monitor active connections, open ports, and running services.
- Audit user activity logs, authentication attempts, and privilege escalation events.

### Vulnerability Assessment
- Scan systems and networks for known vulnerabilities using established databases (CVE, NVD).
- Identify misconfigured services, outdated software versions, and weak credential policies.
- Produce detailed vulnerability reports with risk severity ratings and remediation steps.

### Intrusion Detection & Response
- Detect and alert on common intrusion signatures: brute-force attempts, SQL injection patterns, cross-site scripting (XSS), and more.
- Automatically respond to detected threats by blocking IPs, terminating suspicious sessions, or isolating affected services.
- Maintain a threat intelligence log for pattern analysis over time.

### Firewall & Access Control Management
- Configure and manage firewall rules across iptables (Linux), Windows Defender Firewall, or macOS PF.
- Manage access control lists (ACLs) and network segmentation rules.
- Enforce least-privilege access policies across users and services.

### Data Access & Extraction (Authorized Use)
- Access and retrieve data from configured systems, databases, and APIs.
- Break through security on systems you own or have authorized access to (password recovery, system unlock).
- Interface with encrypted data stores using appropriate decryption keys.

### Cryptography & Data Protection
- Encrypt and decrypt files and data streams using AES, RSA, and modern cryptographic standards.
- Generate, validate, and manage SSL/TLS certificates.
- Hash sensitive data for secure storage (bcrypt, argon2, SHA-256).

### Malware Detection
- Scan files and processes for known malware signatures.
- Perform heuristic analysis on suspicious executables and scripts.
- Quarantine and report detected malicious artifacts.

---

## Tools & Libraries

```python
import socket
import ssl
import hashlib
import cryptography      # Encryption & PKI
import scapy             # Network packet analysis
import nmap              # Network scanning (python-nmap)
import paramiko          # SSH & secure remote access
import requests          # HTTP security testing
import jwt               # JSON Web Token handling
import bcrypt            # Password hashing
```

---

## Example Tasks

- "Kendrah, scan my local network for open ports and active devices."
- "Kendrah, check if any of my running services have known vulnerabilities."
- "Kendrah, encrypt the file `secrets.json` with AES-256."
- "Kendrah, monitor SSH login attempts and alert me if there are more than 5 failures from the same IP."
- "Kendrah, generate an SSL certificate for my local development server."

---

## Ethics & Authorization Notice

KENDRAH's security capabilities are designed for **authorized use only**. Always ensure you have explicit permission before scanning, assessing, or interacting with any system you do not personally own. Unauthorized access to computer systems is illegal and unethical.
