# Arquitetura: Sistema de Gestão de Projetos de Webinários

> **Documento:** Decisão Arquitetural — Estrutura de Projetos
> **Autor:** @architect (Aria)
> **Data:** 2026-03-05
> **Status:** Proposta

---

## 1. Visão Geral

### 1.1 O Problema

Atualmente, o sistema organiza artefatos de webinários por rodada em `docs/webinar/rodada-{N}/`. Isso funciona para um único webinário, mas não escala quando o usuário tem **múltiplos projetos de webinários diferentes**.

**Exemplo real:**
- "Lançamento Curso de Nutrição" (webinário sobre emagrecimento)
- "Workshop de Copywriting" (webinário sobre escrita persuasiva)
- "Infoproduto de Finanças" (webinário sobre investimentos)

Cada um é um **projeto diferente** (público, produto, oferta, canvases únicos), mas cada um pode ter **múltiplas rodadas** (lançamentos ao longo do tempo).

### 1.2 A Solução

Criar uma estrutura `Projetos/` onde:
1. Cada webinário é um **projeto** com pasta própria
2. Cada projeto contém **todas as suas rodadas**
3. O Maestro (`@webinar`) gerencia a seleção de projeto no início de cada conversa
4. O sistema mantém contexto do projeto ativo durante a sessão

---

## 2. Nova Estrutura de Pastas

### 2.1 Árvore Completa

```
Projetos/
│
├── lancamento-curso-nutricao/               # Projeto 1
│   ├── projeto.yaml                         # Manifest do projeto
│   ├── rodada-1/                            # Primeira execução
│   │   ├── planejamento/
│   │   │   ├── canvas-cliente-ideal.md
│   │   │   ├── canvas-produto.md
│   │   │   ├── canvas-webinar.md
│   │   │   ├── avatar-blueprint.md
│   │   │   ├── orcamento-meta.md
│   │   │   └── planejamento-resumo.md
│   │   ├── conteudo/
│   │   │   ├── roteiro-abertura.md
│   │   │   ├── roteiro-empatia.md
│   │   │   ├── roteiro-conteudo.md
│   │   │   ├── roteiro-pitch.md
│   │   │   ├── roteiro-completo.md
│   │   │   ├── mensagens-whatsapp.md
│   │   │   ├── copy-pagina-captura.md
│   │   │   ├── copy-pagina-replay.md
│   │   │   └── copy-pagina-fechamento.md
│   │   ├── execucao/
│   │   │   ├── guia-everwebinar.md
│   │   │   ├── guia-sendflow.md
│   │   │   ├── guia-pagamento.md
│   │   │   ├── guia-pixel.md
│   │   │   ├── timeline-campanha.md
│   │   │   ├── funil-7-etapas.md
│   │   │   └── checklist-lancamento.md
│   │   └── analise/
│   │       ├── relatorio-kpis.md
│   │       ├── diagnostico-funil.md
│   │       ├── orcado-vs-realizado.md
│   │       └── plano-proxima-rodada.md
│   │
│   ├── rodada-2/                            # Segunda execução
│   │   └── (mesma estrutura)
│   │
│   └── estrategias/                         # Cross-rodada
│       ├── estrategia-empilhamento.md
│       └── estrategia-perpetuo.md
│
├── workshop-copywriting/                    # Projeto 2
│   ├── projeto.yaml
│   ├── rodada-1/
│   │   └── ...
│   └── estrategias/
│
└── infoproduto-financas/                    # Projeto 3
    ├── projeto.yaml
    ├── rodada-1/
    │   └── ...
    └── estrategias/

.aiox/
└── webinar-context.yaml                     # Projeto ativo na sessão atual
```

### 2.2 Diferenças da Estrutura Antiga

| Estrutura Antiga | Estrutura Nova |
|------------------|----------------|
| `docs/webinar/rodada-1/` | `Projetos/{nome-projeto}/rodada-1/` |
| `docs/webinar/progress.md` (único) | `Projetos/{projeto}/projeto.yaml` (por projeto) |
| Sem separação de projetos | Cada projeto = pasta isolada |
| Maestro sem contexto de projeto | Maestro gerencia projeto ativo |

