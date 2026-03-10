# Webinário — Product Requirements Document (PRD)

> **Projeto:** Webinário — Squad de Agentes IA para Webinários
> **Autor:** @pm (Morgan)
> **Fonte:** `docs/METHODOLOGY-ANALYSIS.md` (4077 linhas — Análise fusionada Taioba + Brunson)
> **Data:** 2026-03-05
> **Versão:** 2.1

---

## 1. Visão e Contexto

### 1.1 O que é

Um **squad de agentes IA especializados** que guiam qualquer pessoa (não-técnica) pelo processo completo de planejar, construir, executar e analisar webinários de vendas, utilizando a metodologia fusionada "Webinário Infalível" (Taioba) + "Perfect Webinar" (Brunson).

### 1.2 O que NÃO é

- **NÃO é** uma plataforma web, SaaS ou aplicativo
- **NÃO é** um sistema com banco de dados, login ou dashboard
- **NÃO** substitui ferramentas existentes (EverWebinar, SendFlow, etc.)

### 1.3 O que os agentes fazem

| Verbo | Descrição |
|-------|-----------|
| **Guiam** | Conduzem o usuário passo-a-passo pela metodologia via conversa |
| **Geram** | Produzem artefatos prontos: canvases, roteiros, copy, mensagens, checklists |
| **Orientam** | Ensinam a configurar ferramentas existentes (EverWebinar, SendFlow, etc.) |
| **Analisam** | Revisam resultados pós-webinário e sugerem otimizações |

### 1.4 Goals

1. Entregar um squad de agentes IA que cubra o ciclo completo: **Planejar → Construir → Executar → Analisar**
2. Cada agente opera como um especialista que conversa, faz perguntas e gera documentos prontos para uso
3. Os artefatos são documentos markdown salvos em `docs/webinar/` — legíveis, printáveis, compartilháveis
4. Ser **agnóstico de nicho** — funcionar para qualquer produto/serviço com ticket acima de R$200
5. O fluxo deve ser intuitivo para pessoa não-técnica, sem jargão de programação

### 1.5 Background

O mercado digital brasileiro depende de lançamentos complexos para vender infoprodutos e serviços de alto ticket. Webinários oferecem uma alternativa com complexidade média e poder de venda alto para público frio (ticket R$200-R$40.000), mas a maioria dos profissionais não sabe estruturá-los.

A análise metodológica do @analyst consolidou o curso "Webinário Infalível" de Jonathan Taioba com o "Perfect Webinar" de Russell Brunson, criando um framework fusionado de 4077 linhas que mapeia: Espiral de Vendas, 4 Canvases, benchmarks/KPIs, funil de 7 etapas com 50+ templates de mensagens, estrutura Black Box (Avatar → Abertura → Empatia → Conteúdo → Pitch), stack técnica e estratégias avançadas.

Este PRD transforma essa metodologia em especificações de agentes IA executáveis.

### 1.6 Change Log

| Data | Versão | Descrição |
|------|--------|-----------|
| 2026-03-05 | 1.0 | PRD inicial — plataforma web (DESCARTADO) |
| 2026-03-05 | 2.0 | PRD reescrito — squad de agentes IA |
| 2026-03-05 | 2.1 | Revisão @architect: pré-requisitos por comando, estrutura multi-rodada, cross-refs, METHODOLOGY-INDEX |

---

## 2. Arquitetura do Squad

### 2.1 Visão Geral

O squad "Webinário" é composto por **5 agentes especializados** que cobrem as 4 fases do ciclo:

| # | Agente | Persona | Fase | O que faz |
|---|--------|---------|------|-----------|
| 1 | `@webinar` | **Maestro** | Todas | Orquestrador — ponto de entrada, routing, progresso geral |
| 2 | `@webinar-strategist` | **Sage** | Planejar | Canvases, avatar, orçamento, estratégia de campanha |
| 3 | `@webinar-creator` | **Spark** | Construir | Roteiro do webinário, copy, mensagens WhatsApp, conteúdo de páginas |
| 4 | `@webinar-operator` | **Atlas** | Executar | Guias de configuração de ferramentas, funil, timeline, lançamento |
| 5 | `@webinar-analyst` | **Lens** | Analisar | KPIs, diagnóstico de funil, otimização, próxima rodada |

### 2.2 Jornada do Usuário

```
Usuário chega → @webinar (avalia situação, orienta fase)
  │
  ├─ PLANEJAR → @webinar-strategist
  │    Preenche canvases → define avatar → calcula metas
  │    Artefatos: 6 documentos de planejamento
  │
  ├─ CONSTRUIR → @webinar-creator
  │    Monta roteiro → gera copy → cria mensagens
  │    Artefatos: roteiro completo + 41 mensagens + copy de 3 páginas
  │
  ├─ EXECUTAR → @webinar-operator
  │    Configura ferramentas → monta timeline → checa tudo
  │    Artefatos: guias passo-a-passo + cronograma + checklist
  │
  ├─ ANALISAR → @webinar-analyst
  │    Coleta métricas → diagnostica → planeja próxima rodada
  │    Artefatos: relatório + diagnóstico + plano de melhoria
  │
  ├─ @webinar (próximo ciclo ou empilhamento)
  │
  └─ NOVO CICLO → @webinar-strategist (atualizar canvases se necessário)
```

> **Loop de retorno:** Quando @webinar-analyst gera o `plano-proxima-rodada.md`, este inclui seção "Canvases a revisar" indicando quais artefatos de planejamento devem ser atualizados pelo @webinar-strategist antes da próxima rodada (ex: premissas de orçamento, oferta, avatar refinado com dados reais).

### 2.3 Pré-requisitos entre Fases

