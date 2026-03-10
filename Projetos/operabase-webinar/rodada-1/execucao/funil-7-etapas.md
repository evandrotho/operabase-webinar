# Funil de 7 Etapas do Webinario

> **Rodada:** 1 (reagendada)
> **Webinario:** "Como empresarios comuns estao substituindo equipe inteira por IA sem criar nada do zero"
> **Modo:** Estrutura Basica (validacao)
> **D-0:** Terca-feira, 17/03/2026, 20h
> **Gerado em:** 2026-03-10 (atualizado de 2026-03-06)
> **Agente:** @webinar-operator (Atlas)

---

## Diagrama Visual

```
  [1. CAPTACAO]           D-7 a D-0  |  Ads + Organico
       |
       v
  [2. NUTRICAO]           D-5 a D-2  |  WhatsApp (5 msgs)
       |
       v
  [3. ANTECIPACAO]        D-1 a D-0  |  WhatsApp (9 msgs)
       |
       v
  [4. ABERTURA]           D-0        |  Zoom ao vivo + Checkout
       |                      ^
       v                      | Pico 1 de Vendas
  [5. AMPLIACAO]          D+1 a D+4  |  Replay + WhatsApp (7 msgs)
       |
       v
  [6. FECHAMENTO]         D+5        |  WhatsApp (11 msgs) + Countdown
                              ^
                              | Pico 2 de Vendas

  [7. IMPULSIONAMENTO]    ---        |  N/A nesta rodada
```

**Padrao de vendas:** Pico 1 (abertura, D-0) → Vale (replay, D+1 a D+4) → Pico 2 (fechamento, D+5)

---

## Visao Geral

| # | Etapa | Pilar | Periodo | Msgs | Gatilho de Transicao | Status |
|---|-------|-------|---------|------|---------------------|--------|
| 1 | Captacao | Atracao | 10/03 a 17/03 | — | Leads suficientes (meta: 150) | A VERIFICAR |
| 2 | Nutricao | Engajamento | 12/03 a 15/03 | 5 | D-1 se aproxima | PRONTO |
| 3 | Antecipacao | Compromisso | 16/03 a 17/03 | 9 | D-0 hora do webinario | PRONTO |
| 4 | Abertura | Persuasao | 17/03 | 1 | Webinario realizado | PENDENTE |
| 5 | Ampliacao | Urgencia | 18/03 a 21/03 | 7 | Replay disponibilizado | PRONTO |
| 6 | Fechamento | Escassez | 22/03 | 11 | Deadline 23:59 atingido | PRONTO |
| 7 | Impulsionamento | Persuasao + Urgencia | — | — | Pos-fechamento | N/A RODADA 1 |

---

## Detalhamento por Etapa

### Etapa 1: Captacao

- **Pilar:** Atracao
- **Objetivo:** Gerar 150 leads qualificados com CPL <= R$20
- **Periodo:** 10/03 a 17/03 (8 dias — timeline D-7 completo)
- **Ferramentas:**
  - Facebook/Instagram Ads (campanhas prontas para ativar)
  - Pagina de captura (verificar status)
  - Facebook Pixel (instalado e configurado)
- **Metricas-chave:**
  | Metrica | Benchmark | Meta |
  |---------|-----------|------|
  | CPL (Custo por Lead) | ~10% do ticket | R$20 |
  | Taxa de conversao da pagina | 40% | 40% |
  | Volume de leads | — | 150 |
  | Cliques necessarios | — | 375 |
- **Gatilho de transicao:** Leads suficientes para meta OU data da nutricao
- **Artefatos:**
  - `copy-pagina-captura.md` — PRONTO
  - Ads (pixel + criativos + campanhas) — PRONTO
  - Pagina de captura publicada — A VERIFICAR
- **Vantagem D-7:** Com 8 dias de captacao (vs 5 no plano anterior), o algoritmo do Facebook tem mais tempo para otimizar. Espera-se CPL mais baixo e maior volume de leads.
- **Status: A VERIFICAR** — Confirmar se pagina de captura esta ativa e ads prontos para ativar HOJE

---

### Etapa 2: Nutricao

