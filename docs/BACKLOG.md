# BACKLOG · Gate de Rollout Seguro

Versão 0.1 · 21/11/2026 · Dono do produto: o usuário (decide). PM: Claude (propõe, nunca decide).

> **Regra zero (vale para humanos e agentes):** se houver dúvida, **pare e pergunte**. Nunca decida, nunca infira. Perguntas vão para `docs/QUESTIONS.md` com opções e uma recomendação. Decisões respondidas vão para `docs/DECISOES.md`.

## 1. Como usar este arquivo

1. Escolha a próxima história **pronta** (Definition of Ready, seção 5) na ordem da seção 7.
2. Faça o pré-voo da seção 8 (escolha do tier de modelo e checagem de créditos).
3. Execute **uma história por vez**, em uma branch `story/<ID>`.
4. Só marque como feita com as evidências do Definition of Done (seção 5).
5. Ao terminar ou ao trocar de ferramenta, atualize `docs/HANDOFF.md`.

Escopo desta versão: **primeiro tudo o que pode ser feito no GitHub** (épicos E0 a E7); **depois a VPS** (E8 a E10), ainda sem provedor definido.

## 2. Fatos verificados e o que ainda não foi

| Item | Situação | Fonte |
|---|---|---|
| opencode lê `AGENTS.md`; usa `CLAUDE.md` só se não houver `AGENTS.md` | Verificado | https://opencode.ai/docs/rules/ |
| opencode não segue referências a arquivos dentro do `AGENTS.md`; use o campo `instructions` do `opencode.json` ou instrução explícita de leitura | Verificado | https://opencode.ai/docs/rules/ |
| Agentes do opencode em `.opencode/agents/<nome>.md` (frontmatter com `description`, `mode`, `model`, `tools`) na documentação V1 | Verificado (V1). A V2 usa outro formato (`agents`, `permissions`) | https://opencode.ai/docs/agents/ e https://v2.opencode.ai/agents |
| Claude Code lê `CLAUDE.md` e aceita `@AGENTS.md` como importação | Verificado | https://code.claude.com/docs/en/memory |
| Regras de proteção de deploy customizadas: públicas em todos os planos; privadas exigem Enterprise | Verificado | https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/create-custom-protection-rules |
| Rulesets: repositórios públicos no plano Free; privados exigem plano pago | Verificado | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets |
| Efetividade (detecção e falso positivo) de cada ferramenta | **Não verificado** | Fase 0 (E7) |
| Existência de API ou webhook de exportação do Claude Security | **Não verificado** | Fora do escopo do GitHub pessoal |
| Versão do opencode em uso (V1 ou V2) | **Não verificado** | Decisão D-04 |

## 3. Decisões pendentes (bloqueiam histórias)

Nenhuma delas foi decidida. Cada uma traz uma proposta, que **não vale como decisão**.

| ID | Pergunta | Proposta (a confirmar) | Bloqueia |
|---|---|---|---|
| D-01 | ✅ DECIDIDA 21/11/2026: `secure-rollout-gate`, conta pessoal | — | — |
| D-02 | ✅ DECIDIDA 21/11/2026: privado até sanitizar (S0.3). Pergunta original: visibilidade do repositório. Os documentos citam o stack de segurança do ambiente de origem. Há política organizacional sobre uso de GitHub pessoal para este tema? | Privado até sanitizar os documentos (S0.3). Público só depois, e só para o que exigir (regras de proteção de deploy) | S0.1, S0.3, S0.4, S8.8 |
| D-03 | ✅ DECIDIDA 21/11/2026: Python 3.12 + FastAPI, pytest, ruff | — | — |
| D-04 | ✅ DECIDIDA (inventário completo em 21/11/2026; ver LLM-ROUTING.md). Histórico: versão = opencode v2.1.4 (usar doc V2). Faltam provedores/modelos, créditos e plano do Claude Code. Versão do opencode (V1 ou V2), provedores e modelos disponíveis, saldo de créditos e limite do Claude Code | Preencher o inventário em `docs/LLM-ROUTING.md` | S1.2 a S1.5 |
| D-05 | ✅ DECIDIDA 21/11/2026: job de Actions primeiro; GitHub App na VPS depois (E8). Pergunta original:  Gate no GitHub sem VPS: job de Actions como check (com `GITHUB_TOKEN`) ou GitHub App | Job de Actions primeiro (E6). App na VPS depois (E8) | E6 |
| D-06 | Provedor, região e especificação da VPS (CPU ou GPU) | Decidir depois do E7. Critérios em S8.1 | E8, E9 |
| D-07 | Quais LLMs open source rodar na VPS e para qual papel | Levantamento com fontes em S9.1 | E9 |
| D-08 | ⏳ ADIADA 21/11/2026: definir após o 1º ciclo do E7, com dados medidos. Pergunta original:  Critérios numéricos: limite de falso positivo por classe, régua de severidade comum, limiar de cobertura de testes | Definir após o primeiro ciclo do E7 | S2.8, S3.2, S7.1 |
| D-09 | ✅ DECIDIDA 21/11/2026: BACKLOG.md é a fonte de verdade; issues geradas depois. Pergunta original:  Fonte de verdade das histórias: este arquivo ou GitHub Issues e Projects | Este arquivo, com issues geradas depois | S0.7 |
| D-10 | ✅ DECIDIDA 21/11/2026: sem licença por ora (repositório privado); rever ao tornar público. Pergunta original:  Licença do repositório | Nenhuma proposta (depende de D-02) | S0.5 |
| D-11 | ✅ DECIDIDA 21/11/2026: ambos (app próprio com falhas plantadas + app público para DAST). Pergunta original:  Alvos de teste: app vulnerável próprio, fork de app público (por exemplo Juice Shop) ou ambos | Ambos: próprio para SAST, SCA, IaC e segredos; público para DAST | S5.1 |
| D-12 | ✅ DECIDIDA 21/11/2026: revisão de PR por LLM open source rodando na VPS (depende de D-06, D-07; entra no E9). Pergunta original:  Revisão de PR por IA: claude-code-action (chave de API do Claude), agente do opencode ou nenhuma por ora | Nenhuma até D-04 | S2.10 |
| D-13 | ✅ DECIDIDA 21/11/2026: NO-GO prevalece sobre PENDENTE. Pergunta original:  Precedência entre PENDENTE e NO-GO. O fluxograma da Rev 4 avalia "achado de IA sem validação" antes de "alto/crítico sem exceção". Com os dois presentes, o resultado atual seria PENDENTE | Confirmar se NO-GO deveria prevalecer | S3.5 a S3.7 |
| D-14 | ✅ DECIDIDA 21/11/2026: incluir `confianca` como campo opcional. Pergunta original:  Incluir o campo `confianca` no esquema do achado (a base cita "evidência e confiança", a tabela do esquema não tem o campo) | Incluir como opcional | S3.1 |

