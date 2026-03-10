---
tools: []
checklists: []
execution_mode: interactive
---

# webinar-operator-funil

Visualizar o funil de 7 etapas do webinario com status e proximas acoes.

## Purpose

Apresentar ao usuario uma visao clara e visual do funil completo de 7 etapas da campanha de webinario, baseado na metodologia fusionada. Para cada etapa: descricao, pilar da Espiral de Vendas, gatilho de transicao, ferramentas envolvidas, metricas-chave e status atual (pronto/pendente). Tambem diferencia entre Estrutura Basica (validacao) e Estrutura Escalada (escala).

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "funil-visao-geral"
      lines: "L409-L421"
      purpose: "Visao geral do funil de 7 etapas"
    - id: "estrutura-basica-escalada"
      lines: "L422-L434"
      purpose: "Estrutura Basica (validacao) vs Escalada (escala) -- quando usar cada uma"
    - id: "etapa-1-captacao"
      lines: "L451-L525"
      purpose: "Etapa 1: Captacao"
    - id: "etapa-2-nutricao"
      lines: "L526-L685"
      purpose: "Etapa 2: Nutricao"
    - id: "etapa-3-antecipacao"
      lines: "L686-L890"
      purpose: "Etapa 3: Antecipacao"
    - id: "etapa-4-abertura"
      lines: "L891-L984"
      purpose: "Etapa 4: Abertura do Carrinho"
    - id: "etapa-5-ampliacao"
      lines: "L985-L1197"
      purpose: "Etapa 5: Ampliacao do Impacto"
    - id: "etapa-6-fechamento"
      lines: "L1198-L1463"
      purpose: "Etapa 6: Fechamento do Carrinho"
    - id: "etapa-7-impulsionamento"
      lines: "L1464-L1651"
      purpose: "Etapa 7: Impulsionamento do Lucro"
    - id: "metricas-kpis"
      lines: "L1672-L1715"
      purpose: "Metricas e KPIs consolidados por etapa"
    - id: "espiral-vendas"
      lines: "L22-L80"
      purpose: "Espiral de Vendas: 5 pilares e sequencia"
```

## Prerequisites

```yaml
prerequisites:
  required: []  # Instrucional, baseado na metodologia
  optional:
    - artifact: "docs/webinar/rodada-{N}/execucao/timeline-campanha.md"
      description: "Timeline da campanha (para mostrar status de cada etapa)"
      enriches: "Status atual de cada etapa baseado no cronograma"
```

## Task Definition

```yaml
task: funilVisualizacao()
responsavel: Atlas (Executor)
responsavel_type: Agente
elicit: true

Entrada:
- campo: timeline_campanha
  tipo: file
  origem: "docs/webinar/rodada-{N}/execucao/timeline-campanha.md"
  obrigatorio: false

Saida:
- campo: funil_7_etapas
  tipo: file
  destino: "docs/webinar/rodada-{N}/execucao/funil-7-etapas.md"
  persistido: true
  template: webinar-funil-7-etapas-tmpl.md
```

## SEQUENTIAL Task Execution

### 0. Carregar Knowledge Base e Contexto

- Carregar secoes da knowledge base: L409-L434, L451-L1715, L22-L80
- Se `timeline-campanha.md` existir, ler para determinar status de cada etapa
- Verificar quais artefatos ja existem em `docs/webinar/rodada-{N}/`

### 1. Elicitar Modo do Funil

**ELICIT:**

1. "Voce quer visualizar o funil em qual modo?
   1. **Estrutura Basica** -- para validacao do webinario (primeira rodada, testar a oferta)
   2. **Estrutura Escalada** -- para escala (ja validou, quer aumentar volume)
   3. **Ambos** -- ver a comparacao lado a lado"

### 2. Gerar Visao Geral do Funil

Baseado na knowledge base, gerar diagrama ASCII e descricao de cada etapa:

```
[1. CAPTACAO] --> [2. NUTRICAO] --> [3. ANTECIPACAO] --> [4. ABERTURA]
                                                            |