---

## 3. Manifest do Projeto (projeto.yaml)

Cada projeto tem um arquivo `projeto.yaml` na raiz de sua pasta:

```yaml
# projeto.yaml — Manifest do Projeto de Webinário

# ============================================
# IDENTIFICAÇÃO
# ============================================
nome: "Lançamento Curso de Nutrição"
slug: "lancamento-curso-nutricao"          # Nome da pasta (sem espaços, lowercase)
descricao: "Webinário para venda de curso online de emagrecimento saudável"

criado_em: "2026-03-05"
atualizado_em: "2026-03-05"

# ============================================
# PRODUTO E NICHO
# ============================================
nicho: "Nutrição e Emagrecimento"
produto: "Curso Online: Emagreça com Saúde"
ticket: 497.00                              # R$ do produto principal

# ============================================
# RODADAS
# ============================================
rodadas:
  - numero: 1
    status: "Done"                          # Draft | InProgress | Done
    data_webinario: "2026-01-15"
    faturamento: 29820.00
    leads: 1850
    vendas: 60

  - numero: 2
    status: "InProgress"
    data_webinario: "2026-04-10"
    faturamento: null
    leads: null
    vendas: null

rodada_ativa: 2                             # Qual rodada está sendo trabalhada

# ============================================
# PROGRESSO POR FASE
# ============================================
fases:
  planejamento:
    status: "Completed"
    artefatos_completos:
      - canvas-cliente-ideal.md
      - canvas-produto.md
      - canvas-webinar.md
      - avatar-blueprint.md
      - orcamento-meta.md
      - planejamento-resumo.md
    ultima_atualizacao: "2026-03-02"

  construcao:
    status: "InProgress"
    artefatos_completos:
      - roteiro-abertura.md
      - roteiro-empatia.md
    artefatos_pendentes:
      - roteiro-conteudo.md
      - roteiro-pitch.md
      - roteiro-completo.md
      - mensagens-whatsapp.md
      - copy-pagina-captura.md
      - copy-pagina-replay.md
      - copy-pagina-fechamento.md
    ultima_atualizacao: "2026-03-05"

  execucao:
    status: "Pending"
    artefatos_completos: []
    artefatos_pendentes:
      - guia-everwebinar.md
      - guia-sendflow.md
      - guia-pagamento.md
      - guia-pixel.md
      - timeline-campanha.md
      - funil-7-etapas.md
      - checklist-lancamento.md
    ultima_atualizacao: null

  analise:
    status: "Pending"
    artefatos_completos: []
    artefatos_pendentes:
      - relatorio-kpis.md
      - diagnostico-funil.md
      - orcado-vs-realizado.md
      - plano-proxima-rodada.md
    ultima_atualizacao: null

# ============================================
# ESTRATÉGIAS AVANÇADAS
# ============================================
estrategias:
  empilhamento: false                       # Webinários empilhados?
  perpetuo: false                           # Modo evergreen?
  frontend_backend: false                   # VSL + Webinário?

# ============================================
# NOTAS E CONTEXTO
# ============================================
notas: |
  - Público: Mulheres 30-50 anos, classe B/C
  - Diferencial: Método sem dietas restritivas
  - Rodada 1 teve boa conversão (3.2%), mas comparecimento baixo (18%)
  - Rodada 2 vai focar em aumentar comparecimento via antecipação
```

### 3.1 Por que YAML e não Markdown?

- **Estruturado:** Fácil de ler programaticamente (agentes podem parsear)
- **Status claro:** Rodada ativa, progresso por fase, artefatos completos/pendentes
- **Histórico:** Todas as rodadas listadas com resultados
- **Leve:** Manifest pequeno, não compete com os artefatos markdown (que são detalhados)

---

## 4. Fluxo do Maestro (@webinar)

### 4.1 Início de Conversa — Seleção de Projeto

