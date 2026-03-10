---
task: webinar-maestro-guia
responsavel: "@webinar"
responsavel_type: Agent
atomic_layer: Task
elicit: true

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: espiral-vendas-visao-geral
      lines: "L22-L80"
      purpose: "Espiral de Vendas — 5 pilares e visão geral do ciclo"
    - id: canvas-cliente-ideal
      lines: "L83-L140"
      purpose: "Canvas do Cliente Ideal — visão geral das 9 perguntas"
    - id: canvas-produto
      lines: "L141-L199"
      purpose: "Canvas do Produto — visão geral dos 7 blocos"
    - id: canvas-webinar
      lines: "L200-L283"
      purpose: "Canvas do Webinário — visão geral dos 15 blocos"
    - id: canvas-orcamento
      lines: "L284-L338"
      purpose: "Canvas de Orçamento — visão geral das 12 premissas"
    - id: funil-visao-geral
      lines: "L409-L421"
      purpose: "Funil de 7 etapas — visão geral"
    - id: abertura
      lines: "L1867-L2039"
      purpose: "Abertura — visão geral dos 7 blocos"
    - id: empatia
      lines: "L2040-L2251"
      purpose: "Empatia/História — visão geral"
    - id: conteudo
      lines: "L2252-L2471"
      purpose: "Conteúdo — 3 Secrets"
    - id: pitch
      lines: "L2472-L2832"
      purpose: "Pitch — 15 etapas"
    - id: glossario
      lines: "L3041-L3118"
      purpose: "Glossário de termos proprietários"

inputs:
  required: []
  optional:
    - campo: topico
      tipo: string
      origem: User Input
      obrigatorio: false
      validacao: "Tópico específico (ex: 'planejamento', 'roteiro', 'funil')"

output:
  - campo: guia_display
    tipo: string
    destino: Console (display to user)
    persistido: false

Checklist:
  - "[ ] Step 1: Apresentar visão geral do processo"
  - "[ ] Step 2: Explicar cada fase"
  - "[ ] Step 3: Responder dúvidas"
  - "[ ] Step 4: Sugerir próximo passo"
---

# Webinar Maestro — *guia

## Purpose

Explicar ao usuário todo o processo do webinário de vendas em linguagem simples, sem jargão técnico. O guia cobre as 4 fases, o que cada uma produz, e como o squad de agentes funciona. Este é o comando educacional — ajuda o usuário a entender antes de agir.

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] Nenhum — este comando é sempre disponível
    tipo: pre-condition
    blocker: false
    validacao: Sempre acessível, independente do estado do projeto.
    error_message: N/A
```

## Execution Steps

### Step 1: Apresentar Visão Geral

Apresentar ao usuário de forma acolhedora e acessível:

```
🎯 Guia Completo do Webinário de Vendas

Olá! Vou te explicar como funciona o processo completo de criar e executar
um webinário de vendas. Este processo é baseado na metodologia fusionada
"Webinário Infalível" + "Perfect Webinar" — duas das melhores referências
do mercado.

O processo tem 4 fases, e para cada uma existe um especialista que te guia:

┌─────────────────────────────────────────────────────────────┐
│  📋 PLANEJAR  →  🔨 CONSTRUIR  →  🚀 EXECUTAR  →  📊 ANALISAR  │
│    (Sage)          (Spark)          (Atlas)          (Lens)     │
└─────────────────────────────────────────────────────────────┘

Eu (Maestro) sou seu ponto de entrada — te ajudo a entender onde você
está, o que falta fazer, e conecto você ao especialista certo.
```

### Step 2: Explicar Cada Fase em Detalhe

**Elicitation Point** (`elicit: true`)

Perguntar: "Quer que eu explique cada fase em detalhe, ou quer ir direto para uma fase específica?"

Opções:
1. Ver todas as fases (explicação completa)
2. Só a fase de Planejamento
3. Só a fase de Construção
4. Só a fase de Execução
5. Só a fase de Análise
6. Ir direto para a ação (começar a usar)

---

#### Fase 1: PLANEJAR (Especialista: @webinar-strategist / Sage)

```
📋 PLANEJAR — Definir a estratégia