## 4. Princípios de desenvolvimento com IA

1. **Gate determinístico antes de LLM.** Lint, testes, Semgrep, gitleaks, zizmor e `opa test` rodam antes de qualquer revisão por IA.
2. **História atômica.** Um objetivo, no máximo 3 arquivos de código novos ou alterados, aceite executável.
3. **Contexto mínimo.** O agente lê só os arquivos listados em `Ler`.
4. **Planejar e construir separados.** Plano com modelo mais forte (read-only); implementação com modelo mais barato.
5. **Revisor independente.** O revisor usa modelo diferente do implementador e não edita.
6. **Teste primeiro** nas histórias de política e de normalização.
7. **Sem inventar.** API, flag, campo ou comando só entram se estiverem em fonte registrada em `docs/refs/SOURCES.md`.
8. **Escalar ou parar.** Duas tentativas falhas: subir o tier uma vez; se falhar de novo, parar e perguntar.
9. **Dependência nova só com história ou ADR.** Versões e SHAs fixados.
10. **Nada de segredo, dado real ou código corporativo** em prompts, repositório ou testes.

## 5. Definition of Ready e Definition of Done

**Pronta (DoR):** tem todos os campos do template; nenhuma decisão pendente listada em `Bloqueada por`; `Ler` e `Saída` apontam arquivos existentes ou a criar; o aceite é um comando ou uma checagem objetiva.

**Feita (DoD):**
- Aceite executado e a saída colada em `docs/HANDOFF.md`; o humano a leva para a descrição do PR (agentes não abrem PR).
- Nenhum arquivo fora de `Escopo` alterado, exceto `docs/HANDOFF.md`, `docs/USAGE-LOG.md` e `docs/QUESTIONS.md`, sempre permitidos (`scripts/check_scope.py` quando existir, S1.8).
- Testes de regressão e gates determinísticos verdes.
- `docs/HANDOFF.md` atualizado. `docs/DECISOES.md` e `docs/refs/SOURCES.md` só se listados no `Escopo` da história; decisões só o usuário registra.
- Linha em `docs/USAGE-LOG.md`: modelo, tier, tentativas, resultado.

**Template de história:** `docs/templates/STORY.md`.

## 6. Pilha de agentes de desenvolvimento

| Agente | Função | Acesso | Tier | Observação |
|---|---|---|---|---|
| `planner` | Lê a história e produz plano de arquivos, testes e riscos | Somente leitura | T1 | Não escreve código |
| `test-author` | Escreve os testes e as fixtures primeiro | Escrita em testes | T2 | Separado do implementador, para o teste não se moldar ao código |
| `implementer` | Implementa só o plano aprovado | Escrita nos arquivos de `Saída` | T2 ou T3 | Executa o aceite e cola a saída |
| `reviewer` | Compara o diff com o aceite e o `AGENTS.md` | Somente leitura | T1, modelo diferente do implementador | Lista achados por severidade |
| `security-reviewer` | Revisa segredos, dependências, injeção, supply chain e escopo | Somente leitura, roda ferramentas | T1 | Usa os gates determinísticos como entrada |
| `doc-keeper` | Atualiza HANDOFF, DECISOES, SOURCES, USAGE-LOG | Escrita em `docs/` | T3 | Nunca altera código |

**Gates determinísticos (T0, sem LLM):** pre-commit local (formatador, lint, gitleaks), CI (testes, regressão, Semgrep, CodeQL, zizmor, Dependency Review, OSV-Scanner, `opa test`), verificação de escopo do diff.

**Regressão e qualidade:**
- Fixtures reais de saída de cada scanner, com resultado esperado (golden files).
- Tabela-verdade da política, com casos em arquivo de dados.
- Teste de propriedade: nunca GO com alto ou crítico aberto sem exceção.
- Teste de contrato: esquema do achado e OpenAPI validados no CI.

