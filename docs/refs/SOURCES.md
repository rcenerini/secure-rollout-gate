# FONTES OFICIAIS (consultadas em 21/11/2026)

Toda afirmação técnica de código, workflow ou configuração cita uma fonte desta lista ou uma fonte lida na sessão e acrescentada aqui. **O que não está aqui é "não verificado".**

| Assunto | URL | O que foi confirmado |
|---|---|---|
| opencode: regras | https://opencode.ai/docs/rules/ | `AGENTS.md`; fallback para `CLAUDE.md`; campo `instructions` do `opencode.json` aceita globs |
| opencode: agentes (V1) | https://opencode.ai/docs/agents/ | Agentes em `.opencode/agents/<nome>.md` com frontmatter; `agent` no `opencode.json` |
| opencode: agentes (V2) | https://v2.opencode.ai/agents | Formato diferente (`agents`, `permissions`). Versão em uso confirmada: v2.1.4 (V2) |
| opencode: índice V2 | https://opencode.ai/docs/llms.txt | Índice da documentação mais recente |
| Claude Code: memória | https://code.claude.com/docs/en/memory | `CLAUDE.md` com `@AGENTS.md` |
| GitHub: regras de proteção de deploy customizadas | https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/create-custom-protection-rules | App recebe webhook; aprova ou rejeita por REST |
| GitHub: disponibilidade por plano das regras de deploy | https://docs.github.com/en/actions/how-tos/managing-workflow-runs-and-deployments/managing-deployments/configuring-custom-deployment-protection-rules | Públicas em todos os planos; privadas exigem Enterprise |
| GitHub: rulesets | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets | Públicos no Free; check obrigatório pode exigir fonte específica |
| Jira: validador de workflow (Forge) | https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-workflow-validator/ | Módulo em preview, workflows company-managed |
| Incidente Trivy (CVE-2026-33634) | https://www.rapid7.com/db/vulnerabilities/cve-2026-33634/ | Release v0.69.4 e tags das Actions comprometidas em 19/03/2026 |
| SkillSpector | https://github.com/NVIDIA/skillspector | Scanner de skills de agentes |
| Snyk agent-scan | https://github.com/snyk/agent-scan | Scanner de agentes, MCPs e skills |

| opencode V2: configuração | https://opencode.ai/v2/docs/config/ | Campo `instructions` é aceito, **mas a V2 ainda não carrega essas entradas**; instruções ativas vêm do `AGENTS.md`. `agents` e `permissions` no JSON |
| opencode V2: agentes | https://opencode.ai/v2/docs/agents/ | `.opencode/agents/<nome>.md`; frontmatter: description, mode (primary/subagent/all), model (`provider/model#variante`), permissions, steps; corpo = prompt de sistema; campos V1 obsoletos |
| opencode V2: permissões | https://opencode.ai/v2/docs/permissions/ | Regras `{action, resource, effect}` (allow/ask/deny); a última regra que corresponde vence; sem correspondência = ask; ações: read, edit, glob, grep, shell, subagent, skill, webfetch, websearch, external_directory e outras. `permissions` no nível superior do config são globais (valem também para o Build) e vêm antes das regras do agente; a regra do agente que vier depois vence. Padrão de `shell` com `*` (sem espaço antes não está confirmado: usar `git push *`). "Allow always" grava regras `allow` do projeto, que nunca vencem um `deny` configurado; onde ficam e como revogar não está na doc. A chave `policies` faz negação dura (sintaxe com duas formas na doc, não usada). A doc só mostra exemplos em `opencode.jsonc`; **confirmado por teste em 21/11/2026 (opencode v2.1.4): o `deny` global em `opencode.json` bloqueou `gh --version` e `git push --dry-run` no agente Build, sem prompt** |

| opencode Go (plano e ids) | https://opencode.ai/docs/zh-tw/go | Formato do id de modelo na configuração: `opencode-go/<model-id>`; limites do Go definidos em valor em dólar (5 horas, semanal, mensal); modelos DeepSeek V4 exigem região Global em Settings > Privacy |

**Ainda sem fonte registrada:** OPA/Rego (versão e sintaxe), SARIF, CLI de cada scanner, API Checks do GitHub, formato de `.claude/agents`. Registrar na história que usar cada um.
