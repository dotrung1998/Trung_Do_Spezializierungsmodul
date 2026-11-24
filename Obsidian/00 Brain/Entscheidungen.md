---
titel: Entscheidungen
stand: 2026-11-21
---

# Entscheidungen

Regel: nur ergänzen, nie rückwirkend umschreiben. Jede Zeile mit Datum, Grund und
verworfener Alternative. Wenn eine Entscheidung später kippt, wird sie nicht gelöscht,
sondern durch einen neuen Eintrag „ersetzt".

---

## 2026-11-21 — Prüfungsleistung: Bericht 10–15 Seiten mit Code, kein Vortrag

**Entscheidung.** Variante ohne Vortrag.
**Grund.** Der Bericht ist ohnehin Pflicht; der Vortrag kostet zusätzlich Vorbereitung
und Prüfungsangst-Risiko, bringt aber keine eigene Note. Der Aufwand wandert in
Messqualität und Schreibpräzision — genau dort, wo die Bewertung eines
Data-Analytics-Moduls ansetzt: nachvollziehbare Methode, belegte Zahlen, sauberer Code.
**Verworfen.** 5–10 Seiten + Vortrag 20–30 Min. Wäre sinnvoll, wenn die Arbeit
überwiegend konzeptionell wäre und mündlich besser erklärbar als schriftlich. Ist sie nicht.
**Risiko.** Ohne Vortrag muss der Bericht alles allein tragen; keine Gelegenheit, eine
Unschärfe mündlich zu retten. Gegenmaßnahme: Gliederung früh mit der Betreuung abstimmen.

## 2026-11-21 — Priorität 1: 3.1 Konsistenz, Priorität 2: 3.2 Aktualität

**Entscheidung.** Empfehlung an die Person, siehe [[Vergleich und Empfehlung]].
**Grund.** 3.1 ist die Dimension mit dem klarsten Messversprechen: Abweichungen zwischen
Quellen sind zählbar, die Einheit ist definierbar, die Evaluation ist ehrlich (Precision/
Recall gegen einen Goldstandard). 3.2 ist die methodisch risikoärmste Alternative und
teilt sich den Korpus mit 3.1 — ein Quellenstand, zwei Messungen.
**Verworfen.** 3.4 Verständlichkeit (bekannte Antwort auf die gestellte Frage, wenig
Data-Analytics-Substanz), 3.5 Mehrsprachigkeit (überwiegend deskriptiv), 3.3
Auffindbarkeit (kleine Frage, Aufwand für den Crawl steht in keinem Verhältnis).
**Vorbehalt.** Gültig nur, solange die Zuteilung am 27.11. nicht anders entscheidet.
Bei Zuteilung von 3.2 rückt die Arbeit auf 3.2, die Methodik bleibt übertragbar.

## 2026-11-21 — Vault als Gedächtnis, GitLab als Abgabe

**Entscheidung.** Zwei getrennte Orte. `Obsidian/` hält Entscheidungen, Quellen und
Argumente; das GitLab-Repo hält Code, Datenblatt und Bericht.
**Grund.** Der Leitfaden verlangt ein privates Repo mit Mindeststruktur und die Betreuung
als Reporter. Der Vault enthält Arbeitsnotizen, die niemand prüfen muss. Vermischung
würde das Abgaberepo unruhig machen.
**Verworfen.** Alles in ein Repo. Wäre einfacher, würde aber Denknotizen und Abgabe
untrennbar machen.

## 2026-11-21 — Extraktion mit LLM, Prüfung mit Zitatpflicht

**Entscheidung.** Jede automatische Extraktion muss die Fundstelle (Dokument-ID und
Textstelle) mitliefern; ohne Zitat gilt der Wert als nicht extrahiert.
**Grund.** Ein Sprachmodell liefert plausible Werte auch dort, wo keine stehen. Die
Zitatpflicht macht Halluzinationen billig prüfbar und den Goldstandard schneller.
**Verworfen.** Freie Extraktion ohne Belegstelle, danach manuelle Kontrolle von Hand.
Wäre schneller im ersten Schritt und deutlich teurer in der Prüfung.
**Belegt durch.** [[Literatur]] — LLM-Annotatoren müssen gegen menschliche Labels
validiert werden, bevor man ihnen für eine Messung glaubt.

