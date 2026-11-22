"""Verifica se os arquivos alterados no diff estão dentro do escopo da história."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

FIXED_ALLOWLIST = {
    "docs/HANDOFF.md",
    "docs/USAGE-LOG.md",
    "docs/QUESTIONS.md",
}

BACKLOG_PATH = Path(__file__).resolve().parents[1] / "docs" / "BACKLOG.md"
STORY_HEADING_RE = re.compile(r"^####\s+(S\d+\.\d+)\b")
HEADING_RE = re.compile(r"^#{1,4}\s+")
ESCOPE_FIELD_RE = re.compile(r"^-\s+\*\*Escopo:\*\*")
PATH_RE = re.compile(r"`([^`]+)`")
FIELD_RE = re.compile(r"^-\s+\*\*")


def read_backlog(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_git_diff() -> list[str]:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        ["git", "diff", "--name-only", "main...HEAD"],
        capture_output=True,
        text=True,
        shell=False,
        cwd=root,
    )
    if result.returncode != 0:
        print(f"Erro ao executar git diff: {result.stderr.strip()}", file=sys.stderr)
        raise SystemExit(1)
    return [line for line in result.stdout.splitlines() if line]


def find_story_block(content: str, story_id: str) -> str | None:
    lines = content.splitlines()
    start = None
    for index, line in enumerate(lines):
        match = STORY_HEADING_RE.match(line)
        if match and match.group(1) == story_id:
            start = index
            break
    if start is None:
        return None

    end = len(lines)
    for index in range(start + 1, len(lines)):
        if HEADING_RE.match(lines[index]):
            end = index
            break

    return "\n".join(lines[start:end])


def parse_escopo(block: str) -> list[str] | None:
    lines = block.splitlines()
    escopo_start = None
    for index, line in enumerate(lines):
        if ESCOPE_FIELD_RE.match(line):
            escopo_start = index
            break
    if escopo_start is None:
        return None

    escopo_lines = [lines[escopo_start]]
    for line in lines[escopo_start + 1 :]:
        if FIELD_RE.match(line):
            break
        escopo_lines.append(line)

    paths: list[str] = []
    seen: set[str] = set()
    for line in escopo_lines:
        for match in PATH_RE.finditer(line):
            path = match.group(1)
            if path not in seen:
                seen.add(path)
                paths.append(path)

    return paths if paths else None


def evaluate(scope: set[str], changed: list[str], fixed: set[str]) -> list[str]:
    allowed = scope | fixed
    return [path for path in changed if path not in allowed]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verifica se o diff está dentro do escopo da história."
    )
    parser.add_argument("--story", required=True, help="ID da história (ex: S1.8)")
    args = parser.parse_args(argv)

    story_id = args.story.strip()
    if not story_id:
        print("Erro: --story não pode ser vazio.", file=sys.stderr)
        return 2

    try:
        content = read_backlog(BACKLOG_PATH)
    except OSError as exc:
        print(f"Erro ao ler backlog: {exc}", file=sys.stderr)
        return 2

    block = find_story_block(content, story_id)
    if block is None:
        print(f"História {story_id} não encontrada em {BACKLOG_PATH}.", file=sys.stderr)
        return 2

    escopo = parse_escopo(block)
    if escopo is None:
        print(
            f"História {story_id} não possui campo Escopo ou ele está vazio.",
            file=sys.stderr,
        )
        return 2

    changed = run_git_diff()
    fora = evaluate(set(escopo), changed, FIXED_ALLOWLIST)
    if fora:
        print("Arquivos fora do escopo:")
        for path in fora:
            print(path)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
