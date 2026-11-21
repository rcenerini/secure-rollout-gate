# Varredura GitHub — agentes e LLMs para análise ágil de cibersegurança e arquitetura em projetos de negócio

Data da varredura: 20/11/2026. Estrelas (★), data do último push e licença vêm da API de busca do GitHub no dia da varredura.

## 1. Como a varredura foi feita

- Cerca de 190 consultas na busca de repositórios do GitHub, em três rodadas, ordenadas por estrelas e por atualização. Cobriram threat modeling, security architecture/design review, requisitos de segurança, appsec e DevSecOps, GRC e compliance (PCI DSS, LGPD, ISO 27001, NIST, OSCAL), IaC/cloud, MCP e skills, e governança de agentes.
- Resultado: cerca de 2.900 repositórios únicos. Mantive só os com push desde jun/2025 e não arquivados, depois pontuei por relevância.
- Li o README de cerca de 85 candidatos e descartei ruído (spam, forks e listas de portfólio sem código).
- **Limites:** não executei nenhuma ferramenta, então a avaliação é por README e metadados. A busca de código e as páginas github.com não estavam acessíveis no ambiente. Repositórios com 0–20★ são, em sua maioria, projetos de um autor só, criados em 2026. Trate-os como desenhos de referência, não como produto.

## 2. Conclusões

1. **Threat modeling com agente de código virou a categoria mais povoada.** O padrão dominante é um agente que lê repositório, diagrama ou documento de design e devolve um modelo STRIDE/LINDDUN/MAESTRO com evidência citada. Isso roda dentro do Claude Code, Codex, Copilot ou Gemini CLI.
2. **A ponta de "revisão de arquitetura sobre documentos de projeto" é a menos madura.** Lysis, secfoo, ThreatWeaver, Yrek/TMSupportAgent e DocSentinel são os que aceitam docs, diagramas, Jira e Confluence como entrada. Quase todos têm pouca tração.
3. **Não há projeto open source maduro específico para PCI DSS, regulação do setor financeiro.** Só achei skills de PCI com 0–1★ e um plugin de "second line" para serviços financeiros com 2★. LGPD tem uma opção boa (lgpd-skills, 287★). Isso sustenta construir sobre a sua base de requisitos de segurança já existente, e não adotar algo pronto.
4. **Os padrões que valem copiar** aparecem repetidos nos melhores projetos:
   - saída ancorada em evidência (`arquivo:linha` ou documento citado);
   - validação determinística depois do LLM;
   - aprovação humana (HITL);
   - saídas SARIF, JSON e Threat Dragon/OTM para ligar a CI e backlog;
   - modos "PR-scoped" e "atualização iterativa", em vez de modelo único.

## 3. Catálogo

### A. Threat modeling e revisão de arquitetura com LLM/agentes (núcleo do tema)

