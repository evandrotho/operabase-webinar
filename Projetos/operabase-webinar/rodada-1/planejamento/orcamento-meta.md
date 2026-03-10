# Planilha de Orcamento e Meta

> **Rodada:** 1
> **Data de preenchimento:** 2026-03-05
> **Agente:** @webinar-strategist (Sage)
> **Projeto:** Operabase Webinar
> **Referencia metodologica:** Secao 2, Canvas 4 + Secao 3 (KPIs/Benchmarks) — Webinario Infalivel (Taioba)

---

## Premissas (Definidas pelo Usuario)

### Produto Principal

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 1 | Meta de vendas (por webinario) | 4-5 unidades | — |
| 2 | Ticket do produto | R$2.500 | Acima de R$200 |
| 3 | Taxa de conversao vendas/leads | 3% | 3% |
| 4 | Taxa de conversao pagina captura | 40% | 40% |
| 5 | Taxa de comparecimento | 25% | 25% |

### Order Bump

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 6 | Taxa de order bump | 0% | Variavel |
| 7 | Ticket order bump | R$0 | — |

### Upsell

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 8 | Taxa de upsell | 0% | Variavel |
| 9 | Ticket upsell | R$0 | — |

### Downsell

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 10 | Taxa de downsell | 0% | Variavel |
| 11 | Ticket downsell | R$0 | — |

### Midia

| # | Premissa | Valor | Benchmark |
|---|----------|-------|-----------|
| 12 | Custo por lead (CPL) | R$20 | ~10% do ticket |

### Investimento

| # | Premissa | Valor |
|---|----------|-------|
| — | Investimento semanal em midia | R$3.000 |

---

## Calculos Automaticos do Funil (por webinario)

### Volume do Funil

| Metrica | Formula | Resultado |
|---------|---------|-----------|
| **Leads possiveis** | R$3.000 / R$20 (CPL) | **150 leads** |
| **Cliques necessarios** | 150 leads / 40% | **375 cliques** |
| **Comparecimentos esperados** | 150 leads × 25% | **38 presentes** |
| **Vendas esperadas** | 150 leads × 3% | **4-5 vendas** |

### Faturamento (por webinario)

| Receita | Formula | Resultado |
|---------|---------|-----------|
| **Produto principal** | 4,5 vendas × R$2.500 | **R$11.250** |
| Order bump | — | R$0 |
| Upsell | — | R$0 |
| Downsell | — | R$0 |
| **FATURAMENTO TOTAL** | | **R$11.250** |

### Investimento e Retorno (por webinario)

| Metrica | Formula | Resultado |
|---------|---------|-----------|
| **Investimento em midia** | 150 leads × R$20 | **R$3.000** |
| **ROAS** | R$11.250 / R$3.000 | **3,75x** |
| **Lucro liquido** | R$11.250 - R$3.000 | **R$8.250** |
| **Margem liquida** | R$8.250 / R$11.250 × 100 | **73,3%** |

---

## Projecao Mensal (4 webinarios)

| Metrica | Semanal | Mensal (×4) |
|---------|---------|-------------|
| Investimento | R$3.000 | **R$12.000** |
| Leads | 150 | **600** |
| Vendas | 4-5 | **18-20** |
| Faturamento | R$11.250 | **R$45.000-50.000** |
| Lucro | R$8.250 | **R$33.000** |
| ROAS | 3,75x | **3,75x** |

---

## Validacao vs. Benchmarks

| Metrica | Valor | Benchmark | Status |
|---------|-------|-----------|--------|
| Taxa de conversao | 3% | 3% | No benchmark |
| Taxa de captura | 40% | 40% | No benchmark |
| Taxa de comparecimento | 25% | 25% | No benchmark |
| CPL vs. Ticket | R$20 (0,8% do ticket) | ~10% | Excelente |
| ROAS | 3,75x | >= 2x | Saudavel |
| Margem | 73,3% | >= 30% | Excelente |

---

## Cenarios Comparativos

### Cenario Conservador (conversao -30%)

| Metrica | Valor |
|---------|-------|
| Taxa de conversao | 2,1% |
| Vendas/semana | 3 |
| Faturamento/semana | R$7.500 |
| ROAS | 2,5x |
| Lucro/semana | R$4.500 |
| Lucro/mes | R$18.000 |

### Cenario Otimista (conversao +30%)

| Metrica | Valor |
|---------|-------|
| Taxa de conversao | 3,9% |
| Vendas/semana | 6 |
| Faturamento/semana | R$15.000 |
| ROAS | 5,0x |
| Lucro/semana | R$12.000 |
| Lucro/mes | R$48.000 |

---

## Funil Visual (por webinario)

```
CLIQUES           375
    | 40%
    v
LEADS             150
    | 25%
    v
COMPARECIMENTOS   38
    | 3%
    v
VENDAS            4-5

INVESTIMENTO      R$3.000
FATURAMENTO       R$11.250
ROAS              3,75x
LUCRO             R$8.250
```

---

## Notas

- Investimento de R$3.000 por semana em midia paga (Facebook/Instagram Ads)
- Webinario recorrente toda terca-feira a partir de 10/03/2026
- Premissas de order bump, upsell e downsell zeradas nesta rodada — podem ser adicionadas futuramente para aumentar o faturamento sem aumentar investimento em midia
- CPL de R$20 e agressivo para nicho de negocios — monitorar nas primeiras semanas e ajustar se necessario
- A projecao mensal assume 4 webinarios/mes com mesmas premissas

---

## Cross-References

| Dados importados de... | Fonte |
|------------------------|-------|
| Ticket do produto | Canvas do Produto (R$2.500) |
| Condicoes de pagamento | Canvas do Webinario, Bloco 12 (a vista ou 12x) |

| Este orcamento alimenta... | Destino |
|----------------------------|---------|
| Timeline da campanha | @webinar-operator (*timeline) — investimento e datas |
| Pitch do roteiro | @webinar-creator (*pitch) — ticket, condicoes |
| Relatorio pos-webinario | @webinar-analyst (*orcado-vs-realizado) — premissas orcadas |
| Planejamento consolidado | @webinar-strategist (*resumo) — metricas e metas |

---

## Metadata

```yaml
canvas: orcamento-meta
rodada: 1
premissas_definidas: 12/12
calculos_gerados: true
preenchido_em: "2026-03-05"
agente: webinar-strategist
projeto: operabase-webinar
status: completo
```
