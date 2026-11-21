---
titel: E-Mail 2 – Kurzexposé
stand: 2026-11-21
zeitpunkt: nach der Zuteilung (ab 27.11.2026), vor dem Schreiben von Kapitel 5–6
status: Entwurf, versandfertig bis auf zwei Platzhalter
---

# E-Mail 2 — Kurzexposé

**An:** sebastian.busse@admin.uni-giessen.de
**Anhang:** `expose.pdf`, genau eine Seite (Quelle: `report/expose.tex`, Bauen mit
`cd report && ./build.sh expose`)
**Zweck:** schriftliche Bestätigung der Richtung, **bevor** Kapitel 5 (Methode) und
Kapitel 6 (Ergebnisse) geschrieben werden. Kein Termin nötig, eine kurze Antwort genügt.
**Versandfertig:** `E-Mail-2-versandfertig.txt` im Projektordner (außerhalb des Vaults).
Die Datei enthält **nur** die zwei Platzhalter im Fließtext — kein Hinweisblock, damit
nichts Falsches mitgesendet wird. `[Datum]` und `[3.1 Konsistenz über Quellen]` ersetzen,
`expose.pdf` anhängen, senden.

## Vor dem Senden ausfüllen

| Platzhalter | Womit ersetzen |
|---|---|
| `[3.1 Konsistenz über Quellen]` | die tatsächlich zugeteilte Arbeit (3.1 oder 3.2) |
| `[Datum]` | Datum des Jour fixe, in dem zugeteilt wurde |

Bei Zuteilung von **3.2** statt 3.1: Exposé auf Aktualität umstellen (Fragestellung,
H1/H2, Daten — der Korpus bleibt derselbe), nicht nur das Wort austauschen.

---

**Betreff:** Kurzexposé zu meiner Einzelarbeit, Projekt 29 (Team Gamma) — The Trung Do, [Matrikelnummer]

Sehr geehrter Herr Dr. Busse,

vielen Dank für die Zuteilung am [Datum]. Ich arbeite seitdem an [3.1 Konsistenz über Quellen].

Bevor ich Kapitel 5 (Methode) und 6 (Ergebnisse) schreibe, lege ich Ihnen den Aufbau auf
einer Seite vor — als Anlage, damit Sie sich dafür nicht durch den halbfertigen Bericht
arbeiten müssen. Das Exposé enthält die Fragestellung mit zwei Hypothesen, den geplanten
Datenzuschnitt, das Evaluationsverfahren und den Zeitplan bis zur Abgabe am 1. April 2027.

Drei Punkte, bei denen Ihre Einschätzung den weiteren Aufwand stark beeinflusst:

1. Trägt die Aufteilung in eine inhaltliche Hypothese (H1) und eine methodische (H2),
   oder würden Sie beide bündeln?
2. Ist ein Faktkatalog von rund zwölf Sachverhaltstypen für 10 bis 15 Seiten angemessen,
   oder raten Sie zu einer engeren Auswahl?
3. Genügt als Goldstandard ein Durchgang von mir plus ein zweiter Durchgang mit einem
   anderen Modell und manueller Konfliktlösung — oder soll ich eine zweite Person
   einbeziehen?

Wenn Ihnen ein kurzes Gespräch lieber ist als Mail, richte ich mich nach Ihrem Termin,
auch kurzfristig. Sonst genügt mir eine kurze Rückmeldung zu den drei Punkten.

Vielen Dank und freundliche Grüße
The Trung Do

---

## Der Inhalt der Anlage (eine Seite)

> Maßgeblich ist `report/expose.pdf`. Hier steht derselbe Text als Gedächtnis, damit die
> Argumente auch ohne PDF auffindbar bleiben. Änderungen immer in `report/expose.tex`
> vornehmen und von dort neu bauen — nicht hier.

**Kurzexposé — Konsistenz über Quellen**
Abweichungen zwischen Studieninformationen automatisch finden und bewerten.
The Trung Do · M.Sc. Data Analytics, Matrikelnummer [Matrikelnummer] · Projekt 29 (Team Gamma) ·
Betreuung Dr. Sebastian Busse · Stand 21.11.2026 · Arbeitstitel ·
Prüfungsleistung: Bericht 10–15 Seiten mit Programmcode, ohne Vortrag.

