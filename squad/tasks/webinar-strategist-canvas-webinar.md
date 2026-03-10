---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
- Agent asks all 15 blocks in sequence, generates canvas
- **Best for:** Experienced users

### 2. Interactive Mode - Balanced, Educational (15-25 prompts) **[DEFAULT]**
- One block at a time with methodology explanation
- Cross-references data from Canvas do Produto, Avatar Blueprint, and Canvas do Cliente Ideal
- **Best for:** First-time users, deep planning

### 3. Pre-Flight Planning - Review Existing Canvas
- Load existing canvas, show filled/pending blocks
- **Best for:** Updating for next round

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: canvasWebinar()
responsável: Sage (Strategist)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "canvas-webinar"
      lines: "L200-L283"
      purpose: "15 blocos do Canvas do Webinário Infalível — crença-alvo, ponte de crenças, oferta, entregáveis"
    - id: "canvas-produto"
      lines: "L141-L199"
      purpose: "Cross-reference: Grande Promessa, Mecanismo Único (blocos 10, 12, 13)"
    - id: "avatar-blueprint"
      lines: "L1722-L1866"
      purpose: "Cross-reference: crença-alvo, ponte de crenças (blocos 10-11), objeções (bloco 15)"
    - id: "glossario"
      lines: "L3041-L3118"
      purpose: "Glossário de termos proprietários"

**Entrada:**
- campo: rodada
  tipo: number
  origem: Auto-detect or User Input
  obrigatório: true
  default: 1

**Inputs obrigatórios:**
- campo: canvas-produto.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: true
  purpose: Grande Promessa, Mecanismo Único, Proposta de Valor

- campo: avatar-blueprint.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: true
  purpose: Crença-alvo, ponte de crenças, objeções do avatar

**Inputs opcionais:**
- campo: canvas-cliente-ideal.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: false
  purpose: Contexto do público (objeções do bloco 15)

**Saída:**
- campo: canvas_file
  tipo: string
  destino: docs/webinar/rodada-{N}/planejamento/canvas-webinar.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] canvas-produto.md exists in rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    validação: |
      Check for canvas-produto.md. If not found, inform user:
      "Para preencher o Canvas do Webinário, preciso do Canvas do Produto preenchido.
      Quer preencher agora? → *canvas-produto"
    error_message: "Canvas do Produto é pré-requisito. Execute *canvas-produto primeiro."

  - [ ] avatar-blueprint.md exists in rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    validação: |
      Check for avatar-blueprint.md. If not found, inform user:
      "Para preencher o Canvas do Webinário, preciso do Avatar Blueprint preenchido.
      Quer preencher agora? → *avatar"
    error_message: "Avatar Blueprint é pré-requisito. Execute *avatar primeiro."
```

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] Canvas file created at docs/webinar/rodada-{N}/planejamento/canvas-webinar.md
    tipo: post-condition
    blocker: true
  - [ ] All 15 blocks have non-empty content
    tipo: post-condition
    blocker: true
  - [ ] Crença-alvo follows formula: "A única forma de ter [transformação] sem [obstáculo] é através do [mecanismo único]"
    tipo: post-condition
    blocker: true
```

---

# Canvas do Webinário Infalível — Task

## Purpose

Conduzir o usuário pelo preenchimento do Canvas do Webinário Infalível (Canvas 3), com 15 blocos que definem toda a estrutura do webinário: tema, crença-alvo, ponte de crenças, oferta, entregáveis, bônus, objeções e respostas. Puxa dados automaticamente do Canvas do Produto e Avatar Blueprint.

## SEQUENTIAL Task Execution

### 0. Setup e Cross-Reference

- Detectar rodada ativa
- Carregar `canvas-produto.md` — extrair: Grande Promessa, Mecanismo Único, Proposta de Valor
- Carregar `avatar-blueprint.md` — extrair: desejos, obstáculos, falsas crenças, objeções
- Opcionalmente carregar `canvas-cliente-ideal.md` para objeções adicionais
- Informar: "Carreguei o Canvas do Produto e o Avatar Blueprint. Vou usar essas informações para pré-preencher alguns blocos automaticamente."
- Carregar knowledge base: `docs/METHODOLOGY-ANALYSIS.md` linhas L200-L283

### 1. Introdução ao Canvas

