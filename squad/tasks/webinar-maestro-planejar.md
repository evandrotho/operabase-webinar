---
task: webinar-maestro-planejar
responsavel: "@webinar"
responsavel_type: Agent
atomic_layer: Task
elicit: true

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: canvas-cliente-ideal
      lines: "L83-L140"
      purpose: "Canvas 1: Cliente Ideal — 9 perguntas (contexto para orientar o usuário)"
    - id: canvas-produto
      lines: "L141-L199"
      purpose: "Canvas 2: Produto — 7 blocos (contexto para orientar o usuário)"
    - id: canvas-webinar
      lines: "L200-L283"
      purpose: "Canvas 3: Webinário Infalível — 15 blocos"
    - id: canvas-orcamento
      lines: "L284-L338"
      purpose: "Canvas 4: Orçamento e Meta — 12 premissas"
    - id: avatar-blueprint
      lines: "L1722-L1866"
      purpose: "Avatar Blueprint — 7 perguntas + Tabela P×S"

inputs:
  required: []
  optional:
    - campo: rodada
      tipo: number
      origem: User Input
      obrigatorio: false
      validacao: "Número da rodada (default: rodada ativa ou 1 se projeto novo)"

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
  - "[ ] Step 1: Verificar estado do planejamento"
  - "[ ] Step 2: Apresentar visão geral da fase"
  - "[ ] Step 3: Identificar próximo canvas pendente"
  - "[ ] Step 4: Orientar e fazer handoff para @webinar-strategist"
  - "[ ] Step 5: Atualizar progress.md"
---

# Webinar Maestro — *planejar

## Purpose

Iniciar ou continuar a fase de planejamento do webinário. O Maestro avalia quais canvases já foram preenchidos, explica o que falta, e redireciona o usuário para o @webinar-strategist (Sage) que é o especialista em planejamento.

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] Estrutura docs/webinar/rodada-{N}/ acessível (criar se necessário)
    tipo: pre-condition
    blocker: false
    validacao: |
      Se a estrutura não existir, criar diretórios necessários.
    error_message: "Criando estrutura de pastas para a rodada."
```

## Execution Steps

### Step 1: Verificar Estado do Planejamento

1. Determinar rodada ativa (ler `docs/webinar/progress.md` ou usar rodada 1 se projeto novo)
2. Verificar existência de cada artefato de planejamento em `docs/webinar/rodada-{N}/planejamento/`:
   - `canvas-cliente-ideal.md`
   - `canvas-produto.md`
   - `canvas-webinar.md`
   - `avatar-blueprint.md`
   - `orcamento-meta.md`
   - `planejamento-resumo.md`
3. Criar diretório `docs/webinar/rodada-{N}/planejamento/` se não existir

### Step 2: Apresentar Visão Geral da Fase

**Elicitation Point** (`elicit: true`)

Explicar ao usuário em linguagem simples:

```
📋 Fase de Planejamento — Rodada {N}

O planejamento é a fundação do seu webinário. Nesta fase, vamos definir:

1. 👤 **Cliente Ideal** — Quem é seu público, suas dores e desejos
2. 📦 **Produto** — Sua grande promessa, mecanismo único e proposta de valor
3. 🎯 **Webinário** — Estrutura, tema, crença-alvo, oferta e objeções
4. 🧠 **Avatar Blueprint** — Mapa profundo do seu cliente ideal
5. 💰 **Orçamento e Meta** — Números, metas de vendas e investimento em mídia
6. 📊 **Resumo** — Consolidação de tudo (gerado automaticamente)

Status atual:
  ✅/⬜ Canvas do Cliente Ideal
  ✅/⬜ Canvas do Produto
  ✅/⬜ Canvas do Webinário
  ✅/⬜ Avatar Blueprint
  ✅/⬜ Orçamento e Meta
  ✅/⬜ Resumo de Planejamento
