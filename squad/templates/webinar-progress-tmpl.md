# Webinar Progress Template

> Template para o arquivo de progresso geral do projeto de webinário.
> Squad: webinar
> Created: 2026-03-05

---

## Template Variables

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `{{RODADA_ATIVA}}` | number | Yes | Número da rodada ativa (ex: 1, 2, 3) |
| `{{FASE_ATUAL}}` | string | Yes | Fase atual do projeto (Planejar/Construir/Executar/Analisar) |
| `{{DATA_ATUALIZACAO}}` | date | Yes | Data/hora da última atualização |
| `{{PLANEJAMENTO_STATUS}}` | object | No | Status de cada artefato de planejamento |
| `{{CONTEUDO_STATUS}}` | object | No | Status de cada artefato de conteúdo |
| `{{EXECUCAO_STATUS}}` | object | No | Status de cada artefato de execução |
| `{{ANALISE_STATUS}}` | object | No | Status de cada artefato de análise |

---

## Usage

O Maestro (@webinar) cria e atualiza este arquivo em `docs/webinar/progress.md`. Ele é lido pelo comando `*status` e atualizado por todos os comandos de roteamento (`*planejar`, `*construir`, `*executar`, `*analisar`).

---

## Template Content

<!-- BEGIN TEMPLATE -->

# Webinário — Progresso Geral

> Atualizado em: {{DATA_ATUALIZACAO}}
> Rodada Ativa: {{RODADA_ATIVA}}
> Fase Atual: {{FASE_ATUAL}}

---

## Rodada {{RODADA_ATIVA}}

### 📋 Fase 1: Planejar (@webinar-strategist)

| # | Artefato | Status | Arquivo |
|---|----------|--------|---------|
| 1 | Canvas do Cliente Ideal | {{CANVAS_CLIENTE_STATUS}} | `rodada-{{RODADA_ATIVA}}/planejamento/canvas-cliente-ideal.md` |
| 2 | Canvas do Produto | {{CANVAS_PRODUTO_STATUS}} | `rodada-{{RODADA_ATIVA}}/planejamento/canvas-produto.md` |
| 3 | Canvas do Webinário | {{CANVAS_WEBINAR_STATUS}} | `rodada-{{RODADA_ATIVA}}/planejamento/canvas-webinar.md` |
| 4 | Avatar Blueprint | {{AVATAR_STATUS}} | `rodada-{{RODADA_ATIVA}}/planejamento/avatar-blueprint.md` |
| 5 | Orçamento e Meta | {{ORCAMENTO_STATUS}} | `rodada-{{RODADA_ATIVA}}/planejamento/orcamento-meta.md` |
| 6 | Resumo de Planejamento | {{RESUMO_STATUS}} | `rodada-{{RODADA_ATIVA}}/planejamento/planejamento-resumo.md` |

**Progresso:** {{PLANEJAMENTO_COUNT}} de 6 artefatos

---

### 🔨 Fase 2: Construir (@webinar-creator)

| # | Artefato | Status | Arquivo |
|---|----------|--------|---------|
| 1 | Roteiro — Abertura | {{ABERTURA_STATUS}} | `rodada-{{RODADA_ATIVA}}/conteudo/roteiro-abertura.md` |
| 2 | Roteiro — Empatia | {{EMPATIA_STATUS}} | `rodada-{{RODADA_ATIVA}}/conteudo/roteiro-empatia.md` |
| 3 | Roteiro — Conteúdo | {{CONTEUDO_STATUS}} | `rodada-{{RODADA_ATIVA}}/conteudo/roteiro-conteudo.md` |
| 4 | Roteiro — Pitch | {{PITCH_STATUS}} | `rodada-{{RODADA_ATIVA}}/conteudo/roteiro-pitch.md` |
| 5 | Roteiro Completo | {{ROTEIRO_COMPLETO_STATUS}} | `rodada-{{RODADA_ATIVA}}/conteudo/roteiro-completo.md` |
| 6 | Mensagens WhatsApp | {{MENSAGENS_STATUS}} | `rodada-{{RODADA_ATIVA}}/conteudo/mensagens-whatsapp.md` |
| 7 | Copy — Página de Captura | {{COPY_CAPTURA_STATUS}} | `rodada-{{RODADA_ATIVA}}/conteudo/copy-pagina-captura.md` |
| 8 | Copy — Página de Replay | {{COPY_REPLAY_STATUS}} | `rodada-{{RODADA_ATIVA}}/conteudo/copy-pagina-replay.md` |
| 9 | Copy — Página de Fechamento | {{COPY_FECHAMENTO_STATUS}} | `rodada-{{RODADA_ATIVA}}/conteudo/copy-pagina-fechamento.md` |