- **Pilar:** Engajamento
- **Objetivo:** Aquecer leads com conteudo relevante para maximizar comparecimento
- **Periodo:** 12/03 a 15/03 (4 dias — padrao D-7, mais espacado)
- **Ferramentas:**
  - WhatsApp (envio manual — sem SendFlow nesta rodada)
- **Mensagens:** 5 mensagens (1 por dia, melhor espacamento vs plano anterior)
  | Ref | Dia | Data | Hora | Tema |
  |-----|-----|------|------|------|
  | MSG-NUT-01 | Auto | D-7+ | Auto | Boas-vindas + pergunta sobre IA |
  | MSG-NUT-02 | D-5 | 12/03 (Qui) | 15:00 | Agentes de IA que executam trabalho real |
  | MSG-NUT-03 | D-4 | 13/03 (Sex) | 08:00 | Historia do Caio (18 → 0) |
  | MSG-NUT-04 | D-3 | 14/03 (Sab) | 15:00 | Prova social (case Caio detalhado) |
  | MSG-NUT-05 | D-2 | 15/03 (Dom) | 08:00 | Spoiler 3 motivos + presente |
- **Vantagem D-7:** Cada mensagem agendada tem seu proprio dia (1 msg/dia), em vez de 2 msgs no mesmo dia como no plano anterior. Menos bombardeio, mais engajamento.
- **Gatilho de transicao:** D-1 se aproxima
- **Artefatos:**
  - `mensagens-whatsapp.md` (secao nutricao) — PRONTO
- **Status: PRONTO**

---

### Etapa 3: Antecipacao

- **Pilar:** Compromisso
- **Objetivo:** Maximizar taxa de comparecimento no webinario (meta: 25% = 38 presentes)
- **Periodo:** 16/03 (D-1, Segunda) a 17/03 (D-0, Terca)
- **Ferramentas:**
  - WhatsApp (envio manual)
- **Mensagens:** 9 mensagens (2 em D-1 + 7 em D-0)
  | Ref | Dia | Data | Hora | Tema |
  |-----|-----|------|------|------|
  | MSG-ANT-D1-01 | D-1 | 16/03 (Seg) | 09:00 | "AMANHA e o dia" + confirmacao |
  | MSG-ANT-D1-02 | D-1 | 16/03 (Seg) | 20:00 | 3 dicas de preparacao |
  | MSG-ANT-D0-01 | D-0 | 17/03 (Ter) | 08:00 | "HOJE e o dia" |
  | MSG-ANT-D0-02 | D-0 | 17/03 (Ter) | 18:00 | Link da sala (2h antes) |
  | MSG-ANT-D0-03 | D-0 | 17/03 (Ter) | 19:00 | 1h antes |
  | MSG-ANT-D0-04 | D-0 | 17/03 (Ter) | 19:30 | 30min antes |
  | MSG-ANT-D0-05 | D-0 | 17/03 (Ter) | 19:45 | 15min antes |
  | MSG-ANT-D0-06 | D-0 | 17/03 (Ter) | 20:00 | "ESTAMOS AO VIVO!" |
  | MSG-ANT-D0-07 | D-0 | 17/03 (Ter) | 20:10 | "Ainda da tempo" |
- **Gatilho de transicao:** D-0, 20h — inicio do webinario
- **Artefatos:**
  - `mensagens-whatsapp.md` (secao antecipacao) — PRONTO
- **Status: PRONTO**

---

### Etapa 4: Abertura do Carrinho

- **Pilar:** Persuasao
- **Objetivo:** Converter presentes em compradores — **Pico 1 de vendas**
- **Periodo:** 17/03 (D-0), 20h-22h
- **Ferramentas:**
  - Zoom (webinario ao vivo, 90 min)
  - Checkout (link de compra no chat)
  - Slides (~45 slides)
- **Metricas-chave:**
  | Metrica | Benchmark | Meta |
  |---------|-----------|------|
  | Taxa conversao vendas/leads | 3% | 3% |
  | Vendas na abertura | — | 2-3 (do total de 4-5) |
- **Timeline do webinario:**
  | Minuto | Secao | Duracao |
  |--------|-------|---------|
  | 00-08 | Abertura (Headline + Identificacao) | ~8 min |
  | 08-16 | Empatia (Historia do Caio) | ~8 min |
  | 16-46 | Conteudo (3 Secrets) | ~30 min |
  | 47-82 | Pitch (15 etapas + Q&A) | ~25 min |
