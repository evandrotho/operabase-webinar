---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
- Agent asks all questions at once, generates document
- **Best for:** User already has voice defined

### 2. Interactive Mode - Balanced, Educational (4-6 prompts) **[DEFAULT]**
- One bloco at a time with exemplos
- **Best for:** First-time users discovering their voice

### 3. Pre-Flight Planning - Review Existing
- Load existing tom-de-voz, show what's defined, ask about updates
- **Best for:** Updating for next round based on feedback

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: tomDeVozExpert()
responsável: Sage (Strategist)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "glossario"
      lines: "L3041-L3118"
      purpose: "Glossário de termos proprietários"

**Entrada:**
- campo: rodada
  tipo: number
  origem: Auto-detect or User Input
  obrigatório: true
  default: 1

- campo: mode
  tipo: string
  origem: User Input
  obrigatório: false
  default: interactive

**Inputs opcionais (enriquecem):**
- campo: canvas-cliente-ideal.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: false
  purpose: Contexto do público para adaptar o tom

- campo: canvas-produto.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: false
  purpose: Contexto do produto para alinhar posicionamento

- campo: avatar-blueprint.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: false
  purpose: Perfil do avatar para calibrar linguagem

**Saída:**
- campo: tom_de_voz_file
  tipo: string
  destino: docs/webinar/rodada-{N}/planejamento/tom-de-voz-expert.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] Detect active round (rodada) from docs/webinar/ directory
    tipo: pre-condition
    blocker: false
    validação: Check or create rodada-{N}/planejamento/ structure
  - [ ] Recommended: canvas-produto.md exists (helps define positioning)
    tipo: pre-condition
    blocker: false
    validação: If exists, load for context
```

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] Tom de voz file created at docs/webinar/rodada-{N}/planejamento/tom-de-voz-expert.md
    tipo: post-condition
    blocker: true
  - [ ] All 6 sections have non-empty content (Posicionamento, Aberturas, Contexto, Informalidade, Motivação, Emojis)
    tipo: post-condition
    blocker: true
```

---

# Tom de Voz do Expert — Task

## Purpose

Capturar o tom de voz e estilo de comunicação do expert/apresentador do webinário. Este artefato é referência obrigatória para toda copy gerada pelo @webinar-creator (roteiro, mensagens, páginas).

## SEQUENTIAL Task Execution

### 0. Setup e Cross-Reference

- Detectar rodada ativa
- Verificar se `canvas-produto.md` e `avatar-blueprint.md` existem na rodada atual
- Se existirem, carregar para contextualizar as perguntas
- Informar ao usuário: "Vamos definir como você se comunica com seu público. Isso vai guiar todo o conteúdo do webinário — roteiro, mensagens, páginas."

### 1. Introdução

> **Tom de Voz do Expert**
>
> Antes de criar qualquer conteúdo, preciso entender como VOCÊ fala com seu público. Seu tom de voz é único e precisa estar presente em tudo — desde o roteiro do webinário até as mensagens de WhatsApp.
>
> Vou te fazer algumas perguntas rápidas sobre o seu estilo de comunicação.

### 2. Conduzir os 6 Blocos (Interactive Mode)

#### Bloco 1: Posicionamento

```
elicit: true
format: AskUserQuestion (single select)

Como você se posiciona quando fala com seu público?

Opções:
1. Amigo próximo — mesmo nível, dividindo o que sabe
2. Mentor acessível — lidera e ensina, mas de um jeito leve e sem distância
3. Professor animado — é a autoridade, mas com energia e sem ser formal
4. Especialista direto — autoridade técnica, sério mas acessível

{Se avatar-blueprint existe: "Considerando seu público ({avatar}), qual posicionamento combina mais?"}
```

#### Bloco 2: Estilo de Abertura

```
elicit: true
format: open text

Como você costuma abrir uma conversa com seu público? Me dá 2-3 exemplos de como você começaria uma mensagem ou uma live.

Exemplos pra te inspirar:
- "Fala turma, tudo certo?"
- "E aí pessoal, bom dia!"
- "Galera, atenção..."
- "Boa tarde, meus queridos"

Como VOCÊ abre?
```

