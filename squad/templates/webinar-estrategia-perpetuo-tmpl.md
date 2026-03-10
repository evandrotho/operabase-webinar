# Estrategia de Webinario Perpetuo (Evergreen)

> **Gerado por:** @webinar-analyst (Lens)
> **Data:** {{data_geracao}}
> **Base:** relatorio-kpis.md + roteiro-completo.md

---

## 1. Conceito

O **webinario perpetuo (evergreen)** transforma um webinario ao vivo validado em uma maquina de vendas automatizada que roda continuamente. Em vez de depender de lancamentos pontuais, o funil opera 24/7 com chat simulado, agendamento recorrente e automacao completa.

> **Referencia:** Secao 7.1 — Webinario Perpetuo (Evergreen)

---

## 2. Avaliacao de Prontidao

| Criterio | Status | Detalhe |
|----------|--------|---------|
| ROAS positivo validado | {{prontidao_roas}} | ROAS atual: {{roas_atual}}x |
| Roteiro validado (conversao >= 2%) | {{prontidao_roteiro}} | Conversao atual: {{conversao_atual}}% |
| Funil operacional testado | {{prontidao_funil}} | 7 etapas configuradas |
| Gravacao de alta qualidade | {{prontidao_gravacao}} | {{gravacao_detalhe}} |

**Veredicto:** {{veredicto_prontidao}} <!-- PRONTO | QUASE PRONTO | NAO RECOMENDADO -->

---

## 3. Configuracao do Funil Evergreen

### 3.1 EverWebinar

| Configuracao | Valor |
|-------------|-------|
| Modo | Perpetuo / Recorrente |
| Frequencia | {{frequencia}} |
| Agendamento | {{tipo_agendamento}} |
| Chat Simulado | {{chat_simulado}} |
| One-Click Registration | Ativo |
| Replay | Disponivel por {{replay_duracao}} apos sessao |

### 3.2 SendFlow (Automacao WhatsApp)

| Configuracao | Valor |
|-------------|-------|
| Modo | Automacao continua (trigger por data de inscricao) |
| Variaveis | {{data_webinario}} = dinamica por lead |
| Fases | Pre-webinario (relativa) -> Pos-webinario (relativa) -> Fechamento (relativa) |
| Deadline | Relativo: {{deadline_horas}}h apos sessao do lead |

### 3.3 Pagamento

| Configuracao | Valor |
|-------------|-------|
| Webhooks | Ativos 24/7 |
| Deadline | Relativo por comprador |
| Checkout | Sempre disponivel dentro do prazo |

### 3.4 Ads

| Configuracao | Valor |
|-------------|-------|
| Modo | Campanha continua (sem data inicio/fim) |
| Budget diario | R$ {{budget_diario}} |
| Budget mensal | R$ {{budget_mensal}} |
| Otimizacao | Lookalike com base de compradores |

---

## 4. Projecao Mensal

### Funil Semanal

| Metrica | Projecao por Semana |
|---------|-------------------|
| Investimento semanal | R$ {{invest_semanal}} |
| Leads captados | {{leads_semanal}} |
| Comparecimentos ({{taxa_comp}}%) | {{comparecimentos_semanal}} |
| Vendas ({{taxa_conv}}%) | {{vendas_semanal}} |
| Receita semanal | R$ {{receita_semanal}} |

### Consolidacao Mensal

| Metrica | Projecao Mensal |
|---------|----------------|
| Investimento | R$ {{invest_mensal}} |
| Leads | {{leads_mensal}} |
| Vendas | {{vendas_mensal}} |
| Receita Bruta | R$ {{receita_mensal}} |
| ROAS Mensal | {{roas_mensal}}x |
| Margem Liquida | R$ {{margem_mensal}} ({{margem_pct}}%) |

### Projecao Trimestral

| Metrica | Mes 1 | Mes 2 | Mes 3 | Acumulado |
|---------|-------|-------|-------|-----------|
| Investimento | R$ {{m1_invest}} | R$ {{m2_invest}} | R$ {{m3_invest}} | R$ {{total_invest}} |
| Receita | R$ {{m1_receita}} | R$ {{m2_receita}} | R$ {{m3_receita}} | R$ {{total_receita}} |
| Lucro | R$ {{m1_lucro}} | R$ {{m2_lucro}} | R$ {{m3_lucro}} | R$ {{total_lucro}} |

---

## 5. Mudancas Necessarias (Lancamento -> Perpetuo)

### EverWebinar
{{#each mudancas_everwebinar}}
- [ ] {{this}}
{{/each}}

### SendFlow
{{#each mudancas_sendflow}}
- [ ] {{this}}
{{/each}}

### Pagamento
{{#each mudancas_pagamento}}
- [ ] {{this}}
{{/each}}

### Ads
{{#each mudancas_ads}}
- [ ] {{this}}
{{/each}}

---

## 6. Metricas de Monitoramento

| Metrica | Frequencia de Checagem | Alerta Se |
|---------|----------------------|-----------|
| CPL | Diaria | > R$ {{cpl_alerta}} |
| Taxa de Captura | Semanal | < {{captura_alerta}}% |
| Comparecimento | Semanal | < {{comp_alerta}}% |
| Conversao | Semanal | < {{conv_alerta}}% |
| ROAS | Semanal | < {{roas_alerta}}x |

---

## 7. Riscos e Mitigacoes

| Risco | Probabilidade | Mitigacao |
|-------|-------------|-----------|
| Fadiga do criativo (ads) | Alta | Rotacionar criativos a cada 2-3 semanas |
| Queda de conversao ao longo do tempo | Media | Monitorar KPIs semanais, ajustar roteiro se necessario |
| Concorrencia copiando | Media | Atualizar conteudo trimestralmente |
| Problemas tecnicos (EverWebinar) | Baixa | Monitorar sessoes, ter backup do video |

---

## 8. Proximos Passos

| # | Acao | Agente | Comando |
|---|------|--------|---------|
| 1 | Reconfigurar EverWebinar para modo perpetuo | @webinar-operator | `*setup-everwebinar` |
| 2 | Adaptar mensagens WhatsApp para datas dinamicas | @webinar-creator | `*mensagens` |
| 3 | Configurar campanha continua de ads | @webinar-operator | `*timeline` |
| 4 | Monitorar KPIs semanais | @webinar-analyst | `*kpis` (semanal) |

---

*Gerado por @webinar-analyst (Lens) — Estrategia baseada na Secao 7.1 (Webinario Perpetuo/Evergreen)*
