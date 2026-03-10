---
tools: []
checklists: []
execution_mode: interactive
---

# webinar-operator-setup-sendflow

Guia passo-a-passo para configurar o SendFlow para automacao de mensagens WhatsApp.

## Purpose

Orientar o usuario na configuracao completa do SendFlow: criacao de grupos/fases WhatsApp, cronograma de envio semanal, 8 tipos de acao, 4 triggers, deep links com Facebook Pixel, e transicao entre fases da campanha. O agente ENSINA o usuario a configurar, nao configura por ele.

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "sendflow-automacao-whatsapp"
      lines: "L3360-L3597"
      purpose: "Setup completo do SendFlow: 3 fases, cronograma semanal, 8 tipos de acao, 4 triggers, deep links, transicao entre fases"
    - id: "pilar-atracoes"
      lines: "L28-L34"
      purpose: "Pilar 1 da Espiral de Vendas: Atracao -- contexto de captacao"
    - id: "segmentacao-tags"
      lines: "L3759-L3829"
      purpose: "Segmentacao e tags: como organizar leads por comportamento"
    - id: "mapa-ferramentas"
      lines: "L1652-L1671"
      purpose: "Mapa consolidado de ferramentas"
```

## Prerequisites

```yaml
prerequisites:
  required:
    - artifact: "docs/webinar/rodada-{N}/conteudo/mensagens-whatsapp.md"
      description: "Biblioteca de 41+ mensagens WhatsApp (para carregar no SendFlow)"
      if_missing: "Para configurar o SendFlow, preciso das mensagens WhatsApp. Quer ativar o @webinar-creator com *mensagens?"
  optional:
    - artifact: "docs/webinar/rodada-{N}/execucao/timeline-campanha.md"
      description: "Timeline da campanha (para sincronizar datas de envio)"
      enriches: "Datas e horarios exatos de cada mensagem"
```

## Task Definition

```yaml
task: setupSendflow()
responsavel: Atlas (Executor)
responsavel_type: Agente
elicit: true

Entrada:
- campo: mensagens_whatsapp
  tipo: file
  origem: "docs/webinar/rodada-{N}/conteudo/mensagens-whatsapp.md"
  obrigatorio: true
  validacao: Arquivo deve existir e conter templates de mensagens

- campo: timeline_campanha
  tipo: file
  origem: "docs/webinar/rodada-{N}/execucao/timeline-campanha.md"
  obrigatorio: false

Saida:
- campo: guia_sendflow
  tipo: file
  destino: "docs/webinar/rodada-{N}/execucao/guia-sendflow.md"
  persistido: true
  template: webinar-guia-setup-tmpl.md
