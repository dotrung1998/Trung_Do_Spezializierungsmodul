# AGENTS.md — Project JLU (Spezialisierungsmodul, Thema 29 / Team Gamma)

Dieses Repository ist Arbeits- **und** Gedächtnisort für ein Spezialisierungsmodul
(M.Sc. Data Analytics, JLU Gießen, WiSe 2026/27, 12 CP, 360 h, 01.12.2026–01.04.2027).
Betreuung: Dr. Sebastian Busse, sebastian.busse@admin.uni-giessen.de.

## Zuerst lesen

1. `Obsidian/00 Brain/Brain.md` — Einstieg, aktueller Stand, was als Nächstes ansteht.
2. `Obsidian/00 Brain/Status.md` — Fristen und nächste Aktionen.
3. `Obsidian/00 Brain/Offene Entscheidungen.md` — was nur die Person entscheiden kann.

## Ordner

| Pfad                    | Rolle                                                                    |
|-------------------------|--------------------------------------------------------------------------|
| `Project JLU/`          | **Quelle.** Material der Betreuung (Steckbriefe, Protokolle, Leitfaden).  |
| `Obsidian/`             | **Gedächtnis.** Vault mit Brain, Thema, Recherche, Plan, Kommunikation.   |
| `Obsidian/_tools/`      | **Automatik.** ingest, graphify, board_sync, daily, discord_notify.        |
| `Reservierung_Thema_29.txt` | Reservierungsbestätigung der SPZ-Plattform.                          |

`Project JLU/` ist unverändert zu lassen. Es wird in den Vault **eingelesen**, nicht
bearbeitet. Ausnahme: nichts. Auch Tippfehler in den Quellen bleiben stehen.

## Pflichtschritte am Anfang jeder Sitzung

```bash
python3 Obsidian/_tools/ingest.py          # neue/geänderte Quellen einlesen
cat "Obsidian/00 Brain/Neu seit letztem Lauf.md"
```

Danach `Brain.md` und `Status.md` lesen und erst dann arbeiten.

## Pflichtschritte am Ende jeder Sitzung, in der etwas passiert ist

1. `Obsidian/00 Brain/Status.md` — Fristen, nächste Aktion, Stand je Arbeitspaket.
2. `Obsidian/00 Brain/Entscheidungen.md` — **jede** Entscheidung mit Datum, Grund und
   verworfener Alternative anhängen. Nie rückwirkend umschreiben, nur ergänzen.
3. Wenn neue Literatur gelesen wurde: `Obsidian/20 Recherche/Literatur.md` ergänzen —
   vollständige Angabe, URL/DOI, ein Satz „wofür im Bericht", ein Satz Einschränkung.
4. Wenn die Betreuung etwas Neues geschickt hat: Quelle nach `Project JLU/` legen,
   `ingest.py` laufen lassen, betroffene Notizen aktualisieren, Änderung im
   `Ingest Log` steht automatisch.
5. `Obsidian/00 Brain/Brain.md` — nur den Abschnitt „Aktueller Stand" fortschreiben.

## Harte Regeln

- **Keine erfundenen Quellen.** Jede Angabe in `Literatur.md` braucht URL oder DOI.
  Ungeprüftes wird als `Status: zu prüfen` markiert, nicht als Tatsache geschrieben.
- **Keine Zahlen ohne Quelle.** Aussagen wie „40 % der Seiten sind veraltet" nur mit
  Belegstelle; sonst als offene Messung formulieren.
- **Trennung von Befund und Meinung.** Empfehlungen stehen in `Entscheidungen.md` /
  `Vergleich und Empfehlung.md`, nicht in den Steckbrief-Notizen.
- **Personenbezug:** Befunde beziehen sich auf Seiten und Dokumente, nie auf Personen
  oder Organisationseinheiten als Bewertungsobjekt (Vorgabe aus Steckbrief 3.1/3.2).
- **Keine Zugangsdaten, Tokens oder Matrikelnummern** in den Vault schreiben.
  Platzhalter wie `[HRZ-Kennung]` bleiben Platzhalter.
- **Sprache:** Vault-Inhalte auf Deutsch (direkt in den Bericht übernehmbar).
  Chat-Antworten an die Person auf Vietnamesisch, mit deutschen Fachbegriffen.
- Der Bericht wird **nicht** im Vault geschrieben, sondern im GitLab-Repo der Arbeit.
  Der Vault liefert Argumente, Quellen und Gliederung.

## Wenn die Person eine neue Datei der Betreuung herunterlädt

