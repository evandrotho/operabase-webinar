---
tools: []
checklists: []
execution_mode: interactive
---

# webinar-operator-setup-everwebinar

Guia passo-a-passo para configurar o EverWebinar com o conteudo do webinario.

## Purpose

Orientar o usuario na configuracao completa do EverWebinar: upload de video, agendamento (diario/semanal), one-click registration, chat simulado, eventos na timeline, replay e segmentacao. O agente NAO configura a ferramenta -- ele ENSINA o usuario a configurar, campo por campo.

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "everwebinar-setup-completo"
      lines: "L3123-L3359"
      purpose: "Setup completo do EverWebinar: video, agendamento, one-click, chat simulado, eventos, replay, segmentacao"
    - id: "etapa-4-abertura-carrinho"
      lines: "L891-L984"
      purpose: "Etapa 4 do funil: contexto de como o EverWebinar se encaixa na abertura do carrinho"
    - id: "mapa-ferramentas"
      lines: "L1652-L1671"
      purpose: "Mapa consolidado de ferramentas e onde cada uma se encaixa"
```

## Prerequisites

```yaml
prerequisites:
  required:
    - artifact: "docs/webinar/rodada-{N}/conteudo/roteiro-completo.md"
      description: "Roteiro completo do webinario (para configurar timeline de eventos)"
      if_missing: "Para configurar o EverWebinar, preciso do roteiro completo. Quer ativar o @webinar-creator com *roteiro?"
    - artifact: "docs/webinar/rodada-{N}/conteudo/copy-pagina-captura.md"
      description: "Copy da pagina de captura (para configurar pagina de registro)"
      if_missing: "Para configurar a pagina de registro, preciso da copy de captura. Quer ativar o @webinar-creator com *copy-captura?"
  optional:
    - artifact: "docs/webinar/rodada-{N}/planejamento/canvas-webinar.md"
      description: "Canvas do Webinario (formato, plataforma, duracao)"
      enriches: "Decisoes de agendamento e formato"
```

## Task Definition

```yaml
task: setupEverwebinar()
responsavel: Atlas (Executor)
responsavel_type: Agente
elicit: true

Entrada:
- campo: roteiro_completo
  tipo: file
  origem: "docs/webinar/rodada-{N}/conteudo/roteiro-completo.md"
  obrigatorio: true
  validacao: Arquivo deve existir e conter timeline do webinario

- campo: copy_captura
  tipo: file
  origem: "docs/webinar/rodada-{N}/conteudo/copy-pagina-captura.md"
  obrigatorio: true
  validacao: Arquivo deve existir

- campo: canvas_webinar
  tipo: file
  origem: "docs/webinar/rodada-{N}/planejamento/canvas-webinar.md"
  obrigatorio: false

Saida:
- campo: guia_everwebinar
  tipo: file
  destino: "docs/webinar/rodada-{N}/execucao/guia-everwebinar.md"
  persistido: true
  template: webinar-guia-setup-tmpl.md
