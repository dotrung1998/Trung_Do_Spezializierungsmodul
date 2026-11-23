#!/usr/bin/env python3
"""Schickt eine kurze Zusammenfassung des letzten Laufs an Discord.

Der Webhook ist ein Geheimnis. Er wird hier gelesen, in dieser Reihenfolge:
  1. Umgebungsvariable DISCORD_WEBHOOK (so liest ihn GitHub Actions)
  2. Datei `~/.config/projektjlu/discord-webhook` (eigener Kanal)
  3. Datei `~/.config/projektplanung/discord-webhook` (Rückfall, vorhandener Kanal)
Fehlt alles, wird nichts gesendet. Der Webhook steht nie im Vault und nie im Repo.

Aufruf:
    python3 Obsidian/_tools/discord_notify.py
    python3 Obsidian/_tools/discord_notify.py --dry-run
    python3 Obsidian/_tools/discord_notify.py --status fail --detail "ingest.py"
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
VAULT = TOOLS.parent
NEU = VAULT / "00 Brain" / "Neu seit letztem Lauf.md"
BOARD = VAULT / "30 Plan" / "Board.md"
FRISTEN = TOOLS / "fristen.json"
LOG = TOOLS / "daily.log"
WEBHOOK_FILES = (
    Path.home() / ".config" / "projektjlu" / "discord-webhook",
    Path.home() / ".config" / "projektplanung" / "discord-webhook",
)

DRY = "--dry-run" in sys.argv
TITEL = "Spezialisierungsmodul Thema 29"
VAULT_LABEL = "Obsidian"


def arg_value(name: str, default: str = "") -> str:
    if name in sys.argv:
        index = sys.argv.index(name)
        if index + 1 < len(sys.argv):
            return sys.argv[index + 1]
    return default


STATUS = arg_value("--status", "ok")
DETAIL = arg_value("--detail", "")
ALLOWED = (
    "https://discord.com/api/webhooks/",
    "https://canary.discord.com/api/webhooks/",
    "https://ptb.discord.com/api/webhooks/",
    "https://discordapp.com/api/webhooks/",
)


def webhook() -> str:
    url = os.environ.get("DISCORD_WEBHOOK", "").strip()
    if url:
        return url
    for path in WEBHOOK_FILES:
        try:
            return path.read_text(encoding="utf-8").strip()
        except OSError:
            continue
    return ""


def grab(text: str, pattern: str, default: str = "") -> str:
    match = re.search(pattern, text)
    return match.group(1) if match else default


def last_run_stamp() -> str:
    """Zeitpunkt des letzten Laufs aus daily.log (nicht aus der Notiz)."""
    try:
        lines = LOG.read_text(encoding="utf-8").splitlines()
    except OSError:
        return ""
    for line in reversed(lines):
        match = re.match(r"^=== (\d{4}-\d{2}-\d{2} \d{2}:\d{2}):\d{2} ===$", line)
        if match:
            return match.group(1)
    return ""


def board_progress() -> str:
    try:
        lines = BOARD.read_text(encoding="utf-8").splitlines()
    except OSError:
        return ""
    done = sum(1 for line in lines if line.startswith("- [x]"))
    total = done + sum(1 for line in lines if line.startswith("- [ ]"))
    return f"{done}/{total} Karten erledigt" if total else ""


def board_structure() -> str:
    try:
        tail = LOG.read_text(encoding="utf-8").splitlines()[-40:]
    except OSError:
        return ""
    for line in reversed(tail):
        if line.startswith("Board-Struktur:"):
            return line.strip()
    return ""


def faellige(limit: int = 7) -> list:
    try:
        items = json.loads(FRISTEN.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    today = date.today()
    rows = []
    for item in sorted(items, key=lambda entry: entry.get("datum", "")):
        try:
            delta = (datetime.fromisoformat(item["datum"]) - datetime.combine(today, datetime.min.time())).days
        except (KeyError, ValueError, TypeError):
            continue
        if delta > limit:
            continue
        if delta < 0:
            when = f"überfällig seit {-delta} T."
        elif delta == 0:
            when = "heute"
        elif delta == 1:
            when = "morgen"
        else:
            when = f"in {delta} Tagen"
        tag = item["datum"][:10].replace("-", ".")
        rows.append(f"• **{when}** · {item.get('titel', '?')} ({tag}, {item.get('wer', '?')})")
    return rows


def message() -> str:
    try:
        text = NEU.read_text(encoding="utf-8")
    except OSError:
        text = ""

    stamp = last_run_stamp() or grab(text, r"Lauf:\s*(.+)")
    gesamt = grab(text, r"Quellen gesamt:\s*\*\*(\d+)\*\*", "?")
    notiz = grab(text, r"durch Notiz:\s*(\d+)", "?")
    manuell = grab(text, r"manuell beschrieben:\s*(\d+)", "?")
    ausgeschlossen = grab(text, r"ausgeschlossen:\s*(\d+)", "?")
    unbekannt = grab(text, r"\*\*unbekannt:\s*(\d+)\*\*", "?")
    neu = grab(text, r"## Neu \((\d+)\)", "?")
    geaendert = grab(text, r"## Geändert \((\d+)\)", "?")
    unveraendert = grab(text, r"## Unverändert:\s*(\d+) Quellen", "?")

    stamp = stamp or datetime.now().strftime("%Y-%m-%d %H:%M")
    if STATUS == "fail":
        lines = [f"❌ **{TITEL} · Lauf {stamp} fehlgeschlagen**"]
    else:
        lines = [f"**{TITEL} · Lauf {stamp}**"]

    unbekannt_teil = f"**{unbekannt} unbekannt**"
    if unbekannt not in ("0", "?"):
        unbekannt_teil = f"⚠️ {unbekannt_teil}"
    lines.append(
        f"Quellen {gesamt}: {notiz} Notiz · {manuell} manuell · "
        f"{ausgeschlossen} ausgeschlossen · {unbekannt_teil}"
    )
    lines.append(f"Neu {neu} · geändert {geaendert} · unverändert {unveraendert}")
    if STATUS == "fail":
        lines.append(
            f"⚠️ Kernschritt fehlgeschlagen: {DETAIL or 'unbekannt'} — Bericht kann veraltet sein."
        )

    board = board_progress()
    structure = board_structure()
    detail = structure.split(":", 1)[1].strip() if ":" in structure else structure
    if board:
        hint = f" · {detail}" if detail and not detail.startswith("ok") else ""
        lines.append(f"Board: {board}{hint}")
    elif structure:
        lines.append(structure)
    if "FEHLER" in structure:
        lines.append(f"⚠️ **Board-Struktur prüfen** — Details in `{VAULT_LABEL}/_tools/daily.log`")

    rows = faellige()
    lines.append("")
    if rows:
        lines.append("**Fällig (bis 7 Tage)**")
        lines.extend(rows)
    else:
        lines.append("Keine Frist in den nächsten sieben Tagen.")

    lines.append("")
    lines.append(f"Details: `{VAULT_LABEL}/00 Brain/Status.md` · `Board.md`")
    return "\n".join(lines)


def send(url: str, content: str) -> int:
    body = json.dumps(
        {"content": content[:1900], "username": TITEL},
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "ProjektJLU-Notifier"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return response.status


def main() -> int:
    content = message()
    url = webhook()

    if DRY:
        print(content)
        if not url:
            print("\nDiscord: kein Webhook hinterlegt, nicht gesendet.")
        return 0

    if not url:
        print("Discord: übersprungen (kein Webhook hinterlegt)")
        return 0

    if not url.startswith(ALLOWED):
        print("Discord: Adresse ist keine Discord-Webhook-Adresse, nicht gesendet")
        return 1

    try:
        print(f"Discord: gesendet (HTTP {send(url, content)})")
        return 0
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:200]
        print(f"Discord: Fehler HTTP {exc.code} {detail}")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"Discord: Fehler {exc}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
