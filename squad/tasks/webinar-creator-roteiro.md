---

## Task Definition

```yaml
task: webinarCreatorRoteiro()
responsável: Spark (Creator)
responsavel_type: Agente
squad: webinar

knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "timeline-webinario"
      lines: "L2833-L2956"
      purpose: "Seção 5.6: Timeline Completa do Webinário — duração por seção, ordem, fluxo"

inputs:
  required:
    - campo: roteiro-abertura.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/conteudo/roteiro-abertura.md
      purpose: "Seção de Abertura completa"
    - campo: roteiro-empatia.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/conteudo/roteiro-empatia.md
      purpose: "Seção de Empatia completa"
    - campo: roteiro-conteudo.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/conteudo/roteiro-conteudo.md
      purpose: "Seção de Conteúdo completa (3 Secrets)"
    - campo: roteiro-pitch.md
      tipo: artifact
      origem: docs/webinar/rodada-{N}/conteudo/roteiro-pitch.md
      purpose: "Seção de Pitch completa (15 etapas)"

output:
  path: docs/webinar/rodada-{N}/conteudo/roteiro-completo.md
  template: webinar-roteiro-completo-tmpl.md
```

---

## Pre-Conditions

```yaml
pre-conditions:
  - [ ] roteiro-abertura.md exists in docs/webinar/rodada-{N}/conteudo/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-creator *abertura"
    error_message: "Para consolidar o roteiro, preciso da Abertura. Quer construir agora?"
  - [ ] roteiro-empatia.md exists in docs/webinar/rodada-{N}/conteudo/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-creator *empatia"
    error_message: "Para consolidar o roteiro, preciso da Empatia. Quer construir agora?"
  - [ ] roteiro-conteudo.md exists in docs/webinar/rodada-{N}/conteudo/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-creator *conteudo"
    error_message: "Para consolidar o roteiro, preciso do Conteúdo. Quer construir agora?"
  - [ ] roteiro-pitch.md exists in docs/webinar/rodada-{N}/conteudo/
    tipo: pre-condition
    blocker: true
    redirect: "@webinar-creator *pitch"
    error_message: "Para consolidar o roteiro, preciso do Pitch. Quer construir agora?"
```

---

## Task Execution — Semi-Automatic (elicit: minimal)

### Step 0: Detectar Rodada Ativa e Carregar Knowledge Base

- Verificar rodada ativa em `docs/webinar/`
- Carregar knowledge base: linhas L2833-L2956 (Timeline do Webinário)

### Step 1: Carregar e Validar as 4 Seções

- Ler `roteiro-abertura.md` — validar 7 blocos presentes
- Ler `roteiro-empatia.md` — validar modelo (A ou B) completo
- Ler `roteiro-conteudo.md` — validar 3 Secrets completos
- Ler `roteiro-pitch.md` — validar 15 etapas presentes

Se alguma seção estiver incompleta, alertar:
```
A seção [nome] parece incompleta. Faltam: [elementos faltantes].
Quer continuar assim ou quer refazer com `*[comando]`?
```

### Step 2: Montar Timeline (auto)

Distribuir duração por seção conforme metodologia:

| Seção | Duração Recomendada | Porcentagem |
|-------|-------------------|-------------|
| Abertura | 5-10 min | ~10% |
| Empatia/História | 5-10 min | ~10% |
| Conteúdo (3 Secrets) | 25-40 min | ~45% |
| Pitch/Oferta | 20-30 min | ~35% |
| **Total** | **55-90 min** | **100%** |

- Gerar timeline detalhada com marcadores de tempo:
  - 00:00-00:10 — Abertura: Headline + Método + Apresentação
  - 00:10-00:15 — Abertura: Lista + Urgência + Identificação + Regras
  - 00:15-00:25 — Empatia: História + Epiphany Bridge + Transição
  - 00:25-00:40 — Conteúdo: Secret 1 (Vehicle)
  - 00:40-00:55 — Conteúdo: Secret 2 (Internal) + Secret 3 (External)
  - 00:55-01:05 — Pitch: Transição + Produto + Stack + Preço
  - 01:05-01:15 — Pitch: CTA + Bônus + Garantia
  - 01:15-01:25 — Pitch: Recapitulação + Urgência + Q&A + CTA Final

### Step 3: Adicionar Notas de Apresentação (auto)

Para cada seção, adicionar notas práticas:
- **Slides sugeridos:** Quantos slides aproximados por seção
- **Interação com chat:** Momentos de pedir interação no chat
- **Pausas:** Onde fazer pausas dramáticas
- **CTAs visuais:** Quando mostrar botão/link na tela

### Step 4: Gerar Índice e Metadados (auto)

- Gerar índice com links internos para cada seção
- Incluir metadados:
  - Data de geração
  - Rodada
  - Canvases utilizados como input
  - Duração total estimada
  - Número de Trial Closes no pitch

### Step 5: Compilar e Salvar (elicit: confirmação final)

**Elicitation:**
```
Roteiro completo montado!

Resumo:
- Abertura: [X] blocos — [duração] min
- Empatia: Modelo [A/B] — [duração] min
- Conteúdo: 3 Secrets — [duração] min
- Pitch: 15 etapas — [duração] min
- Total: ~[duração total] minutos

Quer que eu salve o roteiro consolidado? (sim/não)
Se quiser revisar alguma seção antes, digite o nome: abertura, empatia, conteudo ou pitch.
```

- Usar template `webinar-roteiro-completo-tmpl.md`
- Salvar em `docs/webinar/rodada-{N}/conteudo/roteiro-completo.md`
- Informar próximos passos:
  - `*mensagens` para gerar mensagens WhatsApp
  - `*copy-captura` para copy da página de captura
  - Ou handoff para @webinar-operator quando tudo estiver pronto

---

## Post-Conditions

```yaml
post-conditions:
  - [ ] roteiro-completo.md salvo em docs/webinar/rodada-{N}/conteudo/
    tipo: post-condition
    blocker: true
  - [ ] Contém as 4 seções completas (Abertura, Empatia, Conteúdo, Pitch)
    tipo: post-condition
    blocker: true
  - [ ] Contém timeline com marcadores de tempo
    tipo: post-condition
    blocker: true
  - [ ] Contém índice navegável
    tipo: post-condition
    blocker: true
```

---

## Handoff

```yaml
next_agent: webinar-creator
next_command: "*mensagens"
condition: "Roteiro completo — próximo passo é mensagens"
alternatives:
  - agent: webinar-creator
    command: "*copy-captura"
    condition: "Usuário quer gerar copy de páginas"
  - agent: webinar-operator
    command: "*setup-everwebinar"
    condition: "Roteiro + mensagens prontos, ir para execução"
```

---

## Performance

```yaml
duration_expected: 5-10 min (consolidação com mínima interação)
token_usage: ~15,000-30,000 tokens (leitura de 4 arquivos + compilação)
```
