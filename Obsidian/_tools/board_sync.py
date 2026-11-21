#!/usr/bin/env python3
"""Tageslauf fuer das Kanban-Board: Status, Abhaengigkeiten, Folgearbeit.

Startet ueber _tools/daily.sh (launchd com.projectjlu.daily, 08:00).
Spalten: To Do · Doing · Done. Karten tragen optional "· braucht: X, Y".

Regeln
  * \\todo im Bericht offen   -> Karte nicht in "Done" (aus "Done" zurueck nach "To Do")
  * \\todo verschwunden       -> Karte nach "Done" mit Erledigt-Datum
  * Karte ohne Berichts-ID    -> "Done" nur, wenn abgehakt oder nach "Done" gezogen
  * Blocker offen             -> Vermerk "· blockiert: X offen"
  * Blocker erledigt          -> #ai wandert "To Do" -> "Doing", dann laeuft die
                                 Folgearbeit (jobs.py); #person/#team werden nur als
                                 "freigegeben durch X" markiert, nie entschieden
  * Karte in "Doing" mit offenem \\todo wird nie zurueckgeschoben
  * Ohne Aenderung wird keine Datei geschrieben (idempotent)

Aufruf: python3 board_sync.py [--board PFAD] [--report PFAD] [--dry-run]
"""

import datetime
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import jobs  # noqa: E402

ROOT = HERE.parents[1]
BOARD = ROOT / "Obsidian" / "30 Plan" / "Board.md"
REPORT = ROOT / "report"
LOG = HERE / "board.log"

# id, Datei, Anker (Textanfang des \todo), Rolle, Kartentitel, Kurzbeschreibung
ITEMS = [
    ("6.1", "chapters/06_ergebnisse.tex", r"\todo{Fehlt: die Tabelle der Abweichungsraten",
     "ai", "6.1 · Abweichungsraten je Sachverhaltstyp", "Tabelle mit Wilson-Intervall; entscheidet H1"),
    ("6.2", "chapters/06_ergebnisse.tex", r"\todo{Fehlt: Precision, Recall und F1",
     "ai", "6.2 · Verfahrensvergleich", "Precision, Recall, F1 je Variante, Recall-Differenz"),
    ("6.3", "chapters/06_ergebnisse.tex", r"\todo{Fehlt: die Häufigkeit je Fehlerklasse",
     "ai", "6.3 · Fehleranalyse", "Häufigkeit je Fehlerklasse aus A.4, je ein Beispiel"),
    ("6.4", "chapters/06_ergebnisse.tex", r"\todo{Fehlt: der zweite Fall",
     "ai", "6.4 · Fall 2: Versionsartefakt", "aus dem klassifizierten Fundbestand, nicht von Hand gewählt"),
    ("7.2", "chapters/07_diskussion.tex", r"\todo{Fehlt: das Urteil je Hypothese",
     "ai", "7.2 · Urteil je Hypothese", "bestätigt / teilweise / widerlegt, mit der Zahl aus Kapitel 6"),
    ("8", "chapters/08_fazit.tex", r"\todo{Fehlt: die eine Zahl mit Intervall",
     "ai", "8 · Fazit: die eine Zahl", "Abweichungsrate oder Anteil echter Widersprüche, mit Intervall"),
    ("ZUS", "frontmatter/abstrakt.tex", r"\todo{Fehlt: die wichtigste Zahl",
     "ai", "ZUS · Zusammenfassung: Ergebnissatz", "dieselbe Zahl in einem Satz"),
    ("A.1", "backmatter/anhang.tex", r"\todo{Tabelle der untersuchten Sachverhaltstypen",
     "person", "A.1 · Faktkatalog: zwölf Sachverhaltstypen festlegen",
     "Entscheidung mit Team Gamma, Grundlage für Kapitel 4.2 und Anhang A.1"),
    ("A.3", "backmatter/anhang.tex", r"\todo{Modellname, Version, Temperatur",
     "person", "A.3 · Modell, Prompt-Version und Umgebung festlegen",
     "Entscheidung, danach Anhang A.3 und der Lauf"),
]
META = {i[0]: i for i in ITEMS}

CARD_RE = re.compile(r"^- \[( |x)\] (?:⚠ )?\*\*([A-Za-z0-9.]+) · ")
DEP_RE = re.compile(r"braucht:\s*([^·]+)")
STAMP = "> Letzter Abgleich: "
NOTE_RE = (
    r"\s*·\s*(?:erledigt \d{4}-\d{2}-\d{2}"
    r"|Ergebnis: [^·]+"
    r"|freigegeben durch [^·]+"
    r"|blockiert: [^·]+"
    r"|wartet: [^·]+"
    r"|offen: [^·]+)"
)


def clean(line):
    """Entfernt alle vom Skript geschriebenen Vermerke, laesst 'braucht:' stehen."""
    return re.sub(NOTE_RE, "", line).rstrip()


