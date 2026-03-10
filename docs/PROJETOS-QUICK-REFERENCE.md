# Guia Rápido — Sistema de Projetos

> **Para:** Usuários finais (não-técnicos)
> **Objetivo:** Referência rápida de comandos e conceitos

---

## Conceitos Básicos

| Conceito | O Que É |
|----------|---------|
| **Projeto** | Um webinário específico (ex: "Curso de Nutrição"). Cada produto/público é um projeto diferente. |
| **Rodada** | Uma execução do webinário (lançamento). Um projeto pode ter rodada 1, 2, 3... |
| **Fase** | Etapa do processo: Planejar → Construir → Executar → Analisar |
| **Artefato** | Documento gerado (canvas, roteiro, mensagens, guias, relatórios) |

---

## Comandos do Maestro (@webinar)

### Gestão de Projetos

| Comando | O Que Faz |
|---------|-----------|
| `*projetos` | Lista todos os seus projetos |
| `*novo-projeto` | Cria um novo webinário (pergunta nome, nicho, produto, ticket) |
| `*mudar-projeto` | Troca para trabalhar em outro webinário |
| `*status` | Mostra progresso completo do projeto atual (todas as fases) |

### Gestão de Rodadas

| Comando | O Que Faz |
|---------|-----------|
| `*rodadas` | Mostra histórico de rodadas (faturamento, leads, vendas de cada lançamento) |
| `*nova-rodada` | Cria rodada 2, 3, etc. (pergunta se quer copiar canvases da rodada anterior) |

### Fases do Webinário

| Comando | O Que Faz | Delega Para |
|---------|-----------|-------------|
| `*planejar` | Fase de planejamento (canvases, avatar, orçamento) | @webinar-strategist |
| `*construir` | Fase de construção (roteiro, mensagens, copy) | @webinar-creator |
| `*executar` | Fase de execução (guias de ferramentas, timeline) | @webinar-operator |
| `*analisar` | Fase de análise (KPIs, diagnóstico, otimização) | @webinar-analyst |

### Outros

| Comando | O Que Faz |
|---------|-----------|
| `*guia` | Explica o processo completo de webinários |
| `*help` | Mostra todos os comandos disponíveis |
| `*migrar` | Migra artefatos antigos para a nova estrutura de projetos |

---

## Fluxo Típico de Trabalho

### Cenário 1: Criar Primeiro Webinário

```
1. @webinar *novo-projeto
   → Nome: "Lançamento Curso de Nutrição"
   → Nicho: "Nutrição e Emagrecimento"
   → Produto: "Curso: Emagreça com Saúde"
   → Ticket: R$ 497

2. *planejar
   → Preencher 6 canvases (30-40 min conversando com @webinar-strategist)

3. *construir
   → Gerar roteiro completo + mensagens + copy (40-60 min)

4. *executar
   → Receber guias de configuração das ferramentas (20-30 min)
   → [VOCÊ EXECUTA O WEBINÁRIO NA VIDA REAL]

5. *analisar
   → Registrar resultados e receber diagnóstico (15-20 min)
```

### Cenário 2: Trabalhar em Múltiplos Projetos

```
DIA 1 — Projeto A
1. @webinar
   → Escolhe "1. Curso de Nutrição"
2. *construir
   → Gera roteiro-abertura.md

DIA 2 — Projeto B
1. @webinar
   → Maestro pergunta: "Quer continuar Curso de Nutrição?" → Não
   → *mudar-projeto
   → Escolhe "2. Workshop de Copywriting"
2. *planejar
   → Gera canvas-produto.md

DIA 3 — Voltar ao Projeto A
1. @webinar
   → *mudar-projeto
   → Escolhe "1. Curso de Nutrição"
2. *status
   → Vê que falta completar roteiro
3. *construir
   → Continua de onde parou
```

### Cenário 3: Fazer Rodada 2 do Mesmo Webinário

```
1. @webinar
   → Seleciona projeto "Curso de Nutrição"

2. *rodadas
   → Vê histórico: Rodada 1 faturou R$29.820

3. *nova-rodada
   → "Quer copiar canvases da Rodada 1?" → Sim
   → Rodada 2 criada com canvases herdados

4. *planejar
   → Revisa canvases herdados (avatar pode ter insights novos)
   → Ajusta orçamento-meta.md (nova meta, novo investimento)

5. *construir
   → Gera roteiro (puxa dados dos canvases ajustados)

6. ... (execução e análise)
```

