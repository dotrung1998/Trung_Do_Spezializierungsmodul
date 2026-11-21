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
