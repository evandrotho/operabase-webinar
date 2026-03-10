---

## Task Definition

```yaml
task: webinarCreatorMensagens()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "espiral-engajamento"
      lines: "L35-L41"
      purpose: "Pilar 2: Engajamento — nutrição"
    - id: "espiral-compromisso"
      lines: "L42-L48"
      purpose: "Pilar 3: Compromisso — antecipação"
    - id: "etapa-nutricao"
      lines: "L526-L685"
      purpose: "Etapa 2: Nutrição — 5 mensagens"
    - id: "etapa-antecipacao"
      lines: "L686-L890"
      purpose: "Etapa 3: Antecipação — 9 mensagens (D-1 e D-0)"
    - id: "etapa-abertura-carrinho"
      lines: "L891-L984"
      purpose: "Etapa 4: Abertura do Carrinho — 1 mensagem pós"
    - id: "etapa-ampliacao"
      lines: "L985-L1197"
      purpose: "Etapa 5: Ampliação — 7 mensagens"
    - id: "etapa-fechamento"
      lines: "L1198-L1463"
      purpose: "Etapa 6: Fechamento — 11 mensagens"
    - id: "etapa-impulsionamento"
      lines: "L1464-L1651"
      purpose: "Etapa 7: Impulsionamento — 8 mensagens downsell"

inputs:
  required:
    - campo: canvas-produto.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-produto.md
      purpose: "Nome do produto, Grande Promessa, Mecanismo Único — variáveis dinâmicas"
    - campo: avatar-blueprint.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md
      purpose: "Desejos, frustrações, linguagem do público — tom das mensagens"
  optional:
    - campo: orcamento-meta.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/orcamento-meta.md
      purpose: "Datas, valores, condições — personalização de variáveis"

output:
  path: docs/webinar/rodada-{N}/conteudo/mensagens-whatsapp.md
  template: webinar-mensagens-whatsapp-tmpl.md
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] canvas-produto.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *canvas-produto"
    error_message: "Para gerar as mensagens, preciso do Canvas do Produto (nome, promessa, mecanismo). Quer preencher agora?"
  - [ ] avatar-blueprint.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *avatar"
    error_message: "Para gerar as mensagens, preciso do Avatar Blueprint (linguagem do público). Quer preencher agora?"
```

---

## Task Execution — Interactive (elicit: true)

### Step 0: Detectar Rodada Ativa e Carregar Knowledge Base

- Verificar rodada ativa em `docs/webinar/`
- Carregar knowledge base: todas as seções de mensagens (L526-L1651)

### Step 1: Carregar Inputs e Extrair Variáveis Dinâmicas

- Ler `canvas-produto.md` — extrair:
  - `{{produto}}` — nome do produto
  - `{{mecanismo}}` — Nome do Mecanismo Único
  - `{{promessa}}` — Grande Promessa
- Ler `avatar-blueprint.md` — extrair:
  - Tom de voz adequado ao público
  - Palavras-chave do universo do avatar
  - Desejos e frustrações para personalização
- Se `orcamento-meta.md` existir, extrair:
  - `{{preco}}` — ticket do produto
  - `{{bonus}}` — bônus definidos
  - Datas planejadas

### Step 2: Coletar Variáveis Personalizadas (elicit)

**Elicitation:**
```
Para personalizar as 41+ mensagens de WhatsApp, preciso de algumas informações:

1. **Nome do expert/apresentador:** (como assinar as mensagens)
2. **Data do webinário:** (ou "a definir" se ainda não sabe)
3. **Link da página de captura:** (ou "{{link}}" como placeholder)
4. **Presente/recompensa por participar:** (ex: e-book, planilha, desconto)
   Se não tiver, posso sugerir baseado no seu nicho.
5. **Tom de comunicação preferido:**
   a) Formal e profissional
   b) Amigável e próximo
   c) Direto e urgente
```

### Step 3: Gerar Mensagens de Nutrição — 5 mensagens (auto)

**Etapa do Funil:** Nutrição | **Pilar da Espiral:** Engajamento

Gerar 5 mensagens de nutrição seguindo a metodologia:
1. **Boas-vindas + expectativa** — agradecer inscrição, criar expectativa
2. **Conteúdo de valor #1** — dica/insight que demonstra expertise
3. **Conteúdo de valor #2** — história/case que gera identificação
4. **Prova social** — resultados de alunos/clientes
5. **Lembrete + conteúdo** — "seu webinário é em X dias" + dica final

Cada mensagem: 3-5 parágrafos curtos, adequada para WhatsApp (sem parágrafos longos).

### Step 4: Gerar Mensagens de Antecipação D-1 — 2 mensagens (auto)

**Etapa do Funil:** Antecipação | **Pilar da Espiral:** Compromisso

1. **D-1 Manhã:** Lembrete + expectativa + "amanhã sua vida pode mudar"
2. **D-1 Noite:** Urgência + instrução prática ("separe X minutos amanhã")

### Step 5: Gerar Mensagens de Antecipação D-0 — 7 mensagens (auto)

**Etapa do Funil:** Antecipação | **Pilar da Espiral:** Compromisso