---

## Perguntas Frequentes (FAQ)

### 1. O que acontece quando abro Claude Code?

**R:** O Maestro (`@webinar`) verifica qual projeto você estava trabalhando e pergunta se quer continuar. Se preferir, pode trocar de projeto.

### 2. Posso ter 10 projetos ao mesmo tempo?

**R:** Sim. Não há limite. Cada projeto fica isolado em sua própria pasta.

### 3. Preciso refazer tudo na rodada 2?

**R:** Não. Você pode copiar os canvases da rodada 1 e só ajustar o que mudou (ex: nova meta de vendas, preço diferente, avatar refinado com dados reais).

### 4. Como sei onde meus arquivos estão?

**R:** Todos os arquivos ficam em `Projetos/{nome-do-projeto}/rodada-{N}/`. Por exemplo:
- `Projetos/curso-nutricao/rodada-1/planejamento/canvas-cliente-ideal.md`
- `Projetos/curso-nutricao/rodada-1/conteudo/roteiro-completo.md`

### 5. O que é o arquivo `projeto.yaml`?

**R:** É um "cartão de visitas" do projeto. Mostra:
- Nome, nicho, produto, ticket
- Histórico de rodadas (faturamento, leads, vendas)
- Progresso de cada fase (quais artefatos já foram gerados)

Você não precisa mexer nele — os agentes gerenciam automaticamente. Mas pode abrir para consultar.

### 6. Posso deletar um projeto antigo?

**R:** Sim. Basta deletar a pasta `Projetos/{nome-do-projeto}/`. Não afeta os outros projetos.

### 7. Como arquivar um projeto?

**R:** Mova a pasta `Projetos/{nome-do-projeto}/` para outra pasta (ex: `Projetos-Arquivados/`). Ou zipar e guardar.

### 8. Posso trabalhar offline?

**R:** Sim, se Claude Code estiver instalado localmente. Mas lembre-se: os agentes precisam gerar texto (LLM), então precisa de conexão para as conversas.

### 9. Como imprimir os artefatos?

**R:** Todos os artefatos são arquivos `.md` (Markdown). Você pode:
- Abrir no VS Code e imprimir (Ctrl+P)
- Converter para PDF usando um conversor markdown
- Copiar o conteúdo e colar no Word/Google Docs

### 10. E se eu esquecer um comando?

**R:** Digite `*help` a qualquer momento. O Maestro lista todos os comandos disponíveis.

---

## Estrutura Visual de Uma Pasta de Projeto

```
Projetos/curso-nutricao/
│
├── projeto.yaml ← "Cartão de visitas" (histórico, progresso)
│
├── rodada-1/ ← Primeira execução
│   ├── planejamento/ ← 6 canvases
│   ├── conteudo/ ← Roteiro + mensagens + copy
│   ├── execucao/ ← Guias de ferramentas
│   └── analise/ ← Relatórios de resultados
│
├── rodada-2/ ← Segunda execução (mesma estrutura)
│   └── ...
│
└── estrategias/ ← Documentos avançados (empilhamento, perpétuo)
```

---

## Legenda de Símbolos (no *status)

| Símbolo | Significado |
|---------|-------------|
| 🟢 | Fase concluída (100%) |
| 🟡 | Fase em andamento (1-99%) |
| ⚪ | Fase pendente (0%) |
| ✅ | Artefato completo |
| ⏸️ | Artefato pendente |
| 📁 | Projeto |
| 💰 | Faturamento |
| 📧 | Leads |
| 🛒 | Vendas |
| 🔄 | Em andamento |

---

## Atalhos e Dicas

### Dica 1: Use *status com frequência
Sempre que retomar um projeto, digite `*status` para ver onde você parou.

### Dica 2: Nomeie projetos de forma clara
Use nomes descritivos:
- ✅ "Lançamento Curso de Nutrição"
- ❌ "Projeto 1"

