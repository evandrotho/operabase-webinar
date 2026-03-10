---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
### 2. Interactive Mode - Balanced, Educational (5-10 prompts) **[DEFAULT]**
### 3. Pre-Flight Planning - Comprehensive Upfront Planning

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: webinarAnalystEmpilhamento()
responsavel: Lens (Decoder)
responsavel_type: Agente
squad: webinar
atomic_layer: Organism

**Entrada:**
- campo: relatorio_kpis
  tipo: file
  origem: docs/webinar/rodada-{N}/analise/relatorio-kpis.md
  obrigatorio: true
  validacao: Must exist with at least one round of real data

- campo: orcamento_meta
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/orcamento-meta.md
  obrigatorio: false
  validacao: Enriches with cost projections

- campo: canvas_produto
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/canvas-produto.md
  obrigatorio: false
  validacao: Enriches with product line information

**Saida:**
- campo: estrategia_empilhamento
  tipo: file
  destino: docs/webinar/estrategias/estrategia-empilhamento.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] relatorio-kpis.md exists with at least one round of data
    tipo: pre-condition
    blocker: true
    validacao: |
      Check docs/webinar/rodada-{N}/analise/relatorio-kpis.md exists.
      If not: "Preciso de pelo menos uma rodada analisada para planejar empilhamento. -> *kpis"
```

---

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "empilhamento-stacking"
      lines: "L3900-L3918"
      purpose: "Empilhamento de webinarios (funnel stacking) - conceito e fluxo"
    - id: "esteira-produtos"
      lines: "L3945-L3964"
      purpose: "Esteira de produtos - como sequenciar ofertas"
    - id: "metricas-benchmarks-consolidados"
      lines: "L3965-L3991"
      purpose: "Benchmarks para projetar ROI do empilhamento"
    - id: "kpis-funil"
      lines: "L339-L352"
      purpose: "Benchmarks de referencia para custo de lead"
```

---

## SEQUENTIAL Task Execution

### 0. Load Context and Validate Prerequisites

- Load `relatorio-kpis.md` from most recent round (REQUIRED)
- Load `orcamento-meta.md` (OPTIONAL)
- Load `canvas-produto.md` (OPTIONAL — product line info for stacking)
- Load knowledge base: empilhamento-stacking (L3900-L3918), esteira-produtos (L3945-L3964)

### 1. Assess Readiness for Stacking (elicit: true)

**Objective:** Determine if the current webinar is ready for stacking.

```yaml
readiness_criteria:
  - name: "Webinario validado"
    check: "Pelo menos 1 rodada executada com dados reais"
    threshold: "ROAS > 1.5x (sustentavel)"

  - name: "Base de leads existente"
    check: "Lista de leads da rodada anterior disponivel"
    threshold: "Minimo 500 leads para empilhamento viavel"

  - name: "Produto complementar disponivel"
    check: "Existe outro produto/servico para oferecer"
    threshold: "Produto com ticket igual ou superior"
```

**Elicitation:**

```yaml
elicit: true
format: sequential-questions
questions:
  - id: produtos_disponiveis
    question: "Voce tem outros produtos ou servicos alem do que vendeu no webinario? Liste-os com nome e ticket."
    why: "Empilhamento funciona quando voce tem uma esteira de produtos para oferecer em sequencia."
    required: true

  - id: base_leads_anterior
    question: "Quantos leads da rodada anterior voce tem na sua lista (que NAO compraram)?"
    why: "O custo de reativar um lead existente (R$0,06-0,25 via API) e muito menor que captar um novo (R$5-10)."
    required: true

  - id: objetivo_empilhamento
    question: |
      Qual seu objetivo principal com o empilhamento?
      1. Vender um produto de ticket mais alto para quem ja comprou
      2. Oferecer um produto diferente para quem nao comprou
      3. Ambos
    why: "O modelo de empilhamento muda conforme o objetivo."
    required: true
```

### 2. Design Stacking Strategy

**Objective:** Map the webinar sequence based on product line and audience segments.

```yaml
stacking_model:
  webinar_1:
    status: "Executado (rodada atual)"
    audience: "Lead frio (midia paga)"
    product: "{{produto_atual}}"
    ticket: "{{ticket_atual}}"
    cpl: "{{cpl_real}}"

  webinar_2:
    status: "Planejado"
    audience_segments:
      - segment: "Compradores do Web 1"
        action: "Upsell/cross-sell"
        cpl_estimado: "R$0,06-0,25 (API/lista existente)"
      - segment: "Nao-compradores do Web 1"
        action: "Nova oferta ou angulo diferente"
        cpl_estimado: "R$0,06-0,25 (API/lista existente)"
      - segment: "Leads novos"
        action: "Captacao fresca"
        cpl_estimado: "{{cpl_real}} (midia paga)"
    product: "{{proximo_produto}}"
    ticket: "{{proximo_ticket}}"

  webinar_3:
    status: "Futuro"
    audience: "Base acumulada Web 1 + Web 2"
    product: "{{produto_premium}}"
    ticket: "{{ticket_premium}}"
```

### 3. Project ROI of Stacking

**Objective:** Calculate projected ROI using real data from round 1 + stacking benchmarks.

```yaml
roi_projection:
  custo_lead_api: "R$0,06-0,25"
  custo_lead_novo: "R$5-10 (midia paga)"
  economia_estimada: "((cpl_novo - cpl_api) * leads_reativados)"
  roi_empilhamento: |
    Projecao conservadora:
    - Web 2 com base existente: leads_existentes * taxa_conversao_real * ticket_web2
    - Custo: leads_existentes * cpl_api
    - ROI = (receita - custo) / custo
```

### 4. Generate Strategy Document

- Load template: `.aiox-core/development/templates/webinar-estrategia-empilhamento-tmpl.md`
- Populate: stacking sequence, audience segmentation, ROI projection, timeline
- Save to: `docs/webinar/estrategias/estrategia-empilhamento.md`

### 5. Present Summary

- Present stacking sequence visual
- Present ROI projection with comparison (custo lead novo vs API)
- Recommend next steps:
  - @webinar-strategist to plan canvases for webinar 2
  - @webinar-creator to adapt content for different audience segments
- Inform user of saved file location

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] estrategia-empilhamento.md created in docs/webinar/estrategias/
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
command: "*empilhamento"
dependencies:
  - relatorio-kpis.md (required)
  - orcamento-meta.md (optional)
tags:
  - strategy
  - stacking
  - advanced
  - webinar
updated_at: 2026-03-05
```

---

## Handoff

next_agent: "@webinar-strategist"
next_command: "*canvas-produto"
condition: Stacking strategy defined, next product needs canvas
alternatives:
  - agent: "@webinar-analyst", command: "*perpetuo", condition: User wants evergreen instead of stacking
  - agent: "@webinar", command: "*planejar", condition: Ready to start planning next webinar in the stack
