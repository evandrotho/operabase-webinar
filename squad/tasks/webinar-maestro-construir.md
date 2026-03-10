---
task: webinar-maestro-construir
responsavel: "@webinar"
responsavel_type: Agent
atomic_layer: Task
elicit: true

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: abertura
      lines: "L1867-L2039"
      purpose: "Abertura do webinário — 7 blocos (contexto geral para orientar)"
    - id: empatia
      lines: "L2040-L2251"
      purpose: "Empatia/História + Epiphany Bridge (contexto geral)"
    - id: conteudo
      lines: "L2252-L2471"
      purpose: "Conteúdo — 3 Secrets + False Beliefs (contexto geral)"
    - id: pitch
      lines: "L2472-L2832"
      purpose: "Pitch/Oferta — 15 etapas + Stack Slide (contexto geral)"
    - id: timeline-webinar
      lines: "L2833-L2956"
      purpose: "Timeline completa do webinário (referência)"

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
  - "[ ] Step 1: Validar pré-requisitos de planejamento"
  - "[ ] Step 2: Verificar estado da construção"
  - "[ ] Step 3: Apresentar visão geral da fase"
  - "[ ] Step 4: Identificar próximo artefato pendente"
  - "[ ] Step 5: Orientar e fazer handoff para @webinar-creator"
  - "[ ] Step 6: Atualizar progress.md"
---

# Webinar Maestro — *construir

## Purpose

Iniciar ou continuar a fase de construção de conteúdo do webinário. O Maestro valida se os pré-requisitos de planejamento estão atendidos, mostra o estado dos artefatos de conteúdo, e redireciona para o @webinar-creator (Spark).

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] Canvases de planejamento obrigatórios preenchidos
    tipo: pre-condition
    blocker: true
    validacao: |
      Verificar existência de:
      - docs/webinar/rodada-{N}/planejamento/canvas-cliente-ideal.md
      - docs/webinar/rodada-{N}/planejamento/canvas-produto.md
      - docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md
      - docs/webinar/rodada-{N}/planejamento/canvas-webinar.md
    error_message: |
      Para construir o conteúdo, precisamos dos canvases de planejamento preenchidos.
      Faltam: {lista dos canvases ausentes}.
      Use *planejar para preencher o que falta.
```

## Execution Steps

### Step 1: Validar Pré-requisitos de Planejamento

1. Determinar rodada ativa
2. Verificar existência dos 4 canvases obrigatórios em `docs/webinar/rodada-{N}/planejamento/`:
   - `canvas-cliente-ideal.md` (OBRIGATÓRIO)
   - `canvas-produto.md` (OBRIGATÓRIO)
   - `avatar-blueprint.md` (OBRIGATÓRIO)
   - `canvas-webinar.md` (OBRIGATÓRIO)

3. Se algum estiver faltando:
   - Informar quais canvases estão faltando
   - Explicar por que cada um é necessário para a construção
   - Sugerir: "Use `*planejar` para preencher o que falta, ou ative `@webinar-strategist` diretamente."
   - **HALT** — não prosseguir sem os pré-requisitos

4. Verificar artefatos opcionais que enriquecem a construção:
   - `orcamento-meta.md` — enriquece mensagens com valores, datas, condições
   - Informar se disponível ou não (sem bloquear)

### Step 2: Verificar Estado da Construção

Verificar existência de cada artefato de conteúdo em `docs/webinar/rodada-{N}/conteudo/`:

| # | Artefato | Arquivo | Pré-req Específico |
|---|----------|---------|-------------------|
| 1 | Roteiro — Abertura | `roteiro-abertura.md` | avatar-blueprint, canvas-produto |
| 2 | Roteiro — Empatia | `roteiro-empatia.md` | avatar-blueprint |
| 3 | Roteiro — Conteúdo | `roteiro-conteudo.md` | avatar-blueprint, canvas-webinar (blocos 10-11) |
| 4 | Roteiro — Pitch | `roteiro-pitch.md` | canvas-webinar (blocos 12-15), canvas-produto |
| 5 | Roteiro Completo | `roteiro-completo.md` | Todos os 4 roteiros acima |
| 6 | Mensagens WhatsApp | `mensagens-whatsapp.md` | canvas-produto, avatar-blueprint |
| 7 | Copy — Captura | `copy-pagina-captura.md` | canvas-produto, avatar-blueprint |
| 8 | Copy — Replay | `copy-pagina-replay.md` | roteiro-completo, canvas-webinar |
| 9 | Copy — Fechamento | `copy-pagina-fechamento.md` | canvas-webinar (blocos 12-15), canvas-produto |

Criar diretório `docs/webinar/rodada-{N}/conteudo/` se não existir.

### Step 3: Apresentar Visão Geral da Fase

**Elicitation Point** (`elicit: true`)

```
🔨 Fase de Construção — Rodada {N}

Nesta fase, transformamos o planejamento em conteúdo pronto para uso.
O roteiro do webinário segue a estrutura Black Box:

1. 🎤 **Abertura** (5-10min) — Headline, método, apresentação, lista, urgência
2. 💜 **Empatia** (5-10min) — Sua história de transformação
3. 📚 **Conteúdo** (25-40min) — 3 Segredos que quebram falsas crenças
4. 💰 **Pitch** (20-30min) — Apresentação da oferta, stack, garantia, CTA

