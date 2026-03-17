#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════╗
║          K.E.N.D.R.A.H - RA1018 | ENTRY ENGINE                        ║
║     Arsenally a Super Intelligent System                                ║
║     Initializing... Stand by, Master.                                   ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import platform
import datetime
import subprocess
import shutil

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.settings import Settings
from kendrah.main import KendrahCore

# ── ANSI Colors ───────────────────────────────────────────────────
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
WHITE  = "\033[97m"
DIM    = "\033[2m"
RESET  = "\033[0m"
BOLD   = "\033[1m"
PK     = "\033[95m"


def banner(settings: Settings):
    print(f"""
{CYAN}{BOLD}
  ██╗  ██╗███████╗███╗  ██╗██████╗ ██████╗  █████╗ ██╗  ██╗
  ██║ ██╔╝██╔════╝████╗ ██║██╔══██╗██╔══██╗██╔══██╗██║  ██║
  █████╔╝ █████╗  ██╔██╗██║██║  ██║██████╔╝███████║███████║
  ██╔═██╗ ██╔══╝  ██║╚████║██║  ██║██╔══██╗██╔══██║██╔══██║
  ██║  ██╗███████╗██║ ╚███║██████╔╝██║  ██║██║  ██║██║  ██║
  ╚═╝  ╚═╝╚══════╝╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
{RESET}
{WHITE}          [ R A 1 0 1 8 ]  |  Arsenally Super Intelligent System{RESET}
{DIM}         Powered by Ollama · {settings.MODEL_PRIMARY} · {settings.MODEL_ENGINEER}{RESET}
""")


def _status(label: str, value: str, ok: bool = True):
    icon = f"{GREEN}✔{RESET}" if ok else f"{YELLOW}⚠{RESET}"
    print(f"  {icon}  {DIM}{label:<34}{RESET}  {WHITE}{value}{RESET}")


def system_check(settings: Settings) -> dict:
    """JARVIS-style system awareness check before entering READY mode."""
    import psutil

    print(f"\n{CYAN}{'─'*60}{RESET}")
    print(f"  {BOLD}SYSTEM INITIALIZATION — SELF-CHECK SEQUENCE{RESET}")
    print(f"{CYAN}{'─'*60}{RESET}\n")

    results = {}

    # Date / Time
    now = datetime.datetime.now()
    _status("Date / Time", now.strftime("%A, %B %d %Y  |  %H:%M:%S"))

    # OS
    os_info = f"{platform.system()} {platform.release()} [{platform.machine()}]"
    _status("Operating System", os_info)
    results["os"] = os_info

    # CPU
    cpu_pct   = psutil.cpu_percent(interval=0.5)
    cpu_cores = psutil.cpu_count()
    _status("CPU", f"{cpu_cores} cores  |  {cpu_pct}% usage", cpu_pct < 90)
    results["cpu"] = cpu_pct

    # RAM
    ram = psutil.virtual_memory()
    _status("RAM", f"{ram.available/1e9:.1f} GB free / {ram.total/1e9:.1f} GB total  ({ram.percent}% used)", ram.percent < 90)
    results["ram"] = ram

    # Disk
    disk = psutil.disk_usage("/" if os.name != "nt" else "C:\\")
    _status("Disk", f"{disk.free/1e9:.1f} GB free / {disk.total/1e9:.1f} GB", disk.percent < 95)

    # Battery
    try:
        bat = psutil.sensors_battery()
        if bat:
            plugged = "Plugged in" if bat.power_plugged else "On battery"
            _status("Battery", f"{bat.percent:.0f}%  |  {plugged}", bat.percent > 15 or bat.power_plugged)
        else:
            _status("Battery", "No battery (Desktop)", True)
    except Exception:
        _status("Battery", "Sensor unavailable", True)

    # Python
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    _status("Python Runtime", py_ver)

    # Ollama binary
    ollama_ok = shutil.which("ollama") is not None
    _status("Ollama Binary", "Found" if ollama_ok else "NOT FOUND — install from ollama.com", ollama_ok)
    results["ollama"] = ollama_ok

    # Models
    if ollama_ok:
        try:
            out = subprocess.check_output(["ollama", "list"], timeout=5, stderr=subprocess.DEVNULL).decode()
            primary_ok  = settings.MODEL_PRIMARY  in out
            engineer_ok = settings.MODEL_ENGINEER in out
            coder_ok    = settings.MODEL_CODER    in out

            _status(f"{settings.MODEL_PRIMARY} (Primary Brain)",  "Ready" if primary_ok  else "Not pulled — run: ollama pull " + settings.MODEL_PRIMARY,  primary_ok)
            _status(f"{settings.MODEL_ENGINEER} (Engineer Brain)", "Ready" if engineer_ok else "Not pulled — run: ollama pull " + settings.MODEL_ENGINEER, engineer_ok)
            _status(f"{settings.MODEL_CODER} (Coder — disabled)", "Available" if coder_ok else "Not pulled (optional)", True)

            results["primary_ready"]  = primary_ok
            results["engineer_ready"] = engineer_ok
        except Exception:
            _status("Ollama Models", "Could not query list", False)

    print(f"\n{CYAN}{'─'*60}{RESET}")
    return results


def boot_animation():
    frames = ["▏","▎","▍","▌","▋","▊","▉","█"]
    bar    = ""
    sys.stdout.write(f"\n  {CYAN}Booting KENDRAH  [")
    for i in range(32):
        bar += frames[i % len(frames)]
        sys.stdout.write(f"\r  {CYAN}Booting KENDRAH  [{bar:<32}] {int((i+1)/32*100)}%{RESET}")
        sys.stdout.flush()
        time.sleep(0.035)
    print(f"\r  {GREEN}KENDRAH ONLINE   [{'█'*32}] 100%{RESET}\n")


def main():
    os.system("cls" if os.name == "nt" else "clear")

    settings = Settings()
    banner(settings)

    check = system_check(settings)

    if not check.get("ollama"):
        print(f"\n{RED}  ✘ CRITICAL: Ollama not found. Install from https://ollama.com{RESET}")
        print(f"  {YELLOW}  Kendrah will run in degraded mode (no LLM brain).{RESET}\n")

    boot_animation()

    core = KendrahCore(settings=settings, system_info=check)
    core.start()


if __name__ == "__main__":
    main()
