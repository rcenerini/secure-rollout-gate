# ARQUITETURA (resumo normativo)

Fonte completa e diagramas: a versão completa da arquitetura (mantida em arquivo privado) (Revisão 4). As revisões anteriores ficam em arquivo privado. **Em caso de divergência, vale este arquivo; divergências viram pergunta em `QUESTIONS.md`.**

## 1. Princípio
Agentes de IA produzem achados. Uma política determinística decide. O Rovo (agente do Jira) só consulta e explica; nunca decide nem move o card.

## 2. Camadas
1. **Produtores de achados:** design e arquitetura (IA, exigem validação), PR e código (IA e regras), scanners determinísticos, compliance.
2. **Ingestão:** normalizador (esquema único, régua de severidade comum, vínculo achado → serviço/release/commit) e etapa de validação.
3. **Base de achados** e registro de exceções.
4. **Decisão:** motor de política (OPA/Rego, versionado em Git) e API de decisão (fonte única do veredito).
5. **Consumidores:** Jira (validador de workflow), Rovo (somente leitura), GitHub (check do PR, merge, deploy) e auditoria.

## 3. Estados
- **GO:** existe avaliação válida e não há achado alto ou crítico aberto sem exceção vigente.
- **NO-GO:** há achado alto ou crítico aberto sem exceção vigente.
- **PENDENTE:** falta avaliação, fonte não respondeu, DAST anterior à release ou achado de IA alto/crítico sem validação. Bloqueia (fail-closed).

## 4. Regra de decisão (D-13: NO-GO prevalece)
1. Existe alto ou crítico aberto sem exceção vigente, confirmado (determinístico ou de IA já validado) → **NO-GO**
2. Não existe avaliação válida (design, código e DAST no prazo; fontes responderam) → **PENDENTE**
3. Existe alto ou crítico de IA sem validação → **PENDENTE**
4. Caso contrário → **GO**

**Frescor do DAST:** o resultado do DAST só conta se `sha_coberto` for igual ao SHA que vai para produção. Scan mais antigo que a release ou em andamento → PENDENTE.

**Validação de achado de IA:** só bloqueia após corroboração por scanner, confirmação do arquiteto ou evidência verificável (arquivo:linha). Antes disso, PENDENTE.

## 5. Três pontos de controle
| Ponto | O que decide | Efeito |
|---|---|---|
| PR e merge | Achado novo alto/crítico introduzido pelo diff | Bloqueia o merge |
| Card para Rollout | Estado completo do serviço e da release | Bloqueia a transição |
| Deploy em produção | Estado atual, no SHA exato | Bloqueia o job |

O veredito vale para um SHA e expira (TTL). Achado novo entre merge e deploy exige nova decisão. O DAST roda em homologação e pesa no card e no deploy, não no PR.

## 6. Esquema do achado
| Campo | Valores / conteúdo |
|---|---|
| `servico`, `release`, `sha` | Identificadores |
| `fonte`, `tipo` | Ferramenta; design, código, infra, compliance |
| `severidade` | crítica, alta, média, baixa (régua comum, D-08) |
| `status` | aberto, corrigido, exceção, falso positivo |
| `origem_ia`, `validacao` | sim/não; nenhuma, scanner, arquiteto |
| `evidencia` | link, arquivo:linha ou trecho do documento |
| `excecao_id`, `validade`, `aprovador` | Registro de aceite de risco; exceção expira e tem dono |
| `escaneado_em`, `sha_coberto` | Data do scan e SHA coberto (regra de frescor) |
| `dono`, `prazo` | Time responsável; data |

Campo `confianca` (opcional, D-14 decidida): incluído no esquema.

## 7. API de decisão (rascunho a validar em S3.3)
`GET /decisao` com `card` ou `sha` e `ambiente`. Resposta: `estado` (GO, NO-GO, PENDENTE), `motivos`, `ttl`, `sha`, `politica_versao`. **Não implementar antes de S3.3.**

## 8. Ferramentas propostas por categoria (não validadas)
Seleção por maturidade (atividade, licença, histórico, incidentes). **A efetividade ainda não foi medida (E7).**

| Categoria | Escolhida | Reserva |
|---|---|---|
| SAST | CodeQL, Semgrep | — |
| Segredos | Secret Protection, TruffleHog | Gitleaks |
| Imagens, SCA, IaC | Grype, Syft, OSV-Scanner, Checkov, Kubescape | Trivy (só com digest fixado; comprometido em mar/2026) |
| DAST e pentest | Strix, Nuclei; ZAP no lugar do DAST corporativo nesta PoC | Shannon, PentAGI |
| Revisão por IA | claude-code-action (D-12) | PR-Agent |
| Skills e MCPs | SkillSpector, Snyk agent-scan | — |
| Pipeline | zizmor, OpenSSF Scorecard, Actions por SHA | — |
| Política | OPA | — |

## 9. Fora do escopo desta PoC
scanner SAST/SCA comercial, CSPM, DAST corporativo, Claude Security e Jira com Rovo reais (a PoC usa o GitHub pessoal e uma VPS; o Jira é simulado).
