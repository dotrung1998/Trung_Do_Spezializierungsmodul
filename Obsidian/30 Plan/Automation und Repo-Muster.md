---
titel: Automation und Repo-Muster
stand: 2026-11-21
---

# Automation und Repo-Muster

Vorbild ist das Kursrepo `jamwithai/production-agentic-rag-course`
(<https://github.com/jamwithai/production-agentic-rag-course>). Dessen Muster ist nicht
die Technik, sondern die **Disziplin**: jede Woche ein lauffähiger Stand, ein README als
einziger Einstieg, ein Befehl für den Gesundheitscheck, Tests, Releases als Meilensteine.
Übertragen auf eine Forschungsarbeit heißt das: jede Phase endet in einem Zustand, den
jemand anderes in fünf Minuten prüfen kann.

## Übertragung

| Muster im Kursrepo | Übertragung hier |
|---|---|
| Wochenabschnitte mit „What You'll Build" | Phasen P0–P6 mit Done-Kriterium ([[Projektplan]]) |
| Release-Tags `week1.0` … `week7.0` | Git-Tags `stage0` … `stage6`, je ein lauffähiger Stand |
| `make start / health / test / stop` | `make corpus / extract / eval / check / report` |
| `/health`-Endpunkt | `make check`: Tests grün, Korpus-Hash unverändert, Bericht baubar |
| `notebooks/weekN/` | `notebooks/01_exploration`, `02_extraktion`, `03_evaluation` |
| `tests/` | Tests für Normalisierung, Schema-Validierung, Gruppierung |
| `.env.example`, keine Secrets | `.env` in `.gitignore`, Konfiguration über Umgebungsvariablen |
| Airflow-DAG für den Datenabruf | ein `make corpus` plus optionaler Cron für den Statuscheck |
| Langfuse-Tracing | `runs/*.jsonl`: jeder LLM-Aufruf mit Prompt-Version, Modell, Tokens, Output |

Das Letzte ist der wichtigste Import: **ein Lauf-Protokoll für LLM-Aufrufe**. Ohne das ist
eine LLM-gestützte Messung nicht reproduzierbar, und Reproduzierbarkeit ist im Modul
Teil der Note.

## Verzeichnis

```
gamma-3-1-konsistenz/
├── README.md            Fragestellung, 3 Befehle bis zum Ergebnis, Stand, Grenzen
├── Makefile             corpus, extract, normalize, eval, report, check
├── docs/                Projektplan, datierte Entscheidungen, Annotationsleitfaden
├── data/
│   ├── DATASHEET.md     Quellen, Abrufdatum, Umfang, Lücken
│   ├── raw/             nicht im Repo (.gitignore)
│   └── processed/       kleine Ergebnisse, im Repo
├── src/
│   ├── corpus/          Abruf, Snapshot, Hash
│   ├── extract/         Schema, Prompts, LLM-Aufruf, Lauf-Protokoll
│   ├── normalize/       Datum, Zahl, Aliasse
│   └── compare/         Gruppierung, Vergleich, Typologie
├── notebooks/           Exploration
├── tests/               Normalisierung, Schema
├── runs/                jsonl-Protokolle (klein, im Repo)
└── requirements.txt
```

## Arbeitsteilung Mensch / Agent

Der Agent (Freebuff) macht die Arbeit, die viel Zeit und wenig Urteil braucht. Die Person
entscheidet, was zählt.

| Aufgabe | Wer | Warum |
|---|---|---|
| Literatur suchen, zusammenfassen, Zitate prüfen | Agent | zeitintensiv, gut prüfbar |
| Code: Abruf, Segmentierung, Normalisierung, Vergleich | Agent | Handwerk |
| Prompts und Schema entwerfen, iterieren | Agent | schnell, messbar |
| Extraktion über den ganzen Korpus fahren | Agent | Mengenarbeit |
| Tabellen und Abbildungen aus Ergebnissen erzeugen | Agent | reine Umsetzung |
| Berichtsentwurf aus Gliederung und Ergebnissen | Agent | Rohfassung, danach Handarbeit |
| **Hypothesen festlegen** | Person | wissenschaftliches Urteil |
| **Goldstandard annotieren** | Person | muss menschlich sein, sonst wertlos |
| **Interpretation und Grenzen** | Person | das ist die Note |
| **Mails an die Betreuung** | Person | Ton und Verbindlichkeit |
| **Letzte Fassung lesen** | Person | Verantwortung |

Merksatz: **Der Agent liefert Zahlen, die Person liefert Bedeutung.** Eine Arbeit, in der
niemand die Zahlen selbst angefasst hat, ist nicht verteidigbar — und ohne Vortrag fällt
das sofort auf.

## Modellwahl

- **Starkes Modell** (Mission Max o. ä.) für: Planung, Methodenentscheidungen,
  Berichtstext, Fehleranalyse, alles mit Urteil.
- **Schnelles Modell** (DeepSeek Flash o. ä.) für: Massenextraktion, Klassifikation,
  Umformulierung, Übersetzung — Aufgaben mit festem Schema und prüfbarer Ausgabe.
- **Gar kein Modell** für: Datumsvergleich, Zahlenvergleich, Aliasabgleich, Zählungen.
  Wer für `2027-01-15 < 2027-01-31` ein Sprachmodell aufruft, macht die Arbeit teurer,
  langsamer und unzuverlässiger.

Diese Regel in den Bericht: „Wir setzen Sprachmodelle nur dort ein, wo die Aufgabe
sprachliches Verstehen verlangt" ist ein Qualitätsmerkmal, kein Eingeständnis.

## Wochenroutine (45 Minuten, freitags)

1. `python3 Obsidian/_tools/ingest.py` — neue Unterlagen der Betreuung einlesen.
2. `00 Brain/Neu seit letztem Lauf.md` lesen.
3. `Status.md`: eine Zeile je Arbeitspaket.
4. `Entscheidungen.md`: was diese Woche entschieden wurde, mit Grund.
5. Ein Commit im GitLab-Repo, Tag setzen, wenn eine Phase endet.

## Was **nicht** automatisiert wird

- Die Annotationsentscheidung im Goldstandard.
- Die Formulierung der Hypothesen.
- Die Kommunikation mit der Betreuung.
- Die Entscheidung, was weggelassen wird, wenn die Zeit knapp wird.

## Bezug

[[Projektplan]] · [[Prüfungsleistung ohne Vortrag]] · [[Methodik]]
