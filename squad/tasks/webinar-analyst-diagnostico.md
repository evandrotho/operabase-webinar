---

## Execution Modes

**Choose your execution mode:**

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
- Autonomous analysis with logging
- **Best for:** Quick diagnostics with data already available

### 2. Interactive Mode - Balanced, Educational (5-10 prompts) **[DEFAULT]**
- Step-by-step funnel walkthrough with explanations
- **Best for:** Understanding WHERE the funnel breaks and WHY

### 3. Pre-Flight Planning - Comprehensive Upfront Planning
- Full data review before analysis
- **Best for:** Complex multi-round comparison

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: webinarAnalystDiagnostico()
responsavel: Lens (Decoder)
responsavel_type: Agente
squad: webinar
atomic_layer: Organism

**Entrada:**
- campo: round_number
  tipo: number
  origem: User Input or Auto-detect
  obrigatorio: true

- campo: relatorio_kpis
  tipo: file
  origem: docs/webinar/rodada-{N}/analise/relatorio-kpis.md
  obrigatorio: true
  validacao: Must exist with KPIs populated

- campo: funil_7_etapas
  tipo: file
  origem: docs/webinar/rodada-{N}/execucao/funil-7-etapas.md
  obrigatorio: true
  validacao: Must exist with funnel stage data

- campo: timeline_campanha
  tipo: file
  origem: docs/webinar/rodada-{N}/execucao/timeline-campanha.md
  obrigatorio: false
  validacao: Enriches with timing data

**Saida:**
- campo: diagnostico_funil
  tipo: file
  destino: docs/webinar/rodada-{N}/analise/diagnostico-funil.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] relatorio-kpis.md exists with KPIs populated
    tipo: pre-condition
    blocker: true
    validacao: |
      Check docs/webinar/rodada-{N}/analise/relatorio-kpis.md exists.
      If not: "Para fazer o diagnostico, preciso do relatorio de KPIs. Quer registrar agora? -> *kpis"
    error_message: "Pre-requisito: relatorio-kpis.md nao encontrado. Execute *kpis primeiro."

  - [ ] funil-7-etapas.md exists
    tipo: pre-condition
    blocker: true
    validacao: |
      Check docs/webinar/rodada-{N}/execucao/funil-7-etapas.md exists.
      If not: "Preciso do funil de 7 etapas para diagnosticar. Quer gerar? -> @webinar-operator *funil"
    error_message: "Pre-requisito: funil-7-etapas.md nao encontrado. Execute @webinar-operator *funil primeiro."
```

---

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "kpis-funil"
      lines: "L339-L352"
      purpose: "Benchmarks de referencia para cada etapa do funil"
    - id: "kpis-adicionais"
      lines: "L366-L374"
      purpose: "KPIs adicionais para diagnostico avancado"
    - id: "funil-visao-geral"
      lines: "L409-L421"
      purpose: "Visao geral do funil de 7 etapas"
    - id: "funil-estrutura"
      lines: "L422-L434"
      purpose: "Estrutura basica vs escalada - qual modelo esta sendo usado"
    - id: "etapa-1-captacao"
      lines: "L451-L525"
      purpose: "Etapa 1 - Captacao: diagnostico de CPL e taxa de captura"
    - id: "etapa-2-nutricao"
      lines: "L526-L685"
      purpose: "Etapa 2 - Nutricao: diagnostico de engajamento pre-webinario"
    - id: "etapa-3-antecipacao"
      lines: "L686-L890"
      purpose: "Etapa 3 - Antecipacao: diagnostico de comparecimento"
    - id: "etapa-4-abertura"
      lines: "L891-L984"
      purpose: "Etapa 4 - Abertura do Carrinho: diagnostico de conversao no webinario"
    - id: "etapa-5-ampliacao"
      lines: "L985-L1197"
      purpose: "Etapa 5 - Ampliacao: diagnostico de vendas no replay"
    - id: "etapa-6-fechamento"
      lines: "L1198-L1463"
      purpose: "Etapa 6 - Fechamento: diagnostico de urgencia/escassez"
    - id: "etapa-7-impulsionamento"
      lines: "L1464-L1651"
      purpose: "Etapa 7 - Impulsionamento: diagnostico de downsell"
    - id: "metricas-consolidadas"
      lines: "L1672-L1715"
      purpose: "Metricas e KPIs consolidados para cross-reference"
```

---

## SEQUENTIAL Task Execution

