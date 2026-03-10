# Roteiro — Pitch/Oferta do Webinário (15 Etapas)

> **Gerado por:** @webinar-creator (Spark)
> **Rodada:** {{rodada}}
> **Data de geração:** {{data_geracao}}
> **Duração estimada:** 20-30 minutos
> **Referência metodológica:** Seção 5.5 — Oferta/Pitch (15 Etapas + Stack Slide)

---

## Timeline

| # | Etapa | Duração | Minuto |
|---|-------|---------|--------|
| 1 | Transição | 1 min | {{minuto_inicio}} |
| 2 | Como vai ajudar | 1 min | — |
| 3 | Transformação | 1-2 min | — |
| 4 | Stack Slide (Produto) | 5-8 min | — |
| 5 | Dupla Queda de Preço | 2-3 min | — |
| 6 | CTA Principal | 1 min | — |
| 7 | Bônus de Ação Rápida | 2 min | — |
| 8 | Reforço | 1 min | — |
| 9 | Bônus Adicionais | 2-3 min | — |
| 10 | Garantia | 1-2 min | — |
| 11 | Recapitulação | 2 min | — |
| 12 | Urgência/Escassez | 1 min | — |
| 13 | Coerência | 1 min | — |
| 14 | Q&A | 3-5 min | — |
| 15 | CTA Final | 1 min | {{minuto_fim}} |

---

## Etapa 1 — Transição

**Técnica escolhida:** {{tecnica_transicao}}