- **Gatilho de transicao:** Webinario realizado, checkout aberto
- **Artefatos:**
  - `roteiro-completo.md` — PRONTO
  - Sala Zoom — A VERIFICAR
  - Checkout (link de compra) — A VERIFICAR
  - Slides (~45) — A VERIFICAR
- **Status: PENDENTE** — Itens operacionais criticos a resolver ate 16/03 (D-1)

---

### Etapa 5: Ampliacao do Impacto

- **Pilar:** Urgencia
- **Objetivo:** Recuperar quem nao compareceu ou nao comprou na abertura
- **Periodo:** 18/03 (D+1) a 21/03 (D+4)
- **Ferramentas:**
  - Pagina de replay (ativar em D+1)
  - WhatsApp (envio manual)
  - Retargeting ads
- **Mensagens:** 1 pos-webinario + 7 ampliacao
  | Ref | Dia | Data | Hora | Tema |
  |-----|-----|------|------|------|
  | MSG-POS-01 | D-0 | 17/03 (Ter) | 22:00 | Agradecimento + oferta |
  | MSG-AMP-01 | D+1 | 18/03 (Qua) | 09:00 | Replay disponivel |
  | MSG-AMP-02 | D+1 | 18/03 (Qua) | 15:00 | Timestamps do replay |
  | MSG-AMP-03 | D+2 | 19/03 (Qui) | 09:00 | Case/depoimento |
  | MSG-AMP-04 | D+2 | 19/03 (Qui) | 15:00 | FAQ ("nao sou tecnico") |
  | MSG-AMP-05 | D+3 | 20/03 (Sex) | 09:00 | Bastidores (18 meses vs semanas) |
  | MSG-AMP-06 | D+3 | 20/03 (Sex) | 15:00 | Lembrete bonus |
  | MSG-AMP-07 | D+4 | 21/03 (Sab) | 10:00 | Ultimo aviso pre-fechamento |
- **Gatilho de transicao:** Replay disponibilizado, D+5 se aproxima
- **Artefatos:**
  - `copy-pagina-replay.md` — PRONTO
  - `mensagens-whatsapp.md` (secao ampliacao) — PRONTO
- **Status: PRONTO** — Pagina de replay sera ativada em D+1

---

### Etapa 6: Fechamento do Carrinho

- **Pilar:** Escassez
- **Objetivo:** Converter indecisos com urgencia maxima — **Pico 2 de vendas**
- **Periodo:** 22/03 (D+5, Sabado) — ultimo dia
- **Ferramentas:**
  - Pagina de fechamento (com contador regressivo)
  - WhatsApp (envio manual)
  - Retargeting ads (intenso)
- **Mensagens:** 11 mensagens em cadencia intensa (08h-23:45)
  | Hora | Ref | Tema |
  |------|-----|------|
  | 08:00 | MSG-FEC-01 | ULTIMO DIA — resumo |
  | 10:00 | MSG-FEC-02 | Depoimento forte |
  | 12:00 | MSG-FEC-03 | Bonus expira |
  | 14:00 | MSG-FEC-04 | FAQ final |
  | 16:00 | MSG-FEC-05 | Prova social |
  | 18:00 | MSG-FEC-06 | Garantia |
  | 20:00 | MSG-FEC-07 | 4 horas |
  | 21:00 | MSG-FEC-08 | 3 horas |
  | 22:00 | MSG-FEC-09 | 2 horas |
  | 23:00 | MSG-FEC-10 | Ultima hora |
  | 23:45 | MSG-FEC-11 | 15 minutos |
- **Vantagem:** Fechamento cai no sabado — leads estao em casa, mais disponiveis para decidir
- **Gatilho de transicao:** 22/03 23:59 — carrinho fecha
- **Artefatos:**
  - `copy-pagina-fechamento.md` — PRONTO
  - `mensagens-whatsapp.md` (secao fechamento) — PRONTO
- **Status: PRONTO** — Pagina de fechamento sera ativada em D+4

---

### Etapa 7: Impulsionamento do Lucro

