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
