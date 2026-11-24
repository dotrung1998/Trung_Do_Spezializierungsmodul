#!/usr/bin/env python3
"""Ausführlicher Tagesbericht an Discord — so vollständig, dass die Arbeit von dort läuft.

Der Webhook ist ein Geheimnis. Er wird hier gelesen, in dieser Reihenfolge:
  1. Umgebungsvariable DISCORD_WEBHOOK (so liest ihn GitHub Actions)
  2. Datei `~/.config/projektjlu/discord-webhook` (eigener Kanal)
  3. Datei `~/.config/projektplanung/discord-webhook` (Rückfall, vorhandener Kanal)
Fehlt alles, wird nichts gesendet. Der Webhook steht nie im Vault und nie im Repo.

Discord erlaubt 2000 Zeichen je Nachricht. Der Bericht besteht deshalb aus mehreren
Nachrichten:

  1. Lage: Lauf, Quellen, Board, was der Lauf geändert hat
  2. Fristen: alle Termine mit Abstand, Verantwortlichem und Begründung
  3. Aufgaben: offene Karten der Person und des Teams, Blockaden, offene Entscheidungen
  4. Mails: je eine Mail als **ein** Codeblock

Der Codeblock ist der Kern: Discord setzt daran einen Kopierknopf. Betreff und Text
stehen in demselben Block, damit ein Klick die ganze Mail in die Zwischenablage legt.

Aufruf:
    python3 Obsidian/_tools/discord_notify.py
    python3 Obsidian/_tools/discord_notify.py --dry-run
    python3 Obsidian/_tools/discord_notify.py --all --dry-run   # alle Mails zeigen
    python3 Obsidian/_tools/discord_notify.py --status fail --detail "ingest.py"
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
VAULT = TOOLS.parent
ROOT = VAULT.parent
NEU = VAULT / "00 Brain" / "Neu seit letztem Lauf.md"
BOARD = VAULT / "30 Plan" / "Board.md"
OFFEN = VAULT / "00 Brain" / "Offene Entscheidungen.md"
KOMM = VAULT / "50 Kommunikation"
REPORT = ROOT / "report"
FRISTEN = TOOLS / "fristen.json"
BOARDLOG = TOOLS / "board.log"
WEBHOOK_FILES = (
    Path.home() / ".config" / "projektjlu" / "discord-webhook",
    Path.home() / ".config" / "projektplanung" / "discord-webhook",
)

DRY = "--dry-run" in sys.argv
ALLES = "--all" in sys.argv
TITEL = "Spezialisierungsmodul Thema 29"
BETREUUNG = "sebastian.busse@admin.uni-giessen.de"

LIMIT = 2000      # Discord-Grenze je Nachricht
SAFE = 1900       # eigene Grenze für Textnachrichten (Reserve für Umbruch)
BLOCKMAX = 1988   # 2000 minus Codezäune und Zeilenumbrüche


def arg_value(name: str, default: str = "") -> str:
    if name in sys.argv:
        index = sys.argv.index(name)
        if index + 1 < len(sys.argv):
            return sys.argv[index + 1]
    return default


STATUS = arg_value("--status", "ok")
DETAIL = arg_value("--detail", "")
ALLOWED = (
    "https://discord.com/api/webhooks/",
    "https://canary.discord.com/api/webhooks/",
    "https://ptb.discord.com/api/webhooks/",
    "https://discordapp.com/api/webhooks/",
)


def webhook() -> str:
    url = os.environ.get("DISCORD_WEBHOOK", "").strip()
    if url:
        return url
    for path in WEBHOOK_FILES:
        try:
            return path.read_text(encoding="utf-8").strip()
        except OSError:
            continue
    return ""


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def grab(text: str, pattern: str, default: str = "") -> str:
    match = re.search(pattern, text)
    return match.group(1) if match else default


def fmt_datum(datum: str) -> str:
    """2026-11-26 -> 26.11.2026; 2026-11-27T11:00 -> 27.11.2026, 11:00."""
    try:
        stamp = datetime.fromisoformat(datum)
    except (TypeError, ValueError):
        return datum
    if len(datum) > 10:
        return stamp.strftime("%d.%m.%Y, %H:%M")
    return stamp.strftime("%d.%m.%Y")


def when(delta: int) -> str:
    if delta < 0:
        return f"überfällig seit {-delta} Tagen"
    if delta == 0:
        return "heute"
    if delta == 1:
        return "morgen"
    return f"in {delta} Tagen"


def days_until(datum: str) -> int | None:
    try:
        return (date.fromisoformat(datum[:10]) - date.today()).days
    except (TypeError, ValueError):
        return None


# --- Discord: Nachrichten bauen -------------------------------------------------

class Post:
    """Sammelt Text und bricht an der Discord-Grenze in eigene Nachrichten um."""

    def __init__(self) -> None:
        self.messages: list[str] = []
        self.buf: list[str] = []

    def line(self, text: str = "") -> None:
        if not text:
            if self.buf and self.buf[-1] != "":
                self.buf.append("")
            return
        if len("\n".join(self.buf + [text])) > SAFE:
            self.flush()
        self.buf.append(text)

    def lines(self, rows: list[str]) -> None:
        for row in rows:
            self.line(row)

    def flush(self) -> None:
        while self.buf and not self.buf[-1].strip():
            self.buf.pop()
        if self.buf:
            self.messages.append("\n".join(self.buf))
        self.buf = []

    def code(self, intro: list[str], text: str, note: str = "", lang: str = "") -> None:
        """Codeblock mit Kopierknopf; Einleitung und Hinweis stehen drumherum."""
        block = f"```{lang}\n{text.strip()}\n```"
        head = "\n".join(intro).strip()
        body = "\n\n".join(part for part in (head, block, note) if part)
        self.flush()
        if len(body) <= 1990:
            self.messages.append(body)
            return
        if head:
            self.messages.append(head)
        if len(block) + len(note) + 2 <= 1990:
            self.messages.append(block + ("\n" + note if note else ""))
            return
        if len(block) <= BLOCKMAX:
            self.messages.append(block)
            if note:
                self.messages.append(note)
            return
        # Sehr lange Mail: in nummerierte Blöcke teilen, jeder mit eigenem Knopf.
        chunks, current = [], ""
        for row in text.strip().splitlines():
            if len(current) + len(row) + 1 > BLOCKMAX - 40:
                chunks.append(current)
                current = row
            else:
                current = f"{current}\n{row}" if current else row
        if current:
            chunks.append(current)
        for index, chunk in enumerate(chunks, 1):
            self.messages.append(f"```{lang}\n{chunk}\n```\n`Teil {index}/{len(chunks)}`")
        if note:
            self.messages.append(note)

    def footer(self, text: str) -> None:
        """Details ans Ende der ersten Nachricht, sonst als eigene Nachricht."""
        self.flush()
        if self.messages and len(self.messages[0]) + len(text) + 2 <= LIMIT - 20:
            self.messages[0] += "\n\n" + text
        else:
            self.messages.append(text)


# --- Quellen und Board ----------------------------------------------------------

def neu_abschnitt(text: str, titel: str) -> list[str]:
    match = re.search(rf"^## {titel}.*?\n(.*?)(?=\n## )", text, re.M | re.S)
    if not match:
        return []
    return [m.strip() for m in re.findall(r"^- `([^`]+)`", match.group(1), re.M)]


def board_cards() -> list[dict]:
    cards: list[dict] = []
    lane = ""
    for line in read(BOARD).splitlines():
        head = re.match(r"^##\s+(.+?)\s*$", line)
        if head:
            lane = head.group(1)
            continue
        match = re.match(r"^- \[([ xX])\] (.+)$", line)
        if not match:
            continue
        rest = match.group(2)
        bold = re.match(r"^\*\*(.+?)\*\*(?:\s*(.*))?$", rest)
        if bold:
            title_part, tail = bold.group(1), bold.group(2) or ""
        else:
            title_part, tail = rest, ""
        if " · " in title_part:
            cid, titel = title_part.split(" · ", 1)
        else:
            cid, titel = title_part.split(" ", 1)[0], title_part
        tail = tail.split("→")[0]

        def note(key: str) -> str:
            found = re.search(rf"·\s*{key}:\s*([^·]+?)(?=\s*·|$)", tail)
            return found.group(1).strip() if found else ""

        due = re.search(r"fällig:?\s*(\d{4}-\d{2}-\d{2})", tail)
        released = re.search(r"·\s*freigegeben durch\s+([^·]+?)(?=\s*·|$)", tail)
        cards.append(
            {
                "id": cid.strip(),
                "titel": titel.strip(),
                "lane": lane,
                "offen": match.group(1) != "x" and lane != "Done",
                "tag": grab(tail, r"#(person|team|ai)\b"),
                "due": due.group(1) if due else "",
                "blockiert": note("blockiert"),
                "wartet": note("wartet"),
                "offen_note": note("offen"),
                "freigegeben": released.group(1).strip() if released else "",
            }
        )
    return cards


def board_ereignisse() -> list[str]:
    today = date.today().isoformat()
    rows = [l for l in read(BOARDLOG).splitlines() if l.startswith(f"[{today}")]
    if not rows:
        return []
    return [part.strip() for part in rows[-1].split(" | ") if part.strip()]


def offene_todos() -> int | None:
    if not REPORT.exists():
        return None
    count = 0
    for path in REPORT.rglob("*.tex"):
        count += len(re.findall(r"\\todo\{", read(path)))
    return count


def entscheidungen() -> list[tuple[str, str]]:
    text = read(OFFEN)
    out: list[tuple[str, str]] = []
    for match in re.finditer(r"^## (\d+)\. (.+)$", text, re.M):
        start = match.end()
        rest = text[start:]
        nxt = re.search(r"^## \d+\. ", rest, re.M)
        block = rest[: nxt.start()] if nxt else rest
        empfehlung = re.search(r"\*\*Empfehlung:\s*(.+?)\*\*", block, re.S)
        rec = re.sub(r"\s+", " ", empfehlung.group(1)).strip() if empfehlung else ""
        if rec:
            sentence = re.split(r"(?<=\.)\s", rec, maxsplit=1)[0]
            rec = sentence if len(sentence) > 40 else rec
            if len(rec) > 220:
                rec = rec[:217].rstrip() + "…"
        out.append((f"{match.group(1)}. {match.group(2).strip()}", rec))
    return out


# --- Mails ----------------------------------------------------------------------

def md_mail(path: Path) -> str:
    """Liest den Brief aus einer Notiz: von '**Betreff:**' bis zur Trennlinie."""
    text = read(path)
    start = text.find("**Betreff:**")
    if start == -1:
        return ""
    rows: list[str] = []
    for line in text[start:].splitlines():
        if line.strip() == "---":
            break
        rows.append(line)
    return "\n".join(rows).replace("**", "").strip()


def mail_text(nummer: int, notiz: str) -> str:
    """Versandfertige .txt hat Vorrang vor der Notiz im Vault."""
    direct = ROOT / f"E-Mail-{nummer}-versandfertig.txt"
    text = read(direct)
    return text.strip() if text.strip() else md_mail(KOMM / notiz)


def shield(text: str) -> str:
    """Personendaten bleiben Platzhalter — auch im Discord-Kanal.

    Die versandfertige Datei liegt lokal und kann eine echte Matrikelnummer
    enthalten. Sie gehört nicht in einen Discord-Verlauf; lange Zahlenfolgen
    werden deshalb vor dem Senden durch den Platzhalter ersetzt.
    """
    return re.sub(r"\b\d{6,}\b", "[Matrikelnummer]", text)


def fristen() -> list[dict]:
    try:
        items = json.loads(read(FRISTEN))
    except ValueError:
        return []
    return sorted(items, key=lambda item: item.get("datum", ""))


def zuteilung_datum() -> str:
    for item in fristen():
        if item.get("id") == "ZUTEILUNG":
            return item.get("datum", "")[:10]
    return "2026-11-27"


def build() -> list[str]:
    post = Post()
    neu = read(NEU)
    jetzt = datetime.now().strftime("%d.%m.%Y, %H:%M")
    lauf_tag = grab(neu, r"(?m)^Lauf:\s*(\d{4}-\d{2}-\d{2})")
    frisch = lauf_tag == date.today().isoformat()

    # 1. Lage ----------------------------------------------------------------
    if STATUS == "fail":
        post.line(f"❌ **{TITEL} · Tageslauf {jetzt} fehlgeschlagen**")
        post.line(f"Kernschritt: {DETAIL or 'unbekannt'} — der Bericht kann veraltet sein.")
    else:
        post.line(f"**{TITEL} · Tageslauf {jetzt}**")
    post.line()

    gesamt = grab(neu, r"Quellen gesamt:\s*\*\*(\d+)\*\*", "?")
    unbekannt = grab(neu, r"\*\*unbekannt:\s*(\d+)\*\*", "?")
    notiz = grab(neu, r"durch Notiz:\s*(\d+)", "?")
    unbekannt_teil = f"{unbekannt} unbekannt ✅" if unbekannt in ("0",) else f"⚠️ {unbekannt} unbekannt"
    post.line(f"**Quellen** · {gesamt} gesamt · {notiz} mit Notiz · {unbekannt_teil}")

    cards = board_cards()
    done = sum(1 for card in cards if not card["offen"])
    total = len(cards)
    todos = offene_todos()
    bericht = f" · Bericht: {todos} offene `\\todo`" if todos is not None else ""
    post.line(f"**Board** · {done}/{total} Karten erledigt{bericht}")

    # Die Notiz wird nur bei Quellenänderung neu geschrieben. Ist ihr Datum älter als
    # heute, gab es heute nichts einzulesen — dann ist ihre "Geändert"-Liste Historie.
    if frisch:
        neu_liste = neu_abschnitt(neu, r"Neu \(\d+\)")
        geaendert = neu_abschnitt(neu, r"Geändert \(\d+\)")
        if neu_liste:
            post.line("**Neu eingelesen** · " + ", ".join(f"`{p}`" for p in neu_liste[:5])
                      + (f" (+{len(neu_liste) - 5})" if len(neu_liste) > 5 else ""))
        if geaendert:
            post.line("**Geändert** · " + ", ".join(f"`{p}`" for p in geaendert[:4])
                      + (f" … (+{len(geaendert) - 4} weitere)" if len(geaendert) > 4 else ""))
        if not neu_liste and not geaendert:
            post.line("**Änderungen** · keine neuen oder geänderten Quellen")
    elif lauf_tag:
        post.line(f"**Änderungen** · heute keine (letzte Quellenänderung: {fmt_datum(lauf_tag)})")
    else:
        post.line("**Änderungen** · unbekannt — `ingest.py` prüfen")
    if unbekannt not in ("0", "?"):
        post.line(f"⚠️ **Quellen ohne Notiz** — `ingest.py` prüfen, der Lauf zählt sie als unbekannt.")

    events = board_ereignisse()
    post.line()
    post.line("**Was der Lauf geändert hat**")
    if events:
        for event in events[:8]:
            post.line(f"• {event}")
        if len(events) > 8:
            post.line(f"• … {len(events) - 8} weitere (Board-Log)")
    else:
        post.line("• keine Änderung — Board und Status sind unverändert")

    # 2. Fristen -------------------------------------------------------------
    post.flush()
    post.line("**Fristen**")
    for item in fristen():
        datum = item.get("datum", "")
        delta = days_until(datum)
        if delta is None:
            continue
        mark = "🔴" if delta < 0 else "🟠" if delta <= 3 else "•"
        post.line(
            f"{mark} **{fmt_datum(datum)}** · {when(delta)} · "
            f"{item.get('titel', '?')} · {item.get('wer', '?')}"
        )
        detail = (item.get("detail") or "").strip()
        if detail and delta <= 30:
            post.line(f"   ↳ {detail}")

    # 3. Aufgaben ------------------------------------------------------------
    post.flush()
    person = [c for c in cards if c["offen"] and c["tag"] == "person"]
    team = [c for c in cards if c["offen"] and c["tag"] == "team"]
    person.sort(key=lambda c: (c["due"] or "9999", c["lane"] != "Doing"))
    team.sort(key=lambda c: (c["due"] or "9999", c["lane"] != "Doing"))

    post.line("**Zu tun · Person**")
    if person:
        for card in person[:10]:
            suffix = ""
            if card["due"]:
                delta = days_until(card["due"])
                if delta is not None:
                    suffix = f" — fällig {fmt_datum(card['due'])} ({when(delta)})"
            post.line(f"• **{card['id']}** · {card['titel']}{suffix}")
            for key in ("wartet", "blockiert", "offen_note"):
                if card[key]:
                    post.line(f"   ↳ {key}: {card[key]}")
    else:
        post.line("• nichts offen")

    if team:
        post.line()
        post.line("**Team Gamma**")
        for card in team[:10]:
            post.line(f"• **{card['id']}** · {card['titel']}" + (f" · {card['freigegeben']}" if card["freigegeben"] else ""))

    groups: dict[str, list[str]] = {}
    for card in cards:
        if card["offen"] and card["blockiert"]:
            key = card["blockiert"].replace(" offen", "").strip()
            groups.setdefault(key, []).append(card["id"])
    if groups:
        post.line()
        post.line("**Blockiert (wartet auf Messdaten)**")
        for blocker, ids in list(groups.items())[:6]:
            post.line(f"• {blocker} offen → {', '.join(ids)}")

    decisions = entscheidungen()
    if decisions:
        post.line()
        post.line("**Offene Entscheidungen (nur du)**")
        for titel, rec in decisions[:5]:
            post.line(f"• {titel}")
            if rec:
                post.line(f"   ↳ {rec}")

    # 4. Mails ---------------------------------------------------------------
    heute = date.today().isoformat()
    zuteilung = zuteilung_datum()
    nach_zuteilung = ALLES or heute >= zuteilung
    done_ids = {c["id"] for c in cards if not c["offen"]}

    mail1 = shield(mail_text(1, "E-Mail 1 – Themenwünsche.md"))
    if mail1 and (ALLES or "MAIL1" not in done_ids):
        frist = next((i.get("datum", "") for i in fristen() if i.get("id") == "MAIL1"), "")
        delta = days_until(frist) if frist else None
        note = f"An: {BETREUUNG}"
        if delta is not None:
            note += f" · Frist {fmt_datum(frist)} ({when(delta)})"
        note += (
            " · ersetzen: `[Matrikelnummer]`, `[HRZ-Kennung]` — "
            "„Kopieren“ übernimmt Betreff und Text."
        )
        post.code(["**Mail 1 · Themenwünsche an Dr. Busse**"], mail1, note)

    mail2 = shield(mail_text(2, "E-Mail 2 – Kurzexposé.md"))
    if mail2 and (ALLES or ("MAIL2" not in done_ids and nach_zuteilung)):
        post.code(
            ["**Mail 2 · Kurzexposé an Dr. Busse**"],
            mail2,
            f"An: {BETREUUNG} · Anhang `expose.pdf` (1 Seite) · ersetzen: `[Datum]`, "
            "`[3.1 Konsistenz über Quellen]` — erst nach der Zuteilung senden.",
        )

    team_mail = shield(md_mail(KOMM / "E-Mail an Team Gamma.md"))
    if team_mail and (ALLES or nach_zuteilung):
        post.code(
            ["**Mail an Team Gamma · gemeinsamer Quellenstand**"],
            team_mail,
            "An: die vier anderen aus Team Gamma (Adressen nach der Zuteilung) · "
            "ersetzen: `[Vorname Nachname]` — erst nach der Zuteilung senden.",
        )

    post.footer("Details: `Obsidian/00 Brain/Status.md` · `Obsidian/30 Plan/Board.md` · `Obsidian/50 Kommunikation/`")
    post.flush()
    return post.messages


# --- Versand --------------------------------------------------------------------

def post(url: str, content: str) -> int:
    body = json.dumps(
        {
            "content": content[:LIMIT],
            "username": TITEL,
            "allowed_mentions": {"parse": []},
        },
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "ProjektJLU-Notifier"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return response.status


def send_all(url: str, messages: list[str]) -> list[int]:
    codes = []
    for index, content in enumerate(messages):
        if index:
            time.sleep(1.0)  # Webhook-Limit: 5 Nachrichten je 2 Sekunden
        try:
            codes.append(post(url, content))
        except urllib.error.HTTPError as exc:
            if exc.code != 429:
                raise
            try:
                wait = float(json.loads(exc.read().decode("utf-8", "replace")).get("retry_after", 2))
            except (ValueError, TypeError):
                wait = 2.0
            time.sleep(min(5.0, wait + 0.2))
            codes.append(post(url, content))
    return codes


def main() -> int:
    messages = build()
    if not messages:
        print("Discord: nichts zu berichten")
        return 0

    over = [i for i, m in enumerate(messages, 1) if len(m) > LIMIT]
    if over:
        print(f"Discord: Nachricht {over} überschreitet {LIMIT} Zeichen, nicht gesendet")
        return 1

    url = webhook()
    if DRY:
        for index, content in enumerate(messages, 1):
            print(f"===== Nachricht {index}/{len(messages)} · {len(content)} Zeichen =====")
            print(content)
            print()
        if not url:
            print("Discord: kein Webhook hinterlegt, nicht gesendet.")
        return 0

    if not url:
        print("Discord: übersprungen (kein Webhook hinterlegt)")
        return 0

    if not url.startswith(ALLOWED):
        print("Discord: Adresse ist keine Discord-Webhook-Adresse, nicht gesendet")
        return 1

    try:
        codes = send_all(url, messages)
        print(f"Discord: gesendet ({len(messages)} Nachrichten, HTTP {'/'.join(str(c) for c in codes)})")
        return 0
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:200]
        print(f"Discord: Fehler HTTP {exc.code} {detail}")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"Discord: Fehler {exc}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
