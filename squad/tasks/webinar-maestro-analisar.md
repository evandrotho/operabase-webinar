---
task: webinar-maestro-analisar
responsavel: "@webinar"
responsavel_type: Agent
atomic_layer: Task
elicit: true

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: kpis-funil
      lines: "L339-L352"
      purpose: "KPIs de funil — benchmarks de referência (contexto geral)"
    - id: kpis-resultado
      lines: "L353-L365"
      purpose: "KPIs de resultado — exemplo modelado"
    - id: metricas-consolidadas
      lines: "L1672-L1715"
      purpose: "Métricas e KPIs consolidados — referência"
    - id: perpetuo
      lines: "L3834-L3872"
      purpose: "Webinário perpétuo — contexto para orientar"
    - id: empilhamento
      lines: "L3900-L3918"
      purpose: "Empilhamento de webinários — contexto"
    - id: frontend-backend
      lines: "L3919-L3944"
      purpose: "Modelo Front-end + Back-end — contexto"

inputs:
  required: []
  optional:
    - campo: rodada
      tipo: number
      origem: User Input
      obrigatorio: false
      validacao: "Número da rodada (default: rodada ativa)"

output:
  - campo: handoff_artifact
    tipo: file
    destino: ".aiox/handoffs/"
    persistido: true
  - campo: progress_update
    tipo: file
    destino: docs/webinar/progress.md
    persistido: true

Checklist:
  - "[ ] Step 1: Verificar se campanha foi executada"
  - "[ ] Step 2: Verificar estado da análise"
  - "[ ] Step 3: Apresentar visão geral da fase"
  - "[ ] Step 4: Identificar próxima análise pendente"
  - "[ ] Step 5: Orientar e fazer handoff para @webinar-analyst"
  - "[ ] Step 6: Atualizar progress.md"
---

# Webinar Maestro — *analisar

## Purpose

Iniciar ou continuar a fase de análise pós-webinário. O Maestro confirma que a campanha foi executada, mostra o estado das análises, e redireciona para o @webinar-analyst (Lens).

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] Campanha executada com dados reais disponíveis
    tipo: pre-condition
    blocker: false
    validacao: |
      Não há como verificar automaticamente se a campanha foi executada.
      Perguntar ao usuário se já tem dados reais para analisar.
    error_message: |
      A fase de análise requer dados reais da campanha executada.
      Se ainda não executou, use *executar para preparar o lançamento.
```

## Execution Steps

### Step 1: Verificar Contexto da Campanha

1. Determinar rodada ativa
2. Verificar se artefatos de execução existem em `docs/webinar/rodada-{N}/execucao/`:
   - Se a fase de execução não foi realizada, alertar o usuário
3. Verificar se `orcamento-meta.md` existe (para comparação Orçado vs. Realizado)

**Elicitation Point** (`elicit: true`)

Perguntar ao usuário:

```
📊 Fase de Análise — Rodada {N}

Antes de começar a análise, preciso confirmar:

1. Você já executou a campanha do webinário?
2. Tem dados reais disponíveis (leads, vendas, faturamento)?

Se sim, vamos analisar! Se não, pode ser cedo demais para esta fase.

Sua campanha já foi executada? (sim/não)
```

Se o usuário responder "não":
- Informar: "Sem problemas! Quando executar a campanha e tiver os dados, volte aqui com `*analisar`."
- Sugerir: "Enquanto isso, quer revisar o checklist de lançamento? Use `*executar`."
- **HALT**

### Step 2: Verificar Estado da Análise

Verificar existência de cada artefato em `docs/webinar/rodada-{N}/analise/`:

| # | Artefato | Arquivo | Input Principal |
|---|----------|---------|----------------|
| 1 | Relatório de KPIs | `relatorio-kpis.md` | orcamento-meta (benchmarks) |
| 2 | Diagnóstico do Funil | `diagnostico-funil.md` | relatorio-kpis, funil-7-etapas |
| 3 | Orçado vs. Realizado | `orcado-vs-realizado.md` | orcamento-meta, relatorio-kpis |
| 4 | Plano Próxima Rodada | `plano-proxima-rodada.md` | diagnostico-funil |

Verificar também em `docs/webinar/estrategias/`:

| # | Artefato | Arquivo | Quando usar |
|---|----------|---------|-------------|
| 5 | Estratégia de Empilhamento | `estrategia-empilhamento.md` | Após 1+ rodadas |
| 6 | Estratégia Perpétuo | `estrategia-perpetuo.md` | Quando quer automatizar |

Criar diretórios se não existirem.

### Step 3: Apresentar Visão Geral da Fase

**Elicitation Point** (`elicit: true`)

```
📊 Fase de Análise — Rodada {N}

Nesta fase, analisamos os resultados da campanha e identificamos melhorias.

Análises principais:
1. 📈 **KPIs** — Registrar e analisar métricas (leads, vendas, ROAS, conversão)
2. 🔍 **Diagnóstico** — Identificar gargalos no funil (onde está perdendo gente?)
3. 📊 **Orçado vs. Realizado** — Comparar projeções com resultados reais
4. 🔄 **Próxima Rodada** — Planejar otimizações para o próximo webinário