```

## SEQUENTIAL Task Execution

### 0. Validar Pre-requisitos

- Verificar se `mensagens-whatsapp.md` existe em `docs/webinar/rodada-{N}/conteudo/`
- Se nao existir, informar o usuario e redirecionar para @webinar-creator
- Carregar knowledge base: L3360-L3597, L3759-L3829, L1652-L1671

### 1. Elicitar Informacoes do SendFlow

**ELICIT (pergunta 1 de cada vez):**

1. "Voce ja tem uma conta ativa no SendFlow? Se sim, ja criou os grupos de WhatsApp para esta campanha?"
2. "Quantos numeros de WhatsApp voce tem disponiveis para envio? (1 numero = limite de ~1000 contatos por grupo)"
3. "Voce quer usar o modelo de **3 fases** da metodologia? Isso organiza os leads em:
   1. **Fase Pre** -- antes do webinario (captacao + nutricao + antecipacao)
   2. **Fase Pos** -- depois do webinario (ampliacao + fechamento)
   3. **Fase Conteudo** -- material extra / retargeting
   Recomendacao: Sim, usar 3 fases."
4. "Voce ja tem o Facebook Pixel configurado? (Necessario para deep links com rastreamento)"

### 2. Gerar Guia de Criacao de Grupos

Baseado na knowledge base (L3360-L3597):

- **Estrutura de grupos:**
  - Grupo Fase Pre: nome sugerido, descricao, imagem de capa
  - Grupo Fase Pos: nome sugerido, descricao, imagem de capa
  - Grupo Fase Conteudo: nome sugerido, descricao, imagem de capa
- **Configuracao de cada grupo:**
  - Passo-a-passo no SendFlow: criar grupo, definir nome, configurar imagem
  - Regras de moderacao (apenas admins postam vs. todos)
  - Link de convite vs. one-click add

### 3. Gerar Guia de Cronograma de Envio

- **Mapeamento mensagens -> fases:**
  - Ler `mensagens-whatsapp.md` e categorizar cada mensagem na fase correta
  - Nutricao (5 msgs) -> Fase Pre
  - Antecipacao D-1 (2 msgs) + D-0 (7 msgs) -> Fase Pre
  - Pos-webinario (1 msg) -> Fase Pos
  - Ampliacao (7 msgs) -> Fase Pos
  - Fechamento (11 msgs) -> Fase Pos
  - Downsell (8 msgs) -> Fase Pos ou Conteudo
- **Cronograma semanal:**
  - Se timeline existe: usar datas reais
  - Se nao: criar template relativo (D-7, D-6, ..., D-0, D+1, ..., D+7)
  - Horarios recomendados por tipo de mensagem (manha, tarde, noite)

### 4. Gerar Guia dos 8 Tipos de Acao

Baseado na knowledge base, documentar como configurar cada tipo:

1. **Mensagem de texto** -- como criar e agendar
2. **Mensagem com imagem** -- formato, tamanho, upload
3. **Mensagem com video** -- link ou upload
4. **Mensagem com audio** -- gravacao ou upload
5. **Mensagem com documento** -- PDF, etc.
6. **Mensagem com botao** -- CTA com link
7. **Mensagem com lista** -- opcoes de selecao
8. **Reacao automatica** -- resposta baseada em keyword

### 5. Gerar Guia dos 4 Triggers

- **Trigger de entrada:** Lead entra no grupo -> acao automatica (boas-vindas)
- **Trigger de tempo:** Agendar mensagem para data/hora especifica
- **Trigger de evento:** Baseado em acao do lead (clicou link, respondeu keyword)
- **Trigger de webhook:** Integracao com pagamento (comprou -> remove do grupo, adiciona em outro)

### 6. Gerar Guia de Deep Links com Pixel

Se usuario tem Pixel configurado:

- **O que sao deep links:** links que passam pelo Pixel antes de redirecionar
- **Como criar no SendFlow:** campo de URL, parametros UTM, integracao Pixel
- **Regra anti-duplicacao:** como evitar contar o mesmo lead duas vezes
- **Links por etapa:** captura, replay, checkout, pagina de vendas

### 7. Gerar Guia de Transicao entre Fases

- **Quando transicionar:**
  - Fase Pre -> Fase Pos: apos o webinario ser realizado
  - Fase Pos -> Fase Conteudo: apos fechamento do carrinho
- **Como transicionar no SendFlow:**
  - Mover leads entre grupos (manual vs. automatico)
  - Tags que ativam a transicao
  - Webhooks de pagamento que removem do grupo

### 8. Compilar e Salvar Guia

- Usar template `webinar-guia-setup-tmpl.md` com ferramenta = "SendFlow"
- Preencher todas as secoes
- Salvar em `docs/webinar/rodada-{N}/execucao/guia-sendflow.md`
- Resumo para o usuario

### 9. Sugerir Proximo Passo

- Se pagamento nao configurado: "Proximo passo: `*setup-pagamento` para integrar webhooks de pagamento"
- Se Pixel nao configurado: "Proximo passo: `*setup-pixel` para configurar o rastreamento"

## Output

```yaml
output:
  path: "docs/webinar/rodada-{N}/execucao/guia-sendflow.md"
  template: webinar-guia-setup-tmpl.md
  format: markdown
  sections:
    - Informacoes do Projeto
    - Estrutura de Grupos
    - Cronograma de Envio
    - Tipos de Acao
    - Triggers e Automacoes
    - Deep Links com Pixel
    - Transicao entre Fases
    - Checklist de Verificacao
```

## Error Handling

**Strategy:** guide-and-retry

**Common Errors:**

1. **Error:** Mensagens WhatsApp nao encontradas
   - **Resolution:** Redirecionar para @webinar-creator com *mensagens
2. **Error:** Usuario nao tem conta SendFlow
   - **Resolution:** Orientar sobre como criar conta e conectar numero de WhatsApp
3. **Error:** Limite de contatos por grupo
   - **Resolution:** Orientar sobre estrategia de multiplos numeros/grupos

## Handoff

```yaml
next_agent: "@webinar-operator"
next_command: "*setup-pagamento"
condition: "SendFlow configurado, pagamento pendente"
alternatives:
  - agent: "@webinar-operator"
    command: "*setup-pixel"
    condition: "Pagamento ja configurado, Pixel pendente"
  - agent: "@webinar-operator"
    command: "*timeline"
    condition: "Todas as ferramentas configuradas"
```