[7. IMPULSO] <-- [6. FECHAMENTO] <-- [5. AMPLIACAO] <------+
```

### 3. Detalhar Cada Etapa

Para cada uma das 7 etapas, gerar bloco com:

**Etapa 1: Captacao**
- Pilar: Atracao
- Objetivo: Gerar leads qualificados para a meta
- Ferramentas: Facebook Ads, Instagram, pagina de captura
- Metricas: CPL, taxa de conversao da pagina, volume de leads
- Gatilho de transicao: Leads suficientes para meta OU data de inicio da nutricao
- Artefatos necessarios: copy-pagina-captura.md, guia-pixel.md
- Status: [Pronto/Pendente/Em Andamento] (baseado em artefatos existentes)

**Etapa 2: Nutricao**
- Pilar: Engajamento
- Objetivo: Aquecer leads com conteudo relevante
- Ferramentas: SendFlow (WhatsApp), email
- Metricas: taxa de abertura, taxa de resposta, engajamento
- Gatilho de transicao: Data do webinario se aproximando (D-1)
- Artefatos: mensagens-whatsapp.md (5 msgs nutricao), guia-sendflow.md
- Status: [Pronto/Pendente/Em Andamento]

**Etapa 3: Antecipacao**
- Pilar: Compromisso
- Objetivo: Maximizar comparecimento no webinario
- Ferramentas: SendFlow (WhatsApp), email, SMS
- Metricas: taxa de comparecimento (benchmark: 25%)
- Gatilho de transicao: D-0, hora do webinario
- Artefatos: mensagens-whatsapp.md (9 msgs antecipacao)
- Status: [Pronto/Pendente/Em Andamento]

**Etapa 4: Abertura do Carrinho**
- Pilar: Persuasao
- Objetivo: Converter presentes em compradores (Pico 1 de vendas)
- Ferramentas: EverWebinar, checkout
- Metricas: taxa de conversao, vendas na abertura
- Gatilho de transicao: Webinario realizado
- Artefatos: roteiro-completo.md, guia-everwebinar.md, guia-pagamento.md
- Status: [Pronto/Pendente/Em Andamento]

**Etapa 5: Ampliacao do Impacto**
- Pilar: Urgencia
- Objetivo: Recuperar quem nao compareceu ou nao comprou
- Ferramentas: pagina de replay, SendFlow, email, retargeting
- Metricas: taxa de replay, conversao do replay
- Gatilho de transicao: Replay disponibilizado
- Artefatos: copy-pagina-replay.md, mensagens-whatsapp.md (7 msgs ampliacao)
- Status: [Pronto/Pendente/Em Andamento]

**Etapa 6: Fechamento do Carrinho**
- Pilar: Escassez
- Objetivo: Converter indecisos com urgencia maxima (Pico 2 de vendas)
- Ferramentas: pagina de fechamento, SendFlow, email, countdown
- Metricas: vendas no fechamento, taxa de escassez
- Gatilho de transicao: Deadline definido atingido
- Artefatos: copy-pagina-fechamento.md, mensagens-whatsapp.md (11 msgs fechamento)
- Status: [Pronto/Pendente/Em Andamento]

**Etapa 7: Impulsionamento do Lucro**
- Pilar: Atracao (novo ciclo) + Persuasao
- Objetivo: Maximizar receita pos-fechamento
- Ferramentas: SendFlow (downsell), checkout
- Metricas: taxa de downsell, receita adicional, LTV
- Gatilho de transicao: Pos-fechamento
- Artefatos: mensagens-whatsapp.md (8 msgs downsell)
- Status: [Pronto/Pendente/Em Andamento]

### 4. Gerar Comparacao Basica vs. Escalada (se solicitado)

| Aspecto | Estrutura Basica | Estrutura Escalada |
|---------|------------------|--------------------|
| Objetivo | Validar oferta | Escalar volume |
| Investimento | Baixo | Alto |
| Captacao | Organico + ads baixo | Ads agressivo |
| Automacao | Basica (SendFlow) | Completa (webhooks, tags, automacoes) |
| Replay | Simples | Com segmentacao e retargeting |
| Downsell | Opcional | Obrigatorio |
| Metricas | Basicas (CPL, conversao) | Avancadas (ROAS, LTV, CAC) |

### 5. Compilar e Salvar Funil

- Usar template `webinar-funil-7-etapas-tmpl.md`
- Preencher com todas as etapas detalhadas
- Incluir diagrama visual (ASCII)
- Incluir status de cada etapa
- Salvar em `docs/webinar/rodada-{N}/execucao/funil-7-etapas.md`

### 6. Sugerir Proximo Passo

- Se alguma etapa pendente: "A etapa [X] esta pendente. Para resolve-la, use [comando]."
- Se tudo pronto: "Proximo passo: `*checklist` para verificacao final pre-lancamento"

## Output

```yaml
output:
  path: "docs/webinar/rodada-{N}/execucao/funil-7-etapas.md"
  template: webinar-funil-7-etapas-tmpl.md
  format: markdown
  sections:
    - Diagrama Visual do Funil
    - Detalhamento por Etapa (7 blocos)
    - Metricas e Benchmarks por Etapa
    - Comparacao Basica vs. Escalada (se solicitado)
    - Status Geral e Proximos Passos
```

## Error Handling

**Strategy:** guide-and-retry

**Common Errors:**

1. **Error:** Nenhum artefato encontrado
   - **Resolution:** Orientar usuario a iniciar do planejamento (@webinar-strategist) ou construcao (@webinar-creator)

## Handoff

```yaml
next_agent: "@webinar-operator"
next_command: "*checklist"
condition: "Funil visualizado, checklist pendente"
alternatives:
  - agent: "@webinar-analyst"
    command: "*kpis"
    condition: "Campanha ja executada, hora de analisar"
```
