#!/usr/bin/env python3
"""Folgearbeit fuer freigegebene #ai-Karten.

Der Lauf erfindet nichts. Er setzt ausschliesslich ein, was eine Messung
tatsaechlich geliefert hat: `report/data/ergebnisse.json` mit einem Eintrag
je Karte.

    {"6.1": {"datei": "chapters/06_ergebnisse.tex",
             "latex": "... fertiger LaTeX-Block ...",
             "summary": "12,5 % (95-%-Intervall 8,1--16,9; n = 64)"}}

Fehlt die Datei, fehlt der Eintrag, fehlt der Anker im Text oder ist der
LaTeX-Block unbrauchbar, bleibt das \\todo stehen und der Grund wird
zurueckgegeben. Es gibt keinen Schatzwert und keinen Platzhalter.
"""

import json
import pathlib

TEX_IDS = {"6.1", "6.2", "6.3", "6.4", "7.2", "8", "ZUS"}


def find_todo(text, anchor):
    """Spannt das \\todo{...} auf, das mit `anchor` beginnt. Brace-balanciert."""
    i = text.find(anchor)
    if i < 0:
        return None
    # Der Anker beginnt selbst mit \todo{; erst pruefen, dann suchen.
    # (rfind mit Fensterende i+1 kann an i nicht matchen und liefert sonst
    #  den vorherigen Block.)
    if text.startswith("\\todo{", i):
        start = i
    else:
        start = text.rfind("\\todo{", 0, i)
    if start < 0:
        return None
    depth = 0
    for j in range(start + 5, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return start, j + 1
    return None


def run(card_id, anchor, report_dir):
    """Fuehrt die Folgearbeit aus. Rueckgabe: (ok, meldung)."""
    if card_id not in TEX_IDS:
        return False, "keine Folgearbeit hinterlegt"

    data_file = report_dir / "data" / "ergebnisse.json"
    if not data_file.exists():
        return False, "keine Messdaten: report/data/ergebnisse.json fehlt"
    try:
        data = json.loads(data_file.read_text(encoding="utf-8"))
    except (OSError, ValueError) as err:
        return False, f"Messdaten unlesbar: {err}"

    entry = data.get(card_id)
    if not isinstance(entry, dict):
        return False, f"kein Ergebnis fuer {card_id} in ergebnisse.json"
    latex = str(entry.get("latex") or "").strip()
    summary = str(entry.get("summary") or "").strip()
    if not latex:
        return False, "Ergebnis ohne LaTeX-Block"
    if "\\todo" in latex:
        return False, "Ergebnis enthaelt selbst ein \\todo"
    if latex.count("{") != latex.count("}"):
        return False, "LaTeX-Block mit unbalancierten Klammern"
    if not summary:
        return False, "Ergebnis ohne Zusammenfassung (summary)"

    rel = entry.get("datei")
    if not rel:
        return False, "Ergebnis ohne Angabe der Zieldatei (datei)"
    path = report_dir / rel
    if not path.exists():
        return False, f"Zieldatei fehlt: {rel}"

    text = path.read_text(encoding="utf-8")
    span = find_todo(text, anchor)
    if span is None:
        return False, "Anker im Text nicht gefunden (\\todo bereits ersetzt?)"

    start, end = span
    path.write_text(text[:start] + latex + text[end:], encoding="utf-8")
    return True, f"eingesetzt in {rel}: {summary}"
