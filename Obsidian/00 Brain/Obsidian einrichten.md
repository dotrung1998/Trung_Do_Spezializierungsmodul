---
titel: Obsidian einrichten
stand: 2026-11-21
---

# Obsidian einrichten

## Warum keine linke Leiste zu sehen war

Der Vault hatte in `.obsidian/appearance.json` den Wert `"showRibbon": false`. Damit
blendet Obsidian die schmale Icon-Leiste am linken Rand aus — und mit ihr die Knöpfe für
**Graph view**, **Bases**, **Befehlspalette**, **Tägliche Notiz**. Die Plugins waren die
ganze Zeit aktiv (`core-plugins.json` führt `graph: true` und `bases: true`), es fehlte
nur der Zugang.

Gesetzt ist jetzt `"showRibbon": true`.

**Wichtig:** Wenn Obsidian beim Ändern der Datei geöffnet war, überschreibt Obsidian die
Einstellung beim Beenden aus dem Speicher. Dann den Schalter direkt in der App setzen:

> Einstellungen (⌘,) → **Erscheinungsbild** → **Ribbon-Menü anzeigen** einschalten.

Danach Obsidian neu starten (⌘Q, dann öffnen). Die Leiste erscheint links mit den Icons
für Dateien, Suche, Graph, Bases, Befehlspalette.

## Graph öffnen

- Icon **Graph view** in der linken Leiste, oder Befehl „Graph view: Open graph view".
- **Lokaler Graph** (Befehl „Open local graph") zeigt nur die Nachbarschaft der offenen
  Notiz — für die Arbeit meist nützlicher als der globale Graph.
- Farbgruppen: Graph-Ansicht → Zahnrad → **Groups** → z. B. `path:"00 Brain"` rot,
  `path:"10 Thema"` blau, `path:"20 Recherche"` grün. Dann sieht man auf einen Blick,
  welche Bereiche gut vernetzt sind und welche Inseln sind.
- Der Graph liest die Dateien im Vault. Er aktualisiert sich, sobald sich Dateien ändern —
  also automatisch mit jedem Ingest-Lauf.

## Bases

Bases ist ein Kern-Plugin (Obsidian 1.9+), das Notizen wie eine kleine Datenbank
tabellarisch darstellt — Filter, Sortierung, berechnete Spalten, alles auf Basis der
Properties im Frontmatter.

Sinnvolle Bases für diesen Vault:

| Base | Filter | Zweck |
|---|---|---|
| Fristen | `stand` vorhanden, Datei in `00 Brain` | was wann fällig ist |
| Literatur | `path:"20 Recherche"` | Quellen nach Jahr, Typ |
| Entscheidungen | manuell | chronologisches Protokoll |

Anlegen: Befehl „Bases: Create new base" → Datei speichern als
`00 Brain/Fristen.base` → Spalten `datei`, `stand`, `frist` wählen.

Die Frontmatter-Felder sind bereits gesetzt: `titel`, `stand`, `status`, `frist`,
`prioritaet`, `tags`, `quelle`, `hash`, `automatisch`.

## Tägliche Aktualisierung

Zwei Dinge müssen täglich passieren: neue Unterlagen der Betreuung einlesen, und die
Codekarte neu erzeugen.

`_tools/daily.sh` macht beides und schreibt ein Protokoll nach `_tools/daily.log`.
Gestartet wird es von **GitHub Actions** (`.github/workflows/tageslauf.yml`), täglich
08:00 Europe/Berlin — der Rechner muss dafür nicht laufen. Von Hand jederzeit:

```bash
bash Obsidian/_tools/daily.sh
tail -20 "Obsidian/_tools/daily.log"
```

**Lokaler LaunchAgent (seit 23.11.2026 aus).** Bis 22.11.2026 lief `com.projectjlu.daily`
über launchd, seit dem Umzug auf Actions ist er entladen und deaktiviert — sonst gäbe es
zwei Läufe, zwei Discord-Berichte und konkurrierende Commits. Die Datei liegt weiter
unter `~/Library/LaunchAgents/`. Zurückholen nur mit entferntem Workflow-Cron:

```bash
launchctl enable gui/$(id -u)/com.projectjlu.daily
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.projectjlu.daily.plist
```

**Nachteil des Agents:** Er enthält den absoluten Pfad
`/Applications/JLU Spezializierungsmodul`. Wird der Ordner verschoben oder umbenannt,
läuft er ins Leere; dann die plist neu erzeugen (Vorlage:
`_tools/com.projectjlu.daily.plist`).

## Was die Codekarte ist

`10 Thema/Codekarte.md` wird von `_tools/graphify.py` erzeugt: ein Mermaid-Diagramm der
Python-Module und ihrer Importe, plus eine Tabelle mit Zeilen, Klassen, Funktionen und
der Frage, ob ein Docstring existiert.

Warum nicht einfach Code in den Graph legen: Obsidian zeigt Notizen, keine Quelldateien.
Ein Wikilink auf `src/extract/llm.py` wäre ein toter Link. Die Mermaid-Karte rendert
direkt in der Notiz und erscheint als **eine** Node im Graph — lesbar, ohne Müll.

Sobald das Repo `gamma-3-1-konsistenz/` existiert, füllt sich die Karte beim nächsten
Lauf von selbst.

## Bezug

[[Brain]] · [[Status]] · [[Automation und Repo-Muster]] · [[Codekarte]]
