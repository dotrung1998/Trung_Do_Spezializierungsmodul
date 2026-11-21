---
titel: Datenquellen
stand: 2026-11-21
---

# Datenquellen

Alles öffentlich, kein Login. Für das Datenblatt (`data/DATASHEET.md`) werden
Abrufdatum, Umfang und bekannte Lücken je Quelle festgehalten.

## Ordnungen (PDF, verbindlich)

**Spezielle Ordnung M.Sc. Data Analytics** — Mitteilungen der JLU, 7.36.07 Nr. 11.
Übersichtsseite mit allen Fassungen:
<https://www.uni-giessen.de/de/mug/7/findex36.html/7_36_07_11>

| Fassung | Geltung (laut Übersichtsseite) | Dateikennung |
|---|---|---|
| **3. Änderung — aktuelle Fassung** | gilt ab **SoSe 2026** | `7_36_07_11_3ae` |
| 2. Änderung | in Kraft 04.12.2024, gültig ab SoSe 2025 | `7_36_07_11_2ae` |
| 1. Änderung | in Kraft 01.12.2023 | `7_36_07_11_1ae` |
| Urfassung | in Kraft 18.05.2023 | `7_36_07_11_2023` |

**Verbindlich für die eigene Arbeit ist die 3. Änderungsfassung**, weil sie ab dem
Sommersemester 2026 gilt und damit im WiSe 2026/27 die geltende Fassung ist:
<https://www.uni-giessen.de/de/mug/7/pdf/7_36/07/7_36_07_11/7_36_07_11_3ae>

**Zitierweise.** Die Fassung im Text nennen, nicht nur das Jahr: „Spezielle Ordnung für
den Masterstudiengang Data Analytics, Fassung des 3. Änderungsbeschlusses, Mitteilungen
der JLU 7.36.07 Nr. 11, gültig ab SoSe 2026“. Ein bloßes „(JLU 2023)“ ist falsch, weil es
vier Fassungen mit vier Geltungszeiträumen gibt.

**Beobachtung für die Arbeit.** Die Übersichtsseite nennt für die 1. Änderung „in Kraft
01.12.2023, gültig ab WiSe 2023/24“, die Titelseite derselben PDF „gilt ab dem
Wintersemester 2024/25“. Zwei Primärquellen derselben Einrichtung widersprechen sich im
Geltungsbeginn — ein echtes Beispiel für die Versionsartefakte, die 3.1 messbar machen
soll. Vor dem Zitat also die Fassung benennen, nicht nur ein Datum.

**Achtung bei Verlinkung.** Die PDF-Adressen enden auf `..._3ae` (3. Änderung), `..._2ae`,
`..._1ae` und `..._2023` (Urfassung). Wer die `1ae`-Adresse aus einer Suchmaschine
übernimmt, zitiert die falsche Fassung — genau dieser Fehler war in einer früheren
Fassung dieser Notiz enthalten.

**Allgemeine Bestimmungen für Bachelor- und Masterstudiengänge (AllB)** — 7.34.00 Nr. 1,
3. Änderungsfassung, gültig ab SoSe 2025:
<https://www.uni-giessen.de/de/mug/7/pdf/7_34/7_34_00_1_3ae/@@download/file/7_34_00_1_3_%C3%84nderungsfassung2025.pdf>
Die AllB ist die Quelle der Rahmenregeln (Fristen, Rücktritt, Wiederholung); die
Spezielle Ordnung verweist darauf. Deshalb ist sie für 3.1 wichtig: dieselbe Frist steht
an zwei Stellen, einmal allgemein und einmal speziell.

## Studiengangsseiten

**Studienangebot M.Sc. Data Analytics:**
<https://www.uni-giessen.de/de/studium/studienangebot/master/data-analytics/index>
Enthält Bewerbung, Zulassung, Fristen, Links zu Ordnungen und Vorlesungsverzeichnis.
Hohe Änderungsrate erwartet (Fristen, Termine).

**Studienführer Data Science / Data Analytics (PDF, Zentrale Studienberatung):**
<https://www.uni-giessen.de/de/studium/dateien/bachelor-master/data-studienfuehrer>
Redaktionsschluss im Dokument vermerkt (z. B. „Dezember 2024") — ein Musterfall für
„Dokument mit Datum, das älter ist als der Stichtag".

## Fachbereich 07

**Fachbereich 07 — Mathematik und Informatik, Physik und Geographie:**
<https://www.uni-giessen.de/fbz/fb07>
Einstiegsseite für 3.3 (Klickpfade) und Quelle für Studiengangs- und
Prüfungsamt-Informationen.

## Frühere Fassungen (für 3.1 und 3.2)

**Wayback Machine, CDX-API** (Liste aller Snapshots einer URL):
```
https://web.archive.org/cdx/search/cdx?url=uni-giessen.de/...&output=json&from=2023&to=2026
```
Wofür: Seitenfassungen zu datierbaren Zeitpunkten, ohne selbst zu crawlen.
Einschränkung: lückenhaft, manche Seiten nie archiviert, JS-Inhalte fehlen oft.

**HTTP-Header** `Last-Modified` — billig, aber unzuverlässig (viele Server liefern
Deploy-Zeit statt Inhaltszeit). Im Bericht als „Proxy" kennzeichnen, nicht als Wahrheit.

## Internationalisierung (nur für 3.5)

- Zentrale JLU-Seiten mit englischer Fassung, `hreflang`-Paare.
- Internationalisierungsstrategie der JLU — `Status: zu prüfen`, genaue Quelle noch nicht
  verifiziert. Vor Zitat im Bericht beschaffen.

## Arbeitsumgebung

- **GitLab der JLU:** <https://gitlab.ub.uni-giessen.de>
  Öffentliche Seiten erreichbar; **SSH nur im Uninetz oder per VPN**, sonst HTTPS mit
  persönlichem Token. 50 Projekte à 1 GB je Person, Git LFS für große Dateien.
- **Repo-Name der eigenen Arbeit** nach Leitfaden: `gamma-3-1-konsistenz`.

## Höflichkeitsregeln beim Abruf (Vorgabe aus den Steckbriefen)

- `robots.txt` beachten.
- Rate begrenzen (z. B. eine Anfrage pro Sekunde, sequenziell).
- Klarer User-Agent mit Kontakt.
- Keine Massenabrufe, keine Umgehung von Sperren.
- Die Webredaktion wird **vorab von der Betreuung informiert**; für 3.2 heißt das: den
  Statuscheck ankündigen, nicht überraschen.

## Was fehlt und im Datenblatt stehen muss

- Seiten hinter Login (StudIP, Prüfungsverwaltung) — nicht erfasst, nicht erfasst werden.
- PDFs ohne Textebene (Scan) — nur mit OCR, Aufwand begründen oder ausschließen.
- Englische Fassungen — nur für 3.5 systematisch.
- Dynamisch geladene Inhalte — je nach Abrufmethode unsichtbar; im Bericht benennen.

## Bezug

[[Team Gamma – gemeinsame Grundlage]] · [[Methodik]] · [[3.1 Konsistenz]]
