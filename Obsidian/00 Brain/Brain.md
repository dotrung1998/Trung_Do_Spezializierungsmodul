---
titel: Brain
stand: 2026-11-21
status: aktiv
---

# Brain — Project JLU

> **Bắt đầu ở đây (VI):** Đọc theo thứ tự [[Status]] → [[Offene Entscheidungen]] →
> [[Vergleich und Empfehlung]]. Ba việc gấp nhất: chọn P1/P2 (đề xuất 3.1 / 3.2),
> gửi mail cho Busse trước **26.11**, đăng nhập GitLab và gửi HRZ-Kennung.

## Worum es geht

Spezialisierungsmodul M.Sc. Data Analytics, WiSe 2026/27. Reserviert ist **Projekt 29**
der SPZ-Plattform: *Project JLU – Informationsqualität. Konsistenz, Aktualität,
Verständlichkeit und Auffindbarkeit der Studieninformationen messen.* Das ist **Team
Gamma** mit fünf Einzelarbeiten (3.1–3.5). Eine davon wird die eigene Arbeit.

Wichtig für die Planung: Projekt 29 ist der Rahmen, nicht die Einzelarbeit. Die
Einzelarbeit entsteht erst durch die Themenwünsche (Priorität 1 und 2) bis Do 26.11.2026
und die Zuteilung am Fr 27.11.2026, 11:00 Uhr.

Gewählte Prüfungsleistung: **kein Vortrag** → Bericht **10–15 Seiten** mit Programmcode
(die Alternative wäre 5–10 Seiten + Vortrag 20–30 Min.). Das ist die Variante mit mehr
Schreib-, aber weniger Redeanteil und passt zum Ziel „höchste Note mit belegter Messung".

## Aktueller Stand

- 03.11.2026: Projekt 29 auf der SPZ-Plattform reserviert.
- 20.11.2026: Kick-off. Rahmen, Fristen und Prüfungsvarianten bekannt ([[2026-11-20 kick-off (Quelle)|Protokoll]]).
- 21.11.2026: Dieses Brain angelegt. Literaturgrundlage für alle fünf Dimensionen
  recherchiert ([[Literatur]]). Empfehlung erarbeitet ([[Vergleich und Empfehlung]]).
- 21.11.2026: Satzordner `report/` angelegt und **bewiesen**: baut mit tectonic 0.17.0
  zu einem 12-seitigen PDF, 0 Fehler, 13/13 Quellen im Literaturverzeichnis. Inhalt ist
  Gerüst — 38 `\todo` stehen noch drin. Details: [[LaTeX-Bericht]].
- 21.11.2026: **Berichtstext, zweiter Durchgang** — 29 von 38 `\todo` geschlossen, 9 bleiben
  (7 Messzahlen, 2 Nutzerentscheidungen A.1/A.3). Neu: A.2 Schema, A.4 Fehlertaxonomie,
  A.5 Code-Verzeichnis, Kapitel 6–8 im Argument. Textteil 13 Seiten, gesamt 22,
  0 Overfull, 0 Missing character. Details: [[Status]] · [[LaTeX-Bericht]].
- 21.11.2026: **[[Board]]** angelegt und zur Kette ausgebaut (To Do / Doing / Done).
  Karten tragen `braucht:`; eine erledigte Karte gibt die abhängige frei, `#ai` läuft
  dann die Folgearbeit (`jobs.py` setzt nur belegte Messwerte ein), `#person` wird nie
  entschieden. Ohne `report/data/ergebnisse.json` bleibt jedes `\todo` stehen. Täglich
  08:00 über `_tools/daily.sh`. Details: [[Status]].
- Offen: Themenwünsche, GitLab-Anmeldung + Kennung, Prüfungsvarianten-Erklärung,
  Team-Gamma-Absprache zum gemeinsamen Quellenstand.

## Board

[[Board]] (`Obsidian/30 Plan/Board.md`) hält alle Aufgaben als To Do · Doing · Done.
Karten tragen `#person`, `#team` oder `#ai` und optional `braucht: <IDs>`; Karten ohne
Abhängigkeit bekommen keine solche Angabe.

