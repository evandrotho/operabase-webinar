# Orcado vs Realizado — Rodada {{rodada_numero}}

> **Gerado por:** @webinar-analyst (Lens)
> **Data:** {{data_geracao}}
> **Base:** orcamento-meta.md + relatorio-kpis.md

---

## 1. Resumo

**Premissa de Maior Impacto:** {{premissa_maior_impacto}} — desvio de {{desvio_maior}}%, representando R$ {{impacto_financeiro}} de diferenca.

**Veredicto:** {{veredicto}} <!-- DENTRO DO ESPERADO | DESVIOS MODERADOS | DESVIOS SIGNIFICATIVOS -->

---

## 2. Comparacao das 12 Premissas

| # | Premissa | Projetado | Realizado | Desvio | Status |
|---|---------|-----------|-----------|--------|--------|
| P1 | Meta de vendas (unidades) | {{p1_projetado}} | {{p1_realizado}} | {{p1_desvio}}% | {{p1_status}} |
| P2 | Ticket do produto (R$) | R$ {{p2_projetado}} | R$ {{p2_realizado}} | {{p2_desvio}}% | {{p2_status}} |
| P3 | Taxa de conversao vendas/leads | {{p3_projetado}}% | {{p3_realizado}}% | {{p3_desvio}}% | {{p3_status}} |
| P4 | Taxa de conversao pagina captura | {{p4_projetado}}% | {{p4_realizado}}% | {{p4_desvio}}% | {{p4_status}} |
| P5 | Taxa de comparecimento | {{p5_projetado}}% | {{p5_realizado}}% | {{p5_desvio}}% | {{p5_status}} |
| P6 | Taxa de order bump | {{p6_projetado}}% | {{p6_realizado}}% | {{p6_desvio}}% | {{p6_status}} |
| P7 | Ticket order bump (R$) | R$ {{p7_projetado}} | R$ {{p7_realizado}} | {{p7_desvio}}% | {{p7_status}} |
| P8 | Taxa de upsell | {{p8_projetado}}% | {{p8_realizado}}% | {{p8_desvio}}% | {{p8_status}} |
| P9 | Ticket upsell (R$) | R$ {{p9_projetado}} | R$ {{p9_realizado}} | {{p9_desvio}}% | {{p9_status}} |
| P10 | Taxa de downsell | {{p10_projetado}}% | {{p10_realizado}}% | {{p10_desvio}}% | {{p10_status}} |
| P11 | Ticket downsell (R$) | R$ {{p11_projetado}} | R$ {{p11_realizado}} | {{p11_desvio}}% | {{p11_status}} |
| P12 | Custo por lead em midia (R$) | R$ {{p12_projetado}} | R$ {{p12_realizado}} | {{p12_desvio}}% | {{p12_status}} |

> **Legenda Status:** DENTRO (-5% a +5%) | ACIMA (>+5%) | ABAIXO (<-5%) | DESVIO SIGNIFICATIVO (>+/-20%)

---

## 3. Resultados Calculados

| Metrica Calculada | Projetado | Realizado | Desvio |
|-------------------|-----------|-----------|--------|
| Leads necessarios | {{leads_projetados}} | {{leads_reais}} | {{leads_desvio}}% |
| Cliques necessarios | {{cliques_projetados}} | {{cliques_reais}} | {{cliques_desvio}}% |
| Comparecimentos | {{comparecimentos_projetados}} | {{comparecimentos_reais}} | {{comp_desvio}}% |
| Faturamento Bruto | R$ {{fat_bruto_projetado}} | R$ {{fat_bruto_real}} | {{fat_bruto_desvio}}% |
| Faturamento Total | R$ {{fat_total_projetado}} | R$ {{fat_total_real}} | {{fat_total_desvio}}% |
| Investimento em Ads | R$ {{invest_projetado}} | R$ {{invest_real}} | {{invest_desvio}}% |
| ROAS | {{roas_projetado}}x | {{roas_real}}x | {{roas_desvio}}% |
| Margem Liquida | {{margem_projetada}}% | {{margem_real}}% | {{margem_desvio}}% |

---

## 4. Analise de Impacto por Premissa

### Ranking de Impacto Financeiro

| # | Premissa | Desvio | Impacto no Resultado (R$) | Explicacao |
|---|---------|--------|--------------------------|------------|
| 1 | {{imp1_premissa}} | {{imp1_desvio}}% | R$ {{imp1_valor}} | {{imp1_explicacao}} |
| 2 | {{imp2_premissa}} | {{imp2_desvio}}% | R$ {{imp2_valor}} | {{imp2_explicacao}} |
| 3 | {{imp3_premissa}} | {{imp3_desvio}}% | R$ {{imp3_valor}} | {{imp3_explicacao}} |

---

## 5. Premissas a Recalibrar para Proxima Rodada

| Premissa | Valor Atual | Valor Sugerido | Justificativa |
|---------|------------|----------------|---------------|
| {{recal1_premissa}} | {{recal1_atual}} | {{recal1_sugerido}} | {{recal1_justificativa}} |
| {{recal2_premissa}} | {{recal2_atual}} | {{recal2_sugerido}} | {{recal2_justificativa}} |
| {{recal3_premissa}} | {{recal3_atual}} | {{recal3_sugerido}} | {{recal3_justificativa}} |

---

## 6. Contexto do Usuario

{{contexto_qualitativo}}

---

## 7. Proximos Passos

| # | Acao | Comando |
|---|------|---------|
| 1 | Planejar proxima rodada com premissas recalibradas | `*proxima-rodada` |
| 2 | {{prox_passo_2}} | {{prox_comando_2}} |

---

*Gerado por @webinar-analyst (Lens) — Comparacao baseada nas 12 premissas da Metodologia Fusionada*
