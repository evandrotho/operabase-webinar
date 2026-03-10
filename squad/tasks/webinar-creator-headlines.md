---

## Task Definition

```yaml
task: webinarCreatorHeadlines()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "abertura-7-blocos"
      lines: "L1867-L2039"
      purpose: "Seção 5.2: Fórmulas de headline — 3 fórmulas principais + variações"
    - id: "etapa-captacao"
      lines: "L451-L525"
      purpose: "Etapa 1: Captação — headlines para página de captura"

inputs:
  required:
    - campo: avatar-blueprint.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md
      purpose: "Campos 1 (desejos) e 3 (obstáculos) — matéria-prima para headlines"
  optional:
    - campo: canvas-produto.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-produto.md
      purpose: "Grande Promessa, Mecanismo Único — enriquece headlines"

output:
  path: docs/webinar/rodada-{N}/conteudo/headlines.md
  template: null
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] avatar-blueprint.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *avatar"
    error_message: "Para gerar headlines, preciso do Avatar Blueprint (desejos e obstáculos). Quer preencher agora?"
```

---

## Task Execution — Interactive (elicit: true)

### Step 0: Detectar Rodada Ativa e Carregar Knowledge Base

- Verificar rodada ativa em `docs/webinar/`
- Carregar knowledge base: linhas L1867-L2039 (fórmulas de headline)

### Step 1: Carregar Inputs

- Ler `avatar-blueprint.md` — extrair:
  - Campo 1: Top 3 desejos
  - Campo 3: O que atrapalha (obstáculos)
  - Campo 4: Frustrações diárias
  - Campo 6: Desejos ocultos
- Se `canvas-produto.md` existir, extrair: Grande Promessa, Mecanismo Único, Nome do Mecanismo

### Step 2: Definir Contexto de Uso (elicit)

**Elicitation:**
```
Para quais peças você precisa de headlines?

1. Webinário (slide de abertura)
2. Página de captura (headline principal)
3. Anúncios (Facebook/Instagram ads)
4. Mensagens WhatsApp (assunto/gancho)
5. Todas as acima

Escolha uma ou mais opções (ex: 1,2,3):
```

### Step 3: Gerar Headlines por Fórmula (auto)

Usando os dados do Avatar Blueprint, gerar variações por fórmula:

**Fórmula 1 — "Como X sem Y"**
- Template: "Como [resultado desejado] sem [obstáculo principal]"
- Gerar 5 variações combinando diferentes desejos e obstáculos

**Fórmula 2 — "Como X mesmo que Z"**
- Template: "Como [resultado desejado] mesmo que [limitação percebida]"
- Gerar 5 variações usando frustrações e crenças limitantes

**Fórmula 3 — "Como X em T"**
- Template: "Como [resultado desejado] em [prazo realista]"
- Gerar 5 variações com diferentes prazos

**Fórmula 4 — Identificação + Desejo**
- Template: "Se você é [perfil] e quer [desejo]..."
- Gerar 3 variações

**Fórmula 5 — Frustração + Medo**
- Template: "Cansado de [frustração]? Descubra como [solução]"
- Gerar 3 variações

**Fórmula 6 — Mecanismo Único** (se Canvas do Produto disponível)
- Template: "O método [Nome do Mecanismo] que [resultado] sem [obstáculo]"
- Gerar 3 variações

### Step 4: Apresentar e Selecionar (elicit)

**Elicitation:**
```
Gerei [X] variações de headlines organizadas por fórmula.

**Fórmula 1 — "Como X sem Y":**
1. [headline]
2. [headline]
3. [headline]
4. [headline]
5. [headline]

**Fórmula 2 — "Como X mesmo que Z":**
6. [headline]
7. [headline]
...

**Top 3 Recomendadas** (baseado em clareza + impacto + especificidade):
- Para webinário: #[N]
- Para página de captura: #[N]
- Para anúncios: #[N]

Quer que eu salve todas ou apenas as selecionadas?
Quer que eu gere mais variações de alguma fórmula específica?
```

### Step 5: Compilar e Salvar

- Salvar todas as headlines geradas em `docs/webinar/rodada-{N}/conteudo/headlines.md`
- Formato: organizado por fórmula, com marcação das selecionadas
- Incluir nota: "Headlines selecionadas estão marcadas com [SELECIONADA]"
- Informar: "Headlines prontas! Estas podem ser usadas em: `*abertura` (slide), `*copy-captura` (página), anúncios."

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] headlines.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Contém variações organizadas por fórmula
    tipo: post-condition
    blocker: true
  - [ ] Headlines top 3 recomendadas marcadas
    tipo: post-condition
    blocker: false
```

---

## Handoff

```yaml
next_agent: webinar-creator
next_command: "*copy-captura"
condition: "Headlines prontas — usar na página de captura"
alternatives:
  - agent: webinar-creator
    command: "*abertura"
    condition: "Usar headline no roteiro de abertura"
```

---

## Performance

```yaml
duration_expected: 10-15 min
token_usage: ~5,000-10,000 tokens
```
