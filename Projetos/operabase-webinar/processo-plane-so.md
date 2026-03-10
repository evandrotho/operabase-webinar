# Processo de Organizacao no Plane.so — Operabase Webinar

> **Versao:** 1.0
> **Criado em:** 2026-03-06
> **Agente:** @plane-master (Orion)
> **Projeto Plane.so:** [OPERA] Operabase AI
> **Project ID:** `e191f747-0b7a-4163-af52-df237123d35c`
> **Workspace:** `operabaseai`

---

## 1. Visao Geral

Este documento define o **processo padronizado** para organizar e manter o projeto de webinario no Plane.so. Serve como referencia para:

- Reorganizacoes futuras
- Novas rodadas do webinario
- Onboarding de qualquer pessoa que precise operar o Plane.so

---

## 2. Estrutura do Projeto

### 2.1 Modulos (Fases)

O projeto e organizado em **5 modulos**, cada um representando uma fase do funil:

| Modulo | Agente Responsavel | Status Esperado |
|--------|-------------------|-----------------|
| Planejamento (Sage) | @webinar-strategist | Concluido antes de tudo |
| Construcao de Conteudo (Spark) | @webinar-creator | Concluido antes da execucao |
| Execucao da Campanha (Atlas) | @webinar-operator | Ativo durante a campanha |
| Checklist Pre-Lancamento | Operador | Ativo antes de D-0 |
| Analise Pos-Webinario (Lens) | @webinar-analyst | Ativo apos D+5 |

### 2.2 Labels

| Label | Uso |
|-------|-----|
| `planejamento` | Itens de planejamento estrategico |
| `construcao` | Itens de criacao de conteudo |
| `execucao` | Itens de execucao da campanha |
| `analise` | Itens de analise pos-webinario |
| `artefato` | Item que gera um documento/arquivo |
| `milestone` | Marco importante (data critica) |
| `setup_guide` | Guia passo-a-passo de configuracao |
| `checklist` | Item de verificacao pre-lancamento |
| `estrategia` | Planejamento estrategico de longo prazo |

### 2.3 Estados do Workflow

| Estado | Grupo | Quando Usar |
|--------|-------|-------------|
| Backlog | backlog | Itens futuros ou de proximas rodadas |
| Todo | unstarted | Itens planejados para esta rodada |
| In Progress | started | Item sendo executado agora |
| Done | completed | Item concluido e verificado |

### 2.4 IDs de Referencia

```
# Estados
backlog:     35f8c95e-030e-40a6-9a78-c3851f60e747
todo:        8ec37452-466d-4080-ad3c-c06379b1e32b
in_progress: cb194a70-d267-40c2-85f8-89025d2b829b
done:        3903dd89-ba34-401e-b252-4384fdebd4cc

# Modulos
planejamento: 1f8fc2d1-7155-4589-a27c-b3b24509eff5
construcao:   d28b0c39-5477-489d-8243-b6da6152d894
execucao:     4ed7600d-cda2-448a-a785-6187277456f8
analise:      4c46aa43-349e-4c3d-9ac1-890e05297b3d
checklist:    547515c3-d4ce-4cc8-bd6a-222101c86559
```

---

## 3. Padroes de Organizacao

### 3.1 Regra de Datas

**OBRIGATORIO:** Todo work item deve ter **start_date** E **target_date**.

| Tipo de Item | start_date | target_date |
|-------------|-----------|-------------|
| Artefato (conteudo/planejamento) | Dia que comecou a ser feito | Dia que foi concluido |
| Tarefa de execucao | Dia que deve comecar | Dia que deve estar pronto |
| Marco (MARCO:) | Dia do evento | Dia do evento |
| Checklist | Inicio da fase de verificacao | Deadline da verificacao |
| Analise | Dia apos o fechamento | Prazo de entrega |
| Sub-tarefa de mensagem | Dia do envio | Dia do envio |

### 3.2 Regra de Decomposicao (Sub-tarefas)

**Quando decompor um item em sub-tarefas:**

