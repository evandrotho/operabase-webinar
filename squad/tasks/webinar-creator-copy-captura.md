---

## Task Definition

```yaml
task: webinarCreatorCopyCaptura()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "etapa-captacao"
      lines: "L451-L525"
      purpose: "Etapa 1: Captação — 2 formatos de página de captura (simples e completa)"

inputs:
  required:
    - campo: canvas-produto.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-produto.md
      purpose: "Grande Promessa, Mecanismo Único — headline e copy principal"
    - campo: avatar-blueprint.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/avatar-blueprint.md
      purpose: "Desejos, frustrações — bullets e identificação"
  optional:
    - campo: canvas-webinar.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/planejamento/canvas-webinar.md
      purpose: "Tema, título, data, formato — contexto do evento"

output:
  path: docs/webinar/rodada-{N}/conteudo/copy-pagina-captura.md
  template: webinar-copy-captura-tmpl.md
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] canvas-produto.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *canvas-produto"
    error_message: "Para gerar a copy de captura, preciso do Canvas do Produto. Quer preencher agora?"
  - [ ] avatar-blueprint.md exists in docs/webinar/rodada-{N}/planejamento/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-strategist *avatar"
    error_message: "Para gerar a copy de captura, preciso do Avatar Blueprint. Quer preencher agora?"
```

---

## Task Execution — Interactive (elicit: true)

### Step 0: Detectar Rodada Ativa e Carregar Knowledge Base

- Verificar rodada ativa em `docs/webinar/`
- Carregar knowledge base: linhas L451-L525 (Captação)

### Step 1: Carregar Inputs

- Ler `canvas-produto.md` — extrair: Grande Promessa, Mecanismo Único, Proposta de Valor
- Ler `avatar-blueprint.md` — extrair: desejos, frustrações, obstáculos
- Se `canvas-webinar.md` existir, puxar: tema, título, data/hora, formato

### Step 2: Escolher Formato (elicit)

**Elicitation:**
```
A metodologia oferece 2 formatos de página de captura:

**1. Página Simples (Recomendada para webinário gratuito)**
- Headline forte
- 3-5 bullets de benefícios
- Formulário de cadastro (nome, e-mail, WhatsApp)
- CTA claro
- Taxa de conversão esperada: ~40%

**2. Página Completa (Recomendada para ingresso pago)**
- Headline forte
- Subheadline com Mecanismo Único
- Seção "Para quem é" (identificação)
- 5-7 bullets expandidos
- Prova social / credenciais
- FAQ (3-5 perguntas)
- Garantia (se ingresso pago)
- Múltiplos CTAs
- Ideal para eventos com ingresso ou de alto valor

Qual formato? (1 ou 2)
```

### Step 3: Gerar Headline e Subheadline (auto + elicit)

- Gerar headline usando fórmulas da metodologia (ou puxar de `headlines.md` se existir)
- Gerar subheadline com Mecanismo Único

**Elicitation:**
```
Headline gerada: "[headline]"
Subheadline: "[subheadline com mecanismo único]"

Quer manter ou quer que eu gere mais opções? (ok / mais opções)
```

### Step 4: Gerar Bullets de Benefícios (auto)

**Formato Simples — 3-5 bullets:**
- Cada bullet: benefício concreto + resultado
- Formato: "Descubra [o quê] para [resultado]"
- Puxar dos desejos do Avatar Blueprint

**Formato Completo — 5-7 bullets expandidos:**
- Cada bullet: benefício + prova/credibilidade
- Incluir ícones/emojis visuais
- Organizar por impacto (maior benefício primeiro)

### Step 5: Gerar Seções Específicas por Formato

**Se Formato Simples:**
- Gerar formulário de cadastro (campos sugeridos)
- Gerar CTA: "Quero minha vaga!" / "Garantir meu lugar"
- Gerar nota de urgência se aplicável

**Se Formato Completo:**
- Gerar seção "Para quem é" (3-4 perfis usando dados do Avatar)
- Gerar seção "Para quem NÃO é" (2-3 anti-perfis)
- Gerar seção de prova social (template para depoimentos)
- Gerar FAQ (3-5 perguntas frequentes usando objeções do Avatar, campo 7)
- Gerar seção de garantia (se ingresso pago)
- Gerar múltiplos CTAs (header, meio, footer)

### Step 6: Gerar Elementos Complementares (auto)

- **Elemento de escassez:** "Vagas limitadas" / "Inscrições até [data]"
- **Elemento de urgência:** Contador regressivo (instrução para configurar)
- **Congruência criativo-página:** Nota sobre manter mesma linguagem dos anúncios

### Step 7: Compilar e Salvar (elicit: revisão)

**Elicitation:**
```
Copy da página de captura gerada (formato [simples/completo])!

Estrutura:
- Headline: [headline]
- Subheadline: [subheadline]
- Bullets: [X] itens
[- Para quem é: [X] perfis] (se formato completo)
[- FAQ: [X] perguntas] (se formato completo)
- CTA: "[texto do CTA]"

Quer revisar alguma seção antes de salvar? (ok para salvar)
```

- Usar template `webinar-copy-captura-tmpl.md`
- Salvar em `docs/webinar/rodada-{N}/conteudo/copy-pagina-captura.md`
- Informar: "Copy de captura pronta! Próximo: `*copy-replay` ou `*copy-fechamento`."

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] copy-pagina-captura.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Contém headline + bullets + CTA no mínimo
    tipo: post-condition
    blocker: true
  - [ ] Formato escolhido (simples ou completo) claramente indicado
    tipo: post-condition
    blocker: true
```

---

## Handoff

```yaml
next_agent: webinar-creator
next_command: "*copy-replay"
condition: "Copy de captura pronta"
alternatives:
  - agent: webinar-creator
    command: "*copy-fechamento"
    condition: "Usuário prefere gerar fechamento antes"
  - agent: webinar-operator
    command: "*setup-everwebinar"
    condition: "Copy pronta, ir para configuração"
```

---

## Performance

```yaml
duration_expected: 10-20 min
token_usage: ~5,000-15,000 tokens
```
