# Guia de Configuracao: {{ferramenta}}

**Template ID:** webinar-guia-setup-template-v1
**Purpose:** Template padrao para guias de configuracao de ferramentas do webinario
**Usado por:** @webinar-operator (Atlas) -- comandos *setup-everwebinar, *setup-sendflow, *setup-pagamento, *setup-pixel

---

## Template Variables

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `{{ferramenta}}` | string | Nome da ferramenta | "EverWebinar" |
| `{{rodada}}` | number | Numero da rodada | 1 |
| `{{data_geracao}}` | string | Data de geracao do guia | "2026-03-10" |
| `{{nome_webinario}}` | string | Nome/titulo do webinario | "Webinario Infalivel" |
| `{{secoes}}` | array | Secoes do guia | [...] |

---

## Document Template

```markdown
# Guia de Configuracao: {{ferramenta}}

> **Rodada:** {{rodada}}
> **Gerado em:** {{data_geracao}}
> **Webinario:** {{nome_webinario}}
> **Agente:** @webinar-operator (Atlas)

---

## Resumo

{{resumo_configuracao}}

---

## Pre-requisitos

Antes de iniciar a configuracao, certifique-se de ter:

{{#each prerequisitos}}
- [ ] {{this}}
{{/each}}

---

## Informacoes do Projeto

| Campo | Valor |
|-------|-------|
| Webinario | {{nome_webinario}} |
| Produto | {{nome_produto}} |
| Ticket | R$ {{ticket}} |
| Data do Webinario | {{data_webinario}} |
| Plataforma | {{ferramenta}} |

---

{{#each secoes}}
## {{this.numero}}. {{this.titulo}}

{{this.descricao}}

{{#each this.passos}}
### Passo {{this.numero}}: {{this.titulo}}

{{this.instrucao}}

{{#if this.dica}}
> **Dica:** {{this.dica}}
{{/if}}

{{#if this.alerta}}
> **ATENCAO:** {{this.alerta}}
{{/if}}

{{/each}}

---

{{/each}}

## Checklist de Verificacao

Apos concluir a configuracao, verifique cada item:

{{#each checklist_verificacao}}
- [ ] {{this}}
{{/each}}

---

## Proximos Passos

{{proximos_passos}}

---

## Referencia Metodologica

{{referencia_metodologica}}

---

> Guia gerado por @webinar-operator (Atlas)
> Metodologia: Webinario Infalivel (Taioba) + Perfect Webinar (Brunson)
```

---

## Section Templates by Tool

### EverWebinar Sections

```yaml
secoes_everwebinar:
  - titulo: "Upload e Configuracao de Video"
    passos:
      - "Acessar painel do EverWebinar"
      - "Criar novo webinario"
      - "Upload ou embed do video"
      - "Configurar qualidade e fallback"

  - titulo: "Agendamento e Horarios"
    passos:
      - "Escolher tipo de agendamento (diario/semanal/JIT)"
      - "Definir timezone (America/Sao_Paulo)"
      - "Configurar horarios de sessao"
      - "Ativar one-click registration (se aplicavel)"

  - titulo: "Chat Simulado"
    passos:
      - "Criar lista de mensagens simuladas"
      - "Definir timings sincronizados com roteiro"
      - "Adicionar nomes e avatares"
      - "Testar fluxo do chat"

  - titulo: "Eventos na Timeline"
    passos:
      - "Adicionar enquetes (momento da Abertura)"
      - "Adicionar CTA de compra (momento do Pitch)"
      - "Adicionar alertas de escassez (Fechamento)"
      - "Testar cada evento"

  - titulo: "Replay e Segmentacao"
    passos:
      - "Configurar disponibilidade do replay"
      - "Definir duracao de acesso"
      - "Configurar tags por comportamento"
      - "Testar segmentacao"
```

### SendFlow Sections

```yaml
secoes_sendflow:
  - titulo: "Criacao de Grupos WhatsApp"
    passos:
      - "Criar grupo Fase Pre"
      - "Criar grupo Fase Pos"
      - "Criar grupo Fase Conteudo"
      - "Configurar regras de cada grupo"

  - titulo: "Carregamento de Mensagens"
    passos:
      - "Importar mensagens de nutricao (5)"
      - "Importar mensagens de antecipacao (9)"
      - "Importar mensagens de ampliacao (7)"
      - "Importar mensagens de fechamento (11)"
      - "Importar mensagens de downsell (8)"
      - "Substituir variaveis dinamicas"

  - titulo: "Cronograma de Envio"
    passos:
      - "Definir datas e horarios para cada mensagem"
      - "Configurar fusos horarios"
      - "Agendar envios"

  - titulo: "Triggers e Automacoes"
    passos:
      - "Configurar trigger de entrada"
      - "Configurar triggers de tempo"
      - "Configurar triggers de evento"
      - "Configurar triggers de webhook"

  - titulo: "Deep Links com Pixel"
    passos:
      - "Criar deep links para cada pagina"
      - "Adicionar parametros UTM"
      - "Testar rastreamento"
```

### Payment Webhooks Sections

```yaml
secoes_pagamento:
  - titulo: "Cadastro do Produto"
    passos:
      - "Verificar produto na plataforma"
      - "Configurar checkout"
      - "Definir formas de pagamento"

  - titulo: "Configuracao de Webhooks"
    passos:
      - "Acessar configuracoes de webhook na plataforma"
      - "Adicionar URL do webhook do SendFlow"
      - "Selecionar eventos a monitorar"
      - "Salvar e ativar"

  - titulo: "Acoes Automaticas"
    passos:
      - "Configurar acao para venda aprovada"
      - "Configurar acao para abandono"
      - "Configurar acao para boleto/PIX"
      - "Configurar acao para chargeback/reembolso"

  - titulo: "Teste de Webhooks"
    passos:
      - "Ativar modo sandbox/teste"
      - "Simular cada evento"
      - "Verificar acoes automaticas"
      - "Desativar sandbox apos teste"
```

### Facebook Pixel Sections

```yaml
secoes_pixel:
  - titulo: "Instalacao do Pixel Base"
    passos:
      - "Criar Pixel no Gerenciador de Anuncios"
      - "Copiar codigo do Pixel"
      - "Instalar em todas as paginas"
      - "Verificar com Pixel Helper"

  - titulo: "Eventos por Pagina"
    passos:
      - "Configurar Lead na pagina de captura"
      - "Configurar CompleteRegistration na obrigado"
      - "Configurar ViewContent no webinario"
      - "Configurar InitiateCheckout no checkout"
      - "Configurar Purchase na confirmacao"

  - titulo: "Deep Links e UTMs"
    passos:
      - "Criar deep links para SendFlow"
      - "Adicionar parametros UTM"
      - "Implementar regra anti-duplicacao"
      - "Testar rastreamento end-to-end"

  - titulo: "Audiencias"
    passos:
      - "Criar audiencia de visitantes"
      - "Criar audiencia de leads"
      - "Criar audiencia de compradores"
      - "Criar lookalike de compradores"
```

---

## Usage Notes

1. **Variable Substitution:** Replace all `{{variables}}` with actual values from the webinar context
2. **Section Selection:** Use the appropriate section template based on the tool being configured
3. **Step Detail:** Each step should include specific field names, button locations, and expected results
4. **Screenshots mentais:** Describe what the user should see at each step (since we can't provide actual screenshots)
5. **Cross-reference:** Pull relevant data from other artifacts (roteiro, mensagens, canvases) to populate fields

---

**Template Version:** 1.0.0
**Created:** 2026-03-05
**Part of:** Squad Webinario (@webinar-operator)
