# Relatorio de KPIs — Rodada {{rodada_numero}}

> **Gerado por:** @webinar-analyst (Lens)
> **Data:** {{data_geracao}}
> **Campanha:** {{nome_campanha}}
> **Periodo:** {{data_inicio}} a {{data_fim}}

---

## 1. Resumo Executivo

{{resumo_executivo}}

**Veredicto Geral:** {{veredicto}} <!-- POSITIVO | ATENCAO | CRITICO -->

---

## 2. KPIs do Funil

| # | Metrica | Valor Real | Benchmark | Projetado | Status | Desvio |
|---|---------|-----------|-----------|-----------|--------|--------|
| 1 | CPL (Custo por Lead) | R$ {{cpl_real}} | ~10% do ticket (R$ {{cpl_benchmark}}) | R$ {{cpl_projetado}} | {{cpl_status}} | {{cpl_desvio}}% |
| 2 | Total de Leads | {{total_leads}} | — | {{leads_projetados}} | {{leads_status}} | {{leads_desvio}}% |
| 3 | Taxa de Captura | {{taxa_captura_real}}% | 40% | {{taxa_captura_projetada}}% | {{captura_status}} | {{captura_desvio}}% |
| 4 | Total de Comparecimentos | {{total_comparecimentos}} | — | {{comparecimentos_projetados}} | {{comparecimentos_status}} | {{comparecimentos_desvio}}% |
| 5 | Taxa de Comparecimento | {{taxa_comparecimento_real}}% | 25% | {{taxa_comparecimento_projetada}}% | {{comparecimento_status}} | {{comparecimento_desvio}}% |
| 6 | Total de Vendas | {{total_vendas}} | — | {{vendas_projetadas}} | {{vendas_status}} | {{vendas_desvio}}% |
| 7 | Taxa de Conversao (Vendas/Leads) | {{taxa_conversao_real}}% | 3% | {{taxa_conversao_projetada}}% | {{conversao_status}} | {{conversao_desvio}}% |
| 8 | Taxa de Conversao (Vendas/Comparecimentos) | {{taxa_conv_comparecimentos}}% | 12% | — | {{conv_comp_status}} | — |

> **Legenda Status:** ACIMA | DENTRO | ABAIXO | CRITICO

---

## 3. KPIs de Resultado

| # | Metrica | Valor Real | Projetado | Desvio |
|---|---------|-----------|-----------|--------|
| 1 | Investimento em Ads | R$ {{investimento_real}} | R$ {{investimento_projetado}} | {{invest_desvio}}% |
| 2 | Faturamento Bruto | R$ {{faturamento_bruto}} | R$ {{faturamento_projetado}} | {{fat_desvio}}% |
| 3 | Order Bump | R$ {{order_bump_total}} | R$ {{order_bump_projetado}} | {{bump_desvio}}% |
| 4 | Upsell | R$ {{upsell_total}} | R$ {{upsell_projetado}} | {{upsell_desvio}}% |
| 5 | Downsell | R$ {{downsell_total}} | R$ {{downsell_projetado}} | {{downsell_desvio}}% |
| 6 | **Faturamento Total** | **R$ {{faturamento_total}}** | **R$ {{faturamento_total_projetado}}** | **{{fat_total_desvio}}%** |
| 7 | ROAS | {{roas_real}}x | {{roas_projetado}}x | {{roas_desvio}}% |
| 8 | Margem Liquida | {{margem_real}}% | {{margem_projetada}}% | {{margem_desvio}}% |
| 9 | Ticket Medio Real | R$ {{ticket_medio_real}} | R$ {{ticket_produto}} | {{ticket_desvio}}% |

---

## 4. Distribuicao de Vendas por Etapa

| Etapa do Funil | Vendas | % do Total | Padrao Esperado |
|----------------|--------|-----------|-----------------|
| Abertura do Carrinho (Pico 1) | {{vendas_abertura}} | {{pct_abertura}}% | Alto (pico) |
| Replay / Ampliacao (Vale) | {{vendas_replay}} | {{pct_replay}}% | Medio (vale) |
| Fechamento (Pico 2) | {{vendas_fechamento}} | {{pct_fechamento}}% | Alto (pico) |
| **Total** | **{{total_vendas}}** | **100%** | **Pico-Vale-Pico** |

> **Padrao da Metodologia:** Pico 1 (abertura) > Vale (replay) < Pico 2 (fechamento)
> **Seu padrao:** {{padrao_vendas_real}}

---

## 5. Top Insights

### {{insight_1_titulo}}
{{insight_1_descricao}}
> **Referencia Metodologica:** {{insight_1_ref}}

### {{insight_2_titulo}}
{{insight_2_descricao}}
> **Referencia Metodologica:** {{insight_2_ref}}

### {{insight_3_titulo}}
{{insight_3_descricao}}
> **Referencia Metodologica:** {{insight_3_ref}}

---

## 6. Proximos Passos Recomendados

| # | Acao | Comando | Agente |
|---|------|---------|--------|
| 1 | {{acao_1}} | {{comando_1}} | {{agente_1}} |
| 2 | {{acao_2}} | {{comando_2}} | {{agente_2}} |
| 3 | {{acao_3}} | {{comando_3}} | {{agente_3}} |

---

## 7. Dados Brutos Coletados

```yaml
dados_coletados:
  investimento_ads: {{investimento_real}}
  total_leads: {{total_leads}}
  total_comparecimentos: {{total_comparecimentos}}
  total_vendas: {{total_vendas}}
  faturamento_bruto: {{faturamento_bruto}}
  vendas_abertura: {{vendas_abertura}}
  vendas_replay: {{vendas_replay}}
  vendas_fechamento: {{vendas_fechamento}}
  taxa_captura: {{taxa_captura_real}}
  order_bump: {{order_bump_total}}
  upsell: {{upsell_total}}
  downsell: {{downsell_total}}
  data_coleta: {{data_geracao}}
```

---

*Gerado por @webinar-analyst (Lens) — Metodologia Fusionada Taioba + Brunson*