| Para iniciar... | Precisa de... |
|-----------------|---------------|
| **Construir** | Canvases de planejamento preenchidos: Cliente Ideal + Produto + Avatar Blueprint + **Canvas Webinário** |
| **Executar** | Roteiro completo + mensagens geradas + orcamento-meta.md (opcional, enriquece timeline) |
| **Analisar** | Campanha executada com dados reais + orcamento-meta.md (para orçado vs. realizado) |

> **Nota:** Pré-requisitos granulares por comando estão detalhados na Seção 5.2.

---

## 3. Especificação dos Agentes

### 3.1 @webinar (Maestro) — Orquestrador

**Papel:** Ponto de entrada do squad. Entende onde o usuário está no processo e direciona para o especialista correto.

**O que faz:**
- Avalia o estágio do projeto (novo? planejamento pronto? pós-webinário?)
- Mostra progresso geral (quais artefatos já foram gerados)
- Explica o processo completo em linguagem simples
- Roteia para o agente certo baseado na necessidade
- Mantém contexto entre sessões via `docs/webinar/progress.md`

**Comandos:**
- `*status` — Mostra progresso do projeto (artefatos gerados/pendentes por fase)
- `*planejar` — Inicia/continua fase de planejamento (→ @webinar-strategist)
- `*construir` — Inicia/continua fase de construção (→ @webinar-creator)
- `*executar` — Inicia/continua fase de execução (→ @webinar-operator)
- `*analisar` — Inicia/continua fase de análise (→ @webinar-analyst)
- `*guia` — Explica todo o processo do webinário em linguagem simples
- `*help` — Mostra comandos disponíveis

**Artefato gerado:**
- `docs/webinar/progress.md` — Status geral do projeto

---

### 3.2 @webinar-strategist (Sage) — Planejamento

**Papel:** Guia o usuário pela fase de planejamento estratégico. Faz perguntas, preenche canvases e calcula metas.

**O que faz:**
- Conduz preenchimento dos 4 Canvases + Avatar Blueprint via conversa interativa
- Faz as perguntas certas, uma por vez, explicando o porquê de cada uma
- Calcula métricas do funil automaticamente (leads necessários, investimento, ROAS)
- Sugere benchmarks da metodologia e explica cada métrica em linguagem simples
- Puxa dados de canvases anteriores para contexto (cross-reference)
- Gera cada canvas como documento markdown formatado

**Comandos:**
- `*canvas-cliente` — Canvas do Cliente Ideal (9 perguntas — Seção 2, Canvas 1)
- `*canvas-produto` — Canvas do Produto (7 blocos — Seção 2, Canvas 2)
- `*canvas-webinar` — Canvas do Webinário Infalível (15 blocos — Seção 2, Canvas 3)
- `*avatar` — Avatar Blueprint (7 perguntas + tabela Problema x Solução — Seção 5.1.1)
- `*orcamento` — Planilha de Orçamento e Meta (12 premissas — Seção 2, Canvas 4)
- `*resumo` — Gera relatório consolidado de planejamento
- `*status` — Progresso dos canvases
- `*help` — Comandos disponíveis

**Artefatos gerados:**

| Artefato | Conteúdo | Referência Metodológica |
|----------|----------|------------------------|
| `canvas-cliente-ideal.md` | 9 perguntas respondidas + validação critérios objetivos/subjetivos + múltiplos perfis | Seção 2, Canvas 1 |
| `canvas-produto.md` | 7 blocos: Grande Promessa, Mecanismo Único, Proposta de Valor (7 tópicos) | Seção 2, Canvas 2 |
| `canvas-webinar.md` | 15 blocos: crença-alvo, ponte de crenças, entregáveis com valores, objeções/respostas | Seção 2, Canvas 3 |
| `avatar-blueprint.md` | 7 perguntas do Mapa do Avatar + Tabela Problema x Solução (8+ linhas) + desejos ocultos | Seção 5.1.1 |
| `orcamento-meta.md` | 12 premissas + cálculos automáticos (leads, cliques, comparecimentos, ROAS, margem) + benchmarks | Seção 2 Canvas 4 + Seção 3 |
| `planejamento-resumo.md` | Consolidação de todos os canvases com visão estratégica | Cross-reference |

**Detalhes de cada canvas:**

#### Canvas do Cliente Ideal (9 perguntas)
1. Quem é o público (critérios objetivos, não subjetivos)
2. Qual o principal problema/dor
3. O que já tentaram para resolver
4. Por que não funcionou
5. Qual o resultado que desejam
6. Quanto pagariam para resolver
7. Onde estão (canais, plataformas)
8. Quais objeções teriam
9. O que os faria agir agora

*Validação: critérios objetivos vs. subjetivos (pergunta 1). Suporte a múltiplos perfis de cliente.*

#### Canvas do Produto (7 blocos)
1. Grande Promessa — fórmula: "[Resultado] em [tempo] sem [obstáculo]"
2. Produto/Serviço (descrição)
3. Mecanismo Único — "duas ou três palavras que geram mistério"
4. Nome do Mecanismo Único
5. Diferencial competitivo
6. Prova (cases, resultados, dados)
7. Resumo da Proposta de Valor (template de 7 tópicos)

#### Canvas do Webinário Infalível (15 blocos)
Blocos 1-9: Estrutura geral (tema, título, objetivo, público, formato, data, plataforma, duração, estrutura)
Bloco 10: Crença-alvo — fórmula: "A única forma de ter [transformação] sem [obstáculo] é através do [mecanismo único]"
Bloco 11: Ponte de crenças (lista de tópicos/afirmações ordenáveis)
Bloco 12: Oferta (ticket, condições, garantia)
Bloco 13: Entregáveis (nome + descrição + valor R$ — para Stack Slide)
Bloco 14: Bônus (nome + descrição + valor R$)
Bloco 15: Objeções (pares objeção/resposta)