Quando o usuário invoca `@webinar`, o agente:

1. **Verifica contexto da sessão** (`.aiox/webinar-context.yaml`)
2. **Se houver projeto ativo:** Resume progresso e pergunta se quer continuar ou mudar
3. **Se não houver projeto ativo:** Lista projetos existentes e oferece criar novo

**Exemplo de interação:**

```
Usuário: @webinar

Maestro:
Olá! Vejo que você tem 3 projetos de webinários:

1. 📁 Lançamento Curso de Nutrição
   Status: Rodada 2 em andamento (Construção 45% completa)
   Última atualização: 5 de março

2. 📁 Workshop de Copywriting
   Status: Rodada 1 concluída (faturou R$15.400)
   Próxima: Planejar rodada 2

3. 📁 Infoproduto de Finanças
   Status: Novo projeto (Planejamento iniciado)

Qual projeto você quer trabalhar agora?
- Digite o número (1, 2 ou 3)
- Ou digite 'novo' para criar um projeto novo

Usuário: 1

Maestro:
Perfeito! Ativando projeto: Lançamento Curso de Nutrição (Rodada 2).

📊 Status atual:
- ✅ Planejamento: 100% completo
- 🔄 Construção: 45% completo (falta roteiro de conteúdo e pitch)
- ⏸️ Execução: Aguardando
- ⏸️ Análise: Aguardando

O que você quer fazer agora?
- Continuar construindo o roteiro → digite *construir
- Ver progresso detalhado → digite *status
- Ver todas as opções → digite *help
```

### 4.2 Contexto da Sessão (`.aiox/webinar-context.yaml`)

Arquivo temporário que registra o projeto ativo na sessão:

```yaml
# .aiox/webinar-context.yaml
projeto_ativo: "lancamento-curso-nutricao"
rodada_ativa: 2
ativado_em: "2026-03-05T15:30:00"
ultima_interacao: "2026-03-05T16:45:00"
```

**Persistência:** Este arquivo é atualizado sempre que o Maestro ativa um projeto e serve como memória de curto prazo. Se o usuário fechar e reabrir Claude Code, o Maestro pergunta se quer continuar de onde parou.

### 4.3 Comandos do Maestro Atualizados

| Comando | Comportamento |
|---------|---------------|
| `*projetos` | Lista todos os projetos e permite selecionar |
| `*novo-projeto` | Cria novo projeto (pergunta nome, nicho, produto, ticket) |
| `*status` | Mostra progresso do projeto ativo (todas as fases) |
| `*rodadas` | Lista rodadas do projeto ativo (histórico + ativa) |
| `*nova-rodada` | Cria nova rodada no projeto ativo |
| `*mudar-projeto` | Troca o projeto ativo |
| `*planejar` | Inicia/continua planejamento → @webinar-strategist |
| `*construir` | Inicia/continua construção → @webinar-creator |
| `*executar` | Inicia/continua execução → @webinar-operator |
| `*analisar` | Inicia/continua análise → @webinar-analyst |
| `*guia` | Explica o processo completo de webinários |
| `*help` | Mostra todos os comandos |

---

## 5. Delegação para Agentes Especializados

### 5.1 Como os Agentes Encontram os Artefatos?

Cada agente especializado (`@webinar-strategist`, `@webinar-creator`, etc.) precisa saber **onde** salvar e **onde** buscar os artefatos.

**Solução:** O Maestro passa o **contexto do projeto** ao delegar:

```yaml
# Contexto passado ao @webinar-creator
projeto:
  nome: "Lançamento Curso de Nutrição"
  slug: "lancamento-curso-nutricao"
  rodada_ativa: 2
  base_path: "Projetos/lancamento-curso-nutricao/rodada-2/"

pre_requisitos:
  avatar-blueprint: "Projetos/lancamento-curso-nutricao/rodada-2/planejamento/avatar-blueprint.md"
  canvas-produto: "Projetos/lancamento-curso-nutricao/rodada-2/planejamento/canvas-produto.md"
  canvas-webinar: "Projetos/lancamento-curso-nutricao/rodada-2/planejamento/canvas-webinar.md"
```

