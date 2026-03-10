# Índice — Sistema de Gestão de Projetos de Webinários

> **Data:** 2026-03-05
> **Autor:** @architect (Aria)
> **Status:** Proposta completa pronta para implementação

---

## Visão Geral

Este conjunto de documentos especifica um **sistema de gestão de projetos** para organizar múltiplos webinários, cada um com múltiplas rodadas (lançamentos), substituindo a estrutura única `docs/webinar/rodada-{N}/` por uma arquitetura escalável `Projetos/{nome-projeto}/rodada-{N}/`.

---

## Documentos

### 1. Arquitetura Completa
**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-ARCHITECTURE.md`

**Para:** Equipe técnica (arquitetos, devs)

**Conteúdo:**
- Nova estrutura de pastas detalhada
- Manifest do projeto (`projeto.yaml`) — schema completo
- Fluxo do Maestro (@webinar) para seleção de projetos
- Delegação de contexto para agentes especializados
- Herança de artefatos entre rodadas
- Criação e migração de projetos
- Atualização automática de progresso
- Impacto em arquivos e agentes
- Plano de migração técnica

**Use para:** Entender a decisão arquitetural completa.

---

### 2. Resumo Executivo
**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-RESUMO-EXECUTIVO.md`

**Para:** Owner (não-técnico), Product Managers

**Conteúdo:**
- O que muda e por quê
- Como funciona na prática (exemplos de conversa)
- O que o usuário ganha
- Comandos novos do Maestro
- Exemplo real de uso com múltiplos projetos
- Estrutura de uma pasta de projeto (simplificada)
- O que o `projeto.yaml` guarda
- FAQs

**Use para:** Entender o impacto no usuário final e valor entregue.

---

### 3. Checklist de Implementação
**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-IMPLEMENTATION-CHECKLIST.md`

**Para:** @dev, @squad-creator, @qa

**Conteúdo:**
- 6 fases de implementação detalhadas
- Templates a criar (projeto.yaml, webinar-context.yaml)
- Atualização do Maestro (6 tasks novas)
- Atualização dos 4 agentes especializados (paths dinâmicos)
- Testes completos (fluxo, validação, regressão)
- Documentação a atualizar
- Rollout gradual
- Estimativa de esforço: 39-51 horas
- Dependências e ordem de execução
- Riscos e mitigações
- Critérios de aceitação

**Use para:** Implementar o sistema passo-a-passo.

---

### 4. Diagramas Visuais
**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-DIAGRAMS.md`

**Para:** Todos (visual)

**Conteúdo:**
- Estrutura de pastas (visão geral e detalhada)
- Fluxo de seleção de projeto (diagrama ASCII)
- Fluxo de criação de projeto (passo-a-passo)
- Fluxo de delegação para agentes (Maestro → especialistas)
- Fluxo de herança entre rodadas
- Schema completo do `projeto.yaml`
- Mapa de responsabilidades dos agentes
- Ciclo de vida de um projeto (criação → execução → rodada 2)
- Dashboard de status (exemplo formatado)

**Use para:** Visualizar a arquitetura rapidamente.

---

### 5. Guia Rápido de Referência
**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-QUICK-REFERENCE.md`

**Para:** Usuários finais

**Conteúdo:**
- Conceitos básicos (projeto, rodada, fase, artefato)
- Todos os comandos do Maestro (tabela)
- Fluxos típicos de trabalho (3 cenários)
- FAQs (10 perguntas comuns)
- Estrutura visual de uma pasta
- Legenda de símbolos
- Atalhos e dicas práticas
- Comandos por situação
- Exemplo real de conversa
- Resumo em 3 frases

**Use para:** Referência rápida durante o uso.

---

## Mapa de Leitura Recomendado

### Para Owner (Não-Técnico)
1. **Comece aqui:** Resumo Executivo
2. **Depois:** Guia Rápido de Referência
3. **Se quiser visualizar:** Diagramas Visuais

### Para Product Manager (@pm)
1. **Comece aqui:** Resumo Executivo
2. **Depois:** Arquitetura Completa (seções 1-7)
3. **Para validar:** Diagramas Visuais (fluxos de usuário)

### Para Arquiteto (@architect)
1. **Comece aqui:** Arquitetura Completa
2. **Depois:** Diagramas Visuais (estrutura técnica)
3. **Para implementar:** Checklist de Implementação (Fase 1)

### Para Desenvolvedor (@dev)
1. **Comece aqui:** Checklist de Implementação
2. **Referência:** Arquitetura Completa (seções 5-8)
3. **Visualizar:** Diagramas Visuais (fluxos de delegação, projeto.yaml)

### Para QA (@qa)
1. **Comece aqui:** Checklist de Implementação (Fase 4 — Testes)
2. **Entender:** Resumo Executivo (comportamento esperado)
3. **Validar:** Diagramas Visuais (fluxos completos)

### Para DevOps (@devops)
1. **Comece aqui:** Checklist de Implementação (Fase 6 — Deploy)
2. **Entender impacto:** Arquitetura Completa (seção 8)

---

## Resumo da Solução

### Problema
Sistema atual organiza webinários em `docs/webinar/rodada-{N}/`, sem separação de projetos. Não escala quando o usuário tem múltiplos webinários diferentes (ex: "Curso de Nutrição" + "Workshop de Copywriting").

### Solução
Nova estrutura `Projetos/{nome-projeto}/rodada-{N}/` com:
- **Isolamento:** Cada webinário = pasta própria
- **Múltiplas rodadas:** Cada projeto suporta N lançamentos
- **Manifest:** `projeto.yaml` registra metadados, progresso e histórico
- **Contexto de sessão:** `.aiox/webinar-context.yaml` mantém projeto ativo
- **Herança:** Rodada 2+ pode copiar canvases da rodada anterior
- **Maestro inteligente:** Lista projetos, permite selecionar/criar/trocar

### Benefícios
1. Usuário pode ter 5, 10, 20 projetos sem confusão
2. Histórico claro: `projeto.yaml` mostra faturamento/leads/vendas de cada rodada
3. Reutilização: Canvases herdados entre rodadas (não refaz tudo do zero)
4. Contexto persistente: Sistema lembra qual projeto estava trabalhando
5. Output organizado: Tudo do projeto em um lugar (fácil arquivar/compartilhar)

---

## Estrutura Visual (Resumida)

```
Projetos/
├── curso-nutricao/
│   ├── projeto.yaml
│   ├── rodada-1/
│   │   ├── planejamento/
│   │   ├── conteudo/
│   │   ├── execucao/
│   │   └── analise/
│   ├── rodada-2/
│   └── estrategias/
├── workshop-copywriting/
│   └── ...
└── infoproduto-financas/
    └── ...
