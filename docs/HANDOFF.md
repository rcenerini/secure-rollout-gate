# HANDOFF

Atualize ao fim de cada sessao e sempre que trocar de ferramenta (opencode <-> Claude Code). Quem assume le **este arquivo primeiro**.

## Estado atual
- **Data/hora:** 22/11/2026
- **Ferramenta e modelo da ultima sessao:** opencode v2.1.4 / opencode-go/deepseek-v4-pro (correcoes pos-revisao)
- **Historia em andamento:** S1.8 (correcoes pos-revisao)
- **Branch:** story/S1.8
- **Ultima historia concluida:** S1.8 (aceite abaixo)

## Proximo passo (exato)
O humano revisa o diff da branch `story/S1.8` e abre o PR. O agente nao faz push nem usa `gh`.

## O que esta feito e verificado
- Criados `scripts/check_scope.py` e `tests/test_check_scope.py`.
- Aceite executado: pytest 16 passed; ruff sem achados.
- Script validado no repositorio real com `--story S1.8` -> codigo 0.
- Correcoes pos-revisao: diff com `-c core.quotepath=false` e `--no-renames`; timeout de 30s; erro do git resume a primeira linha do stderr; 2 testes novos (rename para dentro do escopo e caminho com acento); HANDOFF sem caminhos locais e com a nota do `handoff.ps1` restaurada.

## O que NAO foi feito
- Merge da historia; push e PR ficam com o humano.

## Arquivos tocados na ultima sessao
- `scripts/check_scope.py`
- `tests/test_check_scope.py`
- `docs/HANDOFF.md`
- `docs/USAGE-LOG.md`

## Comandos rodados e resultado

### Aceite S1.8 (correcoes pos-revisao)

```
PS <repo>> & "%LOCALAPPDATA%\Python\bin\python.exe" -m pytest tests/test_check_scope.py -v
============================= test session starts =============================
platform win32 -- Python 3.14.0, pytest-8.3.4, pluggy-1.6.0 -- %LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: <repo>
plugins: anyio-4.12.1, langsmith-0.8.5, asyncio-0.24.0, cov-7.0.0, mock-3.15.1, requests-mock-1.12.1, respx-0.23.1
asyncio: mode=Mode.STRICT, default_loop_scope=None
collecting ... collected 16 items

tests/test_check_scope.py::test_dentro_do_escopo_retorna_0 PASSED        [  6%]
tests/test_check_scope.py::test_fora_do_escopo_retorna_1_listando_infrator PASSED [ 12%]
tests/test_check_scope.py::test_historia_sem_escopo_retorna_2 PASSED     [ 18%]
tests/test_check_scope.py::test_sem_branch_main_retorna_2 PASSED         [ 25%]
tests/test_check_scope.py::test_somente_lista_fixa_retorna_0 PASSED      [ 31%]
tests/test_check_scope.py::test_decisoes_e_sources_no_escopo_retorna_0 PASSED [ 37%]
tests/test_check_scope.py::test_historia_inexistente_retorna_2 PASSED    [ 43%]
tests/test_check_scope.py::test_diff_vazio_retorna_0 PASSED              [ 50%]
tests/test_check_scope.py::test_misto_lista_somente_os_de_fora PASSED    [ 56%]
tests/test_check_scope.py::test_cwd_sem_repo_git_retorna_2 PASSED        [ 62%]
tests/test_check_scope.py::test_escopo_vazio_retorna_2 PASSED            [ 68%]
tests/test_check_scope.py::test_backlog_ausente_retorna_2 PASSED         [ 75%]
tests/test_check_scope.py::test_isolamento_do_parser PASSED              [ 81%]
tests/test_check_scope.py::test_match_exato_retorna_1 PASSED             [ 87%]
tests/test_check_scope.py::test_renomear_fora_para_dentro_retorna_1 PASSED [ 93%]
tests/test_check_scope.py::test_caminho_acentuado_no_escopo_retorna_0 PASSED [100%]

============================== warnings summary ===============================
pytest_asyncio (Python 3.14): 673 warnings de deprecacao (iscoroutinefunction,
get_event_loop_policy e asyncio_default_fixture_loop_scope)
-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
====================== 16 passed, 673 warnings in 18.30s ======================

PS <repo>> & "%LOCALAPPDATA%\Python\bin\python.exe" -m ruff check scripts/check_scope.py tests/test_check_scope.py
All checks passed!
```

### Validacao no repositorio real
```
PS <repo>> & "%LOCALAPPDATA%\Python\bin\python.exe" scripts/check_scope.py --story S1.8
PS <repo>> $LASTEXITCODE
0
```

## Perguntas abertas
Ver `docs/QUESTIONS.md`.

## Observacoes
- Comandos git autorizados na fixture de teste (resolucao P-1, opcao A): `git init` (com `-b main` ou `--initial-branch=main`), `git config user.name`/`git config user.email` (locais, valores falsos de teste), `git add`, `git commit`, `git branch`/`git checkout -b`, `git mv`.
- O script usa `git -c core.quotepath=false diff --no-renames --name-only main...HEAD` com `timeout=30`; desvio autorizado nesta sessao em relacao a Interface do BACKLOG (que citava `git diff --name-only main...HEAD`), para detectar rename e caminhos nao-ASCII. O erro do git resume a primeira linha nao vazia do stderr.
- O aceite foi executado com Python 3.14.0 local; o projeto decide D-03 (3.12) e o `python` do Microsoft Store esta quebrado, entao usamos o caminho completo `%LOCALAPPDATA%\Python\bin\python.exe`.
- Toda leitura de arquivo e stdout do git usa `encoding="utf-8"` explicito.
- Mensagens do script em portugues simples, sem caracteres fora do cp1252.
- Nenhum arquivo fora do escopo da S1.8 foi alterado, exceto os de lista fixa (`docs/HANDOFF.md`, `docs/USAGE-LOG.md`).
- Bloco "Estado automatico" (scripts/handoff.ps1): gerado ao encerrar a sessao; **nao commitar** (descartar com `git restore docs/HANDOFF.md` antes do commit).
