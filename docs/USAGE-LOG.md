# USAGE-LOG

Um registro por história. Colunas: história, data, ferramenta, tier, modelo, tentativas, resultado, observação.

| História | Data | Ferramenta | Tier | Modelo | Tentativas | Resultado | Observação |
|---|---|---|---|---|---|---|---|
| S0.2 e S0.5 | 21/11/2026 | Chat (Claude) + execução manual | T0/T3 | claude-sonnet-5-5 | 1 | concluída | Arquivos preparados no chat; push feito pelo usuário |
| S1.8 | 21/11/2026 | opencode v2.1.4 | T2 (planner T1) | opencode-go/kimi-k2.7-code | 1 | concluída | `scripts/check_scope.py` e `tests/test_check_scope.py` criados; aceite executado com Python 3.12.8 (Astral/uv). Códigos de saída manual: 0 (S1.8), 2 (S1.3), 1 (README.md temporário fora do escopo) |
| S1.8 (teste S1.2, rodada 1) | 21/11/2026 | opencode v2.1.4 | T2 | opencode-go/deepseek-v4-pro | 1 | parou e perguntou (Q-007) | Sem código; só `docs/QUESTIONS.md` alterado (+11 linhas). Consumo: 14 requests, cerca de 0,5 M tokens (painel arredonda em 0,1 M), 5h +4%, semanal +1%, mensal 50% sem mudança visível. Perguntas pertinentes (convenção do `Saída`; base do diff). Afirmações sobre o BACKLOG (§9, histórias sem `Saída`) não verificadas. Evidência na branch `teste/S1.8-deepseek-v4-pro` (não mergear). |
| S1.8 (teste S1.2, rodada 1b) | 21/11/2026 | opencode v2.1.4 | T2 | opencode-go/deepseek-v4-pro | 1 | parou e perguntou (Q-008, Q-009) | Sem código. Alterou `docs/DECISOES.md` e `docs/QUESTIONS.md` (fora do `Escopo` da S1.8, por contradição do DoD, que gerou a Q-008). Não registrou Q-008 e Q-009 no `QUESTIONS.md` antes de parar. Consumo: 14 requests, cerca de 0,4 M tokens, 5h +4, semanal +2, mensal +1. Evidência na branch `teste/S1.8b-deepseek-v4-pro` (não mergear). |
