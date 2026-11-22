"""Testes caixa-preta para scripts/check_scope.py com repositorios git reais."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_scope.py"

BACKLOG = """# BACKLOG

#### S1.1 · Historia com escopo
- **Tier:** T2
- **Saída:** codigo e testes
- **Escopo:**
  - `scripts/check_scope.py`
  - `tests/test_check_scope.py`
- **Interface:** python scripts/check_scope.py --story <ID>

#### S1.2 · Historia com decisoes e fontes
- **Tier:** T2
- **Saída:** documentos
- **Escopo:**
  - `docs/DECISOES.md`
  - `docs/refs/SOURCES.md`
- **Interface:** nenhuma

#### S1.3 · Historia sem escopo
- **Tier:** T2
- **Saída:** nada
- **Interface:** nenhuma

#### S1.4 · Historia com escopo vazio
- **Tier:** T2
- **Saída:** nada
- **Escopo:**
- **Interface:** nenhuma

#### S1.5 · Historia com fonte exata
- **Tier:** T2
- **Saída:** fonte
- **Escopo:**
  - `docs/refs/SOURCES.md`
- **Interface:** nenhuma

#### S1.80 · Proxima historia
- **Tier:** T2
- **Saída:** outro arquivo
- **Escopo:**
  - `docs/other.md`
- **Interface:** nenhuma
"""


def run_script(cwd: Path, story_id: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--story", story_id],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        stdin=subprocess.DEVNULL,
    )


def _git(repo: Path, *args: str) -> None:
    subprocess.run(
        ["git", *args],
        cwd=str(repo),
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        stdin=subprocess.DEVNULL,
    )


def git_init(repo: Path, branch: str = "main") -> None:
    _git(repo, "init")
    _git(repo, "checkout", "-b", branch)
    _git(repo, "config", "user.name", "Test")
    _git(repo, "config", "user.email", "test@example.local")


def write_backlog(repo: Path) -> None:
    path = repo / "docs" / "BACKLOG.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(BACKLOG, encoding="utf-8")


def commit_file(repo: Path, relpath: str, content: str, message: str) -> None:
    path = repo / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    _git(repo, "add", relpath)
    _git(repo, "commit", "-m", message)


def base_repo(tmp_path: Path, branch: str = "main") -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    git_init(repo, branch)
    write_backlog(repo)
    commit_file(repo, "docs/ARQUITETURA.md", "arquitetura\n", "init")
    return repo


def test_dentro_do_escopo_retorna_0(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "scripts/check_scope.py", "codigo\n", "adiciona script")
    commit_file(repo, "tests/test_check_scope.py", "teste\n", "adiciona teste")

    result = run_script(repo, "S1.1")

    assert result.returncode == 0
    assert result.stdout.strip() == ""


def test_fora_do_escopo_retorna_1_listando_infrator(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "docs/DECISOES.md", "decisao\n", "adiciona decisao")

    result = run_script(repo, "S1.1")

    assert result.returncode == 1
    assert result.stdout.strip() == "docs/DECISOES.md"


def test_historia_sem_escopo_retorna_2(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "scripts/check_scope.py", "codigo\n", "adiciona script")

    result = run_script(repo, "S1.3")

    assert result.returncode == 2
    assert "sem campo Escopo" in result.stdout


def test_sem_branch_main_retorna_2(tmp_path: Path) -> None:
    repo = base_repo(tmp_path, branch="trunk")
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "scripts/check_scope.py", "codigo\n", "adiciona script")

    result = run_script(repo, "S1.1")

    assert result.returncode == 2
    assert "nao avaliavel:" in result.stdout


def test_somente_lista_fixa_retorna_0(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "docs/HANDOFF.md", "handoff\n", "atualiza handoff")

    result = run_script(repo, "S1.1")

    assert result.returncode == 0
    assert result.stdout.strip() == ""


def test_decisoes_e_sources_no_escopo_retorna_0(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "docs/DECISOES.md", "decisao\n", "adiciona decisao")
    commit_file(repo, "docs/refs/SOURCES.md", "fonte\n", "adiciona fonte")

    result = run_script(repo, "S1.2")

    assert result.returncode == 0
    assert result.stdout.strip() == ""


def test_historia_inexistente_retorna_2(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "scripts/check_scope.py", "codigo\n", "adiciona script")

    result = run_script(repo, "S99.99")

    assert result.returncode == 2
    assert "historia inexistente" in result.stdout


def test_diff_vazio_retorna_0(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)

    result = run_script(repo, "S1.1")

    assert result.returncode == 0
    assert result.stdout.strip() == ""


def test_misto_lista_somente_os_de_fora(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "scripts/check_scope.py", "codigo\n", "adiciona script")
    commit_file(repo, "docs/DECISOES.md", "decisao\n", "adiciona decisao")

    result = run_script(repo, "S1.1")

    assert result.returncode == 1
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    assert lines == ["docs/DECISOES.md"]


def test_cwd_sem_repo_git_retorna_2(tmp_path: Path) -> None:
    cwd = tmp_path / "not_repo"
    cwd.mkdir()
    write_backlog(cwd)

    result = run_script(cwd, "S1.1")

    assert result.returncode == 2
    assert "nao avaliavel:" in result.stdout


def test_escopo_vazio_retorna_2(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "scripts/check_scope.py", "codigo\n", "adiciona script")

    result = run_script(repo, "S1.4")

    assert result.returncode == 2
    assert "Escopo vazio" in result.stdout


def test_backlog_ausente_retorna_2(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git_init(repo)
    commit_file(repo, "docs/ARQUITETURA.md", "arquitetura\n", "init")

    result = run_script(repo, "S1.1")

    assert result.returncode == 2
    assert "nao avaliavel:" in result.stdout


def test_isolamento_do_parser(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "docs/other.md", "outro\n", "adiciona outro")

    result = run_script(repo, "S1.1")
    assert result.returncode == 1
    assert "docs/other.md" in result.stdout

    result_s180 = run_script(repo, "S1.80")
    assert result_s180.returncode == 0


def test_match_exato_retorna_1(tmp_path: Path) -> None:
    repo = base_repo(tmp_path)
    _git(repo, "checkout", "-b", "feature")
    commit_file(repo, "docs/refs/SOURCES2.md", "fonte2\n", "adiciona fonte2")

    result = run_script(repo, "S1.5")

    assert result.returncode == 1
    assert result.stdout.strip() == "docs/refs/SOURCES2.md"
