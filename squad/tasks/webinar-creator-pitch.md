---

## Task Definition

```yaml
task: webinarCreatorPitch()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "pitch-15-etapas"
      lines: "L2472-L2832"
      purpose: "Seção 5.5: Oferta/Pitch (15 Etapas + Stack Slide + Dupla Queda de Preço)"
    - id: "espiral-conversao"
      lines: "L56-L62"
      purpose: "Pilar 5: Conversão — contexto para estrutura de pitch"

inputs:
  required:
    - campo: canvas-webinar.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-webinar.md
      purpose: "Blocos 12-15: Oferta (ticket, condições, garantia), Entregáveis, Bônus, Objeções/Respostas"
    - campo: canvas-produto.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-produto.md
      purpose: "Grande Promessa, Mecanismo Único, Proposta de Valor — para Stack Slide"
  optional:
    - campo: orcamento-meta.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/orcamento-meta.md
      purpose: "Ticket, condições de pagamento, order bump, upsell — enriquece oferta"

output:
  path: docs/webinar/rodada-{N}/conteudo/roteiro-pitch.md
  template: webinar-roteiro-pitch-tmpl.md
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] canvas-webinar.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *canvas-webinar"
    error_message: "Para construir o Pitch, preciso do Canvas do Webinário (oferta, entregáveis, bônus, garantia). Quer preencher agora?"
  - [ ] canvas-produto.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *canvas-produto"
    error_message: "Para construir o Pitch, preciso do Canvas do Produto (proposta de valor para Stack Slide). Quer preencher agora?"
```

---

## Task Execution — Interactive (elicit: true)

### Step 0: Detectar Rodada Ativa e Carregar Knowledge Base

- Verificar rodada ativa em `docs/webinar/`
- Carregar knowledge base: linhas L2472-L2832 (Pitch 15 Etapas)

### Step 1: Carregar Inputs

- Ler `canvas-webinar.md` — extrair blocos 12-15:
  - Bloco 12: Oferta (ticket, condições, garantia)
  - Bloco 13: Entregáveis (nome + descrição + valor R$)
  - Bloco 14: Bônus (nome + descrição + valor R$)
  - Bloco 15: Objeções (pares objeção/resposta)
- Ler `canvas-produto.md` — extrair Grande Promessa, Mecanismo Único, Proposta de Valor
- Se `orcamento-meta.md` existir, puxar ticket, condições, bump/upsell/downsell

### Step 2: Etapa 1 — Transição do Conteúdo para Pitch (elicit)

**Elicitation:**
```
A transição do conteúdo para o pitch é crucial — feita errado, você perde a audiência.
A metodologia oferece 3 técnicas:

1. **Técnica A — Permissão:** "Posso te mostrar como eu faço isso no dia a dia?"
2. **Técnica B — Revelação:** "O que eu te mostrei até agora é O QUE fazer. Agora vou te mostrar COMO..."
3. **Técnica C — Ajuda direta:** "Deixa eu te ajudar a colocar tudo isso em prática..."

Qual técnica quer usar? (1, 2 ou 3)
```

### Step 3: Etapas 2-3 — Como vai ajudar + Transformação (auto)

- **Etapa 2:** Gerar texto "Como vai ajudar" usando Grande Promessa + Mecanismo Único
- **Etapa 3:** Gerar texto "Transformação" — antes/depois usando dados do Avatar Blueprint (se disponível)

### Step 4: Etapa 4 — Stack Slide (elicit)

Montar composição do Stack Slide usando entregáveis do Canvas do Webinário (bloco 13):

**Elicitation:**
```
Vou montar o Stack Slide — a apresentação visual de tudo que o cliente recebe.

Para cada módulo/entregável, preciso do formato:
[Nome do Módulo] → [O que vai aprender] + [Benefício direto]

Seus entregáveis do Canvas do Webinário:
{lista de entregáveis com nome, descrição e valor}

Quer ajustar algum nome ou descrição para ficar mais atraente? (digite o número para editar, ou "ok")
```

