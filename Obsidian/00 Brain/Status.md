---
titel: Status
stand: 2026-11-24
---

# Status

## Fristen

Bezugsdatum: Sa 21.11.2026. Tage in Klammern ab Bezugsdatum.

| Wann | Was | Tage | Erledigt |
|---|---|---|---|
| sofort | Einmal im JLU-GitLab anmelden, HRZ-Kennung per Mail an die Betreuung | — | ☑ 24.11. (Kennung in Mail 1) |
| Do 26.11.2026 | Zwei Themenwünsche (P1, P2) per Mail an die Betreuung | 5 | ☑ 24.11. gesendet |
| vor Di 01.12.2026 | Prüfungsleistung mitteilen: **Bericht 10–15 S. + Code, kein Vortrag** | 10 | ☑ 24.11. (in Mail 1) |
| Fr 27.11.2026, 11:00 | Zuteilung der Einzelarbeiten + erster Jour fixe (online, selber Raum) | 6 | ☐ |
| Di 01.12.2026 | Offizieller Start | 10 | — |
| KW 1–2 / Januar | Grober Projektplan + Meilensteingespräch (Termin folgt) | — | ☐ |
| Do 01.04.2027 | Abgabe im Abgaberepo der Betreuung | 131 | ☐ |

## Nächste Aktion

**Erledigt am 24.11.2026:** [[E-Mail 1 – Themenwünsche]] ist gesendet — zwei Themenwünsche,
Variante A, HRZ-Kennung, ZAD-Workspace als Rückfallebene. Wortlaut: [[Korrespondenz mit Busse]].

**Jetzt:** Antwort abwarten. Am **Fr 27.11.2026, 11:00** Zuteilung und erster Jour fixe
(online, selber Raum). Ablauf, beide Fragen und der Vorschlag an Team Gamma stehen in
[[Jour fixe 2026-11-27]].

**Danach:** [[E-Mail 2 – Kurzexposé]] mit `expose.pdf` senden, sobald zugeteilte Dimension
und Datum des Jour fixe feststehen. Vorlage: `E-Mail-2-versandfertig.txt` im Projektordner.

**VPN (blockiert den GitLab-Zugang):** Studierende erhalten VPN nur auf Antrag einer
Lehrperson beim HRZ. Befund, Mailtext und alle Schritte stehen in
[[GitLab-Zugang und Repo-Anlage]].

## Formatvorgaben geklärt (24.11.2026)

- **Berichtssprache: Deutsch.** Steht so in der Mail; `report/` bleibt deutsch.
- **Seitenrahmen: 10 bis 15 Seiten für den Textteil.** Titelblatt, Inhaltsverzeichnis,
  Literaturverzeichnis und Anhang zählen nicht mit (Antwort der Betreuung, 24.11.2026).
  Der Stand vom 21.11. — **13 Textseiten** bei 22 Seiten gesamt — liegt damit **im Rahmen**,
  mit zwei Seiten Polster für die Messkapitel. Die zwischenzeitlich geplante Kürzung um
  sieben Seiten entfällt. Budget: [[Prüfungsleistung ohne Vortrag]].
- **Themen-Mail geht ohne Rückfragen raus.** Frage 1 (Kombination) entfällt und wandert in
  den Jour fixe am 27.11. Pflichtangabe ist nur die Variante. Die Seitenangabe ist nach der
  Antwort der Betreuung aus der Mail entfallen, die Berichtssprache steht als ein Satz
  darin. Grund: [[Entscheidungen]].
- **Kick-off am 20.11.2026 nicht besucht** (familiäre Gründe). Protokoll und Unterlagen
  gelesen; die Abwesenheit steht offen in der Mail.

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

- **GitHub:** `dotrung1998/Trung_Do_Spezializierungsmodul`, Branch `main`. Seit
  23.11.2026 **öffentlich** (vorher privat). Nach dem Rewrite heißt der Wurzel-Commit
  `399febf`; die alten SHAs (`aa763b2` …) sind nur noch über direkte Abfrage erreichbar.
- **Commit-Regel** in `AGENTS.md` festgehalten: **keine Bot-Attribution** — keine
  `Co-Authored-By`-Zeile, kein „Generated with …“, keine Trailer. Gilt für jede Sitzung.
- **Seitenprüfung:** alle 12 Seiten von `main.pdf` am 21.11. als Bild gerendert und
  gelesen. Zwei stille Fehler gefunden und behoben: ß wurde als „SS“ gesetzt
  (XeTeX/T1, jetzt über `newunicodechar` auf `\ss{}` umgebogen) und in Anhang A.1 fehlte
  ein Leerzeichen („Änderungsrate,Quellen“). Danach 0 Overfull, 0 Missing character,
  12 Seiten. **Gegenprobe am 24.11.2026** mit `./build.sh`: 22 Seiten gesamt, davon
  13 Textseiten (Seite 1–13), Anhang 14–16, Literatur 17, Erklärung 18; eine
  Overfull-Zeile von 56 pt im Literaturverzeichnis. Die 22/13 sind damit gemessen,
  nicht geschätzt.

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
08:00 über GitHub Actions; der lokale launchd-Job `com.projectjlu.daily` ist seit
23.11.2026 entladen und deaktiviert):

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
| GitLab-Repo | noch nicht angelegt; Zugang nur per VPN, Antrag der Betreuung nötig (23.11. geprüft) | [[GitLab-Zugang und Repo-Anlage]] |
| Kommunikation | E-Mail 1 versandfertig; **E-Mail 2 inkl. Exposé layoutgeprüft und versandfertig** (2 Platzhalter, Sperrdatum 27.11.) | [[Kommunikationsplan]] · [[E-Mail 2 – Kurzexposé]] |
| Satz | `report/` baut mit tectonic: Bericht 22 Seiten (13 Textseiten), Exposé 1 Seite; **9 `\todo` offen** (7 Messzahlen, 2 Entscheidungen) | [[LaTeX-Bericht]] |

