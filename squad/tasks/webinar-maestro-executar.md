---
task: webinar-maestro-executar
responsavel: "@webinar"
responsavel_type: Agent
atomic_layer: Task
elicit: true

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: funil-visao-geral
      lines: "L409-L421"
      purpose: "Visão geral do funil de 7 etapas (contexto para orientar)"
    - id: estrutura-basica-escalada
      lines: "L422-L434"
      purpose: "Estrutura Básica vs. Escalada — para contextualizar"
    - id: mapa-ferramentas
      lines: "L1652-L1671"
      purpose: "Mapa consolidado de ferramentas — referência rápida"
    - id: stack-tecnica
      lines: "L3736-L3758"
      purpose: "Stack técnica completa — para contextualizar setup"

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
  - "[ ] Step 1: Validar pré-requisitos de conteúdo"
  - "[ ] Step 2: Verificar estado da execução"
  - "[ ] Step 3: Apresentar visão geral da fase"
  - "[ ] Step 4: Identificar próxima configuração pendente"
  - "[ ] Step 5: Orientar e fazer handoff para @webinar-operator"
  - "[ ] Step 6: Atualizar progress.md"
---

# Webinar Maestro — *executar

## Purpose

Iniciar ou continuar a fase de execução do webinário. O Maestro valida se o conteúdo necessário foi criado, mostra o estado das configurações de ferramentas, e redireciona para o @webinar-operator (Atlas).

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] Roteiro completo e mensagens gerados
    tipo: pre-condition
    blocker: true
    validacao: |
      Verificar existência de:
      - docs/webinar/rodada-{N}/conteudo/roteiro-completo.md
      - docs/webinar/rodada-{N}/conteudo/mensagens-whatsapp.md
    error_message: |
      Para configurar as ferramentas e preparar o lançamento, precisamos do roteiro e das mensagens.
      Faltam: {lista dos artefatos ausentes}.
      Use *construir para gerar o conteúdo necessário.
```

## Execution Steps

### Step 1: Validar Pré-requisitos de Conteúdo

1. Determinar rodada ativa
2. Verificar existência dos artefatos obrigatórios em `docs/webinar/rodada-{N}/conteudo/`:
   - `roteiro-completo.md` (OBRIGATÓRIO)
   - `mensagens-whatsapp.md` (OBRIGATÓRIO)

3. Se algum estiver faltando:
   - Informar quais artefatos estão faltando
   - Explicar: "O roteiro é o conteúdo que vai no webinário, e as mensagens são o que vai ser enviado pelo WhatsApp. Sem eles, não temos o que configurar nas ferramentas."
   - Sugerir: "Use `*construir` para gerar o conteúdo, ou ative `@webinar-creator` diretamente."
   - **HALT** — não prosseguir sem os pré-requisitos

4. Verificar artefatos opcionais que enriquecem a execução:
   - `orcamento-meta.md` — enriquece timeline com investimento e datas
   - `copy-pagina-captura.md` — necessário para setup do EverWebinar
   - Informar disponibilidade (sem bloquear)

### Step 2: Verificar Estado da Execução

Verificar existência de cada artefato em `docs/webinar/rodada-{N}/execucao/`:

| # | Artefato | Arquivo | Input Principal |
|---|----------|---------|----------------|
| 1 | Guia EverWebinar | `guia-everwebinar.md` | roteiro-completo, copy-captura |
| 2 | Guia SendFlow | `guia-sendflow.md` | mensagens-whatsapp |
| 3 | Guia Pagamento | `guia-pagamento.md` | canvas-produto (ticket) |
| 4 | Guia Pixel | `guia-pixel.md` | instrucional |
| 5 | Timeline da Campanha | `timeline-campanha.md` | roteiro + mensagens |
| 6 | Funil de 7 Etapas | `funil-7-etapas.md` | instrucional (metodologia) |
| 7 | Checklist de Lançamento | `checklist-lancamento.md` | todos os artefatos |

Criar diretório `docs/webinar/rodada-{N}/execucao/` se não existir.

### Step 3: Apresentar Visão Geral da Fase

**Elicitation Point** (`elicit: true`)

```
🚀 Fase de Execução — Rodada {N}

Nesta fase, configuramos todas as ferramentas e preparamos o lançamento.
Cada guia é um passo-a-passo para configurar a ferramenta correspondente.