## 2026-11-21 — Literaturangaben gegen Primärquellen geprüft, Zitierfehler korrigiert

**Entscheidung.** Jede Angabe in [[Literatur]] braucht Verfasser, Titel, Jahr,
Erscheinungsort und Seiten bzw. Artikelnummer, geprüft an der Verlags-, Norm- oder
Repository-Seite. Was nicht belegbar ist, steht mit `[nicht verifiziert]` und Begründung
oder fällt heraus.
**Grund.** Bei der Prüfung der fünf offenen Einträge kam ein **falscher Verfassername**
zum Vorschein: „Kumar, S., et al. (2020)“ statt Mallawaarachchi et al. (2020). Ein
plausibel klingender Name im Literaturverzeichnis ist ein konkreter Notenschaden, weil er
die Sorgfalt der ganzen Arbeit in Frage stellt.
**Korrigiert.** DIN SPEC 33429 (Jahr **2025-03**, nicht 2023), ISO/IEC 25024
(vollständiger Titel, 45 S.), Batini et al. (Article 16, DOI), Li et al. (DOI),
Fetterly et al. (Schreibweise bestätigt, S. 669–678, DOI, Journalfassung 2004),
Weiss & Meurers (zwei Autoren, kein „et al.“), Ruohonen (Verfasser statt „Europäische
Union“), Bleiholder & Naumann und Rosenfeld et al. ergänzt; Reineke (2005) **entfernt**,
weil nicht belegbar.
**Verworfen.** Einträge vorsichtig mit „zu prüfen“ stehen zu lassen. Das sieht ordentlich
aus und ist eine Zeitbombe: Niemand prüft es später.

## 2026-11-21 — Bericht baut mit tectonic, biblatex über BibTeX-Backend

**Entscheidung.** Satz mit **tectonic 0.17.0** (XeTeX). Ein Befehl: `cd report &&
./build.sh` → `tectonic -X compile --keep-logs main.tex`. In `preamble/packages.tex`
steht `backend=bibtex` statt `biber`.
**Grund.** Auf dem Rechner ist keine TeX-Distribution installiert. tectonic ist ein
kleines Binary (schon vorhanden), lädt nur die benötigten Pakete und ruft BibTeX selbst
auf — kein MacTeX (ca. 5 GB), kein sudo. `biber` aus Homebrew (2.22) ist mit biblatex
3.17 aus dem Tectonic-Bundle **messbar** unverträglich: `Found biblatex control file
version 3.8, expected version 3.11` → Abbruch.
**Verworfen.** MacTeX/mactex-no-gui (5 GB, nicht nötig), Docker-Image `texlive/texlive`
(läuft, aber mehrere GB Download für ein 12-seitiges Gerüst), biber 2.22 erzwingen
(Versionsfehler), biblatex durch klassisches BibTeX + natbib ersetzen (verliert
`\textcite` und die Stilverwaltung).
**Ergebnis.** 12 Seiten, 0 Fehler, 0 offene Zitate oder Verweise, 13 von 13 Quellen im
Literaturverzeichnis. Die 38 `\todo`-Platzhalter bleiben absichtlich — das PDF ist ein
Bau-Nachweis, kein Abgabestand.
**Preis.** Eine harmlose Warnung im Log: „Using fall-back BibTeX(8) backend“. Steht so
auch in [[LaTeX-Bericht]], damit sie später niemand für einen Fehler hält.
**Nebenbefund, für die Sorgfalt der Arbeit nützlich.** Drei Fehler, die nur durch echtes
Kompilieren sichtbar wurden: babel war nie geladen (Sprache blieb Englisch), `\citet`
ist in biblatex ohne `natbib` undefiniert, und die Unicode-Gedankenstriche fehlen den
T1/EC-Schriften unter XeTeX. Statische Prüfung hatte alle drei nicht gefunden.

