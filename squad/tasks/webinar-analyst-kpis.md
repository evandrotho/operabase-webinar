---

## Execution Modes

**Choose your execution mode:**

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
- Autonomous decision making with logging
- Minimal user interaction
- **Best for:** Re-running with data already available

### 2. Interactive Mode - Balanced, Educational (5-10 prompts) **[DEFAULT]**
- Explicit decision checkpoints
- Educational explanations of each KPI
- **Best for:** First-time analysis, learning the methodology

### 3. Pre-Flight Planning - Comprehensive Upfront Planning
- Review all available data before starting
- **Best for:** Complex multi-source data scenarios

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: webinarAnalystKpis()
responsavel: Lens (Decoder)
responsavel_type: Agente
squad: webinar
atomic_layer: Organism

**Entrada:**
- campo: round_number
  tipo: number
  origem: User Input or Auto-detect
  obrigatorio: true
  validacao: Must be >= 1, auto-detect from docs/webinar/ if not provided

- campo: orcamento_meta
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/orcamento-meta.md
  obrigatorio: true
  validacao: Must exist with benchmarks populated

- campo: funil_7_etapas
  tipo: file
  origem: docs/webinar/rodada-{N}/execucao/funil-7-etapas.md
  obrigatorio: false
  validacao: Enriches analysis with funnel stage data

- campo: user_metrics
  tipo: object
  origem: User Input (via conversation)
  obrigatorio: true
  validacao: Must include at minimum CPL, leads, comparecimentos, vendas, faturamento

**Saida:**
- campo: relatorio_kpis
  tipo: file
  destino: docs/webinar/rodada-{N}/analise/relatorio-kpis.md
  persistido: true
```

---

## Pre-Conditions

**Purpose:** Validate prerequisites BEFORE task execution (blocking)

**Checklist:**

```yaml
pre-conditions:
  - [ ] orcamento-meta.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    validacao: |
      Check file exists. If not, inform user:
      "Para analisar os KPIs, preciso do orcamento-meta.md com os benchmarks projetados.
       Quer preencher agora? -> @webinar-strategist *orcamento"
    error_message: "Pre-requisito: orcamento-meta.md nao encontrado. Execute @webinar-strategist *orcamento primeiro."

  - [ ] Campaign has been executed with real data available
    tipo: pre-condition
    blocker: true
    validacao: |
      Ask user to confirm campaign was executed and data is available.
    error_message: "Pre-requisito: A campanha precisa ter sido executada com dados reais disponiveis."
```

---

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "kpis-funil"
      lines: "L339-L352"
      purpose: "KPIs de funil com benchmarks de referencia (taxa conversao, captura, comparecimento)"
    - id: "kpis-resultado"
      lines: "L353-L365"
      purpose: "KPIs de resultado com exemplo modelado (faturamento, ROAS, margem)"
    - id: "kpis-adicionais"
      lines: "L366-L374"
      purpose: "KPIs adicionais (retenção no webinário, taxa replay, etc.)"
    - id: "formulas-calculo"
      lines: "L375-L389"
      purpose: "Formulas de calculo do funil (leads necessarios, cliques, investimento)"
    - id: "metricas-consolidadas"
      lines: "L1672-L1715"
      purpose: "Metricas e KPIs consolidados do funil operacional"
    - id: "metricas-benchmarks-consolidados"
      lines: "L3965-L3991"
      purpose: "Metricas e benchmarks consolidados para analise avancada"
    - id: "segmentacao-tags"
      lines: "L3759-L3829"
      purpose: "Segmentacao e tags para analise de dados"
```

---

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 0. Load Context and Validate Prerequisites

- Detect active round number from `docs/webinar/` (highest rodada-{N} folder)
- If user provided round number, use it; otherwise auto-detect
- Load `docs/webinar/rodada-{N}/planejamento/orcamento-meta.md` (REQUIRED)
- Load `docs/webinar/rodada-{N}/execucao/funil-7-etapas.md` (OPTIONAL - enriches)
- Load knowledge base sections: kpis-funil (L339-L352), kpis-resultado (L353-L365), formulas-calculo (L375-L389)
- If orcamento-meta.md missing, HALT with redirect message

### 1. Collect Campaign Metrics (elicit: true)

**Objective:** Gather real campaign data from the user via interactive conversation.

**Elicitation — ask ONE question at a time, explain why each metric matters:**

