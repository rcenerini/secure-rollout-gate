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
- Pergunta: como o `check_scope.py` obtém a lista de arquivos permitidos de uma história?
- Opções: A) campo `Escopo` estruturado; B) extrair caminhos da `Saída`; C) `--allow`; D) adiar a S1.8.
- Status: RESPONDIDA em 21/11/2026 (A, com base do diff `main`; ver DECISOES.md)

### Q-008 · Arquivos de processo e o `check_scope`
- Pergunta: o `check_scope` deve permitir sempre os arquivos de processo que o AGENTS.md manda atualizar em toda história?
- Opções: A) lista fixa (`HANDOFF.md`, `USAGE-LOG.md`, `QUESTIONS.md`); B) nada isento; C) commit separado.
- Status: RESPONDIDA em 21/11/2026 (A; ver DECISOES.md)

### Q-009 · S6.1: como publicar o check do PR
- Pergunta: com job de Actions (D-05), como o gate publica o resultado no PR?
- Opções: A) o próprio job é o check (nome do job como check obrigatório no ruleset); B) check run extra via API com `checks: write`; C) adiar para o GitHub App (S8.6, S8.7).
- Status: RESPONDIDA em 22/11/2026 (A; ver DECISOES.md)

### Q-010 · gitleaks: comando depreciado
- Pergunta: qual comando do gitleaks o projeto usa? `detect` e `protect` estão depreciados desde a v8.19.0.
- Opções: A) `gitleaks dir .` e `gitleaks git .`; B) manter `detect`.
- Status: RESPONDIDA em 22/11/2026 (A; ver DECISOES.md)

### Q-011 · Actions fixadas por SHA e Dependabot
- Pergunta: como conciliar SHA fixo com o Dependabot, que não alerta ações fixadas por SHA?
- Opções: A) SHA com comentário de versão, risco coberto por zizmor e Dependency Review; B) usar tags.
- Status: RESPONDIDA em 22/11/2026 (A; ver DECISOES.md)

### Q-012 · CodeQL na S2.5
- Pergunta: o CodeQL está disponível na visibilidade e no plano atuais?
- Status: RESPONDIDA em 22/11/2026 (gratuito em repositório público; ver DECISOES.md)

### Q-013 · Prefixo de branch
- Pergunta: `story/<ID>` ou `teste/<historia>-<modelo>`?
- Opções: A) `story/` para entrega e `teste/` para evidência de teste; B) `story/` sempre.
- Status: RESPONDIDA em 22/11/2026 (A; ver DECISOES.md)

### Q-014 · Escopo nas histórias cuja Saída não nomeia arquivos exatos
- Pergunta: como preencher o `Escopo` das histórias cuja `Saída` aponta um diretório (`docs/`, `fixtures/`, `tests/regression/`, `policy/`, `fixtures/raw/<ferramenta>/`), usa glob ou extensão indefinida (`*.md`, `src/normalizador/sarif.*`, `scripts/metricas.*`), escreve "(ou equivalente)" / "(ou pasta)", ou não nomeia o arquivo (os workflows das S2.4, S2.5, S2.6, S2.9, S2.10, S5.2 a S5.7, S6.1 e S7.2, e o "arquivo de dependências" da S2.1)?
- Contexto: história S1.11. O `scripts/check_scope.py` compara cada caminho alterado com um conjunto de strings exatas (`allowed = set(escopo) | FIXED_FILES`), então uma entrada de diretório nunca casa com um arquivo do diff. O template `docs/templates/STORY.md` pede "um caminho exato por linha, entre crases, sem prosa, sem '(ou equivalente)', sem contagens". Completar essas listas exigiria nomear arquivos que ainda não existem nem foram decididos, o que a regra anti-alucinação proíbe. A S1.11 preencheu as 17 histórias em que a `Saída` dá a lista completa. Ficaram aqui também três histórias que nomeiam um arquivo exato mas têm saída adicional sem nome: S2.3 (os workflows alterados), S3.1 (`fixtures/achados/validos/` e `invalidos/` com contagem) e S3.4 (`fixtures/politica/*.json`).
- Nota do aceite: o único `Escopo` com caminho que não aparece na `Saída` é o da S1.8 — `tests/test_check_scope.py`, que a `Saída` descreve como "e seu teste" (prosa). Está assim desde a história, foi aprovado por você, e a S1.11 não mexeu nele. A opção C resolveria com uma linha na `Saída` da S1.8.
- Histórias afetadas (29): S0.2, S0.3, S0.4, S1.2, S1.5, S1.6, S2.1, S2.3, S2.4, S2.5, S2.6, S2.7, S2.9, S2.10, S3.1, S3.4, S3.6, S3.9, S4.1, S5.1, S5.2, S5.3, S5.4, S5.5, S5.6, S5.7, S6.1, S7.2, S7.3.
- Opções:
  - A) Preencher o `Escopo` no início de cada história, com os nomes exatos aprovados no plano; a S1.11 fica restrita ao que é determinável hoje.
  - B) Criar história nova (T2) para o `check_scope` tratar entrada terminada em `/` como prefixo de diretório e `*` como sufixo de extensão (mexeria em `scripts/check_scope.py` e nos testes, fora do `Escopo` da S1.11).
  - C) Reescrever a `Saída` dessas histórias com caminhos exatos agora (muda a definição de 29 histórias; aprovação humana).
  - D) Deixar como está: essas histórias continuam devolvendo código 2 quando forem executadas.
- Recomendação: A agora, mais B como história nova a confirmar (S1.12). Para três histórias o nome já está registrado em `docs/DECISOES.md` e poderia receber C sem inventar nada: S0.4 → `.github/rulesets/protecao-main.json`, S1.6 → `scripts/handoff.ps1`, S1.5 → os seis arquivos da lista da S1.4.
- Status: ABERTA
- Resposta do dono do produto:

### Q-015 · Histórias sem campo Saída no aceite da S1.11
- Pergunta: as 12 histórias sem `Saída` contam como "histórias com arquivos de saída" no aceite da S1.11?
- Contexto: história S1.11. Sem campo `Saída`, o `check_scope` devolve código 2 ("sem campo Escopo"). São elas: S2.8, S3.7, S3.8, S4.2, S4.3, S4.4, S4.5, S6.2, S6.3, S6.4, S6.5, S7.4. Algumas claramente alteram arquivos (S3.7 e S3.8 em `policy/`; S4.2 a S4.4 nos parsers; S2.8 em configuração de cobertura), outras são ações no GitHub (S6.2, S6.5) ou coleta de evidência (S6.3, S7.4).
- Opções: A) fora do aceite agora, e exigir `Saída` + `Escopo` quando cada uma for executada; B) acrescentar `Saída` + `Escopo` agora por proposta do agente com aprovação humana; C) dispensar `Escopo` para sempre.
- Recomendação: A.
- Status: ABERTA
- Resposta do dono do produto:

### Demais pendências
Abertas: D-04, D-06, D-07. Adiada: D-08. Demais: ver `docs/BACKLOG.md`, seção 3. Serão abertas aqui quando a história que depende delas for a próxima.
