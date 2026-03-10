# Planilha de Orçamento e Meta

> **Rodada:** {{rodada}}
> **Data de preenchimento:** {{data}}
> **Agente:** @webinar-strategist (Sage)
> **Referência metodológica:** Seção 2, Canvas 4 + Seção 3 (KPIs/Benchmarks) — Webinário Infalível (Taioba)

---

## Premissas (Definidas pelo Usuário)

### Produto Principal

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 1 | Meta de vendas (unidades) | {{meta_vendas}} | — |
| 2 | Ticket do produto | R$ {{ticket}} | Acima de R$200 |
| 3 | Taxa de conversão vendas/leads | {{taxa_conversao}}% | 3% |
| 4 | Taxa de conversão página captura | {{taxa_captura}}% | 40% |
| 5 | Taxa de comparecimento | {{taxa_comparecimento}}% | 25% |

### Order Bump

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 6 | Taxa de order bump | {{taxa_bump}}% | Variável |
| 7 | Ticket order bump | R$ {{ticket_bump}} | — |

### Upsell

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 8 | Taxa de upsell | {{taxa_upsell}}% | Variável |
| 9 | Ticket upsell | R$ {{ticket_upsell}} | — |

### Downsell

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 10 | Taxa de downsell | {{taxa_downsell}}% | Variável |
| 11 | Ticket downsell | R$ {{ticket_downsell}} | — |

### Mídia

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 12 | Custo por lead (CPL) | R$ {{cpl}} | ~10% do ticket |

---

## Cálculos Automáticos do Funil

### Volume do Funil

| Métrica | Fórmula | Resultado |
|---------|---------|-----------|
| **Leads necessários** | Meta ({{meta_vendas}}) / Taxa conversão ({{taxa_conversao}}%) | **{{leads_necessarios}}** |
| **Cliques necessários** | Leads ({{leads_necessarios}}) / Taxa captura ({{taxa_captura}}%) | **{{cliques_necessarios}}** |
| **Comparecimentos esperados** | Leads ({{leads_necessarios}}) x Taxa comp. ({{taxa_comparecimento}}%) | **{{comparecimentos}}** |

### Faturamento

| Receita | Fórmula | Resultado |
|---------|---------|-----------|
| **Produto principal** | {{meta_vendas}} vendas x R$ {{ticket}} | **R$ {{fat_principal}}** |
| **Order bump** | {{meta_vendas}} x {{taxa_bump}}% x R$ {{ticket_bump}} | **R$ {{fat_bump}}** |
| **Upsell** | {{meta_vendas}} x {{taxa_upsell}}% x R$ {{ticket_upsell}} | **R$ {{fat_upsell}}** |
| **Downsell** | ({{leads_necessarios}} - {{meta_vendas}}) x {{taxa_downsell}}% x R$ {{ticket_downsell}} | **R$ {{fat_downsell}}** |
| **FATURAMENTO TOTAL** | | **R$ {{fat_total}}** |

### Investimento e Retorno

| Métrica | Fórmula | Resultado |
|---------|---------|-----------|
| **Investimento em mídia** | {{leads_necessarios}} leads x R$ {{cpl}} | **R$ {{investimento}}** |
| **ROAS** | R$ {{fat_total}} / R$ {{investimento}} | **{{roas}}x** |
| **Lucro líquido** | R$ {{fat_total}} - R$ {{investimento}} | **R$ {{lucro}}** |
| **Margem líquida** | R$ {{lucro}} / R$ {{fat_total}} x 100 | **{{margem_pct}}%** |

---

## Validação vs. Benchmarks

| Métrica | Valor | Benchmark | Status |
|---------|-------|-----------|--------|
| Taxa de conversão | {{taxa_conversao}}% | 3% | {{status_conversao}} |
| Taxa de captura | {{taxa_captura}}% | 40% | {{status_captura}} |
| Taxa de comparecimento | {{taxa_comparecimento}}% | 25% | {{status_comparecimento}} |
| CPL vs. Ticket | R$ {{cpl}} ({{pct_cpl_ticket}}% do ticket) | ~10% | {{status_cpl}} |
| ROAS | {{roas}}x | >= 2x | {{status_roas}} |
| Margem | {{margem_pct}}% | >= 30% | {{status_margem}} |

{{#alertas}}
> **{{tipo}}:** {{mensagem}}
{{/alertas}}

---

## Cenários Comparativos

### Cenário Conservador (premissas -30%)

| Métrica | Valor |
|---------|-------|
| Vendas | {{vendas_conservador}} |
| Faturamento | R$ {{fat_conservador}} |
| ROAS | {{roas_conservador}}x |
| Lucro | R$ {{lucro_conservador}} |

### Cenário Otimista (premissas +30%)

| Métrica | Valor |
|---------|-------|
| Vendas | {{vendas_otimista}} |
| Faturamento | R$ {{fat_otimista}} |
| ROAS | {{roas_otimista}}x |
| Lucro | R$ {{lucro_otimista}} |

---

## Funil Visual

```
CLIQUES           {{cliques_necessarios}}
    │ {{taxa_captura}}%
    ▼
LEADS             {{leads_necessarios}}
    │ {{taxa_comparecimento}}%
    ▼
COMPARECIMENTOS   {{comparecimentos}}
    │ {{taxa_conversao}}%
    ▼
VENDAS            {{meta_vendas}}
    │
    ├── Order Bump ({{taxa_bump}}%) → +R$ {{fat_bump}}
    ├── Upsell ({{taxa_upsell}}%) → +R$ {{fat_upsell}}
    └── Downsell ({{taxa_downsell}}%) → +R$ {{fat_downsell}}

INVESTIMENTO      R$ {{investimento}}
FATURAMENTO       R$ {{fat_total}}
ROAS              {{roas}}x
LUCRO             R$ {{lucro}}
```

---

## Notas

{{notas}}

---

## Cross-References

| Dados importados de... | Fonte |
|------------------------|-------|
| Ticket do produto | Canvas do Produto (se disponível) |
| Ticket, condições | Canvas do Webinário, Bloco 12 (se disponível) |

| Este orçamento alimenta... | Destino |
|----------------------------|---------|
| Timeline da campanha | @webinar-operator (*timeline) — investimento e datas |
| Pitch do roteiro | @webinar-creator (*pitch) — ticket, condições |
| Relatório pós-webinário | @webinar-analyst (*orcado-vs-realizado) — premissas orçadas |
| Planejamento consolidado | @webinar-strategist (*resumo) — métricas e metas |

---

## Metadata

```yaml
canvas: orcamento-meta
rodada: {{rodada}}
premissas_definidas: 12/12
calculos_gerados: true
preenchido_em: {{data}}
agente: webinar-strategist
status: completo
```
