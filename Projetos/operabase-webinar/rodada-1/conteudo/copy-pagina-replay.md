# Copy — Pagina de Replay

> **Gerado por:** @webinar-creator (Spark)
> **Rodada:** 1
> **Data de geracao:** 2026-03-06
> **Referencia metodologica:** Secao 4, Etapa 5 — Ampliacao do Impacto

---

## Regras da Metodologia (OBRIGATORIAS)

| Regra | Status |
|-------|--------|
| Pre-headline de escassez | ✅ PRESENTE |
| Headline de urgencia | ✅ PRESENTE |
| Timestamps como headlines de venda | ✅ PRESENTE (6 timestamps) |
| Oferta com delay | ✅ PRESENTE (aparece apos 55 min) |
| Contador regressivo | ❌ PROIBIDO (diferente da pagina de fechamento) |

---

## Header

### Pre-headline de Escassez

> ⚠️ Este replay ficara disponivel por tempo limitado. Assista antes que saia do ar.

### Headline de Urgencia

> # Assista antes que saia do ar: Como empresarios comuns estao substituindo equipe inteira por IA sem criar nada do zero

### Subheadline

> Assista a aula completa e descubra a **Infraestrutura de IA Espelhada** — o metodo que permite montar IA na sua empresa em semanas, sem ser tecnico.

---

## Player de Video

**[VIDEO DO WEBINARIO — GRAVACAO COMPLETA]**

**Configuracao tecnica:**
- Autoplay: SIM (com mute, se necessario para politicas do browser)
- Controles: Visiveis (permitir avancar/voltar)
- Qualidade: HD minimo
- Duracao: ~71 minutos

---

## Timestamps como Headlines de Venda

> Navegue pelos momentos mais importantes:

### ⏱️ 00:00 — A headline que esta mudando a forma como empresarios veem IA

> Como empresarios sem nenhum conhecimento tecnico estao montando infraestruturas completas de IA. O inicio da aula ja vai mudar sua perspectiva.

**[Assistir do inicio]**

---

### ⏱️ 12:00 — A epifania que transformou tudo: "IA nao e chatbot, e infraestrutura"

> O momento exato em que Caio descobriu que tudo que sabia sobre IA estava errado — e como essa descoberta levou ele a substituir 18 funcionarios. Esse insight vale a aula inteira.

**[Pular para 12:00]**

---

### ⏱️ 16:00 — Os 3 niveis de IA que 99% dos empresarios desconhecem

> A maioria usa IA no nivel "chatbot". Descubra os outros 2 niveis e entenda por que voce estava usando uma Ferrari pra ir ao mercado da esquina.

**[Pular para 16:00]**

---

### ⏱️ 27:00 — Por que "eu nao sou tecnico" NAO e desculpa (e a prova)

> Se voce acha que precisa programar pra usar IA, esse trecho vai mudar sua mente. Veja a analogia que simplifica tudo.

**[Pular para 27:00]**

---

### ⏱️ 37:00 — 18 meses vs. semanas: como encurtar o caminho

> A timeline real de Caio e por que voce NAO precisa repetir os mesmos 18 meses de tentativa e erro. Espelhamento muda tudo.

**[Pular para 37:00]**

---

### ⏱️ 52:00 — Tudo que voce recebe (e o preco que vai surpreender)

> O Stack completo do OperaBase revelado: 6 entregaveis + 3 bonus exclusivos. E a Dupla Queda de Preco que gerou reacao no chat ao vivo.

**[Pular para 52:00]**

---

## Secao da Oferta (aparece com delay)

**CONFIGURACAO:** Esta secao deve aparecer apos **55 minutos** de video.
**Instrucao tecnica:** Usar CSS/JS para mostrar apos delay, ou configurar no EverWebinar/plataforma.

### Resumo da Oferta

> **OperaBase** — Centro de inteligencia para empresarios que querem estruturar IA na empresa sem ser tecnico e sem criar do zero.

### O que esta incluido:

| # | Item | Valor |
|---|------|-------|
| 1 | Area de Membros OperaBase | R$4.997 |
| 2 | Frameworks de IA Prontos | R$7.997 |
| 3 | Dashboard de Infraestrutura | R$9.997 |
| 4 | Squads de IA Operacionais | R$9.997 |
| 5 | Encontros Estrategicos com Caio | R$7.997 |
| 6 | Eventos Presenciais | R$4.997 |
| | **Total do Stack** | **R$45.982** |

**Bonus:**

| # | Bonus | Valor |
|---|-------|-------|
| 1 | Mentoria Individual com Caio (3 vagas) | R$2.997 |
| 2 | Kit de Implementacao Rapida | R$1.997 |
| 3 | Acesso ao Grupo VIP (30 dias) | R$1.497 |
| | **Total de Bonus** | **R$6.491** |

> **De ~~R$52.473~~ por apenas R$2.500**
>
> Ou em 12x de R$208

### CTA

> **QUERO ENTRAR NO OPERABASE AGORA**

**[BOTAO DE COMPRA]** — {{link_compra}}

### Garantia

> Garantia incondicional de 7 dias. Nao gostou? 100% do dinheiro de volta. Sem perguntas.

---

## Nota de Escassez (Footer)

> ⚠️ Este replay sera removido em breve. A oferta especial do webinario (R$2.500 em vez de R$5.000) tem prazo limitado. Nao perca a oportunidade.

**LEMBRETE: SEM contador regressivo nesta pagina.**
A urgencia e criada pela escassez do replay, nao por um timer.

---

## Elementos Tecnicos

### Pixel Events
- `PageView` — ao carregar a pagina
- `ViewContent` — ao iniciar o video
- `AddToCart` — ao clicar no botao de compra (quando oferta aparece)

### Configuracao do Delay
- **EverWebinar:** Configurar "Oferta Timer" para 55 minutos
- **Manual (HTML/JS):** `setTimeout(showOffer, 3300000)` (55 min em ms)
- **Alternativa:** Mostrar oferta quando player atinge minuto 55

### Tracking de Visualizacao
- Registrar: quem acessou, quanto tempo assistiu, se clicou na oferta
- Usar para segmentacao:
  - Assistiu < 30 min → Mensagem "assista o trecho X"
  - Assistiu > 55 min e NAO clicou → Mensagem de urgencia
  - Clicou e NAO comprou → Remarketing

### Configuracao de Remocao
- **Remover replay:** 5 dias apos o webinario (D+5, mesmo dia do fechamento)
- **Redirecionar apos remocao:** Pagina "O replay nao esta mais disponivel"

---

## Diferencas vs. Pagina de Fechamento

| Elemento | Pagina de Replay | Pagina de Fechamento |
|----------|-----------------|---------------------|
| Contador regressivo | **NAO** | **SIM** |
| Oferta visivel | Com delay (55 min) | Imediato |
| Depoimentos | Nao (foco no replay) | Sim |
| FAQ | Nao | Sim |
| Timestamps | Sim (6 headlines de venda) | Nao |
| Urgencia | Via escassez do replay | Via deadline |
| Video | Sim (replay completo) | Nao (foco na oferta) |

---

## Inputs Utilizados

| Artefato | Status |
|----------|--------|
| roteiro-completo.md | Completo (timestamps) |
| canvas-webinar.md | Completo (oferta) |
| roteiro-pitch.md | Completo (Stack atualizado) |

---

*Gerado por @webinar-creator (Spark) — Metodologia "Webinario Infalivel" + "Perfect Webinar"*