### Dica 3: Anote insights no projeto.yaml
O campo `notas:` é livre. Adicione manualmente o que quiser:
```yaml
notas: |
  - Rodada 1: Comparecimento baixo (18%) → focar em antecipação na R2
  - Avatar: Mulheres 30-50, frustradas com dietas restritivas
  - Insight: Oferta com garantia de 30 dias aumentou conversão
```

### Dica 4: Herde canvases estrategicamente
Na rodada 2, copie os canvases mas ajuste com dados reais:
- Avatar: adicione insights de quem comprou na R1
- Orçamento: use CPL real da R1 como base
- Canvas do Webinário: refine objeções baseado em feedback real

### Dica 5: Use pastas de projeto para backups
Cada projeto é uma pasta isolada. Faça backup copiando:
```
Projetos/curso-nutricao/ → Google Drive / Dropbox / USB
```

---

## Comandos por Situação

| Situação | Comando |
|----------|---------|
| Primeira vez usando o sistema | `@webinar *novo-projeto` |
| Não lembro qual projeto estava trabalhando | `@webinar` (ele mostra lista) |
| Quero ver meu progresso | `*status` |
| Quero criar rodada 2 | `*nova-rodada` |
| Fiquei perdido | `*guia` (explica o processo todo) |
| Não sei o que fazer agora | `*status` + ver "Próxima ação sugerida" |
| Quero trabalhar em outro webinário | `*mudar-projeto` |
| Quero ver quanto faturei em cada rodada | `*rodadas` |
| Tenho arquivos antigos (antes do sistema de projetos) | `*migrar` |

---

## Exemplo Real de Conversa

```
Você: @webinar

Maestro:
Você tem 2 projetos:

1. 📁 Curso de Nutrição (Rodada 2 - Construção 45%)
2. 📁 Workshop de Copywriting (Rodada 1 concluída)

Qual você quer trabalhar? Digite o número ou 'novo'.

Você: 1

Maestro:
Projeto ativo: Curso de Nutrição (Rodada 2)

📊 Status:
- ✅ Planejamento: 100%
- 🟡 Construção: 45% (falta roteiro completo + mensagens)
- ⏸️ Execução: Aguardando
- ⏸️ Análise: Aguardando

O que você quer fazer?
- Continuar construindo → *construir
- Ver progresso detalhado → *status
- Todas as opções → *help

Você: *construir

Maestro:
Delegando para @webinar-creator (Spark)...

@webinar-creator:
Olá! Vejo que você já tem roteiro de abertura e empatia prontos.

O que você quer fazer agora?
- Roteiro de conteúdo (3 secrets) → *conteudo
- Roteiro de pitch/oferta → *pitch
- Consolidar roteiro completo → *roteiro
- Gerar mensagens WhatsApp → *mensagens

Você: *conteudo

@webinar-creator:
Vou construir a seção de Conteúdo (3 Secrets) do seu webinário.

Vou usar os dados do seu Avatar Blueprint e do Canvas do Webinário.

[... conversa interativa para gerar o roteiro ...]

@webinar-creator:
✅ Roteiro de Conteúdo gerado!

Salvo em:
Projetos/curso-nutricao/rodada-2/conteudo/roteiro-conteudo.md

Progresso: Construção 60% completa (5 de 9 artefatos)

Próximo: *pitch para gerar a seção de oferta.
```

---

## Resumo em 3 Frases

1. **Cada webinário = 1 projeto** (pasta própria em `Projetos/`)
2. **Cada projeto pode ter múltiplas rodadas** (rodada-1, rodada-2...)
3. **O Maestro pergunta qual projeto você quer trabalhar** no início

**Resultado:** Você gerencia vários webinários sem confusão, reutiliza artefatos entre rodadas e mantém histórico de resultados.

---

## Contato e Suporte

**Dúvidas?**
- Digite `*help` a qualquer momento
- Pergunte ao Maestro: `@webinar` e descreva sua dúvida

**Documentação completa:**
- Resumo Executivo: `docs/PROJETOS-RESUMO-EXECUTIVO.md`
- Arquitetura: `docs/PROJETOS-ARCHITECTURE.md`
- Diagramas: `docs/PROJETOS-DIAGRAMS.md`

---

*@architect (Aria) — Guia Rápido — 2026-03-05*
