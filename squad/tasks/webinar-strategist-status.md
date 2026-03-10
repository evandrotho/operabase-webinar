---

## Task Definition (AIOX Task Format V1.0)

```yaml
task: strategistStatus()
responsável: Sage (Strategist)
responsavel_type: Agente
squad: webinar

**Entrada:**
- campo: rodada
  tipo: number
  origem: Auto-detect
  obrigatório: true
  default: 1

**Saída:**
- campo: status_display
  tipo: string
  destino: Console output
  persistido: false
```

---

# Status dos Canvases — Task

## Purpose

Verificar e exibir o progresso dos canvases de planejamento da rodada ativa, mostrando quais estão preenchidos e quais estão pendentes, com sugestão do próximo passo.

## SEQUENTIAL Task Execution

### 1. Detectar Rodada Ativa

- Verificar `docs/webinar/` por diretórios `rodada-{N}`
- Se nenhum existir: "Nenhuma rodada iniciada. Execute qualquer comando de canvas para começar."
- Se múltiplos: usar o mais recente (maior N) como ativo

### 2. Verificar Artefatos

Para cada artefato, verificar existência em `docs/webinar/rodada-{N}/planejamento/`:

| Artefato | Arquivo | Pré-requisito de |
|----------|---------|-------------------|
| Canvas do Cliente Ideal | `canvas-cliente-ideal.md` | Avatar Blueprint |
| Canvas do Produto | `canvas-produto.md` | Canvas do Webinário |
| Avatar Blueprint | `avatar-blueprint.md` | Canvas do Webinário |
| Canvas do Webinário Infalível | `canvas-webinar.md` | Resumo |
| Planilha de Orçamento e Meta | `orcamento-meta.md` | Resumo (opcional) |
| Relatório Consolidado | `planejamento-resumo.md` | Handoff para Construção |

### 3. Exibir Status

```
STATUS DO PLANEJAMENTO — Rodada {N}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{Para cada artefato:}
{Se existe: "✅ {nome_artefato} — preenchido"}
{Se não existe: "⬜ {nome_artefato} — pendente → *{comando}"}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Progresso: {preenchidos}/{total} ({percentual}%)

{Se todos preenchidos menos resumo:
  "Todos os canvases estão prontos! Execute *resumo para gerar o relatório consolidado."}

{Se todos preenchidos incluindo resumo:
  "Planejamento COMPLETO! Pronto para a fase de construção.
   → Ativar @webinar-creator para iniciar o roteiro e conteúdo."}

{Se há pendências:
  "Próximo passo recomendado: *{comando_do_proximo_pendente}"}

{Mostrar ordem recomendada:
  "Ordem recomendada: *canvas-cliente → *canvas-produto → *avatar → *canvas-webinar → *orcamento → *resumo"}
```

### 4. Verificar Prontidão para Próxima Fase

Se todos os canvases obrigatórios estão preenchidos (cliente, produto, avatar, webinar):

```
PRONTIDÃO PARA CONSTRUÇÃO: ✅

Os artefatos mínimos para iniciar a construção estão prontos:
- ✅ Canvas do Cliente Ideal
- ✅ Canvas do Produto
- ✅ Avatar Blueprint
- ✅ Canvas do Webinário

{Se orcamento pendente: "Observação: O Orçamento e Meta (opcional) não foi preenchido. Ele enriquece a timeline e o pitch. Considere executar *orcamento antes de prosseguir."}

Para iniciar a construção: ative @webinar-creator
```

---

## Error Handling

1. **Error:** docs/webinar/ directory doesn't exist
   - **Resolution:** "Nenhum planejamento iniciado. Execute *canvas-cliente para começar."

---

## Metadata

```yaml
version: 1.0.0
squad: webinar
agent: webinar-strategist
command: "*status"
prd_reference: "PRD v2.1, Seção 3.2 — Status dos canvases"
tags:
  - webinar
  - planning
  - status
  - progress
updated_at: 2026-03-05
```
