---
titel: Projektplan
stand: 2026-11-21
---

# Projektplan

360 Stunden, 17 Wochen. Das Protokoll rechnet mit **rund 22 Stunden je Woche**; auf die
17 Wochen dieses Plans entfallen 21. Start Di 01.12.2026, Abgabe Do 01.04.2027 (vier
Monate ab Startdatum, so die Vorgabe des Modulrahmens).
Der Plan ist grob — die Vorgabe verlangt einen groben Plan bis Januar, keinen Stundenplan.
Er wird nach dem Meilensteingespräch im Januar einmal überarbeitet.

## Phasen

| Phase | Zeitraum | Wochen | Stunden | Ziel |
|---|---|---|---|---|
| P0 Vorbereitung | 21.11.–30.11.2026 | 1,5 | 10 | Mail, GitLab, Repo, Themenwahl |
| P1 Grundlage | 01.12.–20.12.2026 | 3 | 60 | Literatur, Hypothesen, Korpus, gemeinsame Grundlage |
| — Weihnachtspause | 21.12.2026–03.01.2027 | 2 | 0 | Puffer, Korpus bleibt eingefroren |
| P2 Plan und Prototyp | 04.01.–17.01.2027 | 2 | 40 | Projektplan, Meilensteingespräch, Prototyp |
| P3 Pipeline | 18.01.–14.02.2027 | 4 | 90 | Extraktion, Normalisierung, Vergleich, Goldstandard-Aufbau |
| P4 Evaluation | 15.02.–14.03.2027 | 4 | 80 | Annotation, Metriken, Fehleranalyse |
| P5 Schreiben | 15.03.–28.03.2027 | 2 | 60 | Bericht vollständig |
| P6 Abgabe | 29.03.–01.04.2027 | 0,7 | 20 | Endfassung, Code, Abgabe |

## P0 — Vorbereitung (10 h)

- [ ] Zwei Themenwünsche per Mail an die Betreuung (Frist Do 26.11.) — [[E-Mail 1 – Themenwünsche]]
- [ ] Einmal im GitLab anmelden, HRZ-Kennung in dieselbe Mail
- [ ] Prüfungsleistung mitteilen: Bericht 10–15 S. + Code, kein Vortrag
- [ ] Repo `gamma-3-1-konsistenz` anlegen, privat, Betreuung als **Reporter** einladen
- [ ] Mindeststruktur anlegen (README, docs, data, src, notebooks, tests, .gitignore)
- [ ] Diese Vault-Notizen als erste `docs/`-Einträge übernehmen

**Fertig, wenn** die Mail raus ist, das Repo existiert und die Betreuung eingeladen ist.

## P1 — Grundlage (60 h, 3 Wochen)

- [ ] Literaturrecherche zu Konsistenz/Fact Verification, Informationsqualität, Content Drift
- [ ] Hypothesen formulieren und mit der Betreuung abstimmen ([[Hypothesen 3.1]])
- [ ] Korpus mit dem Team sichern, **ein** Stichtag, Hashes, Datenblatt v1
- [ ] Faktkatalog mit dem Team festlegen (12 Typen, [[Team Gamma – gemeinsame Grundlage]])
- [ ] 10 Dokumente manuell durchsehen: Wo genau sind Abweichungen, wie sehen sie aus?

**Fertig, wenn** zwei Hypothesen abgestimmt sind und der Korpus eingefroren ist.

## P2 — Plan und Prototyp (40 h)

- [ ] Grober Projektplan (dieses Dokument, überarbeitet) ins Repo
- [ ] Meilensteingespräch mit der Betreuung
- [ ] Prototyp auf **drei** Dokumenten: ein Sachverhalt, von Hand bis zur Abweichung
- [ ] Entscheidung: welche LLM-Zugänge, welche Bibliotheken, welche Umgebung

**Fertig, wenn** ein Dokument → ein extrahierter Fakt mit Fundstelle automatisch läuft.

## P3 — Pipeline (90 h)

- [ ] Segmentierung (HTML-Hauptinhalt, PDF-Absätze), Boilerplate entfernen
- [ ] Extraktion mit Schema + Zitatpflicht, Lauf-Protokoll (Prompt-Version, Modell)
- [ ] Normalisierung (Datum, Zahl, Aliasliste) mit Tests
- [ ] Gruppierung (Entität, Attribut) und Vergleich (exakt, Toleranz, NLI)
- [ ] Goldstandard: Stichprobe ziehen, Annotationsleitfaden schreiben, 50 % annotieren

**Fertig, wenn** die Pipeline über den ganzen Korpus läuft und reproduzierbar ist.

## P4 — Evaluation (80 h)

- [ ] Annotation abschließen, Krippendorffs α berechnen
- [ ] Precision/Recall/F1 je Sachverhaltstyp, Wilson-Konfidenzintervalle
- [ ] Abweichungstypologie anwenden, Anteile je Typ
- [ ] Fehleranalyse: 20–30 Fälle kategorisieren
- [ ] Alle Tabellen und Abbildungen erzeugen (Skript, nicht Handarbeit)

**Fertig, wenn** jede Zahl im Bericht aus einem Skript kommt.

## P5 — Schreiben (60 h)

- [ ] Gliederung mit der Betreuung abstimmen ([[Prüfungsleistung ohne Vortrag]])
- [ ] Erste Vollfassung
- [ ] Zwei Durchgänge: Argument (trägt jeder Absatz?) und Sprache
- [ ] Literaturverzeichnis vollständig, jede Angabe geprüft

**Fertig, wenn** die Fassung vollständig ist und jemand anderes sie versteht.

## P6 — Abgabe (20 h)

- [ ] PDF erzeugen, Seitenzahl prüfen (10–15 **ohne** Anhang)
- [ ] Code lauffähig aus frischem Klon, `make reproduce` getestet
- [ ] Ordner mit Repo-Namen im Abgaberepo, alles hinein (Leitfaden)
- [ ] Letzter Blick: keine Zugangsdaten, keine Rohdaten, keine Namen Dritter

## Wochenrhythmus

| Tag | Was |
|---|---|
| Mo | 30 Min: Was ist diese Woche fertig? Drei Punkte, nicht zehn. |
| täglich | 2–3 h, immer am selben Arbeitspaket |
| Fr | 45 Min: `ingest.py`, Status fortschreiben, ein Commit, eine Notiz |

## Puffer

Eingeplant sind 0 Stunden Puffer in den Phasen, aber zwei Wochen Weihnachtspause und
eine Woche Reserve vor der Abgabe. Wenn eine Phase reißt, wird **der Umfang** gekürzt,
nicht die Sorgfalt: weniger Sachverhaltstypen, gleiche Methode. Ein Bericht über 8 Typen
mit sauberer Evaluation ist besser als einer über 20 Typen ohne.

## Bezug

[[Prüfungsleistung ohne Vortrag]] · [[Risiken und Gegenmaßnahmen]] · [[Status]]
