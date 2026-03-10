# Funil de 7 Etapas: {{nome_webinario}}

**Template ID:** webinar-funil-7-etapas-template-v1
**Purpose:** Template para visualizacao do funil completo de 7 etapas do webinario
**Usado por:** @webinar-operator (Atlas) -- comando *funil

---

## Template Variables

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `{{nome_webinario}}` | string | Nome do webinario | "Webinario Infalivel" |
| `{{rodada}}` | number | Numero da rodada | 1 |
| `{{data_geracao}}` | string | Data de geracao | "2026-03-10" |
| `{{modo}}` | string | Basica, Escalada ou Ambos | "Basica" |
| `{{etapas}}` | array | 7 etapas com detalhes | [...] |

---

## Document Template

```markdown
# Funil de 7 Etapas do Webinario

> **Rodada:** {{rodada}}
> **Webinario:** {{nome_webinario}}
> **Modo:** {{modo}}
> **Gerado em:** {{data_geracao}}
> **Agente:** @webinar-operator (Atlas)

---

## Diagrama Visual

```
  [1. CAPTACAO]
       |
       v
  [2. NUTRICAO]
       |
       v
  [3. ANTECIPACAO]
       |
       v
  [4. ABERTURA DO CARRINHO]  <-- Pico 1 de Vendas
       |
       v
  [5. AMPLIACAO DO IMPACTO]
       |
       v
  [6. FECHAMENTO DO CARRINHO]  <-- Pico 2 de Vendas
       |
       v
  [7. IMPULSIONAMENTO DO LUCRO]
