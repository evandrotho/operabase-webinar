# Diagnostico de Funil — Rodada {{rodada_numero}}

> **Gerado por:** @webinar-analyst (Lens)
> **Data:** {{data_geracao}}
> **Base:** relatorio-kpis.md + funil-7-etapas.md

---

## 1. Resumo do Diagnostico

**Gargalo Principal:** {{gargalo_principal_etapa}} — {{gargalo_principal_descricao}}

**Severidade:** {{severidade_geral}} <!-- CRITICO | ATENCAO | LEVE | SAUDAVEL -->

**Impacto Estimado:** Se corrigido, estima-se {{impacto_estimado}} em receita adicional.

---

## 2. Mapa do Funil — Visao por Etapa

```
ETAPA 1          ETAPA 2          ETAPA 3          ETAPA 4          ETAPA 5          ETAPA 6          ETAPA 7
Captacao    -->   Nutricao   -->   Antecipacao -->   Abertura   -->   Ampliacao  -->   Fechamento -->   Impulsionamento
{{leads}}         {{engajados}}    {{comparec}}      {{vend_ab}}      {{vend_rep}}     {{vend_fech}}    {{downsell}}
{{cap_status}}    {{nut_status}}   {{ant_status}}    {{abe_status}}   {{amp_status}}   {{fec_status}}   {{imp_status}}
```

> Legenda: OK | ATENCAO | GARGALO

---

## 3. Diagnostico por Etapa

### Etapa 1: Captacao

| Metrica | Valor | Benchmark | Status |
|---------|-------|-----------|--------|
| CPL | R$ {{cpl}} | R$ {{cpl_benchmark}} | {{cpl_status}} |
| Taxa de Captura | {{taxa_captura}}% | 40% | {{captura_status}} |
| Total de Leads | {{total_leads}} | {{leads_meta}} | {{leads_status}} |

**Diagnostico:** {{diag_etapa_1}}

**Acao Corretiva:** {{acao_etapa_1}}

> **Referencia:** {{ref_etapa_1}}

---

### Etapa 2: Nutricao

| Metrica | Valor | Benchmark | Status |
|---------|-------|-----------|--------|
| Engajamento pre-webinario | {{engajamento}}% | — | {{engajamento_status}} |

**Diagnostico:** {{diag_etapa_2}}

**Acao Corretiva:** {{acao_etapa_2}}

> **Referencia:** {{ref_etapa_2}}

---

### Etapa 3: Antecipacao

| Metrica | Valor | Benchmark | Status |
|---------|-------|-----------|--------|
| Taxa de Comparecimento | {{taxa_comparecimento}}% | 25% | {{comparecimento_status}} |

**Diagnostico:** {{diag_etapa_3}}

**Acao Corretiva:** {{acao_etapa_3}}

> **Referencia:** {{ref_etapa_3}}

---

### Etapa 4: Abertura do Carrinho

| Metrica | Valor | Benchmark | Status |
|---------|-------|-----------|--------|
| Vendas na Abertura | {{vendas_abertura}} | — | {{abertura_status}} |
| Conversao Vendas/Comparecimentos | {{conv_comparecimentos}}% | 12% | {{conv_comp_status}} |

**Diagnostico:** {{diag_etapa_4}}

**Acao Corretiva:** {{acao_etapa_4}}

> **Referencia:** {{ref_etapa_4}}

---

### Etapa 5: Ampliacao do Impacto

| Metrica | Valor | Benchmark | Status |
|---------|-------|-----------|--------|
| Vendas no Replay | {{vendas_replay}} | — | {{replay_status}} |

**Diagnostico:** {{diag_etapa_5}}

**Acao Corretiva:** {{acao_etapa_5}}

> **Referencia:** {{ref_etapa_5}}

---

### Etapa 6: Fechamento do Carrinho

| Metrica | Valor | Benchmark | Status |
|---------|-------|-----------|--------|
| Vendas no Fechamento | {{vendas_fechamento}} | — | {{fechamento_status}} |
| Relacao Pico2/Pico1 | {{relacao_picos}} | >= 0.8 | {{picos_status}} |

**Diagnostico:** {{diag_etapa_6}}

**Acao Corretiva:** {{acao_etapa_6}}

> **Referencia:** {{ref_etapa_6}}

---

### Etapa 7: Impulsionamento do Lucro

| Metrica | Valor | Benchmark | Status |
|---------|-------|-----------|--------|
| Downsell | {{downsell_vendas}} vendas / R$ {{downsell_valor}} | — | {{downsell_status}} |
| Order Bump | {{bump_vendas}} vendas / R$ {{bump_valor}} | — | {{bump_status}} |
| Upsell | {{upsell_vendas}} vendas / R$ {{upsell_valor}} | — | {{upsell_status}} |

**Diagnostico:** {{diag_etapa_7}}

**Acao Corretiva:** {{acao_etapa_7}}

> **Referencia:** {{ref_etapa_7}}

---

## 4. Acoes Corretivas Priorizadas

| # | Prioridade | Etapa | Acao | Artefato a Modificar | Agente | Impacto Esperado |
|---|-----------|-------|------|---------------------|--------|-----------------|
| 1 | OBRIGATORIA | {{prio1_etapa}} | {{prio1_acao}} | {{prio1_artefato}} | {{prio1_agente}} | {{prio1_impacto}} |
| 2 | OBRIGATORIA | {{prio2_etapa}} | {{prio2_acao}} | {{prio2_artefato}} | {{prio2_agente}} | {{prio2_impacto}} |
| 3 | RECOMENDADA | {{prio3_etapa}} | {{prio3_acao}} | {{prio3_artefato}} | {{prio3_agente}} | {{prio3_impacto}} |
| 4 | OPCIONAL | {{prio4_etapa}} | {{prio4_acao}} | {{prio4_artefato}} | {{prio4_agente}} | {{prio4_impacto}} |

---

## 5. Contexto Qualitativo do Usuario

{{contexto_qualitativo}}

---

## 6. Proximos Passos

| # | Acao | Comando |
|---|------|---------|
| 1 | {{prox_passo_1}} | {{prox_comando_1}} |
| 2 | {{prox_passo_2}} | {{prox_comando_2}} |
| 3 | {{prox_passo_3}} | {{prox_comando_3}} |

---

*Gerado por @webinar-analyst (Lens) — Diagnostico baseado na Metodologia Fusionada Taioba + Brunson*
