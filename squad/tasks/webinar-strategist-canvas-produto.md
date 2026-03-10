---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
- Agent asks all 7 blocks in sequence, generates canvas
- **Best for:** User already knows all answers

### 2. Interactive Mode - Balanced, Educational (7-12 prompts) **[DEFAULT]**
- One block at a time with explanation
- **Best for:** First-time users

### 3. Pre-Flight Planning - Review Existing Canvas
- Load existing canvas, show what's filled, ask about updates
- **Best for:** Updating for next round

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: canvasProduto()
responsável: Sage (Strategist)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "canvas-produto"
      lines: "L141-L199"
      purpose: "7 blocos do Canvas do Produto — Grande Promessa, Mecanismo Único, Proposta de Valor"
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
  purpose: Contexto do público para enriquecer as respostas

**Saída:**
- campo: canvas_file
  tipo: string
  destino: docs/webinar/rodada-{N}/planejamento/canvas-produto.md
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
  - [ ] Optional: canvas-cliente-ideal.md exists (enriches but not required)
    tipo: pre-condition
    blocker: false
    validação: If exists, load for cross-reference context
```

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] Canvas file created at docs/webinar/rodada-{N}/planejamento/canvas-produto.md
    tipo: post-condition
    blocker: true
  - [ ] All 7 blocks have non-empty content
    tipo: post-condition
    blocker: true
```

---

# Canvas do Produto — Task

## Purpose

Conduzir o usuário pelo preenchimento do Canvas do Produto (Canvas 2 da metodologia), com 7 blocos que definem a Grande Promessa, o Mecanismo Único e a Proposta de Valor do produto/serviço.

## SEQUENTIAL Task Execution

### 0. Setup e Cross-Reference

- Detectar rodada ativa
- Verificar se `canvas-cliente-ideal.md` existe na rodada atual
- Se existir, carregar para cross-reference (usar dados do público para contextualizar)
- Informar ao usuário: "Encontrei o Canvas do Cliente Ideal preenchido. Vou usar as informações do seu público para enriquecer este canvas."
- Carregar knowledge base: `docs/METHODOLOGY-ANALYSIS.md` linhas L141-L199

### 1. Introdução ao Canvas

> **Canvas do Produto**
>
> Agora vamos definir o posicionamento do seu produto/serviço. São 7 blocos que vão construir a proposta de valor completa — desde a Grande Promessa até o Mecanismo Único.
>
> Esses blocos alimentam diretamente o roteiro do webinário: a abertura usa sua Grande Promessa, o conteúdo usa seu Mecanismo Único, e o pitch usa a Proposta de Valor.

### 2. Conduzir os 7 Blocos (Interactive Mode)

#### Bloco 1: Grande Promessa

```
Qual é a GRANDE PROMESSA do seu produto?

Use a fórmula: "[Resultado] em [tempo] sem [obstáculo]"

Exemplos:
- "Emagrecer 10kg em 90 dias sem dietas restritivas"
- "Dobrar o faturamento em 6 meses sem aumentar a equipe"
- "Falar inglês fluente em 1 ano sem sair do Brasil"

{Se canvas-cliente-ideal existe: "Baseado no seu público ({público}), o resultado desejado é '{resultado}'. Vamos transformar isso em uma Grande Promessa:"}

Qual é a sua Grande Promessa?
```

#### Bloco 2: Produto/Serviço

```
Descreva seu produto ou serviço.

O que exatamente você entrega? É um curso, mentoria, consultoria, software, serviço?
Qual o formato de entrega? (online, presencial, híbrido)
Qual a duração ou escopo?

Descreva seu produto:
```

#### Bloco 3: Mecanismo Único

```
Qual é o seu MECANISMO ÚNICO?

O Mecanismo Único são "duas ou três palavras que geram mistério" — é o COMO
você entrega o resultado prometido, mas de uma forma que soa nova e diferente.

Exemplos:
- "Método da Inversão Metabólica" (emagrecimento)
- "Sistema de Escala Autônoma" (negócios)
- "Técnica do Espelhamento Neural" (idiomas)

Qual nome daria ao seu método/sistema/técnica?
```

