# Timeline da Campanha: {{nome_webinario}}

**Template ID:** webinar-timeline-campanha-template-v1
**Purpose:** Template para cronograma completo dia-a-dia da campanha de webinario
**Usado por:** @webinar-operator (Atlas) -- comando *timeline

---

## Template Variables

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `{{nome_webinario}}` | string | Nome do webinario | "Webinario Infalivel" |
| `{{rodada}}` | number | Numero da rodada | 1 |
| `{{data_geracao}}` | string | Data de geracao | "2026-03-10" |
| `{{data_webinario}}` | string | Data do webinario (D-0) | "2026-03-20" |
| `{{data_inicio_captacao}}` | string | Inicio da captacao | "2026-03-13" |
| `{{data_fechamento}}` | string | Fechamento do carrinho | "2026-03-23" |
| `{{data_fim_impulsionamento}}` | string | Fim do impulsionamento | "2026-03-26" |
| `{{total_dias}}` | number | Total de dias da campanha | 14 |
| `{{total_mensagens}}` | number | Total de mensagens agendadas | 41 |

---

## Document Template

```markdown
# Timeline da Campanha

> **Rodada:** {{rodada}}
> **Webinario:** {{nome_webinario}}
> **Data do Webinario (D-0):** {{data_webinario}}
> **Periodo:** {{data_inicio_captacao}} a {{data_fim_impulsionamento}} ({{total_dias}} dias)
> **Total de mensagens:** {{total_mensagens}}
> **Gerado em:** {{data_geracao}}
> **Agente:** @webinar-operator (Atlas)

---

## Resumo da Campanha

| Fase | Periodo | Dias | Pilares | Canais |
|------|---------|------|---------|--------|
| Captacao | {{data_inicio_captacao}} a D-3 | {{dias_captacao}} | Atracao | Ads, Organico |
| Nutricao | {{data_inicio_nutricao}} a D-1 | {{dias_nutricao}} | Engajamento | WhatsApp |
| Antecipacao | D-1 a D-0 | 2 | Compromisso | WhatsApp |
| Abertura | D-0 | 1 | Persuasao | EverWebinar, Checkout |
| Ampliacao | D+1 a D+{{dias_ampliacao}} | {{dias_ampliacao}} | Urgencia | WhatsApp, Email, Replay |
| Fechamento | D+{{dias_ampliacao+1}} a D+{{dias_fechamento}} | {{dias_fechamento_duracao}} | Escassez | WhatsApp, Email, Retargeting |
| Impulsionamento | D+{{dias_fechamento+1}} a D+{{dias_total}} | {{dias_impulsionamento}} | Persuasao | WhatsApp |

---

## Marcos e Checkpoints

| Marco | Data | Hora | Acao Necessaria |
|-------|------|------|-----------------|
| Inicio da captacao | {{data_inicio_captacao}} | 00:00 | Ativar anuncios + publicar conteudo |
| Meta de leads | {{data_meta_leads}} | -- | Verificar se meta de leads foi atingida |
| D-1: Verificacao final | {{data_d_menos_1}} | 09:00 | Rodar *checklist, testar tudo |
| D-0: Webinario | {{data_webinario}} | {{hora_webinario}} | Monitorar EverWebinar e chat |
| Abertura do carrinho | {{data_webinario}} | {{hora_abertura_carrinho}} | Verificar checkout ativo |
| Pico 1 de vendas | {{data_webinario}} | {{hora_pico_1}} | Monitorar conversoes |
| Disponibilizar replay | D+1 | {{hora_replay}} | Ativar pagina de replay |
| Pico 2 de vendas | {{data_fechamento}} | -- | Monitorar pico de fechamento |
| Fechamento do carrinho | {{data_fechamento}} | {{hora_fechamento}} | Desativar checkout |
| Inicio impulsionamento | D+{{dias_fechamento+1}} | 09:00 | Ativar downsell (se aplicavel) |

---

## Cronograma Detalhado

### Fase 1: Captacao ({{data_inicio_captacao}} a D-3)

| Dia | Data | Hora | Acao | Canal | Pilar | Notas |
|-----|------|------|------|-------|-------|-------|
{{#each dias_captacao_detalhes}}
| {{this.dia_relativo}} | {{this.data}} | {{this.hora}} | {{this.acao}} | {{this.canal}} | Atracao | {{this.notas}} |
{{/each}}

### Fase 2: Nutricao (D-{{dias_nutricao}} a D-1)

| Dia | Data | Hora | Acao/Mensagem | Canal | Pilar | Ref. Mensagem |
|-----|------|------|---------------|-------|-------|---------------|
{{#each dias_nutricao_detalhes}}
| {{this.dia_relativo}} | {{this.data}} | {{this.hora}} | {{this.acao}} | {{this.canal}} | Engajamento | {{this.ref_mensagem}} |
{{/each}}

### Fase 3: Antecipacao (D-1 e D-0)

| Dia | Data | Hora | Acao/Mensagem | Canal | Pilar | Ref. Mensagem |
|-----|------|------|---------------|-------|-------|---------------|
{{#each dias_antecipacao_detalhes}}
| {{this.dia_relativo}} | {{this.data}} | {{this.hora}} | {{this.acao}} | {{this.canal}} | Compromisso | {{this.ref_mensagem}} |
{{/each}}

### Fase 4: Abertura do Carrinho (D-0)

| Dia | Data | Hora | Acao | Canal | Pilar | Notas |
|-----|------|------|------|-------|-------|-------|
| D-0 | {{data_webinario}} | {{hora_webinario}} | Sessao do webinario | EverWebinar | Persuasao | Monitorar chat e presenca |
| D-0 | {{data_webinario}} | {{hora_abertura_carrinho}} | Abrir checkout | Checkout | Persuasao | Verificar webhooks |
| D-0 | {{data_webinario}} | {{hora_pos_webinario}} | Mensagem pos-webinario | WhatsApp | Persuasao | Link do checkout |

### Fase 5: Ampliacao do Impacto (D+1 a D+{{dias_ampliacao}})

| Dia | Data | Hora | Acao/Mensagem | Canal | Pilar | Ref. Mensagem |
|-----|------|------|---------------|-------|-------|---------------|
{{#each dias_ampliacao_detalhes}}
| {{this.dia_relativo}} | {{this.data}} | {{this.hora}} | {{this.acao}} | {{this.canal}} | Urgencia | {{this.ref_mensagem}} |
{{/each}}

### Fase 6: Fechamento do Carrinho (D+{{dias_ampliacao+1}} a D+{{dias_fechamento}})

| Dia | Data | Hora | Acao/Mensagem | Canal | Pilar | Ref. Mensagem |
|-----|------|------|---------------|-------|-------|---------------|
{{#each dias_fechamento_detalhes}}
| {{this.dia_relativo}} | {{this.data}} | {{this.hora}} | {{this.acao}} | {{this.canal}} | Escassez | {{this.ref_mensagem}} |
{{/each}}

### Fase 7: Impulsionamento do Lucro (D+{{dias_fechamento+1}} a D+{{dias_total}})

| Dia | Data | Hora | Acao/Mensagem | Canal | Pilar | Ref. Mensagem |
|-----|------|------|---------------|-------|-------|---------------|
{{#each dias_impulsionamento_detalhes}}
| {{this.dia_relativo}} | {{this.data}} | {{this.hora}} | {{this.acao}} | {{this.canal}} | Persuasao | {{this.ref_mensagem}} |
{{/each}}

---

## Distribuicao por Canal

| Canal | Mensagens | Acoes | Total |
|-------|-----------|-------|-------|
| WhatsApp (SendFlow) | {{total_whatsapp}} | -- | {{total_whatsapp}} |
| Email | {{total_email}} | -- | {{total_email}} |
| Facebook Ads | -- | {{total_ads}} | {{total_ads}} |
| EverWebinar | -- | {{total_everwebinar}} | {{total_everwebinar}} |
| Checkout | -- | {{total_checkout}} | {{total_checkout}} |

## Distribuicao por Pilar da Espiral

| Pilar | Acoes | Periodo |
|-------|-------|---------|
| Atracao | {{total_atracao}} | Captacao |
| Engajamento | {{total_engajamento}} | Nutricao |
| Compromisso | {{total_compromisso}} | Antecipacao |
| Persuasao | {{total_persuasao}} | Abertura + Impulsionamento |
| Escassez | {{total_escassez}} | Fechamento |

---

## Notas Operacionais

{{notas_operacionais}}

---

> Timeline gerada por @webinar-operator (Atlas)
> Metodologia: Webinario Infalivel (Taioba) + Perfect Webinar (Brunson)
```

---

## Usage Notes

1. **Date Calculation:** D-0 is the webinar date; all other dates are relative
2. **Message Mapping:** Each message from `mensagens-whatsapp.md` maps to a specific row in the timeline
3. **Multiple Messages Per Day:** D-0 can have 7+ messages; use separate rows for each
4. **Weekend Consideration:** Flag weekends differently (higher engagement on weekends for B2C)
5. **Time Zones:** Always use America/Sao_Paulo for Brazilian campaigns

---

**Template Version:** 1.0.0
**Created:** 2026-03-05
**Part of:** Squad Webinario (@webinar-operator)
