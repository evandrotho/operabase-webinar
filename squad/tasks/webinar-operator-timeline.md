---
tools: []
checklists: []
execution_mode: interactive
---

# webinar-operator-timeline

Gerar cronograma completo da campanha de webinario com datas reais.

## Purpose

Montar um cronograma dia-a-dia de toda a campanha de webinario, desde o inicio da captacao ate o fechamento do carrinho e impulsionamento. Cada linha contem: data, hora, mensagem/acao, canal (WhatsApp, email, anuncio), pilar da Espiral de Vendas e objetivo. Usa como base as mensagens geradas e o funil de 7 etapas.

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "funil-visao-geral"
      lines: "L409-L421"
      purpose: "Visao geral do funil de 7 etapas -- sequencia e gatilhos de transicao"
    - id: "estrutura-basica-escalada"
      lines: "L422-L434"
      purpose: "Estrutura Basica (validacao) vs Escalada (escala)"
    - id: "etapa-1-captacao"
      lines: "L451-L525"
      purpose: "Etapa 1: Captacao -- como captar leads"
    - id: "etapa-2-nutricao"
      lines: "L526-L685"
      purpose: "Etapa 2: Nutricao -- 5 mensagens de engajamento"
    - id: "etapa-3-antecipacao"
      lines: "L686-L890"
      purpose: "Etapa 3: Antecipacao -- D-1 e D-0, 9 mensagens"
    - id: "etapa-4-abertura"
      lines: "L891-L984"
      purpose: "Etapa 4: Abertura do carrinho -- webinario ao vivo/gravado"
    - id: "etapa-5-ampliacao"
      lines: "L985-L1197"
      purpose: "Etapa 5: Ampliacao do impacto -- replay, 7 mensagens"
    - id: "etapa-6-fechamento"
      lines: "L1198-L1463"
      purpose: "Etapa 6: Fechamento do carrinho -- escassez, 11 mensagens"
    - id: "etapa-7-impulsionamento"
      lines: "L1464-L1651"
      purpose: "Etapa 7: Impulsionamento do lucro -- downsell, 8 mensagens"
    - id: "espiral-vendas"
      lines: "L22-L80"
      purpose: "Espiral de Vendas: 5 pilares e dinamica de execucao"
```

## Prerequisites

```yaml
prerequisites:
  required:
    - artifact: "docs/webinar/rodada-{N}/conteudo/roteiro-completo.md"
      description: "Roteiro completo (para saber duracao e estrutura do webinario)"
      if_missing: "Para montar a timeline, preciso do roteiro completo. Quer ativar o @webinar-creator com *roteiro?"
    - artifact: "docs/webinar/rodada-{N}/conteudo/mensagens-whatsapp.md"
      description: "Mensagens WhatsApp (para distribuir no cronograma)"
      if_missing: "Para montar a timeline, preciso das mensagens WhatsApp. Quer ativar o @webinar-creator com *mensagens?"
  optional:
    - artifact: "docs/webinar/rodada-{N}/planejamento/orcamento-meta.md"
      description: "Orcamento e meta (investimento em ads, datas planejadas)"
      enriches: "Datas de inicio/fim da campanha e investimento diario em anuncios"
```

## Task Definition

```yaml
task: timelineCampanha()
responsavel: Atlas (Executor)
responsavel_type: Agente
elicit: true

Entrada:
- campo: roteiro_completo
  tipo: file
  origem: "docs/webinar/rodada-{N}/conteudo/roteiro-completo.md"
  obrigatorio: true

- campo: mensagens_whatsapp
  tipo: file
  origem: "docs/webinar/rodada-{N}/conteudo/mensagens-whatsapp.md"
  obrigatorio: true

- campo: orcamento_meta
  tipo: file
  origem: "docs/webinar/rodada-{N}/planejamento/orcamento-meta.md"
  obrigatorio: false

Saida:
- campo: timeline_campanha
  tipo: file
  destino: "docs/webinar/rodada-{N}/execucao/timeline-campanha.md"
  persistido: true
  template: webinar-timeline-campanha-tmpl.md
