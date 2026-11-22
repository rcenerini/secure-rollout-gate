"""Verifica se os arquivos alterados no diff estao no Escopo da historia."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


BACKLOG_PATH = Path("docs/BACKLOG.md")
FIXED_FILES = {
    "docs/HANDOFF.md",
    "docs/USAGE-LOG.md",
    "docs/QUESTIONS.md",
}


class ScopeError(Exception):
    """Erro controlado durante a avaliacao do escopo."""


def parse_escopo(backlog_text: str, story_id: str) -> list[str]:
    """Extrai a lista de caminhos do campo Escopo de uma historia."""
    pattern = rf"^####\s+{re.escape(story_id)}\b"
    match = re.search(pattern, backlog_text, re.MULTILINE)
    if not match:
        raise ScopeError("historia inexistente")

    block_start = match.end()
    next_heading = re.search(r"^#{1,4}\s", backlog_text[block_start:], re.MULTILINE)
    if next_heading:
        block = backlog_text[block_start : block_start + next_heading.start()]
    else:
        block = backlog_text[block_start:]

    escopo_match = re.search(r"^-\s+\*\*Escopo:\*\*", block, re.MULTILINE)
    if not escopo_match:
        raise ScopeError("sem campo Escopo")

    pos = escopo_match.end()
    paths: list[str] = []
    for line in block[pos:].splitlines():
        if re.match(r"^\s*-\s+\*\*[^*]+:\*\*", line):
            break
        item = re.match(r"^\s*-\s+`([^`]+)`", line)
        if item:
            paths.append(item.group(1).strip())
        elif line.strip() and not re.match(r"^\s*-\s+", line):
            break

    if not paths:
        raise ScopeError("Escopo vazio")

    return paths


def _first_non_empty_line(text: str) -> str:
    """Retorna a primeira linha nao vazia de um texto."""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def get_changed_files() -> list[str]:
    """Retorna os arquivos alterados entre main e HEAD."""
    try:
        result = subprocess.run(
            [
                "git",
                "-c",
                "core.quotepath=false",
                "diff",
                "--no-renames",
                "--name-only",
                "main...HEAD",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=30,
            check=False,
        )
    except FileNotFoundError as exc:
        raise ScopeError("git nao encontrado") from exc
    except subprocess.TimeoutExpired as exc:
        raise ScopeError("git diff excedeu o tempo limite") from exc

    if result.returncode != 0:
        raise ScopeError(_first_non_empty_line(result.stderr) or "git diff falhou")

    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def check_scope(story_id: str) -> tuple[int, list[str]]:
    """Avalia o escopo e retorna o codigo de saida e as linhas de saida."""
    try:
        backlog_text = BACKLOG_PATH.read_text(encoding="utf-8")
    except OSError as exc:
        raise ScopeError(f"nao foi possivel ler {BACKLOG_PATH}: {exc}") from exc

    escopo = parse_escopo(backlog_text, story_id)
    changed = get_changed_files()

    allowed = set(escopo) | FIXED_FILES
    outsiders = [path for path in changed if path not in allowed]

    if outsiders:
        return 1, outsiders

    return 0, []


def main(argv: list[str] | None = None) -> int:
    """Ponto de entrada do script."""
    parser = argparse.ArgumentParser(
        description="Verifica se o diff esta no escopo da historia."
    )
    parser.add_argument("--story", required=True, help="ID da historia")
    args = parser.parse_args(argv)

    try:
        code, output = check_scope(args.story)
    except ScopeError as exc:
        print(f"nao avaliavel: {exc}", file=sys.stdout)
        return 2
    except Exception:  # pragma: no cover - protecao de ultima instancia
        print("nao avaliavel: erro inesperado", file=sys.stdout)
        return 2

    for line in output:
        print(line)

    return code


if __name__ == "__main__":
    sys.exit(main())