**Kette.** KORPUS → GOLD, 6.1, 6.3, 6.4 · GOLD → 6.2 · 6.1 und 6.2 → 7.2 · 7.2 → 8 ·
8 → ZUS.

Der Lauf (`_tools/daily.sh`, 08:00, launchd `com.projectjlu.daily`) ruft `board_sync.py`
und darin `jobs.py`:

- `\todo` offen ⇒ Karte nicht Done; ist die Stelle im Bericht gefüllt, wird die Karte Done.
- `#person` und `#team` werden nie automatisch entschieden, nur als freigegeben oder
  blockiert markiert; `#ai` wandert bei erledigten Blockern von To Do nach Doing.
- Ohne `report/data/ergebnisse.json` bleibt das `\todo` stehen und die Karte trägt
  `· wartet: <Grund>`. Eingesetzt wird nur, was dort als `latex` steht — kein Schätzwert.
- Vom Nutzer nach Doing gezogene Karten bleiben dort; ein Häkchen ohne gefüllte
  Berichtsstelle wird zurückgenommen (`· offen: \todo steht noch`).
- Ohne Änderung schreibt der Lauf keine Vault-Datei (nur höchstens eine Log-Zeile pro Tag).

Stand 21.11.2026: 9 `\todo` offen; alle Messkarten hängen mittelbar an KORPUS. Details: [[Status]].

## Landkarte

| Notiz | Inhalt |
|---|---|
| [[Status]] | Fristen, Tage bis zum Termin, nächste Aktion |
| [[Entscheidungen]] | datiertes Entscheidungsprotokoll inkl. verworfener Alternativen |
| [[Offene Entscheidungen]] | was nur die Person entscheiden kann |
| [[Thema 29 – Überblick]] | Projekt, Team, Ablauf, Prüfungsformen |
| [[Team Gamma – gemeinsame Grundlage]] | was in den ersten drei Wochen gemeinsam entsteht |
| [[Vergleich und Empfehlung]] | Bewertung 3.1–3.5, Empfehlung P1/P2 |
| [[3.1 Konsistenz]] · [[3.2 Aktualität]] · [[3.3 Auffindbarkeit]] · [[3.4 Verständlichkeit]] · [[3.5 Mehrsprachigkeit]] | Arbeitsnotizen je Dimension |
| [[Literatur]] | annotierte Bibliographie mit URL/DOI |
| [[Methodik]] | Messdesign: Einheit, Goldstandard, Metriken, Reproduzierbarkeit |
| [[Datenquellen]] | welche Dokumente, welche Fassungen, welche Adressen |
| [[Hypothesen 3.1]] | Kandidaten-Hypothesen, falsifizierbar formuliert |
| [[Projektplan]] | 17 Wochen, Arbeitspakete, Meilensteine |
| [[Prüfungsleistung ohne Vortrag]] | Seitenbudget, Gliederung, Abgabe |
| [[Risiken und Gegenmaßnahmen]] | was schiefgehen kann und was dann passiert |
| [[Automation und Repo-Muster]] | Stufenmodell, `make`-Ziele, Arbeitsteilung Mensch/Agent |
| [[Kommunikationsplan]] | wer wann was schreibt |
| [[E-Mail 1 – Themenwünsche]] · [[E-Mail 2 – Hypothesen]] · [[E-Mail an Team Gamma]] | Entwürfe |
| [[Obsidian einrichten]] | Ribbon, Bases, Graph, täglicher Lauf |
| [[Board]] | Kanban mit Abhängigkeitskette: erledigte Karte gibt Folgearbeit frei, täglich 08:00 |
| [[LaTeX-Bericht]] | Satzordner `report/`: Aufbau, Bauen, Stand |
| [[Person]] · [[Korrespondenz mit Busse]] | Stammdaten und Mailverlauf |
| [[Codekarte]] | automatische Mermaid-Karte des Codes (ab Repo-Anlage) |

## Arbeitsrhythmus

Wöchentlich, freitags: `ingest.py` laufen lassen, `Status.md` fortschreiben, eine
Entscheidung oder ein Befund in `Entscheidungen.md`, ein Commit im GitLab-Repo.
Der Vault ist das Gedächtnis, das GitLab-Repo ist die Abgabe. Beides getrennt halten.
