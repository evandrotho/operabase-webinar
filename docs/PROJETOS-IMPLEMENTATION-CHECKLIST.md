# Checklist de Implementação — Sistema de Projetos

> **Para:** @dev, @squad-creator, @qa
> **Documento:** Plano de implementação técnico
> **Data:** 2026-03-05

---

## Visão Geral

Este checklist detalha **todas as mudanças técnicas** necessárias para implementar o sistema de gestão de projetos de webinários.

**Referência completa:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-ARCHITECTURE.md`

---

## Fase 1: Templates e Estruturas (Responsável: @architect)

### 1.1 Criar Templates

- [ ] **projeto-manifest-tmpl.yaml** — Template do arquivo `projeto.yaml`
  - Campos: nome, slug, descricao, nicho, produto, ticket
  - Seções: rodadas (array), rodada_ativa, fases (progresso), estrategias, notas
  - Localização: `.aiox-core/development/templates/webinar/`

- [ ] **webinar-context-tmpl.yaml** — Template do contexto de sessão
  - Campos: projeto_ativo, rodada_ativa, ativado_em, ultima_interacao
  - Localização: `.aiox-core/development/templates/webinar/`

- [ ] **README-projeto-tmpl.md** — README opcional para cada projeto (explicativo)
  - Localização: `.aiox-core/development/templates/webinar/`

### 1.2 Definir Schemas de Validação

- [ ] **projeto.schema.yaml** — Validação do manifest (opcional, para @qa)
  - Tipos de dados, campos obrigatórios, valores permitidos (status, fases)

### 1.3 Documentar Convenções de Nomenclatura

- [ ] **naming-conventions.md**
  - Slugs de projetos: lowercase, hífens, sem espaços (ex: `curso-nutricao`)
  - Pastas de rodadas: `rodada-{N}` (N = 1, 2, 3...)
  - Fases: `planejamento`, `conteudo`, `execucao`, `analise`, `estrategias`

---

## Fase 2: Atualização do Maestro (@webinar) (Responsável: @squad-creator + @dev)

### 2.1 Atualizar Definição do Agente

Arquivo: `agents/webinar/AGENT.md` (ou similar)

- [ ] Adicionar novos comandos:
  - `*projetos` — Listar todos os projetos
  - `*novo-projeto` — Criar novo projeto (interativo)
  - `*rodadas` — Listar rodadas do projeto ativo
  - `*nova-rodada` — Criar nova rodada no projeto ativo
  - `*mudar-projeto` — Trocar projeto ativo
  - `*migrar` — Migrar estrutura antiga para nova (se detectar `docs/webinar/`)

- [ ] Atualizar descrição do comando `*status`:
  - Agora mostra progresso do projeto ativo (todas as fases + artefatos completos/pendentes)

- [ ] Adicionar dependencies:
  - Leitura de `projeto.yaml`
  - Leitura/escrita de `.aiox/webinar-context.yaml`
  - Listagem de pastas em `Projetos/`

### 2.2 Criar Tasks do Maestro

Localização: `.aiox-core/development/tasks/webinar/`

- [ ] **listar-projetos.md**
  - Input: Nenhum
  - Output: Lista formatada de projetos com status
  - Lógica: Ler `Projetos/`, parsear cada `projeto.yaml`, mostrar nome + progresso

- [ ] **criar-projeto.md**
  - Input: Perguntas interativas (nome, nicho, produto, ticket)
  - Output: Nova pasta em `Projetos/{slug}/`, `projeto.yaml`, subpastas de rodada-1
  - Validação: Slug único (não sobrescrever projeto existente)
  - Pós-ação: Atualizar `.aiox/webinar-context.yaml` com projeto novo

- [ ] **selecionar-projeto.md**
  - Input: Índice ou slug do projeto
  - Output: Atualizar `.aiox/webinar-context.yaml`
  - Validação: Projeto existe

- [ ] **listar-rodadas.md**
  - Input: Projeto ativo
  - Output: Histórico de rodadas (data, status, faturamento, leads, vendas)

- [ ] **criar-rodada.md**
  - Input: Número da rodada (auto-incremento), herdar canvases? (sim/não)
  - Output: Nova pasta `rodada-{N}/` com subpastas vazias
  - Condicional: Se herdar=sim, copiar `rodada-{N-1}/planejamento/*.md` → `rodada-{N}/planejamento/*.md` e marcar com cabeçalho "Herdado"
  - Atualizar `projeto.yaml`: adicionar rodada no array, definir como `rodada_ativa`

- [ ] **migrar-projeto.md**
  - Input: Path antigo (`docs/webinar/rodada-1/`), nome do projeto
  - Output: Mover estrutura para `Projetos/{slug}/rodada-1/`, criar `projeto.yaml`
  - Validação: Detectar artefatos antigos antes de executar

- [ ] **status-projeto.md**
  - Input: Projeto ativo
  - Output: Dashboard formatado (4 fases, progresso %, artefatos completos/pendentes)
  - Lógica: Ler `projeto.yaml` seção `fases`

---

## Fase 3: Atualização dos Agentes Especializados (Responsável: @dev)

### 3.1 @webinar-strategist (Planejamento)

Arquivo: `agents/webinar-strategist/AGENT.md`

- [ ] Atualizar lógica de paths:
  - Receber `base_path` do Maestro (ex: `Projetos/{slug}/rodada-{N}/`)
  - Salvar artefatos em `{base_path}planejamento/`

- [ ] Atualizar tasks de geração de canvases:
  - `canvas-cliente-ideal.md` → path dinâmico
  - `canvas-produto.md` → path dinâmico
  - `canvas-webinar.md` → path dinâmico
  - `avatar-blueprint.md` → path dinâmico
  - `orcamento-meta.md` → path dinâmico
  - `planejamento-resumo.md` → path dinâmico

- [ ] Adicionar pós-ação em cada task:
  - Após salvar artefato, atualizar `projeto.yaml`:
    - `fases.planejamento.artefatos_completos` (append)
    - `fases.planejamento.artefatos_pendentes` (remove)
    - `fases.planejamento.ultima_atualizacao` (timestamp)

### 3.2 @webinar-creator (Construção)

Arquivo: `agents/webinar-creator/AGENT.md`

- [ ] Atualizar lógica de paths:
  - Receber `base_path` do Maestro
  - Salvar artefatos em `{base_path}conteudo/`

- [ ] Atualizar lógica de cross-reference:
  - Buscar canvases em `{base_path}planejamento/` (não em path fixo)

- [ ] Atualizar tasks de geração de conteúdo:
  - `roteiro-abertura.md` → path dinâmico
  - `roteiro-empatia.md` → path dinâmico
  - `roteiro-conteudo.md` → path dinâmico
  - `roteiro-pitch.md` → path dinâmico
  - `roteiro-completo.md` → path dinâmico
  - `mensagens-whatsapp.md` → path dinâmico
  - `copy-pagina-captura.md` → path dinâmico
  - `copy-pagina-replay.md` → path dinâmico
  - `copy-pagina-fechamento.md` → path dinâmico

- [ ] Adicionar pós-ação em cada task:
  - Atualizar `projeto.yaml` seção `fases.construcao`

### 3.3 @webinar-operator (Execução)

Arquivo: `agents/webinar-operator/AGENT.md`

- [ ] Atualizar lógica de paths:
  - Receber `base_path` do Maestro
  - Salvar artefatos em `{base_path}execucao/`

- [ ] Atualizar lógica de cross-reference:
  - Buscar roteiro em `{base_path}conteudo/`
  - Buscar mensagens em `{base_path}conteudo/`
  - Buscar orçamento em `{base_path}planejamento/`

- [ ] Atualizar tasks de geração de guias:
  - `guia-everwebinar.md` → path dinâmico
  - `guia-sendflow.md` → path dinâmico
  - `guia-pagamento.md` → path dinâmico
  - `guia-pixel.md` → path dinâmico
  - `timeline-campanha.md` → path dinâmico
  - `funil-7-etapas.md` → path dinâmico
  - `checklist-lancamento.md` → path dinâmico

- [ ] Adicionar pós-ação em cada task:
  - Atualizar `projeto.yaml` seção `fases.execucao`

### 3.4 @webinar-analyst (Análise)

Arquivo: `agents/webinar-analyst/AGENT.md`

- [ ] Atualizar lógica de paths:
  - Receber `base_path` do Maestro
  - Salvar artefatos em `{base_path}analise/`
  - Salvar estratégias em `{base_path}../estrategias/` (sobe um nível, fora da rodada)

- [ ] Atualizar lógica de cross-reference:
  - Buscar orçamento em `{base_path}planejamento/`
  - Buscar roteiro em `{base_path}conteudo/`
  - Buscar timeline em `{base_path}execucao/`
  - Buscar funil em `{base_path}execucao/`

- [ ] Atualizar tasks de análise:
  - `relatorio-kpis.md` → path dinâmico
  - `diagnostico-funil.md` → path dinâmico
  - `orcado-vs-realizado.md` → path dinâmico
  - `plano-proxima-rodada.md` → path dinâmico

- [ ] Atualizar tasks de estratégias avançadas:
  - `estrategia-empilhamento.md` → salvar em `estrategias/` (não em `analise/`)
  - `estrategia-perpetuo.md` → salvar em `estrategias/`
  - `estrategia-frontend-backend.md` → salvar em `estrategias/`

- [ ] Adicionar pós-ação em cada task:
  - Atualizar `projeto.yaml` seção `fases.analise`
  - Ao gerar `relatorio-kpis.md`, atualizar `projeto.yaml`:
    - `rodadas[{N}].faturamento` (valor real)
    - `rodadas[{N}].leads` (valor real)
    - `rodadas[{N}].vendas` (valor real)
    - `rodadas[{N}].status` → "Done"

### 3.5 Lógica Compartilhada: Atualização de `projeto.yaml`

Criar função utilitária (pode ser task auxiliar ou função compartilhada):

- [ ] **atualizar-projeto-manifest.md** (ou helper function)
  - Input: projeto_path, fase, artefato, acao (add_completo | remove_pendente | update_rodada)
  - Output: `projeto.yaml` atualizado
  - Lógica:
    - Parsear YAML
    - Modificar seção relevante
    - Escrever de volta
    - Adicionar timestamp em `ultima_atualizacao`

---

## Fase 4: Testes e Validação (Responsável: @qa)

### 4.1 Testes de Fluxo Completo

- [ ] **Teste 1: Criar projeto do zero**
  1. `@webinar *novo-projeto` → preencher interativamente
  2. Verificar: pasta criada, `projeto.yaml` correto, rodada-1 inicializada
  3. `*planejar` → gerar canvas-cliente-ideal
  4. Verificar: artefato salvo no path correto, `projeto.yaml` atualizado

- [ ] **Teste 2: Múltiplos projetos**
  1. Criar projeto A
  2. Criar projeto B
  3. `@webinar` → verificar listagem de 2 projetos
  4. Trabalhar no projeto A → gerar artefato
  5. `*mudar-projeto` → projeto B
  6. Gerar artefato no projeto B
  7. Verificar: artefatos isolados, não misturados

- [ ] **Teste 3: Rodada 2 com herança**
  1. Projeto A → rodada-1 completa (6 canvases)
  2. `*nova-rodada` → herdar=sim
  3. Verificar: canvases copiados para rodada-2 com cabeçalho "Herdado"
  4. Editar canvas herdado → verificar que edição não afeta rodada-1

- [ ] **Teste 4: Cross-reference entre artefatos**
  1. Gerar `avatar-blueprint.md` (Planejamento)
  2. `*construir` → `*abertura` (Creator puxa dados do avatar)
  3. Verificar: roteiro-abertura contém dados corretos do avatar

- [ ] **Teste 5: Progresso e status**
  1. Projeto com planejamento 100%, construção 50%, execução 0%, análise 0%
  2. `*status` → verificar dashboard correto
  3. Completar um artefato de construção
  4. `*status` → verificar % atualizado

- [ ] **Teste 6: Migração de estrutura antiga**
  1. Criar pasta `docs/webinar/rodada-1/planejamento/` com artefatos falsos
  2. `@webinar` → detectar estrutura antiga
  3. `*migrar` → fornecer nome do projeto
  4. Verificar: artefatos movidos para `Projetos/{slug}/rodada-1/`, `projeto.yaml` criado

- [ ] **Teste 7: Persistência de contexto**
  1. Ativar projeto A → gerar artefato
  2. Fechar Claude Code (simulado: apagar `.aiox/webinar-context.yaml` e recriar com timestamp antigo)
  3. Reabrir `@webinar` → verificar: Maestro pergunta se quer continuar projeto A

### 4.2 Testes de Validação

- [ ] **Validação 1: Slugs únicos**
  - Criar projeto "Curso A"
  - Tentar criar outro projeto "Curso A"
  - Verificar: erro ou sugestão de slug diferente

- [ ] **Validação 2: Pré-requisitos**
  - Projeto sem avatar-blueprint
  - Tentar `*construir` → `*abertura`
  - Verificar: erro informando falta de pré-requisito

- [ ] **Validação 3: Rodada inexistente**
  - Tentar acessar rodada-5 quando só existem 2 rodadas
  - Verificar: erro claro

- [ ] **Validação 4: YAML malformado**
  - Corromper `projeto.yaml` manualmente
  - Tentar `*status`
  - Verificar: erro graceful, não crash

### 4.3 Testes de Regressão

- [ ] **Verificar que comandos antigos ainda funcionam:**
  - `*planejar`, `*construir`, `*executar`, `*analisar`, `*guia`, `*help`
  - Todos devem funcionar exatamente como antes (com projeto ativo selecionado)

---

## Fase 5: Documentação (Responsável: @architect + @dev)

- [ ] **Atualizar PRD** (`docs/prd.md`)
  - Seção 2.2: Incluir fluxo de seleção de projeto
  - Seção 3.1: Atualizar comandos do Maestro
  - Seção 5.5: Atualizar estrutura de armazenamento

- [ ] **Criar guia do usuário** (`docs/GUIA-PROJETOS.md`)
  - Como criar projeto
  - Como trocar de projeto
  - Como fazer rodada 2
  - Como migrar estrutura antiga

- [ ] **Atualizar CLAUDE.md** (se necessário)
  - Referências aos novos comandos do Maestro

- [ ] **Criar CHANGELOG** (`docs/CHANGELOG-PROJETOS.md`)
  - Data: 2026-03-05
  - Breaking changes (estrutura de pastas)
  - Novos comandos
  - Migração necessária

---

## Fase 6: Deploy e Rollout (Responsável: @devops + @pm)

### 6.1 Pré-Deploy

- [ ] Todos os testes passando
- [ ] Documentação completa
- [ ] Templates criados e versionados

### 6.2 Rollout Gradual

- [ ] **Fase A: Owner testa com 1 projeto novo**
  - Criar projeto do zero
  - Gerar todos os artefatos
  - Fazer rodada 2
  - Feedback: usabilidade, clareza, bugs

- [ ] **Fase B: Migrar projetos existentes (se houver)**
  - Usar comando `*migrar`
  - Verificar integridade dos artefatos
  - Comparar outputs antes/depois

- [ ] **Fase C: Uso normal com múltiplos projetos**
  - Owner cria 3+ projetos reais
  - Usa por 1-2 semanas
  - Coleta feedback final

### 6.3 Pós-Deploy

- [ ] Resolver bugs críticos encontrados
- [ ] Ajustar UX/wording baseado em feedback
- [ ] Atualizar documentação com FAQs

---

## Estimativa de Esforço

| Fase | Tarefas | Estimativa |
|------|---------|------------|
| 1. Templates | 3 templates + schemas | 2-3 horas |
| 2. Maestro | 6 tasks + atualização de agent definition | 8-10 horas |
| 3. Agentes especializados | 4 agentes × ~4 tasks cada + lógica compartilhada | 16-20 horas |
| 4. Testes | 7 testes de fluxo + 4 validações + regressão | 6-8 horas |
| 5. Documentação | PRD, guias, changelog | 3-4 horas |
| 6. Deploy | Rollout gradual + ajustes | 4-6 horas |
| **TOTAL** | — | **39-51 horas** |

**Distribuição:**
- @architect: 2-3h (Fase 1)
- @squad-creator: 2-3h (Fase 2, agent definitions)
- @dev: 24-30h (Fases 2-3)
- @qa: 6-8h (Fase 4)
- @architect + @dev: 3-4h (Fase 5)
- @devops + @pm: 4-6h (Fase 6)

---

## Dependências e Ordem de Execução

```
Fase 1 (Templates)
    ↓
Fase 2 (Maestro) ← Dependência: templates prontos
    ↓
Fase 3 (Agentes) ← Dependência: Maestro atualizado (passa base_path)
    ↓
Fase 4 (Testes) ← Dependência: tudo implementado
    ↓
Fase 5 (Docs) ← Dependência: testes passando
    ↓
Fase 6 (Deploy) ← Dependência: tudo validado
```

**Bloqueadores:**
- Fase 3 não pode começar sem Fase 2 (agentes precisam do base_path do Maestro)
- Fase 4 precisa de Fases 2+3 completas
- Fase 6 precisa de Fase 4 validada

---

## Riscos e Mitigações

| Risco | Impacto | Probabilidade | Mitigação |
|-------|---------|---------------|-----------|
| Breaking change (estrutura antiga inválida) | Alto | Certo | Comando `*migrar` obrigatório, documentado |
| Complexidade de paths dinâmicos | Médio | Médio | Função utilitária compartilhada, testes robustos |
| YAML parsing frágil | Baixo | Baixo | Validação de schema, error handling graceful |
| Confusão de usuário (muitos comandos) | Médio | Baixo | Resumo executivo claro, `*help` atualizado |
| Herança de artefatos com conflitos | Baixo | Baixo | Cabeçalho "Herdado" visível, usuário edita explicitamente |

---

## Critérios de Aceitação

### MVP (Mínimo Viável)

- [ ] Criar projeto novo funciona
- [ ] Listar projetos funciona
- [ ] Selecionar projeto funciona
- [ ] Gerar artefatos em projeto ativo funciona
- [ ] Trocar de projeto funciona
- [ ] `projeto.yaml` atualiza corretamente
- [ ] Rodada 2 funciona sem herança

### Funcionalidade Completa

- [ ] Todos os itens do MVP
- [ ] Herança de artefatos entre rodadas funciona
- [ ] Migração de estrutura antiga funciona
- [ ] Estratégias avançadas salvam em pasta correta
- [ ] Dashboard de status preciso
- [ ] Persistência de contexto entre sessões
- [ ] Todos os 7 testes de fluxo passam
- [ ] Documentação completa (PRD, guia, resumo executivo)

---

## Notas para @dev

### Convenções de Código

- **Paths:** Sempre usar paths absolutos. Construir com `path.join(base_path, fase, artefato)`
- **YAML:** Usar biblioteca `js-yaml` (se Node.js) ou `pyyaml` (se Python)
- **Timestamps:** ISO 8601 (`2026-03-05T15:30:00`)
- **Slugs:** Lowercase, hífens, sem acentos/caracteres especiais (`slugify` function)

### Funções Utilitárias Sugeridas

```javascript
// Exemplo conceitual (não código final)

function getProjeto(slug) {
  const yamlPath = `Projetos/${slug}/projeto.yaml`;
  return parseYAML(readFile(yamlPath));
}

function updateProjetoManifest(slug, updates) {
  const projeto = getProjeto(slug);
  merge(projeto, updates);
  writeYAML(`Projetos/${slug}/projeto.yaml`, projeto);
}

function getBasePath(slug, rodada) {
  return `Projetos/${slug}/rodada-${rodada}/`;
}

function getProjetoAtivo() {
  const context = parseYAML(readFile('.aiox/webinar-context.yaml'));
  return context.projeto_ativo;
}

function listarProjetos() {
  const slugs = listDirs('Projetos/');
  return slugs.map(slug => getProjeto(slug));
}
```

---

## Contato e Dúvidas

**Documentos de referência:**
- **Arquitetura completa:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-ARCHITECTURE.md`
- **Resumo para owner:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/PROJETOS-RESUMO-EXECUTIVO.md`
- **PRD original:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/docs/prd.md`

**Responsável pela arquitetura:** @architect (Aria)

**Para questões técnicas de implementação:** @dev (Dex)

**Para validação de usabilidade:** Owner (via @pm)

---

**Checklist completo. Pronto para implementação.**

*@architect (Aria) — Checklist de Implementação — 2026-03-05*
