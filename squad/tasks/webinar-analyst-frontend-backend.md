---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
### 2. Interactive Mode - Balanced, Educational (5-10 prompts) **[DEFAULT]**
### 3. Pre-Flight Planning - Comprehensive Upfront Planning

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: webinarAnalystFrontendBackend()
responsavel: Lens (Decoder)
responsavel_type: Agente
squad: webinar
atomic_layer: Organism

**Entrada:**
- campo: canvas_produto
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/canvas-produto.md
  obrigatorio: true
  validacao: Must exist with product information

- campo: relatorio_kpis
  tipo: file
  origem: docs/webinar/rodada-{N}/analise/relatorio-kpis.md
  obrigatorio: true
  validacao: Must exist with conversion data

- campo: orcamento_meta
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/orcamento-meta.md
  obrigatorio: false
  validacao: Enriches with cost structure

**Saida:**
- campo: estrategia_frontend_backend
  tipo: file
  destino: docs/webinar/estrategias/estrategia-frontend-backend.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] canvas-produto.md exists with product details
    tipo: pre-condition
    blocker: true
    validacao: |
      Check docs/webinar/rodada-{N}/planejamento/canvas-produto.md exists.
      If not: "Preciso do canvas do produto. -> @webinar-strategist *canvas-produto"

  - [ ] relatorio-kpis.md exists with conversion data
    tipo: pre-condition
    blocker: true
    validacao: |
      Check relatorio-kpis.md exists.
      If not: "Preciso dos KPIs da campanha. -> *kpis"
```

---

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "frontend-backend-modelo"
      lines: "L3919-L3944"
      purpose: "Modelo Front-end (VSL) + Back-end (Webinario) - conceito e fluxo"
    - id: "comparacao-estrategias"
      lines: "L390-L397"
      purpose: "Comparacao de estrategias de venda (lancamento vs perpetuo vs front+back)"
    - id: "metricas-benchmarks-consolidados"
      lines: "L3965-L3991"
      purpose: "Benchmarks para projetar cada perna do modelo"
```

---

## SEQUENTIAL Task Execution

### 0. Load Context and Validate Prerequisites

- Load `canvas-produto.md` (REQUIRED)
- Load `relatorio-kpis.md` (REQUIRED)
- Load `orcamento-meta.md` (OPTIONAL)
- Load knowledge base: frontend-backend-modelo (L3919-L3944), comparacao-estrategias (L390-L397)

### 1. Assess Current Product Structure (elicit: true)

**Objective:** Understand current product line and identify front-end/back-end opportunities.

**Elicitation:**

```yaml
elicit: true
format: sequential-questions
questions:
  - id: produto_atual_tipo
    question: |
      O produto que voce vende atualmente via webinario e:
      1. O unico produto que voce tem
      2. O produto de maior ticket (premium)
      3. Um produto de ticket medio
      4. Um produto de ticket baixo (entrada)
    why: "O modelo Front-end + Back-end usa um produto de entrada (VSL, ticket baixo) para atrair, e o webinario vende o produto de maior ticket."
    required: true

  - id: produto_frontend
    question: "Voce tem (ou pode criar) um produto de entrada com ticket entre R$47-R$297? Descreva-o brevemente."
    why: "O front-end e um produto de baixo ticket vendido via VSL (Video Sales Letter) curta. Ele paga o trafego e constroi a lista de compradores."
    required: true

  - id: ticket_frontend
    question: "Qual seria o ticket desse produto de entrada? (R$)"
    required: true

  - id: produto_backend
    question: "O produto de alto ticket (vendido via webinario) seria qual? E qual o ticket? (R$)"
    why: "O back-end e onde esta o lucro real. O webinario vende para a base de compradores do front-end."
    required: true

  - id: capacidade_vsl
    question: "Voce tem capacidade de criar uma VSL (Video Sales Letter) de 15-30 minutos para o produto de entrada?"
    why: "A VSL e essencial para o front-end. E um video curto de venda direta, diferente do webinario."
    required: true
```

### 2. Design Front-end + Back-end Model

**Objective:** Map the two-tier sales architecture.

