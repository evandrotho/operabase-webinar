# Diagramas — Sistema de Projetos

> **Documento:** Visualizações da arquitetura
> **Data:** 2026-03-05

---

## 1. Estrutura de Pastas

### 1.1 Visão Geral

```
Projetos/
│
├── lancamento-curso-nutricao/
│   ├── projeto.yaml
│   ├── rodada-1/
│   │   ├── planejamento/
│   │   ├── conteudo/
│   │   ├── execucao/
│   │   └── analise/
│   ├── rodada-2/
│   │   └── (mesma estrutura)
│   └── estrategias/
│
├── workshop-copywriting/
│   ├── projeto.yaml
│   ├── rodada-1/
│   │   └── ...
│   └── estrategias/
│
└── infoproduto-financas/
    └── ...
```

### 1.2 Estrutura Detalhada de Um Projeto

```
Projetos/lancamento-curso-nutricao/
│
├── projeto.yaml                             ← Manifest do projeto
│
├── rodada-1/                                ← Primeira execução
│   │
│   ├── planejamento/                        ← Fase 1 (@webinar-strategist)
│   │   ├── canvas-cliente-ideal.md
│   │   ├── canvas-produto.md
│   │   ├── canvas-webinar.md
│   │   ├── avatar-blueprint.md
│   │   ├── orcamento-meta.md
│   │   └── planejamento-resumo.md
│   │
│   ├── conteudo/                            ← Fase 2 (@webinar-creator)
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
│   ├── execucao/                            ← Fase 3 (@webinar-operator)
│   │   ├── guia-everwebinar.md
│   │   ├── guia-sendflow.md
│   │   ├── guia-pagamento.md
│   │   ├── guia-pixel.md
│   │   ├── timeline-campanha.md
│   │   ├── funil-7-etapas.md
│   │   └── checklist-lancamento.md
│   │
│   └── analise/                             ← Fase 4 (@webinar-analyst)
│       ├── relatorio-kpis.md
│       ├── diagnostico-funil.md
│       ├── orcado-vs-realizado.md
│       └── plano-proxima-rodada.md
│
├── rodada-2/                                ← Segunda execução
│   └── (mesma estrutura de rodada-1)
│
└── estrategias/                             ← Cross-rodada (@webinar-analyst)
    ├── estrategia-empilhamento.md
    └── estrategia-perpetuo.md
```

---

## 2. Fluxo de Seleção de Projeto

```
┌─────────────────────────────────────────────────────────────────┐
│                    USUÁRIO INICIA CONVERSA                      │
│                         @webinar                                │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  Existe .aiox/webinar-context.yaml?   │
        └───────────┬───────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
       SIM                     NÃO
        │                       │
        ▼                       ▼
┌───────────────────┐   ┌──────────────────────┐
│ Projeto ativo:    │   │ Listar projetos em   │
│ "Curso Nutrição"  │   │ Projetos/            │
│                   │   │                      │
│ Quer continuar?   │   │ 1. Curso Nutrição    │
│ [Sim] [Não]       │   │ 2. Workshop Copy     │
└────────┬──────────┘   │ 3. Infoproduto Fin   │
         │              │                      │
    ┌────┴─────┐        │ Escolha (1-3) ou     │
   SIM        NÃO       │ 'novo'               │
    │          │        └──────────┬───────────┘
    │          │                   │
    │          └───────────┬───────┘
    │                      │
    ▼                      ▼
┌─────────────┐    ┌──────────────────────┐
│ Carregar    │    │ Usuário escolhe:     │
│ projeto     │    │ - Número (1-3)       │
│ ativo       │    │ - 'novo'             │
└──────┬──────┘    └──────────┬───────────┘
       │                      │
       │           ┌──────────┴──────────┐
       │          NOVO                NÚMERO
       │           │                     │
       │           ▼                     ▼
       │   ┌────────────────┐   ┌────────────────┐
       │   │ *novo-projeto  │   │ Ativar projeto │
       │   │ (interativo)   │   │ selecionado    │
       │   └───────┬────────┘   └───────┬────────┘
       │           │                    │
       │           └────────┬───────────┘
       │                    │
       └────────────────────┤
                            ▼
            ┌───────────────────────────────┐
            │ Atualizar                     │
            │ .aiox/webinar-context.yaml    │
            │                               │
            │ projeto_ativo: "{slug}"       │
            │ rodada_ativa: {N}             │
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │ PROJETO ATIVO                 │
            │                               │
            │ Comandos disponíveis:         │
            │ *status, *planejar,           │
            │ *construir, *executar,        │
            │ *analisar, *nova-rodada       │
            └───────────────────────────────┘
```

