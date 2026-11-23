#!/bin/bash
# Holt einen verpassten Tageslauf nach — nur für den lokalen LaunchAgent.
#
# Der Agent (com.projectjlu.daily.plist) startet dieses Skript bei Login und alle
# 30 Minuten; es startet daily.sh nur, wenn in daily.log noch kein Lauf von heute
# steht. Damit wird ein Lauf nachgeholt, der wegen Schlaf oder ausgeschaltetem
# Rechner ausfiel. In GitHub Actions wird dieses Skript NICHT benutzt: der Cron im
# Workflow ist der Scheduler.
#
# Kein eigenes Zustandsfile: die Quelle der Wahrheit ist daily.log selbst.
set -uo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR/../.." || exit 1

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

LOG="$DIR/daily.log"
TODAY="$(date '+%Y-%m-%d')"

# Heute schon gelaufen? Dann nichts tun — auch nach einem Fehllauf kein Retry-Sturm.
if [ -f "$LOG" ] && grep -q "^=== $TODAY " "$LOG"; then
  exit 0
fi

echo "Guard: kein Lauf für $TODAY, hole nach ($(date '+%H:%M'))"
/bin/bash "$DIR/daily.sh"
RC=$?
echo "Guard: Nachhol-Lauf rc=$RC"
exit "$RC"