```yaml
elicit: true
format: sequential-questions
questions:
  - id: investimento_ads
    question: "Quanto voce investiu em anuncios (midia paga) nesta campanha? (R$)"
    why: "Preciso desse valor para calcular o CPL (Custo por Lead) e o ROAS (Retorno sobre Investimento em Ads)."
    type: currency
    required: true

  - id: total_leads
    question: "Quantos leads (inscritos) voce captou no total?"
    why: "O numero de leads e a base de todo o funil. Vou comparar com a meta do seu orcamento."
    type: number
    required: true

  - id: total_comparecimentos
    question: "Quantas pessoas compareceram ao webinario (ao vivo ou replay)?"
    why: "A taxa de comparecimento e um dos KPIs mais importantes. O benchmark e 25%."
    type: number
    required: true

  - id: total_vendas
    question: "Quantas vendas foram realizadas no total (incluindo todas as etapas do funil)?"
    why: "Preciso para calcular a taxa de conversao. O benchmark da metodologia e 3% sobre leads."
    type: number
    required: true

  - id: faturamento_bruto
    question: "Qual foi o faturamento bruto total da campanha? (R$)"
    why: "Com esse valor calculo o ROAS e a margem liquida."
    type: currency
    required: true

  - id: vendas_abertura
    question: "Quantas vendas aconteceram na abertura do carrinho (durante/logo apos o webinario)?"
    why: "O padrao saudavel e Pico 1 (abertura) > Vale > Pico 2 (fechamento). Preciso separar para diagnosticar."
    type: number
    required: false
    default: null

  - id: vendas_replay
    question: "Quantas vendas vieram da fase de replay/ampliacao?"
    why: "Se o replay nao gera vendas, pode indicar problema na pagina de replay ou no timing."
    type: number
    required: false
    default: null

  - id: vendas_fechamento
    question: "Quantas vendas vieram na fase de fechamento (urgencia/escassez)?"
    why: "O Pico 2 deve ser forte. Se nao for, indica problema nas mensagens de urgencia."
    type: number
    required: false
    default: null

  - id: taxa_captura
    question: "Qual foi a taxa de conversao da pagina de captura? (%) — se nao souber, me diga quantos cliques a pagina recebeu."
    why: "O benchmark e 40%. Se estiver abaixo, o problema pode estar na headline ou na congruencia com o criativo."
    type: percentage_or_number
    required: false
    default: null

  - id: order_bump_vendas
    question: "Houve vendas de order bump? Se sim, quantas e qual o valor total? (pode pular se nao tem)"
    why: "Order bump, upsell e downsell afetam o faturamento total e o ticket medio real."
    type: text
    required: false
    default: null

  - id: upsell_vendas
    question: "Houve vendas de upsell? Se sim, quantas e qual o valor total? (pode pular se nao tem)"
    type: text
    required: false
    default: null

  - id: downsell_vendas
    question: "Houve vendas de downsell? Se sim, quantas e qual o valor total? (pode pular se nao tem)"
    type: text
    required: false
    default: null
```

### 2. Calculate KPIs

**Objective:** Calculate all KPIs from raw data and compare with benchmarks.

**Calculated KPIs:**

```yaml
kpis_calculados:
  # Funnel KPIs
  - name: CPL (Custo por Lead)
    formula: "investimento_ads / total_leads"
    benchmark: "~10% do ticket do produto"
    source_ref: "Secao 3, L339-L352"

  - name: Taxa de Captura
    formula: "(total_leads / cliques_pagina) * 100"
    benchmark: "40%"
    source_ref: "Secao 3, L339-L352"

  - name: Taxa de Comparecimento
    formula: "(total_comparecimentos / total_leads) * 100"
    benchmark: "25%"
    source_ref: "Secao 3, L339-L352"

  - name: Taxa de Conversao (Vendas/Leads)
    formula: "(total_vendas / total_leads) * 100"
    benchmark: "3%"
    source_ref: "Secao 3, L339-L352"

  - name: Taxa de Conversao (Vendas/Comparecimentos)
    formula: "(total_vendas / total_comparecimentos) * 100"
    benchmark: "12% (derivado: 3% / 25%)"
    source_ref: "Calculo derivado"

  # Result KPIs
  - name: Faturamento Bruto
    formula: "valor informado pelo usuario"
    benchmark: "meta do orcamento-meta.md"
    source_ref: "Secao 3, L353-L365"

  - name: Faturamento Total (com bump/upsell/downsell)
    formula: "faturamento_bruto + order_bump_total + upsell_total + downsell_total"
    benchmark: "meta ajustada"
    source_ref: "Secao 3, L353-L365"

  - name: ROAS (Return on Ad Spend)
    formula: "faturamento_total / investimento_ads"
    benchmark: "variavel por nicho, minimo 2x para sustentavel"
    source_ref: "Secao 3, L353-L365"

  - name: Margem Liquida
    formula: "((faturamento_total - investimento_ads) / faturamento_total) * 100"
    benchmark: ">50% para operacao saudavel"
    source_ref: "Secao 3, L353-L365"

  - name: Ticket Medio Real
    formula: "faturamento_total / total_vendas"
    benchmark: "ticket do produto (orcamento-meta)"
    source_ref: "Calculo derivado"

  # Distribution KPIs (if data available)
  - name: Distribuicao de Vendas
    formula: "vendas_abertura + vendas_replay + vendas_fechamento = total_vendas"
    benchmark: "Pico 1 (abertura) > Vale (replay) < Pico 2 (fechamento)"
    source_ref: "Secao 4, padrao de vendas"
```