{{#if transicao_permissao}}
> "Posso te mostrar como eu faço isso no dia a dia?"
{{/if}}

{{#if transicao_revelacao}}
> "O que eu te mostrei até agora é O QUE fazer. Agora vou te mostrar COMO..."
{{/if}}

{{#if transicao_ajuda}}
> "Deixa eu te ajudar a colocar tudo isso em prática..."
{{/if}}

**Trial Close:** "Faz sentido tudo que você aprendeu até aqui?"

---

## Etapa 2 — Como Vai Ajudar

> "{{fala_como_ajudar}}"

**Usar:** Grande Promessa + Mecanismo Único do Canvas do Produto.

---

## Etapa 3 — Transformação

> **Antes:** {{transformacao_antes}}
> **Depois:** {{transformacao_depois}}

**Trial Close:** "Consegue se imaginar nessa transformação?"

---

## Etapa 4 — Stack Slide (Apresentação do Produto)

### Composição do Stack

| # | Módulo/Entregável | O que vai aprender | Benefício | Valor |
|---|-------------------|-------------------|-----------|-------|
{{#each stack_items}}
| {{this.numero}} | {{this.nome}} | {{this.aprendizado}} | {{this.beneficio}} | R$ {{this.valor}} |
{{/each}}

**Fala por módulo:**
{{#each stack_items}}

#### Módulo {{this.numero}}: {{this.nome}}

> "No módulo {{this.numero}}, **{{this.nome}}**, você vai aprender {{this.aprendizado}}.
> O benefício direto é {{this.beneficio}}.
> Só isso já vale R$ {{this.valor}}."

**Trial Close:** "{{this.trial_close}}"

{{/each}}

---

## Etapa 5 — Dupla Queda de Preço

### Âncora Alta (Soma do Stack)

> "Se você somasse o valor de tudo que eu te mostrei, seria **R$ {{soma_stack}}**."

### Preço Oficial

> "Mas você NÃO vai pagar R$ {{soma_stack}}.
> O valor oficial do {{nome_produto}} é **R$ {{preco_oficial}}**."

### Preço Promocional

> "E hoje, neste webinário, o investimento é de apenas **R$ {{preco_promocional}}**."

{{#if condicoes_pagamento}}
> "Ou em {{parcelas}}x de R$ {{valor_parcela}}."
{{/if}}

**Trial Close:** "Isso faz sentido pra você?"

---

## Etapa 6 — CTA Principal

> "{{fala_cta_principal}}"

**Instrução visual:** [Mostrar botão/link na tela agora]
**Link:** {{link_compra}}

---

## Etapa 7 — Bônus de Ação Rápida

> **{{nome_bonus_rapido}}**
> {{descricao_bonus_rapido}}
> Valor: R$ {{valor_bonus_rapido}}

**Limitação:** {{tipo_limitacao}} — {{detalhe_limitacao}}
<!-- tipo: quantidade / tempo / evento -->

> "Esse bônus é EXCLUSIVO para quem agir agora. {{detalhe_limitacao}}."

---

## Etapa 8 — Reforço

> "Só esse bônus já vale R$ {{valor_bonus_rapido}}.
> Imagina ter {{beneficio_bonus_rapido}} de graça..."

---

## Etapa 9 — Bônus Adicionais

{{#each bonus_adicionais}}
### Bônus {{this.numero}}: {{this.nome}}

> {{this.descricao}}
> Valor: R$ {{this.valor}}

{{/each}}

**Stack Atualizado (visual):**
| Item | Valor |
|------|-------|
{{#each stack_items}}
| {{this.nome}} | R$ {{this.valor}} |
{{/each}}
{{#each bonus_adicionais}}
| Bônus: {{this.nome}} | R$ {{this.valor}} |
{{/each}}
| Bônus Ação Rápida: {{nome_bonus_rapido}} | R$ {{valor_bonus_rapido}} |
| **TOTAL** | **R$ {{soma_total_com_bonus}}** |
| ~~Valor real~~ | ~~R$ {{soma_total_com_bonus}}~~ |
| **Hoje** | **R$ {{preco_promocional}}** |

---

## Etapa 10 — Garantia

> "{{fala_garantia}}"

**Tipo:** {{tipo_garantia}}
**Prazo:** {{prazo_garantia}} dias
**Condição:** {{condicao_garantia}}

**Trial Close:** "Com essa garantia, o risco é todo meu. O que te impede?"

---

## Etapa 11 — Recapitulação

> "Vamos recapitular tudo que você recebe:"

{{#each stack_items}}
- {{this.nome}} — R$ {{this.valor}}
{{/each}}
{{#each bonus_adicionais}}
- Bônus: {{this.nome}} — R$ {{this.valor}}
{{/each}}
- Bônus Ação Rápida: {{nome_bonus_rapido}} — R$ {{valor_bonus_rapido}}
- Garantia de {{prazo_garantia}} dias

> "**Total real: R$ {{soma_total_com_bonus}}.
> Hoje: R$ {{preco_promocional}}.**"

---

## Etapa 12 — Urgência/Escassez

> "{{fala_urgencia_escassez}}"

**Motivos reais:**
{{#each motivos_urgencia}}
- {{this}}
{{/each}}

---

## Etapa 13 — Coerência

> "Se você acredita que **{{crenca_alvo}}**, então faz sentido agir agora.
> {{fala_coerencia}}"

---

## Etapa 14 — Q&A (Perguntas Frequentes)

{{#each faq_items}}
**P: {{this.pergunta}}**
R: {{this.resposta}}

{{/each}}

---

## Etapa 15 — CTA Final

> "{{fala_cta_final}}"

**Instrução visual:** [Mostrar botão/link em tela cheia]
**Link:** {{link_compra}}

---

## Notas de Apresentação

- **Slides sugeridos:** 15-25 slides (Stack Slide é o mais visual)
- **Interação com chat:** Trial Closes a cada 2-3 etapas
- **Pausa dramática:** Antes de revelar preço promocional (Etapa 5)
- **Energia:** Crescente — começa explicativo, termina com urgência máxima
- **Visual:** Stack Slide deve ser construído item por item (efeito acumulativo)
- **CTA:** Mostrar link/botão SEMPRE visível a partir da Etapa 6

---

## Inputs Utilizados

| Artefato | Status |
|----------|--------|
| canvas-webinar.md (blocos 12-15) | {{status_canvas_webinar}} |
| canvas-produto.md | {{status_canvas_produto}} |
| orcamento-meta.md | {{status_orcamento}} |

---

*Gerado por @webinar-creator (Spark) — Metodologia "Webinário Infalível" + "Perfect Webinar"*
