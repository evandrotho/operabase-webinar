---

## Task Definition

```yaml
task: webinarCreatorConteudo()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "conteudo-3-secrets"
      lines: "L2252-L2471"
      purpose: "Seção 5.4: Conteúdo (3 Secrets + False Beliefs) — Vehicle, Internal, External"
    - id: "espiral-persuasao"
      lines: "L49-L55"
      purpose: "Pilar 4: Persuasão — contexto para estrutura de conteúdo"

inputs:
  required:
    - campo: avatar-blueprint.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md
      purpose: "Objeções (campo 7) — base para classificar False Beliefs em Vehicle/Internal/External"
    - campo: canvas-webinar.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-webinar.md
      purpose: "Blocos 10-11: Crença-alvo e Ponte de Crenças — estrutura central do conteúdo"
  optional:
    - campo: canvas-cliente-ideal.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-cliente-ideal.md
      purpose: "Tabela Problema × Solução — enriquece False Beliefs"

output:
  path: docs/webinar/rodada-{N}/conteudo/roteiro-conteudo.md
  template: webinar-roteiro-conteudo-tmpl.md
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] avatar-blueprint.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *avatar"
    error_message: "Para construir o Conteúdo, preciso do Avatar Blueprint (objeções para False Beliefs). Quer preencher agora?"
  - [ ] canvas-webinar.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *canvas-webinar"
    error_message: "Para construir o Conteúdo, preciso do Canvas do Webinário (crença-alvo e ponte de crenças). Quer preencher agora?"
```

---

## Task Execution — Interactive (elicit: true)

### Step 0: Detectar Rodada Ativa e Carregar Knowledge Base

- Verificar rodada ativa em `docs/webinar/`
- Carregar knowledge base: linhas L2252-L2471 (Conteúdo 3 Secrets)

### Step 1: Carregar Inputs e Classificar False Beliefs

- Ler `avatar-blueprint.md` — extrair campo 7: "Razões para NÃO comprar" (objeções)
- Ler `canvas-webinar.md` — extrair bloco 10 (crença-alvo) e bloco 11 (ponte de crenças)
- Se `canvas-cliente-ideal.md` existir, puxar Tabela Problema × Solução

**Classificar objeções em 3 categorias:**
- **Vehicle (Veículo):** Falsas crenças sobre O QUE fazer — "Isso não funciona", "Esse método é furado"
- **Internal (Interno):** Falsas crenças sobre capacidade pessoal — "Não sou capaz", "Não tenho tempo"
- **External (Externo):** Falsas crenças sobre obstáculos externos — "É muito caro", "Meu mercado é diferente"

### Step 2: Apresentar Classificação de False Beliefs (elicit)

**Elicitation:**
```
Analisei as objeções do seu Avatar Blueprint e classifiquei em 3 categorias.
Cada categoria vai virar uma seção do seu conteúdo (os "3 Secrets"):

**SECRET 1 — Vehicle (O QUE fazer):**
Falsa crença: "[falsa crença sobre o método/veículo]"
Nova crença: "[nova crença que você vai plantar]"

**SECRET 2 — Internal (Capacidade pessoal):**
Falsa crença: "[falsa crença sobre capacidade]"
Nova crença: "[nova crença sobre capacidade]"

**SECRET 3 — External (Obstáculos externos):**
Falsa crença: "[falsa crença sobre obstáculo externo]"
Nova crença: "[nova crença sobre obstáculo]"

Essas classificações fazem sentido? Quer ajustar alguma? (digite o número para editar, ou "ok")
```

### Step 3: Construir Secret 1 — Vehicle (elicit)

Para cada Secret, seguir a estrutura:
1. **Falsa Crença** → declaração clara do que o público acredita erroneamente
2. **Nova Crença** → o que você quer que acreditem ao invés
3. **Conteúdo "O Que"** → ensinar O QUE fazer (não COMO — o produto ensina o COMO)
4. **Epiphany Bridge** → história/exemplo que mostra o momento de virada sobre esta crença
5. **Loop Aberto** → terminar com gancho para o próximo Secret

**Elicitation para Epiphany Bridge do Secret 1:**
```
Para o Secret 1 (Vehicle), preciso de uma história ou exemplo que mostre
por que o MÉTODO antigo não funciona e como o seu é diferente.

Pode ser:
- Uma história sua
- Um caso de aluno/cliente
- Um exemplo hipotético baseado em dados reais

Me conte essa história em 3-5 frases:
```

**Checklist de validação por bloco:**
- [ ] Aplicável ao público?
- [ ] A pessoa se vê fazendo?
- [ ] Nível adequado (não técnico demais)?
- [ ] Demonstra transformação possível?

### Step 4: Construir Secret 2 — Internal (elicit)

Mesma estrutura do Step 3, mas focando em crenças INTERNAS.

**Elicitation para Epiphany Bridge do Secret 2:**
```
Para o Secret 2 (Internal), preciso de uma história que mostre
que a CAPACIDADE não é o problema — é o MÉTODO.

Algo como: "Fulano também achava que não conseguia, até que..."

Me conte essa história em 3-5 frases:
```

### Step 5: Construir Secret 3 — External (elicit)

Mesma estrutura do Step 3, mas focando em obstáculos EXTERNOS.

**Elicitation para Epiphany Bridge do Secret 3:**
```
Para o Secret 3 (External), preciso de uma história que mostre
que o obstáculo externo pode ser superado.

Algo como: "Mesmo sem [recurso/tempo/dinheiro], fulano conseguiu..."

Me conte essa história em 3-5 frases:
```

### Step 6: Gerar Loops Abertos e Transições (auto)

- Gerar loop aberto após cada Secret:
  - Secret 1 → "Mas saber O QUE fazer não é suficiente se você acredita que [gancho para Secret 2]..."
  - Secret 2 → "Agora que você sabe que é capaz, falta resolver [gancho para Secret 3]..."
  - Secret 3 → "Agora que eliminamos as 3 barreiras, deixa eu te mostrar como vou te ajudar..." (transição para Pitch)

### Step 7: Aplicar Regra de Ouro e Compilar

- **Regra de ouro:** "No webinário ensine O QUE fazer. O produto ensina COMO fazer."
- Revisar cada Secret para garantir que ensina conceitos, não implementação
- Compilar tudo no template `webinar-roteiro-conteudo-tmpl.md`
- Salvar em `docs/webinar/rodada-{N}/conteudo/roteiro-conteudo.md`
- Mostrar resumo com duração estimada: 25-40 minutos
- Informar: "Conteúdo pronto! Próximo: `*pitch` para construir a seção de Pitch/Oferta (15 etapas)."

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] roteiro-conteudo.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Contém 3 Secrets completos (Vehicle, Internal, External)
    tipo: post-condition
    blocker: true
  - [ ] Cada Secret tem: Falsa Crença, Nova Crença, Conteúdo, Epiphany Bridge, Loop Aberto
    tipo: post-condition
    blocker: true
  - [ ] Respeita regra de ouro: ensina O QUE, não COMO
    tipo: post-condition
    blocker: true
```

---

## Handoff

```yaml
next_agent: webinar-creator
next_command: "*pitch"
condition: "Conteúdo completo com 3 Secrets"
alternatives:
  - agent: webinar-creator
    command: "*empatia"
    condition: "Empatia ainda não foi feita"
```

---

## Performance

```yaml
duration_expected: 20-35 min (3 blocos com elicitação cada)
token_usage: ~10,000-25,000 tokens
```