def strip_note(line, kind):
    """Entfernt nur eine Vermerkart (z. B. 'wartet:')."""
    return re.sub(rf"\s*·\s*{kind}: [^·]+", "", line).rstrip()


def with_note(line, note):
    """Ersetzt Freigabe-/Blockiert-/sonstige Vermerke und behaelt 'wartet:'/'erledigt'."""
    wait = re.search(r"\s*·\s*wartet: [^·]+", line)
    done = re.search(r"\s*·\s*erledigt \d{4}-\d{2}-\d{2}", line)
    out = clean(line) + note
    if wait:
        out += " · " + wait.group(0).split("·", 1)[1].strip()
    if done:
        out += " · " + done.group(0).split("·", 1)[1].strip()
    return out


def deps_of(line):
    m = DEP_RE.search(line)
    if not m:
        return []
    return [d.strip() for d in m.group(1).split(",") if d.strip()]


def read(path):
    raw = path.read_text(encoding="utf-8")
    front, rest = "", raw
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        if end != -1:
            front, rest = raw[: end + 5], raw[end + 5:]
    tail = ""
    cut = rest.find("%% kanban:settings")
    if cut != -1:
        rest, tail = rest[:cut], rest[cut:]
    pre, lanes = [], []
    for line in rest.splitlines():
        if line.startswith("## "):
            lanes.append([line[3:].strip(), []])
        elif lanes:
            if line.strip():
                lanes[-1][1].append(line)
        else:
            pre.append(line)
    while pre and not pre[0].strip():
        pre.pop(0)
    while pre and not pre[-1].strip():
        pre.pop()
    return front, pre, lanes, tail.strip("\n")


def render(front, pre, lanes, tail):
    parts = []
    if front:
        parts.append(front.rstrip("\n"))
    if pre:
        parts.append("\n".join(pre))
    for name, lines in lanes:
        block = f"## {name}"
        if lines:
            block += "\n\n" + "\n".join(lines)
        parts.append(block)
    return "\n\n".join(parts) + "\n\n" + tail + "\n"


def find_card(lanes, cid):
    for name, lines in lanes:
        for i, line in enumerate(lines):
            m = CARD_RE.match(line)
            if m and m.group(2) == cid:
                return name, i, m.group(1) == "x"
    return None, None, False


def take_card(lanes, cid):
    name, i, checked = find_card(lanes, cid)
    if name is None:
        return None, None, False
    return name, next(ls for n, ls in lanes if n == name).pop(i), checked


def put_card(lanes, lane, line):
    next(ls for n, ls in lanes if n == lane).append(line)


def set_open(line):
    return re.sub(r"^- \[x\]", "- [ ]", line)


def done_line(line, date, extra=""):
    """Erledigt-Zeile: behaelt die Freigabe, entfernt Blocker/Warten, setzt Datum."""
    base = line
    for kind in ("blockiert", "wartet", "offen", "erledigt", "Ergebnis"):
        base = strip_note(base, kind)
    base = set_open(base)
    base = re.sub(r"^- \[ \]", "- [x]", base)
    return base + extra + f" · erledigt {date}"


def logged_today(today):
    """Hat der Lauf heute schon eine Zeile geschrieben?"""
    if not LOG.exists():
        return False
    lines = [l for l in LOG.read_text(encoding="utf-8").splitlines() if l.strip()]
    return bool(lines) and lines[-1].startswith(f"[{today}")


