#!/bin/bash
# Taeglicher Lauf: Quellen einlesen, Codekarte, Board und Fristen fortschreiben,
# ausfuehrlicher Bericht an Discord (Fristen, Aufgaben, Mails als Kopierblock).
# Startet in GitHub Actions (.github/workflows/tageslauf.yml) und von Hand.
# Der lokale LaunchAgent (com.projectjlu.daily.plist) ist seit 23.11.2026 entladen und
# deaktiviert — zwei Scheduler am selben Tag erzeugen zwei Berichte und konkurrierende
# Commits.
set -uo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR/../.." || exit 1

# launchd startet mit minimalem PATH; pdftotext und pandoc liegen unter Homebrew.
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

LOG="$DIR/daily.log"
PY="$(command -v python3 || echo /usr/bin/python3)"
BEFORE=0
[ -f "$LOG" ] && BEFORE=$(wc -l < "$LOG" | tr -d ' ')

RC=0
FAILED=""
{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') ==="
  "$PY" "$DIR/ingest.py" || { RC=1; FAILED="ingest.py"; }
  echo "---"
  "$PY" "$DIR/graphify.py" || { RC=1; FAILED="${FAILED:+$FAILED, }graphify.py"; }
  echo "---"
  "$PY" "$DIR/board_sync.py" || { RC=1; FAILED="${FAILED:+$FAILED, }board_sync.py"; }
} >> "$LOG" 2>&1

# Ein gescheiterter Kernschritt muss sichtbar sein: Bericht mit ❌ und Exit ≠ 0.
echo "---" >> "$LOG"
if [ "$RC" -ne 0 ]; then
  echo "Kernschritt fehlgeschlagen: $FAILED"
  "$PY" "$DIR/discord_notify.py" --status fail --detail "$FAILED" >> "$LOG" 2>&1 || true
else
  "$PY" "$DIR/discord_notify.py" --status ok >> "$LOG" 2>&1 || true
fi

# Nur den Block dieses Laufs zeigen, damit Hinweise nicht aus dem Fenster fallen.
tail -n "+$((BEFORE + 1))" "$LOG"

exit "$RC"