Os agentes são criados nas histórias S1.4 e S1.5, depois de D-04.

## 7. Ordem de execução (caminho crítico)

E0 → E1 → E2 → E5 (fixtures reais) → E3 → E4 → E6 → E7 → E8 → E9 → E10.

E3 pode começar o contrato e a política em paralelo ao E5, mas os parsers do E4 precisam das saídas reais do E5.

## 8. Pré-voo de cada história (início da task)

1. Ler a história e confirmar o DoR. Se faltar algo, perguntar.
2. Classificar o tier (T0 a T3, ver `docs/LLM-ROUTING.md`).
3. Consultar a tabela de roteamento e o saldo de créditos. **A escolha do modelo é proposta pelo PM e confirmada pelo usuário.**
4. Criar a branch `story/<ID>`.
5. Registrar tier e modelo no `docs/USAGE-LOG.md`.

---

## 9. Histórias

Formato: **Tier** · **Dep** (depende de) · **Bloq** (bloqueada por decisão) · **Ler** · **Saída** · **Aceite** · **Parar se**.

> **Escopo** é opcional por enquanto: está preenchido apenas nas histórias cuja `Saída` nomeia arquivos exatos; as demais seguem sem o campo (ver Q-014 em `docs/QUESTIONS.md`).

### E0 · Fundação do repositório (GitHub)

#### S0.1 · Criar o repositório no GitHub (primeira tarefa)
- **Tier:** T0 (humano) · **Bloq:** D-01, D-02
- **Ler:** `README.md`, decisões D-01 e D-02
- **Saída:** repositório vazio criado; URL registrada em `docs/DECISOES.md`
- **Escopo:**
  - `docs/DECISOES.md`
- **Aceite:** o repositório existe com o nome e a visibilidade decididos; branch padrão `main`; sem arquivos gerados automaticamente
- **Parar se:** D-01 ou D-02 sem resposta. **Não criar como público sem a resposta de D-02.**

#### S0.2 · Subir o pacote inicial
- **Tier:** T0 · **Dep:** S0.1
- **Ler:** conteúdo do `repo-inicial.zip`
- **Saída:** primeiro commit em `main` com README, AGENTS.md, CLAUDE.md e `docs/`
- **Aceite:** `git log --oneline` mostra o commit; os arquivos aparecem no GitHub; **antes do push**, `gitleaks dir .` (ou equivalente; `detect` está depreciado) sem achados
- **Parar se:** o repositório for público e S0.3 ainda não estiver feita

#### S0.3 · Sanitizar os documentos de referência
- **Tier:** T1 (revisão) + humano · **Dep:** S0.2 · **Bloq:** D-02
- **Ler:** `docs/refs/`, `docs/ARQUITETURA.md`
- **Saída:** lista de trechos que expõem o stack, o ambiente ou a estrutura corporativa; versões sanitizadas ou movidas para repositório privado
- **Aceite:** o humano aprova a lista; nenhuma menção a produto interno, nome de time ou ambiente no que for público
- **Parar se:** houver dúvida sobre o que é confidencial. Perguntar ao humano.

#### S0.4 · Proteção da branch `main`
- **Tier:** T0 · **Dep:** S0.2 · **Bloq:** D-02
- **Ler:** https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
- **Saída:** ruleset (ou proteção de branch) em `main`, conforme o que o plano permitir para a visibilidade escolhida
- **Aceite:** push direto em `main` é recusado; PR exige os checks do CI quando existirem
- **Parar se:** o recurso não estiver disponível para o plano. Perguntar a alternativa.

#### S0.5 · Arquivos básicos do repositório
- **Tier:** T3 · **Dep:** S0.2 · **Bloq:** D-10
- **Saída:** `.gitignore` (sem segredos, sem `.env`), `.editorconfig`, `LICENSE` (conforme D-10), `SECURITY.md`
- **Escopo:**
  - `.gitignore`
  - `.editorconfig`
  - `LICENSE`
  - `SECURITY.md`
- **Aceite:** os arquivos existem; `.gitignore` cobre `.env*`, chaves e artefatos locais
- **Parar se:** D-10 sem resposta

#### S0.6 · Habilitar os recursos de segurança do GitHub
- **Tier:** T0 · **Dep:** S0.2
- **Ler:** configurações do repositório (Code security)
- **Saída:** secret scanning, push protection, Dependabot alerts e code scanning ativos, no que o plano e a visibilidade permitirem; lista do que **não** ficou disponível em `docs/DECISOES.md`
- **Escopo:**
  - `docs/DECISOES.md`
- **Aceite:** captura ou texto confirmando cada recurso ativo ou indisponível
- **Parar se:** algum recurso estiver indisponível. Registrar e perguntar.

#### S0.7 · Templates de PR e issue
- **Tier:** T3 · **Dep:** S0.2 · **Bloq:** D-09
- **Saída:** `.github/pull_request_template.md` com seções: História, Aceite executado (saída colada), Arquivos alterados, Evidências, Perguntas abertas
- **Escopo:**
  - `.github/pull_request_template.md`
- **Aceite:** o template aparece ao abrir um PR
- **Parar se:** D-09 indicar Issues como fonte de verdade (muda o formato)

### E1 · Governança do desenvolvimento com IA

