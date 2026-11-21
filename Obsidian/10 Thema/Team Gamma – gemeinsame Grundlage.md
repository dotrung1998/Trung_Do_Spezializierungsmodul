---
titel: Team Gamma – gemeinsame Grundlage
stand: 2026-11-21
tags: [team, gamma]
---

# Team Gamma — gemeinsame Grundlage

Vorgabe aus dem Steckbrief: In den ersten drei Wochen sichert das Team **einen
gemeinsamen Stand der Quellen** und legt fest, **welche Sachverhalte** es untersucht,
damit alle auf derselben Grundlage messen. Danach arbeitet jede Person unabhängig.

Diese drei Wochen entscheiden über die Vergleichbarkeit aller fünf Arbeiten. Wer hier
schnell ist, prägt die Grundlage — und senkt den eigenen Aufwand später erheblich.

## Vorschlag: drei Artefakte, ein Repo

Ein gemeinsames Repo `team-gamma` (eine Person legt es an, lädt Team und Betreuung ein).

### 1. `korpus/` — eingefrorener Quellenstand

- HTML-Snapshots der FB07- und Studiengangsseiten, PDFs der Ordnungen und
  Informationsblätter, jeweils mit Abrufdatum und SHA256.
- **Ein** Datum für alle. Sonst messen fünf Leute fünf verschiedene Welten und keine
  Zahl ist vergleichbar.
- Keine Rohdaten im Repo (Leitfaden): Hashes und Abrufskript im Repo, Daten daneben.

### 2. `sachverhalte.md` — der Faktkatalog

Die Liste der untersuchten Sachverhalte, mit Typ, erwarteter Quelle und erwarteter
Stabilität. Das ist das eigentliche gemeinsame Gut: 3.1 zählt Abweichungen je Typ,
3.2 sagt Veraltung je Typ vorher, 3.3 misst Wege zu diesen Typen, 3.4 vergleicht Texte,
in denen sie stehen.

Vorschlag für 12 Typen (bewusst klein, bewusst heterogen):

| # | Sachverhaltstyp | Beispiel | Erwartete Änderungsrate |
|---|---|---|---|
| 1 | Bewerbungsfrist | „15.01." / „01.06." | hoch |
| 2 | Immatrikulationsfrist | Frist zur Einschreibung | hoch |
| 3 | Leistungspunkte eines Moduls | „6 LP" | sehr niedrig |
| 4 | Modulnummer | „M-DA-01" | sehr niedrig |
| 5 | Prüfungsform | „Klausur 90 Min." | niedrig |
| 6 | Teilnahmevoraussetzung | „Modul X bestanden" | niedrig |
| 7 | Sprachnachweis | „DSH-2 / IELTS 6.5" | niedrig |
| 8 | Ansprechpartner / Zuständigkeit | Name, Sprechstunde | mittel |
| 9 | Raum / Ort | „Raum 024" | mittel |
| 10 | Gebühr / Entgelt | Semesterbeitrag, Kursgebühr | mittel |
| 11 | Regelstudienzeit | „4 Semester" | sehr niedrig |
| 12 | Termin eines Angebots | Kursdatum | hoch |

Der Kontrast zwischen „sehr niedrig" (3, 4, 11) und „hoch" (1, 2, 12) ist der Kern
der späteren Auswertung: Abweichungen sollten sich auf die instabilen Typen
konzentrieren. Wenn nicht, ist das ein interessanterer Befund als die Bestätigung.

### 3. `datenblatt.md` — was im Korpus ist und was fehlt

Quellen, Abrufdatum, Umfang, Aufbau, bekannte Lücken (Leitfaden verlangt
`data/DATASHEET.md`). Diese Datei ist später die halbe Antwort auf „Reproduzierbarkeit".

## Arbeitsteilung, die allen nützt

| Wer | Beitrag in den ersten drei Wochen |
|---|---|
| 3.1 | Faktkatalog (Sachverhalte, Attribute, Normalform) |
| 3.2 | Korpus-Harvesting + Zeitstempel, Link-Inventar |
| 3.3 | Crawl-Graph, Einstiegsseiten |
| 3.4 | Textsegmente, Satzgrenzen, Textsorte-Labels |
| 3.5 | DE/EN-Paare, hreflang |

Auch wer 3.4 oder 3.5 bearbeitet, profitiert vom Faktkatalog: Ohne definierte
Sachverhalte ist „Verständlichkeit" nur ein Gefühl und „Auffindbarkeit" nur ein Klicktest.

## Was schiefgehen kann

- **Fünf Korpusse.** Dann ist keine Querschnittsaussage möglich und der Bericht verliert
  den Teambezug. Gegenmittel: ein Datum, ein Hash, eine Datenblatt-Datei.
- **Faktkatalog zu groß.** 40 Sachverhalte schafft niemand sauber. Zwölf reichen, wenn
  die Auswahl begründet ist.
- **Team zerfällt nach der Zuteilung.** Normal und vorgesehen. Der gemeinsame Stand ist
  die Versicherung, nicht die Dauerbeziehung.

## Bezug

[[Thema 29 – Überblick]] · [[Datenquellen]] · Entwurf der Team-Mail: [[E-Mail an Team Gamma]]