1. **Item tem checklist na descricao** — Se a descricao lista passos numerados ou checkboxes, cada passo vira sub-tarefa
2. **Item tem acoes em datas/horarios diferentes** — Cada acao com horario proprio vira sub-tarefa
3. **Item agrupa multiplos envios** — Cada envio individual vira sub-tarefa (ex: mensagens WhatsApp)
4. **Item e um marco com multiplas acoes** — Cada acao do marco vira sub-tarefa

**Quando NAO decompor:**

- Item e simples e atomico (1 acao, 1 resultado)
- Item ja e uma sub-tarefa
- Decomposicao criaria sub-tarefas triviais demais

### 3.3 Padrao de Nomes

| Tipo | Formato | Exemplo |
|------|---------|---------|
| Artefato | `Nome do Artefato (detalhe)` | `Canvas do Cliente Ideal (9 perguntas)` |
| Mensagem | `MSG-XXX-NN — Resumo (HH:MM)` | `MSG-FEC-01 — ULTIMO DIA (08:00)` |
| Marco | `MARCO: Descricao (detalhe)` | `MARCO: Webinario Ao Vivo (Terca 20h)` |
| Guia | `Guia de Setup: Ferramenta` | `Guia de Setup: EverWebinar` |
| Checklist | Descricao direta do que verificar | `Pagina de captura ativa e testada` |
| Sub-tarefa | Acao clara e especifica | `Ativar campanha Facebook Ads` |

### 3.4 Padrao de Descricoes

Toda descricao de work item deve conter:

**Para itens de conteudo/artefato:**
```html
<p><strong>Agente:</strong> @nome-do-agente</p>
<p><strong>Comando:</strong> <code>*comando</code></p>
<p><strong>Artefato:</strong> <code>caminho/do/arquivo.md</code></p>
<p>Descricao do que o item faz/entrega.</p>
<p><strong>Dependencias:</strong> arquivo1.md, arquivo2.md</p>
```

**Para sub-tarefas de mensagem WhatsApp:**
```html
<p><strong>Enviar:</strong> DD/MM as HH:MM</p>
<p><strong>Para:</strong> Publico-alvo</p>
<p><strong>Etapa:</strong> Nome da Etapa | <strong>Pilar:</strong> Pilar da Espiral</p>
<hr/>
<p><strong>TEXTO DA MENSAGEM:</strong></p>
<pre>Texto completo pronto para copiar e enviar.</pre>
<p><strong>NOTA:</strong> Instrucoes especiais se houver.</p>
```

**Para marcos (MARCO:):**
```html
<p><strong>MARCO [tipo] — Descricao.</strong></p>
<p><strong>Data:</strong> DD/MM as HH:MM</p>
<p><strong>Sub-tarefas:</strong> N acoes detalhadas como sub-itens.</p>
<p><strong>Meta:</strong> Resultado esperado.</p>
<p><strong>Referencia:</strong> Arquivo local relevante.</p>
```

**Para itens de checklist:**
```html
<p><strong>Verificar:</strong> O que precisa estar funcionando.</p>
<p><strong>Como testar:</strong> Passos para verificar.</p>
<p><strong>Link:</strong> URL relevante (se aplicavel).</p>
```

---

## 4. Processo de Migracao / Reorganizacao

### 4.1 Quando Executar

- Ao criar um novo projeto no Plane.so
- Ao iniciar uma nova rodada do webinario
- Quando detectar inconsistencias na organizacao

### 4.2 Passos do Processo

#### Passo 1: Diagnostico

1. Listar todos os work items (`*tarefas`)
2. Verificar quais itens estao **sem start_date**
3. Verificar quais itens tem **checklists comprimidos na descricao** (candidatos a decomposicao)
4. Verificar quais itens tem **descricoes vagas** (sem contexto, sem links)
5. Verificar se existem **referencias incorretas** (ferramentas que nao serao usadas nesta rodada)

#### Passo 2: Correcao de Referencias

1. Identificar itens que mencionam ferramentas/processos que **nao se aplicam** a esta rodada
2. Renomear os itens para refletir a realidade
3. Atualizar descricoes com instrucoes corretas
4. Itens que devem ser removidos: marcar como `[REMOVIDO]`, prioridade `none`, mover para Backlog

#### Passo 3: Correcao de Datas

1. Para cada item sem `start_date`, usar a **agenda-completa.md** como referencia
2. Aplicar as regras de datas da secao 3.1
3. Validar que nenhum item ficou sem ambas as datas