```

## SEQUENTIAL Task Execution

### 0. Validar Pre-requisitos e Carregar Dados

- Verificar existencia dos artefatos obrigatorios
- Carregar knowledge base: L409-L421, L422-L434, L451-L1651, L22-L80
- Ler `roteiro-completo.md` para extrair timeline do webinario
- Ler `mensagens-whatsapp.md` para mapear mensagens por etapa do funil
- Se `orcamento-meta.md` existir, ler para extrair datas e investimento planejado

### 1. Elicitar Datas da Campanha

**ELICIT (pergunta 1 de cada vez):**

1. "Qual a **data do webinario**? (dia em que o webinario vai ao ar -- ou primeira sessao no EverWebinar)"
2. "Quantos dias **antes** do webinario voce quer comecar a captacao? Recomendacao da metodologia:
   1. **7 dias** (padrao, recomendado para primeira rodada)
   2. **14 dias** (mais tempo para anuncios e nutricao)
   3. **3-5 dias** (campanha curta, publico quente)"
3. "Quantos dias **depois** do webinario voce quer manter o carrinho aberto?
   1. **3 dias** (escassez alta, padrao)
   2. **5 dias** (mais tempo para replay e fechamento)
   3. **7 dias** (campanha longa)"
4. "Voce quer incluir **impulsionamento pos-fechamento** (downsell/order bump/upsell)?
   1. **Sim** -- adicionar 3-5 dias apos fechamento
   2. **Nao** -- campanha termina no fechamento do carrinho"
5. "Qual o **horario padrao** para envio de mensagens WhatsApp? (Sugestao: 8h, 12h, 18h)"

### 2. Calcular Datas do Cronograma

Baseado nas respostas:

- **D-0** = Data do webinario
- **D-X** = X dias antes do webinario (captacao e nutricao)
- **D+1 a D+Y** = Dias apos webinario (ampliacao, fechamento)
- **D+Y+1 a D+Y+Z** = Impulsionamento (se aplicavel)

Gerar calendario com datas reais (dia da semana + data).

### 3. Distribuir Mensagens no Cronograma

Baseado na knowledge base e mensagens-whatsapp.md:

**Fase 1: Captacao (D-X a D-3)**
- Inicio dos anuncios
- Publicacao de conteudo organico
- Canal: Facebook Ads, Instagram, organico

**Fase 2: Nutricao (D-X a D-1)**
- 5 mensagens de nutricao distribuidas
- Pilar: Engajamento
- Canal: WhatsApp (SendFlow)
- Horarios: manhã e tarde, alternados

**Fase 3: Antecipacao (D-1 e D-0)**
- 2 mensagens D-1 (antecipacao)
- 7 mensagens D-0 (dia do webinario: lembrete manha, lembrete tarde, "comecou!", etc.)
- Pilar: Compromisso
- Canal: WhatsApp (SendFlow)

**Fase 4: Abertura do Carrinho (D-0)**
- Horario do webinario
- Abertura do checkout
- Pilar: Persuasao
- Canal: EverWebinar + Checkout

**Fase 5: Ampliacao (D+1 a D+Y-2)**
- 7 mensagens de ampliacao (replay, depoimentos, escassez suave)
- 1 mensagem pos-webinario
- Pilar: Urgencia
- Canal: WhatsApp + Email

**Fase 6: Fechamento (D+Y-1 a D+Y)**
- 11 mensagens de fechamento (urgencia maxima, ultimo dia, countdown)
- Pilar: Escassez
- Canal: WhatsApp + Email + Anuncios retargeting

**Fase 7: Impulsionamento (D+Y+1 a D+Y+Z)** (se aplicavel)
- 8 mensagens de downsell
- Pilar: Persuasao + Urgencia
- Canal: WhatsApp

### 4. Montar Tabela Cronologica

Gerar tabela completa no formato:

| Dia | Data | Hora | Acao/Mensagem | Canal | Etapa Funil | Pilar | Notas |
|-----|------|------|---------------|-------|-------------|-------|-------|

Cada linha corresponde a uma acao especifica (envio de mensagem, publicacao, configuracao).

### 5. Adicionar Marcos e Checkpoints

- **Marcos importantes:**
  - Inicio da captacao
  - Meta de leads atingida (se orcamento disponivel)
  - D-1: verificacao final pre-webinario
  - D-0: webinario ao vivo / sessao EverWebinar
  - Abertura do carrinho
  - Pico 1 de vendas (abertura)
  - Disponibilizacao do replay
  - Pico 2 de vendas (fechamento)
  - Fechamento do carrinho
  - Inicio do impulsionamento (se aplicavel)

### 6. Compilar e Salvar Timeline

- Usar template `webinar-timeline-campanha-tmpl.md`
- Preencher com todas as datas, mensagens, canais e marcos
- Salvar em `docs/webinar/rodada-{N}/execucao/timeline-campanha.md`
- Mostrar resumo: total de dias, total de mensagens, marcos principais

### 7. Sugerir Proximo Passo

- "Proximo passo recomendado: `*funil` para visualizar o funil completo de 7 etapas com status"
- Ou: "`*checklist` para verificacao final pre-lancamento"

## Output

```yaml
output:
  path: "docs/webinar/rodada-{N}/execucao/timeline-campanha.md"
  template: webinar-timeline-campanha-tmpl.md
  format: markdown
  sections:
    - Resumo da Campanha
    - Calendario Geral
    - Cronograma Detalhado (tabela dia-a-dia)
    - Marcos e Checkpoints
    - Distribuicao por Canal
    - Distribuicao por Pilar da Espiral
```

## Error Handling

**Strategy:** guide-and-retry

**Common Errors:**

1. **Error:** Roteiro ou mensagens nao encontrados
   - **Resolution:** Redirecionar para @webinar-creator
2. **Error:** Data do webinario no passado
   - **Resolution:** Solicitar nova data
3. **Error:** Mensagens insuficientes para o periodo
   - **Resolution:** Ajustar periodo ou gerar mensagens adicionais com @webinar-creator

## Handoff

```yaml
next_agent: "@webinar-operator"
next_command: "*funil"
condition: "Timeline montada, funil nao visualizado"
alternatives:
  - agent: "@webinar-operator"
    command: "*checklist"
    condition: "Timeline e funil prontos"
```