### 0. Load Context and Validate Prerequisites

- Detect active round number
- Load `relatorio-kpis.md` (REQUIRED)
- Load `funil-7-etapas.md` (REQUIRED)
- Load `timeline-campanha.md` (OPTIONAL)
- Load knowledge base sections: funil-visao-geral, kpis-funil, kpis-adicionais

### 1. Map KPIs to Funnel Stages

**Objective:** Map each KPI from the report to its corresponding funnel stage.

```yaml
funnel_mapping:
  etapa_1_captacao:
    kpis: [CPL, taxa_captura, total_leads]
    benchmark_refs: ["L339-L352", "L451-L525"]
    diagnostic_question: "Os leads estao chegando em quantidade e custo adequados?"

  etapa_2_nutricao:
    kpis: [engagement_rate, open_rate_messages]
    benchmark_refs: ["L526-L685"]
    diagnostic_question: "Os leads estao engajando com o conteudo pre-webinario?"

  etapa_3_antecipacao:
    kpis: [taxa_comparecimento]
    benchmark_refs: ["L686-L890"]
    diagnostic_question: "Os leads estao comparecendo ao webinario?"

  etapa_4_abertura:
    kpis: [taxa_conversao_vendas, vendas_abertura]
    benchmark_refs: ["L891-L984"]
    diagnostic_question: "O webinario esta convertendo quem assiste?"

  etapa_5_ampliacao:
    kpis: [vendas_replay, taxa_replay]
    benchmark_refs: ["L985-L1197"]
    diagnostic_question: "O replay esta gerando vendas adicionais?"

  etapa_6_fechamento:
    kpis: [vendas_fechamento, conversao_urgencia]
    benchmark_refs: ["L1198-L1463"]
    diagnostic_question: "A fase de urgencia/escassez esta funcionando?"

  etapa_7_impulsionamento:
    kpis: [downsell_vendas, order_bump, upsell]
    benchmark_refs: ["L1464-L1651"]
    diagnostic_question: "O impulsionamento do lucro (downsell/bump/upsell) esta ativo?"
```

### 2. Identify Bottleneck (elicit: true)

**Objective:** Walk through funnel stages with user, identify where the biggest drop-off occurs.

**Logic — apply diagnostic rules from methodology:**

```yaml
diagnostic_rules:
  - condition: "CPL > 10% do ticket"
    verdict: "GARGALO na Etapa 1"
    action: "Revisar criativos de anuncio e segmentacao de publico"
    detail: "O CPL esta acima do benchmark de ~10% do ticket. Isso significa que os anuncios nao estao atraindo o publico certo ou o criativo nao esta suficientemente atrativo."
    methodology_ref: "Secao 4, Etapa 1 (L451-L525)"

  - condition: "Taxa de captura < 40%"
    verdict: "GARGALO na Etapa 1"
    action: "Revisar congruencia entre criativo do anuncio e headline da pagina de captura"
    detail: "A taxa de conversao da pagina esta abaixo de 40%. Verifique se a promessa do anuncio esta alinhada com a headline da pagina. Teste formulas: 'Como X sem Y', 'Como X mesmo que Z'."
    methodology_ref: "Secao 4, Etapa 1 + Secao 5.2 (Abertura, bloco 1)"

  - condition: "Taxa de comparecimento < 25%"
    verdict: "GARGALO nas Etapas 2-3"
    action: "Revisar sequencia de nutricao e mensagens de antecipacao (D-1, D-0)"
    detail: "Menos de 25% dos leads compareceram. Verifique: (1) mensagens de nutricao foram enviadas? (2) lembretes D-1 e D-0 foram eficazes? (3) o conteudo de antecipacao gerou compromisso?"
    methodology_ref: "Secao 4, Etapas 2-3 (L526-L890)"

  - condition: "Conversao < 3% com comparecimento >= 25%"
    verdict: "GARGALO na Etapa 4 (Black Box)"
    action: "Revisar roteiro do webinario — Abertura, Empatia, Conteudo e/ou Pitch"
    detail: "O publico esta comparecendo mas nao comprando. O problema esta no roteiro. Avalie cada secao da Black Box: (1) Abertura criou conexao? (2) Empatia gerou identificacao? (3) Conteudo quebrou falsas crencas? (4) Pitch apresentou oferta irresistivel?"
    methodology_ref: "Secao 5 - Black Box Fusionada (L1722-L2832)"

  - condition: "Replay sem vendas ou vendas_replay = 0"
    verdict: "GARGALO na Etapa 5"
    action: "Revisar pagina de replay e timing de disponibilizacao"
    detail: "O replay nao gerou vendas. Verifique: (1) a pagina de replay tem timestamps como headlines de venda? (2) ha pre-headline de escassez? (3) o delay da oferta esta configurado? (4) NÃO usar contador regressivo na pagina de replay."
    methodology_ref: "Secao 4, Etapa 5 (L985-L1197)"

  - condition: "Fechamento fraco (vendas_fechamento < vendas_abertura * 0.8)"
    verdict: "GARGALO na Etapa 6"
    action: "Revisar mensagens de urgencia/escassez e deadline"
    detail: "O Pico 2 (fechamento) deveria ser comparavel ao Pico 1 (abertura). Verifique: (1) deadline esta claro e visivel? (2) contador regressivo ativo na pagina de fechamento? (3) mensagens de escassez seguem a sequencia da metodologia?"
    methodology_ref: "Secao 4, Etapa 6 (L1198-L1463)"
```