#### Passo 4: Decomposicao de Itens

1. Para cada item candidato (identificado no Passo 1):
   - Criar sub-tarefas usando `parent` para vincular ao item pai
   - Cada sub-tarefa deve ter: nome claro, descricao completa, datas, prioridade
   - Aplicar os padroes de nomes e descricoes da secao 3.3 e 3.4
2. Atualizar a descricao do item pai para referenciar as sub-tarefas

#### Passo 5: Enriquecimento de Descricoes

1. Para cada item com descricao vaga:
   - Adicionar referencia ao arquivo local do artefato
   - Adicionar instrucoes claras de como executar
   - Adicionar dependencias e pre-requisitos
2. Para marcos: adicionar contexto completo (horarios, metas, acoes)

#### Passo 6: Validacao

1. Rodar `*dashboard` para visao geral
2. Verificar que todos os itens tem datas
3. Verificar que itens decompostos tem sub-tarefas visiveis
4. Verificar que nenhuma referencia incorreta permanece

---

## 5. Processo para Nova Rodada

Quando iniciar a **Rodada N+1**, seguir este processo:

### 5.1 Preparacao

1. Duplicar a estrutura de modulos (se necessario)
2. Criar novos work items baseados nos resultados da analise da rodada anterior
3. Aplicar ajustes recomendados pelo @webinar-analyst

### 5.2 Mensagens WhatsApp

1. Gerar novas mensagens com @webinar-creator (`*mensagens`)
2. Para cada mensagem, criar sub-tarefa com:
   - Nome: `MSG-XXX-NN — Resumo (HH:MM)`
   - Descricao: texto completo pronto para copiar
   - Data: dia e hora exatos do envio
   - Parent: item pai "Mensagens WhatsApp — Envio Manual"
3. Vincular ao modulo de Execucao

### 5.3 Timeline

1. Gerar timeline com @webinar-operator (`*timeline`)
2. Mapear datas reais (D-0 = data do webinario)
3. Atualizar start_date e target_date de todos os itens

### 5.4 Checklist

1. Copiar itens do checklist pre-lancamento da rodada anterior
2. Ajustar datas para a nova rodada
3. Adicionar novos itens se necessario (baseado em licoes aprendidas)

---

## 6. Mapeamento de Datas da Campanha

### Template (substituir datas reais):

| Codigo | Dia da Semana | Data Real | Descricao |
|--------|--------------|-----------|-----------|
| D-4 | (definir) | (definir) | Inicio da campanha |
| D-3 | (definir) | (definir) | Captacao + slides |
| D-2 | (definir) | (definir) | Finalizacao slides + checkout |
| D-1 | (definir) | (definir) | Verificacao final |
| **D-0** | **(definir)** | **(definir)** | **DIA DO WEBINARIO** |
| D+1 | (definir) | (definir) | Replay ativo |
| D+2 | (definir) | (definir) | Ampliacao |
| D+3 | (definir) | (definir) | Ampliacao |
| D+4 | (definir) | (definir) | Ultimo lembrete |
| **D+5** | **(definir)** | **(definir)** | **FECHAMENTO DO CARRINHO** |

### Rodada 1 (referencia):

| Codigo | Dia | Data |
|--------|-----|------|
| D-4 | Sexta | 06/03/2026 |
| D-3 | Sabado | 07/03/2026 |
| D-2 | Domingo | 08/03/2026 |
| D-1 | Segunda | 09/03/2026 |
| D-0 | **Terca** | **10/03/2026** |
| D+1 | Quarta | 11/03/2026 |
| D+2 | Quinta | 12/03/2026 |
| D+3 | Sexta | 13/03/2026 |
| D+4 | Sabado | 14/03/2026 |
| D+5 | **Domingo** | **15/03/2026** |

---

## 7. Distribuicao de Mensagens por Dia