| Repositório | ★ | Push | Licença | O que faz | Observação |
|---|---|---|---|---|---|
| secfoo-com/secfoo | 387 | 20/11/26 | MIT | CLI que usa o agente já instalado (Claude Code, Codex, Gemini, Copilot…) para SAST, secrets, SCA, threat modeling e architecture review, usando design docs, Confluence e tickets como contexto. Checklist e formato de relatório fixos. | Melhor aderência ao fluxo "contexto de projeto de negócio". Existe um fork idêntico (Sagar264offici/secfoo), ignorar. |
| jmanico/grim-prompter | 610 | 08/11/26 | MIT | 36 workflows de arquitetura e 29 prompts de método. Threat model rastreado ao código, com workflows de privacidade. | Só prompts, fácil de adaptar. |
| RedHatProductSecurity/agentic-threat-modeling | 15 | 11/08/26 | Apache-2.0 | Módulo para Claude Code/Cursor/Gemini. Seis frameworks (STRIDE, PASTA, LINDDUN, VAST, Attack Trees, OCTAVE), perfil automático de atacantes, cinco modos (inclusive revisão por PR e atualização iterativa). | Poucas estrelas, mas é de um time de product security corporativo e o desenho é o mais completo. |
| davidmatousek/tachi | 97 | 20/11/26 | Apache-2.0 | Harness para Claude Code: STRIDE + IA + MAESTRO, com agentes de detecção cobrindo OWASP LLM, Agentic, ML Top 10 e outros. | Forte para sistemas com IA. |
| aws-samples/sample-agentic-attack-tree-generator (ThreatForest) | 81 | 30/10/26 | MIT-0 | Multi-agente (Strands) que gera attack trees a partir de um repositório e mapeia para MITRE ATT&CK. Tem paper. | Exemplo AWS, bom como referência de arquitetura. |
| jumpycastle/lysis | 12 | 24/10/26 | Apache-2.0 | Recebe docs de arquitetura, DFDs, diagramas, PDFs, screenshots e código opcional. Devolve achados prontos para ticket, decisão de go-live, relatório e diagrama interativo. Roda na API do Claude. | O mais próximo de "triagem de projeto antes do comitê". |
| mrwadams/stride-gpt | 1.156 | 19/11/26 | MIT | Clássico: descreve a aplicação e gera STRIDE e attack trees. Tem modo REPL e seção de enterprise deployment. | Maduro e ativo. Mais "formulário" do que agente sobre o seu repositório. |
| fr33d3m0n/threat-modeling | 353 | 12/05/26 | BSD-3 | Skill "code-first" v3.2: DFD automático, análise CFG/DFG, integração CodeQL, Joern e Ghidra via MCP. | Pesado. Mistura threat model com auditoria e engenharia reversa. |
| monte-carlo-data/secure-design-practicum | 8 | 03/11/26 | MIT | Guias, checklists e GitHub Actions para revisar System Design Documents. | Boa referência de processo de revisão de SDD. |
| Yrek/TMSupportAgent | 3 | 19/05/26 | NOASSERTION | Lê diagrama, markup ou texto, monta o modelo, deixa o humano corrigir e roda análise multi-método. Entrega backlog priorizado. | Fluxo humano-no-loop bem pensado. Licença não declarada. |
| HardikS0lanki/ThreatWeaver-AI | 0 | 05/09/26 | MIT | Transforma diagramas, repositórios, Jira, Confluence e texto em threat model, com validação determinística e "evidência ou premissa declarada". | Imaturo, mas o desenho (evidence-first) é o certo. |
| theAstiv/paranoid | 9 | 19/11/26 | Apache-2.0 | STRIDE + MAESTRO iterativo (1–15 passadas), aprovar/rejeitar por humano. Suporta Anthropic, OpenAI, Ollama (air-gapped) e Bedrock. | Self-hosted, útil se houver restrição de dados. |
| amitkr91221/Security-Threat-Modelling | 0 | 10/09/26 | MIT | Enxame multiagente com lentes STRIDE/LINDDUN/OWASP/LLM, correlação de achados e validação contra o código. Exporta SARIF, OTM e Threat Dragon. | O desenho "o enxame não corrige a própria prova" vale estudar. |
| cognis-digital/castellan | 0 | 28/06/26 | NOASSERTION | Threat model offline, nativo de MCP. STRIDE + LINDDUN, DREAD, attack trees e mapeamento a 600+ controles, a partir de spec ou IaC. | Imaturo. |
| AlexaDeWit/Saerskriven | 0 | 20/11/26 | Apache-2.0 | Modelo de ameaças como arquivo versionado junto do código, editável por humano e por agente via MCP. | Ideia boa: threat model como artefato vivo no repositório. |
| khirawdhi/archsec-reviewer | 0 | 12/11/26 | NOASSERTION | Análise determinística de arquitetura em YAML: fluxos, caminhos de ataque multi-hop, SARIF. | Sem LLM no núcleo. Serve de base determinística. |
| FlyS3c/secarch-copilot | 0 | 10/11/26 | MIT | RAG local e somente leitura que produz rascunhos citados de revisão de arquitetura, com recuperação filtrada por autorização. | Demonstra bem controles de acesso no RAG de referências. |
| shahvatsalofficial/archsutra-ai | 4 | 16/11/26 | Apache-2.0 | Agente de arquitetura (audit/design/threat-model) com provas `arquivo:linha`, 12 papéis especialistas. | Foco mais amplo que segurança. |
| rahozosman/security-claude | 1 | 30/08/26 | MIT | Skill de "security architecture intelligence": fluxo UNDERSTAND→MAP→TRUST BOUNDARIES→THREAT MODEL→VERIFY→FIX, baseado em ASVS, SAMM, SSDF e CISA Secure-by-Design. | Boa estrutura de raciocínio de arquiteto. |
| vankhangfet/threat-model-skills | 1 | 17/11/26 | MIT | Três skills: rascunha STRIDE em formato Threat Dragon, transforma ameaças em requisitos de segurança com IDs e backlog, e confere PRs contra o modelo. | Cobre o elo ameaça → requisito → PR. |
| owaspcornucopia/ThreatSutra | 4 | 16/11/26 | AGPL-3.0 | Gera requisitos de segurança a partir de modelos Threat Dragon e cartas Cornucopia, usando a sessão de gamificação como entrada. | Alinhado a requisitos como saída. |
| OWASP/www-project-lets-threat-model | 13 | 02/02/26 | NOASSERTION | Ferramenta agêntica de threat modeling para fluxos ágeis. Lê YAML de ativos, analisa o repositório e gera relatório em Markdown, JSON ou SARIF. | Projeto OWASP, pouco movimento. |
| Ansvar-Systems/regulatory-threat-model-skill | 1 | 06/11/26 | NOASSERTION | STRIDE + LINDDUN com triagem de obrigações regulatórias da UE (GDPR, NIS2, CRA, AI Act) e dados de CVE/KEV/EPSS ao vivo. | Padrão útil para cruzar threat model com regulação. Foco UE. |
| Cy-S3c/secure-by-design-skills | 0 | 30/10/26 | MIT | Duas skills do documento de planejamento até um STRIDE revisável, com checagem mecânica. | |
| takashi-ohmoto-git/CyberRiskScape | 21 | 17/11/26 | Apache-2.0 | Camada de contexto de segurança sobre threat modeling: correlaciona ASM, CSPM, vulnerabilidades e identidade em caminhos de ataque. | Ideia próxima de integração de visibilidade. |
| InfosecOTB/threat-dragon-ai-tool, LuizBoina/dragon-gpt | 8 / 45 | 03/26 / 06/25 | Apache-2.0 / MIT | LLM sobre modelos OWASP Threat Dragon (STRIDE e mitigações). | dragon-gpt está parado desde jun/2025. |