1. 📹 **EverWebinar** — Configurar o webinário (vídeo, agendamento, chat simulado)
2. 📱 **SendFlow** — Configurar automação de WhatsApp (grupos, fases, mensagens)
3. 💳 **Pagamento** — Configurar webhooks de pagamento (Zouti, Hotmart, Kiwify)
4. 📊 **Pixel** — Configurar Facebook Pixel e tracking
5. 📅 **Timeline** — Cronograma completo da campanha com datas reais
6. 🔄 **Funil** — Visualizar as 7 etapas do funil com status
7. ✅ **Checklist** — Verificação final antes de lançar

Status atual:
  ✅/⬜ Guia EverWebinar
  ✅/⬜ Guia SendFlow
  ✅/⬜ Guia Pagamento
  ✅/⬜ Guia Pixel
  ✅/⬜ Timeline da Campanha
  ✅/⬜ Funil de 7 Etapas
  ✅/⬜ Checklist de Lançamento
```

**Ordem recomendada:** EverWebinar → SendFlow → Pagamento → Pixel → Timeline → Funil → Checklist

> **Nota:** Os guias podem ser gerados em qualquer ordem, mas a timeline e o checklist ficam mais completos se gerados por último.

### Step 4: Identificar Próxima Configuração Pendente

| Prioridade | Artefato | Comando @webinar-operator |
|------------|----------|---------------------------|
| 1 | Guia EverWebinar | `*setup-everwebinar` |
| 2 | Guia SendFlow | `*setup-sendflow` |
| 3 | Guia Pagamento | `*setup-pagamento` |
| 4 | Guia Pixel | `*setup-pixel` |
| 5 | Timeline da Campanha | `*timeline` |
| 6 | Funil de 7 Etapas | `*funil` |
| 7 | Checklist de Lançamento | `*checklist` |

Se todos estiverem gerados:
- Informar: "Configuração completa! Tudo pronto para o lançamento."
- Sugerir: "Revise o checklist de lançamento e, após executar a campanha, use `*analisar` para revisar os resultados."

### Step 5: Orientar e Fazer Handoff

**Elicitation Point** (`elicit: true`)

```
O próximo passo é gerar o {guia pendente}.

Opções:
1. Gerar o {guia pendente} agora (recomendado)
2. Escolher outro guia para gerar
3. Ver o que cada guia contém
4. Voltar ao menu principal

O que prefere?
```

**Handoff artifact:**

```yaml
handoff:
  from_agent: "webinar"
  to_agent: "webinar-operator"
  story_context:
    project: "webinar"
    rodada: {N}
    phase: "execucao"
    current_task: "{guia escolhido}"
    content_artifacts:
      - "docs/webinar/rodada-{N}/conteudo/roteiro-completo.md"
      - "docs/webinar/rodada-{N}/conteudo/mensagens-whatsapp.md"
    planning_artifacts:
      - "docs/webinar/rodada-{N}/planejamento/canvas-produto.md"
  decisions:
    - "Pré-requisitos de conteúdo validados"
    - "Usuário optou por gerar: {guia}"
  files_modified: []
  blockers: []
  next_action: "*{comando correspondente}"
```

### Step 6: Atualizar progress.md

Atualizar `docs/webinar/progress.md` com:
- Fase atual: "Executar"
- Status dos artefatos de execução
- Último acesso

## Post-Conditions

```yaml
post-conditions:
  - [ ] Pré-requisitos validados
    tipo: post-condition
    blocker: false
    validacao: Usuário informado sobre estado dos pré-requisitos.
    error_message: "Falha na validação."
  - [ ] Handoff preparado para @webinar-operator (se aplicável)
    tipo: post-condition
    blocker: false
    validacao: Handoff artifact criado com contexto dos artefatos de conteúdo.
    error_message: "Handoff não criado."
```

## Error Handling

### Error 1: Pré-requisitos não atendidos

```yaml
error: CONTENT_PREREQUISITES_MISSING
cause: Roteiro ou mensagens não encontrados
resolution: Redirecionar para *construir ou @webinar-creator
recovery: "Use *construir para gerar o conteúdo necessário."
```

## Handoff

```yaml
next_agent: "@webinar-operator"
next_command: "*setup-everwebinar | *setup-sendflow | *setup-pagamento | *setup-pixel | *timeline | *funil | *checklist"
condition: Pré-requisitos de conteúdo atendidos e usuário escolheu guia
alternatives:
  - agent: "@webinar-creator", command: "*roteiro", condition: "Pré-requisitos não atendidos"
  - agent: "@webinar-analyst", command: "*kpis", condition: "Execução completa"
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
  - executar
  - routing
  - handoff
```