*Cross-reference: puxa dados do Canvas do Produto (blocos 10, 12, 13), Canvas do Cliente Ideal (bloco 15 — objeções) e Avatar Blueprint (blocos 10-11 — crença-alvo e ponte de crenças).*

#### Avatar Blueprint (7 perguntas + tabela)
1. Top 3 desejos → alimenta Headline + Lista + Transformação
2. Por que querem → alimenta Empatia + Conteúdo
3. O que atrapalha → alimenta Identificação + False Beliefs
4. Frustrações diárias → alimenta Espelhamento + História
5. Tendências que seguem → alimenta Posicionamento
6. Desejos ocultos → alimenta Pitch + Urgência
7. Razões para NÃO comprar → alimenta Objeções + Garantia

Tabela Problema x Solução: 8+ linhas (Problema | Soluções/"Cartas na Manga")

*Cross-reference: importa dados do Canvas do Cliente Ideal quando disponível.*

#### Planilha de Orçamento e Meta (12 premissas)
1. Meta de vendas (unidades)
2. Ticket do produto (R$)
3. Taxa de conversão vendas/leads — benchmark: 3%
4. Taxa de conversão página de captura — benchmark: 40%
5. Taxa de comparecimento — benchmark: 25%
6. Taxa de order bump — benchmark: variável
7. Ticket order bump (R$)
8. Taxa de upsell — benchmark: variável
9. Ticket upsell (R$)
10. Taxa de downsell — benchmark: variável
11. Ticket downsell (R$)
12. Custo por lead em mídia (R$) — benchmark: ~10% do ticket

*Cálculos automáticos: leads necessários, cliques, comparecimentos, faturamento bruto, faturamento total (com bump/upsell/downsell), investimento em ads, ROAS, margem líquida.*

---

### 3.3 @webinar-creator (Spark) — Construção de Conteúdo

**Papel:** Transforma os canvases em conteúdo pronto para uso: roteiro do webinário, copy de páginas, mensagens WhatsApp.

**O que faz:**
- Constrói o roteiro do webinário seção por seção (Abertura → Empatia → Conteúdo → Pitch)
- Gera copy de headlines usando as fórmulas da metodologia
- Cria 41+ templates de mensagens WhatsApp personalizados com dados da campanha
- Gera conteúdo para landing pages (captura, replay, fechamento)
- Sugere False Beliefs classificadas em Vehicle/Internal/External
- Monta composição do Stack Slide com valores e copy
- Usa dados dos canvases como input para todas as gerações

**Pré-requisito:** Canvases de planejamento preenchidos (mínimo: Cliente Ideal + Produto + Avatar Blueprint)

**Comandos:**
- `*abertura` — Construir seção de Abertura (7 blocos + Brunson)
- `*empatia` — Construir seção de Empatia/História (2 modelos + Epiphany Bridge)
- `*conteudo` — Construir seção de Conteúdo (3 Secrets + False Beliefs)
- `*pitch` — Construir seção de Pitch/Oferta (15 etapas + Stack Slide)
- `*roteiro` — Gerar roteiro completo consolidado com timeline
- `*mensagens` — Gerar biblioteca completa de mensagens WhatsApp (41+)
- `*headlines` — Gerar variações de headlines com fórmulas da metodologia
- `*copy-captura` — Gerar conteúdo para página de captura
- `*copy-replay` — Gerar conteúdo para página de replay
- `*copy-fechamento` — Gerar conteúdo para página de fechamento
- `*status` — Progresso dos artefatos de construção
- `*help` — Comandos disponíveis

**Artefatos gerados:**

| Artefato | Conteúdo | Referência |
|----------|----------|------------|
| `roteiro-abertura.md` | 7 blocos: Headline, Método, Apresentação, Lista, Urgência, Identificação, Regras + One Thing + Origin Story | Seção 5.2 |
| `roteiro-empatia.md` | Modelo escolhido (Avatar Transformado 7 passos OU Socorrista 4 passos) + técnica de transição + Epiphany Bridge | Seção 5.3 |
| `roteiro-conteudo.md` | 3 blocos (Vehicle/Internal/External): Falsa Crença → Nova Crença → Conteúdo "O Que" → Epiphany Bridge → Loop Aberto | Seção 5.4 |
| `roteiro-pitch.md` | 15 etapas: Transição → Produto → Stack → Dupla Queda de Preço → CTA → Bônus → Garantia → Urgência → CTA Final + Trial Closes | Seção 5.5 |
| `roteiro-completo.md` | Consolidação com timeline: Abertura 5-10min → Empatia 5-10min → Conteúdo 25-40min → Pitch 20-30min = 60-90min | Seção 5.6 |
| `mensagens-whatsapp.md` | 41+ templates por etapa: Nutrição (5), Antecipação D-1 (2), D-0 (7), Pós (1), Ampliação (7), Fechamento (11), Downsell (8) | Seção 4 |
| `copy-pagina-captura.md` | 2 formatos: Simples (headline + bullets + CTA) e Completa (página full para ingresso pago) | Seção 4, Etapa 1 |
| `copy-pagina-replay.md` | Pré-headline escassez, headline urgência, timestamps como headlines de venda, oferta com delay, SEM contador | Seção 4, Etapa 5 |
| `copy-pagina-fechamento.md` | Deadline explícito, headline oferta, COM contador regressivo, seção depoimentos, tudo carrega imediato | Seção 4, Etapa 6 |

**Detalhes das seções do roteiro:**

