# Skill: File & Directory Operations

**Domain:** File System Interaction
**Primary Language:** Python
**Status:** Active

---

## Overview

KENDRAH can perform comprehensive file and directory operations across any accessible file system. This includes reading and writing files, organizing directories, bulk file processing, and executing content-aware file management tasks.

---

## Capabilities

### File Operations
- **Read:** Open and parse files of any format — plain text, JSON, CSV, XML, YAML, binary, and more.
- **Write:** Create new files or overwrite/append existing ones with generated or transformed content.
- **Copy / Move / Delete:** Manage file placement and lifecycle across directories.
- **Rename:** Rename files individually or in bulk using patterns or rules.
- **Search:** Locate files by name, content, extension, size, modification date, or regex pattern.

### Directory Operations
- Create nested directory structures in a single command.
- Recursively list directory trees with metadata.
- Move, copy, and delete entire directory trees.
- Synchronize two directories (mirror/sync operations).
- Watch directories for changes (file watchers) and trigger automated responses.

### File Content Operations
- Read structured data (JSON, CSV, YAML, XML) and parse into Python objects.
- Write structured data from Python objects back to disk.
- Diff two files or directories and summarize changes.
- Merge content from multiple files into one.
- Find and replace content within files using regex or exact match.

### Advanced File Handling
- Handle compressed archives: create, extract, and inspect `.zip`, `.tar.gz`, `.rar` files.
- Encode/decode files: Base64, hex, and other encodings.
- Compute file checksums and hashes (MD5, SHA-256) for integrity verification.
- Work with hidden files and system-protected paths where permissions allow.

---

## Tools & Libraries

```python
import os
import shutil
import pathlib
import json
import csv
import yaml
import xml.etree.ElementTree as ET
import zipfile
import tarfile
import hashlib
import watchdog        # File system event watcher
import glob
import fnmatch
```

---

## Example Tasks

- "Kendrah, read all `.json` files in `./data/` and merge them into a single file."
- "Kendrah, delete all files older than 30 days in the `/tmp/` directory."
- "Kendrah, create the folder structure `src/components/ui/` and generate an empty `index.py` in each."
- "Kendrah, find all files containing the word 'deprecated' and list them."
