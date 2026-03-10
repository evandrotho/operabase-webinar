---
tools: []
checklists: []
execution_mode: interactive
---

# webinar-operator-checklist

Checklist completo pre-lancamento com verificacao ponto a ponto.

## Purpose

Gerar e conduzir uma verificacao completa de tudo que precisa estar pronto antes do lancamento do webinario. Cruza informacoes de todos os artefatos gerados nas fases anteriores (planejamento, conteudo, execucao) e valida cada ponto critico. O checklist e interativo: o agente pergunta ao usuario item por item e marca como verificado ou pendente.

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "funil-visao-geral"
      lines: "L409-L421"
      purpose: "Visao geral do funil para validar cobertura completa"
    - id: "mapa-ferramentas"
      lines: "L1652-L1671"
      purpose: "Mapa consolidado de ferramentas -- checklist de configuracao"
    - id: "stack-tecnica"
      lines: "L3736-L3758"
      purpose: "Stack tecnica completa para verificar se tudo esta conectado"
    - id: "segmentacao-tags"
      lines: "L3759-L3829"
      purpose: "Segmentacao e tags -- verificar se automacoes estao prontas"
    - id: "estrategias-operacionais"
      lines: "L3992-L4077"
      purpose: "Estrategias operacionais adicionais -- detalhes finais"
```

## Prerequisites

```yaml
prerequisites:
  required: []  # O checklist e o ponto de verificacao final -- valida a existencia de tudo
  optional:
    - artifact: "docs/webinar/rodada-{N}/planejamento/"
      description: "Todos os artefatos de planejamento"
    - artifact: "docs/webinar/rodada-{N}/conteudo/"
      description: "Todos os artefatos de conteudo"
    - artifact: "docs/webinar/rodada-{N}/execucao/"
      description: "Todos os artefatos de execucao"
```

## Task Definition

```yaml
task: checklistLancamento()
responsavel: Atlas (Executor)
responsavel_type: Agente
elicit: true

Entrada:
- campo: rodada_path
  tipo: string
  origem: "docs/webinar/rodada-{N}/"
  obrigatorio: true
  validacao: Diretorio deve existir

Saida:
- campo: checklist_lancamento
  tipo: file
  destino: "docs/webinar/rodada-{N}/execucao/checklist-lancamento.md"
  persistido: true
  template: webinar-checklist-lancamento-tmpl.md
