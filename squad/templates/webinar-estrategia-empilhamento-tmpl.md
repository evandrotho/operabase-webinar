# Estrategia de Empilhamento de Webinarios

> **Gerado por:** @webinar-analyst (Lens)
> **Data:** {{data_geracao}}
> **Base:** relatorio-kpis.md (rodada mais recente)

---

## 1. Conceito

O **empilhamento (funnel stacking)** consiste em criar uma sequencia de webinarios, onde cada webinario alimenta o proximo com a base de leads ja qualificados. O custo de reativacao de um lead existente (R$0,06-0,25 via API) e drasticamente menor que captar um novo (R$5-10 via midia paga).

> **Referencia:** Secao 7.3 — Empilhamento (Funnel Stacking)

---

## 2. Avaliacao de Prontidao

| Criterio | Status | Detalhe |
|----------|--------|---------|
| Webinario validado (ROAS > 1.5x) | {{prontidao_roas}} | ROAS atual: {{roas_atual}}x |
| Base de leads existente | {{prontidao_leads}} | {{total_leads_base}} leads disponiveis |
| Produto complementar disponivel | {{prontidao_produto}} | {{produto_complementar}} |

**Veredicto:** {{veredicto_prontidao}} <!-- PRONTO | QUASE PRONTO | NAO RECOMENDADO -->

---

## 3. Sequencia de Empilhamento

### Webinario 1 (Atual — Rodada {{rodada_atual}})

| Aspecto | Detalhe |
|---------|---------|
| Produto | {{web1_produto}} |
| Ticket | R$ {{web1_ticket}} |
| Publico | Lead frio (midia paga) |
| CPL real | R$ {{web1_cpl}} |
| Conversao | {{web1_conversao}}% |
| Status | Executado |

### Webinario 2 (Planejado)

| Aspecto | Detalhe |
|---------|---------|
| Produto | {{web2_produto}} |
| Ticket | R$ {{web2_ticket}} |
| Publico-alvo | {{web2_publico}} |
| CPL estimado | R$ {{web2_cpl_estimado}} |
| Status | Planejamento |

### Webinario 3 (Futuro)

| Aspecto | Detalhe |
|---------|---------|
| Produto | {{web3_produto}} |
| Ticket | R$ {{web3_ticket}} |
| Publico-alvo | Base acumulada Web 1 + Web 2 |
| CPL estimado | R$ {{web3_cpl_estimado}} |
| Status | Futuro |

---

## 4. Segmentacao de Audiencia

| Segmento | Origem | Tamanho Estimado | Acao no Web 2 | CPL |
|----------|--------|-----------------|---------------|-----|
| Compradores Web 1 | Lista de compradores | {{seg_compradores}} | Upsell / cross-sell | R$0,06-0,25 |
| Nao-compradores Web 1 | Lista geral | {{seg_nao_compradores}} | Nova oferta ou angulo | R$0,06-0,25 |
| Leads novos | Midia paga | {{seg_novos}} | Captacao fresca | R$ {{cpl_novo}} |

---

## 5. Projecao de ROI do Empilhamento

### Custo Comparativo de Leads

| Tipo de Lead | CPL | Volume | Custo Total |
|-------------|-----|--------|-------------|
| Lead novo (midia paga) | R$ {{cpl_novo}} | {{vol_novos}} | R$ {{custo_novos}} |
| Lead reativado (API) | R$ {{cpl_api}} | {{vol_reativados}} | R$ {{custo_reativados}} |
| **Economia** | — | — | **R$ {{economia_total}}** |

### Projecao Web 2 (Conservadora)

| Metrica | Projecao |
|---------|----------|
| Leads base reativados | {{leads_reativados}} |
| Leads novos captados | {{leads_novos_web2}} |
| Total de leads Web 2 | {{total_leads_web2}} |
| Comparecimentos ({{taxa_comp}}%) | {{comparecimentos_web2}} |
| Vendas ({{taxa_conv}}%) | {{vendas_web2}} |
| Receita bruta | R$ {{receita_web2}} |
| Investimento total | R$ {{investimento_web2}} |
| ROAS projetado | {{roas_web2}}x |
| Margem | {{margem_web2}}% |

---

## 6. Esteira de Produtos

| Ordem | Produto | Ticket | Formato de Venda | Status |
|-------|---------|--------|-----------------|--------|
| 1 | {{esteira_1_produto}} | R$ {{esteira_1_ticket}} | {{esteira_1_formato}} | {{esteira_1_status}} |
| 2 | {{esteira_2_produto}} | R$ {{esteira_2_ticket}} | {{esteira_2_formato}} | {{esteira_2_status}} |
| 3 | {{esteira_3_produto}} | R$ {{esteira_3_ticket}} | {{esteira_3_formato}} | {{esteira_3_status}} |

> **Referencia:** Secao 7.5 — Esteira de Produtos

---

## 7. Timeline de Implementacao

| Fase | Acao | Prazo | Agente |
|------|------|-------|--------|
| 1 | {{fase_1_acao}} | {{fase_1_prazo}} | {{fase_1_agente}} |
| 2 | {{fase_2_acao}} | {{fase_2_prazo}} | {{fase_2_agente}} |
| 3 | {{fase_3_acao}} | {{fase_3_prazo}} | {{fase_3_agente}} |
| 4 | {{fase_4_acao}} | {{fase_4_prazo}} | {{fase_4_agente}} |

---

## 8. Proximos Passos

| # | Acao | Comando |
|---|------|---------|
| 1 | Criar canvases para produto do Web 2 | `@webinar-strategist *canvas-produto` |
| 2 | {{prox_passo_2}} | {{prox_comando_2}} |
| 3 | {{prox_passo_3}} | {{prox_comando_3}} |

---

*Gerado por @webinar-analyst (Lens) — Estrategia baseada na Secao 7.3 (Empilhamento) + 7.5 (Esteira de Produtos)*