#### S1.1 · Inventário do opencode e dos modelos
- **Tier:** T0 (humano) · **Bloq:** D-04
- **Saída:** seção "Inventário" em `docs/LLM-ROUTING.md`: versão do opencode, provedores, modelos disponíveis, saldo e renovação de créditos, limites do Claude Code
- **Escopo:**
  - `docs/LLM-ROUTING.md`
- **Aceite:** o humano confirma o inventário
- **Parar se:** faltar qualquer dado. Não estimar.

#### S1.2 · Tabela de roteamento tier → modelo
- **Tier:** T1 (proposta) + humano · **Dep:** S1.1
- **Ler:** `docs/LLM-ROUTING.md`
- **Saída:** tabela preenchida, com modelo principal e reserva por tier, e a regra de escalonamento
- **Aceite:** o humano aprova cada linha. A proposta cita a fonte de capacidade de cada modelo e marca o que não foi verificado.
- **Parar se:** não houver fonte para uma afirmação de desempenho. Marcar "não verificado".

#### S1.3 · `opencode.json` mínimo
- **Tier:** T2 · **Dep:** S1.1 · **Bloq:** D-04
- **Ler:** documentação V2 (versão confirmada v2.1.4): índice em https://opencode.ai/docs/llms.txt; localizar a página de configuração e conferir o esquema antes de escrever
- **Saída:** `opencode.json` mínimo com `$schema` (a V2 aceita `instructions`, mas ainda não as carrega; a lista de leitura fica no `AGENTS.md`)
- **Escopo:**
  - `opencode.json`
- **Aceite:** o opencode inicia no repositório sem erro de configuração e, ao ser perguntado, cita as regras do `AGENTS.md`
- **Parar se:** o formato da versão não estiver documentado. Não copiar exemplo de outra versão.

#### S1.4 · Agentes do opencode
- **Tier:** T2 · **Dep:** S1.2, S1.3
- **Ler:** https://opencode.ai/docs/agents/ (versão confirmada)
- **Saída:** `.opencode/agents/{planner,test-author,implementer,reviewer,security-reviewer,doc-keeper}.md` no formato V2 (frontmatter com description, mode, model `provider/model`, permissions como lista de regras; corpo = prompt)
- **Escopo:**
  - `.opencode/agents/planner.md`
  - `.opencode/agents/test-author.md`
  - `.opencode/agents/implementer.md`
  - `.opencode/agents/reviewer.md`
  - `.opencode/agents/security-reviewer.md`
  - `.opencode/agents/doc-keeper.md`
- **Aceite:** o opencode lista os seis agentes; os de leitura têm `edit` negado; cada um aponta o modelo do tier aprovado na S1.2
- **Parar se:** o identificador `provider/model` do plano Go não tiver sido confirmado pelo usuário
- **Parar se:** o frontmatter divergir da doc da versão

#### S1.5 · Agentes do Claude Code
- **Tier:** T2 · **Dep:** S1.4
- **Ler:** https://code.claude.com/docs/en/sub-agents (confirmar a página antes de usar)
- **Saída:** `.claude/agents/*.md` equivalentes, **sem duplicar o texto das regras**: apontar para `AGENTS.md`
- **Aceite:** o Claude Code lista os agentes; `CLAUDE.md` importa `@AGENTS.md`
- **Parar se:** a doc dos subagentes não puder ser consultada

#### S1.6 · Protocolo de handoff opencode ↔ Claude Code
- **Tier:** T2 · **Dep:** S1.4
- **Ler:** `docs/HANDOFF.md`
- **Saída:** `scripts/handoff` que preenche o estado (branch, `git status`, última história, resultado dos testes) em `docs/HANDOFF.md`
- **Aceite:** rodar o script gera o arquivo; abrir uma sessão nova no Claude Code e pedir "continue a partir do HANDOFF" retoma sem perguntar o que já está escrito
- **Parar se:** a linguagem do script depender de D-03 (usar shell simples, sem dependências)

#### S1.7 · Registro de uso por história
- **Tier:** T3 · **Dep:** S0.2
- **Saída:** `docs/USAGE-LOG.md` com colunas: história, data, ferramenta, tier, modelo, tentativas, resultado, observação
- **Escopo:**
  - `docs/USAGE-LOG.md`
- **Aceite:** o arquivo existe e a primeira linha é de S0.2

#### S1.8 · Verificação de escopo do diff
- **Tier:** T2 · **Dep:** S1.7 · **Bloq:** D-03 (Q-007 respondida: opção A)
- **Saída:** `scripts/check_scope.py` e seu teste. A `Saída` continua sendo a descrição humana; o script lê o campo `Escopo`.
- **Escopo:**
  - `scripts/check_scope.py`
  - `tests/test_check_scope.py`