| Dia | Msgs | IDs | Prioridade |
|-----|------|-----|------------|
| D-4 (06/03) | 2 | NUT-01, NUT-02 | high |
| D-3 (07/03) | 2 | NUT-03, NUT-04 | high |
| D-2 (08/03) | 1 | NUT-05 | high |
| D-1 (09/03) | 2 | ANT-D1-01, ANT-D1-02 | high |
| D-0 (10/03) | 8 | ANT-D0-01 a 07, POS-01 | **urgent** |
| D+1 (11/03) | 2 | AMP-01, AMP-02 | high |
| D+2 (12/03) | 2 | AMP-03, AMP-04 | high |
| D+3 (13/03) | 2 | AMP-05, AMP-06 | medium |
| D+4 (14/03) | 1 | AMP-07 | high |
| D+5 (15/03) | 11 | FEC-01 a FEC-11 | **urgent** |
| **Total** | **33** | | |

---

## 8. Limitacoes Conhecidas do MCP Server

| Limitacao | Impacto | Workaround |
|-----------|---------|------------|
| `plane_create_page` retorna 404 | Nao consegue criar paginas de referencia via API | Criar paginas manualmente no Plane.so |
| `plane_list_pages` retorna 404 | Nao consegue listar paginas existentes | Acessar pelo browser |
| Nao existe `plane_delete_work_item` | Nao consegue remover itens | Marcar como [REMOVIDO], prioridade none, Backlog |
| Paginas sao por projeto, API tenta por workspace | Endpoint incorreto no MCP server | Corrigir MCP server ou usar browser |

---

## 9. Operacao Realizada — Rodada 1 (Registro)

**Data:** 2026-03-06
**Executor:** @plane-master (Orion)

### Resumo Quantitativo

| Acao | Quantidade | Status |
|------|-----------|--------|
| Correcao de datas (start_date) | 22 itens | Concluido |
| Correcao de referencias SendFlow | 5 itens | Concluido |
| Criacao de sub-tarefas | 52 itens | Concluido |
| Enriquecimento de descricoes | 6 itens | Concluido |
| Criacao de paginas | 0 de 3 | Bloqueado (API 404) |
| Remocao de itens | 0 de 1 | Adaptado (marcado REMOVIDO) |

### Sub-tarefas Criadas por Item Pai

| Item Pai | Sub-tarefas | Tipo |
|----------|-------------|------|
| 33 mensagens WhatsApp — Envio Manual | 33 | Mensagens com texto completo |
| MARCO: Ativar Anuncios Facebook/Instagram | 4 | Acoes de ativacao |
| MARCO: Webinario Ao Vivo (Terca 20h) | 6 | Acoes durante o evento |
| MARCO: Fechamento do Carrinho (23:59) | 3 | Acoes de encerramento |
| Teste completo do funil | 6 | Passos de verificacao |

### Itens Renomeados

| ID | De | Para |
|----|----|----|
| 2a434d02 | 33 mensagens agendadas no SendFlow | 33 mensagens WhatsApp — Envio Manual (D-4 a D+5) |
| e5ca8d69 | Grupo/lista WhatsApp criado no SendFlow | Grupo/lista WhatsApp criado |
| 10f620d9 | Automacao de boas-vindas configurada (MSG-NUT-01) | Mensagem de boas-vindas pronta (MSG-NUT-01) |
| 89ad9e82 | Segmentacao de compradores configurada (parar msgs) | Controle manual de compradores (parar msgs de venda) |
| a013e523 | Guia de Setup: SendFlow | [REMOVIDO] Guia de Setup: SendFlow — Rodada 2 |

---

## 10. Checklist de Validacao

Use este checklist apos qualquer reorganizacao:

- [ ] Todos os work items tem `start_date` E `target_date`
- [ ] Nenhum item referencia ferramenta que nao sera usada nesta rodada
- [ ] Itens com checklist na descricao foram decompostos em sub-tarefas
- [ ] Sub-tarefas de mensagem tem texto completo pronto para copiar
- [ ] Sub-tarefas de mensagem tem data e hora exatos
- [ ] Marcos tem sub-tarefas para cada acao
- [ ] Descricoes incluem referencias a arquivos locais quando aplicavel
- [ ] Modulos tem status correto (completed, in-progress, planned)
- [ ] Labels estao aplicados corretamente
- [ ] Dashboard mostra distribuicao coerente

---

*Documento gerado por @plane-master (Orion) — Processo padronizado para organizacao no Plane.so*