**Bases não-LLM (base para alimentar os agentes):** OWASP Threat Dragon (1.694★), OWASP pytm (1.200★), AWS threat-composer (798★), Threagile (787★, YAML, último push abr/2026). Os agentes acima exportam ou leem vários desses formatos.

### B. Revisão de segurança em código, PR e SDLC com agentes

| Repositório | ★ | Push | Licença | O que faz |
|---|---|---|---|---|
| anthropics/claude-code-security-review | 7.041 | 11/02/26 | MIT | GitHub Action oficial: revisão de segurança de PR com Claude, por diff, comentando nos PRs. |
| Kaademos/secure-sdlc-agents | 15 | 30/07/26 | MIT | 8 subagentes por fase: requisitos (ASVS), threat modeling, code review, IaC, compliance, gate de release. |
| arthurpanhku/DocSentinel | 90 | 18/11/26 | MIT | Plataforma SSDLC com agentes (LangGraph) que revisa documentos, formulários, questionários e relatórios, de requisitos a operação. Muito aderente à triagem de projetos. |
| google/mantis | 2.814 | 19/11/26 | Apache-2.0 | Toolkit para agentes acharem, reproduzirem e corrigirem vulnerabilidades. Exige ambiente isolado. |
| dmdhrumilmistry/indra | 44 | 19/11/26 | MIT | Harness multiagente de revisão appsec (mapeia, caça, encadeia, verifica impacto). |
| nb1b3k/SecureFlow-AI | 5 | 18/05/26 | AGPL-3.0 | Revisor de PR que combina scanners determinísticos e raciocínio de LLM, com gate PASS/WARN/FAIL e SARIF. |
| UnitOneAI/SecuritySkills | 115 | 18/06/26 | MIT | Skills ancoradas em OWASP, NIST, MITRE e CIS, para evitar controles inventados. |
| ghostsecurity/skills | 446 | 28/09/26 | Apache-2.0 | Marketplace de skills de appsec para Claude Code. |
| agamm/claude-code-owasp | 457 | 03/11/26 | MIT | Skill OWASP (Top 10:2025, ASVS 5.0, Agentic). |
| trailofbits/skills | 8.320 | 20/11/26 | CC-BY-SA-4.0 | Skills da Trail of Bits para pesquisa de segurança e auditoria. |
| mukul975/Anthropic-Cybersecurity-Skills | 36.463 | 31/08/26 | Apache-2.0 | Biblioteca enorme de skills mapeadas a MITRE ATT&CK, NIST CSF, ATLAS, D3FEND e outros. Mantido por um usuário individual, apesar do nome. |
| AgentSecOps/SecOpsAgentKit | 238 | 15/04/26 | NOASSERTION | Skills de AppSec, DevSecOps e IaC para Claude Code. |
| chainloop-dev/chainloop | 615 | 20/11/26 | Apache-2.0 | Guardrails e registros assinados do SDLC, inclusive de sessões de agentes de código. |

