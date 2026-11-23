# HANDOFF

Atualize ao fim de cada sessao e sempre que trocar de ferramenta (opencode <-> Claude Code). Quem assume le **este arquivo primeiro**.

## Estado atual
- **Data/hora:** 22/11/2026
- **Ferramenta e modelo da ultima sessao:** opencode v2.1.4 / opencode-go/qwen3.8-flash (T3 aprovado na S1.2)
- **Historia em andamento:** S1.11 — **PARCIAL por decisao do dono** (Q-014 e Q-015 respondidas em 22/11/2026; o resto depende de S1.12)
- **Branch:** story/S1.11
- **Ultima historia concluida:** S1.8. A S1.11 esta **parcial**: 17 historias receberam `Escopo`; 29 ficaram sem porque a `Saída` nao determina os arquivos (Q-014, respondida: o que falta depende do prefixo de diretorio, que vira a historia S1.12).

## Proximo passo (exato)
1. O humano cria a historia **S1.12** (T2): `check_scope` aceitar entrada terminada em `/` como prefixo de diretorio e `*` como sufixo de extensao, com testes. Resposta da Q-014: "A agora + B depois".
2. Retomar a S1.11 depois da S1.12 para preencher as 29 historias que dependem de prefixo de diretorio.
3. O humano revisa o diff da branch `story/S1.11` e abre o PR. O agente nao faz push nem usa `gh`.

## Pendencias abertas pela decisao do dono
- **S1.12 (T2, nova):** prefixo de diretorio (`/`) e sufixo de extensao (`*`) no `check_scope`. Sem ela, as 29 historias da Q-014 continuam sem `Escopo`.
- **Historia separada para o `AGENTS.md` (Q-016, ABERTA):** registrar la as restricoes duraveis do `check_scope` (mensagens sem caracteres fora do cp1252; stdout do git lido com `encoding="utf-8"` explicito).
- **Baixa prioridade (achados da revisao):**
  - **M-1:** a evidencia da S1.8 saiu do `HANDOFF` na reescrita. Ela esta no PR #20/#21 e em `git show main:docs/HANDOFF.md`. Ponteiro sugerido: uma linha em Observacoes na proxima edicao do `HANDOFF`.
  - **M-4:** `opencode.json` nao esta na `Saída` da S1.4, mas os commits `096fa2e` e `4923a48` mexeram nele. Uma reexecucao da S1.4 daria codigo 1. Ajuste e na `Saída` da historia (decisao do dono).
  - **M-5:** `LICENSE` esta listado na `Saída` da S0.5, dispensado pela D-10. Manter ou alinhar a `Saída` e decisao do dono.
- **Efeito no aceite (a confirmar pelo dono):** o `Escopo` da S1.11 lista so `docs/BACKLOG.md`. O commit autorizado de `docs/DECISOES.md` (respostas de Q-014 e Q-015) esta fora desse `Escopo`, entao `check_scope --story S1.11` passou de 0 para 1 e a sintese da branch deixou de bater com o "resultado esperado" do Aceite 1. Duas saidas, ambas sua decisao: acrescentar `docs/DECISOES.md` ao `Escopo` da S1.11 (o campo `Escopo` e da propria historia, edicao permitida) ou desfazer o commit do `DECISOES.md` e levar a decisao para la em outro momento.

## O que esta feito e verificado
- `docs/BACKLOG.md`: campo `Escopo` acrescentado em 17 historias cuja `Saída` da a lista completa de arquivos (na S1.4 a lista sai do `{planner,test-author,...}.md` da propria `Saída`): S0.1, S0.5, S0.6, S0.7, S1.1, S1.3, S1.4, S1.7, S1.9, S1.10, S2.2, S3.2, S3.3, S3.5, S3.10, S7.1, S7.5. Total de historias com `Escopo` no arquivo: 19 (as outras duas sao S1.8 e S1.11, que ja tinham).
- `docs/QUESTIONS.md`: Q-014 e Q-015 **respondidas** em 22/11/2026 (repostadas em `docs/DECISOES.md`); Q-016 aberta (onde registrar as restricoes duraveis do `check_scope`). A legenda do `BACKLOG` (§9) agora marca `Escopo` como campo opcional por enquanto.
- Aceite executado (saida colada abaixo): nenhuma historia com `Escopo` devolve codigo 2; a S1.11 devolveu 0 naquele estado (ver em Pendencias o efeito do commit do `DECISOES.md`). Dos 29 caminhos listados nos `Escopo`, 22 aparecem de forma exata na `Saída`, 6 aparecem pela expansao do `{a,b}.md` da S1.4 e 1 nao aparece (`tests/test_check_scope.py` da S1.8, texto preexistente aprovado por voce).
- Gates deterministicos: pytest 16 passed; ruff sem achados (nenhum codigo foi alterado nesta historia).

## O que NAO foi feito
- `Escopo` das 29 historias da Q-014: em nenhuma delas a `Saída` da a lista completa (aponta diretorio, usa glob sem extensao definida, nomeia sem extensao ou nao nomeia o arquivo). Nada foi inventado; o que depende de diretorio e sufixo de extensao fica para a S1.12, e o resto e preenchido no plano de cada historia (opcao A da Q-014).
- As 12 historias sem `Saída` (Q-015) seguem sem `Escopo`, por decisao do dono: cada uma ganha `Saída` + `Escopo` quando for executada.
- Merge, push e PR: ficam com o humano.

## Arquivos tocados na ultima sessao
- `docs/BACKLOG.md`
- `docs/QUESTIONS.md`
- `docs/DECISOES.md` (autorizado pelo dono em 22/11/2026, fora do `Escopo` da S1.11)
- `docs/HANDOFF.md`
- `docs/USAGE-LOG.md`

## Comandos rodados e resultado

### Aceite 1 da S1.11 - check_scope por historia
O laco rodou `python scripts/check_scope.py --story <ID>` para as 60 historias com cabecalho `####` no arquivo, com o diff ja commitado na branch (2 commits: `docs/BACKLOG.md` e `docs/QUESTIONS.md`). `docs/QUESTIONS.md` esta na lista fixa do script, entao o unico arquivo fora do `Escopo` dessas historias e `docs/BACKLOG.md` — por isso o codigo 1. Codigo 2 = sem campo `Escopo`. Apos o commit do `HANDOFF` e do `USAGE-LOG` (tambem na lista fixa) os codigos nao mudam.

```
PS <repo>> Select-String -Path docs/BACKLOG.md -Pattern '^#### (S\d+\.\d+)' | % { $id=$_.Matches[0].Groups[1].Value; & python scripts/check_scope.py --story $id | Out-Null; "$id $LASTEXITCODE" }
resultado esperado: 0=1, 1=18, 2=41
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