## 2026-11-21 — Ordnung: 3. Änderungsfassung zitiert, nicht die 1.

**Entscheidung.** Die Spezielle Ordnung M.Sc. Data Analytics wird als „Fassung des
3. Änderungsbeschlusses, Mitteilungen der JLU 7.36.07 Nr. 11, gültig ab SoSe 2026“
zitiert, Dateikennung `7_36_07_11_3ae`.
**Grund.** Im WiSe 2026/27 ist die 3. Änderungsfassung verbindlich. Die früher verlinkte
Adresse `..._1ae` war die 1. Änderung — zitierbar, aber die falsche Fassung.
**Nebenbefund, für 3.1 verwertbar.** Die Übersichtsseite nennt für die 1. Änderung
„in Kraft 01.12.2023, gültig ab WiSe 2023/24“, die Titelseite derselben PDF „gilt ab dem
Wintersemester 2024/25“. Zwei Primärquellen derselben Einrichtung widersprechen sich im
Geltungsbeginn — ein echtes, belegbares Beispiel für die Versionsartefakte, die die
Arbeit messbar machen soll.

## 2026-11-21 — E-Mail 2 ist das Kurzexposé, die Hypothesenmail wird Vorrat

**Entscheidung.** Die zweite Mail an die Betreuung ist ein Ein-Seiten-Kurzexposé
(Fragestellung, Daten, Methode, Zeitplan) als PDF-Anlage, mit der Bitte um Bestätigung vor
Kapitel 5 und 6. Die frühere Hypothesenmail bleibt als E-Mail 3 im Vorrat.
**Grund.** Das Exposé enthält H1 und H2 ohnehin; eine eigene Hypothesenmail würde dieselben
Fragen ein zweites Mal stellen. Wichtiger: eine schriftliche Freigabe vor dem
Methodenkapitel ist die einzige Absicherung, wenn die Methodenwahl später hinterfragt wird
— mündlich im Januar käme sie zu spät, weil Kapitel 5 und 6 vorher entstehen.
**Verworfen.** Hypothesenmail wie geplant Mitte Dezember senden (Dopplung, zwei Mails
statt einer). Bestätigung nur mündlich im Meilensteingespräch (zu spät). Das Exposé in den
Mailtext schreiben statt als PDF (eine Seite PDF wird gelesen, vier Bildschirme Text nicht).
**Form.** Drei nummerierte Fragen mit Alternative, beantwortbar in zwei Minuten. Kein
Terminwunsch im Vordergrund; ein Gespräch wird angeboten, nicht verlangt.

## 2026-11-21 — Textteil geschrieben, Messkapitel bleiben offen

**Entscheidung.** Kapitel 1–5 sowie 7.3 und 7.4 sind ausformuliert. Kapitel 6, 7.1, 7.2, 8,
die Zusammenfassung und fünf Anhangteile bleiben `\todo`.
**Grund.** Diese Stellen verlangen Zahlen aus dem eigenen Lauf (Korpus, Goldstandard,
Fehleranalyse) oder eine Teamfestlegung (Faktkatalog). Ein Bericht mit erfundenen
Abweichungsraten wäre wertlos und ein Täuschungsversuch; die Bewertung setzt auf belegte
Messung.
**Verworfen.** Platzhalterzahlen `XX` (sieht fertig aus, ist es nicht); erfundene
Beispielwerte (verletzt „keine Zahlen ohne Quelle“); Kapitel 6 als reine
Auswertungsvorschrift umschreiben (ändert die Gliederung, ohne dass die Betreuung sie
gesehen hat — das entscheidet die Betreuung).
**Nebenbefund.** Das belegte Beispiel des Geltungsbeginns steht in Kapitel 1 und in
Tabelle 2; beide Dokumente wurden am 21.11. erneut geöffnet.

## 2026-11-21 — Zweiter Durchgang: Methodenartefakte statt Platzhalter

