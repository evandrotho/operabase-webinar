# Checklist Pre-Lancamento: {{nome_webinario}}

**Template ID:** webinar-checklist-lancamento-template-v1
**Purpose:** Template para checklist completo pre-lancamento do webinario
**Usado por:** @webinar-operator (Atlas) -- comando *checklist

---

## Template Variables

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `{{nome_webinario}}` | string | Nome do webinario | "Webinario Infalivel" |
| `{{rodada}}` | number | Numero da rodada | 1 |
| `{{data_geracao}}` | string | Data da verificacao | "2026-03-10" |
| `{{data_lancamento}}` | string | Data do lancamento | "2026-03-13" |
| `{{score}}` | string | Score geral | "85% (QUASE PRONTO)" |
| `{{total_verificados}}` | number | Itens verificados | 34 |
| `{{total_itens}}` | number | Total de itens | 40 |

---

## Document Template

```markdown
# Checklist Pre-Lancamento

> **Rodada:** {{rodada}}
> **Webinario:** {{nome_webinario}}
> **Data da verificacao:** {{data_geracao}}
> **Data prevista de lancamento:** {{data_lancamento}}
> **Agente:** @webinar-operator (Atlas)

---

## Score Geral

**{{score_percentual}}% verificado** — {{veredicto}}

| Categoria | Verificados | Total | % |
|-----------|-------------|-------|---|
| Planejamento | {{plan_ok}} | {{plan_total}} | {{plan_pct}}% |
| Conteudo | {{cont_ok}} | {{cont_total}} | {{cont_pct}}% |
| Ferramentas | {{ferr_ok}} | {{ferr_total}} | {{ferr_pct}}% |
| Timeline/Funil | {{time_ok}} | {{time_total}} | {{time_pct}}% |
| Criticos | {{crit_ok}} | {{crit_total}} | {{crit_pct}}% |
| **TOTAL** | **{{total_verificados}}** | **{{total_itens}}** | **{{score_percentual}}%** |

### Veredicto

{{#if pronto}}
**PRONTO PARA LANCAR** — Todos os itens criticos verificados. Campanha pode iniciar conforme planejado.
{{/if}}

{{#if quase_pronto}}
**QUASE PRONTO** — Itens nao-criticos pendentes. Revise a lista abaixo e resolva antes do lancamento.
{{/if}}

{{#if precisa_atencao}}
**PRECISA DE ATENCAO** — Itens criticos pendentes. NAO lance antes de resolver os itens marcados como criticos.
{{/if}}

{{#if nao_pronto}}
**NAO PRONTO** — Muitos itens pendentes. Volte ao fluxo de preparacao e complete as etapas necessarias.
{{/if}}

---

## 1. Planejamento

### Canvases e Estrategia

- [{{check_canvas_cliente}}] **Canvas do Cliente Ideal** (`canvas-cliente-ideal.md`)
  - Criticidade: Media
  - {{nota_canvas_cliente}}

- [{{check_canvas_produto}}] **Canvas do Produto** (`canvas-produto.md`)
  - Criticidade: Alta
  - {{nota_canvas_produto}}

- [{{check_canvas_webinar}}] **Canvas do Webinario** (`canvas-webinar.md`)
  - Criticidade: Media
  - {{nota_canvas_webinar}}

- [{{check_avatar}}] **Avatar Blueprint** (`avatar-blueprint.md`)
  - Criticidade: Alta
  - {{nota_avatar}}

- [{{check_orcamento}}] **Orcamento e Meta** (`orcamento-meta.md`)
  - Criticidade: Baixa (recomendado)
  - {{nota_orcamento}}

---

## 2. Conteudo

### Roteiro

- [{{check_abertura}}] **Roteiro - Abertura** (`roteiro-abertura.md`)
  - Criticidade: Critica
  - {{nota_abertura}}

- [{{check_empatia}}] **Roteiro - Empatia** (`roteiro-empatia.md`)
  - Criticidade: Critica
  - {{nota_empatia}}

- [{{check_conteudo}}] **Roteiro - Conteudo** (`roteiro-conteudo.md`)
  - Criticidade: Critica
  - {{nota_conteudo}}

- [{{check_pitch}}] **Roteiro - Pitch** (`roteiro-pitch.md`)
  - Criticidade: Critica
  - {{nota_pitch}}

- [{{check_roteiro_completo}}] **Roteiro Completo** (`roteiro-completo.md`)
  - Criticidade: Critica
  - {{nota_roteiro_completo}}

### Mensagens e Copy

- [{{check_mensagens}}] **Mensagens WhatsApp** (`mensagens-whatsapp.md`) — 41+ templates
  - Criticidade: Critica
  - {{nota_mensagens}}

- [{{check_copy_captura}}] **Copy Pagina de Captura** (`copy-pagina-captura.md`)
  - Criticidade: Alta
  - {{nota_copy_captura}}

- [{{check_copy_replay}}] **Copy Pagina de Replay** (`copy-pagina-replay.md`)
  - Criticidade: Media
  - {{nota_copy_replay}}

- [{{check_copy_fechamento}}] **Copy Pagina de Fechamento** (`copy-pagina-fechamento.md`)
  - Criticidade: Media
  - {{nota_copy_fechamento}}

---

## 3. Ferramentas

### EverWebinar

- [{{check_ew_video}}] Video carregado e testado
  - Criticidade: Critica
- [{{check_ew_agendamento}}] Agendamento configurado ({{tipo_agendamento}})
  - Criticidade: Critica
- [{{check_ew_chat}}] Chat simulado com mensagens programadas
  - Criticidade: Alta
- [{{check_ew_eventos}}] Eventos na timeline sincronizados com roteiro
  - Criticidade: Alta
- [{{check_ew_replay}}] Replay configurado
  - Criticidade: Media
- [{{check_ew_registro}}] Pagina de registro conectada
  - Criticidade: Critica

### SendFlow

- [{{check_sf_grupos}}] Grupos criados (Fase Pre, Pos, Conteudo)
  - Criticidade: Critica
- [{{check_sf_mensagens}}] Mensagens carregadas e agendadas
  - Criticidade: Critica
- [{{check_sf_triggers}}] Triggers configurados
  - Criticidade: Alta
- [{{check_sf_deeplinks}}] Deep links com Pixel funcionando
  - Criticidade: Media
- [{{check_sf_teste}}] Teste de envio realizado
  - Criticidade: Alta

### Pagamento

- [{{check_pg_produto}}] Produto cadastrado na plataforma
  - Criticidade: Critica
- [{{check_pg_checkout}}] Checkout funcionando
  - Criticidade: Critica
- [{{check_pg_webhooks}}] Webhooks configurados e testados
  - Criticidade: Alta
- [{{check_pg_bump}}] Order bump/upsell/downsell ativos
  - Criticidade: Baixa
- [{{check_pg_teste}}] Teste de compra em sandbox realizado
  - Criticidade: Alta

### Facebook Pixel

- [{{check_px_instalado}}] Pixel instalado em todas as paginas
  - Criticidade: Alta
- [{{check_px_eventos}}] Eventos disparando corretamente
  - Criticidade: Alta
- [{{check_px_deeplinks}}] Deep links com UTMs configurados
  - Criticidade: Media
- [{{check_px_audiencias}}] Audiencias criadas
  - Criticidade: Media

---

## 4. Timeline e Funil

- [{{check_timeline}}] **Timeline** (`timeline-campanha.md`) — cronograma com datas reais
  - Criticidade: Alta
  - {{nota_timeline}}

- [{{check_funil}}] **Funil** (`funil-7-etapas.md`) — todas as etapas mapeadas
  - Criticidade: Media
  - {{nota_funil}}

---

## 5. Verificacoes Criticas

- [{{check_teste_e2e}}] **Teste end-to-end do funil**
  - Percorreu todo o caminho: anuncio -> captura -> registro -> mensagem -> webinario -> checkout -> compra
  - Criticidade: Critica

- [{{check_links}}] **Todos os links testados**
  - Captura, webinario, replay, checkout, fechamento
  - Criticidade: Critica

- [{{check_variaveis}}] **Variaveis dinamicas substituidas**
  - {{nome_expert}}, {{data_webinario}}, {{link}}, {{produto}}, {{preco}}, {{bonus}}
  - Criticidade: Critica

- [{{check_backup}}] **Plano de contingencia**
  - Video backup? Checkout alternativo? Responsavel de monitoramento?
  - Criticidade: Alta

---

## Itens Pendentes (Priorizados)

{{#if itens_pendentes}}
| # | Item | Criticidade | Acao | Comando |
|---|------|-------------|------|---------|
{{#each itens_pendentes}}
| {{this.numero}} | {{this.item}} | {{this.criticidade}} | {{this.acao}} | `{{this.comando}}` |
{{/each}}
{{else}}
Nenhum item pendente. Campanha pronta para lancamento!
{{/if}}

---

## Historico de Verificacoes

| Data | Score | Veredicto | Notas |
|------|-------|-----------|-------|
{{#each historico}}
| {{this.data}} | {{this.score}}% | {{this.veredicto}} | {{this.notas}} |
{{/each}}

---

> Checklist gerado por @webinar-operator (Atlas)
> Metodologia: Webinario Infalivel (Taioba) + Perfect Webinar (Brunson)
```

---

## Criticality Levels

| Level | Description | Impact on Veredicto |
|-------|-------------|---------------------|
| **Critica** | Sem isso, a campanha NAO funciona | Bloqueia "PRONTO" |
| **Alta** | Muito importante, mas tem workaround | Gera "QUASE PRONTO" |
| **Media** | Melhora resultado, mas nao bloqueia | Nota no relatorio |
| **Baixa** | Nice-to-have, recomendado | Nao impacta veredicto |

## Score Calculation

```yaml
score_rules:
  pronto: ">= 90% E zero criticos pendentes"
  quase_pronto: "75-89% OU criticos OK mas alta pendente"
  precisa_atencao: "60-74% OU criticos pendentes"
  nao_pronto: "< 60%"
```

---

## Usage Notes

1. **Interactive Verification:** Agent asks each item one-by-one; user confirms or flags
2. **Auto-detection:** Check file existence in `docs/webinar/rodada-{N}/` for auto-marking
3. **Re-run:** Checklist can be re-run multiple times; each run adds to historico
4. **Priority Sort:** Pending items sorted by criticality (Critica > Alta > Media > Baixa)

---

**Template Version:** 1.0.0
**Created:** 2026-03-05
**Part of:** Squad Webinario (@webinar-operator)
