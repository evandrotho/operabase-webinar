---

## Execution Modes

**Choose your execution mode:**

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
- Autonomous decision making with logging
- Minimal user interaction — agent asks all 9 questions in sequence, generates canvas
- **Best for:** User already knows all answers

### 2. Interactive Mode - Balanced, Educational (9-15 prompts) **[DEFAULT]**
- One question at a time with explanation of WHY each matters
- Educational context from methodology
- **Best for:** First-time users, learning the process

### 3. Pre-Flight Planning - Review Existing Canvas
- Load existing canvas, show what's filled, ask about updates
- **Best for:** Updating canvas for next round

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: canvasCliente()
responsável: Sage (Strategist)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "canvas-cliente-ideal"
      lines: "L83-L140"
      purpose: "9 perguntas do Canvas do Cliente Ideal — critérios objetivos vs. subjetivos, múltiplos perfis"
    - id: "glossario"
      lines: "L3041-L3118"
      purpose: "Glossário de termos proprietários"

**Entrada:**
- campo: rodada
  tipo: number
  origem: Auto-detect or User Input
  obrigatório: true
  validação: Positive integer, detect from docs/webinar/ directory
  default: 1

- campo: mode
  tipo: string
  origem: User Input
  obrigatório: false
  validação: One of [interactive, yolo, preflight]
  default: interactive

**Saída:**
- campo: canvas_file
  tipo: string
  destino: docs/webinar/rodada-{N}/planejamento/canvas-cliente-ideal.md
  persistido: true

- campo: success
  tipo: boolean
  destino: Return value
  persistido: false
```

---

## Pre-Conditions

**Purpose:** Validate prerequisites BEFORE task execution (blocking)

**Checklist:**

```yaml
pre-conditions:
  - [ ] Detect active round (rodada) from docs/webinar/ directory structure
    tipo: pre-condition
    blocker: false
    validação: |
      Check docs/webinar/ for rodada-{N} directories.
      If none exist, create rodada-1/planejamento/ directory structure.
      If multiple exist, ask user which round to work on.
    error_message: "Nenhuma rodada detectada. Criando estrutura da rodada 1."

  - [ ] No mandatory input files — this is the FIRST canvas in the recommended flow
    tipo: pre-condition
    blocker: false
    validação: |
      This canvas has no mandatory prerequisites.
      It is the recommended starting point for planning.
```

---

## Post-Conditions

**Purpose:** Validate execution success AFTER task completes

**Checklist:**

```yaml
post-conditions:
  - [ ] Canvas file created at docs/webinar/rodada-{N}/planejamento/canvas-cliente-ideal.md
    tipo: post-condition
    blocker: true
    validação: |
      Verify file exists, is valid markdown, contains all 9 questions answered.
    error_message: "Canvas do Cliente Ideal não foi salvo corretamente."

  - [ ] All 9 questions have non-empty answers
    tipo: post-condition
    blocker: true
    validação: |
      Parse generated canvas and verify each of the 9 sections has content.
    error_message: "Algumas perguntas ficaram sem resposta no canvas."
```

---

## Acceptance Criteria

```yaml
acceptance-criteria:
  - [ ] Canvas contains all 9 questions answered with user's input
    tipo: acceptance-criterion
    blocker: true
  - [ ] Question 1 validates objective vs. subjective criteria
    tipo: acceptance-criterion
    blocker: true
  - [ ] Support for multiple client profiles if user identifies more than one
    tipo: acceptance-criterion
    blocker: false
  - [ ] Canvas saved as formatted markdown using template
    tipo: acceptance-criterion
    blocker: true