**Entscheidung.** A.2 (Extraktionsschema), A.4 (Fehlertaxonomie) und A.5 (Code-Verzeichnis)
sind als Entwurf ausformuliert; Kapitel 6, 7.1/7.2, 8 und die Zusammenfassung tragen Text,
soweit er ohne Messung aussagbar ist. A.1 und A.3 bleiben unangetastet.
**Grund.** Ein Schema und eine Fehlertaxonomie sind Methodenentscheidungen, keine
Messergebnisse; sie lassen sich begründen, bevor Daten da sind. A.5 nennt nur Dateien, die
wirklich existieren — ein Verzeichnis erfundener Module wäre eine Behauptung über das Repo.
**Verworfen.** A.5 mit geplanten Verzeichnissen (`src/`, `data/`, `tests/`) füllen (sieht
vollständiger aus, behauptet aber Existenz); Fehlertaxonomie mit Häufigkeiten (erfunden);
Kapitel 6 mit Beispielzahlen (Täuschung).
**Grenze.** Sieben Lücken bleiben messzahlgebunden: 6.1–6.3, 6.4/Fall 2, 7.2-Urteil,
Fazit-Zahl, Zusammenfassungszahl. Sie sind in [[Status]] einzeln benannt.

## 2026-11-21 — URL-Umbruch über ein eigenes Feldformat gelöst

**Entscheidung.** `\DeclareFieldFormat{url}{URL\addcolon\space\mbox{\url{#1}}}`, gesetzt
nach dem Laden von biblatex.
**Grund.** Die Adresse darf nicht nach `https:` brechen. Die naheliegenden Hebel
(`\UrlBreaks`, `\UrlBigBreaks`, eigenes `\biburlsetup`) greifen nicht, weil biblatex die
Regeln je Eintrag neu setzt; das wurde am gerenderten PDF geprüft, nicht vermutet. Eine
unteilbare Box löst das ohne Eingriff in biblatex.
**Verworfen.** Break an beliebiger Stelle zulassen (der Fehler bleibt sichtbar); Protokoll
aus der Anzeige entfernen (ändert den Inhalt der Angabe); `biber` erzwingen (Versionskonflikt
mit biblatex 3.17).
**Preis.** Für sehr lange URLs wäre die Box riskant (Overfull). Im aktuellen Verzeichnis sind
nur zwei Adressen betroffen, beide passen; bei neuen Einträgen mit langen URLs prüfen.

## 2026-11-23 — Nur ein Scheduler: GitHub Actions, nicht launchd

**Entscheidung.** Den LaunchAgent `com.projectjlu.daily` am 23.11.2026 entladen
(`launchctl bootout`) und deaktiviert (`launchctl disable`). Geplant läuft nur noch
`.github/workflows/tageslauf.yml` um 08:00 Europe/Berlin.
**Grund.** Der Agent war seit dem 21.11. geladen und lief am 21. und 22.11. um 08:00
(Beleg: `Obsidian/_tools/daily.log`). Mit dem neuen Workflow hätte es zwei Läufe pro Tag
gegeben: zwei Discord-Berichte und konkurrierende Commits auf `main`.
**Verworfen.** Agent geladen lassen und den Cron im Workflow auf eine andere Uhrzeit legen
(verschiebt das Problem nur); die plist-Datei löschen (nicht nötig, `disable` ist
umkehrbar und lässt den Rückweg offen); den Agent als einzigen Scheduler behalten (der
Rechner müsste dafür wach sein und der Lauf hinge an einem Gerät).
**Preis.** Der Lauf hängt jetzt an GitHub; ein fehlgeschlagener Run fällt nur im
Actions-Tab und im Discord-Bericht auf.

## 2026-11-24 — Discord-Bericht wird die Arbeitsfläche, nicht nur ein Signal

