---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: planejamentoResumo()
responsável: Sage (Strategist)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "canvas-cliente-ideal"
      lines: "L83-L140"
      purpose: "Cross-reference: consolidação dos dados do público"
    - id: "canvas-produto"
      lines: "L141-L199"
      purpose: "Cross-reference: consolidação da proposta de valor"
    - id: "canvas-webinar"
      lines: "L200-L283"
      purpose: "Cross-reference: consolidação da estrutura do webinário"
    - id: "canvas-orcamento"
      lines: "L284-L338"
      purpose: "Cross-reference: consolidação do orçamento"
    - id: "avatar-blueprint"
      lines: "L1722-L1866"
      purpose: "Cross-reference: consolidação do perfil do avatar"

**Entrada:**
- campo: rodada
  tipo: number
  origem: Auto-detect or User Input
  obrigatório: true
  default: 1

**Inputs obrigatórios:**
- campo: canvas-cliente-ideal.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: true

- campo: canvas-produto.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: true

- campo: canvas-webinar.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: true

- campo: avatar-blueprint.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: true

**Inputs opcionais:**
- campo: orcamento-meta.md
  tipo: file
  origem: docs/webinar/rodada-{N}/planejamento/
  obrigatório: false
  purpose: Dados financeiros e métricas do funil

**Saída:**
- campo: resumo_file
  tipo: string
  destino: docs/webinar/rodada-{N}/planejamento/planejamento-resumo.md
  persistido: true
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] canvas-cliente-ideal.md exists
    tipo: pre-condition
    blocker: true
    error_message: "Canvas do Cliente Ideal é necessário. Execute *canvas-cliente"

  - [ ] canvas-produto.md exists
    tipo: pre-condition
    blocker: true
    error_message: "Canvas do Produto é necessário. Execute *canvas-produto"

  - [ ] canvas-webinar.md exists
    tipo: pre-condition
    blocker: true
    error_message: "Canvas do Webinário é necessário. Execute *canvas-webinar"

  - [ ] avatar-blueprint.md exists
    tipo: pre-condition
    blocker: true
    error_message: "Avatar Blueprint é necessário. Execute *avatar"