```

---

## Performance

```yaml
duration_expected: 10-25 min (interactive mode), 3-5 min (yolo mode)
cost_estimated: $0.005-0.015
token_usage: ~5,000-15,000 tokens
```

---

# Canvas do Cliente Ideal — Task

## Purpose

Conduzir o usuário pelo preenchimento do Canvas do Cliente Ideal (Canvas 1 da metodologia), com 9 perguntas estratégicas que definem quem é o público do webinário. Este é o ponto de partida recomendado para o planejamento.

## SEQUENTIAL Task Execution

### 0. Setup e Detecção de Rodada

- Detectar rodada ativa verificando `docs/webinar/` por diretórios `rodada-{N}`
- Se nenhum existir, criar `docs/webinar/rodada-1/planejamento/`
- Se existir canvas anterior (rodada anterior), perguntar se quer importar como base
- Carregar knowledge base: `docs/METHODOLOGY-ANALYSIS.md` linhas L83-L140

### 1. Introdução ao Canvas

Apresentar ao usuário:

> **Canvas do Cliente Ideal**
>
> Este é o primeiro passo do planejamento do seu webinário. Vamos definir QUEM é o seu público ideal respondendo 9 perguntas estratégicas.
>
> Cada pergunta tem um propósito específico na construção do seu webinário — vou explicar o porquê de cada uma.
>
> Dica: Se você atende mais de um perfil de cliente, podemos criar múltiplos perfis.

### 2. Conduzir as 9 Perguntas (Interactive Mode)

Para CADA pergunta, seguir este padrão:
1. Apresentar a pergunta com explicação do PORQUÊ ela importa
2. Aguardar resposta do usuário (elicit: true)
3. Validar a resposta (especialmente pergunta 1 — critérios objetivos)
4. Confirmar entendimento antes de prosseguir

#### Pergunta 1: Quem é o seu público? (Critérios Objetivos)

```
Quem é o seu público-alvo?

IMPORTANTE: Use critérios OBJETIVOS, não subjetivos.

Critérios objetivos (correto):
- "Dentistas com consultório próprio"
- "Mulheres de 30-45 anos que são nutricionistas"
- "Donos de e-commerce com faturamento acima de R$50mil/mês"

Critérios subjetivos (evitar):
- "Pessoas que querem mudar de vida"
- "Empreendedores ambiciosos"

Descreva seu público usando critérios que você consegue verificar:
```

**Validação:** Se a resposta contiver apenas critérios subjetivos, orientar o usuário a reformular com critérios objetivos. Aceitar uma combinação de ambos, mas garantir que existam critérios objetivos.

#### Pergunta 2: Qual o principal problema ou dor?

```
Qual é o PRINCIPAL problema ou dor que esse público enfrenta?

Isso será usado para criar conexão imediata na abertura do webinário.
O ideal é uma dor que tira o sono — algo que eles pensam antes de dormir.

Qual é essa dor principal?
```

#### Pergunta 3: O que já tentaram para resolver?

```
O que seu público JÁ TENTOU fazer para resolver esse problema?

Saber o que não funcionou é essencial para posicionar seu produto como DIFERENTE
de tudo que já tentaram. Isso alimenta a seção de "Falsas Crenças" do roteiro.

O que eles já tentaram? (Liste 2-5 tentativas comuns)
```

#### Pergunta 4: Por que não funcionou?

```
Por que essas tentativas anteriores NÃO funcionaram?

Essa resposta será usada para invalidar as "soluções antigas" e
posicionar seu Mecanismo Único como a resposta certa.

Por que o que tentaram antes não deu certo?
```

#### Pergunta 5: Qual o resultado desejado?

```
Qual é o RESULTADO FINAL que seu público deseja alcançar?

Esse resultado vira a "Grande Promessa" do seu webinário.
Fórmula: "[Resultado] em [tempo] sem [obstáculo]"

Qual resultado eles querem atingir?
```

#### Pergunta 6: Quanto pagariam para resolver?

```
Quanto seu público pagaria para resolver esse problema de vez?

Isso ajuda a calibrar o ticket do seu produto e a percepção de valor.
Pense no valor que a SOLUÇÃO representa, não no custo do produto.