**Entscheidung.** `_tools/discord_notify.py` sendet mehrere Nachrichten: Lage und
Quellen, alle Fristen mit Begründung, offene Karten und Entscheidungen, danach jede
fällige Mail als **ein** Codeblock mit Kopierknopf — Betreff und Text zusammen.
**Grund.** Der bisherige Bericht nannte nur Zahlen; für die nächste Handlung musste
trotzdem der Vault geöffnet werden. Discord ist auf dem Telefon der zuverlässig
erreichbare Kanal. Ein Codeblock ist dort die einzige Form, die sich mit einem Klick
vollständig kopieren lässt.
**Verworfen.** Eine einzelne Nachricht (2000-Zeichen-Grenze; eine Mail würde mitten im
Text abschneiden). Mailtexte als Fließtext (kein Kopierknopf, Zeilenumbrüche gehen
verloren). Embed-Felder (1024 Zeichen je Feld, zu klein für eine Mail).
**Grenze.** Matrikelnummer und HRZ-Kennung bleiben Platzhalter; `shield()` ersetzt lange
Zahlenfolgen vor dem Senden. Versandfertig wird die Mail erst mit den persönlichen
Angaben, die bewusst nur lokal stehen.

## 2026-11-24 — Bericht auf Deutsch

**Entscheidung.** Der Bericht wird auf Deutsch verfasst.
**Grund.** Steckbrief, Protokoll und Leitfaden sind deutsch, die Fachbegriffe (Konsistenz,
Aktualität, Verständlichkeit) sind im Deutschen geprägt, und die Betreuung liest und
prüft auf Deutsch. Ein englischer Bericht müsste diese Begriffe erst definitorisch
einholen und die Zitate doppelt führen.
**Verworfen.** Englisch. Kein Zusatznutzen für die Bewertung, dafür Übersetzungsarbeit an
Begriffen, Tabellen und Zitaten.
**Stand.** Angabe der Person am 24.11.2026; die Frage entfällt damit aus der Mail und
steht dort als Feststellung.

## 2026-11-24 — Die 10 bis 15 Seiten umfassen Literaturverzeichnis und Anhang

**Entscheidung.** Literaturverzeichnis und Anhang zählen in den Seitenrahmen von 10 bis 15
Seiten hinein. Titelblatt und Inhaltsverzeichnis sind nicht mitgezählt; falls die Betreuung
das anders sieht, wird dieser Eintrag durch einen neuen ersetzt.
**Grund.** Angabe der Person am 24.11.2026. Der Rahmen ist damit deutlich enger als am
21.11. angenommen, als der Textteil mit 13 Seiten plus 9 Seiten Front- und Backmatter
geplant wurde.
**Folge.** Der Satz steht bei 22 Seiten gesamt und damit rund sieben Seiten über dem Limit.
Einzige belastbare Reaktion: Anhang auf das Notwendige kürzen (Fehlertaxonomie und
Code-Verzeichnis gehören ins Repo, nicht in den Bericht), Text auf 12 Seiten verdichten,
Tabellen sparsamer setzen. Neues Budget in [[Prüfungsleistung ohne Vortrag]], Stand in
[[Status]].
**Verworfen.** Seitenzahl klein setzen oder Anhang als „nicht zum Bericht gehörig“
deklarieren. Das ist eine Umgehung des Rahmens und fällt bei der Prüfung auf.

## 2026-11-24 — Themen-Mail ohne Rückfragen, einfachere Sprache

**Entscheidung.** Die Mail an die Betreuung geht ohne die drei Fragen raus. Frage 1
(Kombination 3.1/3.2) entfällt, Fragen 2 und 3 sind geklärt und stehen als Feststellung im
Text. Die Rechenumgebung wird als Einschätzung formuliert, nicht als Frage. Sprachlich:
kurze Sätze, keine Gedankenstriche, keine Semikolons.
**Grund.** P1/P2 ist ein Wunsch, keine Verhandlung; die Zuteilung passiert am 27.11. im
Gespräch, dort ist die Rückfrage billiger. Jede Frage in einer Mail kostet eine
Antwort-Runde, und die Betreuung verwaltet 15 Arbeiten. Frage 1 hätte zudem wie die Bitte
um Bestätigung geklungen, obwohl die Begründung schon im Text stand.
**Verworfen.** Drei Fragen behalten (drei Antwortpunkte statt null). Frage 1 in der Mail
lassen (liest sich als „kann ich beide Themen bekommen?“). Gedankenstriche und Semikolons
als Stilmittel behalten (die Mail wird am Bildschirm überflogen, nicht studiert).
**Grenze.** Frage 1 wandert in den Jour fixe am 27.11.; wenn sie dort nicht beantwortet
wird, bleibt die Priorisierung wie gewählt.

