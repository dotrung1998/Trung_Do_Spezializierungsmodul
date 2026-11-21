---
titel: LaTeX-Bericht
stand: 2026-11-21
status: baut sauber (tectonic); Inhalt ist noch Gerüst
---

# LaTeX-Bericht

Der Bericht wird in `report/` im Projektordner gesetzt — **getrennt vom Vault**. Grund:
Der Vault ist Denkablage, `report/` ist Satz und später Abgabe.

## Stand

| Was | Stand |
|---|---|
| Engine | **tectonic 0.17.0** (XeTeX), auf diesem Rechner installiert und gelaufen |
| Befehl | `cd report && ./build.sh` → intern `tectonic -X compile --keep-logs main.tex` |
| Ergebnis | `main.pdf`, **12 Seiten**, **0 Fehler** |
| Offene Zitate/Verweise | **keine** — `main.log` ohne `undefined`, kein `??`, kein `[?]` |
| Literaturverzeichnis | **13 von 13** zitierten Schlüsseln gerendert |
| Inhalt | **nur Gerüst**: 38 `\todo`-Platzhalter stehen noch im PDF |
| Titel | Arbeitstitel, noch nicht abgestimmt |
| Selbstständigkeitserklärung | Platzhalter, Wortlaut aus Modulvorlage nötig |

**Das PDF ist ein Bau-Nachweis, kein Abgabestand.** Es beweist, dass Satz, Gliederung,
Tabellen, Zitate und Seitenzählung funktionieren — nicht, dass der Bericht geschrieben ist.
Die roten `\todo`-Klammern sind Absicht und bleiben, bis die Betreuung die Richtung
bestätigt hat.

## Bauen

```bash
cd report
./build.sh          # -> main.pdf    (Bericht)
./build.sh expose   # -> expose.pdf  (Ein-Seiten-Exposé für die Betreuung)
./build.sh clean    # beide PDFs und Hilfsdateien löschen
```

`build.sh` nimmt die erste verfügbare Engine: **tectonic**, dann `latexmk`, dann
`pdflatex` + `bibtex`. Fehlt alles:

```bash
brew install tectonic
```

Kein MacTeX (5 GB) und kein sudo nötig. Tectonic lädt beim ersten Lauf nur die Pakete,
die der Quelltext wirklich benutzt.

## Literatur: biblatex mit BibTeX-Backend

Im Quelltext steht `backend=bibtex`, nicht `biber`. Grund, gemessen und nicht vermutet:

- Das Tectonic-Bundle bringt **biblatex 3.17** mit (Control-File 3.8).
- Das per Homebrew installierte **biber 2.22** erwartet Control-File 3.11.
- Ergebnis beim Versuch: `ERROR - Found biblatex control file version 3.8, expected
  version 3.11` → Abbruch.

Tectonic ruft BibTeX selbst auf, deshalb braucht der Bau kein externes Werkzeug. Der
Preis ist eine einzige, harmlose Warnung im Log: „Using fall-back BibTeX(8) backend“.
Für `authoryear`, 13 Quellen und diesen Umfang ändert das nichts am Ergebnis.

Wer später eine vollständige TeX-Live-Installation mit **passendem** biber hat, stellt in
`report/preamble/packages.tex` auf `backend=biber` zurück; dann verschwindet auch die
Warnung. Das per Homebrew installierte biber 2.22 ist derzeit ungenutzt und kann mit
`brew uninstall biber` wieder weg — es schadet aber nicht.

## Was beim Bauen repariert wurde

1. **babel fehlte.** `\documentclass[ngerman]{article}` lädt babel bei `article` nicht.
   Ohne `\usepackage[ngerman]{babel}` blieb die Sprache Englisch — inklusive
   englischer Literaturbezeichnungen (`english.lbx`).
2. **`\citet` ist in biblatex ohne `natbib` undefiniert.** Ersetzt durch `\textcite`.
3. **Gedankenstriche.** `—` und `–` fehlen in den T1/EC-Schriften unter XeTeX
   („Missing character“). Ersetzt durch `---` und `--`, deutsche Anführungszeichen
   durch `\enquote{}`.
4. **Doppelter Seitenanker.** Titelseite und Kapitel 1 trugen beide `page.1` →
   `\hypersetup{pageanchor=false}` um das Titelblatt, danach römische Zählung für den
   Vorspann und arabische ab Kapitel 1.
5. **biblatex-Optionskonflikt.** `giveninits=true` kollidierte mit `uniquename=full`,
   jetzt `uniquename=init`.

## Aufbau

```
report/
├── main.tex              Wurzel
├── build.sh              Bauen / Aufräumen (tectonic → latexmk → pdflatex)
├── literatur.bib         32 geprüfte Einträge, 13 davon zitiert
├── preamble/             packages (Engine-Weiche, babel), settings, commands
├── frontmatter/          titelblatt, abstrakt, eigenstaendigkeit
├── chapters/             01_einleitung … 08_fazit
├── backmatter/anhang.tex Faktkatalog, Schema, Prompts, Fehlertaxonomie, Code
├── figures/  tables/     Abbildungen und Tabellen
└── .gitignore            Build-Artefakte, main.pdf bleibt
```

## Seitenbudget (13 Seiten ohne Literatur und Anhang)

| Kapitel | Seiten |
|---|---|
| 1 Einleitung | 1,5 |
| 2 Hintergrund | 2,5 |
| 3 Forschungsfrage und Hypothesen | 1 |
| 4 Daten und Korpus | 1,5 |
| 5 Methode | 3 |
| 6 Ergebnisse | 3 |
| 7 Diskussion | 1,5 |
| 8 Fazit | 0,5 |

Das Budget steht als Kommentar am Kopf jeder Kapiteldatei. Es stammt aus
[[Prüfungsleistung ohne Vortrag]]; die Aufteilung ist ein Vorschlag, keine Vorgabe.

## Regeln

1. **`\todo{...}` statt Lücke.** Vor der Abgabe:
   `grep -rn "\\\\todo" report/chapters report/frontmatter` muss leer sein.
2. **Nichts in `main.tex` schreiben**, was Inhalt ist.
3. **Jede Zahl aus einem Skript.** Keine Zahl, die nur im Text existiert.
4. **Literatur nur aus `literatur.bib`**, nichts von Hand zitieren.
5. **Die BibTeX-Datei ist die geprüfte Fassung** von [[Literatur]]. Wer dort etwas
   ändert, ändert es hier mit — und umgekehrt.

## Abgabe

Später den Ordner `report/` (ohne Build-Artefakte) plus `main.pdf` plus Code in den
Abgabeordner `gamma-3-1-konsistenz/` des Abgaberepos legen. Details im Leitfaden:
[[GitLab-Leitfaden (Quelle)]].

## Was noch fehlt

- Text: 38 `\todo`-Stellen füllen (Kapitel 5 und 6 zuerst, sie tragen die Note).
- Titel mit der Betreuung abstimmen.
- Wortlaut der Selbstständigkeitserklärung beschaffen.
- Sprache des Berichts klären (Frage 2 in [[E-Mail 1 – Themenwünsche]]). Bei Englisch:
  Klassenoption und babel auf `english` umstellen, biblatex-Stil prüfen.

## Bezug

[[Prüfungsleistung ohne Vortrag]] · [[Literatur]] · [[Person]]
