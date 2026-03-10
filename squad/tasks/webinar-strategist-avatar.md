---

## Execution Modes

### 1. YOLO Mode - Fast, Autonomous (0-1 prompts)
- Agent asks all 7 questions + table in sequence
- **Best for:** Experienced users

### 2. Interactive Mode - Balanced, Educational (8-15 prompts) **[DEFAULT]**
- One question at a time with explanation of how each feeds the webinar
- **Best for:** First-time users, deep avatar work

### 3. Pre-Flight Planning - Review Existing Avatar
- Load existing avatar, show what's filled, ask about updates
- **Best for:** Refining avatar with real data from previous round

**Parameter:** `mode` (optional, default: `interactive`)

---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: avatarBlueprint()
responsável: Sage (Strategist)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "avatar-blueprint"
      lines: "L1722-L1866"
      purpose: "7 perguntas do Mapa do Avatar + Tabela Problema x Solução + One Big Domino"
    - id: "canvas-cliente-ideal"
      lines: "L83-L140"
      purpose: "Cross-reference: dados do público já coletados"
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
- campo: canvas-cliente-ideal.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: true
  purpose: Dados do público para enriquecer o avatar

**Saída:**
- campo: avatar_file
  tipo: string
  destino: docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] canvas-cliente-ideal.md exists in rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    validação: |
      Check for canvas-cliente-ideal.md. If not found:
      "Para criar o Avatar Blueprint, preciso do Canvas do Cliente Ideal preenchido.
      Quer preencher agora? → *canvas-cliente"
    error_message: "Canvas do Cliente Ideal é pré-requisito. Execute *canvas-cliente primeiro."
```

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] Avatar file created at docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md
    tipo: post-condition
    blocker: true
  - [ ] All 7 questions answered
    tipo: post-condition
    blocker: true
  - [ ] Tabela Problema x Solução contains at least 8 rows
    tipo: post-condition
    blocker: true
```

---

# Avatar Blueprint — Task

## Purpose

Conduzir o usuário pelo preenchimento do Avatar Blueprint (Mapa do Avatar), com 7 perguntas que aprofundam o perfil do cliente ideal + Tabela Problema x Solução (8+ linhas). Este artefato alimenta diretamente o roteiro do webinário: Headline, Empatia, Conteúdo, Pitch.

## SEQUENTIAL Task Execution

### 0. Setup e Cross-Reference

- Detectar rodada ativa
- Carregar `canvas-cliente-ideal.md` — extrair: público, dor principal, tentativas, objeções
- Informar: "Carreguei o Canvas do Cliente Ideal. Vou usar as informações do seu público para dar contexto a cada pergunta."
- Carregar knowledge base: `docs/METHODOLOGY-ANALYSIS.md` linhas L1722-L1866

### 1. Introdução ao Avatar Blueprint

> **Avatar Blueprint — Mapa do Avatar**
>
> Agora vamos APROFUNDAR o perfil do seu cliente ideal. São 7 perguntas
> que vão além do Canvas do Cliente — aqui entramos nos desejos, frustrações
> e motivações mais profundas.
>
> Cada pergunta alimenta uma parte específica do roteiro:
> - Pergunta 1 (Desejos) → Headline + Lista de Aprendizado
> - Pergunta 2 (Por que querem) → Empatia + Conteúdo
> - Pergunta 3 (Obstáculos) → Identificação + Falsas Crenças
> - Pergunta 4 (Frustrações) → Espelhamento + História
> - Pergunta 5 (Tendências) → Posicionamento
> - Pergunta 6 (Desejos ocultos) → Pitch + Urgência
> - Pergunta 7 (Razões para NÃO comprar) → Objeções + Garantia
>
> Ao final, montamos a Tabela Problema x Solução com suas "Cartas na Manga".

### 2. Conduzir as 7 Perguntas

#### Pergunta 1: Top 3 Desejos

```
Quais são os TOP 3 DESEJOS do seu avatar?

{Se canvas-cliente existe: "Do Canvas do Cliente Ideal, o resultado desejado é: '{resultado_desejado}'."}

Os desejos alimentam a Headline do webinário e a Lista de Aprendizado na abertura.
Pense no que eles querem CONQUISTAR (positivo), não apenas no que querem evitar.

Liste os 3 maiores desejos:
1.
2.
3.
```

**Alimenta:** Headline + Lista de Aprendizado + Transformação

#### Pergunta 2: Por que querem isso?

```
POR QUE eles querem alcançar esses desejos?

Qual é a motivação REAL por trás? O que muda na vida deles quando conseguem?
Isso vai além do resultado — é sobre o que o resultado SIGNIFICA.

Exemplo: "Não querem só emagrecer — querem se sentir confiantes na praia com os filhos"

Por que eles querem isso?
```

**Alimenta:** Empatia + Conteúdo

#### Pergunta 3: O que os atrapalha?

```
O que ATRAPALHA seu avatar de conquistar esses desejos?

{Se canvas-cliente existe: "Do Canvas do Cliente, eles já tentaram: '{tentativas}'
e não funcionou porque: '{por_que_nao_funcionou}'"}

Pense em obstáculos INTERNOS (crenças, medos, hábitos) e EXTERNOS (tempo, dinheiro, ferramentas).

O que os impede de avançar?
```

**Alimenta:** Identificação + False Beliefs (Vehicle/Internal/External)