#### Abertura (5-10min) — 7 Blocos
1. **Headline** — 3 fórmulas: "Como X sem Y", "Como X mesmo que Z", "Como X em T" (puxa Avatar Blueprint: desejos + obstáculos)
2. **Método** — Apresentação do Mecanismo Único (puxa Canvas do Produto)
3. **Apresentação Pessoal** — com "Teste do Palco" e alerta de "Balelômetro"
4. **Lista de Aprendizado** — itens ao redor dos 3 Segredos (teaser Three Secrets)
5. **Urgência** — motivo para ficar até o final
6. **Identificação** — 4 fórmulas: Especificação+Frustração, Especificação+Desejo, Frustração+Medo, Desejo Oculto
7. **Regras** — template "Isso NÃO é um daqueles..." (3-5 diferenciações)

*Enriquecimento Brunson: One Thing Statement + Origin Story seed*

#### Empatia/História (5-10min) — 2 Modelos
**Modelo A — Avatar Transformado (7 passos):** Início → Dramatização → Invalidação de Soluções → Momento da Virada → O Método → Resultado → Transição
**Modelo B — Socorrista (4 passos):** Início → Caminho até Especialista → Decisão de Ajudar → Transição

**3 técnicas de transição:** Espelhamento de Situação, Espelhamento de Sentimento, História Disfarçada de Conteúdo

*Enriquecimento Brunson: Epiphany Bridge — "momento ESPECÍFICO de epifania, não conclusão gradual"*
*Alerta: 5-10 min no máximo. Remover história aumenta retenção mas destrói conversão.*

#### Conteúdo (25-40min) — 3 Secrets + False Beliefs
**Bloco 1 — Vehicle (Veículo):** Falsa crença sobre O QUE fazer → Nova crença → Conteúdo → Epiphany Bridge → Loop Aberto
**Bloco 2 — Internal (Interno):** Falsa crença sobre capacidade pessoal → Nova crença → Conteúdo → Epiphany Bridge → Loop Aberto
**Bloco 3 — External (Externo):** Falsa crença sobre obstáculos externos → Nova crença → Conteúdo → Epiphany Bridge → Loop Aberto

*Regra de ouro: "No webinário ensine O QUE fazer. O produto ensina COMO fazer."*
*Checklist por bloco: aplicável? Pessoa se vê fazendo? Nível adequado? Demonstra transformação?*
*Cross-reference: puxa objeções do Avatar Blueprint (campo 7) e classifica em Vehicle/Internal/External.*

#### Pitch/Oferta (20-30min) — 15 Etapas + Stack Slide
1. Transição (3 técnicas: A, B ou "Deixa eu te ajudar")
2. Como vai ajudar
3. Transformação
4. Apresentação do Produto (Stack: módulos com [Aprendizado] + [Benefício])
5. Preço — Dupla Queda: Âncora Alta (soma do stack) → Preço Oficial → Preço Promocional
6. CTA principal
7. Bônus de Ação Rápida (limitação: quantidade, tempo ou evento)
8. Reforço
9. Bônus adicionais (entram no Stack visual)
10. Garantia (puxa Canvas do Webinário, bloco 13)
11. Recapitulação (resumo automático de todos os itens do Stack + valor total)
12. Urgência/Escassez
13. Coerência
14. Q&A
15. CTA Final

*Trial Closes após cada etapa: "Faz sentido?", "Isso sozinho já valeria, não valeria?"*

#### Mensagens WhatsApp (41+ templates)

| Etapa do Funil | Qtd | Pilar da Espiral |
|----------------|-----|------------------|
| Nutrição | 5 | Engajamento |
| Antecipação D-1 | 2 | Compromisso |
| Antecipação D-0 | 7 | Compromisso |
| Pós-Webinário | 1 | Persuasão |
| Ampliação | 7 | Urgência |
| Fechamento | 11 | Escassez |
| Downsell | 8 | Persuasão + Urgência |

*Variáveis dinâmicas: {{nome_expert}}, {{data_webinario}}, {{link}}, {{produto}}, {{preco}}, {{bonus}}, {{presente}}*
*Cada template associado ao pilar da Espiral de Vendas e à etapa do funil.*

---

### 3.4 @webinar-operator (Atlas) — Execução

**Papel:** Guia o usuário na configuração das ferramentas existentes e no lançamento da campanha. Não constrói software — ensina a usar as ferramentas.

**O que faz:**
- Orienta setup do EverWebinar passo-a-passo (vídeo, agendamento, chat simulado, eventos)
- Orienta setup do SendFlow passo-a-passo (grupos WhatsApp, fases, automação, deep links)
- Orienta configuração de webhooks de pagamento (Zouti, Hotmart, Kiwify)
- Orienta Facebook Pixel e tracking
- Monta timeline/cronograma completo da campanha com datas reais
- Fornece checklist de lançamento com validação ponto a ponto
- Visualiza o funil de 7 etapas com status e próximas ações

**Pré-requisito:** Roteiro completo + mensagens geradas

**Comandos:**
- `*setup-everwebinar` — Guia de configuração do EverWebinar
- `*setup-sendflow` — Guia de configuração do SendFlow
- `*setup-pagamento` — Guia de configuração de webhooks de pagamento
- `*setup-pixel` — Guia de configuração do Facebook Pixel
- `*timeline` — Gerar cronograma completo da campanha com datas reais
- `*funil` — Visualizar funil de 7 etapas com status e ações
- `*checklist` — Checklist pré-lançamento
- `*status` — Progresso da configuração
- `*help` — Comandos disponíveis

**Artefatos gerados:**

