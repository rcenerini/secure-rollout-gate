# HANDOFF

Atualize ao fim de cada sessao e sempre que trocar de ferramenta (opencode <-> Claude Code). Quem assume le **este arquivo primeiro**.

## Estado atual
- **Data/hora:** 22/11/2026
- **Ferramenta e modelo da ultima sessao:** opencode v2.1.4 / opencode-go/qwen3.8-flash (T3 aprovado na S1.2)
- **Historia em andamento:** S1.11 (parada em pergunta: Q-014 e Q-015)
- **Branch:** story/S1.11
- **Ultima historia concluida:** S1.8. A S1.11 esta **parcial**: 17 historias receberam `Escopo`; 29 ficaram sem porque a `Saída` nao determina os arquivos (Q-014).

## Proximo passo (exato)
1. O humano responde **Q-014** (opcoes A a D) e **Q-015** (opcoes A a C) em `docs/QUESTIONS.md`.
2. Com a resposta: se for A ou C, a S1.11 e retomada para preencher as 29 restantes; se for B, abre-se historia nova para o `check_scope` tratar diretorio e sufixo de extensao.
3. Depois o humano revisa o diff da branch `story/S1.11` e abre o PR. O agente nao faz push nem usa `gh`.

## O que esta feito e verificado
- `docs/BACKLOG.md`: campo `Escopo` acrescentado em 17 historias cuja `Saída` da a lista completa de arquivos (na S1.4 a lista sai do `{planner,test-author,...}.md` da propria `Saída`): S0.1, S0.5, S0.6, S0.7, S1.1, S1.3, S1.4, S1.7, S1.9, S1.10, S2.2, S3.2, S3.3, S3.5, S3.10, S7.1, S7.5. Total de historias com `Escopo` no arquivo: 19 (as outras duas sao S1.8 e S1.11, que ja tinham).
- `docs/QUESTIONS.md`: Q-014 (historias com `Saída` em diretorio, glob, sem nome de arquivo ou com prosa) e Q-015 (12 historias sem campo `Saída`). As duas abertas; a historia nao pode ser fechada sem resposta.
- Aceite executado (saida colada abaixo): nenhuma historia com `Escopo` devolve codigo 2; a S1.11 devolve 0. Dos 29 caminhos listados nos `Escopo`, 22 aparecem de forma exata na `Saída`, 6 aparecem pela expansao do `{a,b}.md` da S1.4 e 1 nao aparece (`tests/test_check_scope.py` da S1.8, texto preexistente aprovado por voce).
- Gates deterministicos: pytest 16 passed; ruff sem achados (nenhum codigo foi alterado nesta historia).

## O que NAO foi feito
- `Escopo` das 29 historias listadas na Q-014 (nomes de workflow, arquivos de fixture por diretorio, globs de extensao). Nao foram inventados.
- Merge, push e PR: ficam com o humano.

## Arquivos tocados na ultima sessao
- `docs/BACKLOG.md`
- `docs/QUESTIONS.md`
- `docs/HANDOFF.md`
- `docs/USAGE-LOG.md`

## Comandos rodados e resultado

### Aceite 1 da S1.11 - check_scope por historia
O laco rodou `python scripts/check_scope.py --story <ID>` para as 60 historias com cabecalho `####` no arquivo, com o diff ja commitado na branch (2 commits: `docs/BACKLOG.md` e `docs/QUESTIONS.md`). `docs/QUESTIONS.md` esta na lista fixa do script, entao o unico arquivo fora do `Escopo` dessas historias e `docs/BACKLOG.md` — por isso o codigo 1. Codigo 2 = sem campo `Escopo`. Apos o commit do `HANDOFF` e do `USAGE-LOG` (tambem na lista fixa) os codigos nao mudam.

