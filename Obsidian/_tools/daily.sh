#!/bin/bash
# Taeglicher Lauf: Quellen einlesen, Codekarte neu erzeugen.
# Wird von launchd gestartet (com.projectjlu.daily), kann aber auch von Hand laufen.
set -uo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR/../.." || exit 1

LOG="$DIR/daily.log"
PY="$(command -v python3 || echo /usr/bin/python3)"

{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') ==="
  "$PY" "$DIR/ingest.py"
  echo "---"
  "$PY" "$DIR/graphify.py"
} >> "$LOG" 2>&1

tail -n 14 "$LOG"
