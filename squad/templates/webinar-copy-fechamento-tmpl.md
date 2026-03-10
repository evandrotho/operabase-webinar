# Copy — Página de Fechamento

> **Gerado por:** @webinar-creator (Spark)
> **Rodada:** {{rodada}}
> **Data de geração:** {{data_geracao}}
> **Referência metodológica:** Seção 4, Etapa 6 — Fechamento do Carrinho

---

## Regras da Metodologia (OBRIGATÓRIAS)

| Regra | Status |
|-------|--------|
| Deadline explícito (data/hora) | OBRIGATÓRIO |
| Headline de oferta (foco na oferta) | OBRIGATÓRIO |
| Contador regressivo | **OBRIGATÓRIO** (diferente da página de replay) |
| Seção de depoimentos | OBRIGATÓRIO |
| Tudo carrega imediato (sem delay) | OBRIGATÓRIO |

---

## Header com Contador

### Contador Regressivo

**[CONTADOR REGRESSIVO ATÉ {{data_hora_fechamento}}]**

**Instrução técnica:** Configurar contador que redireciona para página de "oferta encerrada" quando zerar.

### Headline de Oferta

> # {{headline_oferta}}

<!-- Ex: "Última chance: {{produto}} com {{desconto}}% de desconto" -->
<!-- Ex: "{{produto}}: {{promessa}} por apenas R$ {{preco_promocional}}" -->

### Subheadline

> {{subheadline_oferta}}

<!-- Ex: "Oferta especial válida até {{data_hora_fechamento}}" -->

---

## Resumo da Oferta (Stack Completo)

### O que você recebe:

{{#each stack_items}}
#### {{this.emoji}} {{this.nome}}

{{this.descricao_breve}}

> Valor: **R$ {{this.valor}}**

{{/each}}

### Bônus Inclusos:

{{#each bonus}}
#### {{this.emoji}} Bônus: {{this.nome}}

{{this.descricao_breve}}

> Valor: **R$ {{this.valor}}**

{{/each}}

---

## Preço — Dupla Queda

| | Valor |
|---|---|
| Valor total do Stack | ~~R$ {{soma_stack}}~~ |
| Preço oficial | ~~R$ {{preco_oficial}}~~ |
| **Preço promocional** | **R$ {{preco_promocional}}** |

{{#if condicoes_pagamento}}
> Ou em **{{parcelas}}x de R$ {{valor_parcela}}**
{{/if}}

---

## CTA Principal

> ### {{texto_cta_principal}}

**[BOTÃO DE COMPRA]** — {{link_compra}}

> {{nota_seguranca}}
<!-- Ex: "Pagamento seguro. Seus dados estão protegidos." -->

---

## Garantia

### {{tipo_garantia}}

> {{texto_garantia}}

<!-- Ex: "Garantia incondicional de 7 dias. Se por qualquer motivo você não ficar satisfeito, devolvemos 100% do seu investimento. Sem perguntas, sem burocracia." -->

**Prazo:** {{prazo_garantia}} dias
**Condição:** {{condicao_garantia}}

---

## Depoimentos

{{#each depoimentos}}
### {{this.nome}} — {{this.cidade_profissao}}

> "{{this.texto}}"

{{#if this.resultado}}
**Resultado:** {{this.resultado}}
{{/if}}

---

{{/each}}

> **Nota:** Substitua os depoimentos acima pelos depoimentos reais dos seus clientes.
> Dica: priorize depoimentos com RESULTADOS CONCRETOS (números, transformações específicas).

---

## FAQ — Perguntas Frequentes

{{#each faq}}
### {{this.pergunta}}

{{this.resposta}}

{{/each}}

---

## Urgência e Escassez

> ### {{headline_urgencia}}

{{#each motivos_urgencia}}
- {{this.emoji}} **{{this.motivo}}**
{{/each}}

> **O carrinho fecha em {{data_hora_fechamento}}. Depois disso, a oferta não estará mais disponível.**

---

## Custo de Não Agir

> {{texto_custo_nao_agir}}

<!-- Ex: "Quanto vai custar continuar [problema] por mais 6 meses? Se você calcular o que está perdendo — em dinheiro, tempo e oportunidade — o investimento de R$ [preço] é uma fração do custo de não agir." -->

---

## CTA Final

> ### {{texto_cta_final}}

**[BOTÃO DE COMPRA GRANDE]** — {{link_compra}}

**[CONTADOR REGRESSIVO]**

> {{mensagem_final}}

<!-- Ex: "Essa é a sua última chance. Quando o contador zerar, a oferta será encerrada definitivamente." -->

---

## Diferenças vs. Página de Replay

| Elemento | Página de Fechamento | Página de Replay |
|----------|---------------------|-----------------|
| Contador regressivo | **SIM** | **NÃO** |
| Oferta visível | Imediato | Com delay |
| Depoimentos | **SIM** | Não |
| FAQ | **SIM** | Não |
| Timestamps | Não | Sim |
| Urgência | Via deadline | Via escassez do replay |
| Vídeo do webinário | Não (foco na oferta) | Sim (replay) |

---

## Elementos Técnicos

### Pixel Events
- `PageView` — ao carregar a página
- `ViewContent` — ao visualizar a oferta
- `InitiateCheckout` — ao clicar no botão de compra
- `Purchase` — na página de obrigado (pós-compra)

### Configuração do Contador
- **Ferramenta sugerida:** Deadline Funnel, ClickFunnels, ou timer HTML/JS
- **Comportamento ao zerar:** Redirecionar para página de "oferta encerrada"
- **NUNCA usar contador falso** — a escassez deve ser REAL

### Página de "Oferta Encerrada"
- Headline: "O carrinho fechou"
- Mensagem: "A oferta especial não está mais disponível. Fique atento para a próxima oportunidade."
- Opcional: formulário de lista de espera

### Performance
- Página deve carregar em < 2 segundos (nenhum elemento com delay)
- Botão CTA em cor contrastante, visível acima da dobra
- Mobile-first (maioria acessa por celular via WhatsApp)

---

## Inputs Utilizados

| Artefato | Status |
|----------|--------|
| canvas-webinar.md (blocos 12-15) | {{status_canvas_webinar}} |
| canvas-produto.md | {{status_canvas_produto}} |

---

*Gerado por @webinar-creator (Spark) — Metodologia "Webinário Infalível" + "Perfect Webinar"*