```

---

# Relatório Consolidado de Planejamento — Task

## Purpose

Gerar um relatório consolidado que une todos os canvases em uma visão estratégica completa. Este documento serve como "briefing executivo" do planejamento e é a referência principal para a fase de construção (roteiro, copy, mensagens).

## SEQUENTIAL Task Execution

### 0. Verificar Pré-requisitos

- Detectar rodada ativa
- Verificar existência de TODOS os 4 canvases obrigatórios + avatar:
  - `canvas-cliente-ideal.md`
  - `canvas-produto.md`
  - `canvas-webinar.md`
  - `avatar-blueprint.md`
- Se algum faltar, listar pendências e redirecionar:
  ```
  Para gerar o resumo consolidado, preciso de todos os canvases preenchidos.

  Status:
  ✅ Canvas do Cliente Ideal
  ✅ Canvas do Produto
  ❌ Canvas do Webinário — Execute *canvas-webinar
  ✅ Avatar Blueprint

  Quer preencher o canvas pendente agora?
  ```
- Opcionalmente carregar `orcamento-meta.md` se existir

### 1. Carregar e Extrair Dados

Para cada canvas, extrair os dados principais:

**Do Canvas do Cliente Ideal:**
- Público-alvo (critérios objetivos)
- Dor principal
- Resultado desejado
- Objeções mapeadas
- Canais de aquisição

**Do Canvas do Produto:**
- Grande Promessa (fórmula completa)
- Mecanismo Único (nome)
- Diferenciais
- Provas
- Proposta de Valor (7 tópicos)

**Do Avatar Blueprint:**
- Top 3 desejos
- Obstáculos (internos e externos)
- Desejos ocultos
- One Big Domino
- Tabela Problema x Solução (contagem de linhas)

**Do Canvas do Webinário:**
- Título do webinário
- Crença-alvo
- Ponte de crenças (quantidade de tópicos)
- Oferta (ticket, garantia)
- Entregáveis no Stack (quantidade e valor total)
- Bônus (quantidade e valor total)
- Objeções/Respostas (quantidade de pares)

**Do Orçamento (se existir):**
- Meta de vendas
- Leads necessários
- Investimento em mídia
- Faturamento projetado
- ROAS
- Margem

### 2. Gerar Relatório Consolidado

- Carregar template: `.aiox-core/development/templates/webinar-planejamento-resumo-tmpl.md`
- Montar as seções do relatório:

**Seção 1: Visão Geral**
- Nome do webinário
- Grande Promessa
- Público-alvo
- Ticket
- Formato e data

**Seção 2: O Avatar**
- Perfil consolidado
- Desejos e dores
- One Big Domino

**Seção 3: A Oferta**
- Mecanismo Único
- Stack Slide completo (entregáveis + valores)
- Bônus
- Garantia
- Dupla Queda de Preço (valor stack → preço oficial → preço promo)

**Seção 4: Estratégia de Crenças**
- Crença-alvo
- Ponte de crenças
- Falsas crenças a serem quebradas

**Seção 5: Objeções e Respostas**
- Tabela consolidada de todas as objeções/respostas

**Seção 6: Métricas e Metas (se orçamento existir)**
- Funil completo com números
- Investimento e retorno esperado

**Seção 7: Checklist de Prontidão**
- [ ] Avatar definido com profundidade
- [ ] Grande Promessa clara e objetiva
- [ ] Mecanismo Único nomeado
- [ ] Crença-alvo articulada
- [ ] Oferta completa com Stack
- [ ] Objeções mapeadas e respondidas
- [ ] Metas financeiras calculadas (se aplicável)

**Seção 8: Próximos Passos**
- Recomendações para a fase de construção
- Quais artefatos o @webinar-creator vai gerar
- Sugestão de começar por *abertura ou *roteiro

### 3. Salvar Relatório

- Salvar em: `docs/webinar/rodada-{N}/planejamento/planejamento-resumo.md`

### 4. Apresentar ao Usuário

```
Relatório Consolidado de Planejamento salvo em:
docs/webinar/rodada-{N}/planejamento/planejamento-resumo.md

O planejamento está COMPLETO! Aqui está um resumo:

WEBINÁRIO: {título}
PÚBLICO: {público}
PROMESSA: {grande_promessa}
MECANISMO: {mecanismo_unico}
TICKET: R${ticket}
{Se orçamento: "META: {meta} vendas | ROAS: {roas}x | MARGEM: R${margem}"}

PRONTIDÃO: {X}/7 itens completos

Próximo passo:
→ Ativar @webinar-creator para iniciar a construção do roteiro e conteúdo
→ Comando sugerido: *abertura (para começar pela abertura do webinário)
→ Ou: *roteiro (para gerar o roteiro completo de uma vez)
```

---

## Error Handling

1. **Error:** One or more required canvases missing
   - **Resolution:** List missing canvases with commands to fill them
   - **Recovery:** Wait for user to fill missing canvases

2. **Error:** Canvas data is inconsistent (ex: ticket no orçamento difere do canvas-webinar)
   - **Resolution:** Highlight inconsistency, ask which value is correct
   - **Recovery:** Use corrected value in resumo

---

## Handoff

```yaml
next_agent: "@webinar-creator"
next_command: "*abertura"
condition: Planejamento consolidado completo
alternatives:
  - agent: "@webinar-creator"
    command: "*roteiro"
    condition: "Quer gerar roteiro completo de uma vez"
  - agent: "@webinar"
    command: "*status"
    condition: "Quer ver progresso geral antes de avançar"
```

---

## Metadata

```yaml
version: 1.0.0
squad: webinar
agent: webinar-strategist
command: "*resumo"
prd_reference: "PRD v2.1, Seção 3.2 — Relatório Consolidado de Planejamento"
methodology_reference: "Cross-reference de todas as seções de planejamento"
tags:
  - webinar
  - planning
  - summary
  - consolidation
updated_at: 2026-03-05
```