Além do roteiro, geramos:
5. 📱 **Mensagens WhatsApp** — 41+ templates para todo o funil
6. 📄 **Copy de Páginas** — Captura, replay e fechamento

Status atual:
  ✅/⬜ Roteiro — Abertura
  ✅/⬜ Roteiro — Empatia
  ✅/⬜ Roteiro — Conteúdo
  ✅/⬜ Roteiro — Pitch
  ✅/⬜ Roteiro Completo
  ✅/⬜ Mensagens WhatsApp
  ✅/⬜ Copy — Captura
  ✅/⬜ Copy — Replay
  ✅/⬜ Copy — Fechamento
```

**Ordem recomendada:** Abertura → Empatia → Conteúdo → Pitch → Roteiro Completo → Mensagens → Copy das páginas

### Step 4: Identificar Próximo Artefato Pendente

Seguindo a ordem recomendada, identificar o primeiro artefato não gerado:

| Prioridade | Artefato | Comando @webinar-creator |
|------------|----------|--------------------------|
| 1 | Roteiro — Abertura | `*abertura` |
| 2 | Roteiro — Empatia | `*empatia` |
| 3 | Roteiro — Conteúdo | `*conteudo` |
| 4 | Roteiro — Pitch | `*pitch` |
| 5 | Roteiro Completo | `*roteiro` |
| 6 | Mensagens WhatsApp | `*mensagens` |
| 7 | Copy — Captura | `*copy-captura` |
| 8 | Copy — Replay | `*copy-replay` |
| 9 | Copy — Fechamento | `*copy-fechamento` |

Se todos estiverem gerados:
- Informar: "Construção completa! Todo o conteúdo foi gerado."
- Sugerir: "Quer revisar algum artefato ou avançar para a execução com `*executar`?"

### Step 5: Orientar e Fazer Handoff

**Elicitation Point** (`elicit: true`)

```
O próximo passo é criar o {artefato pendente}.

Opções:
1. Criar o {artefato pendente} agora (recomendado)
2. Escolher outro artefato para criar
3. Ver o que cada artefato contém
4. Voltar ao menu principal

O que prefere?
```

**Após o usuário escolher:**

Criar handoff artifact:

```yaml
handoff:
  from_agent: "webinar"
  to_agent: "webinar-creator"
  story_context:
    project: "webinar"
    rodada: {N}
    phase: "conteudo"
    current_task: "{artefato escolhido}"
    planning_artifacts:
      - "docs/webinar/rodada-{N}/planejamento/canvas-cliente-ideal.md"
      - "docs/webinar/rodada-{N}/planejamento/canvas-produto.md"
      - "docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md"
      - "docs/webinar/rodada-{N}/planejamento/canvas-webinar.md"
  decisions:
    - "Pré-requisitos de planejamento validados"
    - "Usuário optou por criar: {artefato}"
  files_modified: []
  blockers: []
  next_action: "*{comando correspondente}"
```

Orientar: "Ative o `@webinar-creator` e use o comando `*{comando}` para começar."

### Step 6: Atualizar progress.md

Atualizar `docs/webinar/progress.md` com:
- Fase atual: "Construir"
- Status dos artefatos de conteúdo
- Último acesso

## Post-Conditions

```yaml
post-conditions:
  - [ ] Pré-requisitos validados e informados ao usuário
    tipo: post-condition
    blocker: false
    validacao: |
      Usuário foi informado se os pré-requisitos estão ou não atendidos.
    error_message: "Falha na validação de pré-requisitos."
  - [ ] Handoff preparado para @webinar-creator (se aplicável)
    tipo: post-condition
    blocker: false
    validacao: |
      Handoff artifact criado com contexto dos artefatos de planejamento.
    error_message: "Handoff não criado — pré-requisitos não atendidos ou usuário optou por voltar."
```

## Error Handling

### Error 1: Pré-requisitos não atendidos

```yaml
error: PLANNING_PREREQUISITES_MISSING
cause: Canvases obrigatórios de planejamento não encontrados
resolution: |
  Listar quais canvases estão faltando.
  Redirecionar para *planejar ou @webinar-strategist.
recovery: "Use *planejar para preencher os canvases necessários."
```

### Error 2: Artefato parcialmente gerado

```yaml
error: ARTIFACT_INCOMPLETE
cause: Artefato existe mas pode estar incompleto
resolution: |
  Informar ao usuário e perguntar se quer regenerar ou continuar.
recovery: Oferecer opção de regenerar via @webinar-creator
```

## Handoff

```yaml
next_agent: "@webinar-creator"
next_command: "*abertura | *empatia | *conteudo | *pitch | *roteiro | *mensagens | *copy-captura | *copy-replay | *copy-fechamento"
condition: Pré-requisitos de planejamento atendidos e usuário escolheu artefato
alternatives:
  - agent: "@webinar-strategist", command: "*canvas-cliente", condition: "Pré-requisitos não atendidos"
  - agent: "@webinar-operator", command: "*setup-everwebinar", condition: "Construção completa"
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
  - construir
  - routing
  - handoff
```
