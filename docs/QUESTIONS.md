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

### Demais pendências
Abertas: D-04, D-06, D-07. Adiada: D-08. Demais: ver `docs/BACKLOG.md`, seção 3. Serão abertas aqui quando a história que depende delas for a próxima.
