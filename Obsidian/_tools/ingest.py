#!/usr/bin/env python3
"""Liest die Quellen aus 'Project JLU/' in den Obsidian-Vault ein.

- Markdown-Dateien werden zu Notizen mit Frontmatter (quelle, stand, hash).
- Relative Links in den Steckbriefen werden zu Wikilinks umgeschrieben.
- PDFs und Grafiken werden als Anhang kopiert.
- Neue und geänderte Dateien landen im Ingest Log und in 'Neu seit letztem Lauf.md'.

Nur diese Ziele werden geschrieben:
    10 Thema/Steckbriefe/   40 Protokolle/   90 Anhänge/
    10 Thema/Projektrahmen (Quelle).md
    10 Thema/Reservierung (Quelle).md
    30 Plan/GitLab-Leitfaden (Quelle).md
    00 Brain/Ingest Log.md  00 Brain/Neu seit letztem Lauf.md
Handgeschriebene Notizen bleiben unangetastet.

Aufruf:
    python3 Obsidian/_tools/ingest.py           # einlesen
    python3 Obsidian/_tools/ingest.py --check   # nur berichten, nichts schreiben
    python3 Obsidian/_tools/ingest.py --force   # alles neu rendern (nach Änderungen am Skript)
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
ROOT = VAULT.parent
SOURCE_DIR = ROOT / "Project JLU"
STATE_FILE = VAULT / "_tools" / ".ingest-state.json"
LOG_FILE = VAULT / "00 Brain" / "Ingest Log.md"
NEWS_FILE = VAULT / "00 Brain" / "Neu seit letztem Lauf.md"

CHECK_ONLY = "--check" in sys.argv
FORCE = "--force" in sys.argv
NOW = datetime.now().strftime("%Y-%m-%d %H:%M")
TODAY = datetime.now().strftime("%Y-%m-%d")

SKIP_NAMES = {".DS_Store", ".gitkeep"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Warnung: Zustandsdatei unlesbar, wird neu aufgebaut.")
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def title_of(path: Path, text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").replace("_", " ")


def relink(text: str) -> str:
    """Relative Markdown-Links auf Wikilinks umschreiben (Vault-sicher).

    Obsidian löst Wikilinks am kürzesten eindeutigen Dateinamen auf, deshalb werden
    Ordnerpfade entfernt. Grafiken bleiben Markdown-Links mit relativem Pfad.
    """
    # Startseite der Betreuung
    text = re.sub(r"\[([^\]]+)\]\(\.\./README\.md\)", r"[[Thema 29 – Überblick|\1]]", text)
    # Leitfaden (aus README und aus Steckbriefen, auch mit Anker)
    text = re.sub(
        r"\[([^\]]+)\]\([^)]*gitlab-leitfaden\.md(?:#[^)]*)?\)",
        r"[[GitLab-Leitfaden (Quelle)|\1]]",
        text,
    )
    # Grafiken und HTML der Projektkarte liegen im Anhang
    text = re.sub(r"\]\(projektkarte\.(svg|html|png)\)", r"](../90 Anhänge/projektkarte.\1)", text)

    def to_wikilink(match: re.Match) -> str:
        label, target = match.group(1), match.group(2).rstrip("/")
        return f"[[{target.split('/')[-1]}|{label}]]"

    # Nachbardateien, auch mit Ordnerpfad: [2.2](2-2-regelgraph.md) -> [[2-2-regelgraph|2.2]]
    text = re.sub(r"\[([^\]]+)\]\((?!https?:|#|\.\.)([\w./-]+)\.md\)", to_wikilink, text)
    return text


def render_note(src: Path, relative: str, text: str) -> str:
    body = relink(text).strip() + "\n"
    stamp = datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d")
    header = (
        "---\n"
        f'titel: "{title_of(src, text)}"\n'
        f'quelle: "{relative}"\n'
        f"stand: {stamp}\n"
        f"hash: {digest(src)[:12]}\n"
        "automatisch: true\n"
        "---\n\n"
        f"> Automatisch eingelesen aus `{relative}` am {TODAY}.\n"
        "> Diese Notiz nicht bearbeiten — inhaltliche Arbeit gehört in die\n"
        "> handgeschriebenen Notizen, diese Datei wird beim nächsten Lauf überschrieben.\n\n"
    )
    return header + body


def plan() -> list[tuple[Path, Path, str]]:
    """(Quelle, Ziel, relatives Quell-Label)"""
    jobs: list[tuple[Path, Path, str]] = []

    if SOURCE_DIR.is_dir():
        for src in sorted(SOURCE_DIR.rglob("*")):
            if not src.is_file() or src.name in SKIP_NAMES:
                continue
            rel = src.relative_to(SOURCE_DIR)
            label = f"Project JLU/{rel.as_posix()}"

            if src.suffix.lower() == ".md":
                parts = rel.parts
                if parts[0] == "steckbriefe":
                    dest = VAULT / "10 Thema" / "Steckbriefe" / src.name
                elif parts[0] == "protokolle":
                    if rel.name == "README.md":
                        continue  # Hinweise zur Ablage, kein Protokoll
                    dest = VAULT / "40 Protokolle" / (src.stem.replace("_", " ") + " (Quelle).md")
                elif rel.as_posix() == "README.md":
                    dest = VAULT / "10 Thema" / "Projektrahmen (Quelle).md"
                elif rel.as_posix() == "gitlab-leitfaden.md":
                    dest = VAULT / "30 Plan" / "GitLab-Leitfaden (Quelle).md"
                else:
                    dest = VAULT / "90 Anhänge" / src.name
                jobs.append((src, dest, label))
            else:
                jobs.append((src, VAULT / "90 Anhänge" / src.name, label))

    reservierung = ROOT / "Reservierung_Thema_29.txt"
    if reservierung.is_file():
        jobs.append(
            (
                reservierung,
                VAULT / "10 Thema" / "Reservierung (Quelle).md",
                "Reservierung_Thema_29.txt",
            )
        )

    return jobs


def ingest_markdown(src: Path, dest: Path, label: str) -> str:
    text = src.read_text(encoding="utf-8", errors="replace")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(render_note(src, label, text), encoding="utf-8")
    return dest


def ingest_text(src: Path, dest: Path, label: str) -> str:
    text = src.read_text(encoding="utf-8", errors="replace").strip()
    dest.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d")
    body = (
        "---\n"
        'titel: "Reservierung Thema 29 (Quelle)"\n'
        f'quelle: "{label}"\n'
        f"stand: {stamp}\n"
        f"hash: {digest(src)[:12]}\n"
        "automatisch: true\n"
        "---\n\n"
        f"> Automatisch eingelesen aus `{label}` am {TODAY}.\n\n"
        "```\n" + text + "\n```\n"
    )
    dest.write_text(body, encoding="utf-8")
    return dest


def ingest_binary(src: Path, dest: Path) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return dest


def append_log(entries: list[tuple[str, str, str]]) -> None:
    """Zeilen direkt unter der Tabellenkopfzeile einfügen (neueste oben)."""
    if not entries:
        return
    rows = "\n".join(f"| {NOW} | {a} | `{b}` | `{c}` |" for a, b, c in entries)
    if LOG_FILE.exists():
        lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    else:
        lines = ["---", "titel: Ingest Log", "---", "", "# Ingest Log", "",
                 "| Zeitpunkt | Aktion | Quelle | Ziel |", "|---|---|---|---|"]
    insert_at = None
    for i, line in enumerate(lines):
        if re.match(r"^\|\s*-{3,}", line):
            insert_at = i + 1
            break
    if insert_at is None:
        lines += ["", "| Zeitpunkt | Aktion | Quelle | Ziel |", "|---|---|---|---|"]
        insert_at = len(lines)
    lines.insert(insert_at, rows)
    LOG_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_news(new: list[str], changed: list[str], unchanged: int) -> None:
    def block(items: list[str]) -> str:
        if not items:
            return "_nichts_\n"
        return "\n".join(f"- `{i}`" for i in items) + "\n"

    body = (
        "---\n"
        "titel: Neu seit letztem Lauf\n"
        f"stand: {TODAY}\n"
        "---\n\n"
        "# Neu seit letztem Lauf\n\n"
        f"Lauf: {NOW}\n\n"
        f"## Neu ({len(new)})\n\n{block(new)}\n"
        f"## Geändert ({len(changed)})\n\n{block(changed)}\n"
        f"## Unverändert: {unchanged} Dateien\n\n"
        "## Was jetzt zu tun ist\n\n"
        "1. Neue Protokolle lesen: Fristen, Beschlüsse, Aufgaben → [[Status]] fortschreiben.\n"
        "2. Geänderte Steckbriefe prüfen: Fragestellung, Datengrundlage, „Nicht Teil dieser Arbeit“.\n"
        "3. Wenn eine Vorgabe kippt (Prüfungsform, Abgabedatum, Format), Eintrag in\n"
        "   [[Entscheidungen]] mit Datum und Grund.\n"
    )
    NEWS_FILE.write_text(body, encoding="utf-8")


def main() -> int:
    if not SOURCE_DIR.is_dir():
        print(f"Fehler: Quellordner nicht gefunden: {SOURCE_DIR}")
        return 1

    state = load_state()
    new: list[str] = []
    changed: list[str] = []
    unchanged = 0
    log_entries: list[tuple[str, str, str]] = []
    wrote = False

    for src, dest, label in plan():
        current = digest(src)
        previous = state.get(label, {}).get("hash")

        if previous == current and dest.exists() and not FORCE:
            unchanged += 1
            continue

        action = "neu" if previous is None else "geändert"
        if CHECK_ONLY:
            print(f"[{action}] {label} -> {dest.relative_to(VAULT)}")
            (new if previous is None else changed).append(label)
            continue

        if src.suffix.lower() == ".md":
            ingest_markdown(src, dest, label)
        elif src.suffix.lower() == ".txt":
            ingest_text(src, dest, label)
        else:
            ingest_binary(src, dest)

        state[label] = {
            "hash": current,
            "ziel": dest.relative_to(VAULT).as_posix(),
            "eingelesen": NOW,
        }
        log_entries.append((action, label, dest.relative_to(VAULT).as_posix()))
        (new if previous is None else changed).append(label)
        wrote = True

    if CHECK_ONLY:
        print(f"\nNeu: {len(new)}, geändert: {len(changed)}, unverändert: {unchanged}")
        return 0

    # Aufräumen: Ziele, deren Quelle verschwunden ist, aus dem Zustand entfernen.
    live = {label for _, _, label in plan()}
    for label in [k for k in state if k not in live]:
        del state[label]

    save_state(state)
    append_log(log_entries)
    write_news(new, changed, unchanged)

    print(f"Lauf {NOW}")
    print(f"  neu:        {len(new)}")
    print(f"  geändert:   {len(changed)}")
    print(f"  unverändert:{unchanged}")
    if log_entries:
        print("  siehe 00 Brain/Ingest Log.md und 00 Brain/Neu seit letztem Lauf.md")
    if not wrote:
        print("  keine Änderungen an den Quellen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