### C. GRC, compliance e privacidade (PCI, LGPD, ISO, NIST)

| Repositório | ★ | Push | Licença | O que faz |
|---|---|---|---|---|
| intuitem/ciso-assistant-community | 4.656 | 20/11/26 | NOASSERTION (verificar) | Plataforma GRC aberta: risco, appsec, compliance, auditoria, TPRM, privacidade. A mais madura da lista. |
| trycompai/comp | 2.104 | 18/11/26 | AGPL-3.0 | Plataforma de compliance com IA (SOC 2, ISO 27001, HIPAA, GDPR). Alternativa aberta a Vanta/Drata. |
| Sushegaad/Claude-Skills-Governance-Risk-and-Compliance | 1.091 | 15/11/26 | MIT | Skills de GRC cobrindo, entre outros, PCI DSS, LGPD, DORA, SWIFT CSP, ISO 27001 e 42001. Cobertura ampla, profundidade a validar. |
| goul4rt/lgpd-skills | 287 | 19/11/26 | MIT | Toolkit em português para auditoria técnica, implementação de controles e governança sob a LGPD, resoluções da ANPD e ECA Digital. |
| BrunoLagoa/lgpd-enterprise-auditor | 2 | 10/11/26 | MIT | Auditor LGPD com score 0–100, artigo violado, evidência e plano de adequação. |
| kriss-b/llm-iso27001 | 67 | 27/10/26 | MIT | ISMS (ISO 27001 mais overlays 42001, NIS2) feito para ser operado por agentes. |
| Polycentric-Labs/evidentia | 11 | 16/11/26 | Apache-2.0 | Compliance-as-code: gap analysis, evidência e saída OSCAL, com MCP para agentes. |
| ynotbhatc/rego_policy_libraries | 23 | 20/11/26 | Apache-2.0 | Bibliotecas OPA/Rego prontas: CIS, STIG, NIST, ISO 27001, SOC 2, PCI DSS, GDPR. Compatível com a linha OPA. |
| zer0-kr/security-framework-mcp | 14 | 26/04/26 | MIT | Servidor MCP unificado NIST + OWASP (ASVS, CAPEC, CWE) com STRIDE e consulta a NVD/KEV/EPSS. |
| anotb/second-line-financial-services | 2 | 01/11/26 | MIT | Plugin com 68 skills de segunda linha para serviços financeiros, incluindo pagamentos/fintech. |
| p-boaz/graphletter | 1 | 04/11/26 | MIT | Valida políticas, evidências e relatórios contra o Secure Controls Framework e mapeia a 81 frameworks. |
| sharmajii10/arch-security-review, zxc0zxc0zxc/claude-pci-dss-verify, tribal-knowledge/pci-dss-claude-skills | 0–1 | 06–08/26 | MIT / sem licença | Skills de PCI DSS 4.0.1 (revisão de diagrama de arquitetura, auditoria de código, gap analysis). Embrionárias. |

### D. Proteger os próprios agentes e MCPs (ligação com governança de IA)