| Artefato | Conteúdo | Referência |
|----------|----------|------------|
| `guia-everwebinar.md` | Setup: vídeo (Vimeo/YouTube), agendamento (diário/semanal), one-click registration, chat simulado, eventos timeline, replay, segmentação | Seção 6.1 |
| `guia-sendflow.md` | Setup: 3 fases (Pré/Pós/Conteúdo), cronograma semanal, 8 tipos de ação, 4 triggers, deep links com Pixel, transição entre fases | Seção 6.2 |
| `guia-pagamento.md` | Webhooks: 8 eventos (venda, abandono, boleto, chargeback, PIX, reembolso), ações automáticas (remover grupo, mensagem, tag, black list) | Seção 6.3 |
| `guia-pixel.md` | Facebook Pixel: eventos por página (PageView, Lead, Custom), integração deep link SendFlow, regra anti-duplicação | Seção 6.3.2 |
| `timeline-campanha.md` | Cronograma dia-a-dia: data, hora, mensagem, canal, pilar/objetivo — todas as etapas | Seção 4 |
| `funil-7-etapas.md` | 7 etapas: Captação → Nutrição → Antecipação → Abertura → Ampliação → Fechamento → Impulsionamento | Seção 4 |
| `checklist-lancamento.md` | Verificação ponto a ponto de tudo que precisa estar pronto antes de lançar | Cross-reference |

**Detalhes do funil de 7 etapas:**

| # | Etapa | Pilar | Gatilho de Transição |
|---|-------|-------|---------------------|
| 1 | Captação | — | Leads suficientes para meta |
| 2 | Nutrição | Engajamento | Data do webinário se aproximando |
| 3 | Antecipação | Compromisso | D-1 / D-0 |
| 4 | Abertura do Carrinho | Persuasão | Webinário realizado |
| 5 | Ampliação do Impacto | Urgência | Replay disponibilizado |
| 6 | Fechamento do Carrinho | Escassez | Deadline definido |
| 7 | Impulsionamento do Lucro | — | Pós-fechamento |

*Modos: Estrutura Básica (validação) vs. Estrutura Escalada (escala)*

---

### 3.5 @webinar-analyst (Lens) — Análise e Otimização

**Papel:** Analisa resultados pós-webinário, diagnostica gargalos no funil e sugere melhorias baseadas na metodologia.

**O que faz:**
- Coleta métricas reais da campanha via conversa com o usuário
- Compara com benchmarks da metodologia
- Identifica qual etapa do funil está abaixo da meta
- Sugere ações corretivas específicas baseadas na metodologia (não genéricas)
- Compara Orçado vs. Realizado com análise de desvio
- Planeja próxima rodada com otimizações
- Orienta estratégias avançadas (empilhamento, perpétuo, front-end/back-end)

**Pré-requisito:** Campanha executada com dados reais disponíveis

**Comandos:**
- `*kpis` — Registrar e analisar KPIs da campanha
- `*diagnostico` — Diagnóstico de funil (onde está o gargalo?)
- `*orcado-vs-realizado` — Comparar projeção com resultados reais
- `*proxima-rodada` — Planejar otimizações para próximo webinário
- `*empilhamento` — Planejar estratégia de empilhamento de webinários
- `*perpetuo` — Planejar conversão para modo perpétuo/evergreen
- `*frontend-backend` — Planejar modelo Front-end (VSL) + Back-end (Webinário)
- `*status` — Resultados registrados
- `*help` — Comandos disponíveis

**Artefatos gerados:**

| Artefato | Conteúdo | Referência |
|----------|----------|------------|
| `relatorio-kpis.md` | Métricas consolidadas: CPL, leads, comparecimentos, vendas por etapa, faturamento, ROAS, margem + comparação com benchmarks | Seção 3 |
| `diagnostico-funil.md` | Gargalos por etapa + ações corretivas específicas da metodologia | Seção 3 + Seção 4 |
| `orcado-vs-realizado.md` | Comparação das 12 premissas: orçado vs. real + análise de desvio + premissa que mais impactou | Seção 3 |
| `plano-proxima-rodada.md` | Otimizações priorizadas para próximo webinário baseadas nos dados reais | Cross-reference |
| `estrategia-empilhamento.md` | Funnel stacking: Web 1 → 2 → 3, custo lead via API vs. novo, ROI projetado | Seção 7.3 |
| `estrategia-perpetuo.md` | Conversão para evergreen: chat simulado, agendamento recorrente, funil semanal | Seção 7.1 |

**Benchmarks de referência:**

| Métrica | Benchmark | Fonte |
|---------|-----------|-------|
| Taxa de conversão vendas/leads | 3% | Seção 3 |
| Conversão página de captura | 40% | Seção 3 |
| Taxa de comparecimento | 25% | Seção 3 |
| Custo em mídia | ~10% do ticket | Seção 3 |
| Padrão de vendas | Pico 1 (abertura) → Vale → Pico 2 (fechamento) | Seção 4 |
| Custo lead empilhamento | R$0,06-0,25 (API) vs R$5-10 (novo) | Seção 7.3 |

**Diagnóstico de funil — lógica:**
- CPL alto → revisar criativos e segmentação (Etapa 1)
- Captura baixa → revisar congruência criativo-página e headline (Etapa 1)
- Comparecimento baixo → revisar antecipação e nutrição (Etapas 2-3)
- Conversão baixa com comparecimento ok → revisar roteiro do webinário (Black Box)
- Replay sem vendas → revisar página de replay e timing (Etapa 5)
- Fechamento fraco → revisar urgência/escassez e mensagens finais (Etapa 6)

---

## 4. Requisitos Não-Funcionais

| # | Requisito |
|---|-----------|
| NFR1 | Todos os agentes se comunicam em **Português Brasileiro**, sem jargão técnico de programação |
| NFR2 | Cada agente explica o **"porquê"** de cada passo, citando a metodologia quando relevante |
| NFR3 | Artefatos gerados são **markdown bem formatados**, legíveis, printáveis e compartilháveis |
| NFR4 | Agentes fazem **cross-reference** entre canvases (ex: Creator puxa dados do Avatar Blueprint) |
| NFR5 | Fluxo é **interruptível** — usuário pode parar e continuar depois (progresso salvo em arquivos) |
| NFR6 | Agentes **validam pré-requisitos** antes de avançar fase (ex: "Você precisa preencher o Avatar Blueprint primeiro") |
| NFR7 | Interação é por **conversa natural** — o agente faz perguntas uma por vez, não despeja formulário |
| NFR8 | Agentes são **agnósticos de nicho** — funcionam para qualquer produto/serviço |

