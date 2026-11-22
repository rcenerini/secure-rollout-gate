# HANDOFF

Atualize ao fim de cada sessão e sempre que trocar de ferramenta (opencode ↔ Claude Code). Quem assume lê **este arquivo primeiro**.

## Estado atual
- **Data/hora:** 21/11/2026
- **Ferramenta e modelo da última sessão:** opencode v2.1.4 / opencode-go/kimi-k2.7-code
- **História em andamento:** nenhuma
- **Branch:** story/S1.8
- **Última história concluída:** S1.8 (`scripts/check_scope.py` e `tests/test_check_scope.py`; aceite executado)

## Próximo passo (exato)
Abrir PR da branch `story/S1.8` para `main` com a saída do aceite colada na descrição.

## O que está feito e verificado
- `scripts/check_scope.py` criado: lê `Escopo` de `docs/BACKLOG.md`, diff `main...HEAD`, lista fixa de arquivos de processo, códigos 0/1/2.
- `tests/test_check_scope.py` criado: 14 testes unitários/mockados, todos passando.
- Aceite executado: unittest OK; códigos manuais 0 (S1.8), 2 (S1.3), 1 (README.md temporário fora do escopo).

## O que NÃO foi feito
- Merge do PR; lint formal (ruff ainda não configurado — depende de S2.1).

## Arquivos tocados na última sessão
- `scripts/check_scope.py` (criado)
- `tests/test_check_scope.py` (criado)
- `docs/USAGE-LOG.md` (atualizado)
- `docs/HANDOFF.md` (este arquivo)

## Comandos rodados e resultado
- `py -V:Astral\CPython3.12.8 -m unittest discover -s tests -v` → 14/14 OK
- `py -V:Astral\CPython3.12.8 scripts/check_scope.py --story S1.8` → código 0
- `py -V:Astral\CPython3.12.8 scripts/check_scope.py --story S1.3` → código 2
- Commit temporário em `README.md` + script → código 1; restaurado com `git reset --mixed HEAD~1` e `git restore README.md`

## Perguntas abertas
Ver `docs/QUESTIONS.md`.

## Observações
- Créditos do opencode (saldo): não informado
- Tier e modelo usados: —
- Bloco "Estado automatico" (scripts/handoff.ps1): gerado ao encerrar a sessao; **nao commitar** (descartar com `git restore docs/HANDOFF.md` antes do commit)
