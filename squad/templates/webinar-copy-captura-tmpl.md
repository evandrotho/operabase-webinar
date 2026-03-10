# Copy — Página de Captura

> **Gerado por:** @webinar-creator (Spark)
> **Rodada:** {{rodada}}
> **Data de geração:** {{data_geracao}}
> **Formato:** {{formato}}
> **Referência metodológica:** Seção 4, Etapa 1 — Captação
> **Taxa de conversão esperada:** ~40% (benchmark da metodologia)

---

## Formato: {{formato_nome}}

<!-- formato_nome: "Simples (webinário gratuito)" OU "Completa (ingresso pago)" -->

---

{{#if formato_simples}}
## Página Simples — Webinário Gratuito

### Header

**Pré-headline:**
> {{pre_headline}}

**Headline Principal:**
> # {{headline_principal}}

**Subheadline:**
> {{subheadline}}

---

### Data e Horário

> **{{data_webinario}}** às **{{hora_webinario}}**
> Evento online e gratuito

---

### O que você vai aprender:

{{#each bullets}}
- {{this.emoji}} **{{this.titulo}}** — {{this.descricao}}
{{/each}}

---

### Formulário de Cadastro

**Campos sugeridos:**
- Nome completo
- E-mail
- WhatsApp (com DDD)

**Botão CTA:**
> **{{texto_cta}}**

**Nota sob o botão:**
> {{nota_seguranca}}

---

### Elemento de Escassez (opcional)

> {{elemento_escassez}}

---

### Sobre o Apresentador (breve)

> **{{nome_expert}}** — {{bio_breve}}

{{/if}}

{{#if formato_completo}}
## Página Completa — Ingresso Pago ou Alto Valor

### Header

**Pré-headline:**
> {{pre_headline}}

**Headline Principal:**
> # {{headline_principal}}

**Subheadline:**
> {{subheadline}}

**CTA Header:**
> **{{texto_cta_header}}**

---

### Para quem é este webinário:

{{#each perfis_para_quem}}
- {{this.emoji}} {{this.descricao}}
{{/each}}

---

### Para quem NÃO é:

{{#each perfis_nao_para_quem}}
- {{this.descricao}}
{{/each}}

---

### O que você vai aprender (expandido):

{{#each bullets_expandidos}}
#### {{this.numero}}. {{this.titulo}}

{{this.descricao}}

{{/each}}

---

### Quem é {{nome_expert}}

{{bio_completa}}

**Credenciais:**
{{#each credenciais}}
- {{this}}
{{/each}}

---

### Depoimentos

{{#each depoimentos}}
> "{{this.texto}}"
> — **{{this.nome}}**, {{this.cargo}}

{{/each}}

---

### FAQ

{{#each faq}}
**{{this.pergunta}}**
{{this.resposta}}

{{/each}}

---

### Detalhes do Evento

| | |
|---|---|
| **Data** | {{data_webinario}} |
| **Horário** | {{hora_webinario}} |
| **Duração** | {{duracao_evento}} |
| **Formato** | Online ao vivo |
| **Investimento** | {{investimento}} |

---

### CTA Final

> # {{headline_cta_final}}

> **{{texto_cta_final}}**

**Nota de segurança:**
> {{nota_seguranca}}

{{#if tem_garantia}}
**Garantia:**
> {{texto_garantia}}
{{/if}}

{{/if}}

---

## Congruência Criativo-Página

> **IMPORTANTE:** A linguagem e promessa dos anúncios (Facebook, Instagram, Google) DEVEM
> ser congruentes com esta página. Se o anúncio promete X, a página deve confirmar X imediatamente.
>
> **Headline do anúncio deve ecoar:** {{headline_principal}}
> **Imagem do anúncio deve remeter a:** {{tema_visual}}

---

## Elementos Técnicos

### Pixel Events (para configurar)
- `PageView` — ao carregar a página
- `Lead` — ao submeter formulário
- `CompleteRegistration` — na página de obrigado

### SEO
- **Title tag:** {{headline_principal}} | {{nome_expert}}
- **Meta description:** {{subheadline}}

### Performance
- Página deve carregar em < 3 segundos
- Formulário acima da dobra (visível sem scroll)
- Botão CTA em cor contrastante

---

## Inputs Utilizados

| Artefato | Status |
|----------|--------|
| canvas-produto.md | {{status_canvas_produto}} |
| avatar-blueprint.md | {{status_avatar}} |
| canvas-webinar.md | {{status_canvas_webinar}} |

---

*Gerado por @webinar-creator (Spark) — Metodologia "Webinário Infalível" + "Perfect Webinar"*
