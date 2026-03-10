---

## Task Definition

```yaml
task: webinarCreatorCopyFechamento()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "etapa-fechamento"
      lines: "L1198-L1463"
      purpose: "Etapa 6: Fechamento do Carrinho — página com deadline, contador, depoimentos"

inputs:
  required:
    - campo: canvas-webinar.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-webinar.md
      purpose: "Blocos 12-15: Oferta, entregáveis, bônus, garantia, objeções — conteúdo completo da oferta"
    - campo: canvas-produto.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-produto.md
      purpose: "Grande Promessa, Mecanismo Único — headline e posicionamento"

output:
  path: docs/webinar/rodada-{N}/conteudo/copy-pagina-fechamento.md
  template: webinar-copy-fechamento-tmpl.md
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] canvas-webinar.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *canvas-webinar"
    error_message: "Para gerar a copy de fechamento, preciso do Canvas do Webinário (oferta completa). Quer preencher agora?"
  - [ ] canvas-produto.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *canvas-produto"
    error_message: "Para gerar a copy de fechamento, preciso do Canvas do Produto. Quer preencher agora?"
```

---

## Task Execution — Semi-Automatic (elicit: minimal)

### Step 0: Detectar Rodada Ativa e Carregar Knowledge Base

- Verificar rodada ativa em `docs/webinar/`
- Carregar knowledge base: linhas L1198-L1463 (Fechamento)

### Step 1: Carregar Inputs

- Ler `canvas-webinar.md` — extrair blocos 12-15:
  - Oferta: ticket, condições, garantia
  - Entregáveis: nome + valor
  - Bônus: nome + valor
  - Objeções: pares objeção/resposta
- Ler `canvas-produto.md` — extrair: Grande Promessa, Mecanismo Único

### Step 2: Gerar Copy da Página de Fechamento

Seguir regras específicas da metodologia para página de fechamento:

**REGRAS OBRIGATÓRIAS:**
1. **Deadline explícito:** Data/hora exata do fechamento visível
2. **Headline de oferta:** Foco na oferta, não no conteúdo
3. **COM contador regressivo:** Diferente da página de replay
4. **Seção de depoimentos:** Espaço para provas sociais
5. **Tudo carrega imediato:** Sem delay de oferta (diferente do replay)

**Gerar seções:**

**A. Header com Contador:**
- Headline de oferta: "[Produto]: [Promessa] por [Preço Promocional]"
- Subheadline: "Oferta especial válida até [data/hora]"
- Contador regressivo: [INSTRUÇÃO: Configurar contador até data/hora de fechamento]

**B. Resumo da Oferta:**
- O que está incluído (Stack resumido):
  - Módulo 1: [Nome] — Valor: R$ [valor]
  - Módulo 2: [Nome] — Valor: R$ [valor]
  - ...
  - Bônus 1: [Nome] — Valor: R$ [valor]
  - Bônus 2: [Nome] — Valor: R$ [valor]
  - **Total do Stack: R$ [soma]**
  - ~~De R$ [soma]~~
  - **Hoje: R$ [preço promocional]**
- Condições de pagamento (se aplicável)

**C. CTA Principal:**
- Botão grande e claro
- Texto: "Quero começar agora!" / "Garantir minha vaga"
- Nota de segurança: "Pagamento seguro. Seus dados estão protegidos."

**D. Seção de Garantia:**
- Texto de garantia do Canvas do Webinário
- Formato visual: badge/selo de garantia
- Exemplo: "Garantia incondicional de [X] dias. Se não gostar, devolvemos 100%."

**E. Seção de Depoimentos:**
- Template para 3-6 depoimentos:
  - "[Nome] — [Cidade/Profissão]"
  - "[Depoimento ou resultado]"
  - Nota: "Substitua pelos depoimentos reais dos seus clientes"

**F. FAQ (Objeções Respondidas):**
- Transformar objeções do Canvas do Webinário (bloco 15) em FAQ
- Formato: Pergunta → Resposta
- 5-8 perguntas frequentes

**G. CTA Final + Urgência:**
- Repetição do CTA
- Reforço de escassez: "Essa oferta expira em [contador]"
- Custo de não agir: "Quanto vai custar continuar [problema] por mais [tempo]?"

### Step 3: Gerar Instruções Técnicas (auto)

- Configurar contador regressivo (ferramenta sugerida)
- Configurar redirecionamento após deadline (página de "oferta encerrada")
- Pixel events: Purchase, InitiateCheckout

### Step 4: Compilar e Salvar (elicit: confirmação)

**Elicitation:**
```
Copy da página de fechamento gerada!

Estrutura:
- Header COM contador regressivo
- Stack completo: [X] módulos + [X] bônus = R$ [soma]
- Preço: De R$ [soma] por R$ [preço]
- Garantia: [X] dias
- FAQ: [X] perguntas (baseadas nas objeções)
- Depoimentos: [X] templates
- CTAs: [X] pontos de conversão

Diferenças vs. página de replay:
- COM contador (replay não tem)
- Oferta visível imediato (replay tem delay)
- FAQ presente (replay não tem)

Quer revisar alguma seção? (ok para salvar)
```

- Usar template `webinar-copy-fechamento-tmpl.md`
- Salvar em `docs/webinar/rodada-{N}/conteudo/copy-pagina-fechamento.md`
- Informar: "Copy de fechamento pronta! Todos os artefatos de conteúdo estão completos. Handoff para @webinar-operator quando quiser."

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] copy-pagina-fechamento.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Contém deadline explícito
    tipo: post-condition
    blocker: true
  - [ ] COM contador regressivo (instrução)
    tipo: post-condition
    blocker: true
  - [ ] Contém Stack + Dupla Queda de Preço
    tipo: post-condition
    blocker: true
  - [ ] Contém seção de depoimentos (template)
    tipo: post-condition
    blocker: true
  - [ ] Contém FAQ baseado em objeções
    tipo: post-condition
    blocker: true
```

---

## Handoff

```yaml
next_agent: webinar-operator
next_command: "*setup-everwebinar"
condition: "Todas as copies prontas — ir para execução"
alternatives:
  - agent: webinar-creator
    command: "*status"
    condition: "Verificar progresso geral antes do handoff"
  - agent: webinar
    command: "*status"
    condition: "Ver visão geral do projeto"
```

---

## Performance

```yaml
duration_expected: 10-18 min
token_usage: ~8,000-15,000 tokens
```