| Repositório | ★ | Observação |
|---|---|---|
| cisco-ai-defense/mcp-scanner | 1.123 | Scanner de servidores MCP. |
| hashgraph-online/hol-guard | 1.116 | "Antivírus/firewall" de agentes: bloqueia ferramentas arriscadas, segredos e prompt injection. |
| node9-ai/node9-proxy | 225 | Controle de acesso para agentes e MCPs. Retém ações destrutivas para revisão. |
| apisec-inc/mcp-audit | 168 | Audita configs de MCP e gera AI-BOM. |
| Repello-AI/Agent-Wiz | 398 | Extrai fluxos de agentes (LangGraph, AutoGen, CrewAI) e avalia ameaças. Último push nov/2025. |
| CyberStrategyInstitute/ai-safe2-framework | 159 | Framework GRC para IA agêntica e identidades não humanas. |
| vineethsai/asi | 21 | Guia interativo para proteger aplicações agênticas (OWASP). |

**Listas curadas para continuar a exploração:** scadastrangelove/awesome-ai-security-tools (1.766★), AmanPriyanshu/Awesome-AI-For-Security (156★), LLMSecurity/awesome-agent-skills-security (290★), Ed-Marcavage/awesome-security-agent-harnesses (83★), systempromptio/awesome-ai-agent-governance (58★), wearetyomsmnv/Awesome-LLMSecOps (172★), RiccardoBiosas/awesome-MLSecOps (493★), github/awesome-copilot (41.393★).

### E. Ofensiva e SOC (relevância menor para arquitetura, mas conforme o tema)

- usestrix/strix (76.801★, Apache-2.0), KeygraphHQ/shannon (52.133★, AGPL-3.0), vxcontrol/pentagi (34.685★, MIT), 0x4m4/hexstrike-ai (13.785★): pentest autônomo com agentes. O README do Shannon cita uma sonda experimental para o RCE "php2shell", o que se conecta ao projeto de radar de RCE.
- beenuar/AiSOC (7.100★, MIT) e FunnyWolf/agentic-soc-platform (1.235★): SOC com agentes e triagem de alertas.
- No levantamento anterior você já tinha PentestAgent, VulnBot, CAI e benchmarks. Não repeti.

### F. Emergentes aderentes à sua stack (todos 0–27★, só PoC)

- stackql/code-estate-warden: auditoria agêntica de postura em todos os repositórios de um GitHub Enterprise.
- g4bri-3l3/IDWolf (27★): auditor read-only de higiene de Active Directory e Entra ID em PowerShell.
- knox309/Entra-Security-Agent: avaliação de segurança do Entra ID com Microsoft Graph.
- jayekwere/ai-cloud-security-triage-agent: triagem de cloud com EPSS/KEV e propostas de Terraform aprovadas por humano.
- coffeestained/public-skills: diagramas C4 e modelos STRIDE em HTML.

## 4. Recomendação de próximos passos (para a camada agêntica de apoio à Arquitetura)

1. **Pilotar em paralelo, num projeto real e fechado:** secfoo, grim-prompter e agentic-threat-modeling (Red Hat). Comparar a saída com um threat model que os arquitetos já fizeram à mão.
2. **Triagem antes do comitê:** estudar o desenho de Lysis (entrada de docs, diagramas e PDFs; saída de achados e decisão de go-live) e de DocSentinel (questionários e formulários). Copiar a estrutura, não necessariamente adotar.
3. **Elo ameaça → requisito → PR:** o conjunto vankhangfet/threat-model-skills + ThreatSutra mostra o caminho. Sua base de requisitos de segurança já existente é o diferencial, porque nada aberto traz requisitos de adquirência (PCI, BACEN).
4. **LGPD:** lgpd-skills é a única opção com tração. Vale uma revisão técnica do conteúdo antes de usar.
5. **Regulação financeira:** tratar como espaço em branco. Construir skills próprias sobre a base interna, usando como molde a estrutura de UnitOneAI/SecuritySkills (controles ancorados em fonte) e os padrões de saída em evidência.

## 5. Alerta de cadeia de suprimentos

Skills, plugins e marketplaces de agente são instruções executáveis, e os repositórios acima são, em sua maioria, de autor único e recentes. Antes de instalar qualquer um: ler o conteúdo, fixar o commit, rodar em sandbox sem credenciais e passar por scanners de skill/MCP (por exemplo hol-guard ou mcp-scanner). Para avaliar a licença, note que Comp AI, Shannon, SecureFlow-AI e ThreatSutra são AGPL-3.0, e que CISO Assistant e vários outros aparecem como "NOASSERTION" na API, o que exige leitura do arquivo de licença.
