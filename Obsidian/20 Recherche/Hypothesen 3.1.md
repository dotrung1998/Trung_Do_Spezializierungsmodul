---
titel: Hypothesen 3.1
stand: 2026-11-21
---

# Hypothesen 3.1

Die Vorgabe ist: eigene Hypothesen aus der Literatur ableiten und **mit der Betreuung
abstimmen**, bevor die Arbeit beginnt. Hier drei Kandidaten, falsifizierbar formuliert.
Nach der Abstimmung bleiben ein bis zwei davon übrig — nicht alle drei.

## H1 — Abweichungen konzentrieren sich auf instabile Sachverhaltstypen

> Abweichungen zwischen den Quellen treten überwiegend bei Sachverhaltstypen mit hoher
> Änderungsrate auf (Fristen, Termine, Ansprechpartner). Bei stabilen Typen
> (Leistungspunkte, Modulnummern, Regelstudienzeit) ist die Abweichungsrate nahe null.

**Begründung aus der Literatur.** Seiten ändern sich unterschiedlich schnell, und die
Änderungsrate hängt am Inhaltstyp, nicht an der Domain ([[Literatur]]: Cho &
Garcia-Molina; Fetterly et al.). Wenn das stimmt, ist die Verteilung der Abweichungen
über Typen **schief** — und das ist messbar.

**Operationalisierung.** Abweichungsrate je Typ mit Wilson-KI; Vergleich der Raten
zwischen „instabil" und „stabil" (Fishers exakter Test bei kleinem n).

**Was sie widerlegt.** Wenn Abweichungen gleichmäßig über Typen streuen, ist Veraltung
nicht der Mechanismus — dann liegt es an Redaktionsprozessen oder an der Extraktion.
Auch das ein Ergebnis, und ein interessantes.

## H2 — LLM-Extraktion ist präzise, aber nicht vollständig

> Ein sprachmodellgestütztes Verfahren erkennt Abweichungen mit hoher Precision, aber
> begrenztem Recall; die Kombination mit regelbasierter Normalisierung erhöht den Recall
> deutlich, ohne die Precision zu senken.

**Begründung.** LLMs sind gut darin, eine Stelle zu interpretieren, aber schlecht darin,
systematisch alle Stellen zu finden (Recall-Problem, nicht Präzisionsproblem). Die
Literatur zu Claim Detection zeigt genau dieses Muster ([[Literatur]]: FEVER; Judge-Bench
zur Notwendigkeit der Validierung).

**Operationalisierung.** Precision/Recall je Verfahrensvariante (nur LLM / nur Regeln /
Hybrid) gegen denselben Goldstandard. Berichtet wird die Differenz mit Konfidenzintervall.

**Was sie widerlegt.** Wenn der Hybrid den Recall nicht erhöht, war die Normalisierung
nutzlos — dann ist der Bericht kürzer, aber ehrlicher.

## H3 — Die meisten „Widersprüche" sind Zeitartefakte

> Ein großer Teil der gefundenen Abweichungen ist kein echter Widerspruch, sondern die
> Folge unterschiedlicher Fassungen oder Zielgruppen. Echte Widersprüche sind selten,
> aber systematisch bei Fristen zu finden.

**Begründung.** Content Drift ist von Link Rot zu trennen, und die meisten
Inkonsistenzen in gewachsenen Informationsangeboten entstehen durch nicht mitgezogene
Aktualisierungen ([[Literatur]]: Jones et al. 2016; Klein et al. 2014). Zusätzlich
existiert die Spezielle Ordnung in mehreren Änderungsfassungen — der Mechanismus ist
also im Korpus angelegt.

**Operationalisierung.** Typologie der Abweichung (echt / Version / Scope /
Formulierung / Fehler), Anteile je Typ mit KI. Zusätzlich: Abgleich mit dem Datum der
zitierten Fassung.

**Was sie widerlegt.** Wenn die Mehrheit echte Widersprüche sind, ist das der stärkere
Befund — und die Empfehlung an die JLU entsprechend dringlicher.

## Welche Hypothese den Bericht trägt

**H3 ist die interessanteste**, weil sie die Frage verschiebt: von „wie inkonsistent ist
die JLU" zu „welche Art von Inkonsistenz dominiert". Sie ist auch die, die am ehesten
überrascht — und Überraschung ist das, was eine sehr gute Note ausmacht.

**H1 ist die sicherste**, weil die Literatur sie stützt und die Messung einfach ist.
**H2 ist die methodische**, und sie ist Pflicht, wenn ein LLM im Spiel ist: Ohne
Validierung ist die ganze Arbeit angreifbar.

Empfehlung für die Abstimmung: **H3 als Haupthypothese, H1 als Nebenhypothese, H2 als
methodische Absicherung.** Drei Hypothesen sind für 15 Seiten zu viel; zwei tragen.

## Formulierung für die Mail an die Betreuung

Siehe [[E-Mail 2 – Kurzexposé]] — dort stehen die Hypothesen in der Fassung, die man
verschickt: kürzer, ohne Operationalisierung, mit der Bitte um Einschätzung. Die frühere
Hypothesenmail liegt als Vorrat in [[E-Mail 2 – Hypothesen]] (jetzt E-Mail 3).

## Bezug

[[3.1 Konsistenz]] · [[Methodik]] · [[Literatur]]