#### Bloco 4: Nome do Mecanismo Único

```
Confirme o nome do seu Mecanismo Único.

O nome deve ser:
- Curto (2-4 palavras)
- Intrigante (gera curiosidade)
- Proprietário (parece exclusivamente seu)

{Se bloco 3 já definiu: "Você mencionou '{mecanismo}'. Quer manter esse nome ou ajustar?"}

Nome final do Mecanismo Único:
```

#### Bloco 5: Diferencial Competitivo

```
O que DIFERENCIA seu produto de tudo que já existe?

Por que alguém escolheria o SEU produto em vez de:
- Cursos concorrentes?
- Fazer sozinho com YouTube/Google?
- Não fazer nada?

Liste 2-3 diferenciais reais:
```

#### Bloco 6: Prova

```
Que PROVAS você tem de que seu produto funciona?

Tipos de prova:
- Cases de sucesso (alunos/clientes com resultados)
- Dados e números (% de aprovação, resultados médios)
- Sua própria história (você conseguiu o resultado prometido?)
- Autoridade (certificações, tempo de mercado, mídia)

Quais provas você pode apresentar?
```

#### Bloco 7: Proposta de Valor (Template de 7 Tópicos)

```
Vamos montar sua Proposta de Valor completa. Responda cada tópico:

1. Público-alvo: Para quem é?
   {Se canvas-cliente existe: Sugestão: "{público do canvas}"}
2. Problema: Qual problema resolve?
3. Solução: Como resolve?
4. Benefício principal: Qual o maior ganho?
5. Diferencial: Por que escolher você?
6. Prova: Como demonstra que funciona?
7. CTA: Qual a próxima ação?
```

### 3. Gerar Canvas

- Carregar template: `.aiox-core/development/templates/webinar-canvas-produto-tmpl.md`
- Preencher com respostas do usuário
- Salvar em: `docs/webinar/rodada-{N}/planejamento/canvas-produto.md`

### 4. Apresentar Resumo e Próximo Passo

```
Canvas do Produto salvo em:
docs/webinar/rodada-{N}/planejamento/canvas-produto.md

Resumo:
- Grande Promessa: [bloco 1]
- Mecanismo Único: [bloco 3/4]
- Diferenciais: [quantidade de diferenciais]
- Provas: [quantidade de provas]

Próximo passo recomendado:
→ *avatar — para aprofundar o perfil do cliente ideal (requer *canvas-cliente)
→ *canvas-webinar — para definir a estrutura do webinário (requer este canvas + avatar)
```

---

## Error Handling

1. **Error:** User can't articulate Mecanismo Único
   - **Resolution:** Offer brainstorming prompts: "O que torna seu método diferente? Qual passo do seu processo é incomum?"
   - **Recovery:** Help create a name from the user's description

2. **Error:** Grande Promessa is vague
   - **Resolution:** Apply formula "[Resultado] em [tempo] sem [obstáculo]" explicitly
   - **Recovery:** Offer 3 variations based on user's description

---

## Handoff

```yaml
next_agent: "@webinar-strategist"
next_command: "*avatar"
condition: Canvas do Produto preenchido e Canvas do Cliente Ideal disponível
alternatives:
  - agent: "@webinar-strategist"
    command: "*canvas-webinar"
    condition: "Avatar Blueprint já preenchido"
```

---

## Metadata

```yaml
version: 1.0.0
squad: webinar
agent: webinar-strategist
command: "*canvas-produto"
prd_reference: "PRD v2.1, Seção 3.2 — Canvas do Produto (7 blocos)"
methodology_reference: "Seção 2, Canvas 2 — METHODOLOGY-ANALYSIS.md L141-L199"
tags:
  - webinar
  - planning
  - canvas
  - produto
updated_at: 2026-03-05
```