1. **D-0 Manhã cedo:** "Hoje é o dia!" + motivação
2. **D-0 2h antes:** Lembrete prático + link
3. **D-0 1h antes:** Contagem regressiva + instrução
4. **D-0 30min antes:** "Faltam 30 minutos" + link
5. **D-0 15min antes:** "Estamos quase ao vivo" + link
6. **D-0 Início:** "Estamos ao vivo! Entre agora:" + link
7. **D-0 10min após início:** "Já começou! Ainda dá tempo:" + link

### Step 6: Gerar Mensagem Pós-Webinário — 1 mensagem (auto)

**Etapa do Funil:** Abertura do Carrinho | **Pilar da Espiral:** Persuasão

1. **Pós-imediato:** Agradecimento + replay (se aplicável) + CTA para oferta

### Step 7: Gerar Mensagens de Ampliação — 7 mensagens (auto)

**Etapa do Funil:** Ampliação do Impacto | **Pilar da Espiral:** Urgência

1. **D+1 Manhã:** Replay disponível + depoimento
2. **D+1 Tarde:** "Assista o momento [timestamp] — essa parte é crucial"
3. **D+2 Manhã:** Novo depoimento + CTA
4. **D+2 Tarde:** FAQ (objeção mais comum respondida)
5. **D+3 Manhã:** Bastidores / história pessoal + CTA
6. **D+3 Tarde:** Bônus exclusivo para quem está na dúvida
7. **D+4:** Último lembrete antes do fechamento

### Step 8: Gerar Mensagens de Fechamento — 11 mensagens (auto)

**Etapa do Funil:** Fechamento do Carrinho | **Pilar da Espiral:** Escassez

1. **D+5 Manhã:** "Último dia" + resumo da oferta
2. **D+5 10h:** Depoimento forte + CTA
3. **D+5 12h:** "Faltam 12 horas" + bônus que expira
4. **D+5 14h:** FAQ final (3 perguntas mais frequentes)
5. **D+5 16h:** "Faltam 8 horas" + prova social
6. **D+5 18h:** "Faltam 6 horas" + garantia reforçada
7. **D+5 20h:** "Faltam 4 horas" + escassez real
8. **D+5 21h:** "Faltam 3 horas" + último depoimento
9. **D+5 22h:** "Faltam 2 horas" + custo de não agir
10. **D+5 23h:** "Última hora" + urgência máxima
11. **D+5 23:45:** "Últimos 15 minutos" + CTA final

### Step 9: Gerar Mensagens de Downsell — 8 mensagens (auto)

**Etapa do Funil:** Impulsionamento do Lucro | **Pilar da Espiral:** Persuasão + Urgência

1. **D+6 Manhã:** "Carrinho fechou, MAS..." + oferta alternativa
2. **D+6 Tarde:** Explicação do downsell + valor
3. **D+7 Manhã:** Depoimento de quem começou pelo downsell
4. **D+7 Tarde:** Comparação: investimento vs. resultado
5. **D+8 Manhã:** "Última chance para a oferta especial"
6. **D+8 Tarde:** "Faltam X horas para esta oferta"
7. **D+9 Manhã:** "Hoje é o último dia"
8. **D+9 Noite:** Fechamento final do downsell

### Step 10: Revisar e Apresentar Resumo (elicit)

**Elicitation:**
```
Biblioteca de mensagens WhatsApp gerada!

Resumo:
- Nutrição: 5 mensagens (engajamento)
- Antecipação D-1: 2 mensagens (compromisso)
- Antecipação D-0: 7 mensagens (compromisso)
- Pós-Webinário: 1 mensagem (persuasão)
- Ampliação: 7 mensagens (urgência)
- Fechamento: 11 mensagens (escassez)
- Downsell: 8 mensagens (persuasão + urgência)
Total: 41 mensagens

Variáveis dinâmicas usadas:
- {{nome_expert}}: [valor]
- {{data_webinario}}: [valor]
- {{link}}: [valor]
- {{produto}}: [valor]
- {{preco}}: [valor]
- {{bonus}}: [valor]
- {{presente}}: [valor]

Quer revisar alguma etapa específica? (digite o nome: nutricao, d1, d0, pos, ampliacao, fechamento, downsell)
Ou "ok" para salvar.
```

### Step 11: Compilar e Salvar

- Usar template `webinar-mensagens-whatsapp-tmpl.md`
- Salvar em `docs/webinar/rodada-{N}/conteudo/mensagens-whatsapp.md`
- Informar: "Mensagens prontas! Próximo: `*copy-captura` para criar a página de captura, ou handoff para @webinar-operator."

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] mensagens-whatsapp.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Contém 41+ mensagens organizadas por etapa do funil
    tipo: post-condition
    blocker: true
  - [ ] Cada mensagem associada ao pilar da Espiral de Vendas
    tipo: post-condition
    blocker: true
  - [ ] Variáveis dinâmicas claramente marcadas com {{}}
    tipo: post-condition
    blocker: true
```

---

## Handoff

```yaml
next_agent: webinar-creator
next_command: "*copy-captura"
condition: "Mensagens completas — gerar copy de páginas"
alternatives:
  - agent: webinar-operator
    command: "*setup-sendflow"
    condition: "Mensagens prontas, ir para configuração do SendFlow"
  - agent: webinar-operator
    command: "*timeline"
    condition: "Roteiro + mensagens prontos, montar cronograma"
```

---

## Performance

```yaml
duration_expected: 15-25 min (geração em lote com revisão)
token_usage: ~20,000-40,000 tokens (41+ mensagens completas)
```