Estratégias avançadas (opcionais):
5. 📚 **Empilhamento** — Planejar sequência de webinários
6. ♾️ **Perpétuo** — Converter para modo evergreen/automático
7. 🔀 **Front-end/Back-end** — Modelo VSL + Webinário

Status atual:
  ✅/⬜ Relatório de KPIs
  ✅/⬜ Diagnóstico do Funil
  ✅/⬜ Orçado vs. Realizado
  ✅/⬜ Plano Próxima Rodada
  ✅/⬜ Estratégia de Empilhamento
  ✅/⬜ Estratégia Perpétuo
```

**Ordem recomendada:** KPIs → Diagnóstico → Orçado vs. Realizado → Plano Próxima Rodada

> **Nota:** As estratégias avançadas (empilhamento, perpétuo, front-end/back-end) são opcionais e podem ser feitas a qualquer momento após a primeira análise.

### Step 4: Identificar Próxima Análise Pendente

| Prioridade | Artefato | Comando @webinar-analyst | Pré-req |
|------------|----------|--------------------------|---------|
| 1 | Relatório de KPIs | `*kpis` | orcamento-meta (benchmarks) |
| 2 | Diagnóstico do Funil | `*diagnostico` | relatorio-kpis |
| 3 | Orçado vs. Realizado | `*orcado-vs-realizado` | orcamento-meta + relatorio-kpis |
| 4 | Plano Próxima Rodada | `*proxima-rodada` | diagnostico-funil |
| 5 | Empilhamento (opcional) | `*empilhamento` | relatorio-kpis |
| 6 | Perpétuo (opcional) | `*perpetuo` | roteiro-completo + relatorio-kpis |
| 7 | Front-end/Back-end (opc.) | `*frontend-backend` | canvas-produto + relatorio-kpis |

Se as 4 análises principais estiverem completas:
- Informar: "Análise principal completa!"
- Sugerir: "Quer explorar estratégias avançadas (empilhamento, perpétuo)? Ou iniciar a próxima rodada com `*planejar`?"

### Step 5: Orientar e Fazer Handoff

**Elicitation Point** (`elicit: true`)

```
O próximo passo é {análise pendente}.

Opções:
1. Realizar {análise pendente} agora (recomendado)
2. Escolher outra análise
3. Explorar estratégias avançadas
4. Iniciar próxima rodada (*planejar)
5. Voltar ao menu principal

O que prefere?
```

**Handoff artifact:**

```yaml
handoff:
  from_agent: "webinar"
  to_agent: "webinar-analyst"
  story_context:
    project: "webinar"
    rodada: {N}
    phase: "analise"
    current_task: "{análise escolhida}"
    available_data:
      - "docs/webinar/rodada-{N}/planejamento/orcamento-meta.md"
      - "docs/webinar/rodada-{N}/execucao/funil-7-etapas.md"
      - "docs/webinar/rodada-{N}/execucao/timeline-campanha.md"
  decisions:
    - "Usuário confirmou que campanha foi executada"
    - "Usuário optou por: {análise}"
  files_modified: []
  blockers: []
  next_action: "*{comando correspondente}"
```

### Step 6: Atualizar progress.md

Atualizar `docs/webinar/progress.md` com:
- Fase atual: "Analisar"
- Status dos artefatos de análise
- Último acesso

## Post-Conditions

```yaml
post-conditions:
  - [ ] Confirmação de campanha executada obtida
    tipo: post-condition
    blocker: false
    validacao: Usuário confirmou que tem dados reais.
    error_message: "Usuário não confirmou execução da campanha."
  - [ ] Handoff preparado para @webinar-analyst (se aplicável)
    tipo: post-condition
    blocker: false
    validacao: Handoff artifact criado com contexto adequado.
    error_message: "Handoff não criado."
```

## Error Handling

### Error 1: Campanha não executada

```yaml
error: CAMPAIGN_NOT_EXECUTED
cause: Usuário não executou a campanha ainda
resolution: Orientar a completar a fase de execução primeiro
recovery: "Use *executar para preparar o lançamento."
```

### Error 2: Dados insuficientes para análise

```yaml
error: INSUFFICIENT_DATA
cause: Orcamento-meta.md não existe para comparação
resolution: Informar que a comparação Orçado vs. Realizado ficará limitada
recovery: "Podemos registrar os KPIs mesmo sem o orçamento original. A comparação ficará parcial."
```

## Handoff

```yaml
next_agent: "@webinar-analyst"
next_command: "*kpis | *diagnostico | *orcado-vs-realizado | *proxima-rodada | *empilhamento | *perpetuo | *frontend-backend"
condition: Campanha executada e usuário escolheu análise
alternatives:
  - agent: "@webinar-operator", command: "*checklist", condition: "Campanha não executada ainda"
  - agent: "@webinar-strategist", command: "*canvas-cliente", condition: "Próxima rodada"
  - agent: "@webinar", command: "*status", condition: "Usuário quer voltar"
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
  - analisar
  - routing
  - handoff
```