---

## 3. Fluxo de Criação de Projeto

```
┌─────────────────────────────────────────────┐
│    USUÁRIO: @webinar *novo-projeto          │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ MAESTRO PERGUNTA:                            │
│ "Qual o nome do projeto?"                    │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ USUÁRIO: "Lançamento Curso de Nutrição"      │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ MAESTRO PERGUNTA:                            │
│ "Qual o nicho/mercado?"                      │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ USUÁRIO: "Nutrição e Emagrecimento"          │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ MAESTRO PERGUNTA:                            │
│ "Qual o nome do produto/serviço?"            │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ USUÁRIO: "Curso: Emagreça com Saúde"         │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ MAESTRO PERGUNTA:                            │
│ "Qual o valor (ticket) do produto? (R$)"     │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ USUÁRIO: "497"                               │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ MAESTRO PROCESSA:                            │
│                                              │
│ 1. Gera slug: "lancamento-curso-nutricao"    │
│ 2. Cria pasta: Projetos/{slug}/              │
│ 3. Cria subpastas: rodada-1/planejamento/... │
│ 4. Gera projeto.yaml com dados               │
│ 5. Atualiza .aiox/webinar-context.yaml       │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ MAESTRO CONFIRMA:                            │
│                                              │
│ ✅ Projeto criado!                           │
│                                              │
│ 📁 Lançamento Curso de Nutrição              │
│    Nicho: Nutrição e Emagrecimento           │
│    Produto: Curso: Emagreça com Saúde        │
│    Ticket: R$ 497,00                         │
│    Rodada: 1 (ativa)                         │
│                                              │
│ Próximo passo: Digite *planejar              │
└──────────────────────────────────────────────┘
```

---

## 4. Fluxo de Delegação para Agentes

```
┌──────────────────────────────────────────────────────────────────┐
│                         USUÁRIO                                  │
│                    @webinar *construir                           │
└───────────────────────────────┬──────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────┐
│                     MAESTRO (@webinar)                            │
│                                                                   │
│ 1. Lê .aiox/webinar-context.yaml → projeto_ativo = "curso-...    │
│ 2. Lê Projetos/curso-nutricao/projeto.yaml → rodada_ativa = 2    │
│ 3. Constrói base_path: "Projetos/curso-nutricao/rodada-2/"       │
│ 4. Identifica pré-requisitos:                                    │
│    - avatar-blueprint.md (planejamento/)                         │
│    - canvas-produto.md (planejamento/)                           │
│    - canvas-webinar.md (planejamento/)                           │
│ 5. Valida: todos os pré-requisitos existem?                      │
└───────────────────────────────┬───────────────────────────────────┘
                                │
                    ┌───────────┴──────────┐
                   SIM                    NÃO
                    │                      │
                    ▼                      ▼
        ┌───────────────────┐   ┌────────────────────────┐
        │ Delegar para      │   │ ERRO:                  │
        │ @webinar-creator  │   │ "Falta avatar-blueprint│
        │                   │   │  para construir roteiro│
        │ Passa contexto:   │   │  Quer preencher agora?"│
        │ - base_path       │   └────────────────────────┘
        │ - projeto.yaml    │
        │ - pré-requisitos  │
        └─────────┬─────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────────┐
│              @webinar-creator (Spark)                           │
│                                                                 │
│ 1. Recebe base_path                                             │
│ 2. Lê pré-requisitos:                                           │
│    - {base_path}planejamento/avatar-blueprint.md                │
│    - {base_path}planejamento/canvas-produto.md                  │
│ 3. Executa comando solicitado (ex: *abertura)                   │
│ 4. Gera roteiro-abertura.md                                     │
│ 5. Salva em {base_path}conteudo/roteiro-abertura.md            │
│ 6. Atualiza projeto.yaml:                                       │
│    - fases.construcao.artefatos_completos += roteiro-abertura   │
│    - fases.construcao.artefatos_pendentes -= roteiro-abertura   │
│    - fases.construcao.ultima_atualizacao = timestamp            │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        RETORNO AO USUÁRIO                       │
│                                                                 │
│ ✅ Roteiro de Abertura gerado!                                  │
│                                                                 │
│ Salvo em:                                                       │
│ Projetos/curso-nutricao/rodada-2/conteudo/roteiro-abertura.md  │
│                                                                 │
│ Progresso: Construção 33% completa (3 de 9 artefatos)          │
│                                                                 │
│ Próximo: *empatia, *conteudo ou *pitch                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Fluxo de Herança entre Rodadas

```
┌──────────────────────────────────────────────────┐
│    PROJETO: Curso de Nutrição                    │
│    Rodada 1: CONCLUÍDA                           │
│    Faturamento: R$29.820                         │
└────────────────────┬─────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────┐
│    USUÁRIO: @webinar *nova-rodada                │
└────────────────────┬─────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────┐
│ MAESTRO PERGUNTA:                                │
│ "Quer copiar os canvases de planejamento        │
│  da Rodada 1? [Sim] [Não]"                       │
└────────────────────┬─────────────────────────────┘
                     │
         ┌───────────┴──────────┐
        SIM                    NÃO
         │                      │
         ▼                      ▼
