# AGENTS.md · Gate de Rollout Seguro

Instruções para qualquer agente de código (opencode, Claude Code ou outro). Seja objetivo e siga à risca.

## O que é o projeto
Gate de decisão GO / NO-GO / PENDENTE para liberar rollout: uma API de decisão (política determinística em OPA/Rego) lê uma base de achados de segurança e devolve o veredito para o Jira, o PR e o deploy. Agentes de IA **produzem achados**; **a política decide**.

## Leia antes de qualquer tarefa (use a ferramenta de leitura, nesta ordem)
1. `docs/BACKLOG.md` — a história que você vai executar (seção 9) e as regras (seções 4 e 5)
2. `docs/ARQUITETURA.md` — regra de decisão e esquema do achado (fonte da verdade)
3. `docs/HANDOFF.md` — onde o trabalho parou
4. `docs/QUESTIONS.md` e `docs/DECISOES.md` — o que já foi perguntado e decidido
Leia só o que o campo `Ler` da história pedir além disso.

## Precedência das regras
Se houver regras globais do usuário (por exemplo em `~/.config/opencode/AGENTS.md`) em conflito com este arquivo, **vale este arquivo**. Não resolva o conflito sozinho: registre-o em `docs/QUESTIONS.md` e pergunte.

## Regra zero
**Se houver dúvida, pare e pergunte.** Nunca decida e nunca infira. Escreva a pergunta em `docs/QUESTIONS.md` (contexto, opções, sua recomendação) e **espere a resposta do humano**. Histórias com decisão pendente em `Bloq` **não podem ser executadas**.

## Como trabalhar
1. Execute **uma história por vez**, em uma branch `story/<ID>`.
2. Confirme o Definition of Ready. Se faltar algo, pergunte.
3. Faça o plano (arquivos que vai tocar, testes, riscos) e **mostre antes de codar** quando a história for T1 ou T2.
4. Teste primeiro nas histórias de política e de normalização.
5. Mexa **somente** nos arquivos listados em `Saída`.
6. Rode o `Aceite` e **cole a saída real** em `docs/HANDOFF.md`. Quem abre o PR é o humano, que cola essa saída na descrição. Sem saída colada, a história não está feita.
7. Atualize `docs/HANDOFF.md`, `docs/USAGE-LOG.md` (criado na história S1.7) e, se aplicável, `docs/DECISOES.md` e `docs/refs/SOURCES.md`.
8. Commits pequenos e em português, no formato `S<ID>: <o que mudou>`.

## Anti-alucinação (obrigatório)
- **Nunca invente** endpoint, parâmetro, flag de linha de comando, campo de API, sintaxe ou versão. Só use o que estiver em fonte listada em `docs/refs/SOURCES.md` ou que você tenha lido na documentação oficial **nesta sessão**. Registre a fonte.
- Se não puder consultar a documentação, **pare e pergunte**. Não use memória como fonte.
- Código de Rego só é válido depois de `opa check` e `opa test`.
- SHA de commit de GitHub Action: obtenha pela API do GitHub e confira. **Nunca digite de memória.**
- Campo ausente em uma saída de ferramenta fica **nulo**. Nunca preencha por suposição.
- Proibido escrever "assumo que", "provavelmente" ou "deve funcionar" em código, testes ou documentação. Escreva a dúvida em `QUESTIONS.md`.
- Não declare concluído sem evidência executada.
- Não altere um golden file para fazer um teste passar. Mudança de saída esperada exige aprovação humana.

## Segurança
- **Agentes não fazem `git push`, não abrem PR e não usam `gh`.** Entregam a branch local e a saída do aceite no `docs/HANDOFF.md`; o push e o PR são do humano.
- Nunca coloque segredo, chave, token, dado real ou código corporativo no repositório, em prompt ou em teste. Segredos de teste são **falsos e identificados como falsos**.
- Não adicione dependência sem uma história ou ADR. Fixe versões; GitHub Actions fixadas por SHA.
- Workflows: `permissions` mínimas; nunca `pull_request_target` com checkout de código do PR; não passar segredos a PR de fork.
- Não instale skills, plugins ou MCPs de terceiros sem o procedimento de `docs/refs/ADMISSAO-SKILLS.md` (quando existir).
- Não rode ferramenta ofensiva (por exemplo Strix) fora do alvo de teste autorizado.

## Escolha do modelo (economia)
- O humano confirma o tier e o modelo no início de cada história (`docs/LLM-ROUTING.md`). Não troque de modelo por conta própria.
- Duas tentativas falhas: avise o humano e proponha subir o tier. Falhando de novo, pare e pergunte.
- Leia só os arquivos necessários. Não releia o repositório inteiro.
- Se os créditos do opencode estiverem no fim: faça commit do que está pronto e atualize `docs/HANDOFF.md`.

## Stack
Decidido (D-03): Python 3.12, FastAPI, pytest, ruff. Não crie código nem dependências antes da história S2.1, que fixa as versões com fonte. Não invente comandos.

## Comandos de verificação
Definidos na história S2.1. Até lá, não invente comandos.