> **Canvas do Webinário Infalível**
>
> Este é o canvas mais completo — 15 blocos que definem TODO o webinário.
> Muitos blocos serão pré-preenchidos com dados dos canvases anteriores.
> Você só precisa confirmar ou ajustar.
>
> Blocos 1-9: Estrutura geral (tema, título, formato, etc.)
> Bloco 10: Crença-alvo (o pilar central do webinário)
> Bloco 11: Ponte de crenças (tópicos que sustentam a crença)
> Blocos 12-15: Oferta, entregáveis, bônus e objeções

### 2. Conduzir os 15 Blocos

#### Blocos 1-9: Estrutura Geral

**Bloco 1 — Tema do Webinário:**
```
Qual é o TEMA central do seu webinário?

O tema deve ser específico o suficiente para atrair o público certo,
mas amplo o suficiente para gerar curiosidade.

{Se canvas-produto existe: "Baseado na sua Grande Promessa ('{grande_promessa}'), sugiro algo como: '{sugestão_tema}'"}

Qual é o tema?
```

**Bloco 2 — Título do Webinário:**
```
Qual será o TÍTULO do webinário?

Fórmulas que funcionam:
- "Como [resultado] sem [obstáculo]"
- "Como [resultado] mesmo que [limitação]"
- "Os 3 segredos para [resultado]"
- "[Número] passos para [resultado] em [tempo]"

{Sugestões baseadas em canvas-produto e avatar-blueprint}

Qual título você prefere?
```

**Bloco 3 — Objetivo:**
```
Qual o OBJETIVO principal deste webinário?

Normalmente é: "Vender [produto] para [público] com ticket de R$[valor]"

Objetivo:
```

**Bloco 4 — Público-alvo:**
```
{Se canvas-cliente existe: "Importado do Canvas do Cliente Ideal: {público}. Quer manter ou ajustar?"}
{Senão: "Quem é o público-alvo deste webinário?"}
```

**Bloco 5 — Formato:**
```
Qual o formato do webinário?

Opções comuns:
1. Ao vivo (uma data, uma sessão)
2. Evergreen/Perpétuo (gravado, roda automaticamente)
3. Série (2-3 sessões em dias consecutivos)

Qual formato?
```

**Bloco 6 — Data/Frequência:**
```
{Se formato=ao_vivo: "Qual a data planejada para o webinário?"}
{Se formato=evergreen: "Qual a frequência de exibição? (diária, a cada 3 dias, semanal)"}
{Se formato=serie: "Quais as datas das sessões?"}
```

**Bloco 7 — Plataforma:**
```
Qual plataforma será usada para transmitir?

Opções:
1. EverWebinar (recomendado pela metodologia — suporte a evergreen)
2. Zoom
3. YouTube Live
4. StreamYard
5. Outra

Qual plataforma?
```

**Bloco 8 — Duração estimada:**
```
Qual a duração estimada do webinário?

Benchmark da metodologia:
- Abertura: 5-10 min
- Empatia/História: 5-10 min
- Conteúdo: 25-40 min
- Pitch/Oferta: 20-30 min
- Total recomendado: 60-90 min

Duração planejada:
```

**Bloco 9 — Estrutura:**
```
A estrutura do webinário segue o modelo "Black Box":
Abertura → Empatia → Conteúdo (3 Secrets) → Pitch (15 etapas)

Confirma essa estrutura ou quer alguma variação?
```

#### Bloco 10: Crença-Alvo (CENTRAL)

```
Agora vamos definir a CRENÇA-ALVO — o pilar central de todo o webinário.

Fórmula:
"A única forma de ter [transformação] sem [obstáculo] é através do [mecanismo único]"

{Dados importados:
- Transformação (Grande Promessa): "{grande_promessa}"
- Obstáculo (Avatar Blueprint): "{obstáculo_principal}"
- Mecanismo Único: "{mecanismo_unico}"}

Sugestão automática:
"A única forma de {transformação} sem {obstáculo} é através do {mecanismo_unico}"

Quer usar essa crença-alvo ou ajustar?
```

#### Bloco 11: Ponte de Crenças

```
A PONTE DE CRENÇAS é uma lista de tópicos/afirmações que sustentam a crença-alvo.
São os "degraus" que levam a pessoa da descrença à crença.

{Dados importados do Avatar Blueprint:
- Falsas crenças identificadas: {lista_falsas_crencas}
- Obstáculos: {obstaculos}}

Cada tópico deve ser uma afirmação que, se a pessoa acreditar,
a leva mais perto de acreditar na crença-alvo.

Liste 5-8 tópicos para a ponte de crenças:
```

