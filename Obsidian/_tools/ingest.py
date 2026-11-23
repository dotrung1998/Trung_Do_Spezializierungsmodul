#!/usr/bin/env python3
"""Liest die Quellen aus 'Project JLU/' in den Obsidian-Vault ein und prueft die Abdeckung.

Quellen:
    Project JLU/                 Unterlagen der Betreuung (Steckbriefe, Protokolle,
                                 Leitfaden, Projektkarte)
    Reservierung_Thema_29.txt    Reservierungsbestaetigung der SPZ-Plattform

Jede Quelldatei muss am Ende genau einen Zustand haben:
    notiz            automatisch erzeugte (Quelle)-Notiz
    manuell          in einer handgeschriebenen Notiz beschrieben (abdeckung-regeln.json)
    ausgeschlossen   bewusst ausgelassen, mit Grund (abdeckung-regeln.json)
    unbekannt        nichts davon -> wird gemeldet und der Lauf endet mit Fehler

Geschrieben werden ausschliesslich:
    10 Thema/Steckbriefe/*       40 Protokolle/*
    10 Thema/Projektrahmen (Quelle).md, Reservierung (Quelle).md
    30 Plan/GitLab-Leitfaden (Quelle).md, Abgaben (auto).md
    90 Anhaenge/…                (Notizen ohne eigenen Ort, kopierte Binaerdateien)
    00 Brain/Ingest Log.md       00 Brain/Neu seit letztem Lauf.md
    _tools/abdeckung.json        _tools/.ingest-state.json

Handgeschriebene Notizen bleiben unangetastet.

Aufruf:
    python3 Obsidian/_tools/ingest.py            # einlesen und Abdeckung pruefen
    python3 Obsidian/_tools/ingest.py --check    # nur berichten, nichts schreiben
    python3 Obsidian/_tools/ingest.py --force    # alles neu rendern
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
VAULT = TOOLS.parent
ROOT = VAULT.parent

SOURCE = ROOT / "Project JLU"
ATTACH = VAULT / "90 Anhänge"

STATE_FILE = TOOLS / ".ingest-state.json"
RULES_FILE = TOOLS / "abdeckung-regeln.json"
COVER_FILE = TOOLS / "abdeckung.json"
FRISTEN_FILE = TOOLS / "fristen.json"
LOG_FILE = VAULT / "00 Brain" / "Ingest Log.md"
NEWS_FILE = VAULT / "00 Brain" / "Neu seit letztem Lauf.md"
ABGABEN_FILE = VAULT / "30 Plan" / "Abgaben (auto).md"

CHECK_ONLY = "--check" in sys.argv
FORCE = "--force" in sys.argv
NOW = datetime.now().strftime("%Y-%m-%d %H:%M")
TODAY = datetime.now().strftime("%Y-%m-%d")
RENDER_VERSION = 1

SKIP_NAMES = {".gitkeep", ".DS_Store"}
# Formate, die zu einer Notiz mit extrahiertem Text werden. Alles andere ist
# entweder in abdeckung-regeln.json beschrieben oder gilt als unbekannt.
TEXT_SUFFIX = {".md", ".txt", ".pdf", ".docx", ".tex"}

# Abgabeartefakte im Projektordner: Pfad -> (Titel, Zielnotiz, Frist-ID)
# Nur echte, pruefbare Dateien. Fehlt die Datei, steht in der Tabelle "fehlt".
ABGABEN = {
    "report/main.pdf": ("Bericht (PDF)", "30 Plan/LaTeX-Bericht.md", "ABGABE"),
    "report/expose.pdf": ("Kurzexposé (PDF)", "50 Kommunikation/E-Mail 2 – Kurzexposé.md", "MAIL2"),
}


# ------------------------------------------------------------------ Grundlagen


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel_root(path: Path) -> str:
    return unicodedata.normalize("NFC", path.relative_to(ROOT).as_posix())


def run_tool(cmd: list) -> str:
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout if out.returncode == 0 else ""


def extract(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return run_tool(["pdftotext", "-layout", str(path), "-"])
    if suffix == ".docx":
        return run_tool(["pandoc", str(path), "-t", "plain"])
    if suffix in {".md", ".txt", ".tex"}:
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""
    return ""


def load_json(path: Path, fallback):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            print(f"Warnung: {path.name} unlesbar, wird neu aufgebaut.")
    return fallback


def load_rules() -> dict:
    data = load_json(RULES_FILE, {})
    data.setdefault("ausgeschlossen", [])
    data.setdefault("manuell", [])
    return data


def write_if_changed(path: Path, body: str, volatile: str = r"^$") -> bool:
    if path.exists():
        old = path.read_text(encoding="utf-8")
        strip = lambda t: re.sub(volatile, "", t, flags=re.M)
        if strip(old) == strip(body):
            return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return True


def fence(text: str, limit: int = 6000) -> str:
    text = text.strip()
    if not text:
        return ""
    if len(text) > limit:
        text = text[:limit].rstrip() + "\n… (gekürzt)"
    return "~~~~\n" + text.replace("~~~~", "~~~") + "\n~~~~"


# ------------------------------------------------------------------ Ziele


def relink(text: str) -> str:
    """Relative Markdown-Links auf Wikilinks umschreiben (Vault-sicher)."""
    text = re.sub(r"\[([^\]]+)\]\(\.\./README\.md\)", r"[[Thema 29 – Überblick|\1]]", text)
    text = re.sub(
        r"\[([^\]]+)\]\([^)]*gitlab-leitfaden\.md(?:#[^)]*)?\)",
        r"[[GitLab-Leitfaden (Quelle)|\1]]",
        text,
    )
    text = re.sub(r"\]\(projektkarte\.(svg|html|png)\)", r"](../90 Anhänge/projektkarte.\1)", text)

    def to_wikilink(match: re.Match) -> str:
        label, target = match.group(1), match.group(2).rstrip("/")
        return f"[[{target.split('/')[-1]}|{label}]]"

    text = re.sub(r"\[([^\]]+)\]\((?!https?:|#|\.\.)([\w./-]+)\.md\)", to_wikilink, text)
    return text


def title_of(src: Path, text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return src.stem.replace("-", " ").replace("_", " ")


def target_for(src: Path, key: str):
    """(Notiz, Anhang oder None, Titel) fuer eine Quelle; None = kein Weg bekannt."""
    suffix = src.suffix.lower()
    if suffix not in TEXT_SUFFIX:
        return None

    prefix = "Project JLU/"
    rel = Path(key[len(prefix):]) if key.startswith(prefix) else Path(key)
    stem = src.stem.replace("_", " ")

    if suffix == ".md":
        parts = rel.parts
        if parts[0] == "steckbriefe":
            return VAULT / "10 Thema" / "Steckbriefe" / src.name, None, src.stem
        if parts[0] == "protokolle":
            return VAULT / "40 Protokolle" / f"{stem} (Quelle).md", None, stem
        if rel.as_posix() == "README.md":
            return VAULT / "10 Thema" / "Projektrahmen (Quelle).md", None, "Projektrahmen"
        if rel.as_posix() == "gitlab-leitfaden.md":
            return VAULT / "30 Plan" / "GitLab-Leitfaden (Quelle).md", None, "GitLab-Leitfaden"

    if key == "Reservierung_Thema_29.txt":
        return VAULT / "10 Thema" / "Reservierung (Quelle).md", None, "Reservierung Thema 29"

    note = VAULT / "90 Anhänge" / f"{stem} (Quelle).md"
    attach = ATTACH / src.name
    return note, attach, stem


def source_note(title: str, key: str, src: Path, body: str, hash_value: str) -> str:
    stamp = datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d")
    return (
        "---\n"
        f'titel: "{title}"\n'
        f'quelle: "{key}"\n'
        f"stand: {stamp}\n"
        f"hash: {hash_value[:12]}\n"
        "automatisch: true\n"
        "---\n\n"
        f"> Automatisch eingelesen aus `{key}` am {TODAY}. Nicht bearbeiten —\n"
        "> inhaltliche Arbeit gehört in die handgeschriebenen Notizen.\n\n"
        + body.strip()
        + "\n"
    )


# ------------------------------------------------------------------ Einlesen


def discover() -> list:
    """Alle Quelldateien, die in die Abdeckung eingehen."""
    found = []
    if SOURCE.is_dir():
        found += [p for p in SOURCE.rglob("*") if p.is_file() and p.name not in SKIP_NAMES]
    reservierung = ROOT / "Reservierung_Thema_29.txt"
    if reservierung.is_file():
        found.append(reservierung)
    return sorted(set(found))


def ingest_file(src: Path, state: dict, log: list) -> str:
    key = rel_root(src)
    current = digest(src)
    target = target_for(src, key)
    if target is None:
        return "unbekannt"
    dest, attach, title = target
    prev = state.get(key, {})
    if (
        prev.get("hash") == current
        and prev.get("v") == RENDER_VERSION
        and dest.exists()
        and not FORCE
    ):
        return "unverändert"

    text = extract(src)
    label = title_of(src, text) if src.suffix.lower() == ".md" else title

    if src.suffix.lower() == ".md":
        body = relink(text)
    elif src.suffix.lower() == ".txt":
        body = "```\n" + text.strip() + "\n```\n"
    else:
        head = f"# {label} (Quelle)\n\n"
        if attach is not None:
            head += f"Anhang: `{attach.relative_to(VAULT).as_posix()}`\n\n"
        head += "## Inhalt (automatisch extrahiert)\n\n"
        body = head + (
            fence(text)
            if text.strip()
            else (
                "_Kein Text extrahiert. Grafik oder nicht lesbares Format — "
                "Inhalt in der handgeschriebenen Notiz beschreiben._\n"
            )
        )

    action = "neu" if not prev else "geändert"
    if CHECK_ONLY:
        print(f"[{action}] {key} -> {dest.relative_to(VAULT)}")
        return action

    write_if_changed(dest, source_note(label, key, src, body, current))
    if attach is not None:
        attach.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, attach)
    state[key] = {
        "hash": current,
        "ziel": dest.relative_to(VAULT).as_posix(),
        "anhang": attach.relative_to(VAULT).as_posix() if attach else "",
        "text": bool(text.strip()),
        "v": RENDER_VERSION,
        "eingelesen": NOW,
    }
    log.append((action, key, dest.relative_to(VAULT).as_posix()))
    return action


# ------------------------------------------------------------------ Abgaben


def load_fristen() -> dict:
    items = load_json(FRISTEN_FILE, [])
    return {item.get("id", ""): item for item in items if isinstance(item, dict)}


def save_cover(cov: dict) -> None:
    """Abdeckung schreiben, ohne bei gleichbleibendem Inhalt neu zu schreiben."""
    body = json.dumps(cov, indent=2, ensure_ascii=False) + "\n"
    if COVER_FILE.exists():
        try:
            old = json.loads(COVER_FILE.read_text(encoding="utf-8"))
            new = json.loads(body)
            old.pop("stand", None)
            new.pop("stand", None)
            if old == new:
                return
        except (OSError, ValueError):
            pass
    COVER_FILE.write_text(body, encoding="utf-8")


def render_abgaben() -> bool:
    fristen = load_fristen()
    rows = []
    for path, (title, note, frist_id) in ABGABEN.items():
        file = ROOT / path
        frist = fristen.get(frist_id, {})
        termin = frist.get("datum", "—")
        if file.is_file():
            kb = max(1, round(file.stat().st_size / 1024))
            stand = datetime.fromtimestamp(file.stat().st_mtime).strftime("%Y-%m-%d")
            rows.append(f"| {title} | `{path}` | {kb} KB | {stand} | {termin} |")
        else:
            rows.append(f"| {title} | `{path}` | — | **fehlt** | {termin} |")

    body = (
        "---\n"
        "titel: Abgaben (auto)\n"
        f"stand: {TODAY}\n"
        "automatisch: true\n"
        "---\n\n"
        "# Abgaben (automatisch)\n\n"
        f"Lauf: {NOW}. Quelle: die Dateien im Projektordner.\n\n"
        "| Artefakt | Datei | Größe | Stand | Frist |\n|---|---|---|---|---|\n"
        + "\n".join(rows)
        + "\n\n"
        "Die Frist kommt aus `_tools/fristen.json`. Eine vorhandene PDF belegt nur, dass\n"
        "der Satz gebaut wurde — nicht, dass die Abgabe im Abgaberepo liegt.\n"
    )
    return write_if_changed(ABGABEN_FILE, body, r"^Lauf: .*$")


# ------------------------------------------------------------------ Abdeckung


def manual_note(key: str, rules: dict) -> str:
    for entry in rules.get("manuell", []):
        if unicodedata.normalize("NFC", entry.get("pfad", "")) == key:
            return entry.get("notiz", "")
    return ""


def excluded(key: str, name: str, rules: dict):
    for rule in rules.get("ausgeschlossen", []):
        if fnmatch.fnmatch(key, rule.get("muster", "")) or fnmatch.fnmatch(name, rule.get("muster", "")):
            return rule.get("grund", "")
    return None


def coverage(state: dict, rules: dict) -> dict:
    entries, unknown, ohne_text = [], [], []

    for p in discover():
        key = rel_root(p)
        grund = excluded(key, p.name, rules)
        if grund is not None:
            entries.append({"pfad": key, "status": "ausgeschlossen", "ziel": "", "grund": grund})
            continue

        note = manual_note(key, rules)
        if note:
            entries.append({"pfad": key, "status": "manuell", "ziel": note, "grund": ""})
            continue

        entry = state.get(key)
        if entry:
            entries.append(
                {"pfad": key, "status": "notiz", "ziel": entry.get("ziel", ""), "grund": ""}
            )
            if not entry.get("text", True):
                ohne_text.append(key)
            continue

        unknown.append(key)
        entries.append({"pfad": key, "status": "unbekannt", "ziel": "", "grund": ""})

    zaehlung = {
        s: sum(1 for e in entries if e["status"] == s)
        for s in ("notiz", "manuell", "ausgeschlossen", "unbekannt")
    }
    return {
        "stand": NOW,
        "dateien": entries,
        "unbekannt": unknown,
        "ohne_text": ohne_text,
        "zaehlung": zaehlung,
    }


# ------------------------------------------------------------------ Protokoll


def append_log(entries: list) -> None:
    if not entries:
        return
    rows = "\n".join(f"| {NOW} | {a} | `{b}` | `{c}` |" for a, b, c in entries)
    if LOG_FILE.exists():
        lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    else:
        lines = [
            "---", "titel: Ingest Log", "---", "", "# Ingest Log", "",
            "| Zeitpunkt | Aktion | Quelle | Ziel |", "|---|---|---|---|",
        ]
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


def write_news(new: list, changed: list, unchanged: int, cov: dict) -> None:
    def block(items: list) -> str:
        return "\n".join(f"- `{i}`" for i in items) + "\n" if items else "_nichts_\n"

    z = cov["zaehlung"]
    unknown = cov["unbekannt"]
    ohne_text = cov["ohne_text"]

    body = (
        "---\n"
        "titel: Neu seit letztem Lauf\n"
        f"stand: {TODAY}\n"
        "---\n\n"
        "# Neu seit letztem Lauf\n\n"
        f"Lauf: {NOW}\n\n"
        f"## Neu ({len(new)})\n\n{block(new)}\n"
        f"## Geändert ({len(changed)})\n\n{block(changed)}\n"
        f"## Unverändert: {unchanged} Quellen\n\n"
        "## Abdeckung\n\n"
        f"- Quellen gesamt: **{sum(z.values())}**\n"
        f"- durch Notiz: {z['notiz']} · manuell beschrieben: {z['manuell']} · "
        f"ausgeschlossen: {z['ausgeschlossen']} · **unbekannt: {z['unbekannt']}**\n"
        + (
            "\n**Unbekannt (weder Notiz noch Ausschluss):**\n\n"
            + "\n".join(f"- `{u}`" for u in unknown)
            + "\n\n> Diese Dateien tragen möglicherweise Vorgaben und sind noch nicht\n"
            "> erfasst. Entweder einlesen (Format ergänzen) oder in\n"
            "> `_tools/abdeckung-regeln.json` mit Grund ausschließen.\n"
            if unknown
            else "\nAlle Quellen sind erfasst oder begründet ausgeschlossen.\n"
        )
        + (
            "\n**Ohne Text extrahiert:**\n\n" + "\n".join(f"- `{u}`" for u in ohne_text) + "\n"
            if ohne_text
            else ""
        )
        + "\n## Was jetzt zu tun ist\n\n"
        "1. Neue Protokolle lesen: Fristen, Beschlüsse, Aufgaben → [[Status]] fortschreiben.\n"
        "2. Geänderte Steckbriefe prüfen: Fragestellung, Datengrundlage, „Nicht Teil dieser Arbeit“.\n"
        "3. Wenn eine Vorgabe kippt (Prüfungsform, Abgabedatum, Format), Eintrag in\n"
        "   [[Entscheidungen]] mit Datum und Grund.\n"
    )
    write_if_changed(NEWS_FILE, body, r"^Lauf: .*$")


def cleanup(state: dict, live: set) -> list:
    """Quelle weg oder Zielnotiz verschwunden -> Zustand und Notiz aufraeumen."""
    removed = []
    for key in [k for k in state if k not in live]:
        entry = state.pop(key)
        target = VAULT / entry.get("ziel", "")
        if entry.get("ziel") and target.is_file():
            target.unlink()
        removed.append((key, entry.get("ziel", "")))
    return removed


def main() -> int:
    if not SOURCE.is_dir():
        print(f"Fehler: Quellordner nicht gefunden: {SOURCE}")
        return 1

    state = load_json(STATE_FILE, {})
    rules = load_rules()
    new, changed, unchanged, log = [], [], 0, []

    for src in discover():
        if excluded(rel_root(src), src.name, rules) is not None:
            continue
        if manual_note(rel_root(src), rules):
            continue
        result = ingest_file(src, state, log)
        if result == "unbekannt":
            continue  # wird von der Abdeckung gemeldet
        if result == "neu":
            new.append(rel_root(src))
        elif result == "geändert":
            changed.append(rel_root(src))
        else:
            unchanged += 1

    live = {rel_root(p) for p in discover()}
    cov = coverage(state, rules)

    if CHECK_ONLY:
        print(f"\nNeu: {len(new)}, geändert: {len(changed)}, unverändert: {unchanged}")
        print(
            f"Abdeckung: {cov['zaehlung']['notiz']} Notiz, "
            f"{cov['zaehlung']['manuell']} manuell, "
            f"{cov['zaehlung']['ausgeschlossen']} ausgeschlossen, "
            f"{cov['zaehlung']['unbekannt']} unbekannt"
        )
        for u in cov["unbekannt"]:
            print(f"  unbekannt: {u}")
        return 1 if cov["unbekannt"] else 0

    removed = cleanup(state, live)
    log.extend(("entfernt", key, ziel) for key, ziel in removed)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    append_log(log)
    # Ohne Quellenänderung bleibt der letzte Bericht stehen. Fehlt er aber (frischer
    # Checkout auf dem Runner) oder weicht die Abdeckung ab, wird er neu geschrieben.
    def coverage_stale() -> bool:
        if not NEWS_FILE.exists():
            return True
        text = NEWS_FILE.read_text(encoding="utf-8")
        u = re.search(r"\*\*unbekannt: (\d+)\*\*", text)
        t = re.search(r"Quellen gesamt: \*\*(\d+)\*\*", text)
        return (
            not u or not t
            or int(u.group(1)) != len(cov["unbekannt"])
            or int(t.group(1)) != sum(cov["zaehlung"].values())
        )

    if new or changed or removed or coverage_stale():
        write_news(new, changed, unchanged, cov)
    abgaben_changed = render_abgaben()
    save_cover(cov)

    print(f"Lauf {NOW}")
    print(f"  neu:         {len(new)}")
    print(f"  geändert:    {len(changed)}")
    print(f"  unverändert: {unchanged}")
    if removed:
        print(f"  entfernt:    {len(removed)} (verwaiste Zustände aufgeräumt)")
    if abgaben_changed:
        print("  Abgaben-Tabelle aktualisiert: 30 Plan/Abgaben (auto).md")
    print(
        f"  Abdeckung:   {cov['zaehlung']['notiz']} Notiz, "
        f"{cov['zaehlung']['manuell']} manuell, "
        f"{cov['zaehlung']['ausgeschlossen']} ausgeschlossen, "
        f"{cov['zaehlung']['unbekannt']} unbekannt"
    )
    if cov["unbekannt"]:
        print("\n  WARNUNG: Quellen ohne Notiz und ohne Ausschluss:")
        for u in cov["unbekannt"]:
            print(f"    - {u}")
        print("  -> Format ergänzen oder in _tools/abdeckung-regeln.json begründet ausschließen.")
        return 1
    if cov["ohne_text"]:
        print("  ohne Text extrahiert:")
        for u in cov["ohne_text"]:
            print(f"    - {u}")
    if not log and not abgaben_changed:
        print("  keine Änderungen an den Quellen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