```

Padrao de vendas: **Pico 1** (abertura) -> **Vale** (meio) -> **Pico 2** (fechamento)

---

## Visao Geral

| # | Etapa | Pilar | Gatilho de Transicao | Status |
|---|-------|-------|---------------------|--------|
| 1 | Captacao | Atracao | Leads suficientes para meta | {{status_etapa_1}} |
| 2 | Nutricao | Engajamento | Data do webinario se aproxima | {{status_etapa_2}} |
| 3 | Antecipacao | Compromisso | D-1 / D-0 | {{status_etapa_3}} |
| 4 | Abertura do Carrinho | Persuasao | Webinario realizado | {{status_etapa_4}} |
| 5 | Ampliacao do Impacto | Urgencia | Replay disponibilizado | {{status_etapa_5}} |
| 6 | Fechamento do Carrinho | Escassez | Deadline definido | {{status_etapa_6}} |
| 7 | Impulsionamento do Lucro | Persuasao + Urgencia | Pos-fechamento | {{status_etapa_7}} |

---

## Detalhamento por Etapa

### Etapa 1: Captacao

- **Pilar:** Atracao
- **Objetivo:** Gerar leads qualificados para atingir a meta de {{meta_leads}} leads
- **Ferramentas:** Facebook Ads, Instagram, pagina de captura, Facebook Pixel
- **Metricas-chave:**
  - CPL (Custo por Lead) -- benchmark: ~10% do ticket
  - Taxa de conversao da pagina de captura -- benchmark: 40%
  - Volume de leads
- **Gatilho de transicao:** Leads suficientes OU data de inicio da nutricao
- **Artefatos:**
  - `copy-pagina-captura.md` — {{status_copy_captura}}
  - `guia-pixel.md` — {{status_pixel}}
- **Status:** {{status_etapa_1}}

---

### Etapa 2: Nutricao

- **Pilar:** Engajamento
- **Objetivo:** Aquecer leads para maximizar comparecimento
- **Ferramentas:** SendFlow (WhatsApp), email
- **Metricas-chave:**
  - Taxa de abertura das mensagens
  - Taxa de resposta/engajamento
- **Mensagens:** 5 mensagens de nutricao
- **Gatilho de transicao:** Data do webinario se aproximando (D-1)
- **Artefatos:**
  - `mensagens-whatsapp.md` (secao nutricao) — {{status_mensagens}}
  - `guia-sendflow.md` — {{status_sendflow}}
- **Status:** {{status_etapa_2}}

---

### Etapa 3: Antecipacao

- **Pilar:** Compromisso
- **Objetivo:** Maximizar taxa de comparecimento no webinario
- **Ferramentas:** SendFlow (WhatsApp), email, SMS (opcional)
- **Metricas-chave:**
  - Taxa de comparecimento -- benchmark: 25%
- **Mensagens:** 2 mensagens D-1 + 7 mensagens D-0
- **Gatilho de transicao:** D-0, hora do webinario
- **Artefatos:**
  - `mensagens-whatsapp.md` (secao antecipacao) — {{status_mensagens}}
- **Status:** {{status_etapa_3}}

---

### Etapa 4: Abertura do Carrinho

- **Pilar:** Persuasao
- **Objetivo:** Converter presentes em compradores (Pico 1 de vendas)
- **Ferramentas:** EverWebinar, checkout da plataforma de pagamento
- **Metricas-chave:**
  - Taxa de conversao vendas/leads -- benchmark: 3%
  - Vendas na abertura
- **Gatilho de transicao:** Webinario realizado
- **Artefatos:**
  - `roteiro-completo.md` — {{status_roteiro}}
  - `guia-everwebinar.md` — {{status_everwebinar}}
  - `guia-pagamento.md` — {{status_pagamento}}
- **Status:** {{status_etapa_4}}

---

### Etapa 5: Ampliacao do Impacto

- **Pilar:** Urgencia
- **Objetivo:** Recuperar quem nao compareceu ou nao comprou
- **Ferramentas:** Pagina de replay, SendFlow, email, retargeting
- **Metricas-chave:**
  - Taxa de replay
  - Conversao do replay
- **Mensagens:** 1 pos-webinario + 7 ampliacao
- **Gatilho de transicao:** Replay disponibilizado
- **Artefatos:**
  - `copy-pagina-replay.md` — {{status_copy_replay}}
  - `mensagens-whatsapp.md` (secao ampliacao) — {{status_mensagens}}
- **Status:** {{status_etapa_5}}

---

### Etapa 6: Fechamento do Carrinho

- **Pilar:** Escassez
- **Objetivo:** Converter indecisos com urgencia maxima (Pico 2 de vendas)
- **Ferramentas:** Pagina de fechamento, SendFlow, email, countdown
- **Metricas-chave:**
  - Vendas no fechamento
  - Taxa de escassez
- **Mensagens:** 11 mensagens de fechamento
- **Gatilho de transicao:** Deadline definido atingido
- **Artefatos:**
  - `copy-pagina-fechamento.md` — {{status_copy_fechamento}}
  - `mensagens-whatsapp.md` (secao fechamento) — {{status_mensagens}}
- **Status:** {{status_etapa_6}}

---

### Etapa 7: Impulsionamento do Lucro

- **Pilar:** Persuasao + Urgencia
- **Objetivo:** Maximizar receita pos-fechamento com downsell/upsell
- **Ferramentas:** SendFlow, checkout
- **Metricas-chave:**
  - Taxa de downsell
  - Receita adicional
  - LTV (Lifetime Value)
- **Mensagens:** 8 mensagens de downsell
- **Gatilho de transicao:** Pos-fechamento do carrinho
- **Artefatos:**
  - `mensagens-whatsapp.md` (secao downsell) — {{status_mensagens}}
- **Status:** {{status_etapa_7}}

---

{{#if modo_comparacao}}
## Comparacao: Basica vs. Escalada

| Aspecto | Estrutura Basica | Estrutura Escalada |
|---------|------------------|--------------------|
| **Objetivo** | Validar oferta e mensagem | Escalar volume e receita |
| **Investimento** | Baixo (validacao) | Alto (escala) |
| **Captacao** | Organico + ads basico | Ads agressivo + multiplas fontes |
| **Automacao** | Basica (SendFlow manual) | Completa (webhooks + tags + automacoes) |
| **Chat** | Opcional | Obrigatorio (simulado otimizado) |
| **Replay** | Simples | Com segmentacao e retargeting |
| **Downsell** | Opcional | Obrigatorio |
| **Metricas** | Basicas (CPL, conversao) | Avancadas (ROAS, LTV, CAC) |
| **Empilhamento** | Nao aplica (1a rodada) | Sim (2a+ rodada com leads existentes) |
{{/if}}

---

## Metricas e Benchmarks Consolidados

| Metrica | Benchmark | Etapa |
|---------|-----------|-------|
| CPL (Custo por Lead) | ~10% do ticket | Captacao |
| Taxa conversao pagina captura | 40% | Captacao |
| Taxa de comparecimento | 25% | Antecipacao |
| Taxa conversao vendas/leads | 3% | Abertura |
| Padrao de vendas | Pico-Vale-Pico | Abertura + Fechamento |
| Custo lead empilhamento | R$0,06-0,25 (API) | Impulsionamento |

---

## Status Geral

- **Artefatos prontos:** {{total_prontos}} de {{total_artefatos}}
- **Artefatos pendentes:** {{total_pendentes}}
- **Etapas prontas para execucao:** {{etapas_prontas}} de 7
- **Veredicto:** {{veredicto_geral}}

### Proximos Passos

{{#each proximos_passos}}
{{this.prioridade}}. {{this.acao}} — `{{this.comando}}`
{{/each}}

---

> Funil gerado por @webinar-operator (Atlas)
> Metodologia: Webinario Infalivel (Taioba) + Perfect Webinar (Brunson)
```

---

## Usage Notes

1. **Status Values:** Use "Pronto", "Pendente", "Em Andamento", or "N/A"
2. **Status Detection:** Check file existence in `docs/webinar/rodada-{N}/` to auto-detect status
3. **Mode Selection:** User chooses Basica, Escalada, or Ambos in elicitation
4. **Cross-reference:** Pull benchmark data from knowledge base sections A.3 and A.4

---

**Template Version:** 1.0.0
**Created:** 2026-03-05
**Part of:** Squad Webinario (@webinar-operator)