┌────────────────────┐   ┌──────────────────┐
│ COPIAR ARTEFATOS   │   │ RODADA VAZIA     │
│                    │   │                  │
│ FOR EACH canvas:   │   │ Criar apenas     │
│   origem =         │   │ estrutura de     │
│    rodada-1/       │   │ pastas vazias    │
│     planejamento/  │   └──────────────────┘
│                    │
│   destino =        │
│    rodada-2/       │
│     planejamento/  │
│                    │
│   Adicionar        │
│   cabeçalho:       │
│   "Herdado da      │
│    Rodada 1"       │
└──────┬─────────────┘
       │
       ▼
┌──────────────────────────────────────────────────┐
│ RESULTADO:                                       │
│                                                  │
│ Projetos/curso-nutricao/rodada-2/planejamento/  │
│   ├── canvas-cliente-ideal.md ← HERDADO         │
│   ├── canvas-produto.md ← HERDADO               │
│   ├── canvas-webinar.md ← HERDADO               │
│   ├── avatar-blueprint.md ← HERDADO             │
│   └── orcamento-meta.md ← VAZIO (específico)    │
│                                                  │
│ MAESTRO:                                         │
│ "✅ Rodada 2 criada! Canvases herdados.          │
│  Digite *planejar para revisar."                 │
└──────────────────────────────────────────────────┘
```

### 5.1 Exemplo de Artefato Herdado

```markdown
# Canvas do Cliente Ideal

> ⚠️ **Herdado da Rodada 1** — Revisado em 05/03/2026
> Ajustes: Refinamento com dados reais de conversão (taxa 3.2%)

## 1. Quem é o público?

**Mulheres, 30-50 anos, classe B/C, casadas, com filhos,
trabalham fora, renda R$3.000-8.000/mês**

...

(resto do canvas copiado integralmente)
```

---

## 6. Estrutura do projeto.yaml

```yaml
# ============================================
# IDENTIFICAÇÃO
# ============================================
nome: "Lançamento Curso de Nutrição"
slug: "lancamento-curso-nutricao"
descricao: "Webinário para venda de curso online de emagrecimento"
criado_em: "2026-03-05"
atualizado_em: "2026-03-05"

# ============================================
# PRODUTO E NICHO
# ============================================
nicho: "Nutrição e Emagrecimento"
produto: "Curso Online: Emagreça com Saúde"
ticket: 497.00

# ============================================
# RODADAS (array de execuções)
# ============================================
rodadas:
  - numero: 1
    status: "Done"
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

rodada_ativa: 2

# ============================================
# PROGRESSO POR FASE (da rodada ativa)
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
  empilhamento: false
  perpetuo: false
  frontend_backend: false

# ============================================
# NOTAS E CONTEXTO
# ============================================
notas: |
  - Público: Mulheres 30-50 anos, classe B/C
  - Diferencial: Método sem dietas restritivas
  - Rodada 1 teve boa conversão (3.2%), mas comparecimento baixo (18%)
  - Rodada 2 vai focar em aumentar comparecimento via antecipação