---

## 5. Implementação Técnica

### 5.1 Definição dos Agentes

Cada agente é definido em `.aiox-core/development/agents/` como arquivo YAML/Markdown seguindo o padrão AIOX existente (mesmo formato de `pm.md`, `dev.md`, etc.).

### 5.2 Tasks

Cada comando de agente mapeia para uma task em `.aiox-core/development/tasks/` que define:
- Fluxo interativo (elicitation points)
- Inputs necessários (outros artefatos)
- Outputs gerados (path do artefato)
- Validações
- Knowledge base (seções do METHODOLOGY-ANALYSIS.md via Anexo A)

#### Pré-requisitos por Comando

Validação granular — cada comando declara seus inputs obrigatórios e opcionais:

**@webinar-strategist:**

| Comando | Inputs obrigatórios | Inputs opcionais (enriquecem) |
|---------|---------------------|-------------------------------|
| `*canvas-cliente` | — (primeiro artefato) | — |
| `*canvas-produto` | — (pode ser feito independente) | canvas-cliente-ideal.md (contexto do público) |
| `*avatar` | canvas-cliente-ideal.md | — |
| `*canvas-webinar` | canvas-produto.md, avatar-blueprint.md | canvas-cliente-ideal.md |
| `*orcamento` | — (premissas inseridas pelo usuário) | canvas-produto.md (ticket, oferta) |
| `*resumo` | Todos os 4 canvases + avatar-blueprint.md | orcamento-meta.md |

**@webinar-creator:**

| Comando | Inputs obrigatórios | Inputs opcionais (enriquecem) |
|---------|---------------------|-------------------------------|
| `*abertura` | avatar-blueprint.md, canvas-produto.md | canvas-webinar.md (blocos 1-7) |
| `*empatia` | avatar-blueprint.md | canvas-cliente-ideal.md |
| `*conteudo` | avatar-blueprint.md, canvas-webinar.md (blocos 10-11) | canvas-cliente-ideal.md (Tabela P×S) |
| `*pitch` | canvas-webinar.md (blocos 12-15), canvas-produto.md | orcamento-meta.md (ticket, condições) |
| `*roteiro` | roteiro-abertura + empatia + conteudo + pitch | — |
| `*mensagens` | canvas-produto.md, avatar-blueprint.md | orcamento-meta.md (datas, valores) |
| `*headlines` | avatar-blueprint.md (campos 1+3) | canvas-produto.md |
| `*copy-captura` | canvas-produto.md, avatar-blueprint.md | canvas-webinar.md |
| `*copy-replay` | roteiro-completo.md, canvas-webinar.md | — |
| `*copy-fechamento` | canvas-webinar.md (blocos 12-15), canvas-produto.md | — |

**@webinar-operator:**

| Comando | Inputs obrigatórios | Inputs opcionais (enriquecem) |
|---------|---------------------|-------------------------------|
| `*setup-everwebinar` | roteiro-completo.md, copy-pagina-captura.md | canvas-webinar.md (formato, plataforma) |
| `*setup-sendflow` | mensagens-whatsapp.md | timeline-campanha.md |
| `*setup-pagamento` | canvas-produto.md (ticket, condições) | — |
| `*setup-pixel` | — (instrucional) | copy-pagina-captura.md (URLs) |
| `*timeline` | roteiro-completo.md, mensagens-whatsapp.md | orcamento-meta.md (investimento, datas) |
| `*funil` | — (instrucional, baseado na metodologia) | timeline-campanha.md |
| `*checklist` | Todos os artefatos das fases anteriores | — |

**@webinar-analyst:**

| Comando | Inputs obrigatórios | Inputs opcionais (enriquecem) |
|---------|---------------------|-------------------------------|
| `*kpis` | orcamento-meta.md (benchmarks) | funil-7-etapas.md |
| `*diagnostico` | relatorio-kpis.md, funil-7-etapas.md | timeline-campanha.md |
| `*orcado-vs-realizado` | orcamento-meta.md, relatorio-kpis.md | — |
| `*proxima-rodada` | diagnostico-funil.md | Todos os canvases (para indicar revisões) |
| `*empilhamento` | relatorio-kpis.md | orcamento-meta.md |
| `*perpetuo` | roteiro-completo.md, relatorio-kpis.md | guia-everwebinar.md |
| `*frontend-backend` | canvas-produto.md, relatorio-kpis.md | — |

> **Regra de validação:** Quando o usuário executa um comando, o agente verifica se os inputs obrigatórios existem em `docs/webinar/rodada-{N}/`. Se não existirem, orienta: *"Para gerar o [artefato], preciso do [input]. Quer preencher agora?"* — redirecionando para o agente/comando correto.

### 5.3 Templates de Artefatos

Templates dos documentos gerados em `.aiox-core/development/templates/`:
- `canvas-cliente-ideal-tmpl.md`
- `canvas-produto-tmpl.md`
- `canvas-webinar-tmpl.md`
- `avatar-blueprint-tmpl.md`
- `orcamento-meta-tmpl.md`
- `roteiro-abertura-tmpl.md`
- `roteiro-empatia-tmpl.md`
- `roteiro-conteudo-tmpl.md`
- `roteiro-pitch-tmpl.md`
- `mensagens-whatsapp-tmpl.md`
- `guia-setup-tmpl.md`
- `timeline-campanha-tmpl.md`
- `relatorio-kpis-tmpl.md`