Nesta fase, respondemos às perguntas fundamentais sobre seu negócio e webinário.
É como montar a fundação de uma casa — se fizer bem, o resto fica fácil.

O que produzimos:

  👤 Canvas do Cliente Ideal (9 perguntas)
     Quem é seu público? Quais são suas dores? Onde estão?
     → Comando: @webinar-strategist *canvas-cliente

  📦 Canvas do Produto (7 blocos)
     Qual sua Grande Promessa? Qual seu Mecanismo Único?
     → Comando: @webinar-strategist *canvas-produto

  🎯 Canvas do Webinário (15 blocos)
     Tema, crença-alvo, oferta, bônus, objeções...
     → Comando: @webinar-strategist *canvas-webinar

  🧠 Avatar Blueprint (7 perguntas + tabela)
     Mapa profundo do cliente: desejos, frustrações, objeções
     → Comando: @webinar-strategist *avatar

  💰 Orçamento e Meta (12 premissas)
     Meta de vendas, investimento, ROAS esperado
     → Comando: @webinar-strategist *orcamento

  📊 Resumo de Planejamento
     Consolidação de tudo — visão estratégica completa
     → Comando: @webinar-strategist *resumo

Tempo estimado: 2-4 horas (depende do preparo)
Pré-requisito: Nenhum — é aqui que tudo começa!
```

#### Fase 2: CONSTRUIR (Especialista: @webinar-creator / Spark)

```
🔨 CONSTRUIR — Criar o conteúdo

Com o planejamento pronto, transformamos tudo em conteúdo utilizável.
O roteiro segue a estrutura "Black Box" com 4 partes:

  🎤 Abertura (5-10 min) — Captar atenção, criar identificação
     → Comando: @webinar-creator *abertura

  💜 Empatia (5-10 min) — Contar sua história de transformação
     → Comando: @webinar-creator *empatia

  📚 Conteúdo (25-40 min) — 3 Segredos que quebram falsas crenças
     → Comando: @webinar-creator *conteudo

  💰 Pitch (20-30 min) — Apresentar oferta com stack e garantia
     → Comando: @webinar-creator *pitch

  📄 Roteiro Completo — Consolidação com timeline
     → Comando: @webinar-creator *roteiro

Além do roteiro:

  📱 Mensagens WhatsApp (41+ templates)
     Para nutrição, antecipação, pós-webinário, fechamento, downsell
     → Comando: @webinar-creator *mensagens

  📄 Copy de Páginas
     Captura, replay e fechamento — textos prontos para usar
     → Comandos: *copy-captura, *copy-replay, *copy-fechamento

Tempo estimado: 4-8 horas
Pré-requisito: Canvases de planejamento preenchidos
```

#### Fase 3: EXECUTAR (Especialista: @webinar-operator / Atlas)

```
🚀 EXECUTAR — Configurar e lançar

Com o conteúdo pronto, configuramos as ferramentas e preparamos o lançamento.
Cada guia é um passo-a-passo detalhado.

  📹 Guia EverWebinar — Configurar o webinário automatizado
     Vídeo, agendamento, chat simulado, replay
     → Comando: @webinar-operator *setup-everwebinar

  📱 Guia SendFlow — Configurar automação WhatsApp
     Grupos, fases, mensagens automáticas, deep links
     → Comando: @webinar-operator *setup-sendflow

  💳 Guia Pagamento — Webhooks de pagamento
     Zouti, Hotmart, Kiwify — ações automáticas
     → Comando: @webinar-operator *setup-pagamento

  📊 Guia Pixel — Facebook Pixel e tracking
     Eventos por página, integração
     → Comando: @webinar-operator *setup-pixel

  📅 Timeline — Cronograma dia-a-dia da campanha
     → Comando: @webinar-operator *timeline

  🔄 Funil — Visualizar as 7 etapas do funil
     → Comando: @webinar-operator *funil

  ✅ Checklist — Verificação final antes de lançar
     → Comando: @webinar-operator *checklist

