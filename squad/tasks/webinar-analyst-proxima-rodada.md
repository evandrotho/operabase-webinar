---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
### 2. Interactive Mode - Balanced, Educational (5-10 prompts) **[DEFAULT]**
### 3. Pre-Flight Planning - Comprehensive Upfront Planning

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: webinarAnalystProximaRodada()
responsavel: Lens (Decoder)
responsavel_type: Agente
squad: webinar
atomic_layer: Organism

**Entrada:**
- campo: round_number
  tipo: number
  origem: User Input or Auto-detect
  obrigatorio: true

- campo: diagnostico_funil
  tipo: file
  origem: docs/webinar/rodada-{N}/analise/diagnostico-funil.md
  obrigatorio: true
  validacao: Must exist with bottleneck analysis

- campo: all_canvases
  tipo: files
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatorio: false
  validacao: Used to indicate which canvases need revision

- campo: orcado_vs_realizado
  tipo: file
  origem: docs/webinar/rodada-{N}/analise/orcado-vs-realizado.md
  obrigatorio: false
  validacao: Enriches with recalibrated premises

**Saida:**
- campo: plano_proxima_rodada
  tipo: file
  destino: docs/webinar/rodada-{N}/analise/plano-proxima-rodada.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] diagnostico-funil.md exists with corrective actions
    tipo: pre-condition
    blocker: true
    validacao: |
      Check docs/webinar/rodada-{N}/analise/diagnostico-funil.md exists.
      If not: "Preciso do diagnostico de funil para planejar. -> *diagnostico"
```

---

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "estrategias-operacionais"
      lines: "L3992-L4077"
      purpose: "Estrategias operacionais adicionais para otimizacao"
    - id: "metricas-benchmarks-consolidados"
      lines: "L3965-L3991"
      purpose: "Benchmarks consolidados para definir novas metas"
    - id: "funil-visao-geral"
      lines: "L409-L421"
      purpose: "Visao geral do funil para re-planejamento"
    - id: "glossario"
      lines: "L3041-L3118"
      purpose: "Glossario de termos para clareza"
```

---

## SEQUENTIAL Task Execution

### 0. Load Context and Validate Prerequisites

- Load `diagnostico-funil.md` (REQUIRED)
- Load `orcado-vs-realizado.md` (OPTIONAL — enriches with recalibrated premises)
- Load `relatorio-kpis.md` (cross-reference for data)
- Scan `docs/webinar/rodada-{N}/planejamento/` for all canvas files
- Load knowledge base: estrategias-operacionais (L3992-L4077), metricas-benchmarks-consolidados (L3965-L3991)

### 1. Extract Corrective Actions from Diagnostic

**Objective:** Compile all corrective actions identified in the diagnostic.

- Parse diagnostico-funil.md for:
  - Identified bottlenecks (stage + severity)
  - Recommended corrective actions
  - Impacted artifacts
  - Responsible agents for each fix

### 2. Identify Canvases to Revise

**Objective:** Determine which planning canvases need updating based on real data.

```yaml
canvas_revision_logic:
  - condition: "CPL or leads significantly different from projected"
    canvas: "orcamento-meta.md"
    revision: "Recalibrar premissas de investimento e CPL com dados reais"
    agent: "@webinar-strategist"

  - condition: "Conversion below benchmark despite good attendance"
    canvas: "canvas-webinar.md"
    revision: "Revisar crenca-alvo, ponte de crencas, oferta baseado em feedback real"
    agent: "@webinar-strategist"

  - condition: "Attendance below 25%"
    canvas: "avatar-blueprint.md"
    revision: "Refinar avatar com dados de quem realmente compareceu vs quem nao compareceu"
    agent: "@webinar-strategist"

  - condition: "Offer not compelling (low conversion with good content)"
    canvas: "canvas-produto.md"
    revision: "Revisar proposta de valor, mecanismo unico, grande promessa"
    agent: "@webinar-strategist"

  - condition: "Wrong audience (high CPL, low engagement)"
    canvas: "canvas-cliente-ideal.md"
    revision: "Refinar criterios do cliente ideal com dados de quem converteu"
    agent: "@webinar-strategist"
```

### 3. Build Optimization Plan (elicit: true)

**Objective:** Create prioritized list of optimizations with user input on priorities.

**Elicitation:**

```yaml
elicit: true
format: priority-review
interaction: |
  1. Present list of all optimizations organized by:
     - OBRIGATORIAS (fixes for CRITICO bottlenecks)
     - RECOMENDADAS (fixes for ABAIXO metrics)
     - OPCIONAIS (micro-optimizations for good metrics)
  2. For each optimization, show:
     - O que mudar
     - Impacto esperado (baseado nos benchmarks)
     - Esforco estimado (baixo/medio/alto)
     - Quem executa (@webinar-strategist, @webinar-creator, @webinar-operator)
  3. Ask: "Quer ajustar a prioridade de alguma otimizacao?"
  4. Ask: "Ha alguma restricao para a proxima rodada? (ex: orcamento menor, data especifica, novo produto)"
```

### 4. Define New Targets for Next Round

**Objective:** Set realistic targets based on real data + optimizations.

- For each KPI that was ABAIXO:
  - Set new target between current real value and benchmark
  - Explain: "Na rodada 1 voce teve [X%]. Com as otimizacoes, a meta para rodada 2 e [Y%]."
- For each KPI that was DENTRO or ACIMA:
  - Maintain or slightly increase target
  - Explain: "Esse KPI esta saudavel. Vamos manter e focar energia nas melhorias prioritarias."

### 5. Generate Plan Document

- Load template: `.aiox-core/development/templates/webinar-plano-proxima-rodada-tmpl.md`
- Populate all sections:
  - Resumo da Rodada Anterior (dados reais + diagnostico)
  - Canvases a Revisar (lista com especificacao do que mudar)
  - Otimizacoes Priorizadas (obrigatorias, recomendadas, opcionais)
  - Novas Metas (KPIs recalibrados)
  - Proximos Passos (sequencia de acao com responsaveis)
- Save to: `docs/webinar/rodada-{N}/analise/plano-proxima-rodada.md`

### 6. Present Summary and Handoff

- Present: "Plano da proxima rodada pronto! [X] otimizacoes identificadas, [Y] canvases para revisar."
- Explain the handoff loop:
  - "O proximo passo e ativar @webinar-strategist para revisar os canvases indicados no plano."
  - "Depois, @webinar-creator ajusta os conteudos afetados."
  - "Finalmente, @webinar-operator configura as mudancas operacionais."
- Inform user of saved file location

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] plano-proxima-rodada.md created with optimizations and canvas revision list
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
command: "*proxima-rodada"
dependencies:
  - diagnostico-funil.md (required)
  - orcado-vs-realizado.md (optional)
  - all planning canvases (optional)
tags:
  - analysis
  - optimization
  - planning
  - next-round
  - webinar
updated_at: 2026-03-05
```

---

## Handoff

next_agent: "@webinar-strategist"
next_command: "*canvas-webinar"
condition: Plan includes canvas revisions for next round
alternatives:
  - agent: "@webinar-strategist", command: "*orcamento", condition: Budget premises need recalibration
  - agent: "@webinar-creator", command: "*roteiro", condition: Script revisions needed
  - agent: "@webinar", command: "*planejar", condition: Starting fresh round from orchestrator
