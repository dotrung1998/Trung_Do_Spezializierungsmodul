#!/usr/bin/env python3
"""Erzeugt '10 Thema/Codekarte.md' — eine Mermaid-Karte des Code-Repos.

Die Karte kommt ohne zusätzliche Notizen aus: keine Wikilinks auf Code, sondern ein
Mermaid-Diagramm, das Obsidian direkt rendert. Damit erscheint der Code im Graph nicht
als Haufen toter Links, sondern als lesbare Struktur in einer Notiz.

Sobald das Repo der Einzelarbeit existiert, wird die Karte bei jedem Lauf neu erzeugt
(taeglich ueber _tools/daily.sh). Existiert noch kein Code, schreibt das Skript eine
Notiz mit Hinweis statt einer leeren Karte.

Aufruf:
    python3 Obsidian/_tools/graphify.py
"""

from __future__ import annotations

import ast
import re
from datetime import datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
ROOT = VAULT.parent
OUT = VAULT / "10 Thema" / "Codekarte.md"

SKIP_DIRS = {
    ".git", ".venv", "venv", "__pycache__", ".ipynb_checkpoints",
    "node_modules", ".mypy_cache", ".pytest_cache", "data", "runs", "build", "dist",
}
CANDIDATES = [
    ROOT / "gamma-3-1-konsistenz",
    ROOT / "src",
    ROOT / "code",
]
MAX_MODULES = 80


def python_files(repo: Path) -> list[Path]:
    found = []
    for p in sorted(repo.rglob("*.py")):
        rel = p.relative_to(repo)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        found.append(p)
    return found


def find_repo() -> tuple[Path | None, list[Path]]:
    for c in CANDIDATES:
        if c.is_dir():
            files = python_files(c)
            if files:
                return c, files
    return None, []


def module_name(path: Path, files: list[Path]) -> str:
    """Kuerzester eindeutiger Modulname: Pfad ohne Endung, __init__ entfernt."""
    for base in {p.parent for p in files}:
        try:
            rel = path.relative_to(base)
        except ValueError:
            continue
        parts = [x for x in rel.with_suffix("").parts if x != "__init__"]
        if parts:
            return ".".join(parts)
    return path.stem


def analyse(path: Path) -> dict:
    info = {"lines": 0, "classes": [], "functions": [], "imports": set(), "doc": False}
    try:
        source = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return info
    info["lines"] = source.count("\n") + 1
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return info
    info["doc"] = ast.get_docstring(tree) is not None
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            info["classes"].append(node.name)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            info["functions"].append(node.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                info["imports"].add(alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            info["imports"].add(node.module)
    return info


def node_id(name: str) -> str:
    return "n_" + re.sub(r"\W", "_", name)


def build_map(repo: Path, files: list[Path]) -> str:
    names = {module_name(p, files): p for p in files}
    infos = {name: analyse(p) for name, p in names.items()}
    order = sorted(names)

    edges: list[tuple[str, str]] = []
    for name in order:
        for imported in infos[name]["imports"]:
            if imported in names and imported != name:
                edges.append((name, imported))
            else:
                for candidate in names:
                    if candidate != name and candidate.endswith("." + imported.split(".")[-1]):
                        if imported.startswith(candidate.rsplit(".", 1)[0]):
                            edges.append((name, candidate))
                            break
    seen = set()
    unique_edges = []
    for e in edges:
        if e not in seen:
            seen.add(e)
            unique_edges.append(e)
    unique_edges = unique_edges[:200]

    lines = ["```mermaid", "graph TD"]
    for name in order[:MAX_MODULES]:
        label = name.replace('"', "'")
        lines.append(f'    {node_id(name)}["{label}"]')
    for src, dst in unique_edges:
        lines.append(f"    {node_id(src)} --> {node_id(dst)}")
    lines.append("```")
    return "\n".join(lines)


def build_table(repo: Path, files: list[Path]) -> str:
    names = {module_name(p, files): p for p in files}
    rows = ["| Modul | Zeilen | Klassen | Funktionen | Docstring |",
            "|---|---:|---|---|---|"]
    for name in sorted(names):
        info = analyse(names[name])
        k = ", ".join(info["classes"]) or "—"
        f = ", ".join(info["functions"]) or "—"
        rows.append(
            f"| `{name}` | {info['lines']} | {k} | {f} | "
            f"{'ja' if info['doc'] else '**nein**'} |"
        )
    return "\n".join(rows)


def write_note(body: str, frontmatter_extra: str = "") -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    OUT.write_text(
        "---\n"
        'titel: "Codekarte"\n'
        f"stand: {datetime.now():%Y-%m-%d}\n"
        "automatisch: true\n"
        f"{frontmatter_extra}"
        "---\n\n"
        f"> Automatisch erzeugt von `Obsidian/_tools/graphify.py` am {stamp}.\n"
        "> Nicht von Hand bearbeiten — der nächste Lauf überschreibt die Datei.\n\n"
        + body,
        encoding="utf-8",
    )


def main() -> int:
    repo, files = find_repo()
    if repo is None:
        write_note(
            "# Codekarte\n\n"
            "**Noch kein Code vorhanden.** Die Karte entsteht automatisch, sobald eines\n"
            "dieser Verzeichnisse Python-Dateien enthält:\n\n"
            "- `gamma-3-1-konsistenz/` (das Repo der Einzelarbeit)\n"
            "- `src/`\n"
            "- `code/`\n\n"
            "Warum das hier steht: Der Graph in Obsidian zeigt Notizen. Code erscheint nur,\n"
            "wenn ihn jemand in eine Notiz übersetzt. Diese Karte macht das automatisch —\n"
            "als Mermaid-Diagramm der Module und ihrer Importe, ohne tote Wikilinks.\n"
        )
        print("Codekarte: kein Code gefunden, Platzhalter geschrieben.")
        return 0

    body = (
        "# Codekarte\n\n"
        f"Quelle: `{repo.name}/` — {len(files)} Python-Dateien.\n\n"
        "## Struktur\n\n"
        + build_map(repo, files)
        + "\n\n## Module\n\n"
        + build_table(repo, files)
        + "\n\n## Lesart\n\n"
        "Kanten sind Importe innerhalb des Repos. Ein Modul ohne eingehende Kante ist ein\n"
        "Einstiegspunkt (Skript, CLI, Pipeline). Ein Modul ohne Docstring ist eine offene\n"
        "Baustelle — die Spalte ist absichtlich so streng.\n"
    )
    write_note(body)
    print(f"Codekarte: {len(files)} Module aus {repo.name}/ geschrieben.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
