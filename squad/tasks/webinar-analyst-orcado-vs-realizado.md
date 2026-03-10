---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
### 2. Interactive Mode - Balanced, Educational (5-10 prompts) **[DEFAULT]**
### 3. Pre-Flight Planning - Comprehensive Upfront Planning

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: webinarAnalystOrcadoVsRealizado()
responsavel: Lens (Decoder)
responsavel_type: Agente
squad: webinar
atomic_layer: Organism

**Entrada:**
- campo: round_number
  tipo: number
  origem: User Input or Auto-detect
  obrigatorio: true

- campo: orcamento_meta
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/orcamento-meta.md
  obrigatorio: true
  validacao: Must exist with 12 premises populated

- campo: relatorio_kpis
  tipo: file
  origem: docs/webinar/rodada-{N}/analise/relatorio-kpis.md
  obrigatorio: true
  validacao: Must exist with real campaign metrics

**Saida:**
- campo: orcado_vs_realizado
  tipo: file
  destino: docs/webinar/rodada-{N}/analise/orcado-vs-realizado.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] orcamento-meta.md exists with projected values
    tipo: pre-condition
    blocker: true
    validacao: |
      Check docs/webinar/rodada-{N}/planejamento/orcamento-meta.md exists.
      If not: "Preciso do orcamento-meta.md para comparar. -> @webinar-strategist *orcamento"

  - [ ] relatorio-kpis.md exists with real metrics
    tipo: pre-condition
    blocker: true
    validacao: |
      Check docs/webinar/rodada-{N}/analise/relatorio-kpis.md exists.
      If not: "Preciso do relatorio de KPIs com dados reais. -> *kpis"
```

---

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "orcado-vs-realizado"
      lines: "L398-L408"
      purpose: "Estrutura de comparacao orcado vs realizado"
    - id: "formulas-calculo"
      lines: "L375-L389"
      purpose: "Formulas de calculo para validar desvios"
    - id: "kpis-funil"
      lines: "L339-L352"
      purpose: "Benchmarks de referencia para contextualizar desvios"
```

---

## SEQUENTIAL Task Execution

### 0. Load Context and Validate Prerequisites

- Load `orcamento-meta.md` (REQUIRED) — extract 12 projected premises
- Load `relatorio-kpis.md` (REQUIRED) — extract real campaign data
- Load knowledge base: orcado-vs-realizado (L398-L408), formulas-calculo (L375-L389)

### 1. Extract Projected Premises from Orcamento-Meta

**Objective:** Parse all 12 premises from the projected budget.

```yaml
premises:
  - id: P1
    name: "Meta de vendas (unidades)"
    field: meta_vendas
  - id: P2
    name: "Ticket do produto (R$)"
    field: ticket_produto
  - id: P3
    name: "Taxa de conversao vendas/leads"
    field: taxa_conversao
    benchmark: "3%"
  - id: P4
    name: "Taxa de conversao pagina de captura"
    field: taxa_captura
    benchmark: "40%"
  - id: P5
    name: "Taxa de comparecimento"
    field: taxa_comparecimento
    benchmark: "25%"
  - id: P6
    name: "Taxa de order bump"
    field: taxa_order_bump
  - id: P7
    name: "Ticket order bump (R$)"
    field: ticket_order_bump
  - id: P8
    name: "Taxa de upsell"
    field: taxa_upsell
  - id: P9
    name: "Ticket upsell (R$)"
    field: ticket_upsell
  - id: P10
    name: "Taxa de downsell"
    field: taxa_downsell
  - id: P11
    name: "Ticket downsell (R$)"
    field: ticket_downsell
  - id: P12
    name: "Custo por lead em midia (R$)"
    field: cpl_projetado
    benchmark: "~10% do ticket"
```

### 2. Extract Real Values from Relatorio-KPIs

**Objective:** Map real campaign results to each projected premise.

- For each of the 12 premises, extract the corresponding real value from relatorio-kpis.md
- If a real value is not available, mark as "N/D" and note in the report

### 3. Calculate Deviations (elicit: true)

**Objective:** Calculate deviation for each premise and identify the most impactful one.

```yaml
deviation_calculation:
  formula: "((real - projetado) / projetado) * 100"
  classification:
    - range: "-5% to +5%"
      status: "DENTRO"
      meaning: "Premissa validada"
    - range: "+5% to +20%"
      status: "ACIMA"
      meaning: "Superou a projecao"
    - range: "-5% to -20%"
      status: "ABAIXO"
      meaning: "Ficou abaixo da projecao"
    - range: "beyond +/-20%"
      status: "DESVIO SIGNIFICATIVO"
      meaning: "Premissa precisa ser recalibrada"
```

**Elicitation — present comparison table and ask for context:**

```yaml
elicit: true
format: table-review
interaction: |
  1. Present the comparison table of all 12 premises
  2. Highlight the premise with BIGGEST deviation
  3. Ask: "Essa premissa [nome] ficou [X%] diferente do projetado. Voce sabe o que pode ter causado esse desvio?"
  4. Record user's qualitative input
  5. For each DESVIO SIGNIFICATIVO, ask: "Quer ajustar essa premissa para a proxima rodada?"
```

### 4. Identify Most Impactful Premise

**Objective:** Determine which premise deviation had the greatest impact on the result.

- Calculate the "revenue impact" of each deviation:
  - If taxa_conversao was 1.5% instead of 3% -> how much revenue was lost?
  - If CPL was R$15 instead of R$10 -> how much more was spent?
- Rank premises by revenue impact (descending)
- Present: "A premissa que mais impactou seu resultado foi [premissa]: desvio de [X%], representando [R$ Y] de diferenca."

### 5. Generate Report

- Load template: `.aiox-core/development/templates/webinar-orcado-vs-realizado-tmpl.md`
- Populate comparison table (12 premises x 4 columns: Premissa, Projetado, Realizado, Desvio%)
- Include impact analysis section
- Include recommendations for recalibration
- Save to: `docs/webinar/rodada-{N}/analise/orcado-vs-realizado.md`

### 6. Present Summary and Recommend Next Steps

- Present top 3 deviation findings
- Recommend: `*proxima-rodada` to build optimization plan with recalibrated premises
- Inform user of saved file location

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] orcado-vs-realizado.md created with all 12 premises compared
    tipo: post-condition
    blocker: true
```

---

## Metadata

```yaml
story: N/A
version: 1.0.0
squad: webinar
agent: webinar-analyst
command: "*orcado-vs-realizado"
dependencies:
  - orcamento-meta.md (required)
  - relatorio-kpis.md (required)
tags:
  - analysis
  - budget
  - comparison
  - webinar
updated_at: 2026-03-05
```

---

## Handoff

next_agent: "@webinar-analyst"
next_command: "*proxima-rodada"
condition: Budget comparison complete
alternatives:
  - agent: "@webinar-analyst", command: "*diagnostico", condition: Funnel diagnostic not yet done
