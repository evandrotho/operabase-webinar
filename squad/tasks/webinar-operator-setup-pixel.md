---
tools: []
checklists: []
execution_mode: interactive
---

# webinar-operator-setup-pixel

Guia passo-a-passo para configurar o Facebook Pixel e tracking em todas as paginas do funil.

## Purpose

Orientar o usuario na configuracao do Facebook Pixel: instalacao do pixel base, eventos por pagina (PageView, Lead, Custom), integracao com deep links do SendFlow e regra anti-duplicacao. Essencial para medir performance de anuncios e otimizar campanhas.

## Knowledge Base

```yaml
knowledge_base:
  source: docs/METHODOLOGY-ANALYSIS.md
  sections:
    - id: "integracoes-pixel"
      lines: "L3598-L3735"
      purpose: "Integracoes e Webhooks: inclui secao 6.3.2 sobre Facebook Pixel -- eventos por pagina, deep link SendFlow, regra anti-duplicacao"
    - id: "etapa-1-captacao"
      lines: "L451-L525"
      purpose: "Etapa 1 do funil (Captacao): pagina de captura onde Pixel deve disparar Lead"
    - id: "stack-tecnica"
      lines: "L3736-L3758"
      purpose: "Stack tecnica completa"
```

## Prerequisites

```yaml
prerequisites:
  required: []  # Este comando e instrucional e nao depende de artefatos especificos
  optional:
    - artifact: "docs/webinar/rodada-{N}/conteudo/copy-pagina-captura.md"
      description: "URLs das paginas onde instalar o Pixel"
      enriches: "URLs especificas para configurar eventos"
```

## Task Definition

```yaml
task: setupPixel()
responsavel: Atlas (Executor)
responsavel_type: Agente
elicit: true

Entrada:
- campo: copy_captura
  tipo: file
  origem: "docs/webinar/rodada-{N}/conteudo/copy-pagina-captura.md"
  obrigatorio: false

Saida:
- campo: guia_pixel
  tipo: file
  destino: "docs/webinar/rodada-{N}/execucao/guia-pixel.md"
  persistido: true
  template: webinar-guia-setup-tmpl.md
```

## SEQUENTIAL Task Execution

### 0. Carregar Knowledge Base

- Carregar secoes: L3598-L3735 (foco em 6.3.2), L451-L525, L3736-L3758
- Se `copy-pagina-captura.md` existir, ler para extrair contexto de paginas

### 1. Elicitar Informacoes do Pixel

**ELICIT (pergunta 1 de cada vez):**

1. "Voce ja tem um Facebook Pixel criado no Gerenciador de Anuncios? Se sim, qual o ID do Pixel?"
2. "Quais paginas voce vai usar na campanha? (Marque todas que se aplicam)
   1. Pagina de captura (landing page)
   2. Pagina de obrigado/confirmacao
   3. Pagina do webinario (EverWebinar)
   4. Pagina de replay
   5. Pagina de checkout/vendas
   6. Pagina de fechamento
   7. Outras?"
3. "Voce usa alguma ferramenta de construcao de paginas? (LeadPages, ClickFunnels, WordPress, Elementor, outra?)"
4. "Voce vai rodar anuncios no Facebook/Instagram para esta campanha?"

### 2. Gerar Guia de Instalacao do Pixel Base

- **Criacao do Pixel** (se nao tem):
  - Passo-a-passo no Gerenciador de Anuncios do Facebook
  - Onde encontrar: Configuracoes > Fontes de Dados > Pixels
  - Como nomear (sugestao: "Pixel - [Nome do Webinario]")
- **Instalacao do codigo base:**
  - Onde colar o codigo (head do site)
  - Instrucoes por ferramenta de paginas (LeadPages, ClickFunnels, WordPress, etc.)
  - Como verificar se esta funcionando (Facebook Pixel Helper extensao do Chrome)

### 3. Gerar Guia de Eventos por Pagina

Baseado na knowledge base (L3598-L3735, secao 6.3.2):

| Pagina | Evento Pixel | Tipo | Quando Dispara |
|--------|-------------|------|----------------|
| Pagina de captura | `PageView` | Padrao | Ao carregar pagina |
| Pagina de captura | `Lead` | Padrao | Ao preencher formulario |
| Pagina de obrigado | `PageView` | Padrao | Ao carregar (confirma lead) |
| Pagina de obrigado | `CompleteRegistration` | Padrao | Ao carregar |
| Pagina do webinario | `PageView` | Padrao | Ao carregar |
| Pagina do webinario | `ViewContent` | Padrao | Ao iniciar assistir |
| Pagina de replay | `PageView` | Padrao | Ao carregar |
| Pagina de replay | `ViewContent` | Custom | Ao clicar play |
| Pagina de checkout | `PageView` | Padrao | Ao carregar |
| Pagina de checkout | `InitiateCheckout` | Padrao | Ao iniciar checkout |
| Pagina de checkout | `Purchase` | Padrao | Ao confirmar pagamento |
| Pagina de fechamento | `PageView` | Padrao | Ao carregar |

