---

## Task Definition

```yaml
task: webinarCreatorAbertura()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "abertura-7-blocos"
      lines: "L1867-L2039"
      purpose: "Seção 5.2: Abertura (7 Blocos + Brunson enriquecido com One Thing + Origin Story)"
    - id: "espiral-persuasao"
      lines: "L49-L55"
      purpose: "Pilar 4: Persuasão — contexto para estrutura de abertura"

inputs:
  required:
    - campo: avatar-blueprint.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md
      purpose: "Desejos (campo 1), obstáculos (campo 3), objeções (campo 7) — alimentam Headline, Identificação"
    - campo: canvas-produto.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-produto.md
      purpose: "Grande Promessa, Mecanismo Único, Nome do Mecanismo — alimentam Headline, Método"
  optional:
    - campo: canvas-webinar.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-webinar.md
      purpose: "Blocos 1-7 (tema, título, objetivo, público, formato) — enriquece contexto geral"

output:
  path: docs/webinar/rodada-{N}/conteudo/roteiro-abertura.md
  template: webinar-roteiro-abertura-tmpl.md
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] avatar-blueprint.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *avatar"
    error_message: "Para construir a Abertura, preciso do Avatar Blueprint. Quer preencher agora com @webinar-strategist?"
  - [ ] canvas-produto.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *canvas-produto"
    error_message: "Para construir a Abertura, preciso do Canvas do Produto. Quer preencher agora com @webinar-strategist?"
```

---

## Task Execution — Interactive (elicit: true)

### Step 0: Detectar Rodada Ativa

- Verificar `docs/webinar/` para identificar a rodada ativa (rodada-1, rodada-2, etc.)
- Se nenhuma rodada existir, criar `docs/webinar/rodada-1/conteudo/`
- Se múltiplas existirem, perguntar qual rodada usar

### Step 1: Carregar Inputs

- Ler `avatar-blueprint.md` — extrair: Top 3 desejos, obstáculos, frustrações, razões para NÃO comprar
- Ler `canvas-produto.md` — extrair: Grande Promessa, Mecanismo Único, Nome do Mecanismo, Diferencial
- Se `canvas-webinar.md` existir, ler blocos 1-7 para contexto adicional
- Carregar knowledge base: linhas L1867-L2039 (Abertura 7 Blocos)

### Step 2: Bloco 1 — Headline (elicit)

Gerar 3 variações de headline usando as fórmulas da metodologia:

1. **"Como [resultado] sem [obstáculo]"** — puxa desejos do Avatar (campo 1) e obstáculos (campo 3)
2. **"Como [resultado] mesmo que [limitação]"** — puxa desejos e frustrações (campo 4)
3. **"Como [resultado] em [tempo]"** — puxa desejos e prazo realista

**Elicitation:**
```
Gerei 3 opções de headline para a abertura do seu webinário:

1. [headline opção 1]
2. [headline opção 2]
3. [headline opção 3]

Qual você prefere? (1, 2 ou 3) — ou descreva uma variação personalizada.
```

### Step 3: Bloco 2 — Método (auto)

- Gerar apresentação do Mecanismo Único usando dados do Canvas do Produto
- Formato: "Hoje vou te mostrar [Nome do Mecanismo Único] — [descrição breve de como funciona]"
- Incluir alerta: o Mecanismo deve gerar curiosidade, não explicar tudo

### Step 4: Bloco 3 — Apresentação Pessoal (elicit)

**Elicitation:**
```
Agora preciso montar sua apresentação pessoal para o webinário.
O "Teste do Palco" diz: apresente credenciais que o PÚBLICO considera relevantes.
O "Balelômetro" alerta: NÃO liste títulos demais — causa descrença.

Me conte:
1. Qual sua principal credencial que seu público respeita?
2. Qual resultado concreto mais impressionante que já alcançou?
3. Há quanto tempo trabalha nessa área?
```

- Com as respostas, gerar apresentação pessoal concisa (3-5 frases)

### Step 5: Bloco 4 — Lista de Aprendizado (auto)

- Gerar lista de 5-7 itens que o participante vai aprender
- Cada item deve ser um teaser dos 3 Secrets (Vehicle, Internal, External) sem revelar
- Formato: "Neste webinário, você vai descobrir: ..."
- Usar linguagem de benefício, não de feature

### Step 6: Bloco 5 — Urgência (auto)

- Gerar motivo para ficar até o final
- Fórmulas: "No final, vou revelar...", "Quem ficar até o fim vai receber..."
- Puxa do Canvas do Webinário (bônus de ação rápida) se disponível

### Step 7: Bloco 6 — Identificação (elicit)

Gerar 4 frases de identificação usando as fórmulas:

1. **Especificação + Frustração:** "Se você é [perfil] e está cansado de [frustração]..."
2. **Especificação + Desejo:** "Se você é [perfil] e quer [desejo]..."
3. **Frustração + Medo:** "Se você já tentou [solução] e tem medo de [consequência]..."
4. **Desejo Oculto:** "Se no fundo você quer [desejo oculto]..."

**Elicitation:**
```
Gerei 4 frases de identificação. Veja se representam bem seu público:

1. [frase 1]
2. [frase 2]
3. [frase 3]
4. [frase 4]

Quer ajustar alguma? (digite o número para editar, ou "ok" para aprovar todas)
```

### Step 8: Bloco 7 — Regras (auto)

- Gerar template "Isso NÃO é um daqueles..." com 3-5 diferenciações
- Formato: "Antes de começar, quero deixar claro: isso NÃO é [coisa comum]. Isso é [diferencial]."
- Puxa do Canvas do Produto: diferencial competitivo

### Step 9: Enriquecimento Brunson — One Thing + Origin Story Seed (auto)

- **One Thing Statement:** "Se você sair daqui com apenas uma coisa, que seja: [crença-alvo do Canvas do Webinário, bloco 10]"
- **Origin Story Seed:** Anotar seed para a seção de Empatia — "Na seção de Empatia, usar esta história de origem como base: [resumo de como o expert descobriu o método]"
- Se canvas-webinar não disponível, gerar One Thing genérico baseado no Mecanismo Único

### Step 10: Compilar e Salvar

- Compilar todos os 7 blocos + enriquecimento Brunson no template `webinar-roteiro-abertura-tmpl.md`
- Salvar em `docs/webinar/rodada-{N}/conteudo/roteiro-abertura.md`
- Mostrar resumo ao usuário com duração estimada: 5-10 minutos
- Informar próximo passo: "Abertura pronta! Próximo: `*empatia` para construir a seção de Empatia/História."

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] roteiro-abertura.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Arquivo contém todos os 7 blocos + enriquecimento Brunson
    tipo: post-condition
    blocker: true
  - [ ] Headline escolhida pelo usuário registrada
    tipo: post-condition
    blocker: false
```

---

## Handoff

```yaml
next_agent: webinar-creator
next_command: "*empatia"
condition: "Abertura completa"
alternatives:
  - agent: webinar-creator
    command: "*status"
    condition: "Usuário quer ver progresso geral"
```

---

## Performance

```yaml
duration_expected: 10-20 min (interativo com usuário)
token_usage: ~5,000-15,000 tokens
```
