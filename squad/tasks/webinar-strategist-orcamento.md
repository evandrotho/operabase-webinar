---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
- Agent asks all 12 premises, calculates, generates spreadsheet
- **Best for:** Experienced users with all numbers ready

### 2. Interactive Mode - Balanced, Educational (12-18 prompts) **[DEFAULT]**
- One premise at a time with benchmark explanation
- Shows calculations step by step
- **Best for:** First-time users, understanding the funnel math

### 3. Pre-Flight Planning - Review Existing Budget
- Load existing budget, show changes needed
- **Best for:** Updating for next round with real data

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: orcamentoMeta()
responsável: Sage (Strategist)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "canvas-orcamento"
      lines: "L284-L338"
      purpose: "12 premissas da Planilha de Orçamento e Meta"
    - id: "formulas-funil"
      lines: "L375-L389"
      purpose: "Fórmulas de cálculo do funil — leads, cliques, comparecimentos, ROAS"
    - id: "kpis-funil"
      lines: "L339-L352"
      purpose: "Benchmarks de KPIs do funil"
    - id: "glossario"
      lines: "L3041-L3118"
      purpose: "Glossário de termos proprietários"

**Entrada:**
- campo: rodada
  tipo: number
  origem: Auto-detect or User Input
  obrigatório: true
  default: 1

**Inputs opcionais:**
- campo: canvas-produto.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: false
  purpose: Ticket do produto, oferta (para pré-preencher premissas 2, 7, 9, 11)

**Saída:**
- campo: orcamento_file
  tipo: string
  destino: docs/webinar/rodada-{N}/planejamento/orcamento-meta.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] No mandatory prerequisites — user provides premises directly
    tipo: pre-condition
    blocker: false
  - [ ] Optional: canvas-produto.md exists (enriches ticket and offer data)
    tipo: pre-condition
    blocker: false
```

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] File created at docs/webinar/rodada-{N}/planejamento/orcamento-meta.md
    tipo: post-condition
    blocker: true
  - [ ] All 12 premises have values
    tipo: post-condition
    blocker: true
  - [ ] Automatic calculations section is populated (leads, cliques, ROAS, margem)
    tipo: post-condition
    blocker: true
```

---

# Planilha de Orçamento e Meta — Task

## Purpose

Conduzir o usuário pelo preenchimento das 12 premissas da Planilha de Orçamento e Meta (Canvas 4), calculando automaticamente leads necessários, cliques, comparecimentos, faturamento bruto, faturamento total (com bump/upsell/downsell), investimento em ads, ROAS e margem líquida.

## SEQUENTIAL Task Execution

### 0. Setup e Cross-Reference

- Detectar rodada ativa
- Verificar se `canvas-produto.md` existe — extrair ticket, condições
- Se existir: "Encontrei o Canvas do Produto. Vou usar o ticket (R${ticket}) como base."
- Carregar knowledge base: `docs/METHODOLOGY-ANALYSIS.md` linhas L284-L338, L375-L389, L339-L352

### 1. Introdução

> **Planilha de Orçamento e Meta**
>
> Vamos calcular TODAS as métricas do seu funil de webinário.
> São 12 premissas que você define, e eu calculo automaticamente:
> - Quantos leads você precisa captar
> - Quantos cliques precisa gerar
> - Quanto investir em mídia
> - Qual o ROAS esperado
> - Qual a margem líquida
>
> Para cada premissa, vou mostrar o benchmark da metodologia como referência.

### 2. Coletar as 12 Premissas

#### Premissa 1: Meta de vendas (unidades)

```
Quantas VENDAS você quer fazer neste webinário?

Dica: Se é seu primeiro webinário, comece com uma meta conservadora (5-10 vendas).
Se já fez antes, use seus dados reais como base.

Meta de vendas (número de unidades):
```

#### Premissa 2: Ticket do produto (R$)

```
Qual o TICKET (preço) do seu produto?

{Se canvas-produto existe: "Do Canvas do Produto: R${ticket}. Quer manter?"}

A metodologia recomenda ticket acima de R$200 para webinários.
Tickets mais altos (R$997+) são ideais para o formato.

Ticket do produto (R$):
```