**Com isso, o agente especializado:**
1. Sabe onde encontrar os canvases necessários (cross-reference)
2. Sabe onde salvar os novos artefatos (`base_path + pasta da fase`)
3. Atualiza o `projeto.yaml` ao completar artefatos

### 5.2 Herança de Artefatos entre Rodadas

**Cenário:** Rodada 2 pode reusar canvases da Rodada 1 (avatar não muda muito).

**Solução:**
- Quando o usuário cria Rodada 2, o Maestro pergunta: *"Quer copiar os canvases de planejamento da Rodada 1?"*
- Se sim: copia `rodada-1/planejamento/*.md` → `rodada-2/planejamento/*.md` e marca com cabeçalho:

```markdown
> ⚠️ **Herdado da Rodada 1** — Revisado em 05/03/2026
> Ajustes: Refinamento do avatar com dados reais de conversão
```

- O `@webinar-strategist` pode editar normalmente (não é read-only)

---

## 6. Criação de Novo Projeto

### 6.1 Fluxo Interativo

```
Usuário: @webinar *novo-projeto

Maestro:
Vamos criar um novo projeto de webinário! Preciso de algumas informações:

1️⃣ Qual o nome do projeto? (ex: "Lançamento Curso de Nutrição")

Usuário: Workshop de Inteligência Emocional

Maestro:
Ótimo! "Workshop de Inteligência Emocional".

2️⃣ Qual o nicho/mercado? (ex: "Desenvolvimento Pessoal", "Finanças")

Usuário: Psicologia e Desenvolvimento Pessoal

Maestro:
Perfeito!

3️⃣ Qual o nome do produto/serviço que você vai vender?

Usuário: Método de Gestão Emocional — 8 Semanas

Maestro:
Entendi.

4️⃣ Qual o valor (ticket) do produto? (em R$)

Usuário: 697

Maestro:
✅ Projeto criado com sucesso!

📁 Workshop de Inteligência Emocional
   Nicho: Psicologia e Desenvolvimento Pessoal
   Produto: Método de Gestão Emocional — 8 Semanas
   Ticket: R$ 697,00
   Rodada: 1 (ativa)

O projeto foi salvo em:
Projetos/workshop-inteligencia-emocional/

Próximo passo: Planejar o webinário.
Digite *planejar para começar com os canvases.
```

### 6.2 Estrutura Criada Automaticamente

O Maestro cria:

1. **Pasta do projeto:** `Projetos/workshop-inteligencia-emocional/`
2. **Manifest:** `projeto.yaml` com dados básicos e rodada-1 inicializada
3. **Subpastas da rodada:** `rodada-1/planejamento/`, `rodada-1/conteudo/`, `rodada-1/execucao/`, `rodada-1/analise/`
4. **Contexto da sessão:** `.aiox/webinar-context.yaml` apontando para o novo projeto

---

## 7. Atualização de Progresso

### 7.1 Quando um Agente Completa um Artefato

Exemplo: `@webinar-creator` gera `roteiro-abertura.md`.

**Ações automáticas:**
1. Salva o arquivo em `Projetos/{projeto}/rodada-{N}/conteudo/roteiro-abertura.md`
2. Atualiza `projeto.yaml`:
   ```yaml
   fases:
     construcao:
       artefatos_completos:
         - roteiro-abertura.md  # ← adiciona
       artefatos_pendentes:
         - roteiro-empatia.md
         - ...
       ultima_atualizacao: "2026-03-05"
   ```
3. Informa ao usuário: *"✅ Roteiro de Abertura gerado! Faltam 8 artefatos para concluir a fase de Construção."*

### 7.2 Dashboard de Progresso (`*status`)

