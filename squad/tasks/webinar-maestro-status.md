---
task: webinar-maestro-status
responsavel: "@webinar"
responsavel_type: Agent
atomic_layer: Task
elicit: true

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: espiral-vendas-visao-geral
      lines: "L22-L80"
      purpose: "Visão geral da Espiral de Vendas — contexto das 4 fases"
    - id: dinamica-sequencia-execucao
      lines: "L63-L80"
      purpose: "Sequência de execução — para orientar próximo passo"

inputs:
  required: []
  optional:
    - campo: rodada
      tipo: number
      origem: User Input
      obrigatorio: false
      validacao: "Número da rodada (default: rodada ativa ou mais recente)"

output:
  - campo: status_display
    tipo: string
    destino: Console (display to user)
    persistido: false
  - campo: progress_file
    tipo: file
    destino: docs/webinar/progress.md
    persistido: true

Checklist:
  - "[ ] Step 1: Verificar existência de docs/webinar/"
  - "[ ] Step 2: Ler progress.md ou criar se não existir"
  - "[ ] Step 3: Escanear artefatos por fase/rodada"
  - "[ ] Step 4: Exibir resumo visual ao usuário"
  - "[ ] Step 5: Sugerir próximo passo"
---

# Webinar Maestro — *status

## Purpose

Mostrar ao usuário o progresso completo do projeto de webinário: quais artefatos já foram gerados, quais estão pendentes, em qual fase e rodada o projeto se encontra, e qual é o próximo passo recomendado.

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] Diretório docs/webinar/ acessível (será criado se não existir)
    tipo: pre-condition
    blocker: false
    validacao: |
      Se docs/webinar/ não existir, considerar projeto novo e criar estrutura inicial.
    error_message: "Nenhum problema — projeto novo detectado."
```

## Execution Steps

### Step 1: Verificar Estrutura do Projeto

1. Verificar se `docs/webinar/` existe
2. Se NÃO existir:
   - Informar: "Projeto novo — nenhum webinário em andamento."
   - Criar diretório `docs/webinar/`
   - Criar `docs/webinar/progress.md` usando template `webinar-progress-tmpl.md` com valores iniciais
   - Pular para Step 5 (sugerir começar pelo planejamento)
3. Se existir: continuar para Step 2

### Step 2: Ler Estado Atual

1. Ler `docs/webinar/progress.md`
2. Identificar:
   - Rodada ativa (rodada-{N})
   - Fase atual (Planejar/Construir/Executar/Analisar)
   - Data de última atualização

### Step 3: Escanear Artefatos por Fase

Para a rodada ativa (ou rodada especificada pelo usuário), verificar a existência de cada artefato esperado:

**Fase: Planejar** (`docs/webinar/rodada-{N}/planejamento/`)

| # | Artefato | Arquivo | Status |
|---|----------|---------|--------|
| 1 | Canvas do Cliente Ideal | `canvas-cliente-ideal.md` | Verificar |
| 2 | Canvas do Produto | `canvas-produto.md` | Verificar |
| 3 | Canvas do Webinário | `canvas-webinar.md` | Verificar |
| 4 | Avatar Blueprint | `avatar-blueprint.md` | Verificar |
| 5 | Orçamento e Meta | `orcamento-meta.md` | Verificar |
| 6 | Resumo de Planejamento | `planejamento-resumo.md` | Verificar |

**Fase: Construir** (`docs/webinar/rodada-{N}/conteudo/`)

| # | Artefato | Arquivo | Status |
|---|----------|---------|--------|
| 1 | Roteiro — Abertura | `roteiro-abertura.md` | Verificar |
| 2 | Roteiro — Empatia | `roteiro-empatia.md` | Verificar |
| 3 | Roteiro — Conteúdo | `roteiro-conteudo.md` | Verificar |
| 4 | Roteiro — Pitch | `roteiro-pitch.md` | Verificar |
| 5 | Roteiro Completo | `roteiro-completo.md` | Verificar |
| 6 | Mensagens WhatsApp | `mensagens-whatsapp.md` | Verificar |
| 7 | Copy — Página de Captura | `copy-pagina-captura.md` | Verificar |
| 8 | Copy — Página de Replay | `copy-pagina-replay.md` | Verificar |
| 9 | Copy — Página de Fechamento | `copy-pagina-fechamento.md` | Verificar |

**Fase: Executar** (`docs/webinar/rodada-{N}/execucao/`)

| # | Artefato | Arquivo | Status |
|---|----------|---------|--------|
| 1 | Guia EverWebinar | `guia-everwebinar.md` | Verificar |
| 2 | Guia SendFlow | `guia-sendflow.md` | Verificar |
| 3 | Guia Pagamento | `guia-pagamento.md` | Verificar |
| 4 | Guia Pixel | `guia-pixel.md` | Verificar |
| 5 | Timeline da Campanha | `timeline-campanha.md` | Verificar |
| 6 | Funil de 7 Etapas | `funil-7-etapas.md` | Verificar |
| 7 | Checklist de Lançamento | `checklist-lancamento.md` | Verificar |

**Fase: Analisar** (`docs/webinar/rodada-{N}/analise/`)

| # | Artefato | Arquivo | Status |
|---|----------|---------|--------|
| 1 | Relatório de KPIs | `relatorio-kpis.md` | Verificar |
| 2 | Diagnóstico do Funil | `diagnostico-funil.md` | Verificar |
| 3 | Orçado vs. Realizado | `orcado-vs-realizado.md` | Verificar |
| 4 | Plano Próxima Rodada | `plano-proxima-rodada.md` | Verificar |

**Cross-rodada** (`docs/webinar/estrategias/`)

| # | Artefato | Arquivo | Status |
|---|----------|---------|--------|
| 1 | Estratégia de Empilhamento | `estrategia-empilhamento.md` | Verificar |
| 2 | Estratégia Perpétuo | `estrategia-perpetuo.md` | Verificar |

### Step 4: Exibir Resumo Visual

Apresentar ao usuário de forma clara e visual:

```
🎯 Status do Webinário — Rodada {N}