### 3. Compare with Benchmarks and Orcamento-Meta

**Objective:** Compare each KPI calculated with methodology benchmarks AND projected values from orcamento-meta.md.

- For each KPI, determine status:
  - **ACIMA** — metric above benchmark (positive for most KPIs)
  - **DENTRO** — metric within acceptable range of benchmark
  - **ABAIXO** — metric below benchmark (attention needed)
  - **CRITICO** — metric significantly below benchmark (action required)
- Cross-reference with orcamento-meta.md projected values
- Calculate deviation percentage for each metric

### 4. Generate Report

**Objective:** Generate the final KPI report using the template.

- Load template: `.aiox-core/development/templates/webinar-relatorio-kpis-tmpl.md`
- Populate all sections with calculated data
- Include benchmark comparisons with visual indicators
- Add summary section with top insights
- Save to: `docs/webinar/rodada-{N}/analise/relatorio-kpis.md`

### 5. Present Summary and Recommend Next Steps

**Objective:** Present key findings to user and suggest next actions.

- Present top 3 insights (most impactful findings)
- Recommend next command based on results:
  - If any KPI is CRITICO -> recommend `*diagnostico` for deep funnel analysis
  - If significant deviation from orcamento -> recommend `*orcado-vs-realizado`
  - If results are good -> recommend `*proxima-rodada` for optimization
- Inform user: "O relatorio completo foi salvo em `docs/webinar/rodada-{N}/analise/relatorio-kpis.md`"

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] relatorio-kpis.md created in docs/webinar/rodada-{N}/analise/
    tipo: post-condition
    blocker: true
    validacao: |
      Verify file exists and contains all calculated KPIs with benchmark comparisons.
    error_message: "Post-condition failed: relatorio-kpis.md not created or incomplete."
```

---

## Error Handling

**Strategy:** retry

**Common Errors:**

1. **Error:** Orcamento-meta not found
   - **Cause:** Planning phase was skipped or file not generated
   - **Resolution:** Redirect to @webinar-strategist *orcamento
   - **Recovery:** Can proceed with methodology benchmarks only (without projected values)

2. **Error:** Incomplete metrics from user
   - **Cause:** User doesn't have all data available
   - **Resolution:** Calculate with available data, mark missing metrics as "N/D (nao disponivel)"
   - **Recovery:** Allow partial report generation, note limitations

3. **Error:** Invalid numeric input
   - **Cause:** User provided text instead of numbers
   - **Resolution:** Re-ask with example format
   - **Recovery:** Parse common formats (R$ 1.500, 1500, 1.500,00)

---

## Performance

```yaml
duration_expected: 10-20 min (interactive mode)
cost_estimated: $0.005-0.015
token_usage: ~5,000-15,000 tokens
```

---

## Metadata

```yaml
story: N/A
version: 1.0.0
squad: webinar
agent: webinar-analyst
command: "*kpis"
dependencies:
  - orcamento-meta.md (required)
  - funil-7-etapas.md (optional)
tags:
  - analysis
  - kpis
  - webinar
  - post-campaign
updated_at: 2026-03-05
```

---

## Handoff

next_agent: "@webinar-analyst"
next_command: "*diagnostico"
condition: KPIs registered, at least one metric ABAIXO or CRITICO
alternatives:
  - agent: "@webinar-analyst", command: "*orcado-vs-realizado", condition: Significant deviation from orcamento-meta
  - agent: "@webinar-analyst", command: "*proxima-rodada", condition: Results are satisfactory, ready to optimize