```
Usuário: *status

Maestro:
📊 Projeto: Lançamento Curso de Nutrição (Rodada 2)

🟢 PLANEJAMENTO — 100% completo
   ✅ canvas-cliente-ideal.md
   ✅ canvas-produto.md
   ✅ canvas-webinar.md
   ✅ avatar-blueprint.md
   ✅ orcamento-meta.md
   ✅ planejamento-resumo.md

🟡 CONSTRUÇÃO — 45% completo (4 de 9)
   ✅ roteiro-abertura.md
   ✅ roteiro-empatia.md
   ⏸️ roteiro-conteudo.md
   ⏸️ roteiro-pitch.md
   ⏸️ roteiro-completo.md
   ⏸️ mensagens-whatsapp.md
   ⏸️ copy-pagina-captura.md
   ⏸️ copy-pagina-replay.md
   ⏸️ copy-pagina-fechamento.md

⚪ EXECUÇÃO — Aguardando (0 de 7)

⚪ ANÁLISE — Aguardando (0 de 4)

Próxima ação sugerida:
Digite *construir para continuar o roteiro (falta conteúdo e pitch).
```

---

## 8. Impacto e Migrações

### 8.1 Arquivos Afetados

| Arquivo/Pasta | Mudança |
|---------------|---------|
| **Maestro (`@webinar`)** | Adicionar comandos: `*projetos`, `*novo-projeto`, `*rodadas`, `*nova-rodada`, `*mudar-projeto` |
| **Tasks do Maestro** | Nova task: `criar-projeto.md`, `selecionar-projeto.md`, `criar-rodada.md` |
| **Agentes especializados** | Atualizar paths: receber `base_path` do Maestro, salvar em `Projetos/{projeto}/rodada-{N}/` |
| **Templates** | Adicionar: `projeto-manifest-tmpl.yaml`, `webinar-context-tmpl.yaml` |
| **Estrutura antiga** | Migrar `docs/webinar/rodada-1/` → `Projetos/{primeiro-projeto}/rodada-1/` (manual ou via comando) |

### 8.2 Migração de Projetos Existentes

Se já existe `docs/webinar/rodada-1/`, o Maestro oferece migração:

```
Maestro:
Detectei artefatos de webinário na estrutura antiga (docs/webinar/).

Quer migrar para o novo sistema de projetos?
- Sim → Crio um projeto com esses artefatos
- Não → Mantenho os arquivos onde estão (mas não funcionarão com comandos novos)

Usuário: Sim

Maestro:
Perfeito! Qual o nome do projeto? (ex: "Lançamento Curso de Nutrição")

Usuário: Meu Primeiro Webinário

Maestro:
✅ Projeto migrado!

Artefatos movidos de docs/webinar/rodada-1/ para:
Projetos/meu-primeiro-webinario/rodada-1/

Manifest criado em:
Projetos/meu-primeiro-webinario/projeto.yaml
```

### 8.3 Plano de Migração (Tasks)

| Task | Responsável | Ordem |
|------|-------------|-------|
| Criar template `projeto.yaml` | @architect | 1 |
| Criar template `webinar-context.yaml` | @architect | 2 |
| Atualizar definição do `@webinar` (comandos novos) | @squad-creator | 3 |
| Criar task `criar-projeto.md` | @dev | 4 |
| Criar task `selecionar-projeto.md` | @dev | 5 |
| Criar task `criar-rodada.md` | @dev | 6 |
| Atualizar `@webinar-strategist` (paths dinâmicos) | @dev | 7 |
| Atualizar `@webinar-creator` (paths dinâmicos) | @dev | 8 |
| Atualizar `@webinar-operator` (paths dinâmicos) | @dev | 9 |
| Atualizar `@webinar-analyst` (paths dinâmicos) | @dev | 10 |
| Criar comando `*migrar` no Maestro | @dev | 11 |
| Testar fluxo completo novo → rodada-1 → rodada-2 | @qa | 12 |

---

## 9. Benefícios da Nova Arquitetura

