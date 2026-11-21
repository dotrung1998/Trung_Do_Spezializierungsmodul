#!/bin/bash
# Baut den Bericht oder das Kurzexposé.
#
#   ./build.sh            -> main.pdf    (Bericht)
#   ./build.sh expose     -> expose.pdf  (Ein-Seiten-Exposé für die Betreuung)
#   ./build.sh clean      -> beide PDFs und alle Hilfsdateien löschen
#
# Bewiesener Weg auf diesem Rechner: tectonic (XeTeX, lädt nur die benötigten
# Pakete nach, ruft BibTeX selbst auf).
# Fallback, falls tectonic fehlt: latexmk, dann pdflatex + bibtex von Hand.
set -uo pipefail
cd "$(dirname "$0")" || exit 1

case "${1:-}" in
  ""|main) DOC=main ;;
  expose)  DOC=expose ;;
  clean)
    command -v latexmk >/dev/null 2>&1 && latexmk -C >/dev/null 2>&1
    rm -f ./*.aux ./*.bbl ./*.bcf ./*.blg ./*.log ./*.out ./*.toc \
          ./*.run.xml ./*.fdb_latexmk ./*.fls ./*.xdv ./*.synctex.gz ./main-blx.bib
    rm -f main.pdf expose.pdf
    rm -rf build
    echo "Aufgeräumt."
    exit 0 ;;
  *)
    echo "Unbekanntes Ziel: $1"
    echo "Erlaubt: (ohne Argument) = Bericht, expose = Kurzexposé, clean"
    exit 2 ;;
esac

rc=0
if command -v tectonic >/dev/null 2>&1; then
  echo "Engine: tectonic $(tectonic --version 2>/dev/null | awk '{print $2}') -- $DOC.tex"
  tectonic -X compile --keep-logs "$DOC.tex" || rc=$?
elif command -v latexmk >/dev/null 2>&1; then
  echo "Engine: latexmk -- $DOC.tex"
  latexmk -pdf -interaction=nonstopmode -halt-on-error "$DOC.tex" || rc=$?
elif command -v pdflatex >/dev/null 2>&1; then
  echo "Engine: pdflatex + bibtex -- $DOC.tex"
  pdflatex -interaction=nonstopmode -halt-on-error "$DOC.tex" || exit 1
  if [ -f "$DOC.aux" ] && grep -q '\\bibdata' "$DOC.aux" 2>/dev/null; then
    command -v bibtex >/dev/null 2>&1 && { bibtex "$DOC" || exit 1; }
  fi
  pdflatex -interaction=nonstopmode -halt-on-error "$DOC.tex" || exit 1
  pdflatex -interaction=nonstopmode -halt-on-error "$DOC.tex" || exit 1
else
  cat <<'MSG'
Fehler: keine TeX-Engine gefunden.

  brew install tectonic     # klein, lädt nur die benötigten Pakete nach
MSG
  exit 127
fi

if [ "$rc" -ne 0 ]; then
  echo "Build fehlgeschlagen (Code $rc). Details in $DOC.log."
  exit "$rc"
fi
if [ ! -f "$DOC.pdf" ]; then
  echo "Kein PDF erzeugt -- Ausgabe oben prüfen."
  exit 1
fi

# Selbstkontrolle: offene Verweise sind ein Fehler, keine Randnotiz.
if [ -f "$DOC.log" ]; then
  if grep -q "There were undefined references\|Citation .* undefined\|LaTeX Warning: Reference" "$DOC.log"; then
    echo "WARNUNG: offene Verweise oder Zitate in $DOC.log."
  fi
fi
echo "Fertig: $DOC.pdf ($(du -h "$DOC.pdf" | cut -f1)), Protokoll: $DOC.log"