```

---

## Novos Comandos do Maestro

| Comando | O Que Faz |
|---------|-----------|
| `*projetos` | Lista todos os projetos |
| `*novo-projeto` | Cria novo webinário |
| `*mudar-projeto` | Troca projeto ativo |
| `*rodadas` | Histórico de rodadas |
| `*nova-rodada` | Cria rodada 2, 3... |
| `*status` | Dashboard de progresso |
| `*migrar` | Migra estrutura antiga |

**Comandos antigos continuam funcionando:**
- `*planejar`, `*construir`, `*executar`, `*analisar`, `*guia`, `*help`

---

## Próximos Passos

### 1. Validação
- [ ] Owner valida conceito (Resumo Executivo)
- [ ] @pm valida impacto no produto (Arquitetura seções 1-4)
- [ ] @architect valida decisões técnicas (Arquitetura completa)

### 2. Implementação
- [ ] @architect cria templates (projeto.yaml, context.yaml)
- [ ] @squad-creator atualiza definição do Maestro
- [ ] @dev implementa tasks e atualiza agentes especializados
- [ ] @qa testa fluxos completos
- [ ] @devops faz rollout gradual

### 3. Documentação
- [ ] Atualizar PRD (`docs/prd.md`)
- [ ] Criar CHANGELOG
- [ ] Atualizar CLAUDE.md (se necessário)

---

## Estimativa

**Esforço total:** 39-51 horas

**Distribuição:**
- @architect: 2-3h (templates)
- @squad-creator: 2-3h (agent definitions)
- @dev: 24-30h (tasks + agentes)
- @qa: 6-8h (testes)
- Docs + Deploy: 7-10h

**Timeline sugerido:** 1-2 semanas (com 1-2 devs full-time)

---

## Riscos

| Risco | Mitigação |
|-------|-----------|
| Breaking change (estrutura antiga) | Comando `*migrar` obrigatório |
| Complexidade de paths dinâmicos | Função utilitária compartilhada |
| Confusão de usuário | Resumo executivo + `*help` atualizado |

---

## Critérios de Sucesso

### MVP
- ✅ Criar projeto novo
- ✅ Listar e selecionar projetos
- ✅ Gerar artefatos em projeto ativo
- ✅ Trocar de projeto
- ✅ `projeto.yaml` atualiza corretamente

### Completo
- ✅ Herança de artefatos entre rodadas
- ✅ Migração de estrutura antiga
- ✅ Dashboard de status preciso
- ✅ Persistência de contexto
- ✅ Todos os testes passam

---

## Contato

**Responsável pela arquitetura:** @architect (Aria)

**Dúvidas técnicas:** Consultar Arquitetura Completa ou Checklist de Implementação

**Dúvidas de produto:** Consultar Resumo Executivo ou Guia Rápido

---

## Referências Cruzadas

| Documento | Seção | Referência |
|-----------|-------|------------|
| PRD original | Seção 5.5 | Estrutura de armazenamento atual |
| PRD original | Seção 3.1 | Comandos do Maestro (a atualizar) |
| Arquitetura | Seção 8 | Impacto em arquivos existentes |
| Checklist | Fase 5 | Documentação a atualizar |

---

## Changelog

| Data | Versão | Descrição |
|------|--------|-----------|
| 2026-03-05 | 1.0 | Proposta inicial completa — 5 documentos criados |

---

**Sistema de Gestão de Projetos — Proposta completa**

*@architect (Aria) — 2026-03-05*

**Arquivos criados:**
1. `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-ARCHITECTURE.md`
2. `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-RESUMO-EXECUTIVO.md`
3. `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-IMPLEMENTATION-CHECKLIST.md`
4. `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-DIAGRAMS.md`
5. `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-QUICK-REFERENCE.md`
6. `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-INDEX.md` (este arquivo)

**Pronto para validação e implementação.**