## 2026-11-24 — Pflichtangabe ist nur die Variante, Sprache und Seiten sind Annahme

**Entscheidung.** Die Mail nennt die Prüfungsvariante als Pflichtangabe. Berichtssprache
und Seitenzählung stehen als Annahme im Text, mit der Bitte um Korrektur in einer Zeile,
aber ohne Fragezeichen. Die Abwesenheit beim Kick-off am 20.11.2026 wird offen genannt.
**Grund.** Im Protokoll vom 20.11. steht nur eine Mitteilungspflicht: „Die Wahl teilt jede
Person vor dem offiziellen Start mit.“ Für Sprache und Seitenzählung gibt es keine
Vorgabe in Protokoll, Rahmen oder Leitfaden. Beides bleibt trotzdem in der Mail, weil die
Seitenzählung über rund sieben Seiten Umbau entscheidet; eine Zeile der Betreuung ist
billiger als ein Befund im März.
**Nachtrag (24.11.2026).** Die Betreuung hat die Zählweise am selben Tag beantwortet:
Titelblatt, Inhaltsverzeichnis, Literaturverzeichnis und Anhang zählen nicht mit. Die
Seitenangabe ist damit aus der Mail gestrichen. Maßgeblich ist der Eintrag „10 bis 15
Seiten ohne Titelblatt, Inhaltsverzeichnis, Literatur und Anhang“.
**Zur Abwesenheit.** Der Kick-off fand ohne die Person statt. Eine Mail, die sich für den
Kick-off bedankt, behauptet eine Teilnahme, die es nicht gab. Zwei Sätze, die das klären,
verhindern die Rechtfertigung später.
**Verworfen.** „Der Bericht wird auf Deutsch verfasst“ als Feststellung ohne Rückkanal
(keine Quelle für die Vorgabe). Die beiden Formatsätze ganz streichen (dann fehlt die
Absicherung für das Seitenbudget). Teilnahme am Kick-off stillschweigend übergehen.

## 2026-11-24 — 10 bis 15 Seiten ohne Titelblatt, Inhaltsverzeichnis, Literatur und Anhang

**Entscheidung.** Die 10 bis 15 Seiten beziehen sich auf den Textteil. Titelblatt,
Inhaltsverzeichnis, Literaturverzeichnis, Anhang und Selbstständigkeitserklärung zählen
nicht mit.
**Grund.** Antwort der Betreuung auf die Rückfrage der Person am 24.11.2026. Damit ist der
Eintrag „Die 10 bis 15 Seiten umfassen Literaturverzeichnis und Anhang“ vom selben Tag
**überholt**; er bleibt als Verlauf stehen und wird nicht umgeschrieben.
**Folge.** Der Satz steht mit **13 Textseiten** innerhalb des Rahmens von 10 bis 15. Die
geplante Kürzung um rund sieben Seiten entfällt. Es bleibt ein Polster von zwei Seiten nach
oben, das in Kapitel 6 und 7 gebraucht wird, sobald die Messzahlen da sind. Anhang und
Literatur werden nicht mehr aus Platzgründen gekürzt, sondern nur noch aus Qualitätsgründen
(Fehlertaxonomie und Code-Verzeichnis gehören weiterhin ins Repo, weil sie dort prüfbar sind).
Budget in [[Prüfungsleistung ohne Vortrag]].
**Verworfen.** Die frühere Annahme „Anhang zählt mit“ beibehalten (hätte sieben Seiten
Text gekostet, die niemand verlangt). Die Formatsätze in der Mail stehen lassen (die
Seitenangabe wäre jetzt falsch und würde eine Rückfrage erzeugen, die es nicht braucht).

## 2026-11-24 — Themen-Mail gesendet