- Gerar Stack Slide com formato:
  - Módulo 1: [Nome] — [Aprendizado] + [Benefício] — Valor: R$ [valor]
  - Módulo 2: ...
  - Total do Stack: R$ [soma]

### Step 5: Etapa 5 — Dupla Queda de Preço (auto)

Gerar sequência de Dupla Queda de Preço:
1. **Âncora Alta:** "Se você somasse tudo isso, o valor seria R$ [soma do stack]"
2. **Preço Oficial:** "Mas você não vai pagar R$ [soma]. O valor oficial é R$ [preço oficial]"
3. **Preço Promocional:** "E hoje, neste webinário, o investimento é de apenas R$ [preço promocional]"

### Step 6: Etapa 6 — CTA Principal (auto)

- Gerar CTA principal claro e direto
- Formato: "Clique no botão abaixo / Acesse o link na descrição"
- Incluir instrução visual (onde clicar, o que vai acontecer)

### Step 7: Etapas 7-9 — Bônus (elicit)

**Elicitation:**
```
Agora vamos aos bônus. Do Canvas do Webinário:

{lista de bônus com nome, descrição, valor}

Bônus de Ação Rápida (limitado):
- Tipo de limitação: quantidade, tempo ou evento?
- Qual o limite? (ex: "primeiros 20", "até meia-noite", "só quem comprar hoje")
```

- Gerar apresentação de bônus com:
  - Etapa 7: Bônus de Ação Rápida (com limitação)
  - Etapa 8: Reforço ("só esse bônus já vale...")
  - Etapa 9: Bônus adicionais (entram no Stack visual)

### Step 8: Etapa 10 — Garantia (auto)

- Puxar garantia do Canvas do Webinário (bloco 12)
- Gerar texto de garantia com formato persuasivo
- Exemplo: "Você tem [X] dias para testar. Se não gostar, devolvemos 100% do valor."

### Step 9: Etapas 11-15 — Fechamento (auto)

- **Etapa 11 — Recapitulação:** Resumo automático de todos os itens do Stack + bônus + valor total
- **Etapa 12 — Urgência/Escassez:** Gerar motivos reais (preço sobe, bônus expira, vagas limitadas)
- **Etapa 13 — Coerência:** "Se você acredita que [crença-alvo], então faz sentido agir agora"
- **Etapa 14 — Q&A:** Template de perguntas frequentes (baseado em objeções do Canvas, bloco 15)
- **Etapa 15 — CTA Final:** Último chamado à ação com urgência máxima

### Step 10: Gerar Trial Closes (auto)

- Inserir Trial Closes após cada etapa principal:
  - "Faz sentido?"
  - "Isso sozinho já valeria, não valeria?"
  - "Consegue ver como isso te ajudaria?"
- Distribuir naturalmente ao longo do pitch

### Step 11: Compilar e Salvar

- Compilar todas as 15 etapas + Trial Closes no template `webinar-roteiro-pitch-tmpl.md`
- Salvar em `docs/webinar/rodada-{N}/conteudo/roteiro-pitch.md`
- Mostrar resumo com duração estimada: 20-30 minutos
- Informar: "Pitch pronto! Agora você pode: `*roteiro` para consolidar o roteiro completo."

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] roteiro-pitch.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Contém todas as 15 etapas
    tipo: post-condition
    blocker: true
  - [ ] Stack Slide completo com valores
    tipo: post-condition
    blocker: true
  - [ ] Dupla Queda de Preço configurada
    tipo: post-condition
    blocker: true
  - [ ] Trial Closes distribuídos
    tipo: post-condition
    blocker: false
```

---

## Handoff

```yaml
next_agent: webinar-creator
next_command: "*roteiro"
condition: "Pitch completo — todas as 4 seções prontas"
alternatives:
  - agent: webinar-creator
    command: "*conteudo"
    condition: "Conteúdo ainda não foi feito"
  - agent: webinar-creator
    command: "*mensagens"
    condition: "Usuário quer gerar mensagens antes do roteiro consolidado"
```

---

## Performance

```yaml
duration_expected: 20-35 min (Stack Slide e bônus requerem interação)
token_usage: ~12,000-30,000 tokens
```