- **Interface:** `python scripts/check_scope.py --story <ID>`. Lê o campo `Escopo` da história `<ID>` em `docs/BACKLOG.md` (um caminho exato por linha, entre crases). Os arquivos alterados vêm de `git -c core.quotepath=false diff --no-renames --name-only main...HEAD` (sem detecção de renomeação, para a origem de um arquivo movido aparecer; caminhos não-ASCII sem escape; `timeout` de 30 s). Sempre permitidos, mesmo fora do `Escopo`: `docs/HANDOFF.md`, `docs/USAGE-LOG.md` e `docs/QUESTIONS.md` (lista fixa no script). `docs/DECISOES.md` e `docs/refs/SOURCES.md` só se listados no `Escopo` da história. Código de saída 0 se todos os alterados estão no `Escopo` ou na lista fixa, 1 se algum está fora (listando-os), 2 se não foi possível avaliar: a história não existe, não tem campo `Escopo`, ou o `git diff` falha (ref inexistente, fora de repositório, clone raso). Nesses casos imprime o motivo e nunca devolve 0.
- **Aceite:** teste com um diff que altera arquivo fora do `Escopo` falha (código 1); com diff dentro do `Escopo` passa (código 0); história sem `Escopo` retorna código 2; quando o `git diff` falha (por exemplo, `main` inexistente) retorna código 2 e nunca 0. O teste da falha do git usa um repositório git temporário real, não a substituição da função que lista os arquivos; mover (`git mv`) um arquivo de fora do `Escopo` para dentro dele retorna código 1, listando a origem
- **Parar se:** o campo `Escopo` da história for ambíguo, o teste exigir dependência não listada em D-03 ou o `git` não puder ser executado no ambiente de teste

#### S1.9 · Registro de fontes oficiais
- **Tier:** T3 · **Dep:** S0.2
- **Saída:** `docs/refs/SOURCES.md` completado (o pacote inicial já traz as fontes verificadas em 21/11/2026): URL, data de consulta e o que foi usado
- **Escopo:**
  - `docs/refs/SOURCES.md`
- **Aceite:** cada afirmação técnica de `AGENTS.md` e deste backlog tem fonte ou está marcada "não verificado"