```

**Ordem recomendada:** Cliente Ideal → Produto → Avatar Blueprint → Canvas do Webinário → Orçamento → Resumo

> **Nota:** O Canvas do Cliente Ideal e o Canvas do Produto podem ser feitos independentemente. O Avatar Blueprint precisa do Canvas do Cliente Ideal. O Canvas do Webinário precisa do Produto e do Avatar. O Orçamento pode ser feito a qualquer momento. O Resumo requer todos os anteriores.

### Step 3: Identificar Próximo Canvas Pendente

Seguindo a ordem recomendada, identificar o primeiro canvas não preenchido:

| Prioridade | Canvas | Pré-requisitos | Comando @webinar-strategist |
|------------|--------|----------------|----------------------------|
| 1 | Cliente Ideal | Nenhum | `*canvas-cliente` |
| 2 | Produto | Nenhum (enriquecido por Cliente Ideal) | `*canvas-produto` |
| 3 | Avatar Blueprint | Cliente Ideal | `*avatar` |
| 4 | Canvas do Webinário | Produto + Avatar Blueprint | `*canvas-webinar` |
| 5 | Orçamento e Meta | Nenhum obrigatório (enriquecido por Produto) | `*orcamento` |
| 6 | Resumo | Todos os anteriores | `*resumo` |

Se todos estiverem preenchidos:
- Informar: "Planejamento completo! Todos os canvases foram preenchidos."
- Sugerir: "Quer revisar algum canvas ou avançar para a construção do conteúdo com `*construir`?"

### Step 4: Orientar e Fazer Handoff

**Elicitation Point** (`elicit: true`)

Apresentar as opções ao usuário:

```
O próximo passo é preencher o {nome do canvas pendente}.

Opções:
1. Preencher o {canvas pendente} agora (recomendado)
2. Escolher outro canvas para preencher
3. Ver o que cada canvas contém antes de decidir
4. Voltar ao menu principal

O que prefere?
```

Aguardar resposta do usuário.

**Após o usuário escolher:**

1. Se escolheu preencher: Criar handoff artifact e orientar a ativar `@webinar-strategist`
2. Se escolheu outro canvas: Listar opções disponíveis e fazer handoff para o comando correspondente
3. Se quer detalhes: Explicar brevemente cada canvas usando o conhecimento da knowledge_base
4. Se quer voltar: Encerrar task

**Handoff artifact:**

```yaml
handoff:
  from_agent: "webinar"
  to_agent: "webinar-strategist"
  story_context:
    project: "webinar"
    rodada: {N}
    phase: "planejamento"
    current_task: "{canvas escolhido}"
  decisions:
    - "Usuário optou por preencher: {canvas}"
  files_modified: []
  blockers: []
  next_action: "*{comando correspondente}"
```

### Step 5: Atualizar progress.md

Atualizar `docs/webinar/progress.md` com:
- Fase atual: "Planejar"
- Rodada ativa: {N}
- Último acesso: data/hora
- Status dos artefatos de planejamento

## Post-Conditions

```yaml
post-conditions:
  - [ ] Usuário informado sobre estado do planejamento
    tipo: post-condition
    blocker: false
    validacao: |
      Usuário recebeu visão clara do que já foi feito e do que falta.
    error_message: "Falha ao exibir estado do planejamento."
  - [ ] Handoff preparado para @webinar-strategist (se usuário decidiu continuar)
    tipo: post-condition
    blocker: false
    validacao: |
      Handoff artifact criado em .aiox/handoffs/ com contexto adequado.
    error_message: "Handoff não foi necessário — usuário optou por voltar."
```

## Error Handling

### Error 1: Pré-requisitos de canvas não atendidos

```yaml
error: PREREQUISITE_MISSING
cause: Usuário quer preencher um canvas que depende de outro ainda não preenchido
resolution: |
  Informar qual pré-requisito está faltando e sugerir preenchê-lo primeiro.
  Exemplo: "Para o Canvas do Webinário, precisamos primeiro do Canvas do Produto e do Avatar Blueprint."
recovery: Redirecionar para o canvas pré-requisito
```

### Error 2: Rodada inexistente

```yaml
error: ROUND_NOT_FOUND
cause: Usuário especificou rodada que não existe
resolution: Criar estrutura da rodada ou orientar qual rodada usar
recovery: Listar rodadas existentes e perguntar se quer criar nova
```

## Handoff

```yaml
next_agent: "@webinar-strategist"
next_command: "*canvas-cliente | *canvas-produto | *canvas-webinar | *avatar | *orcamento | *resumo"
condition: Usuário escolheu preencher um canvas
alternatives:
  - agent: "@webinar-creator", command: "*roteiro", condition: "Planejamento completo, quer construir"
  - agent: "@webinar", command: "*status", condition: "Usuário quer voltar ao menu"
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
  - planejar
  - routing
  - handoff
```
