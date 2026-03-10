# Canvas do Webinário Infalível

> **Rodada:** {{rodada}}
> **Data de preenchimento:** {{data}}
> **Agente:** @webinar-strategist (Sage)
> **Referência metodológica:** Seção 2, Canvas 3 — Webinário Infalível (Taioba) + Perfect Webinar (Brunson)

---

## Blocos 1-9: Estrutura Geral

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Tema** | {{tema}} |
| 2 | **Título** | {{titulo}} |
| 3 | **Objetivo** | {{objetivo}} |
| 4 | **Público-alvo** | {{publico}} |
| 5 | **Formato** | {{formato}} |
| 6 | **Data/Frequência** | {{data_frequencia}} |
| 7 | **Plataforma** | {{plataforma}} |
| 8 | **Duração** | {{duracao}} |
| 9 | **Estrutura** | {{estrutura}} |

---

## Bloco 10: Crença-Alvo

> **Fórmula:** "A única forma de ter [transformação] sem [obstáculo] é através do [mecanismo único]"

**Crença-alvo:**
> {{crenca_alvo}}

| Componente | Valor | Fonte |
|------------|-------|-------|
| Transformação | {{transformacao}} | Canvas do Produto (Grande Promessa) |
| Obstáculo | {{obstaculo}} | Avatar Blueprint (Pergunta 3) |
| Mecanismo Único | {{mecanismo_unico}} | Canvas do Produto (Bloco 3-4) |

> Esta é a crença central do webinário. Todo o conteúdo (3 Secrets) será construído para sustentar esta crença.

---

## Bloco 11: Ponte de Crenças

> Lista de tópicos/afirmações que levam a audiência da descrença à crença na Crença-Alvo.

| # | Tópico da Ponte | Tipo |
|---|-----------------|------|
{{#ponte_crencas}}
| {{numero}} | {{topico}} | {{tipo}} |
{{/ponte_crencas}}

> Esses tópicos alimentam os 3 Secrets do conteúdo do webinário (Vehicle, Internal, External).

---

## Bloco 12: Oferta

| Atributo | Valor |
|----------|-------|
| **Ticket (preço)** | R$ {{ticket}} |
| **Condições de pagamento** | {{condicoes_pagamento}} |
| **Garantia** | {{garantia}} |

---

## Bloco 13: Entregáveis (Stack Slide)

| # | Nome | Descrição | Valor (R$) |
|---|------|-----------|------------|
{{#entregaveis}}
| {{numero}} | {{nome}} | {{descricao}} | R$ {{valor}} |
{{/entregaveis}}

| | **TOTAL DO STACK** | | **R$ {{total_stack}}** |

> O Stack Slide mostra todos os entregáveis com valores individuais, soma o total (âncora alta), e depois revela o preço real (dupla queda de preço).

---

## Bloco 14: Bônus

| # | Nome | Descrição | Valor (R$) |
|---|------|-----------|------------|
{{#bonus}}
| {{numero}} | {{nome}} | {{descricao}} | R$ {{valor}} |
{{/bonus}}

| | **TOTAL DE BÔNUS** | | **R$ {{total_bonus}}** |

> Bônus de Ação Rápida: limitação por quantidade, tempo ou evento.

---

## Bloco 15: Objeções e Respostas

| # | Objeção | Resposta |
|---|---------|----------|
{{#objecoes}}
| {{numero}} | {{objecao}} | {{resposta}} |
{{/objecoes}}

> Fonte: Canvas do Cliente Ideal (Pergunta 8) + Avatar Blueprint (Pergunta 7)

---

## Resumo da Oferta (Dupla Queda de Preço)

| Etapa | Valor |
|-------|-------|
| Valor total do Stack (âncora alta) | R$ {{total_stack}} |
| + Bônus | R$ {{total_bonus}} |
| = **Valor total percebido** | **R$ {{valor_total_percebido}}** |
| Preço oficial | ~~R$ {{preco_oficial}}~~ |
| **Preço promocional (webinário)** | **R$ {{ticket}}** |
| Economia | R$ {{economia}} ({{percentual_desconto}}% off) |

---

## Cross-References

| Este canvas alimenta... | Seção |
|-------------------------|-------|
| Roteiro — Abertura | Título (Bloco 2), Público (Bloco 4) |
| Roteiro — Conteúdo | Crença-alvo (Bloco 10), Ponte de crenças (Bloco 11) |
| Roteiro — Pitch | Oferta (12), Stack (13), Bônus (14), Objeções (15) |
| Copy — Página de Captura | Título, Grande Promessa |
| Copy — Página de Fechamento | Oferta, Dupla Queda de Preço |
| Orçamento e Meta | Ticket (Bloco 12) |
| Timeline | Data/Frequência (Bloco 6), Formato (Bloco 5) |

---

## Metadata

```yaml
canvas: webinar-infallible
rodada: {{rodada}}
blocos_preenchidos: {{blocos_preenchidos}}/15
preenchido_em: {{data}}
agente: webinar-strategist
status: completo
```