**Entscheidung.** [[E-Mail 1 – Themenwünsche]] ist am Di 24.11.2026 an die Betreuung
gesendet. Inhalt: Abwesenheit beim Kick-off, zwei Themenwünsche P1/P2, Variante A mit
Deutsch als Berichtssprache, HRZ-Kennung, eigener Rechner als Messumgebung mit dem
ZAD-Workspace als Rückfallebene.
**Grund.** Frist für die Themenwünsche ist Do 26.11. Wer bis dahin nichts schickt, wird
ohne eigene Stimme zugeteilt (Projektrahmen). Die Zuteilung findet am Fr 27.11., 11:00
statt, also zwei Tage nach der Frist — die Mail ist der einzige Kanal vorher.
**Was gegenüber dem Entwurf geändert wurde.** Unterschrift „Trung Do“ mit der
Matrikelnummer in der Signaturzeile statt im Betreff. „Kein zwingender Bedarf“ statt „kein
Bedarf“, dazu die Bitte um den Workspace als Rückfallebene (Grund: kein Warten im Januar).
Der Satz zum Goldstandard gestrichen, der Satz zur Seitenzählung entfällt, weil geklärt.
**Folge.** Antwort und Zuteilung abwarten, dann [[Korrespondenz mit Busse]] ergänzen und
[[E-Mail 2 – Kurzexposé]] senden. Die aus der Mail gestrichene Frage zur Kombination
3.1/3.2 gehört in den Jour fixe am 27.11.
**Offen.** Die Mail nennt einen erfolgten GitLab-Login. Der Befund vom 23.11. (TCP 443
läuft ohne VPN in einen Timeout) widerspricht dem nicht zwingend, belegt es aber auch
nicht ([[GitLab-Zugang und Repo-Anlage]]). Beim ersten eigenen Login prüfen und, falls er
nicht klappt, in der Antwort an die Betreuung korrigieren.
**Verworfen.** Bis zum 26.11. warten (kein Vorteil, jede Verzögerung erhöht das Risiko,
ohne eigene Stimme zugeteilt zu werden). Die Frage nach dem Workspace als Bitte um
Entscheidung formulieren (die Mail soll keine Rückfrage erzeugen).

## 2026-11-24 — Jour fixe mit drei Punkten vorbereitet, Berichtsumfang im README korrigiert