- **Pilar:** Persuasao + Urgencia
- **Objetivo:** Maximizar receita pos-fechamento com downsell
- **Periodo:** N/A nesta rodada
- **Ferramentas:** WhatsApp
- **Mensagens:** 8 templates de downsell ja criados em `mensagens-whatsapp.md` (disponiveis para rodada 2+)
- **Status: N/A NESTA RODADA** — Decisao do owner: sem downsell na rodada 1. Pode ser ativado em rodadas futuras.

---

## Metricas e Benchmarks Consolidados

| Metrica | Benchmark | Meta Rodada 1 | Etapa |
|---------|-----------|---------------|-------|
| CPL | ~10% do ticket | R$20 | Captacao |
| Taxa conversao pagina | 40% | 40% | Captacao |
| Volume de leads | — | 150 | Captacao |
| Taxa de comparecimento | 25% | 38 presentes | Antecipacao |
| Taxa conversao vendas/leads | 3% | 4-5 vendas | Abertura |
| Padrao de vendas | Pico-Vale-Pico | — | Abertura + Fechamento |
| ROAS | >= 2x | 3,75x | Geral |
| Investimento | — | R$3.000 | Captacao |
| Faturamento | — | R$11.250 | Geral |
| Lucro | — | R$8.250 | Geral |

---

## Comparacao: D-7 (atual) vs. D-4 (plano anterior)

| Aspecto | D-4 Comprimido (plano anterior) | D-7 Completo (plano atual) |
|---------|--------------------------------|---------------------------|
| **Dias de captacao** | 5 (06/03 a 10/03) | 8 (10/03 a 17/03) |
| **Dias de nutricao** | 3 (comprimido) | 4 (padrao metodologia) |
| **Msgs nutricao/dia** | 2 msgs em D-4, 2 msgs em D-3 | 1 msg/dia (melhor espacamento) |
| **Duracao total** | 10 dias | 13 dias |
| **Tempo de preparacao** | 4 dias (apertado) | 7 dias (confortavel) |
| **Otimizacao de ads** | Pouco tempo para algoritmo aprender | Algoritmo tem 5+ dias para otimizar |
| **Budget diario** | ~R$600/dia captacao | ~R$450/dia captacao |
| **Dia do fechamento** | Domingo (15/03) | Sabado (22/03) |

---

## Comparacao: Basica vs. Escalada

| Aspecto | Rodada 1 (Basica) | Rodadas Futuras (Escalada) |
|---------|-------------------|---------------------------|
| **Objetivo** | Validar oferta e mensagem | Escalar volume e receita |
| **Investimento** | R$3.000 | Aumentar conforme ROAS |
| **Captacao** | Ads + organico basico | Ads agressivo + multiplas fontes |
| **Automacao** | Envio manual WhatsApp | SendFlow completo (webhooks + tags) |
| **Chat** | Equipe de apoio ao vivo | Chat simulado otimizado (se EverWebinar) |
| **Replay** | Pagina simples | Com segmentacao e retargeting avancado |
| **Downsell** | Desativado | Ativado (8 msgs + oferta alternativa) |
| **Metricas** | Basicas (CPL, conversao, ROAS) | Avancadas (LTV, CAC, empilhamento) |
| **Empilhamento** | N/A (1a rodada) | Sim (reimpactar leads de rodadas anteriores) |

---

## Status Geral

- **Artefatos de conteudo:** 14 de 14 prontos (100%)
- **Ferramentas operacionais:** A verificar (verificar status atual)
- **Etapas prontas para execucao:** Conteudo 100% pronto, operacional a confirmar
- **Vantagem principal:** 7 dias de preparacao (vs 4 no plano anterior)

### Proximos Passos

1. **Hoje (10/03, D-7):** Verificar pagina de captura e ativar anuncios — libera Etapa 1
2. **Ate 15/03 (D-2):** Configurar Zoom, checkout e slides — com calma
3. **16/03 (D-1):** Rodar `*checklist` para verificacao final + teste e2e
4. **17/03 (D-0):** Executar webinario seguindo `agenda-completa.md`
5. **Apos 22/03:** Ativar @webinar-analyst com `*kpis` para analise da rodada

---

> Funil atualizado por @webinar-operator (Atlas)
> Reagendamento: D-0 de 10/03 para 17/03 | Timeline: D-4 → D-7 (completo)
> Metodologia: Webinario Infalivel (Taioba) + Perfect Webinar (Brunson)