#### Bloco 12: Oferta

```
Vamos definir a OFERTA do webinário.

{Se canvas-produto existe: "Dados importados: Produto: {produto}, Grande Promessa: {grande_promessa}"}

Defina:
1. Ticket (preço) do produto: R$
2. Condições de pagamento: (à vista, parcelado, etc.)
3. Garantia: (7 dias, 30 dias, incondicional, condicional)
```

#### Bloco 13: Entregáveis (Stack Slide)

```
Agora vamos montar os ENTREGÁVEIS — o que a pessoa RECEBE ao comprar.
Cada entregável terá nome + descrição + valor em R$ para o Stack Slide.

O Stack Slide mostra todos os itens com valores individuais,
soma tudo (âncora alta) e depois mostra o preço real (dupla queda de preço).

Liste seus entregáveis:
(Para cada um: Nome | Descrição | Valor em R$)

Exemplo:
- Módulo 1: Fundamentos | 8 aulas sobre a base do método | R$497
- Módulo 2: Prática | 12 aulas com exercícios | R$697
```

#### Bloco 14: Bônus

```
Quais BÔNUS você oferece?

Bônus são itens extras que aumentam a percepção de valor.
Cada bônus também tem nome + descrição + valor em R$ (entram no Stack Slide).

Liste seus bônus:
(Para cada um: Nome | Descrição | Valor em R$)

Exemplo:
- Bônus 1: Planilha de Controle | Template pronto para usar | R$197
- Bônus 2: Grupo VIP | 30 dias de suporte no WhatsApp | R$297
```

#### Bloco 15: Objeções e Respostas

```
Vamos mapear as OBJEÇÕES e preparar as respostas para cada uma.

{Se canvas-cliente existe: "Objeções importadas do Canvas do Cliente Ideal: {objecoes_canvas}"}
{Se avatar-blueprint existe: "Razões para NÃO comprar (Avatar Blueprint): {razoes_nao_comprar}"}

Para cada objeção, prepare uma resposta direta que será usada no pitch.

Pares Objeção → Resposta:
```

### 3. Gerar Canvas

- Carregar template: `.aiox-core/development/templates/webinar-canvas-webinar-tmpl.md`
- Preencher com respostas do usuário + dados importados
- Salvar em: `docs/webinar/rodada-{N}/planejamento/canvas-webinar.md`

### 4. Apresentar Resumo e Próximo Passo

```
Canvas do Webinário Infalível salvo em:
docs/webinar/rodada-{N}/planejamento/canvas-webinar.md

Resumo:
- Título: [bloco 2]
- Crença-alvo: [bloco 10]
- Ticket: R$[bloco 12]
- Entregáveis: [quantidade] itens no Stack Slide
- Bônus: [quantidade] bônus
- Objeções mapeadas: [quantidade]

Próximo passo recomendado:
→ *orcamento — para calcular metas e investimento
→ *resumo — para gerar relatório consolidado (se todos os canvases estão prontos)
```

---

## Error Handling

1. **Error:** Missing prerequisite canvas
   - **Resolution:** Redirect to correct command with explanation
   - **Recovery:** "*canvas-produto" or "*avatar" as appropriate

2. **Error:** Crença-alvo doesn't follow formula
   - **Resolution:** Show formula again, offer to rebuild from imported data

---

## Handoff

```yaml
next_agent: "@webinar-strategist"
next_command: "*orcamento"
condition: Canvas do Webinário preenchido
alternatives:
  - agent: "@webinar-strategist"
    command: "*resumo"
    condition: "Todos os canvases preenchidos"
  - agent: "@webinar-creator"
    command: "*abertura"
    condition: "Planejamento completo, quer iniciar construção"
```

---

## Metadata

```yaml
version: 1.0.0
squad: webinar
agent: webinar-strategist
command: "*canvas-webinar"
prd_reference: "PRD v2.1, Seção 3.2 — Canvas do Webinário Infalível (15 blocos)"
methodology_reference: "Seção 2, Canvas 3 — METHODOLOGY-ANALYSIS.md L200-L283"
tags:
  - webinar
  - planning
  - canvas
  - webinar-infallible
updated_at: 2026-03-05
```