**Fragestellung.** Dieselben Sachverhalte — Fristen, Leistungspunkte, Modulnummern,
Ansprechpartner — stehen an mehreren Stellen: Spezielle Ordnung, Allgemeine Bestimmungen,
Studiengangsseite, Studienführer, Fachbereichsseite. Ob sie übereinstimmen, ist offen.
*Leitfrage:* Welche Sachverhalte werden in mehreren Quellen unterschiedlich dargestellt,
und wie zuverlässig lässt sich das automatisch finden?
*H1 (inhaltlich):* Ein großer Teil der Abweichungen ist kein echter Widerspruch, sondern
Folge unterschiedlicher Fassungen oder Zielgruppen; echte Widersprüche sind seltener,
treten aber systematisch bei Fristen auf.
*H2 (methodisch):* Sprachmodellgestützte Extraktion erreicht hohe Precision bei begrenztem
Recall; regelbasierte Normalisierung erhöht den Recall, ohne die Precision zu senken.

**Daten.** Öffentliche Quellen, ein Stichtag, ein Hash je Dokument, ein Datenblatt mit
Umfang und Lücken. Spezielle Ordnung (3. Änderungsbeschluss, gültig ab SoSe 2026) und die
drei früheren Fassungen; Allgemeine Bestimmungen (3. Änderungsfassung); Studiengangsseite,
Studienführer, Fachbereichsseite; für datierbare Fassungen die Wayback Machine (CDX-API).
Nicht erfasst: Login-Bereiche, Scans ohne Textebene, dynamische Inhalte. Korpus und
Faktkatalog (rund zwölf Typen) mit Team Gamma bis Mitte Dezember.

**Methode.** Sachverhalt als Tupel aus Entität, Attribut, Wert, Gültigkeitsintervall,
Quelle und Fundstelle. Extraktion mit Zitatpflicht — Werte ohne Belegstelle werden
verworfen. Normalisierung von Datum (ISO 8601), Zahl, Einheit, Entitätsalias, Zielgruppe.
Typologie: echter Widerspruch, Versionsartefakt, Scope-Unterschied, Formulierung,
Extraktionsfehler. Evaluation: stratifizierte Stichprobe, Goldstandard mit zwei
Durchgängen, Krippendorffs α; Precision, Recall und F1 je Sachverhaltstyp mit
Wilson-Konfidenzintervall; Übereinstimmung Modell/Mensch vor dem Lauf über den vollen
Korpus; Fehleranalyse über 20–30 Fälle.

**Zeitplan.** P1 Grundlage 01.12.–20.12.2026 · P2 Plan und Prototyp 04.01.–17.01.2027 ·
P3 Pipeline 18.01.–14.02.2027 · P4 Evaluation 15.02.–14.03.2027 · P5 Schreiben
15.03.–28.03.2027 · P6 Abgabe 29.03.–01.04.2027. Weihnachtspause 21.12.2026–03.01.2027,
Korpus eingefroren.

---

## Verlauf

| Feld | Wert |
|---|---|
| Gesendet am | **[Datum eintragen]** |
| Uhrzeit | [optional] |
| Anhang | `expose.pdf` (1 Seite) |
| Antwort am | **[Datum eintragen]** |
| Status | **noch nicht gesendet** |

### Antwort der Betreuung

> **[Antwort hier einfügen — Datum, Absender, vollständiger Text]**

### Was daraus folgt

- [ ] Antwort zu Frage 1 (H1/H2 bündeln?) → [[Hypothesen 3.1]] und Kapitel 3
- [ ] Antwort zu Frage 2 (Faktkatalog zwölf Typen?) → Kapitel 4, Faktkatalog
- [ ] Antwort zu Frage 3 (Goldstandard ohne zweite Person?) → [[Methodik]], Kapitel 5
- [ ] Falls Freigabe: Kapitel 5 und 6 schreiben, `\todo` dort ersetzen
- [ ] Falls Änderungswunsch: Exposé anpassen, neu bauen, Antwort kurz bestätigen

## Warum diese Fassung

- **Die Mail bittet um Bestätigung, nicht um Mitarbeit.** Drei Fragen, jede mit
  Alternative — das ist in zwei Minuten beantwortet, auch von jemandem mit 15 Arbeiten.
- **Das Exposé steht in der Anlage, nicht im Mailtext.** Eine Seite PDF wird gelesen;
  vier Bildschirme Mailtext werden überflogen.
- **Kein Terminwunsch im Vordergrund.** Ein Gespräch wird angeboten, aber nicht verlangt;
  das Meilensteingespräch im Januar bleibt der Ort für alles Größere.
- **Die Formulierung „bevor ich Kapitel 5 und 6 schreibe“** macht aus der Mail eine
  prüfbare Zäsur: Wenn später jemand fragt, warum die Methode so aussieht, gibt es eine
  schriftliche Freigabe.

## Bezug

[[Korrespondenz mit Busse]] · [[Kommunikationsplan]] · [[Hypothesen 3.1]] · [[Methodik]] ·
[[Projektplan]] · [[LaTeX-Bericht]]