| Benefício | Descrição |
|-----------|-----------|
| **Isolamento** | Cada webinário tem sua própria pasta — não mistura projetos |
| **Escalabilidade** | Usuário pode ter 5, 10, 20 projetos sem confusão |
| **Histórico claro** | `projeto.yaml` registra todas as rodadas com resultados |
| **Reutilização** | Rodada 2+ pode herdar canvases da rodada anterior |
| **Contexto persistente** | `.aiox/webinar-context.yaml` mantém projeto ativo entre sessões |
| **Navegação intuitiva** | Maestro lista projetos, usuário escolhe qual trabalhar |
| **Output organizado** | Tudo do projeto fica em um lugar — fácil de compartilhar/arquivar |

---

## 10. Exemplo de Uso Completo

### 10.1 Cenário Real

Usuário tem 2 projetos:
1. "Lançamento Curso de Nutrição" — Rodada 2 em andamento
2. "Workshop de Copywriting" — Rodada 1 concluída, quer planejar Rodada 2

**Fluxo:**

```
# Sessão 1 — Trabalhar no Curso de Nutrição
@webinar
> Lista projetos → usuário escolhe "1"
*construir
> @webinar-creator gera roteiro-conteudo.md
> Salva em Projetos/lancamento-curso-nutricao/rodada-2/conteudo/
> Atualiza projeto.yaml

# Sessão 2 (outro dia) — Trabalhar no Workshop de Copywriting
@webinar
> Maestro pergunta: "Quer continuar 'Curso de Nutrição'?" → usuário: "Não, mudar"
*mudar-projeto
> Lista projetos → usuário escolhe "2"
*nova-rodada
> Maestro cria rodada-2/ e pergunta se quer herdar canvases
*planejar
> @webinar-strategist revisa avatar-blueprint.md herdado da rodada-1
```

---

## 11. Glossário

| Termo | Definição |
|-------|-----------|
| **Projeto** | Um webinário específico (ex: "Curso de Nutrição") com produto, nicho e público únicos |
| **Rodada** | Uma execução do webinário (ex: lançamento em janeiro = rodada-1, lançamento em abril = rodada-2) |
| **Manifest** | Arquivo `projeto.yaml` com metadados, progresso e histórico do projeto |
| **Contexto da sessão** | Arquivo `.aiox/webinar-context.yaml` que registra qual projeto está ativo |
| **Herança** | Copiar artefatos da rodada anterior para a nova (ex: canvases que não mudam muito) |
| **Base path** | Caminho raiz do projeto (ex: `Projetos/lancamento-curso-nutricao/rodada-2/`) |

---

## 12. Próximos Passos

### 12.1 Para o Owner (Não-Técnico)

**O que isso significa para você:**
- Você poderá trabalhar em **vários webinários ao mesmo tempo** sem confusão
- Cada webinário terá sua própria **pasta organizada** com tudo dentro
- Quando abrir Claude Code, o sistema vai **perguntar qual projeto** você quer trabalhar
- Se você fizer a **mesma oferta de novo** (rodada 2), não precisa refazer tudo do zero — pode reaproveitar os canvases

**Nada muda no jeito de usar:**
- Você ainda vai digitar `@webinar`, `*planejar`, `*construir`, etc.
- Os agentes ainda vão conversar com você do mesmo jeito
- Os documentos gerados continuam sendo markdown (legíveis, imprimíveis)

**Único acréscimo:**
- Agora você vai dar um **nome** para cada projeto de webinário (ex: "Curso de Nutrição")
- E vai escolher qual projeto trabalhar quando começar uma sessão

### 12.2 Para Implementação Técnica

1. **@architect** cria templates (projeto.yaml, webinar-context.yaml)
2. **@squad-creator** atualiza definição do `@webinar` com comandos novos
3. **@dev** implementa tasks: `criar-projeto`, `selecionar-projeto`, `criar-rodada`
4. **@dev** atualiza os 4 agentes especializados (paths dinâmicos)
5. **@qa** testa fluxo multi-projeto + herança de rodadas

---

**Documento completo. Pronto para validação e implementação.**

*@architect (Aria) — 2026-03-05*
