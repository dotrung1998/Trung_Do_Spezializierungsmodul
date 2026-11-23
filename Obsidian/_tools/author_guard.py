#!/usr/bin/env python3
"""Erzwingt den erlaubten Commit-Autor und verbietet Bot-/Co-Author-Trailer.

Erlaubt ist genau ein Autor (Standard: Trung Do <dotrung1998@gmail.com>),
änderbar über AUTHOR_NAME / AUTHOR_EMAIL. Verboten sind Co-Authored-By- und
verwandte Trailer-Zeilen, Bot-Adressen sowie Bot- und Werkzeugnamen in der
Commit-Nachricht.

Der Hook `.githooks/commit-msg` ruft dieses Skript mit --message-file auf und
bricht den Commit bei einem Treffer ab. Dieselben Regeln prüfen die Commits im
Workflow `.github/workflows/author-guard.yml`.

Verwendung:
    python3 Obsidian/_tools/author_guard.py --commit HEAD
    python3 Obsidian/_tools/author_guard.py --range origin/main..HEAD
    python3 Obsidian/_tools/author_guard.py --config
    python3 Obsidian/_tools/author_guard.py --message-file .git/COMMIT_EDITMSG --config
"""

from __future__ import annotations

import os
import re
import subprocess
import sys

ALLOWED_NAME = os.environ.get("AUTHOR_NAME", "Trung Do")
ALLOWED_EMAIL = os.environ.get("AUTHOR_EMAIL", "dotrung1998@gmail.com")
FORBIDDEN_NAMES = {"projektjlu", "projektplanung", "buffy", "codebuff", "claude"}

# Trailer-Zeilen, die einen zweiten Autor oder ein Werkzeug ausweisen.
TRAILER = re.compile(
    r"(?i)^[ \t>#*_-]*("
    r"co-authored-by|co-authored\s+by|coauthored-by|co-author|"
    r"generated\s+(?:with|by)|generated-by|"
    r"assisted\s+by|assisted-by|"
    r"written\s+by\s+(?:ai|an?\s+ai|a\s+bot)|"
    r"ai[-\s]assisted|ai[-\s]generated|"
    r"made\s+with|created\s+with|powered\s+by"
    r")\s*:"
)

# Bot- und Werkzeugnamen, Bot-Adressen und das Roboter-Emoji.
BOT_TOOL = re.compile(
    r"(?i)\b(?:codebuff|buffy|claude|anthropic|chatgpt|openai|copilot|codex|aider)\b"
    r"|\[\s*bot\s*\]"
    r"|noreply@(?:anthropic|openai)\.com"
    r"|\U0001F916"
)

RULES = (
    ("Trailer-Zeile (Co-Authored-By o. Ä.)", TRAILER),
    ("Bot-/Werkzeug-Hinweis", BOT_TOOL),
)
ZERO = re.compile(r"^0+$")


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], capture_output=True, text=True)


def check_message(label: str, message: str) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for line in message.splitlines():
        text = line.strip()
        hits = [rule for rule, pattern in RULES if pattern.search(line)]
        if hits and text not in seen:
            seen.add(text)
            errors.append(f"{label}: {' / '.join(hits)}: {text!r}")
    return errors


def check_commit(sha: str) -> list[str]:
    out = git("show", "-s", "--format=%an%x00%ae%x00%cn%x00%B", sha)
    if out.returncode != 0:
        return [f"{sha}: Commit nicht lesbar: {out.stderr.strip()}"]
    name, email, committer, message = out.stdout.split("\x00", 3)
    errors: list[str] = []
    if name != ALLOWED_NAME or email != ALLOWED_EMAIL:
        errors.append(
            f"{sha[:7]}: Autor {name} <{email}> ist nicht {ALLOWED_NAME} <{ALLOWED_EMAIL}>"
        )
    if name.lower() in FORBIDDEN_NAMES or committer.lower() in FORBIDDEN_NAMES:
        errors.append(f"{sha[:7]}: Bot-/Tool-Name als Autor/Committer ({name} / {committer})")
    errors += check_message(sha[:7], message)
    return errors


def check_config() -> list[str]:
    name = git("config", "user.name").stdout.strip()
    email = git("config", "user.email").stdout.strip()
    if name != ALLOWED_NAME or email != ALLOWED_EMAIL:
        return [
            f"git config user.name/email ist {name} <{email}>, "
            f"erlaubt ist {ALLOWED_NAME} <{ALLOWED_EMAIL}>"
        ]
    return []


def commits_in_range(rev_range: str) -> tuple[list[str], str | None]:
    out = git("rev-list", "--reverse", rev_range)
    if out.returncode != 0:
        start = rev_range.split("..", 1)[0]
        if ZERO.fullmatch(start or ""):
            head = git("rev-parse", "HEAD").stdout.strip()
            return ([head] if head else []), None
        return [], out.stderr.strip()
    return out.stdout.split(), None


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--range", dest="rev_range")
    parser.add_argument("--commit")
    parser.add_argument("--message-file")
    parser.add_argument("--config", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    if args.message_file:
        try:
            message = open(args.message_file, encoding="utf-8", errors="replace").read()
        except OSError as exc:
            print(f"author_guard: Nachricht nicht lesbar: {exc}", file=sys.stderr)
            return 1
        errors += check_message("Nachricht", message)
    if args.config:
        errors += check_config()
    if args.rev_range:
        shas, err = commits_in_range(args.rev_range)
        if err:
            errors.append(f"git rev-list {args.rev_range} fehlgeschlagen: {err}")
        for sha in shas:
            errors += check_commit(sha)
    elif args.commit:
        errors += check_commit(args.commit)
    elif not args.message_file and not args.config:
        errors += check_commit("HEAD")

    if errors:
        print("author_guard: FEHLGESCHLAGEN", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        print('Regel: AGENTS.md, Abschnitt "Harte Regeln".', file=sys.stderr)
        return 1
    print("author_guard: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
