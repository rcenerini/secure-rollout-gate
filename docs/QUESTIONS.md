# QUESTIONS

Perguntas abertas ao dono do produto. **Quem tem dúvida escreve aqui e para.** Formato:

```
### Q-NNN · <título curto>
- Pergunta
- Contexto (história, arquivo)
- Opções (2 a 4)
- Recomendação (se houver) e por quê
- Status: ABERTA | RESPONDIDA em <data>
- Resposta do dono do produto: (só o dono preenche)
```

Ao responder, o PM copia a decisão para `docs/DECISOES.md`.

---

### Q-001 · D-01 Nome e conta do repositório
- Qual o nome do repositório e em qual conta do GitHub?
- Opções: `secure-rollout-gate` na conta pessoal (proposta); outro nome; organização pessoal.
- Status: RESPONDIDA em 21/11/2026 (ver DECISOES.md)

### Q-002 · D-02 Visibilidade e política organizacional
- Os documentos citam o stack de segurança do ambiente de origem. O repositório será privado ou público? Existe política organizacional sobre uso de GitHub pessoal para este tema?
- Opções: privado até sanitizar (proposta); público já; dois repositórios (público genérico e privado com o contexto corporativo).
- Observação: regras de proteção de deploy customizadas só existem em repositório público no plano Free.
- Status: RESPONDIDA em 21/11/2026 (ver DECISOES.md)

### Q-003 · D-03 Stack do código
- Opções: Python 3.12 + FastAPI + pytest + ruff (proposta); TypeScript; Go.
- Status: RESPONDIDA em 21/11/2026 (ver DECISOES.md)

### Q-004 · D-04 opencode e modelos
- Qual versão do opencode (V1 ou V2), quais provedores e modelos estão disponíveis, saldo de créditos e limite do Claude Code?
- Status: RESPONDIDA em 21/11/2026 (inventário completo em LLM-ROUTING.md)

### Q-005 · D-05 Gate sem VPS
- Opções: job de Actions como check (proposta); GitHub App direto na VPS.
- Status: RESPONDIDA em 21/11/2026 (job de Actions)

### Q-006 · D-13 Precedência PENDENTE × NO-GO
- Com achado de IA não validado e alto/crítico determinístico ao mesmo tempo, o fluxograma da Rev 4 dá PENDENTE. NO-GO deveria prevalecer?
- Status: RESPONDIDA em 21/11/2026 (NO-GO prevalece)

### Q-007 · Convenção do campo `Saída`/escopo para o `check_scope` (S1.8)
- Pergunta: qual convenção o `check_scope.py` deve usar para obter a lista de arquivos permitidos da história, já que o campo `Saída` é prosa livre (mistura paths, "(ou equivalente)", contagens "(6)", diretórios e, em várias histórias, nem existe)?
- Contexto: S1.8 ("Parar se: o formato do campo Saída for ambíguo"). BACKLOG.md §9 usa `Saída` em formato compacto não parseável. O script também precisa saber qual história verificar e de onde vêm os arquivos alterados (base do diff).
- Opções:
  - A) Campo estruturado `Escopo:` em cada história (um path exato por linha, entre crases, sem prosa, sem "(ou equivalente)", sem contagens), mantendo `Saída` como descrição humana; `check_scope` lê `Escopo`. Exige editar BACKLOG.md e docs/templates/STORY.md (excede o `Saída` atual da S1.8 → vira parte do escopo ou história separada).
  - B) Extração dentro do próprio `Saída`: só contam tokens entre crases que pareçam caminhos (ex.: começam por `src/`, `scripts/`, `docs/`, `tests/`, `policy/`, `schemas/`, `fixtures/`, `api/`, `.github/` ou terminam em extensão de arquivo). "(ou equivalente)", "(n)" e prosa são ignorados. Heurística, não 100% determinística.
  - C) `check_scope` não parseia BACKLOG.md: recebe o allowlist como argumento/arquivo sidecar (`--allow <path...>`). Determinístico, mas deixa de "comparar com a Saída da história" literalmente.
  - D) Adiar S1.8 para depois de S2.1 (esqueleto/pytest) e decidir a convenção junto do esqueleto do projeto.
- Recomendação: A + definir também (i) que `check_scope` recebe `--story <ID>` e lê BACKLOG.md, e (ii) que os arquivos alterados vêm de `git diff --name-only` contra a branch base (a confirmar qual base: `main`). A opção A é a única totalmente determinística e alinhada ao DoD ("nenhum arquivo fora de Saída alterado"). Se o custo de reescrever as histórias agora for alto, B é a alternativa de menor atrito, aceitando heurística documentada.
- Status: RESPONDIDA em 21/11/2026
- Resposta do dono do produto: opção A (campo estruturado `Escopo:` em cada história, um path exato por linha entre crases, mantendo `Saída` como descrição humana); `check_scope` recebe `--story <ID>` e lê o BACKLOG.md; arquivos alterados de `git diff --name-only` contra `main`.

### Demais pendências
Abertas: D-04, D-06, D-07. Adiada: D-08. Demais: ver `docs/BACKLOG.md`, seção 3. Serão abertas aqui quando a história que depende delas for a próxima.
