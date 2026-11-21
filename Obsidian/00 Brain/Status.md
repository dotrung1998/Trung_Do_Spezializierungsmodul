---
titel: Status
stand: 2026-11-21
---

# Status

## Fristen

Bezugsdatum: Sa 21.11.2026. Tage in Klammern ab Bezugsdatum.

| Wann | Was | Tage | Erledigt |
|---|---|---|---|
| sofort | Einmal im JLU-GitLab anmelden, HRZ-Kennung per Mail an die Betreuung | — | ☐ |
| Do 26.11.2026 | Zwei Themenwünsche (P1, P2) per Mail an die Betreuung | 5 | ☐ |
| vor Di 01.12.2026 | Prüfungsleistung mitteilen: **Bericht 10–15 S. + Code, kein Vortrag** | 10 | ☐ |
| Fr 27.11.2026, 11:00 | Zuteilung der Einzelarbeiten + erster Jour fixe (online, selber Raum) | 6 | ☐ |
| Di 01.12.2026 | Offizieller Start | 10 | — |
| KW 1–2 / Januar | Grober Projektplan + Meilensteingespräch (Termin folgt) | — | ☐ |
| Do 01.04.2027 | Abgabe im Abgaberepo der Betreuung | 131 | ☐ |

## Nächste Aktion

**Heute:** [[E-Mail 1 – Themenwünsche]] ausfüllen (Name, Matrikelnummer, HRZ-Kennung)
und senden. Danach GitLab-Anmeldung, falls noch nicht geschehen — die Kennung steht in
derselben Mail.

**Danach (nach der Zuteilung am 27.11.):** [[E-Mail 2 – Kurzexposé]] mit `expose.pdf`
senden. Zwei Platzhalter ausfüllen (zugeteilte Arbeit, Datum des Jour fixe), Rest ist
versandfertig. Vorlage: `E-Mail-2-versandfertig.txt` im Projektordner.

## E-Mail 2 — layoutgeprüft und versandfertig (21.11.2026)

- **Dateien:** `E-Mail-2-versandfertig.txt` (Projektordner) + `report/expose.pdf` (genau 1 Seite).
- **Geprüft:** Seite als Bild gerendert (150 dpi) und gelesen; Text zusätzlich über
  `pdftotext -bbox` auf Positionen geprüft. Inhalt innerhalb der Ränder, keine
  Überlappungen, keine abgeschnittenen Zeilen, Tabelle P1–P6 vollständig, Umlaute und
  deutsche Anführungszeichen korrekt, Abschnitte in der Reihenfolge
  Fragestellung → Daten → Methode → Zeitplan. Build: 0 Warnungen, 0 Overfull,
  0 Missing character, 1 Seite.
- **Verbleibende Platzhalter:** `[Datum]` und `[3.1 Konsistenz über Quellen]`.
- **Sperrdatum:** **nicht vor Fr 27.11.2026, 11:00** senden — erst nach der Zuteilung im
  Jour fixe. Anhang `expose.pdf` nicht vergessen.

## Repository (21.11.2026)

- **GitHub privat:** `dotrung1998/Trung_Do_Spezializierungsmodul`, Branch `main`,
  erster Commit `aa763b2` (119 Dateien: Vault, `report/` mit beiden PDFs, Mail-Entwürfe,
  `AGENTS.md`).
- **Commit-Regel** in `AGENTS.md` festgehalten: **keine Bot-Attribution** — keine
  `Co-Authored-By`-Zeile, kein „Generated with …“, keine Trailer. Gilt für jede Sitzung.
- **Seitenprüfung:** alle 12 Seiten von `main.pdf` am 21.11. als Bild gerendert und
  gelesen. Zwei stille Fehler gefunden und behoben: ß wurde als „SS“ gesetzt
  (XeTeX/T1, jetzt über `newunicodechar` auf `\ss{}` umgebogen) und in Anhang A.1 fehlte
  ein Leerzeichen („Änderungsrate,Quellen“). Danach 0 Overfull, 0 Missing character,
  12 Seiten.

## Stand der Arbeitspakete

| Paket | Stand | Notiz |
|---|---|---|
| Themenwahl | Empfehlung fertig, Entscheidung offen | [[Vergleich und Empfehlung]] |
| Literatur | am 21.11. gegen Primärquellen geprüft; 3.1/3.2 vollständig belegt, 3.5-Quelle offen | [[Literatur]] |
| Methodik | Messdesign entworfen | [[Methodik]] |
| Datenquellen | Adressen und Fassungen erfasst | [[Datenquellen]] |
| Hypothesen | drei Kandidaten, falsifizierbar | [[Hypothesen 3.1]] |
| Projektplan | 17-Wochen-Raster | [[Projektplan]] |
| GitLab-Repo | noch nicht angelegt | [[Prüfungsleistung ohne Vortrag]] |
| Kommunikation | E-Mail 1 versandfertig; **E-Mail 2 inkl. Exposé layoutgeprüft und versandfertig** (2 Platzhalter, Sperrdatum 27.11.) | [[Kommunikationsplan]] · [[E-Mail 2 – Kurzexposé]] |
| Satz | `report/` baut mit tectonic: Bericht 12 Seiten, Exposé 1 Seite | [[LaTeX-Bericht]] |

## Was in dieser Woche zählt

1. Mail raus (Frist 26.11. ist hart, danach entscheidet die Zuteilung ohne die eigene Stimme).
2. GitLab-Zugang real testen, nicht nur „sollte gehen" — SSH nur im Uninetz oder per VPN,
   sonst HTTPS mit persönlichem Token.
3. Nichts weiter bauen. Vor der Zuteilung ist jede Codezeile Spekulation.
