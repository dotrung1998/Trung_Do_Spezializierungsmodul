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
- Offen: Themenwünsche, GitLab-Anmeldung + Kennung, Prüfungsvarianten-Erklärung,
  Team-Gamma-Absprache zum gemeinsamen Quellenstand.

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
| [[LaTeX-Bericht]] | Satzordner `report/`: Aufbau, Bauen, Stand |
| [[Person]] · [[Korrespondenz mit Busse]] | Stammdaten und Mailverlauf |
| [[Codekarte]] | automatische Mermaid-Karte des Codes (ab Repo-Anlage) |

## Arbeitsrhythmus

Wöchentlich, freitags: `ingest.py` laufen lassen, `Status.md` fortschreiben, eine
Entscheidung oder ein Befund in `Entscheidungen.md`, ein Commit im GitLab-Repo.
Der Vault ist das Gedächtnis, das GitLab-Repo ist die Abgabe. Beides getrennt halten.
