# Obsidian-Vault: Project JLU

Dieser Ordner **ist** der Vault. Öffnen mit Obsidian → „Ordner als Vault öffnen" →
`Obsidian/` auswählen. Keine Plugins nötig, alles ist reines Markdown mit Wikilinks.

## Aufbau

```
00 Brain/        Einstieg, Status, Entscheidungen, offene Entscheidungen, Ingest-Log
10 Thema/        Thema 29, Team Gamma, die fünf Einzelarbeiten, Vergleich + Empfehlung
10 Thema/Steckbriefe/    automatisch eingelesene Steckbriefe der Betreuung
20 Recherche/    Literatur, Methodik, Datenquellen, Hypothesen
30 Plan/         Projektplan, Prüfungsleistung ohne Vortrag, Risiken, Automation
40 Protokolle/   automatisch eingelesene Protokolle der Gesamtgruppe
50 Kommunikation/ E-Mail-Entwürfe und Kommunikationsplan
_tools/          ingest.py — liest Project JLU/ in den Vault ein
90 Anhänge/      automatisch kopierte PDFs und Binärdateien (zu lesen, nicht durchsuchbar)
```

## Einstieg

[[Brain]] → [[Status]] → [[Offene Entscheidungen]]

## Wenn die Betreuung neue Unterlagen schickt

1. Datei nach `Project JLU/` legen (Unterordner `protokolle/` bzw. `steckbriefe/`).
2. Im Projektordner ausführen:

```bash
python3 Obsidian/_tools/ingest.py
```

3. `00 Brain/Neu seit letztem Lauf.md` lesen — dort steht, was neu oder geändert ist.
4. Betroffene Notizen in `00 Brain/` fortschreiben.

Der Ingest überschreibt **nur** `10 Thema/Steckbriefe/`, `40 Protokolle/` und
`90 Anhänge/`. Alle handgeschriebenen Notizen bleiben unberührt.