## Was in dieser Woche zählt

1. Mail raus (Frist 26.11. ist hart, danach entscheidet die Zuteilung ohne die eigene Stimme).
2. GitLab-Zugang real testen, nicht nur „sollte gehen" — SSH nur im Uninetz oder per VPN,
   sonst HTTPS mit persönlichem Token.
3. Nichts weiter bauen. Vor der Zuteilung ist jede Codezeile Spekulation.

## Automatisch (Fristen und Board)

Dieser Block wird bei jedem Tageslauf aus `Obsidian/_tools/fristen.json` und dem Board
neu geschrieben. Nicht von Hand bearbeiten — Änderungen gehören in `fristen.json`.

<!-- AUTO:START -->
**Fristen (automatisch, Stand 2026-11-24)**

| Termin | Was | Abstand | Wer |
|---|---|---|---|
| 2026-11-26 | Zwei Themenwünsche (P1, P2) per Mail an die Betreuung | in 2 Tagen | person |
| 2026-11-27, 11:00 | Zuteilung der Einzelarbeiten, erster Jour fixe (online) | in 3 Tagen | team |
| 2026-12-01 | Offizieller Start des Bearbeitungszeitraums | in 7 Tagen | team |
| 2027-04-01 | Abgabe im Abgaberepo der Betreuung | in 128 Tagen | person |

Board: 3 von 17 Karten erledigt; Quellenstand in [[Abgaben (auto)]].
<!-- AUTO:END -->

## Automatik, Repo und Datenschutz (23.11.2026)

- **GitHub Actions läuft.** Run 45099269485 (Tageslauf, 23.11.) war erfolgreich:
  10 Steps, echter Runner, `Bestätigt: Discord: gesendet (HTTP 204)`. Der Lauf hat
  seinen Commit selbst gepusht (`Tageslauf 2026-11-23: Quellen eingelesen, Board
  fortgeschrieben`). Der Author-Guard ist nach dem Fix für Force-Pushes grün
  (`dd6d854`).
- **Repo öffentlich.** `dotrung1998/Trung_Do_Spezializierungsmodul` ist seit 23.11.2026
  public (vorher privat).
- **Geschichte bereinigt.** Matrikelnummer und HRZ-Kennung stehen überall nur noch als
  `[Matrikelnummer]` / `[HRZ-Kennung]`. Die beiden gebauten PDFs (das Titelblatt druckte
  die Nummer) sind aus Baum und Geschichte entfernt, ebenso alle alten Commits per
  Force-Push (`+ e65d683...4196ea8`). Geprüft über alle 13 Commits von `origin/main`:
  **0 Treffer** für beide Werte, **0 PDF-Objekte**.
  **Grenze:** Die alten SHAs antworten über die API weiterhin; restlos weg sind sie erst
  nach einem Purge durch den GitHub-Support. Wegen der öffentlichen Phase ist die
  HRZ-Kennung als bekannt zu behandeln.
- **Titelblatt lokal.** `report/private.tex` (ignoriert, chmod 600) definiert
  `\matrikelnummer`. `main.tex` und `expose.tex` binden die Datei nur ein, wenn sie
  existiert; sonst bleibt der Platzhalter. Geprüft: mit Datei steht die Nummer im PDF,
  ohne sie baut es mit Platzhalter (rc=0).
- **Lokal.** Der LaunchAgent `com.projectjlu.daily` bleibt entladen und deaktiviert; es
  läuft nur der Cron in Actions.
- **Discord.** Das Secret `DISCORD_WEBHOOK` funktioniert (HTTP 204 im Run). Kommt im
  Channel nichts an, zeigt der Webhook auf einen anderen Kanal als den beobachteten.

## Discord-Bericht (24.11.2026)

`_tools/discord_notify.py` sendet seit dem 24.11. mehrere Nachrichten statt einer:
Lage (Quellen, Board, Änderungen), alle Fristen mit Begründung, offene Karten und
Entscheidungen, danach jede fällige Mail als **ein** Codeblock mit Kopierknopf.
Discord setzt an Codeblöcke einen Kopierknopf; Betreff und Mailtext stehen deshalb
zusammen in einem Block.

Geprüft mit `--dry-run`: 4 Nachrichten, längste 1953 von 2000 Zeichen; mit `--all`
6 Nachrichten (alle drei Mails). Matrikelnummer und HRZ-Kennung bleiben Platzhalter,
`shield()` entfernt lange Zahlenfolgen vor dem Senden. Die Quellen-Notiz wird nur bei
Änderung neu geschrieben; ältere „Geändert“-Listen erscheinen deshalb nicht als heutige
Änderung.

**Webhook (24.11.2026).** Der Kanal wurde gewechselt. Das GitHub-Secret
`DISCORD_WEBHOOK` trägt den Stand 24.11., 18:56; die lokale Datei
`~/.config/projektjlu/discord-webhook` wurde am Abend aus der Zwischenablage neu gesetzt
(chmod 600, Wert nicht im Vault). Testversand an den neuen Kanal: 4 Nachrichten,
HTTP 204 je Nachricht. Beide Wege — Actions und Mac — sind damit aktualisiert.
