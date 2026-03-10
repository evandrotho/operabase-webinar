---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
### 2. Interactive Mode - Balanced, Educational (5-10 prompts) **[DEFAULT]**
### 3. Pre-Flight Planning - Comprehensive Upfront Planning

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: webinarAnalystPerpetuo()
responsavel: Lens (Decoder)
responsavel_type: Agente
squad: webinar
atomic_layer: Organism

**Entrada:**
- campo: roteiro_completo
  tipo: file
  origem: docs/webinar/rodada-{N}/conteudo/roteiro-completo.md
  obrigatorio: true
  validacao: Must exist — script needs to be validated before going evergreen

- campo: relatorio_kpis
  tipo: file
  origem: docs/webinar/rodada-{N}/analise/relatorio-kpis.md
  obrigatorio: true
  validacao: Must have positive ROAS to justify evergreen conversion

- campo: guia_everwebinar
  tipo: file
  origem: docs/webinar/rodada-{N}/execucao/guia-everwebinar.md
  obrigatorio: false
  validacao: Enriches with current EverWebinar configuration

**Saida:**
- campo: estrategia_perpetuo
  tipo: file
  destino: docs/webinar/estrategias/estrategia-perpetuo.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] roteiro-completo.md exists (validated script)
    tipo: pre-condition
    blocker: true
    validacao: |
      Check docs/webinar/rodada-{N}/conteudo/roteiro-completo.md exists.
      If not: "Para converter em perpetuo, preciso de um roteiro validado. -> @webinar-creator *roteiro"

  - [ ] relatorio-kpis.md exists with positive ROAS
    tipo: pre-condition
    blocker: true
    validacao: |
      Check relatorio-kpis.md exists AND ROAS > 1.0.
      If ROAS <= 1.0: "O ROAS atual e [X]. Para modo perpetuo ser viavel, precisa ser positivo.
       Recomendo primeiro otimizar com *proxima-rodada."
```

---

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "perpetuo-evergreen"
      lines: "L3834-L3872"
      purpose: "Webinario perpetuo/evergreen - configuracao, chat simulado, agendamento recorrente"
    - id: "metricas-benchmarks-consolidados"
      lines: "L3965-L3991"
      purpose: "Benchmarks para projecao de funil semanal perpetuo"
    - id: "estrategias-operacionais"
      lines: "L3992-L4077"
      purpose: "Estrategias operacionais para perpetuo"
```

---

## SEQUENTIAL Task Execution

### 0. Load Context and Validate Prerequisites

- Load `roteiro-completo.md` (REQUIRED)
- Load `relatorio-kpis.md` (REQUIRED — validate positive ROAS)
- Load `guia-everwebinar.md` (OPTIONAL — current EverWebinar config)
- Load knowledge base: perpetuo-evergreen (L3834-L3872)

### 1. Assess Readiness for Evergreen (elicit: true)

**Objective:** Determine if the webinar is ready for perpetual mode.

```yaml
readiness_criteria:
  - name: "ROAS positivo validado"
    check: "ROAS > 1.0 em pelo menos 1 rodada"
    status: "check from relatorio-kpis"

  - name: "Roteiro validado"
    check: "Roteiro executado com taxa de conversao >= 2%"
    status: "check from relatorio-kpis"

  - name: "Funil operacional funcional"
    check: "Todas as 7 etapas do funil configuradas e testadas"
    status: "check from funil-7-etapas existence"

  - name: "Gravacao de alta qualidade"
    check: "Video do webinario gravado com boa qualidade (audio, video, slides)"
    status: "ask user"
```

**Elicitation:**

```yaml
elicit: true
format: sequential-questions
questions:
  - id: gravacao_disponivel
    question: "Voce ja tem uma gravacao do webinario com boa qualidade de audio e video?"
    why: "O modo perpetuo roda a gravacao automaticamente. A qualidade da gravacao impacta diretamente a conversao."
    required: true

  - id: frequencia_desejada
    question: |
      Com que frequencia voce quer rodar o webinario perpetuo?
      1. Diario (webinario disponivel todo dia)
      2. A cada 2-3 dias
      3. Semanal (1 sessao por semana)
      4. Sob demanda (lead agenda quando quiser)
    why: "A frequencia afeta o volume de leads necessario e a urgencia percebida."
    required: true

  - id: investimento_midia_mensal
    question: "Quanto pretende investir em midia por mes no modo perpetuo? (R$)"
    why: "Preciso calcular o funil semanal/mensal projetado baseado no CPL real."
    required: true

  - id: chat_simulado
    question: "Voce quer usar chat simulado no EverWebinar? (mensagens automaticas aparecendo durante o webinario)"
    why: "Chat simulado aumenta a percepcao de evento ao vivo e engajamento. A metodologia recomenda usar."
    required: true
```