```

## SEQUENTIAL Task Execution

### 0. Validar Pre-requisitos

- Verificar se `roteiro-completo.md` existe em `docs/webinar/rodada-{N}/conteudo/`
- Verificar se `copy-pagina-captura.md` existe
- Se nao existirem, informar o usuario e oferecer redirecionamento para @webinar-creator
- Carregar as secoes da knowledge base declaradas acima (L3123-L3359, L891-L984, L1652-L1671)

### 1. Elicitar Informacoes Basicas

**ELICIT (pergunta 1 de cada vez):**

1. "Voce ja tem o video do webinario gravado? Em qual plataforma ele esta hospedado? (Vimeo, YouTube, ou vai fazer upload direto no EverWebinar?)"
2. "Qual o formato de agendamento que deseja? Opcoes:
   1. **Diario** -- sessoes todos os dias (recomendado para inicio)
   2. **Semanal** -- dias especificos da semana
   3. **Just-in-Time** -- proxima sessao em 15 minutos (alta conversao)"
3. "Voce quer usar **One-Click Registration**? (O lead clica no email/WhatsApp e ja esta registrado, sem formulario. Recomendado para quem usa SendFlow.)"
4. "Quer configurar o **chat simulado**? (Mensagens pre-programadas que aparecem durante o webinario, simulando participacao ao vivo. A metodologia recomenda fortemente.)"

### 2. Gerar Guia de Configuracao do Video

Baseado na knowledge base (L3123-L3359), gerar instrucoes passo-a-passo para:

- **Upload/Embed do video:**
  - Se Vimeo: configurar privacidade, gerar link embed, colar no EverWebinar
  - Se YouTube: configurar como nao listado, gerar embed, colar no EverWebinar
  - Se upload direto: limites de tamanho, formatos aceitos
- **Configuracao de qualidade:** resolucao recomendada, bitrate, formato de arquivo

### 3. Gerar Guia de Agendamento

Baseado na resposta do usuario e knowledge base:

- **Configuracao do Schedule:**
  - Passo-a-passo para configurar o tipo escolhido (diario/semanal/JIT)
  - Timezone: orientar sobre fusos horarios para publico brasileiro
  - Horarios recomendados pela metodologia
- **One-Click Registration** (se escolhido):
  - Como ativar no EverWebinar
  - Como gerar links personalizados
  - Integracao com SendFlow (deep links)

### 4. Gerar Guia do Chat Simulado

Se o usuario optou por chat simulado:

- **Criacao de mensagens de chat:**
  - Baseado no roteiro: criar mensagens que acompanham cada secao
  - Timing: sincronizar com timeline do roteiro (Abertura 0-10min, Empatia 10-20min, etc.)
  - Tipos de mensagem: perguntas, reacoes, depoimentos simulados
  - Quantidade recomendada: 15-25 mensagens distribuidas
- **Configuracao no EverWebinar:**
  - Onde adicionar as mensagens
  - Como definir os timings
  - Nomes e avatares dos participantes simulados

### 5. Gerar Guia de Eventos na Timeline

Baseado no roteiro-completo.md:

- **Eventos de interacao:**
  - Enquetes (momento da Abertura -- identificacao)
  - Ofertas/CTAs (momento do Pitch -- quando mostrar botao de compra)
  - Alertas de escassez (Fechamento -- urgencia)
- **Configuracao de cada evento:**
  - Tipo, timing, duracao, texto, URL do CTA
  - Quando mostrar/esconder elementos

### 6. Gerar Guia de Replay e Segmentacao

- **Configuracao de replay:**
  - Quando disponibilizar (imediatamente apos? com delay?)
  - Duracao do acesso ao replay
  - Pagina de replay (referenciar copy-pagina-replay se existir)
- **Segmentacao:**
  - Eventos que geram tags (registrou, compareceu, assistiu X%, clicou no CTA, comprou)
  - Como configurar essas tags no EverWebinar
  - Integracao com SendFlow para automacao baseada em tags

### 7. Compilar e Salvar Guia

- Usar template `webinar-guia-setup-tmpl.md` com ferramenta = "EverWebinar"
- Preencher todas as secoes com as instrucoes geradas
- Salvar em `docs/webinar/rodada-{N}/execucao/guia-everwebinar.md`
- Mostrar resumo ao usuario: secoes configuradas, proximos passos

### 8. Sugerir Proximo Passo

- Se SendFlow nao configurado: "Proximo passo recomendado: `*setup-sendflow` para configurar a automacao de WhatsApp"
- Se ja configurado: "Proximo passo: `*timeline` para montar o cronograma completo"

## Output

```yaml
output:
  path: "docs/webinar/rodada-{N}/execucao/guia-everwebinar.md"
  template: webinar-guia-setup-tmpl.md
  format: markdown
  sections:
    - Informacoes do Projeto
    - Configuracao de Video
    - Configuracao de Agendamento
    - Chat Simulado (se aplicavel)
    - Eventos na Timeline
    - Replay e Segmentacao
    - Checklist de Verificacao
```

## Error Handling

**Strategy:** guide-and-retry

**Common Errors:**

1. **Error:** Roteiro completo nao encontrado
   - **Resolution:** Redirecionar para @webinar-creator com *roteiro
2. **Error:** Usuario nao tem acesso ao EverWebinar
   - **Resolution:** Orientar sobre como criar conta e plano necessario
3. **Error:** Video nao esta no formato correto
   - **Resolution:** Orientar sobre conversao de formato e resolucao recomendada

## Handoff

```yaml
next_agent: "@webinar-operator"
next_command: "*setup-sendflow"
condition: "EverWebinar configurado, SendFlow pendente"
alternatives:
  - agent: "@webinar-operator"
    command: "*timeline"
    condition: "Todas as ferramentas ja configuradas"
  - agent: "@webinar-operator"
    command: "*checklist"
    condition: "Timeline ja montada, pronto para verificacao final"
```