**Entscheidung.** Für den Jour fixe am Fr 27.11.2026, 11:00 stehen vier Punkte in dieser
Reihenfolge fest ([[Jour fixe 2026-11-27]]): Zuteilung, Kombination 3.1/3.2, VPN und
GitLab, Vorschlag an Team Gamma. Die Frage zur Kombination wird als geschlossene
Alternative gestellt („trägt die Kombination, oder ist eine zu viel?" und „welche fehlt
dem Team mehr?"). Der Team-Vorschlag kommt als drei verabredbare Punkte: ein Stichtag,
ein Projekt `team-gamma`, ein Katalog von zwölf Sachverhalten.
**Grund.** Zwei der drei Themen wurden bewusst aus Mail 1 herausgehalten, damit die Mail
keine Rückfrage erzeugt. Der Jour fixe ist der nächste Kanal, nicht eine zweite Mail.
Regel 2 des [[Kommunikationsplan]]s verlangt geschlossene Fragen, deshalb die Alternative
statt „Wie soll ich vorgehen?".
**Zweitens.** `report/README.md` nannte als Umfang noch 12 Seiten. Richtig sind 22 Seiten
gesamt mit 13 Textseiten; Titelblatt, Inhaltsverzeichnis, Literaturverzeichnis und Anhang
zählen nicht mit (Antwort der Betreuung vom 24.11.2026). Die alte Zahl widersprach
[[Prüfungsleistung ohne Vortrag]] und dem Kopfkommentar der Kapitel.
**Folge.** Nach dem Termin: Zuteilung eintragen, Zusammenfassungsmail schreiben, Team-Mail
anpassen, Projekt anlegen sobald der Login geht, Exposé vorbereiten.
**Offen.** Die Themenmail behauptet einen erfolgten GitLab-Login. Wenn er nicht aufging,
wird das im Termin korrigiert und nicht per Mail nachgeschoben.
**Verworfen.** Die Kombinationsfrage vor dem 27.11. per Mail nachschieben (zweite Mail,
zweite Rückfrage, Frist war der 26.11.). Die Zahl im README stehen lassen, bis der Bericht
gebaut wird (der Widerspruch wäre bis zur Abgabe mitgeschleppt worden).

## 2026-11-24 — Kapitelbudgets an die verbindliche Tabelle angeglichen

**Entscheidung.** Verbindlich für den Seitenumfang ist allein die Tabelle in
[[Prüfungsleistung ohne Vortrag]]: 13 Textseiten im Stand vom 21.11., Ziel 15, Rahmen 10
bis 15 ohne Titelblatt, Inhaltsverzeichnis, Literaturverzeichnis und Anhang. Die
Kapitelköpfe in `report/chapters/` und die Übersicht in [[LaTeX-Bericht]] geben genau
diesen Stand wieder: Kapitel 2 mit 2 statt 2,5, Kapitel 5 mit 2,5 statt 3, Kapitel 6 mit
Ziel 4 statt 3, Kapitel 7 mit Ziel 2 statt 1,5. Die Summe der Ziele ergibt 15.
**Grund.** Beim Durchsuchen des Repos nach abweichenden Seitenzahlen kamen drei Fassungen
desselben Budgets zum Vorschein: die verbindliche Tabelle mit 13, die Übersicht in
[[LaTeX-Bericht]] mit 14,5 und die Kapitelköpfe, die teils der einen, teils der anderen
folgten. Drei Zahlen für eine Sache sind ein Fehler, der beim Schreiben Zeit kostet.
**Drittens.** In `report/README.md` stand unter „Offen“ noch, die Sprache hänge an der
Antwort der Betreuung. Sie ist seit dem 24.11. entschieden (Deutsch) und in der Mail
mitgeteilt.
**Folge.** Wer das Budget ändert, ändert zuerst [[Prüfungsleistung ohne Vortrag]] und zieht
dann die Kapitelköpfe nach.
**Verworfen.** Die Kapitelköpfe an der Übersicht in [[LaTeX-Bericht]] ausrichten (die
Übersicht war selbst die falsche Fassung). Die Zahl der Textseiten neu messen (ohne
gebautes `main.pdf` gäbe es dafür keinen Beleg; der Stand vom 21.11. bleibt bis zum
nächsten Bau die Referenz).

## 2026-11-24 — 22 Seiten und 13 Textseiten sind gemessen, nicht geschätzt

**Entscheidung.** Die Zahlen bleiben, wie sie sind: **22 Seiten gesamt, 13 Textseiten**.
`cd report && ./build.sh` (tectonic 0.17.0) hat sie am 24.11.2026 bestätigt: Vorspann
4 Seiten (Titelblatt ohne Nummer, Zusammenfassung i, Inhaltsverzeichnis ii–iii), Textteil
Seite 1–13, Anhang 14–16, Literaturverzeichnis 17, Selbstständigkeitserklärung 18.
**Grund.** Die Zahl stand vorher ohne Beleg im Vault, und die Statusnotiz vom 21.11.
nennt 12 Seiten für denselben Bau-Nachweis. Beides ist vereinbar: der Stand vom 21.11.
war ein früherer Bau; der Textteil ist seither um Vorspann, Anhang und Literatur
gewachsen. Ein Widerspruch bleibt also nicht stehen, sondern eine datierte Messung.
**Folge.** Wer die Zahl im Bericht oder im Vault nennt, nennt den Bau vom 24.11.2026.
Die Kapitelbudgets (13 im Stand, 15 als Ziel) bleiben unverändert gültig.
**Offen.** Eine Overfull-Zeile von 56 pt im Literaturverzeichnis, ein DOI bricht nicht um.
Kosmetisch, vor der Abgabe beheben (`\sloppy` lokal oder `url`-Umbruch).
