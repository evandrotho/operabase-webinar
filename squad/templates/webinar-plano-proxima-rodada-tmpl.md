# Plano da Proxima Rodada — Rodada {{rodada_proximo}} (baseado na Rodada {{rodada_anterior}})

> **Gerado por:** @webinar-analyst (Lens)
> **Data:** {{data_geracao}}
> **Base:** diagnostico-funil.md + orcado-vs-realizado.md

---

## 1. Resumo da Rodada Anterior

| Metrica | Rodada {{rodada_anterior}} | Benchmark |
|---------|--------------------------|-----------|
| Leads | {{leads_anterior}} | — |
| Comparecimentos | {{comparecimentos_anterior}} ({{taxa_comp_anterior}}%) | 25% |
| Vendas | {{vendas_anterior}} ({{taxa_conv_anterior}}%) | 3% |
| Faturamento | R$ {{faturamento_anterior}} | R$ {{faturamento_meta}} |
| ROAS | {{roas_anterior}}x | > 2x |
| Gargalo Principal | {{gargalo_anterior}} | — |

---

## 2. Canvases a Revisar

> **IMPORTANTE:** Estes canvases devem ser revisados pelo @webinar-strategist ANTES de iniciar a proxima rodada.

| # | Canvas | O que Revisar | Por que | Prioridade |
|---|--------|--------------|---------|------------|
{{#each canvases_revisar}}
| {{this.numero}} | {{this.canvas}} | {{this.revisao}} | {{this.justificativa}} | {{this.prioridade}} |
{{/each}}

**Como revisar:**
1. Ativar `@webinar-strategist`
2. Executar o comando correspondente ao canvas (ex: `*canvas-webinar`, `*orcamento`)
3. O strategist vai carregar o canvas atual e perguntar o que ajustar com base nos dados reais

---

## 3. Otimizacoes Priorizadas

### OBRIGATORIAS (corrigir antes da proxima rodada)

| # | Otimizacao | Etapa do Funil | O que Mudar | Quem Executa | Impacto Esperado |
|---|-----------|---------------|------------|-------------|-----------------|
{{#each otimizacoes_obrigatorias}}
| {{this.numero}} | {{this.nome}} | {{this.etapa}} | {{this.acao}} | {{this.agente}} | {{this.impacto}} |
{{/each}}

### RECOMENDADAS (melhorias significativas)

| # | Otimizacao | Etapa do Funil | O que Mudar | Quem Executa | Impacto Esperado |
|---|-----------|---------------|------------|-------------|-----------------|
{{#each otimizacoes_recomendadas}}
| {{this.numero}} | {{this.nome}} | {{this.etapa}} | {{this.acao}} | {{this.agente}} | {{this.impacto}} |
{{/each}}

### OPCIONAIS (micro-otimizacoes)

| # | Otimizacao | Etapa do Funil | O que Mudar | Quem Executa |
|---|-----------|---------------|------------|-------------|
{{#each otimizacoes_opcionais}}
| {{this.numero}} | {{this.nome}} | {{this.etapa}} | {{this.acao}} | {{this.agente}} |
{{/each}}

---

## 4. Novas Metas para Rodada {{rodada_proximo}}

| Metrica | Rodada {{rodada_anterior}} (real) | Meta Rodada {{rodada_proximo}} | Variacao | Justificativa |
|---------|----------------------------------|-------------------------------|----------|---------------|
| CPL | R$ {{cpl_anterior}} | R$ {{cpl_meta}} | {{cpl_var}}% | {{cpl_justificativa}} |
| Taxa de Captura | {{captura_anterior}}% | {{captura_meta}}% | {{captura_var}}% | {{captura_justificativa}} |
| Taxa de Comparecimento | {{comp_anterior}}% | {{comp_meta}}% | {{comp_var}}% | {{comp_justificativa}} |
| Taxa de Conversao | {{conv_anterior}}% | {{conv_meta}}% | {{conv_var}}% | {{conv_justificativa}} |
| ROAS | {{roas_anterior}}x | {{roas_meta}}x | {{roas_var}}% | {{roas_justificativa}} |
| Faturamento | R$ {{fat_anterior}} | R$ {{fat_meta}} | {{fat_var}}% | {{fat_justificativa}} |

---

## 5. Sequencia de Acao

> Ordem recomendada para preparar a proxima rodada:

| Passo | Acao | Agente | Comando | Dependencia |
|-------|------|--------|---------|-------------|
| 1 | {{passo_1_acao}} | {{passo_1_agente}} | `{{passo_1_comando}}` | — |
| 2 | {{passo_2_acao}} | {{passo_2_agente}} | `{{passo_2_comando}}` | Passo 1 |
| 3 | {{passo_3_acao}} | {{passo_3_agente}} | `{{passo_3_comando}}` | Passo 2 |
| 4 | {{passo_4_acao}} | {{passo_4_agente}} | `{{passo_4_comando}}` | Passo 3 |
| 5 | {{passo_5_acao}} | {{passo_5_agente}} | `{{passo_5_comando}}` | Passo 4 |

---

## 6. Restricoes e Observacoes

{{restricoes_observacoes}}

---

## 7. Consideracoes para Estrategia Avancada

{{#if considerar_empilhamento}}
### Empilhamento
{{empilhamento_nota}}
> Para planejar: `@webinar-analyst *empilhamento`
{{/if}}

{{#if considerar_perpetuo}}
### Modo Perpetuo
{{perpetuo_nota}}
> Para planejar: `@webinar-analyst *perpetuo`
{{/if}}

{{#if considerar_frontend_backend}}
### Modelo Front-end + Back-end
{{frontend_backend_nota}}
> Para planejar: `@webinar-analyst *frontend-backend`
{{/if}}

---

*Gerado por @webinar-analyst (Lens) — Plano baseado em dados reais da Rodada {{rodada_anterior}}*
