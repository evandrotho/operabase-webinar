# Copy — Página de Replay

> **Gerado por:** @webinar-creator (Spark)
> **Rodada:** {{rodada}}
> **Data de geração:** {{data_geracao}}
> **Referência metodológica:** Seção 4, Etapa 5 — Ampliação do Impacto

---

## Regras da Metodologia (OBRIGATÓRIAS)

| Regra | Status |
|-------|--------|
| Pré-headline de escassez | OBRIGATÓRIO |
| Headline de urgência | OBRIGATÓRIO |
| Timestamps como headlines de venda | OBRIGATÓRIO |
| Oferta com delay | OBRIGATÓRIO |
| Contador regressivo | **PROIBIDO** (diferente da página de fechamento) |

---

## Header

### Pré-headline de Escassez

> {{pre_headline_escassez}}

<!-- Ex: "Este replay ficará disponível por tempo limitado" -->
<!-- Ex: "Replay disponível apenas até {{data_expiracao}}" -->

### Headline de Urgência

> # {{headline_urgencia}}

<!-- Ex: "Assista antes que saia do ar: Como [resultado] sem [obstáculo]" -->

### Subheadline

> {{subheadline}}

<!-- Ex: "Assista a aula completa e descubra o {{mecanismo_unico}} que já ajudou [X] pessoas" -->

---

## Player de Vídeo

**[VÍDEO DO WEBINÁRIO]**

**Configuração técnica:**
- Autoplay: SIM (com mute, se necessário)
- Controles: Visíveis (permitir avançar/voltar)
- Qualidade: HD mínimo

---

## Timestamps como Headlines de Venda

> Navegue pelos momentos mais importantes:

{{#each timestamps}}
### {{this.minuto}} — {{this.headline}}

> {{this.descricao}}

**[Pular para este momento]** _(link com timestamp)_

{{/each}}

<!-- Exemplo:
### 15:30 — O erro #1 que impede [resultado]
> A maioria das pessoas comete este erro sem perceber. Descubra como evitar.

### 32:00 — O método {{mecanismo_unico}} explicado na prática
> Veja exatamente O QUE fazer para [resultado] usando [mecanismo].

### 48:00 — A história que vai mudar sua perspectiva
> Quando [expert] descobriu isso, tudo mudou. Veja por quê.

### 58:00 — A oferta que vai surpreender você
> Como ter acesso a tudo isso por um valor que vai te impressionar.
-->

---

## Seção da Oferta (aparece com delay)

**CONFIGURAÇÃO:** Esta seção deve aparecer após {{delay_minutos}} minutos.
**Instrução técnica:** Usar CSS/JS para mostrar após delay ou configurar no EverWebinar.

### Resumo da Oferta

> **{{nome_produto}}**
>
> {{descricao_breve_oferta}}

### O que está incluído:

{{#each stack_resumido}}
- {{this.nome}} — R$ {{this.valor}}
{{/each}}

> **De ~~R$ {{soma_stack}}~~ por apenas R$ {{preco_promocional}}**

{{#if condicoes_pagamento}}
> Ou em {{parcelas}}x de R$ {{valor_parcela}}
{{/if}}

### CTA

> **{{texto_cta}}**

**[BOTÃO DE COMPRA]** — {{link_compra}}

### Garantia

> {{texto_garantia_breve}}

---

## Nota de Escassez (Footer)

> {{nota_escassez_footer}}

<!-- Ex: "Este replay será removido em {{data_remocao}}. Não perca a oportunidade." -->

**LEMBRETE: SEM contador regressivo nesta página.**
A urgência é criada pela escassez do replay, não por um timer.

---

## Elementos Técnicos

### Pixel Events
- `PageView` — ao carregar a página
- `ViewContent` — ao iniciar o vídeo
- `AddToCart` — ao clicar no botão de compra (quando oferta aparece)

### Configuração do Delay
- **EverWebinar:** Configurar "Oferta Timer" para {{delay_minutos}} minutos
- **Manual (HTML/JS):** `setTimeout(showOffer, {{delay_segundos}} * 1000)`

### Tracking de Visualização
- Registrar: quem acessou, quanto tempo assistiu, se clicou na oferta
- Usar para segmentação de mensagens posteriores

---

## Diferenças vs. Página de Fechamento

| Elemento | Página de Replay | Página de Fechamento |
|----------|-----------------|---------------------|
| Contador regressivo | **NÃO** | **SIM** |
| Oferta visível | Com delay | Imediato |
| Depoimentos | Não (foco no replay) | Sim |
| FAQ | Não | Sim |
| Timestamps | Sim (headlines de venda) | Não |
| Urgência | Via escassez do replay | Via deadline |

---

## Inputs Utilizados

| Artefato | Status |
|----------|--------|
| roteiro-completo.md | {{status_roteiro}} |
| canvas-webinar.md | {{status_canvas_webinar}} |

---

*Gerado por @webinar-creator (Spark) — Metodologia "Webinário Infalível" + "Perfect Webinar"*