def main(argv):
    board, report, dry = BOARD, REPORT, False
    for i, a in enumerate(argv):
        if a == "--board":
            board = pathlib.Path(argv[i + 1])
        elif a == "--report":
            report = pathlib.Path(argv[i + 1])
        elif a == "--dry-run":
            dry = True

    original = board.read_text(encoding="utf-8")
    front, pre, lanes, tail = read(board)
    today = datetime.date.today().isoformat()
    events = []

    texts = {rel: (report / rel).read_text(encoding="utf-8") for _, rel, *_ in ITEMS}

    def todo_open(cid):
        _, rel, phrase, *_ = META[cid]
        return phrase in texts[rel]

    def is_done(cid):
        if cid in META:
            return not todo_open(cid)
        name, _, checked = find_card(lanes, cid)
        return checked or name == "Done"

    for _ in range(5):
        acted = False

        # A. Platzierung nach Erledigtstand (Berichtskarten)
        for cid in META:
            name, idx, checked = find_card(lanes, cid)
            if name is None:
                continue
            if todo_open(cid) and checked and name != "Done":
                lines = next(ls for n, ls in lanes if n == name)
                line = lines[idx]
                new = set_open(strip_note(line, "offen")) + " · offen: \\todo steht noch"
                if new != line:
                    lines[idx] = new
                    events.append(f"{cid} abgehakt, aber \\todo steht noch -> offen")
                    acted = True
                continue
            if todo_open(cid) and name == "Done":
                _, line, _ = take_card(lanes, cid)
                put_card(lanes, "To Do", set_open(clean(line)))
                events.append(f"{cid} wieder offen -> To Do")
                acted = True
            elif not todo_open(cid) and name != "Done":
                _, line, _ = take_card(lanes, cid)
                put_card(lanes, "Done", done_line(line, today))
                events.append(f"{cid} erledigt -> Done")
                acted = True

        # B. Karten ohne Berichts-ID: abgehakt heisst erledigt
        for name, lines in lanes:
            for line in list(lines):
                m = CARD_RE.match(line)
                if not m or m.group(2) in META:
                    continue
                if m.group(1) == "x" and name != "Done":
                    _, card, _ = take_card(lanes, m.group(2))
                    put_card(lanes, "Done", done_line(card, today))
                    events.append(f"{m.group(2)} abgehakt -> Done")
                    acted = True

        # C. Abhaengigkeiten: blockiert markieren oder freigeben
        ids = [CARD_RE.match(l).group(2) for _, lines in lanes for l in lines if CARD_RE.match(l)]
        for cid in ids:
            name, idx, checked = find_card(lanes, cid)
            if name is None:
                continue
            line = next(ls for n, ls in lanes if n == name)[idx]
            base = clean(line)
            deps = deps_of(base)
            if not deps:
                if base != line:
                    next(ls for n, ls in lanes if n == name)[idx] = base
                    acted = True
                continue
            open_deps = [d for d in deps if not is_done(d)]
            tag = "#person" if "#person" in base else "#team" if "#team" in base else "#ai"
            if open_deps:
                note = " · blockiert: " + ", ".join(open_deps) + " offen"
                if note in line and "freigegeben durch" not in line:
                    continue
                new = with_note(line, note)
                if new != line:
                    next(ls for n, ls in lanes if n == name)[idx] = new
                    events.append(f"{cid} blockiert: {', '.join(open_deps)}")
                    acted = True
            elif tag == "#ai" and name == "To Do":
                _, card, _ = take_card(lanes, cid)
                new = set_open(clean(card)) + f" · freigegeben durch {', '.join(deps)} ({today})"
                put_card(lanes, "Doing", new)
                events.append(f"{cid} freigegeben durch {', '.join(deps)} -> Doing")
                acted = True
            else:
                marker = f" · freigegeben durch {', '.join(deps)} ("
                if marker in line and "blockiert:" not in line:
                    continue
                new = with_note(line, f" · freigegeben durch {', '.join(deps)} ({today})")
                if new != line:
                    next(ls for n, ls in lanes if n == name)[idx] = new
                    events.append(f"{cid} freigegeben durch {', '.join(deps)}")
                    acted = True

        # D. Folgearbeit fuer freigegebene #ai-Karten in "Doing"
        ids = [CARD_RE.match(l).group(2) for _, lines in lanes for l in lines if CARD_RE.match(l)]
        for cid in ids:
            if cid not in META:
                continue
            name, idx, _ = find_card(lanes, cid)
            if name != "Doing":
                continue
            line = next(ls for n, ls in lanes if n == name)[idx]
            base = clean(line)
            if "#ai" not in base or not deps_of(base):
                continue
            if any(not is_done(d) for d in deps_of(base)) or not todo_open(cid):
                continue
            if dry:
                events.append(f"{cid}: dry-run, Folgearbeit uebersprungen")
                continue
            ok, msg = jobs.run(cid, META[cid][2], report)
            if ok:
                texts[META[cid][1]] = (report / META[cid][1]).read_text(encoding="utf-8")
                _, card, _ = take_card(lanes, cid)
                summary = msg.split(": ", 1)[-1]
                new = done_line(card, today, f" · Ergebnis: {summary}")
                put_card(lanes, "Done", new)
                events.append(f"{cid} Folgearbeit: {msg} -> Done")
            else:
                new = strip_note(line, "wartet") + f" · wartet: {msg}"
                if new != line:
                    next(ls for n, ls in lanes if n == name)[idx] = new
                    events.append(f"{cid} Folgearbeit nicht moeglich: {msg}")
                    acted = True

        if not acted:
            break

    pre = [STAMP + today if l.startswith(STAMP) else l for l in pre]
    rendered = render(front, pre, lanes, tail)
    changed = rendered != original
    if changed and not dry:
        board.write_text(rendered, encoding="utf-8")

    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if events:
        line = f"[{stamp}] " + " | ".join(events)
    elif changed:
        line = f"[{stamp}] Board normalisiert (Formatierung)"
    else:
        line = f"[{stamp}] keine Aenderung (offen: {sum(todo_open(c) for c in META)}/{len(META)})"
    print(line)
    write = bool(events or changed) or (not dry and not logged_today(today))
    if write and not dry:
        with LOG.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