```

## SEQUENTIAL Task Execution

### 0. Inventariar Artefatos Existentes

- Listar todos os arquivos em `docs/webinar/rodada-{N}/`
- Categorizar por fase: planejamento, conteudo, execucao
- Carregar knowledge base: L409-L421, L1652-L1671, L3736-L3758, L3759-L3829, L3992-L4077

### 1. Verificar Artefatos de Planejamento

**ELICIT (item por item):**

Para cada artefato abaixo, verificar se existe e perguntar ao usuario:

- [ ] **Canvas do Cliente Ideal** (`canvas-cliente-ideal.md`)
  - Existe? Se sim: "O Canvas do Cliente Ideal esta preenchido?"
  - Se nao: "ALERTA: Canvas do Cliente Ideal nao encontrado. Isso pode impactar a segmentacao dos anuncios."

- [ ] **Canvas do Produto** (`canvas-produto.md`)
  - Existe? Se sim: "A Grande Promessa, Mecanismo Unico e Proposta de Valor estao definidos?"
  - Se nao: "ALERTA: Canvas do Produto nao encontrado. Essencial para o roteiro."

- [ ] **Canvas do Webinario** (`canvas-webinar.md`)
  - Existe? Se sim: "Todos os 15 blocos estao preenchidos?"

- [ ] **Avatar Blueprint** (`avatar-blueprint.md`)
  - Existe? Se sim: "7 perguntas respondidas + Tabela P x S completa?"

- [ ] **Orcamento e Meta** (`orcamento-meta.md`)
  - Existe? Se sim: "As 12 premissas estao preenchidas com valores atualizados?"
  - Nota: Opcional mas fortemente recomendado.

### 2. Verificar Artefatos de Conteudo

- [ ] **Roteiro - Abertura** (`roteiro-abertura.md`)
  - "Os 7 blocos da abertura estao completos?"

- [ ] **Roteiro - Empatia** (`roteiro-empatia.md`)
  - "O modelo de historia (Avatar Transformado ou Socorrista) foi escolhido e escrito?"

- [ ] **Roteiro - Conteudo** (`roteiro-conteudo.md`)
  - "Os 3 Secrets (Vehicle, Internal, External) estao com False Beliefs definidas?"

- [ ] **Roteiro - Pitch** (`roteiro-pitch.md`)
  - "As 15 etapas do pitch estao completas? Stack Slide montado?"

- [ ] **Roteiro Completo** (`roteiro-completo.md`)
  - "O roteiro consolidado esta pronto com timeline de 60-90 minutos?"

- [ ] **Mensagens WhatsApp** (`mensagens-whatsapp.md`)
  - "41+ mensagens geradas e personalizadas com dados da campanha?"

- [ ] **Copy Pagina de Captura** (`copy-pagina-captura.md`)
  - "Copy pronta para montar a pagina?"

- [ ] **Copy Pagina de Replay** (`copy-pagina-replay.md`)
  - "Copy pronta? Sem contador regressivo, com timestamps?"

- [ ] **Copy Pagina de Fechamento** (`copy-pagina-fechamento.md`)
  - "Copy pronta? Com contador regressivo e deadline explicito?"

### 3. Verificar Configuracao de Ferramentas

- [ ] **EverWebinar** (`guia-everwebinar.md`)
  - "Video carregado e testado?"
  - "Agendamento configurado (diario/semanal/JIT)?"
  - "Chat simulado com mensagens programadas?"
  - "Eventos na timeline sincronizados com roteiro?"
  - "Replay configurado?"
  - "Pagina de registro conectada?"

- [ ] **SendFlow** (`guia-sendflow.md`)
  - "Grupos criados (Fase Pre, Fase Pos, Fase Conteudo)?"
  - "Mensagens carregadas e agendadas?"
  - "Triggers configurados (entrada, tempo, evento, webhook)?"
  - "Deep links com Pixel funcionando?"
  - "Teste de envio realizado?"

- [ ] **Pagamento** (`guia-pagamento.md`)
  - "Produto cadastrado na plataforma?"
  - "Checkout funcionando?"
  - "Webhooks configurados e testados?"
  - "Order bump/upsell/downsell ativos (se aplicavel)?"
  - "Teste de compra realizado em sandbox?"

- [ ] **Facebook Pixel** (`guia-pixel.md`)
  - "Pixel instalado em todas as paginas?"
  - "Eventos disparando corretamente (verificado com Pixel Helper)?"
  - "Deep links com UTMs configurados?"
  - "Audiencias criadas?"

### 4. Verificar Timeline e Funil

- [ ] **Timeline** (`timeline-campanha.md`)
  - "Cronograma com datas reais definido?"
  - "Mensagens distribuidas nos dias corretos?"
  - "Marcos e checkpoints definidos?"

- [ ] **Funil** (`funil-7-etapas.md`)
  - "Todas as 7 etapas com ferramentas atribuidas?"
  - "Gatilhos de transicao entre etapas definidos?"

### 5. Verificacoes Criticas Pre-Lancamento

- [ ] **Teste end-to-end do funil:**
  - "Voce fez o percurso completo como se fosse um lead? (clicar no anuncio -> pagina de captura -> registrar -> receber mensagem de boas-vindas -> assistir webinario -> receber link de checkout -> simular compra)"

- [ ] **Links funcionando:**
  - "Todos os links testados? (captura, webinario, replay, checkout, fechamento)"

- [ ] **Mensagens sem erro:**
  - "Variaveis dinamicas substituidas? ({{nome_expert}}, {{data_webinario}}, {{link}}, etc.)"

- [ ] **Backup e contingencia:**
  - "O que acontece se o video parar? (plano B)"
  - "O que acontece se o checkout cair? (link alternativo)"
  - "Quem monitora durante o webinario?"

### 6. Compilar Checklist e Calcular Score

- Contar itens verificados vs. total
- Classificar:
  - **PRONTO PARA LANCAR** (>= 90% verificado, zero criticos pendentes)
  - **QUASE PRONTO** (75-89%, apenas nao-criticos pendentes)
  - **PRECISA DE ATENCAO** (60-74%, itens criticos pendentes)
  - **NAO PRONTO** (< 60%, muitos itens criticos pendentes)
- Listar itens pendentes priorizados por criticidade

### 7. Salvar Checklist

- Usar template `webinar-checklist-lancamento-tmpl.md`
- Preencher com todos os itens, status e score
- Salvar em `docs/webinar/rodada-{N}/execucao/checklist-lancamento.md`

### 8. Orientar Proximos Passos

Baseado no resultado:
- **PRONTO:** "Parabens! Tudo verificado. Quando lancar e a campanha estiver rodando, ative o @webinar-analyst com *kpis para acompanhar resultados."
- **QUASE PRONTO:** "Faltam [X] itens nao-criticos. Veja a lista e resolva. Depois rode `*checklist` novamente."
- **PRECISA DE ATENCAO:** "Faltam [X] itens criticos. Resolva antes de lancar: [lista]."
- **NAO PRONTO:** "Ainda ha muito a preparar. Veja os itens pendentes e use os comandos indicados para resolver cada um."

## Output

```yaml
output:
  path: "docs/webinar/rodada-{N}/execucao/checklist-lancamento.md"
  template: webinar-checklist-lancamento-tmpl.md
  format: markdown
  sections:
    - Score Geral
    - Planejamento (itens + status)
    - Conteudo (itens + status)
    - Ferramentas (itens + status)
    - Timeline e Funil (itens + status)
    - Verificacoes Criticas (itens + status)
    - Itens Pendentes Priorizados
    - Veredicto Final
```

## Error Handling

**Strategy:** guide-and-retry

**Common Errors:**

1. **Error:** Diretorio da rodada nao existe
   - **Resolution:** Orientar sobre como iniciar o projeto com @webinar e *planejar
2. **Error:** Poucos artefatos encontrados
   - **Resolution:** Orientar sobre a sequencia correta: Planejar -> Construir -> Executar

## Handoff

```yaml
next_agent: "@webinar-analyst"
next_command: "*kpis"
condition: "Checklist PRONTO, campanha lancada e executada com dados reais"
alternatives:
  - agent: "@webinar"
    command: "*status"
    condition: "Retornar ao orquestrador para visao geral"
```