Die Datei kommt in `Project JLU/` (gleiche Unterordnerlogik: `protokolle/`,
`steckbriefe/`). Danach `ingest.py`. Der Vault macht daraus eine Notiz mit
Frontmatter (`quelle`, `stand`, `hash`) und trägt die Änderung ins `Ingest Log` ein.
Inhaltliche Auswirkung bewerten: neue Frist? geänderte Fragestellung? neue Vorgabe
zur Prüfungsleistung? → `Status.md` und `Entscheidungen.md` fortschreiben.

## Automatik

Ein Ablauf, zwei Startpunkte.

**GitHub (der geplante Lauf):** `.github/workflows/tageslauf.yml`, täglich 08:00
Europe/Berlin (`schedule` mit `timezone`), zusätzlich per `workflow_dispatch` startbar.
Der Workflow ruft `Obsidian/_tools/daily.sh`, committet das Ergebnis als „Trung Do“,
prüft den eigenen Commit mit `author_guard.py` und pusht auf `main` zurück.

**Mac (von Hand oder optional):** derselbe `daily.sh`. Für Dauerbetrieb liegen
`_tools/com.projectjlu.daily.plist` und `daily_guard.sh` bei — **nicht installiert**.
Zwei Scheduler am selben Tag erzeugen zwei Discord-Berichte und konkurrierende Commits.
Wer den Agent lädt, entfernt vorher den Cron im Workflow.

Ablauf je Lauf: `ingest.py` (Quellen), `graphify.py` (Codekarte), `board_sync.py`
(Board, Fristenblock), `discord_notify.py` (Bericht). Exit ≠ 0, wenn ein Kernschritt
scheitert oder eine Quelle `unbekannt` bleibt.

Der Lauf schreibt ausschließlich:

- `…(Quelle).md`, `90 Anhänge/`, `30 Plan/Abgaben (auto).md`
- `00 Brain/Ingest Log.md`, `00 Brain/Neu seit letztem Lauf.md`
- den Block `<!-- AUTO:START --> … <!-- AUTO:END -->` in `Status.md`
- Statusvermerke am Zeilenende der Board-Karten und `_tools/abdeckung.json`

Handgeschriebene Notizen werden nie überschrieben. Ohne Änderung schreibt der Lauf
nichts; ein zweiter Lauf am selben Tag ist identisch.

### Prüfen, ohne zu schreiben

```bash
python3 Obsidian/_tools/ingest.py --check
python3 Obsidian/_tools/board_sync.py --check
python3 Obsidian/_tools/author_guard.py --config
python3 Obsidian/_tools/discord_notify.py --dry-run
```

### Fristen und Abdeckung

`Obsidian/_tools/fristen.json` ist die **einzige** Stelle mit Datumsangaben; jeder
Eintrag trägt `quelle`. Eine neue Frist nur mit Beleg in `Project JLU/` oder in einer
Notiz eintragen, sonst gar nicht. `abdeckung-regeln.json` begründet, warum eine Quelle
keine Notiz bekommt; fehlt der Grund, bleibt sie `unbekannt` und der Lauf schlägt fehl.

### Hooks und Secret

`core.hooksPath` ist lokale Konfiguration und wird nicht committet. Nach dem Klonen:

```bash
git config core.hooksPath .githooks
```

`pre-commit` und `commit-msg` prüfen jeden Commit, `pre-push` jeden Push gegen
`author_guard.py` — ein erlaubter Autor, keine Trailer, keine Bot-Namen. Derselbe Prüfer
läuft in `.github/workflows/author-guard.yml`.

Der Discord-Webhook liegt als Repository-Secret `DISCORD_WEBHOOK` und lokal unter
`~/.config/projektjlu/discord-webhook` (Rückfall `~/.config/projektplanung/discord-webhook`).
Er steht nie im Repo, nie im Vault, nie im Log.

## Git und Commits

- Remote: `https://github.com/dotrung1998/Trung_Do_Spezializierungsmodul.git`
  (**privat**). Daneben bleibt das JLU-GitLab der Ort für die Abgabe.
- **Keine Bot- oder Werkzeug-Attribution in Commits.** Keine `Co-Authored-By:`-Zeile,
  kein „Generated with …", keine Trailer, die ein Modell oder Werkzeug als Mitautor
  nennen. Die Commit-Message endet mit ihrem letzten inhaltlichen Satz. Das gilt für
  jede Sitzung und jedes Werkzeug — die Person hat es ausdrücklich so verlangt.
- Commit-Messages auf Deutsch: eine Zeile Zusammenfassung, darunter Stichpunkte.
- Push nur, wenn die Person es verlangt. Vor dem Push `git status` prüfen: keine
  Zugangsdaten, keine Build-Artefakte, keine temporären Renderordner.
