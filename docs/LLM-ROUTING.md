# ROTEAMENTO DE MODELOS (custo-benefício por bloco)

**Estado:** estrutura pronta; **a tabela de modelos está vazia de propósito**. Depende de D-04 (inventário). Nenhum modelo, desempenho ou limite foi assumido neste arquivo.

## 1. Tiers por tipo de bloco

| Tier | Tipo de bloco | Exemplos no backlog | Perfil de modelo desejado |
|---|---|---|---|
| T0 | Sem LLM: ação humana ou automação | Criar repositório, configurar ruleset, gates do CI | — |
| T1 | Raciocínio forte, baixo volume | Política e contratos (S3.2 a S3.4), planos, revisão independente, revisão de segurança, relatórios de avaliação | Mais capaz; usar com contexto curto |
| T2 | Implementação com teste | Política em Rego, parsers, scripts, workflows | Bom em código; custo médio |
| T3 | Mecânico e repetitivo | Boilerplate, YAML de scanner, fixtures, documentação, templates | Rápido e barato |

## 2. Pré-voo de cada história (início da task)
1. Ler a história e o DoR (`docs/BACKLOG.md`, seções 5 e 9).
2. Classificar o tier (a história traz uma sugestão; o PM confirma).
3. Consultar a tabela da seção 4 e o saldo de créditos do opencode.
4. **O PM propõe o modelo; o usuário confirma.** Nenhum agente troca de modelo sozinho.
5. Registrar em `docs/USAGE-LOG.md`: história, ferramenta, tier, modelo.

## 3. Regras de economia
- **Planejar e construir separados:** `planner` (T1, somente leitura) e `implementer` (T2 ou T3).
- **Revisor independente** usa modelo diferente do implementador.
- **Gates determinísticos antes de LLM:** lint, testes e `opa test` rodam primeiro; o LLM só vê o que falhou.
- **Contexto mínimo:** ler só os arquivos de `Ler`; `AGENTS.md` curto; sem reler o repositório.
- **Parada de segurança:** 2 tentativas falhas → propor subir um tier; falhou de novo → parar e perguntar.
- **Histórias atômicas** limitam o custo de uma tentativa falha.
- **Medir:** `USAGE-LOG.md` registra tentativas e resultado; a cada 10 histórias, revisar com o usuário a relação tier × resultado × créditos gastos.

## 4. Tabela de roteamento (preencher na história S1.2)

| Tier | Modelo principal | Reserva | Limite de tentativas | Quem aprovou |
|---|---|---|---|---|
| T1 | opencode-go/qwen4-max | opencode-go/kimi-k3.1-pro | 2 | Usuário, 22/11/2026 (teste S1.2) |
| T2 | opencode-go/kimi-k2.7-code | opencode-go/deepseek-v4-pro | 2 | Usuário, 22/11/2026 (teste S1.2) |
| T3 | opencode-go/qwen3.8-flash | opencode-go/claude-haiku-5-5 | 2 | Usuário, 22/11/2026 (teste S1.2) |

**Base da aprovação (teste S1.2, 22/11/2026):** uma rodada por modelo; vale para este projeto, não como ranking geral. Resultados em `docs/USAGE-LOG.md`.
- **T2:** os três passaram o aceite da S1.8 em 1 tentativa. O `kimi-k2.7-code` previu no plano a falha do git (fail-closed); o `deepseek-v4-pro` deixou fail-open; o `glm-5.3` ficou sem veredito (rodada contaminada). Ressalva: o kimi fez push e abriu PR antes do bloqueio; agora negado por `opencode.json`, `implementer.md` e `AGENTS.md`.
- **T3:** os três não inventaram fonte. `qwen3.8-flash` e `claude-haiku-5-5` ficaram sem web (cobertura 60 e 36 afirmações). `deepseek-v4.1-flash` só se a tarefa exigir web (usou web liberada por padrão; 84 afirmações, 11 URLs novas, 73 requests).
- **T1:** os dois acharam o fail-open sem dica. `qwen4-max` foi o mais completo (prova por execução, 27 requests, mensal +2 pontos); `kimi-k3.1-pro` custou +5 pontos do mensal em 11 requests.
- **Pendências desta tabela:** os arquivos `.opencode/agents/*.md` ainda não têm `model:`; o `deny` de web no `opencode.json`; revisor ≠ implementador continua valendo (T1 revisa T2 de outra família).