#### Premissa 3: Taxa de conversão vendas/leads

```
Qual a taxa de CONVERSÃO que espera? (vendas ÷ leads)

Benchmark da metodologia: 3%
- Primeiro webinário: 1-2% (conservador)
- Webinário otimizado: 3-5%
- Top performers: 5-10%

Taxa de conversão (%):
[Sugestão: 3% se for primeiro webinário]
```

#### Premissa 4: Taxa de conversão página de captura

```
Qual a taxa de conversão da PÁGINA DE CAPTURA? (leads ÷ visitantes)

Benchmark da metodologia: 40%
- Página simples (sem ingresso pago): 30-50%
- Página completa (com ingresso pago): 15-25%

Taxa de conversão da página (%):
[Sugestão: 40%]
```

#### Premissa 5: Taxa de comparecimento

```
Qual a taxa de COMPARECIMENTO esperada? (presentes ÷ inscritos)

Benchmark da metodologia: 25%
- Sem aquecimento (nutrição fraca): 10-15%
- Com aquecimento (nutrição forte via WhatsApp): 25-35%
- Evergreen (perpétuo): 20-30%

Taxa de comparecimento (%):
[Sugestão: 25%]
```

#### Premissa 6: Taxa de order bump

```
Você terá ORDER BUMP (compra adicional no checkout)?

Order bump é um produto complementar oferecido durante o pagamento.
Exemplo: "Adicione o pack de templates por R$47"

Se SIM, qual a taxa esperada de adesão (%)?
Se NÃO, digite 0.

Taxa de order bump (%):
```

#### Premissa 7: Ticket do order bump (R$)

```
{Se premissa 6 > 0: "Qual o ticket do order bump? (R$)"}
{Se premissa 6 = 0: Pular esta premissa — valor = 0}
```

#### Premissa 8: Taxa de upsell

```
Você terá UPSELL (oferta superior após a compra)?

Upsell é uma oferta de ticket mais alto logo após a compra principal.
Exemplo: "Faça upgrade para mentoria por R$1.997"

Se SIM, qual a taxa esperada de adesão (%)?
Se NÃO, digite 0.

Taxa de upsell (%):
```

#### Premissa 9: Ticket do upsell (R$)

```
{Se premissa 8 > 0: "Qual o ticket do upsell? (R$)"}
{Se premissa 8 = 0: Pular esta premissa — valor = 0}
```

#### Premissa 10: Taxa de downsell

```
Você terá DOWNSELL (oferta menor para quem não comprou)?

Downsell é uma oferta de ticket mais baixo para quem rejeitou a oferta principal.
Exemplo: "Que tal começar com o módulo básico por R$197?"

Se SIM, qual a taxa esperada de adesão sobre leads não-compradores (%)?
Se NÃO, digite 0.

Taxa de downsell (%):
```

#### Premissa 11: Ticket do downsell (R$)

```
{Se premissa 10 > 0: "Qual o ticket do downsell? (R$)"}
{Se premissa 10 = 0: Pular esta premissa — valor = 0}
```

#### Premissa 12: Custo por lead em mídia (R$)

```
Quanto espera PAGAR POR LEAD em mídia (anúncios)?

Benchmark da metodologia: ~10% do ticket
- Ticket R$500 → CPL R$50
- Ticket R$997 → CPL R$100
- Ticket R$2.000 → CPL R$200

Para primeiro webinário, use um CPL conservador.
Se usar tráfego orgânico (sem anúncios), digite 0.

Custo por lead (R$):
```

### 3. Cálculos Automáticos

Executar TODOS os cálculos e mostrar passo a passo:

```
Calculando suas métricas de funil...

CÁLCULOS DO FUNIL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Leads necessários:
  Meta de vendas ({meta}) ÷ Taxa de conversão ({taxa_conv}%) = {leads} leads

Cliques necessários:
  Leads ({leads}) ÷ Taxa de captura ({taxa_captura}%) = {cliques} cliques

Comparecimentos esperados:
  Leads ({leads}) × Taxa de comparecimento ({taxa_comp}%) = {comparecimentos} presentes

FATURAMENTO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Faturamento bruto (produto principal):
  {meta} vendas × R${ticket} = R${fat_bruto}

Faturamento order bump:
  {meta} vendas × {taxa_bump}% × R${ticket_bump} = R${fat_bump}

Faturamento upsell:
  {meta} vendas × {taxa_upsell}% × R${ticket_upsell} = R${fat_upsell}

Faturamento downsell:
  ({leads} - {meta}) leads não-compradores × {taxa_downsell}% × R${ticket_downsell} = R${fat_downsell}

FATURAMENTO TOTAL: R${fat_total}

INVESTIMENTO E RETORNO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Investimento em mídia:
  {leads} leads × R${cpl} = R${investimento}

ROAS:
  R${fat_total} ÷ R${investimento} = {roas}x

Margem líquida:
  R${fat_total} - R${investimento} = R${margem}
  Margem %: {margem_pct}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 4. Validação dos Resultados

```
VALIDAÇÃO vs. BENCHMARKS:
{Se ROAS < 2: "ALERTA: ROAS de {roas}x está abaixo do mínimo recomendado (2x). Considere ajustar ticket ou CPL."}
{Se ROAS >= 3: "ROAS de {roas}x está saudável."}
{Se margem_pct < 30: "ALERTA: Margem de {margem_pct}% está apertada. Considere aumentar ticket ou reduzir CPL."}
{Se margem_pct >= 50: "Margem de {margem_pct}% está excelente."}

Quer ajustar alguma premissa e recalcular?
```

Se sim, permitir ajuste e recalcular.

### 5. Gerar Planilha

- Carregar template: `.aiox-core/development/templates/webinar-orcamento-meta-tmpl.md`
- Preencher com premissas + cálculos + benchmarks + validação
- Salvar em: `docs/webinar/rodada-{N}/planejamento/orcamento-meta.md`

### 6. Apresentar Resumo e Próximo Passo

```
Planilha de Orçamento e Meta salva em:
docs/webinar/rodada-{N}/planejamento/orcamento-meta.md

Resumo:
- Meta: {meta} vendas de R${ticket}
- Leads necessários: {leads}
- Investimento estimado: R${investimento}
- Faturamento total projetado: R${fat_total}
- ROAS: {roas}x
- Margem: R${margem} ({margem_pct}%)

Próximo passo recomendado:
→ *resumo — gerar relatório consolidado (se todos os canvases estão prontos)
→ *canvas-webinar — se ainda não preencheu o Canvas do Webinário
```

---

## Error Handling

1. **Error:** User enters negative or zero values for ticket/meta
   - **Resolution:** "O valor precisa ser maior que zero. Qual o valor correto?"

2. **Error:** ROAS calculated below 1.0
   - **Resolution:** "ALERTA: Com essas premissas, você teria PREJUÍZO (ROAS {roas}x). Recomendo ajustar: aumentar ticket, reduzir CPL, ou aumentar taxa de conversão."
   - **Recovery:** Loop back to premise adjustment

3. **Error:** CPL is 0 but user expects paid traffic
   - **Resolution:** "Você indicou CPL R$0. Isso significa tráfego 100% orgânico? Se for usar anúncios, defina um CPL."

---

## Handoff

```yaml
next_agent: "@webinar-strategist"
next_command: "*resumo"
condition: Orçamento preenchido e demais canvases disponíveis
alternatives:
  - agent: "@webinar-strategist"
    command: "*canvas-webinar"
    condition: "Canvas do Webinário ainda pendente"
  - agent: "@webinar-creator"
    command: "*roteiro"
    condition: "Planejamento completo"
```

---

## Metadata

```yaml
version: 1.0.0
squad: webinar
agent: webinar-strategist
command: "*orcamento"
prd_reference: "PRD v2.1, Seção 3.2 — Planilha de Orçamento e Meta (12 premissas)"
methodology_reference: "Seção 2, Canvas 4 — METHODOLOGY-ANALYSIS.md L284-L338, L375-L389"
tags:
  - webinar
  - planning
  - budget
  - orcamento
  - funnel-math
updated_at: 2026-03-05
```
