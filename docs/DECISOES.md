# DECISÕES

Registro de decisões e fatos. Só o dono do produto decide. Agentes **não** acrescentam decisões por conta própria: propõem em `QUESTIONS.md`.

## Confirmadas pelo usuário (até 21/11/2026)

| # | Decisão ou fato | Observação |
|---|---|---|
| C-01 | O Jira permite validador de workflow e o Rovo consegue chamar a API | Ambiente corporativo, fora da PoC |
| C-02 | O DAST vem do DAST corporativo (não do scanner SAST/SCA comercial) | Ambiente corporativo |
| C-03 | Code Security e Secret Protection do GitHub já estão licenciados | Ambiente corporativo |
| C-04 | O Claude Security substitui o Codex Security como produtor de varredura por IA | Beta; entra em sombra |
| C-05 | Prioridade de desenvolvimento: primeiro o que for possível no GitHub; depois a VPS | VPS ainda não escolhida |
| C-06 | Desenvolvimento principal no opencode; Claude Code quando os créditos do opencode acabarem | Detalhes em `LLM-ROUTING.md` |
| C-07 | Modelos escolhidos por custo-benefício do bloco a desenvolver, decididos no início da task | Tiers em `LLM-ROUTING.md` |
| C-08 | LLMs na VPS devem ser open source, os que melhor se encaixarem no contexto | Levantamento em S9.1 |
| C-09 | Nenhum agente ou PM decide ou infere em caso de dúvida; sempre pergunta e propõe | Regra zero |
| C-10 | A primeira tarefa é criar o repositório no GitHub e subir projeto, tarefas, arquitetura e decisões | S0.1 e S0.2 |

## Decisões do dono do produto (21/11/2026)

| # | Decisão | Efeito |
|---|---|---|
| D-01 | Repositório `secure-rollout-gate`, conta pessoal do GitHub | Libera S0.1 |
| S0.1 | Repositório criado: https://github.com/rcenerini/secure-rollout-gate (21/11/2026). Visibilidade a confirmar como Private no GitHub | Libera S0.2 |
| D-02 | Privado até sanitizar os documentos (S0.3) | Nada público antes da S0.3; S8.8 será revisitada |
| D-03 | Python 3.12 + FastAPI, pytest e ruff | Libera S2.1; versões de bibliotecas serão fixadas na S2.1 com fonte |

| D-04 | ✅ opencode v2.1.4 (V2); plano Go com lista de modelos; modelos gratuitos liberados; Claude Code no plano Pro pessoal. Faltam só a aprovação dos modelos por tier (S1.2) | S1.3 e S1.4 usam a doc V2 |
| S0.3 | Dispensada por ora: o usuário informou que nada é confidencial e que o repositório fica privado (21/11/2026). **Rever antes de tornar o repositório público** | S0.3 volta a valer na mudança de visibilidade |
| S0.2 | Pacote inicial enviado ao repositório; gitleaks 8.30.1 sem achados (21/11/2026) | Libera S0.4 a S0.7 e E1 |
| D-02 (revisada) | 21/11/2026: o usuário decidiu tornar o repositório público após sanitizar e recriar. As HTML das revisões 3 e 4 ficam só em arquivo privado | Substitui "privado até sanitizar"; S0.4 passa a usar proteção de branch do GitHub Free em repositório público |
| S0.4 | Ruleset `protecao-main` ativo (sem exclusão de deleção, sem force push, PR obrigatório com 0 aprovações). Push direto na `main` recusado (21/11/2026). Definição em `.github/rulesets/protecao-main.json` | Falta incluir o check obrigatório na S2.2/S6.2 |
| S0.6 | Painel Advanced Security em 21/11/2026: ativos dependency graph, Dependabot alerts, malware alerts, security updates (agrupados), push protection. Ativos também recursos de IA do GitHub (AI Scan de repositório e de PR, scan de apps de IA, Copilot Autofix, Agentic autofix), que o painel diz consumirem créditos de IA. Pendentes: private vulnerability reporting (estado não informado), CodeQL (S2.5), Dependabot version updates (S2.3) | Decisão do usuário: desligar os recursos de IA por ora; reavaliar no E7. Private vulnerability reporting: ligado |
| S1.6 | Script de handoff em PowerShell (`scripts/handoff.ps1`); a adaptação para o ambiente corporativo (GitHub Enterprise) fica fora do escopo deste projeto por ora (21/11/2026) | Libera S1.6 |
| S1.3/S1.4 | Validação no opencode (app): os seis agentes do projeto aparecem. Apareceram também 16 agentes externos ao repositório (provavelmente globais do usuário). Decisão do usuário (21/11/2026): desativar 13 deles neste projeto via `opencode.json` (`disabled: true`); `explore` e `general` (embutidos) foram mantidos | A sua configuração global não é alterada |
| S1.3 | Validada em 21/11/2026: o opencode carregou o AGENTS.md do projeto e citou a Regra zero. Carregou também o AGENTS.md global do usuário. Decisão do usuário: o projeto prevalece em conflito, e o conflito vira pergunta (regra acrescentada ao AGENTS.md) | Fecha a S1.3 |
| S1.2 | Teste prático de modelos aprovado pelo usuário em 21/11/2026 (protocolo em `docs/testes/S1.2-protocolo.md`) | Inicia a S1.2 |
| D-05 | Gate no GitHub via job de Actions primeiro; GitHub App na VPS depois | Libera E6 |
| D-08 | Limites numéricos adiados para depois do 1º ciclo do E7 | S2.8, S3.2, S7.1 seguem bloqueadas até lá |
| D-09 | BACKLOG.md é a fonte de verdade das histórias | Libera S0.7 |
| D-10 | Sem licença por ora | Libera S0.5 sem LICENSE |
| D-11 | Alvos: app próprio com falhas plantadas e app público para DAST | Libera S5.1 |
| D-12 | Revisão de PR por IA com LLM open source na VPS | S2.10 e S7.4 movidas para o E9 |
| D-13 | NO-GO prevalece sobre PENDENTE | Libera S3.5 a S3.7; ordem da regra muda |
| D-14 | Campo `confianca` opcional no esquema | Libera S3.1 |

## Direções propostas (ainda não aprovadas formalmente)

Princípio "IA produz achado, política decide"; três pontos de controle; estados GO, NO-GO e PENDENTE com bloqueio por padrão; seleção de ferramentas por maturidade; fase 0 de avaliação de efetividade antes de qualquer bloqueio.

## Decisões pendentes
Ver `docs/BACKLOG.md`, seção 3 (D-01 a D-14).

## Registro de ADRs
Modelo em `docs/templates/ADR.md`. Nenhum ADR ainda.