```

---

## 7. Mapa de Responsabilidades dos Agentes

```
┌──────────────────────────────────────────────────────────────────┐
│                       @webinar (Maestro)                         │
│                                                                  │
│  Responsabilidades:                                              │
│  - Listar projetos                                               │
│  - Criar projeto                                                 │
│  - Selecionar projeto                                            │
│  - Criar rodada                                                  │
│  - Mostrar status (dashboard)                                    │
│  - Delegar para especialistas                                    │
│  - Gerenciar contexto de sessão                                  │
│                                                                  │
│  Artefatos gerenciados:                                          │
│  - projeto.yaml (estrutura)                                      │
│  - .aiox/webinar-context.yaml                                    │
└────────────┬─────────────────────────────────────────────────────┘
             │
     ┌───────┴────────┐
     │                │
     ▼                ▼
┌─────────────┐  ┌─────────────┐
│ PLANEJAR    │  │ CONSTRUIR   │
└──────┬──────┘  └──────┬──────┘
       │                │
       ▼                ▼
┌────────────────────────────────────┐  ┌────────────────────────────────────┐
│  @webinar-strategist (Sage)        │  │  @webinar-creator (Spark)          │
│                                    │  │                                    │
│  Fase: Planejamento                │  │  Fase: Construção                  │
│  Pasta: rodada-{N}/planejamento/   │  │  Pasta: rodada-{N}/conteudo/       │
│                                    │  │                                    │
│  Artefatos gerados:                │  │  Artefatos gerados:                │
│  - canvas-cliente-ideal.md         │  │  - roteiro-abertura.md             │
│  - canvas-produto.md               │  │  - roteiro-empatia.md              │
│  - canvas-webinar.md               │  │  - roteiro-conteudo.md             │
│  - avatar-blueprint.md             │  │  - roteiro-pitch.md                │
│  - orcamento-meta.md               │  │  - roteiro-completo.md             │
│  - planejamento-resumo.md          │  │  - mensagens-whatsapp.md           │
│                                    │  │  - copy-pagina-captura.md          │
│  Atualiza: projeto.yaml            │  │  - copy-pagina-replay.md           │
│    fases.planejamento              │  │  - copy-pagina-fechamento.md       │
└────────────────────────────────────┘  │                                    │
                                        │  Atualiza: projeto.yaml            │
                                        │    fases.construcao                │
                                        └────────────────────────────────────┘

     ┌───────────────┐  ┌───────────────┐
     │ EXECUTAR      │  │ ANALISAR      │
     └───────┬───────┘  └───────┬───────┘
             │                  │
             ▼                  ▼
┌────────────────────────────────────┐  ┌────────────────────────────────────┐
│  @webinar-operator (Atlas)         │  │  @webinar-analyst (Lens)           │
│                                    │  │                                    │
│  Fase: Execução                    │  │  Fase: Análise                     │
│  Pasta: rodada-{N}/execucao/       │  │  Pastas:                           │
│                                    │  │   - rodada-{N}/analise/            │
│  Artefatos gerados:                │  │   - estrategias/ (cross-rodada)    │
│  - guia-everwebinar.md             │  │                                    │
│  - guia-sendflow.md                │  │  Artefatos gerados:                │
│  - guia-pagamento.md               │  │  - relatorio-kpis.md               │
│  - guia-pixel.md                   │  │  - diagnostico-funil.md            │
│  - timeline-campanha.md            │  │  - orcado-vs-realizado.md          │
│  - funil-7-etapas.md               │  │  - plano-proxima-rodada.md         │
│  - checklist-lancamento.md         │  │  - estrategia-empilhamento.md      │
│                                    │  │  - estrategia-perpetuo.md          │
│  Atualiza: projeto.yaml            │  │                                    │
│    fases.execucao                  │  │  Atualiza: projeto.yaml            │
└────────────────────────────────────┘  │    fases.analise                   │
                                        │    rodadas[{N}].faturamento        │
                                        │    rodadas[{N}].leads              │
                                        │    rodadas[{N}].vendas             │
                                        │    rodadas[{N}].status → "Done"    │
                                        └────────────────────────────────────┘