**Progresso:** {{CONTEUDO_COUNT}} de 9 artefatos

---

### 🚀 Fase 3: Executar (@webinar-operator)

| # | Artefato | Status | Arquivo |
|---|----------|--------|---------|
| 1 | Guia EverWebinar | {{EVERWEBINAR_STATUS}} | `rodada-{{RODADA_ATIVA}}/execucao/guia-everwebinar.md` |
| 2 | Guia SendFlow | {{SENDFLOW_STATUS}} | `rodada-{{RODADA_ATIVA}}/execucao/guia-sendflow.md` |
| 3 | Guia Pagamento | {{PAGAMENTO_STATUS}} | `rodada-{{RODADA_ATIVA}}/execucao/guia-pagamento.md` |
| 4 | Guia Pixel | {{PIXEL_STATUS}} | `rodada-{{RODADA_ATIVA}}/execucao/guia-pixel.md` |
| 5 | Timeline da Campanha | {{TIMELINE_STATUS}} | `rodada-{{RODADA_ATIVA}}/execucao/timeline-campanha.md` |
| 6 | Funil de 7 Etapas | {{FUNIL_STATUS}} | `rodada-{{RODADA_ATIVA}}/execucao/funil-7-etapas.md` |
| 7 | Checklist de Lançamento | {{CHECKLIST_STATUS}} | `rodada-{{RODADA_ATIVA}}/execucao/checklist-lancamento.md` |

**Progresso:** {{EXECUCAO_COUNT}} de 7 artefatos

---

### 📊 Fase 4: Analisar (@webinar-analyst)

| # | Artefato | Status | Arquivo |
|---|----------|--------|---------|
| 1 | Relatório de KPIs | {{KPIS_STATUS}} | `rodada-{{RODADA_ATIVA}}/analise/relatorio-kpis.md` |
| 2 | Diagnóstico do Funil | {{DIAGNOSTICO_STATUS}} | `rodada-{{RODADA_ATIVA}}/analise/diagnostico-funil.md` |
| 3 | Orçado vs. Realizado | {{ORCADO_REAL_STATUS}} | `rodada-{{RODADA_ATIVA}}/analise/orcado-vs-realizado.md` |
| 4 | Plano Próxima Rodada | {{PROXIMA_RODADA_STATUS}} | `rodada-{{RODADA_ATIVA}}/analise/plano-proxima-rodada.md` |

**Progresso:** {{ANALISE_COUNT}} de 4 artefatos

---

### Estratégias Avançadas (cross-rodada)

| # | Artefato | Status | Arquivo |
|---|----------|--------|---------|
| 1 | Estratégia de Empilhamento | {{EMPILHAMENTO_STATUS}} | `estrategias/estrategia-empilhamento.md` |
| 2 | Estratégia Perpétuo | {{PERPETUO_STATUS}} | `estrategias/estrategia-perpetuo.md` |

---

## Resumo Geral

| Fase | Artefatos | Progresso |
|------|-----------|-----------|
| Planejar | {{PLANEJAMENTO_COUNT}}/6 | {{PLANEJAMENTO_PERCENT}}% |
| Construir | {{CONTEUDO_COUNT}}/9 | {{CONTEUDO_PERCENT}}% |
| Executar | {{EXECUCAO_COUNT}}/7 | {{EXECUCAO_PERCENT}}% |
| Analisar | {{ANALISE_COUNT}}/4 | {{ANALISE_PERCENT}}% |
| **Total** | **{{TOTAL_COUNT}}/26** | **{{TOTAL_PERCENT}}%** |

---

## Histórico de Rodadas

| Rodada | Status | Início | Conclusão | Notas |
|--------|--------|--------|-----------|-------|
| {{RODADA_ATIVA}} | {{RODADA_STATUS}} | {{RODADA_INICIO}} | — | Rodada ativa |

---

## Log de Atualizações

| Data | Ação | Agente |
|------|------|--------|
| {{DATA_ATUALIZACAO}} | Arquivo de progresso criado | @webinar (Maestro) |

---

*Gerado por @webinar (Maestro) — Webinário Squad*

<!-- END TEMPLATE -->

---

## Status Values

Os valores de status usados nas variáveis são:

| Valor | Significado | Ícone |
|-------|-------------|-------|
| `Pendente` | Artefato ainda não foi gerado | (vazio) |
| `Concluído` | Artefato foi gerado com sucesso | checkmark |
| `Revisando` | Artefato existe mas está sendo revisado | (em andamento) |
| `Herdado` | Artefato herdado de rodada anterior | (referência) |

## Initial Values (Projeto Novo)

Para um projeto novo, todos os artefatos devem ser inicializados como `Pendente`, a rodada ativa como `1`, e a fase atual como `Planejar`.

---

*Template created by squad-creator*
