---
titel: "1.5 Kurs- und Serviceangebote (HRZ, ZfbK, Bibliothek)"
quelle: "Project JLU/steckbriefe/1-5-kurs-und-serviceangebote.md"
stand: 2026-11-19
hash: b85cc1fd8b9b
automatisch: true
---

> Automatisch eingelesen aus `Project JLU/steckbriefe/1-5-kurs-und-serviceangebote.md` am 2026-11-21.
> Diese Notiz nicht bearbeiten — inhaltliche Arbeit gehört in die
> handgeschriebenen Notizen, diese Datei wird beim nächsten Lauf überschrieben.

<!-- Quelle: Planungsmodul Project JLU WiSe 2026/27, Fassung v3. Stand 19.11.2026. -->
# 1.5 Kurs- und Serviceangebote (HRZ, ZfbK, Bibliothek)

Team Alpha α · JLU-Wissenskorpus · Projektsteckbrief WiSe 2026/27

## Worum es geht

Kurse und Angebote von HRZ, ZfbK und Universitätsbibliothek sind terminierte Einträge mit Datum, Anmeldefrist oder Laufzeit. Bleiben abgelaufene Angebote auf den Seiten stehen, finden Nutzende das Aktuelle schwer, und den Redaktionen fehlt ein Hinweis, was zu pflegen ist.

## Fragestellung

> **Wie lassen sich terminierte Angebote aus Webseiten automatisch extrahieren und abgelaufene oder veraltete Einträge zuverlässig erkennen?**

## Ausrichtung

Am Ende steht ein Werkzeug, das Angebote mit ihren Zeitangaben aus den Seiten extrahiert und veraltete Einträge erkennt. Es kann in zwei Richtungen weisen: als Hinweisgeber für Redaktionen, welche Einträge zu löschen oder anzupassen sind, oder als Filter für Nutzende, der nur aktuelle Angebote zeigt. Dazu gehört eine Auswertung, wie verbreitet veraltete Einträge sind. Was „veraltet“ heißt, legen Sie selbst begründet fest. Verläufe untersuchen Sie rückwirkend an früheren Fassungen der Seiten.

## Datengrundlage

Öffentliche Angebots- und Kursseiten von HRZ, ZfbK und Universitätsbibliothek, dazu frühere Fassungen dieser Seiten, soweit verfügbar.

## Womit Sie anfangen

1. Sichten Sie die Angebotsseiten und notieren Sie, wie Angebote und ihre Zeitangaben aufgebaut sind und woran sich ein veralteter Eintrag erkennen lässt.
2. Recherchieren Sie, wie Zeitangaben und Ereignisse aus Texten extrahiert und wie veraltete Webinhalte erkannt werden.
3. Präzisieren Sie die Fragestellung, leiten Sie eigene Hypothesen ab und stimmen Sie diese mit der Betreuung ab.

Erste Suchbegriffe für die Recherche: `temporal information extraction`, `event extraction web pages`, `stale content detection`

## Im Team

In den ersten drei Wochen verständigt sich das Team auf ein gemeinsames Format für die Dokumente und sichert die Quellen. Danach bearbeitet jede Person ihren Quellentyp unabhängig von den anderen Arbeiten.

**Hilfreich:** Python, Interesse an Informationsextraktion und an Werkzeugen für Redaktionen oder Nutzende.  
**Nicht Teil dieser Arbeit:** Bewertung der Qualität der Angebote, Aktualität der übrigen Studieninformationen ([[3-2-aktualitaet|3.2]]).  
**Zu beachten:** Automatisierte Abrufe erfolgen schonend und nach den Regeln der Seiten. Die Webredaktion der JLU wird vorab von der Betreuung informiert.

---

Vorgegeben ist das Ziel. Hypothesen, Methoden, Werkzeuge und Vorgehen entwickeln und begründen Sie selbst. Eigene Ideen für die Ausrichtung sind willkommen, solange sie zur Gesamtvision passen. Übersicht und Ablauf: [[Thema 29 – Überblick|Zur Startseite]]
