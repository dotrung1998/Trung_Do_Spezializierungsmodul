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

## Quellenprüfung (21.11.2026)

Alle 13 im Bericht zitierten Einträge wurden am Original geöffnet (ACL Anthology, ACM, PLOS,
Taylor & Francis, ISO, arXiv, Sage) und gegen den Satz geprüft, an dem sie hängen. Metadaten
waren bis auf fehlende DOIs korrekt. Zwei inhaltliche Fehlzuschreibungen sind korrigiert:

- **Pielka u. a. 2022** belegte nicht, was im Text stand; das Zitat folgt jetzt dem Abstract
  (sprachliche Phänomene, an denen Widerspruchsmodelle scheitern), der Eintrag ist auf die
  arXiv-Fassung umgestellt, erfundene Seitenzahlen sind entfernt.
- **Cho & Garcia-Molina 2000** stand für Änderungsraten nach Domain und Seitentyp; das ist
  Fetterly u. a. 2003. Cho & Garcia-Molina liefern jetzt die Refresh-Policy.

Ergänzt: DOIs für Thorne, Bowman, Conneau, Wang & Strong; FEVER-Band (Vol. 1, Long Papers);
Literaturverzeichnis wieder vollständig auf einer Seite (`\small`-Versuche verworfen,
stattdessen Einträge entrümpelt). Details: [[Literatur#Prüfprotokoll 21.11.2026 — alle 13 zitierten Einträge am Original]].

## Berichtstext (21.11.2026, zweiter Durchgang)

Der Textteil ist auf **13 Seiten** geschrieben (Budget 10–15 ohne Anhang). Von den
ursprünglich 38 `\todo`-Lücken sind **29 geschlossen**; **9 bleiben**, jede einzeln begründet:

| Lücke | warum offen |
|---|---|
| 6.1 | Abweichungsrate je Typ mit Wilson-Intervall — entscheidet, ob das Profil steil oder flach ist (H1) |
| 6.2 | Precision/Recall/F1 je Verfahrensvariante und Recall-Differenz (H2) |
| 6.3 | Häufigkeit je Fehlerklasse aus A.4 — zeigt den Engpass des Verfahrens |
| 6.4 (Fall 2) | Versionsartefakt aus dem klassifizierten Fundbestand des eingefrorenen Korpus; ein von Hand gewählter Fall würde die Methode umgehen |
| 7.2 | Urteil je Hypothese, gebunden an die entscheidende Zahl aus Kapitel 6 |
| 8 | die eine Zahl mit Intervall, die man sich merken soll |
| Zusammenfassung | dieselbe Zahl in einem Satz |
| A.1 | **Nutzerentscheidung**: Festlegung der zwölf Faktentypen mit dem Team |
| A.3 | **Nutzerentscheidung**: Modell, Prompt-Version, Umgebung, Datum |

Sieben Lücken sind damit messzahlgebunden, zwei sind Entscheidungsbedarf. Jede Messzahl-Lücke
ist im Quelltext mit „Fehlt: …" eröffnet und sagt, was die fehlende Zahl zeigen wird.

In diesem Durchgang neu geschrieben: Kapitel 6 (Auswertungslogik je Abschnitt und ein
vollständig belegter Fall — der Geltungsbeginn der 1. Änderungsfassung, mit der
Prüfregel-Kette aus 5.4), Kapitel 7.1 (vier Interpretationsmuster mit ihren Folgen),
7.2 (Folgen je Hypothese, Urteil offen), Kapitel 8 (zwei Absätze), Zusammenfassung (vier
von fünf Bausteinen), **A.2 Extraktionsschema** (16 Felder, Pflichtfelder, Validierung,
Bezug zu 5.1 und 5.3), **A.4 Fehlertaxonomie** (fünf Klassen mit Folge für Precision/
Recall, Abgrenzung zur Abweichungstypologie), **A.5 Code-Verzeichnis** (nur real
vorhandene Dateien: `build.sh`, `main.tex`, `literatur.bib`, `preamble/`, `frontmatter/`,
`chapters/`, `backmatter/`, `figures/`, `tables/`, `expose.tex`, `README.md`,
`.gitignore`; ausdrücklich vermerkt, dass Korpus-, Code- und Testverzeichnisse noch fehlen).

**Keine neue Quelle.** Der gesamte Text steht auf den 13 am 21.11. geprüften Einträgen;
die Reserve-Einträge in `literatur.bib` bleiben unbenutzt. Das Korpus-Beispiel wurde an
der Übersichtsseite 7.36.07 Nr. 11 und der PDF-Titelseite selbst nachgelesen.

Bau: **22 Seiten gesamt, 13 Textseiten**, 0 Overfull, 0 Missing character, 0 undefined,
Literaturverzeichnis 13/13 auf einer Seite.

**URL-Umbruch gelöst (21.11.2026).** Die beiden ISO-Einträge trennten die Adresse nach
`https:`. Ursache war nicht url.sty oder hyperref (beide brechen korrekt nach `/`), sondern
die Feldformatierung von biblatex, die die URL mitten in der Zeile setzt. Lösung in
`preamble/packages.tex` nach dem Laden von biblatex:
`\DeclareFieldFormat{url}{URL\addcolon\space\mbox{\url{#1}}}`. Die Adresse ist damit
unteilbar; passt sie nicht mehr in die Zeile, rutscht sie geschlossen in die nächste. Label
bewusst als normales `URL` statt `\mkbibacro` — sonst standen die beiden Einträge einmal in
Kapitälchen und einmal in Normalbuchstaben. Geprüft am gerenderten PDF (200 dpi): beide
Adressen stehen vollständig, 0 Overfull. Nebenbefund: `\UrlBreaks`/`\UrlBigBreaks` und ein
eigenes `\biburlsetup` wirken nicht, weil biblatex sie pro Eintrag neu setzt.

## Board und Tageslauf — Kette (21.11.2026)

Board: [[Board]] (`Obsidian/30 Plan/Board.md`), Spalten **To Do · Doing · Done**.
Karten tragen `#person`, `#team` oder `#ai` und optional `braucht: <IDs>`; Karten ohne
Abhängigkeit bekommen keine solche Angabe. Jede Karte verweist am Zeilenende mit
`→ [[…]]` auf die Notiz, in der die Arbeit liegt.

**Kette.** Jede erledigte Karte gibt frei, was von ihr abhängt:

| Karte | gibt frei |
|---|---|
| KORPUS | GOLD, 6.1, 6.3, 6.4 |
| GOLD | 6.2 |
| 6.1, 6.2 | 7.2 |
| 7.2 | 8 |
| 8 | ZUS |

Regeln im Lauf (`Obsidian/_tools/board_sync.py`, gestartet über `_tools/daily.sh`,
launchd `com.projectjlu.daily`, 08:00):

- `\todo` offen → Karte nicht in Done; `\todo` verschwunden → Done mit Datum.
- Blocker offen → Vermerk `· blockiert: X offen`. Blocker erledigt → `#ai` wandert von
  To Do nach Doing mit `· freigegeben durch X (Datum)`; `#person` und `#team` werden nur
  markiert, nie entschieden und nie verschoben.
- `#ai` in Doing mit erledigten Blockern → Folgearbeit in `_tools/jobs.py`. Sie setzt
  ausschließlich ein, was `report/data/ergebnisse.json` liefert (`latex` je Karte, `summary`
  fürs Board). Fehlt Datei, Eintrag oder Anker, bleibt das `\todo` stehen und die Karte
  trägt `· wartet: <Grund>`. Es gibt keinen Schätzwert und keine erfundene Zahl.
- Ein Häkchen an einer Berichtskarte, deren `\todo` noch steht, wird sichtbar
  zurückgenommen: Kästchen wieder leer, Vermerk `· offen: \todo steht noch`.
  Eine Karte gilt nur dann als erledigt, wenn die Stelle im Bericht wirklich gefüllt ist.
- Manuell nach Doing gezogene Karten mit offenem `\todo` bleiben dort.
- Ohne Änderung wird keine Notiz und keine `.tex`-Datei geschrieben; `board.log` bekommt
  höchstens eine Bestätigungszeile pro Tag. Ein zweiter Lauf am selben Tag ist identisch.

Neun Karten sind an genau eine `\todo`-Stelle gebunden:

| Karte | Datei | Zeile |
|---|---|---|
| 6.1 Abweichungsraten | `report/chapters/06_ergebnisse.tex` | 29 |
| 6.2 Verfahrensvergleich | `report/chapters/06_ergebnisse.tex` | 53 |
| 6.3 Fehleranalyse | `report/chapters/06_ergebnisse.tex` | 73 |
| 6.4 Fall 2 (Versionsartefakt) | `report/chapters/06_ergebnisse.tex` | 98 |
| 7.2 Urteil je Hypothese | `report/chapters/07_diskussion.tex` | 49 |
| 8 Fazit-Zahl | `report/chapters/08_fazit.tex` | 15 |
| ZUS Ergebnissatz | `report/frontmatter/abstrakt.tex` | 18 |
| A.1 Faktkatalog | `report/backmatter/anhang.tex` | 9 |
| A.3 Modell/Prompt/Umgebung | `report/backmatter/anhang.tex` | 67 |

Geprüft am 21.11. auf Vault-Kopien mit demselben Einstiegspunkt `daily.sh`:

| Szenario | Ergebnis |
|---|---|
| KORPUS abgehakt | GOLD `freigegeben`, 6.1/6.3/6.4 nach Doing, Log „keine Messdaten", `\todo` bleibt |
| zusätzlich `ergebnisse.json` (Testdaten) | 6.1/6.3 eingesetzt, Karten Done mit `· Ergebnis`, `\todo` weg; 6.4 loggt fehlenden Eintrag |
| A.3-`\todo` entfernt | A.3 Done, kein Job, A.1 unberührt |
| 7.2 manuell nach Doing | bleibt Doing, `blockiert: 6.1, 6.2 offen` |
| zweiter Lauf | keine Notiz und keine `.tex` geändert (md5 identisch) |

Protokoll: `Obsidian/_tools/board.log` — Ereignisse immer, sonst höchstens eine
Bestätigungszeile pro Tag. Solange `report/data/ergebnisse.json` fehlt,
bleiben alle Messzahlen offen — die Kette ist scharf, aber ohne Daten tut sie nichts.

## Stand der Arbeitspakete

| Paket | Stand | Notiz |
|---|---|---|
| Themenwahl | Empfehlung fertig, Entscheidung offen | [[Vergleich und Empfehlung]] |
| Literatur | **13 zitierte Einträge am 21.11. am Original geprüft**, 2 Fehlzuschreibungen korrigiert; Reserve-Einträge und 3.5-Quelle offen | [[Literatur]] |
| Methodik | Messdesign entworfen | [[Methodik]] |
| Datenquellen | Adressen und Fassungen erfasst | [[Datenquellen]] |
| Hypothesen | drei Kandidaten, falsifizierbar | [[Hypothesen 3.1]] |
| Projektplan | 17-Wochen-Raster | [[Projektplan]] |
| GitLab-Repo | noch nicht angelegt | [[Prüfungsleistung ohne Vortrag]] |
| Kommunikation | E-Mail 1 versandfertig; **E-Mail 2 inkl. Exposé layoutgeprüft und versandfertig** (2 Platzhalter, Sperrdatum 27.11.) | [[Kommunikationsplan]] · [[E-Mail 2 – Kurzexposé]] |
| Satz | `report/` baut mit tectonic: Bericht 22 Seiten (13 Textseiten), Exposé 1 Seite; **9 `\todo` offen** (7 Messzahlen, 2 Entscheidungen) | [[LaTeX-Bericht]] |

## Was in dieser Woche zählt

1. Mail raus (Frist 26.11. ist hart, danach entscheidet die Zuteilung ohne die eigene Stimme).
2. GitLab-Zugang real testen, nicht nur „sollte gehen" — SSH nur im Uninetz oder per VPN,
   sonst HTTPS mit persönlichem Token.
3. Nichts weiter bauen. Vor der Zuteilung ist jede Codezeile Spekulation.