```
PS <repo>> $env:PYTHONIOENCODING='utf-8'; & "<python>" "<temp>\opencode\run_acceptance.py"   # laco que roda: python scripts/check_scope.py --story <ID>
historias no BACKLOG: 60
ID      cod  saida
S0.1     1    docs/BACKLOG.md
S0.2     2    nao avaliavel: sem campo Escopo
S0.3     2    nao avaliavel: sem campo Escopo
S0.4     2    nao avaliavel: sem campo Escopo
S0.5     1    docs/BACKLOG.md
S0.6     1    docs/BACKLOG.md
S0.7     1    docs/BACKLOG.md
S1.1     1    docs/BACKLOG.md
S1.2     2    nao avaliavel: sem campo Escopo
S1.3     1    docs/BACKLOG.md
S1.4     1    docs/BACKLOG.md
S1.5     2    nao avaliavel: sem campo Escopo
S1.6     2    nao avaliavel: sem campo Escopo
S1.7     1    docs/BACKLOG.md
S1.8     1    docs/BACKLOG.md
S1.9     1    docs/BACKLOG.md
S1.10    1    docs/BACKLOG.md
S1.11    0
S2.1     2    nao avaliavel: sem campo Escopo
S2.2     1    docs/BACKLOG.md
S2.3     2    nao avaliavel: sem campo Escopo
S2.4     2    nao avaliavel: sem campo Escopo
S2.5     2    nao avaliavel: sem campo Escopo
S2.6     2    nao avaliavel: sem campo Escopo
S2.7     2    nao avaliavel: sem campo Escopo
S2.8     2    nao avaliavel: sem campo Escopo
S2.9     2    nao avaliavel: sem campo Escopo
S2.10    2    nao avaliavel: sem campo Escopo
S3.1     2    nao avaliavel: sem campo Escopo
S3.2     1    docs/BACKLOG.md
S3.3     1    docs/BACKLOG.md
S3.4     2    nao avaliavel: sem campo Escopo
S3.5     1    docs/BACKLOG.md
S3.6     2    nao avaliavel: sem campo Escopo
S3.7     2    nao avaliavel: sem campo Escopo
S3.8     2    nao avaliavel: sem campo Escopo
S3.9     2    nao avaliavel: sem campo Escopo
S3.10    1    docs/BACKLOG.md
S5.1     2    nao avaliavel: sem campo Escopo
S5.2     2    nao avaliavel: sem campo Escopo
S5.3     2    nao avaliavel: sem campo Escopo
S5.4     2    nao avaliavel: sem campo Escopo
S5.5     2    nao avaliavel: sem campo Escopo
S5.6     2    nao avaliavel: sem campo Escopo
S5.7     2    nao avaliavel: sem campo Escopo
S4.1     2    nao avaliavel: sem campo Escopo
S4.2     2    nao avaliavel: sem campo Escopo
S4.3     2    nao avaliavel: sem campo Escopo
S4.4     2    nao avaliavel: sem campo Escopo
S4.5     2    nao avaliavel: sem campo Escopo
S6.1     2    nao avaliavel: sem campo Escopo
S6.2     2    nao avaliavel: sem campo Escopo
S6.3     2    nao avaliavel: sem campo Escopo
S6.4     2    nao avaliavel: sem campo Escopo
S6.5     2    nao avaliavel: sem campo Escopo
S7.1     1    docs/BACKLOG.md
S7.2     2    nao avaliavel: sem campo Escopo
S7.3     2    nao avaliavel: sem campo Escopo
S7.4     2    nao avaliavel: sem campo Escopo
S7.5     1    docs/BACKLOG.md

sintese: 0=1  1=18  2=41
```

Leitura do aceite: as 18 historias com codigo 1 sao exatamente as 17 preenchidas nesta historia mais a S1.8 (que ja tinha `Escopo`). **Nenhuma delas devolve 2.** As 41 com codigo 2 dividem-se em 29 com `Saída` ambigua (Q-014) e 12 sem campo `Saída` (Q-015).

