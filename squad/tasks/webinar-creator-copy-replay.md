---

## Task Definition

```yaml
task: webinarCreatorCopyReplay()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "etapa-ampliacao"
      lines: "L985-L1197"
      purpose: "Etapa 5: Ampliação do Impacto — página de replay com regras específicas"

inputs:
  required:
    - campo: roteiro-completo.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/conteudo/roteiro-completo.md
      purpose: "Timestamps dos momentos-chave para usar como headlines de venda"
    - campo: canvas-webinar.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-webinar.md
      purpose: "Oferta, produto, CTA — informações da oferta para a página"

output:
  path: docs/webinar/rodada-{N}/conteudo/copy-pagina-replay.md
  template: webinar-copy-replay-tmpl.md
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] roteiro-completo.md exists in docs/webinar/rodada-{N}/conteudo/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-creator *roteiro"
    error_message: "Para gerar a copy de replay, preciso do roteiro completo (timestamps). Quer consolidar agora?"
  - [ ] canvas-webinar.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *canvas-webinar"
    error_message: "Para gerar a copy de replay, preciso do Canvas do Webinário (oferta). Quer preencher agora?"
```

---

## Task Execution — Semi-Automatic (elicit: minimal)

### Step 0: Detectar Rodada Ativa e Carregar Knowledge Base

- Verificar rodada ativa em `docs/webinar/`
- Carregar knowledge base: linhas L985-L1197 (Ampliação)

### Step 1: Carregar Inputs

- Ler `roteiro-completo.md` — extrair:
  - Timeline com timestamps
  - Momentos-chave: cada Secret, revelação principal, abertura da oferta
- Ler `canvas-webinar.md` — extrair:
  - Oferta, ticket, garantia
  - Produto e CTA

### Step 2: Gerar Copy da Página de Replay

Seguir regras específicas da metodologia para página de replay:

**REGRAS OBRIGATÓRIAS:**
1. **Pré-headline de escassez:** "O replay ficará disponível por tempo limitado"
2. **Headline de urgência:** "Assista antes que saia do ar: [headline principal do webinário]"
3. **Timestamps como headlines de venda:** Transformar momentos-chave do roteiro em ganchos
4. **Oferta com delay:** A oferta/botão aparece após X minutos (instrução para configurar)
5. **SEM contador regressivo** (diferente da página de fechamento)

**Gerar seções:**

**A. Header:**
- Pré-headline de escassez
- Headline de urgência
- Subheadline: "Assista a aula completa e descubra [promessa]"

**B. Timestamps como Headlines:**
Extrair 4-6 momentos-chave do roteiro e transformar em ganchos:
- "Aos [MM:SS] — [headline de venda sobre o momento]"
- Ex: "Aos 15:30 — O erro #1 que impede [resultado] (e como evitar)"
- Ex: "Aos 42:00 — A técnica de [Mecanismo Único] explicada passo a passo"
- Ex: "Aos 58:00 — Como ter acesso a tudo isso por um valor surpreendente"

**C. Oferta (aparece com delay):**
- Resumo da oferta (breve)
- CTA principal
- Nota: "Configure para aparecer após [X] minutos" (instrução técnica)

**D. Nota de escassez:**
- "Este replay será removido em [prazo]"
- SEM contador regressivo (regra da metodologia)

### Step 3: Gerar Instruções Técnicas (auto)

- Instrução para configurar delay da oferta no EverWebinar/plataforma
- Instrução sobre quando remover o replay
- Nota sobre rastreamento (quem assistiu, até que minuto)

### Step 4: Compilar e Salvar (elicit: confirmação)

**Elicitation:**
```
Copy da página de replay gerada!

Estrutura:
- Pré-headline de escassez
- Headline de urgência
- [X] timestamps como headlines de venda
- Oferta com delay (aparece após [X] min)
- SEM contador regressivo (conforme metodologia)

Quer revisar os timestamps ou a oferta? (ok para salvar)
```

- Usar template `webinar-copy-replay-tmpl.md`
- Salvar em `docs/webinar/rodada-{N}/conteudo/copy-pagina-replay.md`
- Informar: "Copy de replay pronta! Próximo: `*copy-fechamento` para a página de fechamento."

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] copy-pagina-replay.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Contém pré-headline de escassez
    tipo: post-condition
    blocker: true
  - [ ] Contém timestamps como headlines de venda
    tipo: post-condition
    blocker: true
  - [ ] SEM contador regressivo (regra da metodologia)
    tipo: post-condition
    blocker: true
  - [ ] Oferta configurada com delay
    tipo: post-condition
    blocker: true
```

---

## Handoff

```yaml
next_agent: webinar-creator
next_command: "*copy-fechamento"
condition: "Copy de replay pronta"
alternatives:
  - agent: webinar-operator
    command: "*setup-everwebinar"
    condition: "Todas as copies prontas, ir para setup"
```

---

## Performance

```yaml
duration_expected: 8-15 min
token_usage: ~5,000-10,000 tokens
```