### 5.4 Knowledge Base

O documento `docs/METHODOLOGY-ANALYSIS.md` (4077 linhas) serve como knowledge base. O Anexo A deste PRD mapeia cada seção com line ranges exatos, permitindo que tasks carreguem apenas os trechos necessários.

Cada task declara no header quais seções precisa:

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "avatar-blueprint"
      lines: "L1722-L1866"
      purpose: "7 perguntas do avatar + Tabela P×S + One Big Domino"
```

O agente lê APENAS as linhas declaradas — sem carregar o documento inteiro no contexto.

### 5.5 Armazenamento de Artefatos

Estrutura organizada por rodada e fase, suportando empilhamento e modo perpétuo:

```
docs/webinar/
├── progress.md                          # Status geral — todas as rodadas (@webinar)
│
├── rodada-1/                            # Primeira execução do webinário
│   ├── planejamento/                    # Fase: Planejar (@webinar-strategist)
│   │   ├── canvas-cliente-ideal.md
│   │   ├── canvas-produto.md
│   │   ├── canvas-webinar.md
│   │   ├── avatar-blueprint.md
│   │   ├── orcamento-meta.md
│   │   └── planejamento-resumo.md
│   │
│   ├── conteudo/                        # Fase: Construir (@webinar-creator)
│   │   ├── roteiro-abertura.md
│   │   ├── roteiro-empatia.md
│   │   ├── roteiro-conteudo.md
│   │   ├── roteiro-pitch.md
│   │   ├── roteiro-completo.md
│   │   ├── mensagens-whatsapp.md
│   │   ├── copy-pagina-captura.md
│   │   ├── copy-pagina-replay.md
│   │   └── copy-pagina-fechamento.md
│   │
│   ├── execucao/                        # Fase: Executar (@webinar-operator)
│   │   ├── guia-everwebinar.md
│   │   ├── guia-sendflow.md
│   │   ├── guia-pagamento.md
│   │   ├── guia-pixel.md
│   │   ├── timeline-campanha.md
│   │   ├── funil-7-etapas.md
│   │   └── checklist-lancamento.md
│   │
│   └── analise/                         # Fase: Analisar (@webinar-analyst)
│       ├── relatorio-kpis.md
│       ├── diagnostico-funil.md
│       ├── orcado-vs-realizado.md
│       └── plano-proxima-rodada.md
│
├── rodada-2/                            # Empilhamento — mesma estrutura
│   └── ...                              # Canvases podem herdar da rodada-1 (apenas delta)
│
└── estrategias/                         # Documentos cross-rodada (@webinar-analyst)
    ├── estrategia-empilhamento.md
    └── estrategia-perpetuo.md
