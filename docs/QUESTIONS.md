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

### Demais pendências
Abertas: D-04, D-06, D-07. Adiada: D-08. Demais: ver `docs/BACKLOG.md`, seção 3. Serão abertas aqui quando a história que depende delas for a próxima.