```

---

## 8. Ciclo de Vida de Um Projeto

```
┌─────────────────────────────────────────────────────────────────┐
│                    CRIAÇÃO DO PROJETO                           │
│                  @webinar *novo-projeto                         │
│                                                                 │
│  Status: Projeto criado, Rodada 1 inicializada                 │
│  Fases: Todas "Pending"                                         │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FASE 1: PLANEJAMENTO                         │
│              @webinar *planejar → @webinar-strategist           │
│                                                                 │
│  Gera: 6 canvases                                               │
│  Status: fases.planejamento = "Completed"                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FASE 2: CONSTRUÇÃO                           │
│              @webinar *construir → @webinar-creator             │
│                                                                 │
│  Gera: Roteiro completo + mensagens + copy                      │
│  Status: fases.construcao = "Completed"                         │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FASE 3: EXECUÇÃO                             │
│              @webinar *executar → @webinar-operator             │
│                                                                 │
│  Gera: Guias de setup + timeline + checklist                    │
│  Status: fases.execucao = "Completed"                           │
│                                                                 │
│  [USUÁRIO EXECUTA O WEBINÁRIO NA VIDA REAL]                     │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FASE 4: ANÁLISE                              │
│              @webinar *analisar → @webinar-analyst              │
│                                                                 │
│  Gera: Relatório de KPIs + diagnóstico + plano próxima rodada  │
│  Status: fases.analise = "Completed"                            │
│  Atualiza: rodadas[1].status = "Done"                           │
│             rodadas[1].faturamento, leads, vendas               │
└────────────────────────┬────────────────────────────────────────┘
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
┌────────────────────┐          ┌────────────────────┐
│  RODADA 2          │          │  PROJETO ARQUIVADO │
│  *nova-rodada      │          │  (sem mais rodadas)│
│                    │          └────────────────────┘
│  Herdar canvases?  │
│  [Sim] [Não]       │
└──────────┬─────────┘
           │
           ▼
┌──────────────────────────────────────────┐
│  CICLO RECOMEÇA                          │
│  Rodada 2: Planejamento → ... → Análise  │
│                                          │
│  Rodada 3...                             │
│  Rodada N...                             │
└──────────────────────────────────────────┘
```

---

## 9. Dashboard de Status (*status)

```
══════════════════════════════════════════════════════════════════
                        PROJETO ATIVO
══════════════════════════════════════════════════════════════════

📁 Lançamento Curso de Nutrição
   Rodada: 2 de 2
   Produto: Curso Online: Emagreça com Saúde
   Ticket: R$ 497,00

──────────────────────────────────────────────────────────────────

🟢 PLANEJAMENTO — 100% completo (6 de 6)

   ✅ canvas-cliente-ideal.md
   ✅ canvas-produto.md
   ✅ canvas-webinar.md
   ✅ avatar-blueprint.md
   ✅ orcamento-meta.md
   ✅ planejamento-resumo.md

   Última atualização: 02/03/2026

──────────────────────────────────────────────────────────────────

🟡 CONSTRUÇÃO — 45% completo (4 de 9)

   ✅ roteiro-abertura.md
   ✅ roteiro-empatia.md
   ✅ roteiro-conteudo.md
   ✅ roteiro-pitch.md
   ⏸️ roteiro-completo.md
   ⏸️ mensagens-whatsapp.md
   ⏸️ copy-pagina-captura.md
   ⏸️ copy-pagina-replay.md
   ⏸️ copy-pagina-fechamento.md

   Última atualização: 05/03/2026

──────────────────────────────────────────────────────────────────

⚪ EXECUÇÃO — Aguardando (0 de 7)

   ⏸️ guia-everwebinar.md
   ⏸️ guia-sendflow.md
   ⏸️ guia-pagamento.md
   ⏸️ guia-pixel.md
   ⏸️ timeline-campanha.md
   ⏸️ funil-7-etapas.md
   ⏸️ checklist-lancamento.md

──────────────────────────────────────────────────────────────────

⚪ ANÁLISE — Aguardando (0 de 4)

   ⏸️ relatorio-kpis.md
   ⏸️ diagnostico-funil.md
   ⏸️ orcado-vs-realizado.md
   ⏸️ plano-proxima-rodada.md

──────────────────────────────────────────────────────────────────

📊 HISTÓRICO DE RODADAS

   Rodada 1:
   ✅ Concluída em 15/01/2026
   💰 Faturamento: R$ 29.820,00
   📧 Leads: 1.850
   🛒 Vendas: 60 (conversão 3,2%)

   Rodada 2:
   🔄 Em andamento (Construção 45%)

══════════════════════════════════════════════════════════════════

PRÓXIMA AÇÃO SUGERIDA:
Digite *construir para consolidar o roteiro completo.

══════════════════════════════════════════════════════════════════
```

---

*@architect (Aria) — Diagramas da Arquitetura — 2026-03-05*