- **Para cada evento:**
  - Codigo exato do evento (fbq('track', 'EventName', {params}))
  - Onde inserir na pagina
  - Parametros recomendados (value, currency, content_name)

### 4. Gerar Guia de Integracao Deep Link com SendFlow

- **O que e deep link com Pixel:**
  - Link que passa pelo Facebook antes de redirecionar, permitindo rastreamento de conversoes a partir de cliques no WhatsApp
- **Como configurar:**
  - Criar link de redirecionamento com parametros UTM
  - Configurar no SendFlow: usar deep link em vez de link direto
  - Parametros UTM recomendados: utm_source=whatsapp, utm_medium=sendflow, utm_campaign=[nome-campanha], utm_content=[etapa-funil]
- **Regra anti-duplicacao:**
  - Problema: mesmo lead pode clicar multiplas vezes
  - Solucao: usar deduplicacao do Pixel (event_id unico por lead)
  - Como implementar: incluir external_id no evento

### 5. Gerar Guia de Verificacao e Teste

- **Ferramentas de teste:**
  - Facebook Pixel Helper (extensao Chrome)
  - Test Events no Gerenciador de Anuncios
  - Como acessar: Gerenciador de Eventos > Pixel > Teste de Eventos
- **Checklist de teste:**
  - [ ] Pixel base instalado em todas as paginas
  - [ ] PageView disparando em cada pagina
  - [ ] Lead disparando na pagina de captura
  - [ ] CompleteRegistration na pagina de obrigado
  - [ ] ViewContent na pagina do webinario
  - [ ] InitiateCheckout na pagina de checkout
  - [ ] Purchase na confirmacao de pagamento
  - [ ] Deep links do SendFlow com parametros UTM
  - [ ] Eventos nao duplicam ao recarregar pagina

### 6. Gerar Guia de Audiencias e Otimizacao

- **Audiencias para criar baseadas nos eventos:**
  - Visitantes da pagina de captura (PageView) -- excluir quem ja converteu
  - Leads que registraram mas nao compareceram
  - Leads que compareceram mas nao compraram
  - Compradores (para audiencias lookalike)
- **Orientacoes basicas de otimizacao:**
  - Campanha de conversao otimizada para Lead
  - Retargeting de quem visitou mas nao registrou
  - Retargeting de replay para quem compareceu

### 7. Compilar e Salvar Guia

- Usar template `webinar-guia-setup-tmpl.md` com ferramenta = "Facebook Pixel"
- Preencher todas as secoes
- Salvar em `docs/webinar/rodada-{N}/execucao/guia-pixel.md`

### 8. Sugerir Proximo Passo

- Se timeline nao montada: "Proximo passo: `*timeline` para montar o cronograma completo"
- Se todas as ferramentas configuradas: "Proximo passo: `*checklist` para verificacao final"

## Output

```yaml
output:
  path: "docs/webinar/rodada-{N}/execucao/guia-pixel.md"
  template: webinar-guia-setup-tmpl.md
  format: markdown
  sections:
    - Informacoes do Projeto
    - Instalacao do Pixel Base
    - Eventos por Pagina
    - Deep Links com SendFlow
    - Verificacao e Teste
    - Audiencias e Otimizacao
    - Checklist de Verificacao
```

## Error Handling

**Strategy:** guide-and-retry

**Common Errors:**

1. **Error:** Usuario nao tem conta de anuncios do Facebook
   - **Resolution:** Orientar sobre criacao do Gerenciador de Anuncios
2. **Error:** Pixel Helper mostra erro
   - **Resolution:** Verificar codigo instalado, testar em aba anonima, limpar cache
3. **Error:** Eventos duplicados
   - **Resolution:** Implementar regra anti-duplicacao com event_id

## Handoff

```yaml
next_agent: "@webinar-operator"
next_command: "*timeline"
condition: "Pixel configurado, timeline pendente"
alternatives:
  - agent: "@webinar-operator"
    command: "*checklist"
    condition: "Todas as ferramentas e timeline prontas"
```