#### Bloco 3: Nível de Informalidade

```
elicit: true
format: AskUserQuestion (single select)

Você usa gírias e expressões informais na comunicação?

Opções:
1. Sim, bastante — faz parte do meu jeito de falar
2. Às vezes — uso quando cabe, mas sem forçar
3. Pouco — sou informal mas sem gíria demais
4. Quase nunca — prefiro um tom mais polido

{Se bloco 2 já respondido: analisar as aberturas e sugerir o nível detectado}
```

#### Bloco 4: Estilo de Motivação

```
elicit: true
format: AskUserQuestion (multi select)

Quando você quer motivar alguém a agir, qual estilo combina mais com você?

Opções (pode escolher mais de uma):
1. Energia e empolgação — "Bora, isso vai mudar tudo pra você!"
2. Verdade direta — "Se você não fizer agora, vai continuar do mesmo jeito."
3. Prova e resultado — "Fulano fez e conseguiu X. Você também consegue."
4. Empatia e acolhimento — "Eu sei que é difícil, mas você pode começar pequeno."
```

#### Bloco 5: Uso de Emojis

```
elicit: true
format: AskUserQuestion (single select)

Você costuma usar emojis nas mensagens?

Opções:
1. Sim, sempre — faz parte da comunicação
2. Moderado — uso pra destacar pontos, sem exagero
3. Pouco — só quando realmente faz sentido
4. Quase nunca — prefiro texto limpo
```

#### Bloco 6: Exemplos e Ajustes

```
elicit: true
format: open text

Com base nas suas respostas, montei um resumo do seu tom. Vou te mostrar um exemplo de mensagem nesse tom. Me diz o que ajustar:

{Gerar mensagem exemplo no tom detectado}

O que está bom e o que precisa mudar?
```

### 3. Gerar Documento

- Carregar template: `squad/templates/webinar-tom-de-voz-tmpl.md`
- Preencher com respostas do usuário
- Incluir mensagem exemplo aprovada
- Salvar em: `docs/webinar/rodada-{N}/planejamento/tom-de-voz-expert.md`

### 4. Apresentar Resumo e Próximo Passo

```
Tom de voz salvo em:
docs/webinar/rodada-{N}/planejamento/tom-de-voz-expert.md

Resumo:
- Posicionamento: [bloco 1]
- Aberturas: [exemplos do bloco 2]
- Informalidade: [bloco 3]
- Motivação: [bloco 4]
- Emojis: [bloco 5]

Este documento será usado como referência obrigatória pelo @webinar-creator para gerar todo o conteúdo (roteiro, mensagens, copy).

Próximo passo recomendado:
→ *canvas-webinar — para definir a estrutura do webinário
→ *orcamento — para calcular metas e investimento
→ *resumo — se todos os canvases já estão preenchidos
```

---

## Error Handling

1. **Error:** User can't describe their tone
   - **Resolution:** Show 3 example messages in different tones and ask which feels more natural
   - **Recovery:** Let user pick and adjust

2. **Error:** Tone seems inconsistent with avatar
   - **Resolution:** Flag: "Seu público é [avatar]. Esse tom mais [X] pode funcionar melhor. O que acha?"
   - **Recovery:** User decides, their preference wins

---

## Handoff

```yaml
next_agent: "@webinar-strategist"
next_command: "*canvas-webinar"
condition: Tom de voz definido, Canvas do Produto e Avatar Blueprint disponíveis
alternatives:
  - agent: "@webinar-strategist"
    command: "*orcamento"
    condition: "Canvas do Webinário já preenchido"
  - agent: "@webinar-strategist"
    command: "*resumo"
    condition: "Todos os canvases preenchidos"
```

---

## Metadata

```yaml
version: 1.0.0
squad: webinar
agent: webinar-strategist
command: "*tom-de-voz"
prd_reference: "PRD v2.1 — Definição de tom de voz para personalização de conteúdo"
tags:
  - webinar
  - planning
  - tom-de-voz
  - brand-voice
updated_at: 2026-03-10
```