Qual a faixa de investimento que eles fariam? (R$)
```

#### Pergunta 7: Onde estão? (Canais e plataformas)

```
Onde seu público ESTÁ? Em quais canais e plataformas?

Isso define onde você vai captar leads para o webinário.
Instagram? YouTube? LinkedIn? Grupos de WhatsApp? Google?

Liste os principais canais onde seu público consome conteúdo:
```

#### Pergunta 8: Quais objeções teriam?

```
Quais OBJEÇÕES seu público teria para NÃO comprar seu produto?

Essas objeções serão respondidas uma a uma no pitch do webinário.
Pense nas desculpas mais comuns que ouve (ou ouviria).

Liste as principais objeções (3-5 objeções):
```

#### Pergunta 9: O que os faria agir agora?

```
O que faria seu público AGIR AGORA em vez de "pensar depois"?

Isso alimenta os gatilhos de urgência e escassez do pitch.
Pode ser: desconto por tempo, vagas limitadas, bônus exclusivo, etc.

O que os motivaria a tomar ação imediata?
```

### 3. Validação de Múltiplos Perfis

Após as 9 perguntas:

```
Perfeito! Temos o perfil do seu cliente ideal definido.

Você atende mais de um perfil de cliente com este produto?
Se sim, podemos criar perfis adicionais. Cada perfil terá suas
próprias respostas para as 9 perguntas.

Quer adicionar outro perfil ou está completo?
```

Se sim, repetir as 9 perguntas para o perfil adicional.

### 4. Gerar Canvas

- Carregar template: `.aiox-core/development/templates/webinar-canvas-cliente-ideal-tmpl.md`
- Preencher com respostas do usuário
- Salvar em: `docs/webinar/rodada-{N}/planejamento/canvas-cliente-ideal.md`

### 5. Apresentar Resumo e Próximo Passo

```
Canvas do Cliente Ideal salvo em:
docs/webinar/rodada-{N}/planejamento/canvas-cliente-ideal.md

Resumo:
- Público: [resumo da pergunta 1]
- Dor principal: [resumo da pergunta 2]
- Resultado desejado: [resumo da pergunta 5]
- Objeções mapeadas: [quantidade]

Próximo passo recomendado:
→ *canvas-produto — para definir sua Grande Promessa e Mecanismo Único
→ *avatar — para aprofundar o perfil do cliente (requer este canvas)
```

---

## Error Handling

**Strategy:** retry

1. **Error:** User provides only subjective criteria for Question 1
   - **Resolution:** Explain objective vs. subjective with examples, ask to reformulate
   - **Recovery:** Accept mixed criteria but ensure at least one objective criterion exists

2. **Error:** User skips a question
   - **Resolution:** Explain why the question matters for the webinar structure
   - **Recovery:** Allow skip but mark as "[A preencher]" in canvas

3. **Error:** Output directory doesn't exist
   - **Resolution:** Create directory structure automatically
   - **Recovery:** Create docs/webinar/rodada-{N}/planejamento/

---

## Handoff

```yaml
next_agent: "@webinar-strategist"
next_command: "*canvas-produto"
condition: Canvas do Cliente Ideal preenchido
alternatives:
  - agent: "@webinar-strategist"
    command: "*avatar"
    condition: "Usuário quer aprofundar o perfil do cliente"
  - agent: "@webinar-creator"
    command: "*abertura"
    condition: "Planejamento já completo (todos os canvases preenchidos)"
```

---

## Metadata

```yaml
version: 1.0.0
squad: webinar
agent: webinar-strategist
command: "*canvas-cliente"
prd_reference: "PRD v2.1, Seção 3.2 — Canvas do Cliente Ideal (9 perguntas)"
methodology_reference: "Seção 2, Canvas 1 — METHODOLOGY-ANALYSIS.md L83-L140"
tags:
  - webinar
  - planning
  - canvas
  - cliente-ideal
updated_at: 2026-03-05
```
