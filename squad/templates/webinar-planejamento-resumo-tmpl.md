# Relatório Consolidado de Planejamento

> **Rodada:** {{rodada}}
> **Data de geração:** {{data}}
> **Agente:** @webinar-strategist (Sage)
> **Status:** {{status_planejamento}}

---

## 1. Visão Geral do Webinário

| Atributo | Valor |
|----------|-------|
| **Nome do webinário** | {{titulo_webinar}} |
| **Grande Promessa** | {{grande_promessa}} |
| **Mecanismo Único** | {{mecanismo_unico}} |
| **Público-alvo** | {{publico_alvo}} |
| **Ticket** | R$ {{ticket}} |
| **Formato** | {{formato}} |
| **Data/Frequência** | {{data_frequencia}} |
| **Plataforma** | {{plataforma}} |
| **Duração estimada** | {{duracao}} |

---

## 2. O Avatar

### Perfil Consolidado

**Quem é:** {{perfil_avatar}}

**Top 3 Desejos:**
{{#desejos}}
{{numero}}. {{desejo}}
{{/desejos}}

**Dor Principal:** {{dor_principal}}

**Obstáculos:**
- Internos: {{obstaculos_internos}}
- Externos: {{obstaculos_externos}}

**Desejos Ocultos:** {{desejos_ocultos}}

### One Big Domino

> {{one_big_domino}}

---

## 3. A Oferta

### Mecanismo Único

**Nome:** {{mecanismo_unico}}
**Conceito:** {{descricao_mecanismo}}

### Stack Slide (Entregáveis)

| # | Item | Valor (R$) |
|---|------|------------|
{{#entregaveis}}
| {{numero}} | {{nome}} | R$ {{valor}} |
{{/entregaveis}}
| | **Subtotal Entregáveis** | **R$ {{total_entregaveis}}** |

### Bônus

| # | Bônus | Valor (R$) |
|---|-------|------------|
{{#bonus}}
| {{numero}} | {{nome}} | R$ {{valor}} |
{{/bonus}}
| | **Subtotal Bônus** | **R$ {{total_bonus}}** |

### Dupla Queda de Preço

| Etapa | Valor |
|-------|-------|
| Valor total percebido (Stack + Bônus) | R$ {{valor_total_percebido}} |
| Preço oficial | ~~R$ {{preco_oficial}}~~ |
| **Preço do webinário** | **R$ {{ticket}}** |
| Economia para o participante | R$ {{economia}} ({{pct_desconto}}%) |

### Garantia

{{garantia}}

---

## 4. Estratégia de Crenças

### Crença-Alvo

> {{crenca_alvo}}

### Ponte de Crenças

{{#ponte_crencas}}
{{numero}}. {{topico}}
{{/ponte_crencas}}

### Falsas Crenças a Serem Quebradas

| Falsa Crença | Tipo | Nova Crença |
|--------------|------|-------------|
{{#falsas_crencas}}
| {{falsa_crenca}} | {{tipo}} | {{nova_crenca}} |
{{/falsas_crencas}}

---

## 5. Objeções e Respostas

| # | Objeção | Resposta | Fonte |
|---|---------|----------|-------|
{{#objecoes}}
| {{numero}} | {{objecao}} | {{resposta}} | {{fonte}} |
{{/objecoes}}

---

{{#tem_orcamento}}
## 6. Métricas e Metas

### Funil Projetado

```
CLIQUES           {{cliques}}
    ▼ ({{taxa_captura}}%)
LEADS             {{leads}}
    ▼ ({{taxa_comparecimento}}%)
COMPARECIMENTOS   {{comparecimentos}}
    ▼ ({{taxa_conversao}}%)
VENDAS            {{meta_vendas}}
```

### Financeiro

| Métrica | Valor |
|---------|-------|
| Investimento em mídia | R$ {{investimento}} |
| Faturamento projetado | R$ {{fat_total}} |
| ROAS | {{roas}}x |
| Lucro líquido | R$ {{lucro}} |
| Margem | {{margem_pct}}% |

{{/tem_orcamento}}

---

## 7. Checklist de Prontidão para Construção

| # | Item | Status | Observação |
|---|------|--------|------------|
| 1 | Avatar definido com profundidade | {{status_avatar}} | {{obs_avatar}} |
| 2 | Grande Promessa clara e objetiva | {{status_promessa}} | {{obs_promessa}} |
| 3 | Mecanismo Único nomeado | {{status_mecanismo}} | {{obs_mecanismo}} |
| 4 | Crença-alvo articulada | {{status_crenca}} | {{obs_crenca}} |
| 5 | Oferta completa com Stack | {{status_oferta}} | {{obs_oferta}} |
| 6 | Objeções mapeadas e respondidas | {{status_objecoes}} | {{obs_objecoes}} |
| 7 | Metas financeiras calculadas | {{status_metas}} | {{obs_metas}} |

**Prontidão geral:** {{itens_prontos}}/7 ({{pct_prontidao}}%)

---

## 8. Próximos Passos

### Fase de Construção (@webinar-creator / Spark)

O @webinar-creator usará este planejamento para gerar:

| # | Artefato | Comando | Input Principal |
|---|----------|---------|-----------------|
| 1 | Roteiro — Abertura | `*abertura` | Avatar + Canvas Produto |
| 2 | Roteiro — Empatia | `*empatia` | Avatar + Canvas Cliente |
| 3 | Roteiro — Conteúdo | `*conteudo` | Avatar + Canvas Webinário (Blocos 10-11) |
| 4 | Roteiro — Pitch | `*pitch` | Canvas Webinário (Blocos 12-15) + Canvas Produto |
| 5 | Roteiro Completo | `*roteiro` | Todos os 4 acima |
| 6 | Mensagens WhatsApp | `*mensagens` | Canvas Produto + Avatar |
| 7 | Copy — Captura | `*copy-captura` | Canvas Produto + Avatar |
| 8 | Copy — Replay | `*copy-replay` | Roteiro + Canvas Webinário |
| 9 | Copy — Fechamento | `*copy-fechamento` | Canvas Webinário (Blocos 12-15) |

### Recomendação

{{recomendacao_proximos_passos}}

> Para iniciar a construção: ative **@webinar-creator** e execute `*abertura` ou `*roteiro`.

---

## Canvases Fonte

| Canvas | Arquivo | Status |
|--------|---------|--------|
| Cliente Ideal | `docs/webinar/rodada-{{rodada}}/planejamento/canvas-cliente-ideal.md` | {{status_canvas_cliente}} |
| Produto | `docs/webinar/rodada-{{rodada}}/planejamento/canvas-produto.md` | {{status_canvas_produto}} |
| Webinário Infalível | `docs/webinar/rodada-{{rodada}}/planejamento/canvas-webinar.md` | {{status_canvas_webinar}} |
| Avatar Blueprint | `docs/webinar/rodada-{{rodada}}/planejamento/avatar-blueprint.md` | {{status_avatar_blueprint}} |
| Orçamento e Meta | `docs/webinar/rodada-{{rodada}}/planejamento/orcamento-meta.md` | {{status_orcamento}} |

---

## Metadata

```yaml
tipo: planejamento-resumo
rodada: {{rodada}}
canvases_consolidados: {{canvases_consolidados}}/5
prontidao: {{pct_prontidao}}%
gerado_em: {{data}}
agente: webinar-strategist
status: {{status_planejamento}}
```