Tempo estimado: 3-6 horas
Pré-requisito: Roteiro completo + mensagens geradas
```

#### Fase 4: ANALISAR (Especialista: @webinar-analyst / Lens)

```
📊 ANALISAR — Medir e otimizar

Após executar a campanha e ter dados reais, analisamos os resultados.

  📈 Relatório de KPIs — Métricas da campanha vs. benchmarks
     → Comando: @webinar-analyst *kpis

  🔍 Diagnóstico do Funil — Onde está o gargalo?
     → Comando: @webinar-analyst *diagnostico

  📊 Orçado vs. Realizado — Comparação detalhada
     → Comando: @webinar-analyst *orcado-vs-realizado

  🔄 Plano Próxima Rodada — Otimizações priorizadas
     → Comando: @webinar-analyst *proxima-rodada

Estratégias avançadas (opcionais):
  📚 Empilhamento — Sequência de webinários
  ♾️ Perpétuo — Modo evergreen automático
  🔀 Front-end/Back-end — VSL + Webinário

Tempo estimado: 1-2 horas (com dados em mãos)
Pré-requisito: Campanha executada com dados reais
```

### Step 3: Responder Dúvidas

**Elicitation Point** (`elicit: true`)

```
Tem alguma dúvida sobre o processo? Posso explicar melhor qualquer fase
ou conceito. Alguns termos comuns:

- **Black Box:** A estrutura do webinário (Abertura → Empatia → Conteúdo → Pitch)
- **Espiral de Vendas:** Os 5 pilares (Atração → Engajamento → Compromisso → Persuasão → Conversão)
- **Mecanismo Único:** "Duas ou três palavras que geram mistério" sobre como seu produto funciona
- **Stack Slide:** A composição visual da sua oferta com todos os entregáveis e valores
- **False Beliefs:** Crenças erradas do público que o conteúdo precisa quebrar
- **Epiphany Bridge:** Técnica de história que gera "momento de epifania" no público
- **Trial Close:** Micro-confirmações durante o pitch ("Faz sentido?")

Opções:
1. Explicar algum termo ou conceito
2. Começar a usar — *planejar
3. Ver status do projeto — *status
4. Voltar ao menu principal
```

### Step 4: Sugerir Próximo Passo

Com base na resposta do usuário, orientar:

1. Se quer explicação: Usar knowledge_base para explicar o conceito em linguagem simples
2. Se quer começar: Sugerir `*planejar` para novos projetos ou `*status` para projetos em andamento
3. Se quer ver status: Redirecionar para `*status`

## Post-Conditions

```yaml
post-conditions:
  - [ ] Usuário recebeu explicação clara do processo
    tipo: post-condition
    blocker: false
    validacao: Usuário entende as 4 fases e o papel de cada agente.
    error_message: N/A
```

## Error Handling

```yaml
error: NONE
cause: Este comando é puramente informacional e não tem cenários de erro.
resolution: N/A
recovery: N/A
```

## Handoff

```yaml
next_agent: Depende da escolha do usuário
next_command: "*planejar | *status | *construir | *executar | *analisar"
condition: Usuário decidiu agir após entender o processo
alternatives:
  - agent: "@webinar-strategist", command: "*canvas-cliente", condition: "Quer ir direto ao planejamento"
  - agent: "@webinar", command: "*status", condition: "Quer ver estado do projeto"
```

## Metadata

```yaml
version: 1.0.0
created: 2026-03-05
updated: 2026-03-05
author: squad-creator
tags:
  - webinar
  - maestro
  - guia
  - educacional
  - onboarding
```
