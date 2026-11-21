# Gate de Rollout Seguro

Gate de decisão **GO / NO-GO / PENDENTE** para liberar rollout. Uma API de decisão com política determinística (OPA/Rego) lê uma base de achados de segurança e devolve o veredito ao Jira, ao PR e ao deploy. Agentes de IA produzem achados; a política decide.

**Status:** planejamento. Nenhum código ainda. Stack decidida: Python 3.12 + FastAPI.

> Projeto pessoal de pesquisa. Nenhum dado, código ou segredo de terceiros deve entrar neste repositório.

## Onde está cada coisa

| Arquivo | Para quê |
|---|---|
| `AGENTS.md` | Regras para agentes de código (opencode e outros) |
| `CLAUDE.md` | Importa o `AGENTS.md` para o Claude Code |
| `docs/BACKLOG.md` | Épicos, micro histórias, decisões pendentes, pilha de agentes |
| `docs/ARQUITETURA.md` | Regra de decisão e esquema do achado (fonte da verdade) |
| `docs/DECISOES.md` | Decisões já tomadas e fatos confirmados |
| `docs/QUESTIONS.md` | Perguntas abertas, que agentes e PM fazem ao dono do produto |
| `docs/LLM-ROUTING.md` | Tiers de modelo, pré-voo e fallback para o Claude Code |
| `docs/HANDOFF.md` | Estado atual para trocar de ferramenta sem perder contexto |
| `docs/refs/` | Fontes e relatório de projetos do GitHub |
| `docs/templates/` | Modelos de história e de ADR |

## Primeiros passos

1. D-01, D-02 e D-03 já decididas (ver `docs/DECISOES.md`).
2. Executar S0.1 (criar o repositório **privado**) e S0.2 (subir este pacote).
3. Seguir a ordem da seção 7 do `docs/BACKLOG.md`.
