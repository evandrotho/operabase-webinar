---
tools: []
checklists: []
execution_mode: interactive
---

# webinar-operator-setup-pagamento

Guia passo-a-passo para configurar webhooks de pagamento e acoes automaticas.

## Purpose

Orientar o usuario na configuracao de webhooks de pagamento com plataformas como Zouti, Hotmart e Kiwify. Inclui os 8 eventos de pagamento, acoes automaticas (remover de grupo, enviar mensagem, aplicar tag, black list) e integracao com SendFlow.

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "integracoes-webhooks"
      lines: "L3598-L3735"
      purpose: "Integracoes e Webhooks: 8 eventos (venda, abandono, boleto, chargeback, PIX, reembolso), acoes automaticas"
    - id: "stack-tecnica"
      lines: "L3736-L3758"
      purpose: "Stack tecnica completa: ferramentas e como se conectam"
    - id: "segmentacao-tags"
      lines: "L3759-L3829"
      purpose: "Segmentacao e tags para automacao baseada em eventos"
```

## Prerequisites

```yaml
prerequisites:
  required:
    - artifact: "docs/webinar/rodada-{N}/planejamento/canvas-produto.md"
      description: "Canvas do Produto (ticket, condicoes de pagamento)"
      if_missing: "Para configurar webhooks de pagamento, preciso saber o ticket e condicoes. Quer ativar o @webinar-strategist com *canvas-produto?"
  optional: []
```

## Task Definition

```yaml
task: setupPagamento()
responsavel: Atlas (Executor)
responsavel_type: Agente
elicit: true

Entrada:
- campo: canvas_produto
  tipo: file
  origem: "docs/webinar/rodada-{N}/planejamento/canvas-produto.md"
  obrigatorio: true
  validacao: Arquivo deve existir com informacoes de ticket e condicoes

Saida:
- campo: guia_pagamento
  tipo: file
  destino: "docs/webinar/rodada-{N}/execucao/guia-pagamento.md"
  persistido: true
  template: webinar-guia-setup-tmpl.md
```

## SEQUENTIAL Task Execution

### 0. Validar Pre-requisitos

- Verificar se `canvas-produto.md` existe
- Se nao existir, redirecionar para @webinar-strategist
- Carregar knowledge base: L3598-L3735, L3736-L3758, L3759-L3829

### 1. Elicitar Plataforma de Pagamento

**ELICIT (pergunta 1 de cada vez):**

1. "Qual plataforma de pagamento voce usa para vender seu produto?
   1. **Zouti**
   2. **Hotmart**
   3. **Kiwify**
   4. **Outra** (qual?)"
2. "Voce ja tem o produto cadastrado nessa plataforma com checkout configurado?"
3. "Voce tem order bump, upsell ou downsell configurados? Se sim, quais?"
4. "Quais formas de pagamento estao habilitadas? (Cartao, PIX, Boleto)"

### 2. Gerar Guia dos 8 Eventos de Webhook

Baseado na knowledge base (L3598-L3735), documentar cada evento:

| # | Evento | O que acontece | Acao automatica recomendada |
|---|--------|----------------|----------------------------|
| 1 | **Venda aprovada** | Pagamento confirmado | Remover do grupo de vendas, adicionar ao grupo de alunos, enviar mensagem de boas-vindas |
| 2 | **Abandono de carrinho** | Iniciou checkout mas nao pagou | Enviar mensagem de lembrete no WhatsApp, aplicar tag "abandono" |
| 3 | **Boleto gerado** | Gerou boleto mas nao pagou | Enviar lembrete de pagamento, aplicar tag "boleto-pendente" |
| 4 | **Boleto pago** | Pagou o boleto | Mesma acao de venda aprovada |
| 5 | **PIX gerado** | Gerou PIX mas nao pagou | Enviar lembrete com QR code, aplicar tag "pix-pendente" |
| 6 | **PIX pago** | Pagou via PIX | Mesma acao de venda aprovada |
| 7 | **Chargeback** | Contestacao de pagamento | Remover acesso, aplicar tag "chargeback", notificar |
| 8 | **Reembolso** | Pediu reembolso | Remover acesso, aplicar tag "reembolso", mover para lista de nao-compradores |

### 3. Gerar Guia de Configuracao por Plataforma

Baseado na plataforma escolhida, gerar instrucoes especificas:

**Para cada plataforma:**
- Onde encontrar configuracoes de webhook
- Como adicionar URL do webhook do SendFlow
- Quais eventos ativar
- Como testar se o webhook esta funcionando
- Formato dos dados recebidos (JSON)

### 4. Gerar Guia de Acoes Automaticas no SendFlow

- **Mapeamento evento -> acao:**
  - Para cada evento do webhook, configurar a acao correspondente no SendFlow
  - Passo-a-passo: criar automacao, definir trigger (webhook), definir acao
- **Tags automaticas:**
  - Lista de tags recomendadas: "comprador", "abandono", "boleto-pendente", "pix-pendente", "chargeback", "reembolso"
  - Como criar e aplicar tags no SendFlow
- **Black list:**
  - Quando adicionar a black list (chargeback, fraude)
  - Como configurar no SendFlow

### 5. Gerar Guia de Teste de Webhooks

- **Ambiente de teste:**
  - Como usar modo sandbox/teste da plataforma de pagamento
  - Como simular cada evento
  - Como verificar se a acao automatica foi executada
- **Checklist de teste:**
  - [ ] Venda aprovada -> lead removido do grupo de vendas
  - [ ] Abandono -> mensagem de lembrete enviada
  - [ ] Boleto gerado -> lembrete agendado
  - [ ] PIX -> lembrete com QR code
  - [ ] Chargeback -> acesso removido
  - [ ] Reembolso -> acesso removido

### 6. Compilar e Salvar Guia

- Usar template `webinar-guia-setup-tmpl.md` com ferramenta = plataforma escolhida + "SendFlow (Webhooks)"
- Preencher todas as secoes
- Salvar em `docs/webinar/rodada-{N}/execucao/guia-pagamento.md`

### 7. Sugerir Proximo Passo

- Se Pixel nao configurado: "Proximo passo: `*setup-pixel` para configurar rastreamento"
- Se ferramentas configuradas: "Proximo passo: `*timeline` para montar cronograma"

## Output

```yaml
output:
  path: "docs/webinar/rodada-{N}/execucao/guia-pagamento.md"
  template: webinar-guia-setup-tmpl.md
  format: markdown
  sections:
    - Informacoes do Projeto
    - Plataforma de Pagamento
    - Eventos de Webhook
    - Configuracao de Webhooks
    - Acoes Automaticas no SendFlow
    - Teste de Webhooks
    - Checklist de Verificacao
```

## Error Handling

**Strategy:** guide-and-retry

**Common Errors:**

1. **Error:** Canvas produto nao encontrado
   - **Resolution:** Redirecionar para @webinar-strategist com *canvas-produto
2. **Error:** Plataforma de pagamento nao suportada
   - **Resolution:** Orientar usuario sobre principios gerais de webhooks aplicaveis a qualquer plataforma
3. **Error:** Webhook nao dispara
   - **Resolution:** Verificar URL, formato, eventos ativados, testar com sandbox

## Handoff

```yaml
next_agent: "@webinar-operator"
next_command: "*setup-pixel"
condition: "Pagamento configurado, Pixel pendente"
alternatives:
  - agent: "@webinar-operator"
    command: "*timeline"
    condition: "Todas as ferramentas configuradas"
```