### 2. Design Evergreen Funnel

**Objective:** Map the perpetual funnel structure based on methodology.

```yaml
evergreen_funnel:
  captacao:
    mode: "Continua (ads sempre ativos)"
    agendamento: "{{frequencia_desejada}}"
    pagina_captura: "Mesma pagina, com agendamento automatico"

  nutricao:
    mode: "Automatizada"
    messages: "Sequencia de mensagens WhatsApp adaptada para perpetuo (sem datas fixas, com {data_webinario} dinamica)"
    timing: "Baseado na data de inscricao do lead"

  webinario:
    mode: "Gravado no EverWebinar"
    chat_simulado: "{{chat_simulado}}"
    agendamento_recorrente: "{{frequencia_desejada}}"
    one_click_registration: true

  pos_webinario:
    mode: "Automacao completa"
    replay: "Disponivel por tempo limitado apos sessao"
    fechamento: "Deadline relativo (ex: 48h apos o webinario)"
    downsell: "Ativado automaticamente apos deadline"

  funil_semanal_projetado:
    leads_por_semana: "investimento_midia_mensal / 4 / cpl_real"
    comparecimentos: "leads_semana * taxa_comparecimento_real"
    vendas: "leads_semana * taxa_conversao_real"
    faturamento_semanal: "vendas * ticket"
    faturamento_mensal: "faturamento_semanal * 4"
```

### 3. Project Monthly ROI

**Objective:** Calculate monthly projections using real data.

- Use real CPL, conversion rate, attendance from relatorio-kpis
- Calculate: leads/week, sales/week, revenue/week, monthly totals
- Compare with monthly ad spend
- Present: ROAS mensal projetado, margem, breakeven

### 4. Plan Configuration Changes

**Objective:** List what needs to change from launch mode to perpetual mode.

```yaml
configuration_changes:
  everwebinar:
    - "Alterar agendamento de 'evento unico' para 'recorrente {{frequencia}}'"
    - "Configurar chat simulado (se escolhido)"
    - "Habilitar one-click registration"
    - "Configurar replay com timer relativo"

  sendflow:
    - "Adaptar mensagens para datas dinamicas (variavel {{data_webinario}})"
    - "Configurar triggers por data de inscricao (nao data fixa)"
    - "Manter automacao rodando continuamente"

  pagamento:
    - "Manter webhooks ativos 24/7"
    - "Configurar deadline relativo por comprador"

  ads:
    - "Configurar campanha continua (sem data de inicio/fim)"
    - "Otimizar lookalike com base de compradores da rodada anterior"
    - "Budget diario estavel: investimento_mensal / 30"
```

### 5. Generate Strategy Document

- Load template: `.aiox-core/development/templates/webinar-estrategia-perpetuo-tmpl.md`
- Populate: readiness assessment, evergreen funnel design, monthly projections, configuration changes
- Save to: `docs/webinar/estrategias/estrategia-perpetuo.md`

### 6. Present Summary

- Present monthly projection summary
- List configuration changes needed
- Recommend:
  - @webinar-operator for EverWebinar reconfiguration
  - @webinar-creator for message adaptation (dates -> dynamic variables)
- Inform user of saved file location

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] estrategia-perpetuo.md created in docs/webinar/estrategias/
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
command: "*perpetuo"
dependencies:
  - roteiro-completo.md (required)
  - relatorio-kpis.md (required)
  - guia-everwebinar.md (optional)
tags:
  - strategy
  - evergreen
  - perpetual
  - advanced
  - webinar
updated_at: 2026-03-05
```

---

## Handoff

next_agent: "@webinar-operator"
next_command: "*setup-everwebinar"
condition: Evergreen strategy approved, EverWebinar reconfiguration needed
alternatives:
  - agent: "@webinar-creator", command: "*mensagens", condition: Messages need adaptation for dynamic dates
  - agent: "@webinar-analyst", command: "*empilhamento", condition: User wants to combine perpetual + stacking
