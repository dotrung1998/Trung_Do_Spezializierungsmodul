---
titel: "1.3 Bewerbung, Zulassung, Sprachnachweise"
quelle: "Project JLU/steckbriefe/1-3-bewerbung-zulassung.md"
stand: 2026-11-19
hash: 872dcc46815b
automatisch: true
---

> Automatisch eingelesen aus `Project JLU/steckbriefe/1-3-bewerbung-zulassung.md` am 2026-11-23. Nicht bearbeiten —
> inhaltliche Arbeit gehört in die handgeschriebenen Notizen.

<!-- Quelle: Planungsmodul Project JLU WiSe 2026/27, Fassung v3. Stand 19.11.2026. -->
# 1.3 Bewerbung, Zulassung, Sprachnachweise

Team Alpha α · JLU-Wissenskorpus · Projektsteckbrief WiSe 2026/27

## Worum es geht

Informationen zu Bewerbung und Zulassung bestehen aus bedingten Regeln: Wer braucht welchen Nachweis bis wann, und welche Ausnahmen gibt es? Diese Bedingungen stehen in Fließtext und FAQ, nicht in Tabellen, und sind deshalb schwer maschinell zu erfassen.

## Fragestellung

> **Wie lassen sich bedingte Regeln (wer braucht welchen Nachweis bis wann) aus Fließtext- und FAQ-Seiten strukturiert erfassen?**

## Ausrichtung

Im Mittelpunkt steht der Vergleich unterschiedlicher Ansätze der Extraktion, zum Beispiel eines sprachmodellgestützten und eines regelbasierten. Am Ende steht eine begründete Aussage, welcher Ansatz Regeln vollständiger und welcher sie genauer erfasst und wo typische Fehler entstehen. Ein naheliegender Kandidat ist auch das RAG-System der JLU: Wie gut lassen sich damit Informationen zu Bewerbung, Zulassung und Sprachnachweisen gewinnen?

## Datengrundlage

Bewerbungs- und Zulassungsseiten des M.Sc. Data Analytics, zentrale Seiten der JLU zu Bewerbung und Sprachnachweisen, FAQ.

## Womit Sie anfangen

1. Sammeln Sie Beispiele bedingter Regeln und überlegen Sie, aus welchen Bestandteilen eine solche Regel besteht.
2. Recherchieren Sie, wie Informationen mit Sprachmodellen und mit regelbasierten Verfahren aus Texten extrahiert und wie solche Verfahren evaluiert werden.
3. Präzisieren Sie die Fragestellung, leiten Sie eigene Hypothesen ab und stimmen Sie diese mit der Betreuung ab.

Erste Suchbegriffe für die Recherche: `information extraction from regulatory text`, `LLM structured output`, `rule-based information extraction`

## Im Team

In den ersten drei Wochen verständigt sich das Team auf ein gemeinsames Format für die Dokumente und sichert die Quellen. Danach bearbeitet jede Person ihren Quellentyp unabhängig von den anderen Arbeiten.

**Hilfreich:** Python, Interesse an Sprachmodellen und ihrer Evaluation, Informationsextraktion.  
**Nicht Teil dieser Arbeit:** Beratung zu Einzelfällen, Abgleich der Angaben über verschiedene Quellen ([[3-1-konsistenz|3.1]]).  
**Zu beachten:** Für die Arbeit mit einem Sprachmodell wird ein Zugang über die JLU geklärt. Ob und wie das RAG-System der JLU genutzt werden kann, klärt die Betreuung.

---

Vorgegeben ist das Ziel. Hypothesen, Methoden, Werkzeuge und Vorgehen entwickeln und begründen Sie selbst. Eigene Ideen für die Ausrichtung sind willkommen, solange sie zur Gesamtvision passen. Übersicht und Ablauf: [[Thema 29 – Überblick|Zur Startseite]]
