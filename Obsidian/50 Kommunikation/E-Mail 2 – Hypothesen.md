---
titel: E-Mail 3 – Hypothesen (Vorrat)
stand: 2026-11-21
frist: 2026-12-18
status: Vorrat — nur senden, wenn das Kurzexposé die Hypothesen nicht beantwortet
---

# E-Mail 3 — Hypothesen abstimmen

> **Verschoben.** Diese Mail ist nicht mehr E-Mail 2. Zuerst geht das
> [[E-Mail 2 – Kurzexposé]] an die Betreuung; es enthält H1 und H2 bereits. Diese
> Fassung bleibt als Vorrat liegen, falls die Rückmeldung die Hypothesen offen lässt.

**An:** sebastian.busse@admin.uni-giessen.de
**Zeitpunkt:** nach der Zuteilung (27.11.), sinnvoll Mitte Dezember, vor der Weihnachtspause
**Zweck:** Die Vorgabe verlangt, die Hypothesen mit der Betreuung abzustimmen. Diese Mail
erledigt das schriftlich und schafft eine prüfbare Grundlage für den Januar.

Platzhalter: `[Nummer der zugeteilten Arbeit]`, `[ggf. anpassen]`.

---

**Betreff:** Hypothesen zu meiner Einzelarbeit ([Nummer]), Abstimmung vor der Weihnachtspause

Sehr geehrter Herr Dr. Busse,

seit der Zuteilung arbeite ich an [Nummer]. Ich habe die Literatur gesichtet und zwei
Hypothesen abgeleitet. Bevor ich den Korpus und die Pipeline darauf zuschneide, würde ich
sie gern mit Ihnen abstimmen.

**Ausgangsbeobachtung.** Dieselben Sachverhalte stehen in Ordnungen, Informationsblättern
und Webseiten mehrfach. Die Spezielle Ordnung des M.Sc. Data Analytics liegt zudem in
mehreren Änderungsfassungen vor. Es ist daher zu erwarten, dass ein Teil der Abweichungen
zwischen Quellen keine echten Widersprüche sind, sondern Folgen unterschiedlicher
Fassungen oder Zielgruppen.

**H1 (Haupthypothese).** Ein großer Teil der gefundenen Abweichungen ist kein echter
Widerspruch, sondern Folge unterschiedlicher Fassungen oder Zielgruppen. Echte
Widersprüche sind seltener, treten aber systematisch bei Fristen auf.

**H2 (methodisch).** Ein sprachmodellgestütztes Verfahren erkennt Abweichungen mit hoher
Präzision, aber begrenztem Recall; die Kombination mit regelbasierter Normalisierung
erhöht den Recall, ohne die Präzision zu senken.

**Vorgehen.** Ich definiere einen Sachverhalt als Tupel aus Entität, Attribut, Wert,
Gültigkeitsintervall und Fundstelle und baue einen Katalog von rund zwölf
Sachverhaltstypen. Die Extraktion erfolgt mit einem Sprachmodell, jeder Wert muss eine
Fundstelle mitliefern. Geprüft wird an einem eigenen Goldstandard; die Übereinstimmung
zwischen Modell und menschlicher Annotation berichte ich als Krippendorffs α. Für H1
ordne ich jede Abweichung einem Typ zu (echter Widerspruch, Versionsartefakt,
Scope-Unterschied, Formulierung, Extraktionsfehler).

**Zwei Fragen.**

1. Ist die Aufteilung in eine inhaltliche und eine methodische Hypothese so sinnvoll,
   oder würden Sie beide in einer Frage bündeln?
2. Ist ein Katalog von zwölf Sachverhaltstypen für den Umfang angemessen, oder raten Sie
   zu einer engeren Auswahl?

Für den Januar plane ich den groben Projektplan und einen Prototyp auf drei Dokumenten.
Falls Sie dafür einen Termin vorsehen, richte ich mich gern danach.

Vielen Dank und freundliche Grüße
[Vorname Nachname]

---

## Warum diese Fassung

- **Ausgangsbeobachtung vor den Hypothesen.** Die Betreuung sieht, woher die Vermutung
  kommt — nicht nur, was behauptet wird.
- **Zwei Hypothesen, nicht vier.** Wer fünf Hypothesen vorlegt, bekommt keine
  Rückmeldung, sondern eine Vorlesung.
- **Das Vorgehen in fünf Sätzen.** Genug, um zu erkennen, dass die Person weiß, was ein
  Goldstandard ist, ohne das Methodenkapitel vorwegzunehmen.
- **Genau zwei Fragen**, beide mit Alternative. Das lässt sich in zwei Zeilen beantworten.

## Nach der Antwort

Die abgestimmte Fassung nach `docs/` im GitLab-Repo übernehmen und in
[[Hypothesen 3.1]] als „abgestimmt am …" markieren. Der Eintrag in
[[Entscheidungen]] hält fest, was sich durch das Feedback geändert hat.

## Bezug

[[Hypothesen 3.1]] · [[Kommunikationsplan]] · [[Methodik]]
