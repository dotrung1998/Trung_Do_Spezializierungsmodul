---
titel: Prüfungsleistung ohne Vortrag
stand: 2026-11-21
---

# Prüfungsleistung ohne Vortrag

## Was gewählt ist

Aus dem Protokoll des Kick-offs: Zur Wahl stehen

- **A:** Bericht **10–15 Seiten** mit Programmcode — *gewählt*
- B: Bericht 5–10 Seiten mit Programmcode **und** Vortrag 20–30 Min.

Variante A muss **vor dem offiziellen Start (Di 01.12.2026)** mitgeteilt werden. Sie steht
in [[E-Mail 1 – Themenwünsche]].

## Konsequenz der Wahl

Es gibt keine mündliche Gelegenheit, eine Unschärfe zu erklären. Der Bericht muss allein
tragen:

- jede Zahl mit Bezugsgröße und Unsicherheit,
- jede methodische Entscheidung mit Begründung und verworfener Alternative,
- jede Einschränkung ausdrücklich, nicht im Kleingedruckten.

Das ist ein Vorteil, wenn es gut gemacht ist: Ein Bericht, der seine eigene Schwäche
benennt, wirkt souveräner als ein Vortrag, der sie überspielt.

## Seitenbudget (Ziel: 13 Seiten ohne Literatur und Anhang)

| Abschnitt | Seiten | Inhalt |
|---|---|---|
| 1 Einleitung | 1,5 | Problem, Relevanz, Beitrag, Aufbau |
| 2 Hintergrund und verwandte Arbeiten | 2,5 | Informationsqualität (ISO 25012, Wang & Strong), Widerspruchserkennung, Content Drift, Abgrenzung zu 2.2/2.4 |
| 3 Forschungsfrage und Hypothesen | 1 | Fragestellung, H1–H3, was als Widerlegung gilt |
| 4 Daten und Korpus | 1,5 | Quellen, Faktkatalog, Stichtag, Ausschlüsse, Höflichkeitsregeln |
| 5 Methode | 3 | Pipeline, Zitatpflicht, Normalisierung, Abweichungstypologie, Goldstandard, Metriken |
| 6 Ergebnisse | 3 | Abweichungsraten je Typ mit KI, Verfahrensvergleich, Fehleranalyse, zwei Beispiele |
| 7 Diskussion | 1,5 | Interpretation, Hypothesenprüfung, Grenzen, Anschluss an Team Beta |
| 8 Fazit | 0,5 | Drei Sätze, keine Wiederholung |

**Anhang** (zählt nicht als Seiten): Faktkatalog, Extraktionsschema, Prompt-Version,
Fehlertaxonomie, Abbildungsverzeichnis, Code-Verzeichnis.

Vor dem Schreiben klären: Zählt das Literaturverzeichnis in die 10–15 Seiten? Annahme:
nein. Steht als Frage in der Mail — eine Zeile, die später Zeit spart.

## Was den Unterschied zwischen „gut" und „sehr gut" macht

1. **Die Typologie der Abweichung.** Sie ist der eigene Beitrag. Ohne sie ist die Arbeit
   eine Zählung; mit ihr ist sie eine Erklärung.
2. **Ehrliche Fehlerzahlen.** Precision 0,62 bei Ansprechpartnern zu berichten und zu
   erklären, warum, ist stärker als ein geschöntes 0,9.
3. **Ein prüfbarer Satz als Ergebnis.** Nicht „die Informationsqualität ist verbesserungs-
   würdig", sondern: „Von 41 gefundenen Abweichungen sind 9 echte Widersprüche; 8 davon
   betreffen Fristen; 24 sind Versionsartefakte."
4. **Reproduzierbarkeit.** Ein frischer Klon, drei Befehle, dieselben Zahlen.

## Satz

Der Bericht wird in LaTeX gesetzt, im Ordner `report/` des Projektordners. Gerüst,
Seitenbudget je Kapitel und Bauanleitung: [[LaTeX-Bericht]].

## Code

- Öffentlich lesbar, privat bis zur Veröffentlichung (Vereinbarung zur Weiterverwendung
  kommt noch, Lizenz CC mit Namensnennung — Formular abwarten).
- README mit: Fragestellung (ein Satz), Installation, ein Befehl bis zum Ergebnis,
  Stand, bekannte Grenzen.
- Tests für die Normalisierung (Datumsformate, Zahlen, Aliasse) — dort entstehen die
  stillen Fehler.
- Keine Zugangsdaten, keine Rohdaten, kein `.env` im Repo.

## Abgabe (nach Leitfaden)

1. Die Betreuung legt ein Abgaberepo an; kurz vor dem Stichtag gibt es Schreibrechte.
2. Ordner mit dem Namen des eigenen Repos anlegen: `gamma-3-1-konsistenz/`.
3. Hinein: Bericht als PDF, Stand von Code und Daten, mit dem die Ergebnisse entstanden.
4. Stichtag Do 01.04.2027. Danach enden die Schreibrechte. Abgegeben ist, was im
   Abgaberepo liegt.

## Checkliste eine Woche vor Abgabe

- [ ] Seitenzahl im Limit, Anhang getrennt gezählt
- [ ] Jede Zahl im Text auch in einer Tabelle oder Abbildung auffindbar
- [ ] Jede Quelle im Verzeichnis, jede Verzeichnisangabe im Text
- [ ] Frischer Klon getestet
- [ ] Datenblatt aktuell (Abrufdatum, Hashes, Lücken)
- [ ] Keine personenbezogenen Daten, keine Tokens