#### Pergunta 4: Frustrações diárias

```
Quais são as FRUSTRAÇÕES DIÁRIAS do seu avatar relacionadas a esse tema?

Essas frustrações serão usadas para criar ESPELHAMENTO na seção de Empatia.
Quando a pessoa ouve suas frustrações descritas com precisão, pensa: "Essa pessoa me entende!"

Descreva 3-5 frustrações do dia-a-dia:
```

**Alimenta:** Espelhamento + História (seção Empatia)

#### Pergunta 5: Tendências que seguem

```
Que TENDÊNCIAS, influenciadores ou movimentos seu avatar segue?

Isso ajuda no posicionamento: seu produto precisa se alinhar com
o que eles já acreditam e valorizam.

Que tendências, gurus ou movimentos eles acompanham?
```

**Alimenta:** Posicionamento do webinário

#### Pergunta 6: Desejos ocultos

```
Quais são os DESEJOS OCULTOS do seu avatar?

Desejos ocultos são o que eles querem mas NÃO falam abertamente.
São motivações mais profundas: status, aprovação social, vingança contra descrença, etc.

Exemplo: "O empresário não quer só faturar mais — quer provar para o sócio que saiu que ele estava certo"

Quais desejos ocultos seu avatar tem?
```

**Alimenta:** Pitch + Urgência (gatilhos emocionais)

#### Pergunta 7: Razões para NÃO comprar

```
Quais as razões que seu avatar daria para NÃO COMPRAR seu produto?

{Se canvas-cliente existe: "Objeções já mapeadas: '{objecoes}'"}

Essas razões viram as objeções do pitch — cada uma será respondida diretamente.
Também alimentam a seção de Garantia.

Liste todas as razões/desculpas para não comprar:
```

**Alimenta:** Objeções + Garantia (seção Pitch)

### 3. Tabela Problema x Solução

```
Agora vamos montar a TABELA PROBLEMA x SOLUÇÃO.

Para cada problema do seu avatar, qual é a "Carta na Manga" — a solução
que você oferece dentro do seu produto?

Mínimo: 8 linhas. Idealmente 10-15.

{Dados importados para ajudar:
- Dor principal: {dor_principal}
- Obstáculos: {obstaculos}
- Frustrações: {frustracoes}}

Formato:
| Problema | Solução ("Carta na Manga") |
|----------|---------------------------|
| {problema_1} | {solução_1} |
| ... | ... |

Liste os pares Problema → Solução:
```

### 4. One Big Domino (Conceito Brunson)

```
Agora vamos identificar o ONE BIG DOMINO.

Segundo Russell Brunson, se você conseguir derrubar UMA crença,
todas as outras caem como dominós.

Baseado nas respostas anteriores:
- Desejos: {desejos}
- Obstáculos: {obstaculos}
- Falsas crenças implícitas: {falsas_crencas}

Qual é a ÚNICA crença que, se a pessoa acreditar, resolve todas as objeções?

Dica: Geralmente é algo como: "Se eu acreditar que {mecanismo_único} funciona para pessoas como eu, todas as outras objeções desaparecem."

Qual é o One Big Domino?
```

### 5. Gerar Avatar Blueprint

- Carregar template: `.aiox-core/development/templates/webinar-avatar-blueprint-tmpl.md`
- Preencher com respostas do usuário + dados importados + tabela + One Big Domino
- Salvar em: `docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md`

### 6. Apresentar Resumo e Próximo Passo

```
Avatar Blueprint salvo em:
docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md

Resumo:
- Top 3 desejos: [resumo]
- Obstáculos principais: [resumo]
- Problemas mapeados: [quantidade] na Tabela P×S
- One Big Domino: [resumo]
- Objeções para o pitch: [quantidade]

Próximo passo recomendado:
→ *canvas-webinar — para definir a estrutura completa do webinário (requer este avatar + canvas-produto)
→ *orcamento — para calcular metas e investimento
```

---

## Error Handling

1. **Error:** canvas-cliente-ideal.md not found
   - **Resolution:** "Preciso do Canvas do Cliente Ideal primeiro. Execute *canvas-cliente"
   - **Recovery:** Redirect to *canvas-cliente

2. **Error:** Tabela Problema x Solução has less than 8 rows
   - **Resolution:** "A metodologia recomenda mínimo 8 pares. Tente pensar em mais problemas."
   - **Recovery:** Offer brainstorming prompts based on frustrações e obstáculos

---

## Handoff

```yaml
next_agent: "@webinar-strategist"
next_command: "*canvas-webinar"
condition: Avatar Blueprint preenchido e Canvas do Produto disponível
alternatives:
  - agent: "@webinar-strategist"
    command: "*orcamento"
    condition: "Quer calcular orçamento antes do Canvas do Webinário"
  - agent: "@webinar-creator"
    command: "*abertura"
    condition: "Já tem canvas-produto e quer começar a construir"
```

---

## Metadata

```yaml
version: 1.0.0
squad: webinar
agent: webinar-strategist
command: "*avatar"
prd_reference: "PRD v2.1, Seção 3.2 — Avatar Blueprint (7 perguntas + Tabela P×S)"
methodology_reference: "Seção 5.1.1 — METHODOLOGY-ANALYSIS.md L1722-L1866"
tags:
  - webinar
  - planning
  - avatar
  - blueprint
updated_at: 2026-03-05
```