```

> **Regras:**
> - Cada rodada é autônoma — todos os artefatos de uma execução ficam juntos
> - `progress.md` na raiz mantém visão cross-rodada (qual rodada está ativa, histórico)
> - Na rodada-2+, canvases podem referenciar a rodada anterior com anotação "Herdado de rodada-1, ajustes: [...]"
> - `estrategias/` fica fora das rodadas porque se aplica ao negócio, não a uma execução específica

---

## 6. Epics

| Epic | Título | Goal | Entregáveis |
|------|--------|------|-------------|
| **1** | Squad Foundation | Definir os 5 agentes com personas, commands e handoff protocol | 5 agent definitions + squad config |
| **2** | Planning Tasks | Tasks interativas para os 5 canvases + calculadora de orçamento | 6 tasks + 6 templates |
| **3** | Content Creation Tasks | Tasks para roteiro (4 seções), mensagens (41+) e copy de 3 páginas | 10 tasks + 10 templates |
| **4** | Execution Guidance Tasks | Tasks para guias de setup de ferramentas, timeline e checklist | 7 tasks + 7 templates |
| **5** | Analysis Tasks | Tasks para KPIs, diagnóstico, orçado vs. realizado e estratégias avançadas | 6 tasks + 6 templates |

---

## 7. Next Steps

### 7.1 Squad Creation

> **Para @squad-creator:**
> Criar o squad "webinar" com os 5 agentes definidos neste PRD, seguindo o padrão AIOX. Cada agente deve ter: persona completa, commands mapeados para tasks, dependencies e handoff protocol.

### 7.2 Architect Review

> **Status: CONCLUÍDA** — @architect (Aria) revisou em 2026-03-05.
> 7 issues identificadas e aplicadas no PRD v2.1: pré-requisitos por comando, estrutura multi-rodada, cross-refs corrigidas, índice da knowledge base.

### 7.3 Task Development

> Após squad criado e arquitetura validada, desenvolver as tasks interativas por epic (2 → 3 → 4 → 5).

---

## Anexo A: Índice do METHODOLOGY-ANALYSIS.md

> Mapa de referência para que tasks dos agentes carreguem apenas os trechos necessários da knowledge base (4077 linhas).

### A.1 Espiral de Vendas (5 Pilares)

| Subseção | Linhas | Usado por |
|----------|--------|-----------|
| Espiral de Vendas — visão geral | L22-L80 | @webinar (contexto geral) |
| Pilar 1: Atração | L28-L34 | @webinar-operator |
| Pilar 2: Engajamento | L35-L41 | @webinar-creator (*mensagens: nutrição) |
| Pilar 3: Compromisso | L42-L48 | @webinar-creator (*mensagens: antecipação) |
| Pilar 4: Persuasão | L49-L55 | @webinar-creator (*roteiro, *pitch) |
| Pilar 5: Conversão | L56-L62 | @webinar-creator (*pitch) |
| Dinâmica + Sequência de Execução | L63-L80 | @webinar (orquestração) |

### A.2 Canvas de Planejamento

| Subseção | Linhas | Usado por |
|----------|--------|-----------|
| **Canvas 1: Cliente Ideal (9 perguntas)** | L83-L140 | @webinar-strategist (*canvas-cliente) |
| **Canvas 2: Produto (7 blocos)** | L141-L199 | @webinar-strategist (*canvas-produto) |
| **Canvas 3: Webinário Infalível (15 blocos)** | L200-L283 | @webinar-strategist (*canvas-webinar) |
| **Canvas 4: Orçamento e Meta (12 premissas)** | L284-L338 | @webinar-strategist (*orcamento) |

### A.3 Benchmarks e KPIs

| Subseção | Linhas | Usado por |
|----------|--------|-----------|
| KPIs de Funil (benchmarks) | L339-L352 | @webinar-analyst (*kpis) |
| KPIs de Resultado (exemplo modelado) | L353-L365 | @webinar-analyst (*kpis) |
| KPIs Adicionais | L366-L374 | @webinar-analyst (*diagnostico) |
| Fórmulas de Cálculo do Funil | L375-L389 | @webinar-strategist (*orcamento) |
| Comparação de Estratégias | L390-L397 | @webinar-analyst (*frontend-backend) |
| Orçado vs Realizado (estrutura) | L398-L408 | @webinar-analyst (*orcado-vs-realizado) |

### A.4 Funil Operacional — 7 Etapas

| Subseção | Linhas | Usado por |
|----------|--------|-----------|
| Visão Geral do Funil | L409-L421 | @webinar-operator (*funil) |
| Estrutura Básica vs. Escalada | L422-L434 | @webinar-operator (*funil) |
| **Etapa 1: Captação** | L451-L525 | @webinar-operator, @webinar-creator (*copy-captura) |
| **Etapa 2: Nutrição** | L526-L685 | @webinar-creator (*mensagens: 5 msgs nutrição) |
| **Etapa 3: Antecipação** | L686-L890 | @webinar-creator (*mensagens: 9 msgs antecipação) |
| **Etapa 4: Abertura do Carrinho** | L891-L984 | @webinar-creator (*roteiro), @webinar-operator (*setup-everwebinar) |
| **Etapa 5: Ampliação do Impacto** | L985-L1197 | @webinar-creator (*copy-replay, *mensagens: 7 msgs) |
| **Etapa 6: Fechamento do Carrinho** | L1198-L1463 | @webinar-creator (*copy-fechamento, *mensagens: 11 msgs) |
| **Etapa 7: Impulsionamento do Lucro** | L1464-L1651 | @webinar-creator (*mensagens: 8 msgs downsell), @webinar-analyst |
| Mapa de Ferramentas Consolidado | L1652-L1671 | @webinar-operator |
| Métricas e KPIs Consolidados | L1672-L1715 | @webinar-analyst (*kpis, *diagnostico) |

### A.5 Estrutura do Webinário — Black Box Fusionada

| Subseção | Linhas | Usado por |
|----------|--------|-----------|
| **5.1 Avatar Blueprint + One Big Domino** | L1722-L1866 | @webinar-strategist (*avatar) |
| **5.2 Abertura (7 Blocos + Brunson)** | L1867-L2039 | @webinar-creator (*abertura) |
| **5.3 Empatia/História + Epiphany Bridge** | L2040-L2251 | @webinar-creator (*empatia) |
| **5.4 Conteúdo (3 Secrets + False Beliefs)** | L2252-L2471 | @webinar-creator (*conteudo) |
| **5.5 Oferta/Pitch (15 Etapas + Stack Slide)** | L2472-L2832 | @webinar-creator (*pitch) |
| 5.6 Timeline Completa do Webinário | L2833-L2956 | @webinar-creator (*roteiro) |
| 5.7 Mapeamento de Fusão | L2957-L3040 | @webinar (referência geral) |
| 5.8 Glossário de Termos Proprietários | L3041-L3118 | Todos os agentes |

### A.6 Automação e Stack Técnica

| Subseção | Linhas | Usado por |
|----------|--------|-----------|
| **6.1 EverWebinar — Setup Completo** | L3123-L3359 | @webinar-operator (*setup-everwebinar) |
| **6.2 SendFlow — Automação WhatsApp** | L3360-L3597 | @webinar-operator (*setup-sendflow) |
| **6.3 Integrações e Webhooks** | L3598-L3735 | @webinar-operator (*setup-pagamento, *setup-pixel) |
| **6.4 Stack Técnica Completa** | L3736-L3758 | @webinar-operator |
| **6.5 Segmentação e Tags** | L3759-L3829 | @webinar-operator, @webinar-analyst |

### A.7 Estratégias Avançadas

| Subseção | Linhas | Usado por |
|----------|--------|-----------|
| **7.1 Webinário Perpétuo (Evergreen)** | L3834-L3872 | @webinar-analyst (*perpetuo) |
| **7.2 IA Aplicada a Webinários** | L3873-L3899 | @webinar (referência) |
| **7.3 Empilhamento (Funnel Stacking)** | L3900-L3918 | @webinar-analyst (*empilhamento) |
| **7.4 Modelo Front-end + Back-end** | L3919-L3944 | @webinar-analyst (*frontend-backend) |
| **7.5 Esteira de Produtos** | L3945-L3964 | @webinar-analyst (*empilhamento) |
| **7.6 Métricas e Benchmarks Consolidados** | L3965-L3991 | @webinar-analyst (*kpis) |
| **7.7 Estratégias Operacionais Adicionais** | L3992-L4077 | Vários agentes |

---

*Synkra AIOX — PRD v2.1 gerado por @pm (Morgan), revisado por @architect (Aria)*
*Squad de Agentes IA para Webinários — NÃO é uma plataforma web*