```yaml
frontend_backend_model:
  frontend:
    format: "VSL (Video Sales Letter)"
    duration: "15-30 minutos"
    product: "{{produto_frontend}}"
    ticket: "R$ {{ticket_frontend}}"
    objective: "Pagar o trafego + construir lista de compradores"
    funnel: "Ad -> Landing Page com VSL -> Checkout -> Order Bump -> Upsell"
    kpis_projetados:
      cpl: "{{cpl_real}}"
      taxa_conversao_vsl: "2-5%"
      roas_frontend: "1.0-1.5x (breakeven e aceitavel)"

  backend:
    format: "Webinario (ao vivo ou perpetuo)"
    duration: "60-90 minutos"
    product: "{{produto_backend}}"
    ticket: "R$ {{ticket_backend}}"
    objective: "Lucro real - vender para base qualificada"
    funnel: "Email/WhatsApp para compradores do front-end -> Webinario -> Oferta High-Ticket"
    kpis_projetados:
      cpl_backend: "R$0 (base propria de compradores)"
      taxa_conversao_webinar: "5-10% (publico pre-qualificado)"
      roas_backend: "Infinito (sem custo de aquisicao)"

  fluxo_integrado:
    step_1: "Ads direcionam para VSL do front-end"
    step_2: "Compradores do front-end entram na lista VIP"
    step_3: "Lista VIP recebe convite para webinario (back-end)"
    step_4: "Webinario vende produto high-ticket para base qualificada"
    step_5: "Nao-compradores do webinario recebem downsell ou novo ciclo"
```

### 3. Project Combined ROI

**Objective:** Calculate combined ROI of the front-end + back-end model.

```yaml
roi_projection:
  frontend_mensal:
    leads: "orcamento_mensal / cpl"
    vendas_vsl: "leads * taxa_conversao_vsl"
    receita_frontend: "vendas_vsl * ticket_frontend"
    custo: "orcamento_mensal"
    margem_frontend: "receita_frontend - custo"
    nota: "Front-end pode dar breakeven ou pequeno lucro. O objetivo e PAGAR O TRAFEGO."

  backend_mensal:
    base_compradores: "vendas_vsl (acumulado)"
    convidados_webinar: "base_compradores * taxa_abertura_email"
    comparecimentos: "convidados * taxa_comparecimento"
    vendas_webinar: "comparecimentos * taxa_conversao_webinar"
    receita_backend: "vendas_webinar * ticket_backend"
    custo_backend: "R$ 0 (base propria)"
    margem_backend: "receita_backend (100% margem)"

  total_mensal:
    receita_total: "receita_frontend + receita_backend"
    custo_total: "orcamento_mensal"
    margem_total: "receita_total - custo_total"
    roas_combinado: "receita_total / custo_total"
```

### 4. Compare Strategies

**Objective:** Present comparison between current model and front-end + back-end.

```yaml
comparison_table:
  columns: ["Metrica", "Modelo Atual (Webinario Direto)", "Modelo Front+Back"]
  rows:
    - metrica: "CPL efetivo"
      atual: "{{cpl_real}}"
      frontback: "Pago pelo front-end"
    - metrica: "Custo para vender high-ticket"
      atual: "{{cpl_real}} * leads necessarios"
      frontback: "R$0 (base propria)"
    - metrica: "Taxa de conversao webinario"
      atual: "{{taxa_conversao_real}}"
      frontback: "5-10% (publico pre-qualificado)"
    - metrica: "Risco financeiro"
      atual: "Alto (investe antes de vender)"
      frontback: "Baixo (front-end paga o trafego)"
    - metrica: "Escalabilidade"
      atual: "Limitada pelo orcamento"
      frontback: "Alta (front-end auto-sustentavel)"
```

### 5. Generate Strategy Document

- Populate: product structure, two-tier model, ROI projections, strategy comparison
- Save to: `docs/webinar/estrategias/estrategia-frontend-backend.md`

### 6. Present Summary

- Present the model visually
- Present combined ROI projection
- Recommend next steps:
  - @webinar-strategist to create canvases for the front-end product
  - @webinar-creator to build the VSL script
  - @webinar-operator to configure the front-end funnel
- Inform user of saved file location

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] estrategia-frontend-backend.md created in docs/webinar/estrategias/
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
command: "*frontend-backend"
dependencies:
  - canvas-produto.md (required)
  - relatorio-kpis.md (required)
tags:
  - strategy
  - frontend-backend
  - vsl
  - advanced
  - webinar
updated_at: 2026-03-05
```

---

## Handoff

next_agent: "@webinar-strategist"
next_command: "*canvas-produto"
condition: Front-end product needs canvas creation
alternatives:
  - agent: "@webinar-analyst", command: "*empilhamento", condition: Combine with stacking strategy
  - agent: "@webinar-analyst", command: "*perpetuo", condition: Back-end should run as evergreen
