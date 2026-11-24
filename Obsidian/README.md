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
_tools/          Automatik: ingest.py, graphify.py, board_sync.py, daily.sh,
                 discord_notify.py, author_guard.py, fristen.json, abdeckung-regeln.json
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

## Tageslauf

`_tools/daily.sh` liest die Quellen ein, schreibt die Codekarte, das Board und den
Fristenblock in [[Status]] fort und schickt einen ausführlichen Bericht an Discord:
Lage und Quellen, alle Fristen mit Begründung, offene Karten und Entscheidungen sowie
jede Mail als Codeblock mit Kopierknopf. Der Bericht umfasst mehrere Nachrichten, weil
Discord 2000 Zeichen je Nachricht erlaubt. Geplant läuft er in GitHub Actions
(`.github/workflows/tageslauf.yml`, 08:00 Europe/Berlin); von Hand geht er jederzeit:

```bash
bash Obsidian/_tools/daily.sh
```

Prüfen ohne zu schreiben:

```bash
python3 Obsidian/_tools/ingest.py --check
python3 Obsidian/_tools/board_sync.py --check
python3 Obsidian/_tools/discord_notify.py --dry-run
```

Fristen stehen nur in `_tools/fristen.json` (mit Quelle), Ausschlüsse und manuell
beschriebene Dateien in `_tools/abdeckung-regeln.json`. Der lokale LaunchAgent
(`com.projectjlu.daily.plist`) ist seit 23.11.2026 entladen und deaktiviert; geplant
läuft nur GitHub Actions.

Nach dem Klonen einmalig die Hooks aktivieren:

```bash
git config core.hooksPath .githooks
```