**Elicitation — present findings and ask for context:**

```yaml
elicit: true
format: diagnostic-walkthrough
interaction: |
  For each stage where a bottleneck is detected:
  1. Present the finding with data: "Na Etapa X, seu [metrica] foi [valor] vs benchmark de [benchmark]"
  2. Explain what it means in simple terms
  3. Ask: "Voce percebeu algo nessa etapa que pode explicar esse resultado?"
  4. Record user's qualitative input to enrich the diagnostic
  5. Present the recommended corrective action from methodology
```

### 3. Prioritize Corrective Actions

**Objective:** Rank bottlenecks by impact and provide prioritized action plan.

- Rank bottlenecks by:
  1. **Impact on revenue** — which fix would generate most additional revenue
  2. **Ease of implementation** — which fix is fastest to apply
  3. **Position in funnel** — earlier funnel fixes have cascading impact
- For each corrective action, specify:
  - What to change
  - Which artifact to modify (e.g., roteiro-abertura.md, mensagens-whatsapp.md)
  - Which agent to activate (e.g., @webinar-creator for roteiro changes)
  - Expected impact based on methodology benchmarks

### 4. Generate Diagnostic Report

**Objective:** Generate the diagnostic report using the template.

- Load template: `.aiox-core/development/templates/webinar-diagnostico-funil-tmpl.md`
- Populate all sections with diagnostic data
- Include funnel visualization with drop-off points
- Save to: `docs/webinar/rodada-{N}/analise/diagnostico-funil.md`

### 5. Present Summary and Recommend Next Steps

- Present: "Diagnostico completo! O principal gargalo esta na [Etapa X]: [descricao]"
- Top 3 acoes corretivas priorizadas
- Recommend next command:
  - `*orcado-vs-realizado` if not yet done
  - `*proxima-rodada` to build optimization plan
- Inform user of saved file location

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] diagnostico-funil.md created with bottleneck identification and corrective actions
    tipo: post-condition
    blocker: true
```

---

## Error Handling

**Strategy:** retry

1. **Error:** KPI report missing metrics
   - **Resolution:** Proceed with available data, mark gaps
   - **Recovery:** Recommend re-running *kpis with complete data

2. **Error:** No clear bottleneck (all metrics within range)
   - **Resolution:** Generate positive report with micro-optimization suggestions
   - **Recovery:** Focus on advanced strategies (empilhamento, perpetuo)

---

## Metadata

```yaml
story: N/A
version: 1.0.0
squad: webinar
agent: webinar-analyst
command: "*diagnostico"
dependencies:
  - relatorio-kpis.md (required)
  - funil-7-etapas.md (required)
  - timeline-campanha.md (optional)
tags:
  - analysis
  - diagnostics
  - funnel
  - webinar
updated_at: 2026-03-05
```

---

## Handoff

next_agent: "@webinar-analyst"
next_command: "*proxima-rodada"
condition: Diagnostic complete with corrective actions identified
alternatives:
  - agent: "@webinar-analyst", command: "*orcado-vs-realizado", condition: Budget comparison not yet done
  - agent: "@webinar-creator", command: "*roteiro", condition: Bottleneck is in Black Box (script issues)
  - agent: "@webinar-operator", command: "*setup-sendflow", condition: Bottleneck is in messaging/automation