#### S1.10 · Admissão de skills de terceiros
- **Tier:** T2 · **Dep:** S1.9
- **Ler:** README do SkillSpector e do Snyk agent-scan (https://github.com/NVIDIA/skillspector, https://github.com/snyk/agent-scan)
- **Saída:** procedimento em `docs/refs/ADMISSAO-SKILLS.md`: nenhuma skill ou MCP entra no projeto sem scan, commit fixado e revisão humana
- **Escopo:**
  - `docs/refs/ADMISSAO-SKILLS.md`
- **Aceite:** uma skill de teste passa pelo procedimento e o resultado é registrado
- **Parar se:** o comando da ferramenta não estiver na doc oficial


#### S1.11 · Preencher o campo Escopo nas histórias
- **Tier:** T3 · **Dep:** S1.8 · **Bloq:** nenhuma
- **Saída:** `docs/BACKLOG.md` com o campo `Escopo` em cada história que tem `Saída` com arquivos
- **Escopo:**
  - `docs/BACKLOG.md`
  - `docs/DECISOES.md`
- **Aceite:** `python scripts/check_scope.py --story <ID>` não retorna código 2 para nenhuma história com arquivos de saída; `Escopo` de cada história só lista caminhos que aparecem na `Saída` dela
- **Parar se:** a `Saída` de uma história for ambígua sobre quais arquivos criar

### E2 · Qualidade e segurança do próprio código (CI)

#### S2.1 · Esqueleto do projeto
- **Tier:** T3 · **Dep:** S0.2 · **Bloq:** D-03
- **Saída:** estrutura de pastas (`src/`, `tests/`, `policy/`, `schemas/`, `fixtures/`, `scripts/`), arquivo de dependências com versões fixadas
- **Aceite:** o comando de testes roda e passa com um teste vazio
- **Parar se:** D-03 sem resposta

#### S2.2 · CI de lint e testes
- **Tier:** T2 · **Dep:** S2.1
- **Saída:** `.github/workflows/ci.yml` com `permissions` mínimas (`contents: read`)
- **Escopo:**
  - `.github/workflows/ci.yml`
- **Aceite:** o workflow roda em PR e passa; `permissions` declaradas no topo
- **Parar se:** precisar de permissão além de leitura

#### S2.3 · Actions fixadas por SHA e Dependabot de Actions
- **Tier:** T2 · **Dep:** S2.2
- **Saída:** `uses:` com SHA de commit completo e comentário com a versão; `.github/dependabot.yml` com o ecossistema `github-actions`
- **Aceite:** nenhum `uses:` sem SHA (checagem por script ou zizmor); cada SHA **verificado** na API do GitHub, não digitado de memória
- **Parar se:** não conseguir resolver o SHA de uma action. Não inventar.

#### S2.4 · zizmor no CI
- **Tier:** T3 · **Dep:** S2.3
- **Ler:** README do zizmor (https://github.com/zizmorcore/zizmor)
- **Saída:** job que roda o zizmor nos workflows
- **Aceite:** o job passa; um workflow de teste com `pull_request_target` e checkout do PR é sinalizado

#### S2.5 · Semgrep, CodeQL e gitleaks no CI
- **Tier:** T3 · **Dep:** S2.3
- **Saída:** workflows separados, SARIF enviado ao code scanning quando disponível (S0.6)
- **Aceite:** os três rodam; achado plantado em um arquivo de teste é detectado
- **Parar se:** o CodeQL não estiver disponível para a visibilidade escolhida

#### S2.6 · Dependency Review e OSV-Scanner
- **Tier:** T3 · **Dep:** S2.3
- **Saída:** jobs de revisão de dependências no PR e varredura do arquivo de dependências
- **Aceite:** uma dependência com vulnerabilidade conhecida, adicionada em PR de teste, falha o job

#### S2.7 · Estrutura de regressão
- **Tier:** T2 · **Dep:** S2.1
- **Saída:** `fixtures/` e `tests/regression/` com o padrão golden file: entrada, saída esperada, comando para atualizar a saída esperada **somente com aprovação humana**
- **Aceite:** alterar uma saída esperada sem atualizar o golden faz o teste falhar

#### S2.8 · Limiar de cobertura
- **Tier:** T3 · **Dep:** S2.7 · **Bloq:** D-08
- **Aceite:** o CI falha abaixo do limiar decidido
- **Parar se:** D-08 sem resposta

#### S2.9 · Verificação das evidências no PR
- **Tier:** T3 · **Dep:** S0.7, S1.8
- **Saída:** job que falha se o PR não tiver as seções do template preenchidas

#### S2.10 · Revisão de IA no PR (adiada para o E9: D-12 decidiu LLM open source na VPS)
- **Tier:** T2 · **Dep:** S2.2, S9.2 · **Bloq:** D-06, D-07
- **Saída:** conforme D-12. Se for o claude-code-action: ler o README oficial e fixar por SHA
- **Aceite:** o PR de teste recebe comentário de revisão; o job **não** tem acesso a segredos além da chave necessária e **não** roda para PR de fork
- **Parar se:** a VPS e o modelo ainda não existirem

### E3 · Contratos e política (sem servidor)

#### S3.1 · JSON Schema do achado
- **Tier:** T2 · **Dep:** S2.1 · **Bloq:** D-14
- **Ler:** `docs/ARQUITETURA.md` (seção Esquema do achado)
- **Saída:** `schemas/achado.schema.json`, `fixtures/achados/validos/` (6) e `invalidos/` (6)
- **Aceite:** o validador aceita os 6 válidos e rejeita os 6 inválidos, cada inválido por um motivo diferente
- **Parar se:** um campo ou valor do esquema não estiver em `docs/ARQUITETURA.md`

#### S3.2 · Régua de severidade comum
- **Tier:** T1 (proposta) + humano · **Dep:** S3.1 · **Bloq:** D-08
- **Saída:** `docs/SEVERIDADE.md` com o mapeamento de cada fonte (SARIF `level`, CVSS, severidade da ferramenta) para crítica, alta, média e baixa
- **Escopo:**
  - `docs/SEVERIDADE.md`
- **Aceite:** o humano aprova; cada mapeamento cita a fonte da escala da ferramenta
- **Parar se:** uma ferramenta não documentar a própria escala

#### S3.3 · Contrato da API de decisão (OpenAPI)
- **Tier:** T1 · **Dep:** S3.1
- **Saída:** `api/openapi.yaml` com `GET /decisao` (parâmetros: `card` ou `sha` e `ambiente`) e resposta com `estado` (GO, NO-GO, PENDENTE), `motivos`, `ttl`, `sha`, `politica_versao`
- **Escopo:**
  - `api/openapi.yaml`
- **Aceite:** o arquivo passa em um validador de OpenAPI; exemplos de resposta para os três estados
- **Parar se:** precisar de campo que não esteja em `docs/ARQUITETURA.md`. Propor e perguntar.

#### S3.4 · Entrada e saída do OPA
- **Tier:** T1 · **Dep:** S3.1, S3.3
- **Saída:** `policy/INPUT.md` com o formato do `input` e do resultado; `fixtures/politica/*.json` de exemplo
- **Aceite:** os exemplos validam contra o esquema do achado

#### S3.5 · Política: PENDENTE por falta de avaliação ou DAST antigo
- **Tier:** T2 · **Dep:** S3.4 · **Bloq:** D-13
- **Ler:** regra de decisão em `docs/ARQUITETURA.md`; documentação do OPA da versão fixada
- **Saída:** `policy/decisao.rego`, `policy/decisao_test.rego`
- **Escopo:**
  - `policy/decisao.rego`
  - `policy/decisao_test.rego`
- **Aceite:** `opa check policy` e `opa test policy -v` passam; casos: sem avaliação → PENDENTE; fonte sem resposta → PENDENTE; `sha_coberto` diferente do SHA da release → PENDENTE
- **Parar se:** a sintaxe Rego não for validada por `opa check`. **Não escrever Rego de memória sem rodar `opa check`.**

#### S3.6 · Política: NO-GO por alto ou crítico sem exceção
- **Tier:** T2 · **Dep:** S3.5 · **Bloq:** D-13
- **Saída:** regras e testes em `policy/`
- **Aceite:** alto e crítico abertos sem exceção → NO-GO; média e baixa não bloqueiam; achado `corrigido` ou `falso positivo` não conta

#### S3.7 · Política: achado de IA sem validação
- **Tier:** T2 · **Dep:** S3.6 · **Bloq:** D-13
- **Aceite:** alto ou crítico com `origem_ia = sim` e `validacao = nenhuma` → PENDENTE; com `validacao = scanner` ou `arquiteto` conta como achado normal

#### S3.8 · Política: exceções com validade
- **Tier:** T2 · **Dep:** S3.6
- **Aceite:** exceção vigente tira o achado da conta; exceção expirada volta a contar; exceção sem aprovador é inválida

#### S3.9 · Tabela-verdade e teste de propriedade
- **Tier:** T2 · **Dep:** S3.5 a S3.8
- **Saída:** casos em `fixtures/politica/` e teste que gera combinações
- **Aceite:** propriedade "nunca GO com alto ou crítico aberto sem exceção vigente" verificada sobre todas as combinações do conjunto de teste; `opa test` verde

#### S3.10 · Revisão independente da política
- **Tier:** T1 (modelo diferente do que implementou) · **Dep:** S3.9
- **Saída:** relatório de revisão em `docs/revisoes/S3.10.md`
- **Escopo:**
  - `docs/revisoes/S3.10.md`
- **Aceite:** o humano lê e decide sobre cada achado do revisor

### E5 · Laboratório de teste e scanners no GitHub

#### S5.1 · Repositório alvo com falhas plantadas
- **Tier:** T2 · **Dep:** S0.6 · **Bloq:** D-11
- **Saída:** repositório (ou pasta) com: uma falha de injeção, um segredo falso, uma dependência com CVE conhecido, uma IaC mal configurada, cada uma **documentada em `GROUND-TRUTH.md`** (arquivo, linha, tipo, severidade esperada)
- **Aceite:** o `GROUND-TRUTH.md` lista todas as falhas; nenhum segredo é real
- **Parar se:** D-11 sem resposta

#### S5.2 · CodeQL no alvo
- **Tier:** T3 · **Dep:** S5.1 · **Saída:** workflow e SARIF em `fixtures/raw/codeql/` · **Aceite:** SARIF gerado e arquivado como artefato

#### S5.3 · Semgrep no alvo
- **Tier:** T3 · **Dep:** S5.1 · **Saída:** workflow e SARIF em `fixtures/raw/semgrep/` · **Aceite:** idem

#### S5.4 · Gitleaks e TruffleHog no alvo
- **Tier:** T3 · **Dep:** S5.1 · **Saída:** saídas em `fixtures/raw/{gitleaks,trufflehog}/` · **Aceite:** o segredo plantado é detectado, ou a ausência fica registrada

#### S5.5 · Grype e Syft no alvo
- **Tier:** T3 · **Dep:** S5.1 · **Saída:** saídas em `fixtures/raw/{grype,syft}/` · **Aceite:** a dependência vulnerável plantada aparece, ou a ausência fica registrada

#### S5.6 · Checkov no alvo
- **Tier:** T3 · **Dep:** S5.1 · **Saída:** saída em `fixtures/raw/checkov/` · **Aceite:** a IaC plantada é sinalizada, ou a ausência fica registrada

#### S5.7 · zizmor no alvo
- **Tier:** T3 · **Dep:** S5.1 · **Saída:** saída em `fixtures/raw/zizmor/` · **Aceite:** um workflow inseguro plantado é sinalizado

> Em todas as histórias E5: o agente **não corrige** as falhas plantadas e **não ajusta a ferramenta para achar mais**. O objetivo é registrar o que cada ferramenta acha, como está.

### E4 · Ingestão e normalização

#### S4.1 · Parser SARIF → achado
- **Tier:** T2 · **Dep:** S3.1, S3.2, S5.2, S5.3
- **Ler:** esquema SARIF (fonte oficial, registrar em SOURCES); `fixtures/raw/`
- **Saída:** `src/normalizador/sarif.*`, testes com golden files
- **Aceite:** SARIF do CodeQL e do Semgrep viram achados válidos no esquema; campos ausentes ficam nulos, **nunca preenchidos por suposição**
- **Parar se:** o SARIF trouxer campo sem mapeamento definido. Perguntar.

#### S4.2 · Parser Grype e Syft
- **Tier:** T2 · **Dep:** S4.1, S5.5 · **Aceite:** igual ao S4.1, com golden files

#### S4.3 · Parser Gitleaks e TruffleHog
- **Tier:** T2 · **Dep:** S4.1, S5.4 · **Aceite:** igual; segredo verificado como ativo mapeia para a severidade definida em S3.2

#### S4.4 · Parser Checkov e zizmor
- **Tier:** T2 · **Dep:** S4.1, S5.6, S5.7 · **Aceite:** igual

#### S4.5 · Vínculo achado → serviço, release e SHA
- **Tier:** T2 · **Dep:** S4.1
- **Aceite:** achado sem `servico` ou `sha` é rejeitado com erro explícito

### E6 · Gate no GitHub (sem VPS)

#### S6.1 · Job de decisão no Actions
- **Tier:** T2 · **Dep:** S3.9, S4.5 · **Bloq:** D-05
- **Saída:** workflow que baixa os achados normalizados, roda `opa eval` com a política; o resultado é o status do próprio job, que vira o check do PR (o nome do job entra como check obrigatório no ruleset, S6.2); `permissions` mínimas
- **Aceite:** em PR de teste, o job termina com sucesso para GO e falha para NO-GO e PENDENTE
- **Parar se:** a forma de publicar o check exigir permissão não documentada

#### S6.2 · Check obrigatório no ruleset do alvo
- **Tier:** T0 · **Dep:** S6.1, S0.4
- **Aceite:** com o check vermelho, o merge é bloqueado; com verde, liberado

#### S6.3 · Teste de ponta a ponta no PR
- **Tier:** T2 · **Dep:** S6.2
- **Aceite:** três PRs de teste: (a) introduz alto/crítico → bloqueado; (b) limpo → liberado; (c) corrige achado antigo → liberado. Evidências anexadas.

#### S6.4 · Comentário no PR com os motivos
- **Tier:** T3 · **Dep:** S6.1 · **Aceite:** o comentário lista o estado e os motivos, sem expor conteúdo de segredo

#### S6.5 · Ambiente `production` do alvo
- **Tier:** T0 · **Dep:** S6.2 · **Aceite:** ambiente criado; o gate de deploy customizado fica para S8.8 (depende de GitHub App)

### E7 · Avaliação de efetividade (fase 0)

#### S7.1 · Alvos e métricas
- **Tier:** T1 (proposta) + humano · **Dep:** S5.1 · **Bloq:** D-08
- **Saída:** `docs/AVALIACAO.md`: alvos, métricas (verdadeiros, falsos positivos, exclusivos por ferramenta, tempo, esforço de triagem, estabilidade) e limites de aceitação
- **Escopo:**
  - `docs/AVALIACAO.md`
- **Aceite:** o humano aprova os limites. **O agente não define limite sozinho.**

#### S7.2 · Harness de execução
- **Tier:** T2 · **Dep:** S5.2 a S5.7, S7.1
- **Saída:** workflow em matriz que roda cada ferramenta nos alvos e arquiva os resultados com data e versão da ferramenta
- **Aceite:** uma rodada completa gera todos os arquivos; a versão de cada ferramenta está registrada

#### S7.3 · Script de métricas
- **Tier:** T2 · **Dep:** S7.2
- **Saída:** `scripts/metricas.*` que compara os achados com `GROUND-TRUTH.md`
- **Aceite:** teste com resultado conhecido produz as métricas esperadas

#### S7.4 · Estabilidade das ferramentas de IA (adiada para o E9, S9.7)
- **Tier:** T2 · **Dep:** S7.3, S9.3
- **Aceite:** a mesma varredura roda 3 vezes no mesmo commit; a variação é registrada.

#### S7.5 · Relatório e decisão de entrada
- **Tier:** T1 (relatório) + humano · **Dep:** S7.3, S7.4
- **Saída:** `docs/RESULTADO-AVALIACAO.md`
- **Escopo:**
  - `docs/RESULTADO-AVALIACAO.md`
- **Aceite:** para cada ferramenta, a recomendação (bloqueia, sombra ou descarta) e o humano decide

### E8 · VPS (candidatas; detalhar após D-06)

Não executar antes de D-06. Cada item vira história completa (com o template) no momento da decisão.

- **S8.1** Critérios e escolha do provedor e da especificação (T1 propõe, humano decide)
- **S8.2** Provisionamento e hardening básico (acesso por chave, firewall, atualizações automáticas, usuário sem privilégio)
- **S8.3** Domínio, TLS e exposição mínima para o webhook
- **S8.4** Implantação da API de decisão em contêiner, com fluxo de atualização por CI
- **S8.5** Armazenamento da base de achados e backup
- **S8.6** GitHub App com permissões mínimas, assinatura do webhook validada, token de instalação (sem PAT)
- **S8.7** Check "Security Gate" publicado pelo App e ruleset aceitando só o App
- **S8.8** Regra de proteção de deploy customizada (exige repositório público no plano Free; ver D-02)
- **S8.9** Logs de auditoria de cada decisão (quem, quando, estado, motivos, versão da política)
- **S8.10** Gestão de segredos da VPS e rotação

### E9 · Agentes e LLMs open source na VPS (candidatas; após D-06 e D-07)

- **S9.1** Levantar candidatos de modelos open source por papel (revisão de PR, triagem de achados), com **fonte, licença, requisitos de hardware e evidência de desempenho**; T1 propõe, humano decide (D-07)
- **S9.2** Servir o modelo escolhido (runtime a definir após S9.1)
- **S9.3** Integrar o produtor de IA ao normalizador, com saída no esquema e `origem_ia = sim`
- **S9.4** Strix com alvo vulnerável isolado na VPS (rede segregada, sem credenciais reais, escopo autorizado)
- **S9.5** ZAP em modo baseline contra o alvo, como DAST de substituição ao DAST corporativo
- **S9.6** Regra de validação cruzada dos achados de IA antes de contarem para o NO-GO
- **S9.7** Repetição 3x e medição de variação dos produtores de IA (E7 na VPS)

### E10 · Jira simulado (candidatas; após E8)

- **S10.1** CLI que simula o validador do Jira chamando `GET /decisao`
- **S10.2** Simulação da consulta do Rovo (explica motivos e sugere remediação, somente leitura)
- **S10.3** Validador real no Jira de teste: **só depois** de confirmar na documentação da Atlassian o suporte do plano (módulo `jira:workflowValidator` está documentado como preview)

---

## 10. Riscos do próprio desenvolvimento

| Risco | Controle |
|---|---|
| Agente inventa API, flag ou campo | Fontes registradas; `Parar se`; revisão por modelo diferente |
| Agente altera arquivos fora da história | `check_scope`, revisão e DoD |
| Teste moldado ao código | `test-author` separado e golden files com aprovação humana |
| Exposição de informação corporativa no GitHub pessoal | D-02, S0.3, gitleaks no push, nada de dado real |
| Segredo ou chave de LLM vazando para o repositório | push protection, gitleaks, `.gitignore`, chave só em segredo do GitHub |
| Ferramenta comprometida (caso Trivy) | Actions por SHA, zizmor, versões fixadas, S1.10 |
| Créditos do opencode acabando no meio de uma história | Histórias atômicas, commit por história, `HANDOFF.md`, fallback no Claude Code |
| Decisão tomada pelo agente por conveniência | Regra zero, `QUESTIONS.md`, `DECISOES.md` |