### Inventário (S1.1, preenchido em 21/11/2026 com dados informados pelo usuário)
- **opencode:** v2.1.4 (documentação V2)
- **Plano no opencode:** "Go" (painel do usuário). Renova em 24/11 (faltam ~3 dias).
- **Uso até 21/11:** mensal 50% usado (ritmo para 56%); semanal 0% (reinicia em ~1 dia); janela de 5 horas 0%. 474 requisições, 208,5 M de tokens, 100% em DeepSeek V4 Pro.
- **Uso extra:** desligado; o painel mostra crédito disponível de 0,00. Ao atingir o limite, as requisições pausam.
- **Provedores conectados no opencode (tela "Conectar provedor"):** OpenCode Go (plano de assinatura) e OpenCode Console (catálogo avulso, grupo "OpenCode" no seletor). Segundo a documentação oficial do Go, o id de modelo na configuração usa o formato `opencode-go/<model-id>`; por exemplo `opencode-go/deepseek-v4-pro`. **Usar só modelos do grupo Go.** O grupo "OpenCode" é o catálogo avulso e pode consumir crédito; o id desse grupo (provavelmente `opencode/<model-id>`, não confirmado na doc oficial) não deve ser usado.
- **Modelos incluídos no plano Go** (lista informada pelo usuário em 21/11/2026): beam-free, claude-haiku-5-5, deepseek-v4-pro, deepseek-v4.1-flash, gemini-4-argon, glm-5.3, glm-5.3-flash, gpt-5.6-luna, gpt-6-luna, grok-4.7, hy3, hy4, hy4-flash-free, hy4-preview, iceman-contributor-free, kimi-k2.7-code, kimi-k3, kimi-k3.1-pro, longcat-2.0, longcat-2.5-free, mimo-v2.5, mimo-v2.5-pro, mimo-v2.6-flash, mimo-v2.6-pro, minimax-m3, minimax-m3.1-flash, muse-spark-1.2-contributor, muse-spark-1.3-contributor, qwen3.7-plus, qwen3.8-flash, qwen3.8-max, qwen4-max, step-5-preview.
- **Fora do plano Go** (só no catálogo completo, `docs/refs/opencode-catalogo-modelos.md`): Claude Sonnet, Opus e Fable, GPT-5.x e GPT-6.x (exceto os Luna acima), demais Gemini. Usá-los exigiria uso extra, hoje desligado.
- **Modelos gratuitos (-free, contributor):** liberados pelo usuário em 21/11/2026 para todo o código do projeto, porque ainda não há dado produtivo. Revisar a regra antes de qualquer dado real.
- **Claude Code (fallback):** conta Claude **Pro** pessoal (painel de 21/11/2026): sessão atual 17% usada (reinicia 13:30); semana 6% usada (reinicia quinta 16:00). Créditos de uso: R$ 0; uso extra ativado, com limite de gastos mensal de R$ 30 (R$ 0 gastos). Recarga automática desativada.
- **Não verificado:** se o limite do Pro é compartilhado entre chat e Claude Code (confirmar em support.claude.com); o que cada limite do Go significa em requisições ou tokens; desempenho de cada modelo para as tarefas do projeto.

### Proposta de candidatos por tier (NÃO APROVADA; só nomes do plano Go, sem evidência de desempenho)
| Tier | Candidatos a testar (todos do plano Go) | Observação |
|---|---|---|
| T1 | kimi-k3.1-pro, qwen4-max, mimo-v2.6-pro, deepseek-v4-pro | Reasoning e revisão: testar nas mesmas 3 histórias e comparar |
| T2 | deepseek-v4-pro (já em uso), kimi-k2.7-code, glm-5.3, minimax-m3 | Código com testes |
| T3 | claude-haiku-5-5, deepseek-v4.1-flash, qwen3.8-flash, glm-5.3-flash, gratuitos | Boilerplate, YAML, fixtures, docs |
| Revisor | Modelo de outra família que o implementador | Regra: revisor ≠ implementador |

Para evitar confiar em nome de modelo, a S1.2 inclui um **teste prático**: a mesma história pequena executada em 2 ou 3 candidatos por tier, comparando aceite, tentativas e tokens gastos. O usuário aprova cada linha.

## 5. Fallback para o Claude Code (quando os créditos do opencode acabam)
1. O agente atual faz commit do que está pronto e roda `scripts/handoff` (S1.6) ou preenche `docs/HANDOFF.md` à mão.
2. No Claude Code, abrir o repositório; o `CLAUDE.md` importa o `AGENTS.md`.
3. Pedir: "Leia `docs/HANDOFF.md` e continue do Próximo passo."
4. Preferir, no Claude Code, as histórias que forem ser retomadas com menos contexto (T3 e T2 já planejadas). A distribuição por tier no Claude Code é **decisão pendente** (D-04).
5. Ao voltar ao opencode, o HANDOFF faz o caminho inverso.

## 6. Fora do escopo deste arquivo
Preços, comparativos de desempenho e escolha de modelos open source da VPS (S9.1, D-07). Nada disso foi pesquisado nem assumido.
