---

## Task Definition

```yaml
task: webinarCreatorEmpatia()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "empatia-historia"
      lines: "L2040-L2251"
      purpose: "Seção 5.3: Empatia/História + Epiphany Bridge (2 modelos, 3 técnicas de transição)"

inputs:
  required:
    - campo: avatar-blueprint.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md
      purpose: "Frustrações (campo 4), desejos (campo 1), obstáculos (campo 3) — alimentam história de empatia"
  optional:
    - campo: canvas-cliente-ideal.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-cliente-ideal.md
      purpose: "Contexto do público para melhorar identificação na história"
    - campo: roteiro-abertura.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/conteudo/roteiro-abertura.md
      purpose: "Origin Story Seed do enriquecimento Brunson para continuidade"

output:
  path: docs/webinar/rodada-{N}/conteudo/roteiro-empatia.md
  template: webinar-roteiro-empatia-tmpl.md
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] avatar-blueprint.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *avatar"
    error_message: "Para construir a Empatia, preciso do Avatar Blueprint. Quer preencher agora com @webinar-strategist?"
```

---

## Task Execution — Interactive (elicit: true)

### Step 0: Detectar Rodada Ativa

- Verificar `docs/webinar/` para identificar a rodada ativa
- Carregar knowledge base: linhas L2040-L2251 (Empatia/História)

### Step 1: Carregar Inputs

- Ler `avatar-blueprint.md` — extrair: frustrações, desejos, obstáculos, soluções tentadas
- Se `roteiro-abertura.md` existir, buscar Origin Story Seed (Bloco Brunson)
- Se `canvas-cliente-ideal.md` existir, puxar contexto do público

### Step 2: Escolher Modelo de História (elicit)

**Elicitation:**
```
A seção de Empatia é onde você conta sua história para criar conexão com o público.
A metodologia oferece 2 modelos — escolha o que melhor se encaixa:

**Modelo A — Avatar Transformado (7 passos)**
Você VIVEU o problema do seu público e se transformou.
Passos: Início → Dramatização → Invalidação de Soluções → Momento da Virada → O Método → Resultado → Transição
Ideal para: quem tem uma história pessoal de superação no nicho.

**Modelo B — Socorrista (4 passos)**
Você é o especialista que AJUDA outros a resolver o problema.
Passos: Início → Caminho até Especialista → Decisão de Ajudar → Transição
Ideal para: profissionais, consultores, quem ajuda clientes.

Qual modelo se encaixa melhor? (A ou B)
```

### Step 3: Coletar História do Expert (elicit)

**Se Modelo A — Avatar Transformado:**
```
Vou te guiar pelos 7 passos da sua história. Responda uma pergunta por vez:

1. INÍCIO: Como era sua vida ANTES de resolver esse problema?
   (descreva a situação, frustrações, o que sentia)
```
Após resposta:
```
2. DRAMATIZAÇÃO: Qual foi o momento mais difícil? O "fundo do poço"?
   (episódio específico, não genérico)
```
Após resposta:
```
3. INVALIDAÇÃO: Quais soluções você tentou que NÃO funcionaram?
   (liste 2-3 coisas que tentou e por que falharam)
```
Após resposta:
```
4. MOMENTO DA VIRADA: Qual foi o momento exato de "epifania"?
   (Epiphany Bridge de Brunson: momento ESPECÍFICO, não conclusão gradual)
   Dica: "Eu estava [fazendo algo] quando [algo aconteceu] e percebi que..."
```
Após resposta:
```
5. O MÉTODO: Como você descobriu/criou a solução?
   (não precisa detalhar — só a jornada até encontrar)
```
Após resposta:
```
6. RESULTADO: Qual foi o resultado concreto da transformação?
   (números, mudanças de vida, antes/depois)
```
Após resposta:
```
7. TRANSIÇÃO: Agora vou montar a transição para o conteúdo.
```

**Se Modelo B — Socorrista:**
```
Vou te guiar pelos 4 passos da sua história. Responda uma pergunta por vez:

1. INÍCIO: Como você começou nessa área? O que te trouxe até aqui?
```
Após resposta:
```
2. CAMINHO: Como você se tornou especialista? Qual foi sua jornada?
   (formação, experiência, casos marcantes)
```
Após resposta:
```
3. DECISÃO: Por que decidiu ajudar outras pessoas com isso?
   (momento específico que te motivou — Epiphany Bridge)
```
Após resposta:
```
4. TRANSIÇÃO: Agora vou montar a transição para o conteúdo.
```

### Step 4: Escolher Técnica de Transição (elicit)

**Elicitation:**
```
Agora preciso da transição da história para o conteúdo. A metodologia oferece 3 técnicas:

1. **Espelhamento de Situação:** "Talvez você esteja passando por algo parecido..."
   Conecta a SUA história com a SITUAÇÃO do público.

2. **Espelhamento de Sentimento:** "Talvez você esteja se sentindo [emoção]..."
   Conecta a SUA história com os SENTIMENTOS do público.

3. **História Disfarçada de Conteúdo:** A história já ensina algo útil,
   e a transição é natural: "E foi assim que descobri o primeiro segredo..."

Qual técnica quer usar? (1, 2 ou 3)
```

### Step 5: Gerar Epiphany Bridge (auto)

- Estruturar o momento de epifania no formato Brunson:
  - "Eu estava [contexto] quando [evento específico] e percebi que [insight]"
  - DEVE ser um momento ESPECÍFICO, não uma conclusão gradual
  - Usar as respostas do Step 3 (momento da virada) como base

### Step 6: Compilar e Salvar

- Montar a seção de Empatia com:
  - Modelo escolhido (A ou B) com todos os passos preenchidos
  - Técnica de transição escolhida
  - Epiphany Bridge formatado
  - Alerta de duração: "5-10 minutos no máximo. Remover história aumenta retenção mas destrói conversão."
- Usar template `webinar-roteiro-empatia-tmpl.md`
- Salvar em `docs/webinar/rodada-{N}/conteudo/roteiro-empatia.md`
- Informar: "Empatia pronta! Próximo: `*conteudo` para construir a seção de Conteúdo (3 Secrets)."

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] roteiro-empatia.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Contém modelo de história completo (A ou B)
    tipo: post-condition
    blocker: true
  - [ ] Contém Epiphany Bridge estruturado
    tipo: post-condition
    blocker: true
  - [ ] Contém técnica de transição
    tipo: post-condition
    blocker: true
```

---

## Handoff

```yaml
next_agent: webinar-creator
next_command: "*conteudo"
condition: "Empatia completa"
alternatives:
  - agent: webinar-creator
    command: "*abertura"
    condition: "Abertura ainda não foi feita"
```

---

## Performance

```yaml
duration_expected: 15-25 min (muita elicitação de história pessoal)
token_usage: ~8,000-20,000 tokens
```