📋 PLANEJAR (X de 6 artefatos)
  ✅ Canvas do Cliente Ideal
  ✅ Canvas do Produto
  ⬜ Canvas do Webinário
  ⬜ Avatar Blueprint
  ⬜ Orçamento e Meta
  ⬜ Resumo de Planejamento

🔨 CONSTRUIR (X de 9 artefatos)
  ⬜ Roteiro — Abertura
  ... (listar todos)

🚀 EXECUTAR (X de 7 artefatos)
  ⬜ Guia EverWebinar
  ... (listar todos)

📊 ANALISAR (X de 4 artefatos)
  ⬜ Relatório de KPIs
  ... (listar todos)

Progresso geral: X de 26 artefatos (XX%)
```

### Step 5: Sugerir Próximo Passo

**Elicitation Point** (`elicit: true`)

Com base no estado atual, sugerir a próxima ação:

1. **Nenhum artefato:** "Vamos começar pelo planejamento! Use `*planejar` ou ative `@webinar-strategist` para preencher o primeiro canvas."
2. **Planejamento incompleto:** "Ainda faltam canvases no planejamento. O próximo é: {canvas pendente}. Use `*planejar` para continuar."
3. **Planejamento completo, conteúdo vazio:** "Planejamento concluído! Hora de construir o conteúdo. Use `*construir` ou ative `@webinar-creator`."
4. **Conteúdo incompleto:** "Faltam artefatos de conteúdo. O próximo é: {artefato pendente}. Use `*construir` para continuar."
5. **Conteúdo completo, execução vazia:** "Conteúdo pronto! Hora de configurar as ferramentas. Use `*executar` ou ative `@webinar-operator`."
6. **Execução incompleta:** "Faltam configurações. Use `*executar` para continuar."
7. **Execução completa, análise vazia:** "Tudo pronto para lançar! Após executar a campanha e coletar dados, use `*analisar` para revisar os resultados."
8. **Análise completa:** "Rodada {N} completa! Quer planejar a próxima rodada? Use `*planejar` para a rodada {N+1}."

Perguntar: "O que gostaria de fazer?"

### Step 6: Atualizar progress.md

Atualizar `docs/webinar/progress.md` com:
- Contagem atualizada de artefatos por fase
- Data/hora da última verificação
- Fase atual identificada

## Post-Conditions

```yaml
post-conditions:
  - [ ] Resumo de progresso exibido ao usuário
    tipo: post-condition
    blocker: false
    validacao: |
      Usuário recebeu informação clara sobre o estado do projeto.
    error_message: "Não foi possível exibir o status."
  - [ ] progress.md atualizado
    tipo: post-condition
    blocker: false
    validacao: |
      Arquivo progress.md reflete o estado atual dos artefatos.
    error_message: "Não foi possível atualizar progress.md."
```

## Error Handling

### Error 1: Diretório não encontrado

```yaml
error: DIRECTORY_NOT_FOUND
cause: docs/webinar/ não existe
resolution: Criar diretório e progress.md com valores iniciais
recovery: Tratar como projeto novo — orientar usuário a começar pelo planejamento
```

### Error 2: progress.md corrompido

```yaml
error: PROGRESS_FILE_CORRUPT
cause: progress.md existe mas não pode ser parseado
resolution: Recriar progress.md escaneando artefatos existentes
recovery: Reconstruir estado a partir dos arquivos encontrados no filesystem
```

## Handoff

```yaml
next_agent: Depende do estado
next_command: "*planejar | *construir | *executar | *analisar"
condition: Baseado na sugestão de próximo passo (Step 5)
alternatives:
  - agent: "@webinar-strategist", command: "*canvas-cliente", condition: "Projeto novo"
  - agent: "@webinar-creator", command: "*roteiro", condition: "Planejamento completo"
  - agent: "@webinar-operator", command: "*setup-everwebinar", condition: "Conteúdo completo"
  - agent: "@webinar-analyst", command: "*kpis", condition: "Campanha executada"
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
  - status
  - orchestration
```
