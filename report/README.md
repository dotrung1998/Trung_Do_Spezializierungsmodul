# Bericht (LaTeX)

Satzkasten für den Bericht im Spezialisierungsmodul. Er ist **noch nicht** das
Abgabepaket: dorthin kommen später Bericht, Code und Daten zusammen (siehe „Abgabe“).

## Bauen

```bash
./build.sh          # -> main.pdf
./build.sh clean    # PDF und Hilfsdateien löschen
open main.pdf
```

`build.sh` nimmt die erste verfügbare Engine:

1. **tectonic** (bewiesen auf diesem Rechner, siehe unten),
2. `latexmk`,
3. `pdflatex` + `bibtex` von Hand.

Fehlt alles: `brew install tectonic` — ein kleines Binary, das nur die tatsächlich
benötigten Pakete nachlädt. Kein MacTeX nötig.

## Was hier bewiesen ist

| Punkt | Stand |
|---|---|
| Engine | tectonic 0.17.0 (XeTeX), `tectonic -X compile --keep-logs main.tex` |
| Fehler | keine |
| Offene Zitate/Verweise | keine (`main.log` sauber) |
| Literaturverzeichnis | 13 von 13 zitierten Schlüsseln gerendert |
| Umfang | 22 Seiten gesamt, davon 13 Textseiten (am 24.11.2026 am gebauten PDF gezählt); Titelblatt, Inhaltsverzeichnis, Literaturverzeichnis und Anhang zählen nicht mit |
| Inhalt | **nur Gerüst** — die `\todo`-Platzhalter stehen noch drin |

Das PDF ist ein **Bau-Nachweis**, kein Abgabestand.

### Literatur: biblatex mit BibTeX-Backend

Im Quelltext steht `backend=bibtex`. Grund: Das Tectonic-Bundle bringt biblatex 3.17
mit (Control-File 3.8), das per Homebrew installierte biber ist 2.22 (Control-File 3.11)
— die beiden verweigern zusammen die Arbeit. Tectonic ruft BibTeX selbst auf, also
braucht der Bau kein externes Werkzeug.

Wer später eine vollständige TeX-Live-Installation mit **passendem** biber hat, kann in
`preamble/packages.tex` auf `backend=biber` zurückstellen; dann verschwindet auch die
Warnung „Using fall-back BibTeX(8) backend“.

## Aufbau

```
main.tex                 Wurzel: lädt Vorspann, Kapitel, Anhang, Literatur
build.sh                 Bauen und Aufräumen
literatur.bib            Literaturverzeichnis (BibTeX, geprüfte Angaben)
preamble/
  packages.tex           Pakete, Engine-Weiche, babel ngerman
  settings.tex           Satz, PDF-Metadaten
  commands.tex           \todo, \arbeitstitel, \fakt
frontmatter/
  titelblatt.tex         Titel, Name, Matrikelnummer, Betreuung
  abstrakt.tex           Zusammenfassung (Platzhalter)
  eigenstaendigkeit.tex  Selbstständigkeitserklärung (Wortlaut prüfen!)
chapters/
  01_einleitung.tex      bis 08_fazit.tex
backmatter/anhang.tex    Faktkatalog, Schema, Prompts, Fehlertaxonomie, Code
figures/  tables/        Abbildungen und Tabellen
```

Seitenzählung: Titelseite ohne Anker, Vorspann römisch, Text arabisch.

## Arbeitsweise

1. **Ein Kapitel, eine Datei.** Nichts Inhaltliches in `main.tex`.
2. **`\todo{...}` statt Lücke.** Vor der Abgabe muss
   `grep -rn "\\\\todo" chapters/ frontmatter/` leer sein — dann ist nichts offen.
3. **Zahlen aus Skripten.** Jede Zahl im Text kommt aus einem Lauf, nicht aus dem Kopf.
4. **Seitenbudget** steht als Kommentar am Kopf jedes Kapitels. Es stammt aus
   `Obsidian/30 Plan/Prüfungsleistung ohne Vortrag.md`.
5. **Literatur** nur aus `literatur.bib`, keine handgeschriebenen Zitate im Text.

## Abgabe

Später einen Ordner `gamma-3-1-konsistenz/` im Abgaberepo anlegen und hineinlegen:

- `main.pdf` (der Bericht),
- `quellen/` mit dem LaTeX-Quelltext (dieser Ordner ohne Build-Artefakte),
- den Stand von Code und Daten, mit dem die Ergebnisse entstanden sind.

Nicht hinein: Build-Artefakte, Rohdaten, `.env`, Zugangsdaten.

## Offen

- Titel ist ein Arbeitstitel.
- Wortlaut der Selbstständigkeitserklärung ist ein Platzhalter.
- Sprache: **Deutsch**, entschieden und in der Mail an die Betreuung mitgeteilt
  (24.11.2026). Keine offene Frage mehr.