O laco foi rodado de novo depois do ultimo commit, com a mesma sintese (`0=1  1=18  2=41`), e `check_scope.py --story S1.11` continuou com codigo 0. Diff final da branch contra `main`: `docs/BACKLOG.md`, `docs/HANDOFF.md`, `docs/QUESTIONS.md`, `docs/USAGE-LOG.md` — nada fora do `Escopo` mais a lista fixa.

### Aceite 1 - historia desta sessao
```
PS <repo>> & "<python>" scripts/check_scope.py --story S1.11
PS <repo>> $LASTEXITCODE
0
```

### Aceite 2 da S1.11 - todo caminho do `Escopo` aparece na `Saída`
O script de verificacao importou `parse_escopo` do proprio `scripts/check_scope.py` (mesmo parser do aceite) e classificou cada caminho. Saida completa:

```
historias com Escopo: 19 de 60
caminhos no Escopo: 29
caminhos fora da Saida: 1 -> [('S1.8', 'tests/test_check_scope.py')]
```

Detalhe por historia (caminhos marcados `exato` ou `expansao`): S0.1 (1), S0.5 (4), S0.6 (1), S0.7 (1), S1.1 (1), S1.3 (1), S1.4 (6, todos por expansao de `{planner,test-author,implementer,reviewer,security-reviewer,doc-keeper}.md`), S1.7 (1), S1.9 (1), S1.10 (1), S1.11 (1), S2.2 (1), S3.2 (1), S3.3 (1), S3.5 (2), S3.10 (1), S7.1 (1), S7.5 (1) = 22 exatos + 6 por expansao. A S1.8 tem 2 caminhos: `scripts/check_scope.py` esta na `Saída`; `tests/test_check_scope.py` nao — a `Saída` diz "e seu teste" (prosa). Texto preexistente, aprovado por voce na historia; nao foi mexido. Registrado na nota da Q-014.

### Gates deterministicos (sem alteracao de codigo)
```
PS <repo>> & "<python>" -m pytest tests/test_check_scope.py -q
16 passed, 673 warnings in 18.16s
PS <repo>> & "<python>" -m ruff check scripts tests
All checks passed!
```

## Perguntas abertas
Q-014 e Q-015, nesta sessao. Demais em `docs/QUESTIONS.md`.

## Observacoes
- Comandos git autorizados na fixture de teste (resolucao P-1, opcao A): `git init` (com `-b main` ou `--initial-branch=main`), `git config user.name`/`git config user.email` (locais, valores falsos de teste), `git add`, `git commit`, `git branch`/`git checkout -b`, `git mv`.
- Os dois scripts de verificacao do aceite ficaram fora do repositorio (pasta temporaria da sessao), porque o `Escopo` da S1.11 so permite `docs/BACKLOG.md`. Nao ha artefato de teste para reproduzir o aceite 1 e 2 alem dos comandos colados acima.
- A S1.11 nao alterou `scripts/check_scope.py` nem seus testes.
- O aceite do tipo "codigo 1" nas outras historias e esperado nesta branch: o diff tem `docs/BACKLOG.md`, que nao esta no `Escopo` delas. O criterio da historia e "nao retorna codigo 2".
- `docs/DECISOES.md` e `docs/refs/SOURCES.md` nao estavam no `Escopo` da S1.11, entao nao foram alterados.
- Aceite executado com o Python 3.14 local (o `python` da Microsoft Store esta quebrado); a D-03 (3.12) segue valendo, e a execucao em 3.12 passa a ser criterio da S2.2 (CI), conforme `docs/DECISOES.md`.
- Toda leitura de arquivo usou `encoding="utf-8"`; `docs/BACKLOG.md` continua com terminacoes LF (0 CRLF) e o diff e de insercao pura (43 linhas).
- Bloco "Estado automatico" (scripts/handoff.ps1): gerado ao encerrar a sessao; **nao commitar** (descartar com `git restore docs/HANDOFF.md` antes do commit).
