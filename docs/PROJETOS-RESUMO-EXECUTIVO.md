# Resumo Executivo — Sistema de Projetos

> **Para:** Owner (não-técnico)
> **Assunto:** Nova estrutura de organização de webinários
> **Data:** 2026-03-05

---

## O Que Muda?

### Antes
```
docs/webinar/
└── rodada-1/
    ├── planejamento/
    ├── conteudo/
    ├── execucao/
    └── analise/
```
**Problema:** Só dá para trabalhar em um webinário por vez. Se você tem "Curso de Nutrição" + "Workshop de Copywriting", os arquivos ficam misturados.

### Agora
```
Projetos/
├── curso-nutricao/
│   ├── rodada-1/
│   ├── rodada-2/
│   └── projeto.yaml
└── workshop-copywriting/
    ├── rodada-1/
    └── projeto.yaml
```
**Solução:** Cada webinário tem sua própria pasta. Cada projeto pode ter múltiplas rodadas (lançamentos).

---

## Como Funciona na Prática?

### 1. Começar a Conversa

```
Você: @webinar

Maestro:
Você tem 3 projetos:

1. 📁 Curso de Nutrição (Rodada 2 - 45% completa)
2. 📁 Workshop de Copywriting (Rodada 1 concluída)
3. 📁 Infoproduto de Finanças (Novo)

Qual você quer trabalhar? Digite o número.

Você: 1

Maestro:
Ativado: Curso de Nutrição (Rodada 2)
O que você quer fazer? Digite *construir, *status ou *help
```

### 2. Criar Novo Projeto

```
Você: @webinar *novo-projeto

Maestro: Qual o nome do projeto?
Você: Webinário de Vendas B2B

Maestro: Qual o nicho?
Você: Vendas e Negócios

Maestro: Qual o produto?
Você: Consultoria de Vendas Consultivas

Maestro: Qual o valor (R$)?
Você: 2997

Maestro:
✅ Projeto criado!
📁 Webinário de Vendas B2B
   Produto: Consultoria de Vendas Consultivas
   Valor: R$ 2.997
   Rodada: 1

Digite *planejar para começar.
```

### 3. Fazer Rodada 2 do Mesmo Webinário

```
Você: @webinar *nova-rodada

Maestro:
Criar Rodada 2 do projeto "Curso de Nutrição".

Quer copiar os canvases de planejamento da Rodada 1?
(Avatar, Cliente Ideal, Produto, etc.)

Sim ou Não?

Você: Sim

Maestro:
✅ Rodada 2 criada!
Canvases copiados da Rodada 1.

Você pode ajustá-los com os aprendizados do lançamento anterior.
Digite *planejar para revisar os canvases.
```

---

## O Que Você Ganha?

| Antes | Agora |
|-------|-------|
| Só 1 webinário por vez | Quantos webinários você quiser |
| Refazer tudo do zero na rodada 2 | Reaproveitar canvases da rodada anterior |
| Arquivos misturados | Cada projeto isolado em sua pasta |
| Sem histórico de resultados | `projeto.yaml` registra faturamento de todas as rodadas |

---

## Comandos Novos do Maestro

| Comando | O Que Faz |
|---------|-----------|
| `*projetos` | Lista todos os seus projetos |
| `*novo-projeto` | Cria um novo webinário |
| `*rodadas` | Mostra histórico de rodadas do projeto atual |
| `*nova-rodada` | Cria rodada 2, 3, etc. |
| `*mudar-projeto` | Troca para trabalhar em outro webinário |
| `*status` | Mostra progresso completo (Planejamento, Construção, Execução, Análise) |

**Os comandos antigos continuam funcionando:**
- `*planejar` → @webinar-strategist
- `*construir` → @webinar-creator
- `*executar` → @webinar-operator
- `*analisar` → @webinar-analyst
- `*guia` → Explicação completa
- `*help` → Ajuda

---

## Exemplo Real de Uso

### Cenário: Você tem 2 webinários

**Webinário A:** "Curso de Nutrição"
- Rodada 1: faturou R$29.800 (concluída)
- Rodada 2: em andamento (construindo roteiro)

**Webinário B:** "Workshop de Copywriting"
- Rodada 1: concluída, faturou R$15.400
- Quer fazer rodada 2 agora

### Fluxo de Trabalho

**Segunda-feira:** Trabalhar no Curso de Nutrição (Rodada 2)
```
@webinar → escolhe "1" → *construir → gera roteiro
```

**Terça-feira:** Trabalhar no Workshop de Copywriting (Rodada 2)
```
@webinar → *mudar-projeto → escolhe "2" → *nova-rodada → *planejar
```

**Quarta-feira:** Voltar ao Curso de Nutrição
```
@webinar → (Maestro pergunta se quer continuar Workshop) → "Não" → escolhe "1"
```

**Tudo organizado. Sem confusão.**

---

## O Que NÃO Muda?

✅ Você ainda conversa com os agentes em português, do mesmo jeito
✅ Os agentes ainda fazem perguntas e geram documentos markdown
✅ Nada de código, tudo intuitivo
✅ Os artefatos continuam legíveis e imprimíveis
✅ A metodologia (canvases, roteiro, funil) continua a mesma

**Só muda a organização:** Agora cada webinário tem sua própria "gaveta" (pasta).

---

## Estrutura de Uma Pasta de Projeto

```
Projetos/curso-nutricao/
│
├── projeto.yaml                    # Informações do projeto (nome, produto, rodadas)
│
├── rodada-1/                       # Primeira execução
│   ├── planejamento/
│   │   ├── canvas-cliente-ideal.md
│   │   ├── canvas-produto.md
│   │   ├── avatar-blueprint.md
│   │   └── ...
│   ├── conteudo/
│   │   ├── roteiro-completo.md
│   │   ├── mensagens-whatsapp.md
│   │   └── ...
│   ├── execucao/
│   │   ├── timeline-campanha.md
│   │   └── ...
│   └── analise/
│       ├── relatorio-kpis.md
│       └── ...
│
├── rodada-2/                       # Segunda execução
│   └── (mesma estrutura)
│
└── estrategias/                    # Documentos que valem para todas as rodadas
    ├── estrategia-empilhamento.md
    └── estrategia-perpetuo.md
```

**Tudo do webinário fica em um só lugar.** Fácil de compartilhar, arquivar ou imprimir.

---

## O Que o `projeto.yaml` Guarda?

Exemplo:

```yaml
nome: "Lançamento Curso de Nutrição"
nicho: "Nutrição e Emagrecimento"
produto: "Curso Online: Emagreça com Saúde"
ticket: 497.00

rodadas:
  - numero: 1
    status: "Done"
    data_webinario: "2026-01-15"
    faturamento: 29820.00
    leads: 1850
    vendas: 60

  - numero: 2
    status: "InProgress"
    data_webinario: "2026-04-10"

rodada_ativa: 2

fases:
  planejamento:
    status: "Completed"
    artefatos_completos: [todos os 6 canvases]

  construcao:
    status: "InProgress"
    artefatos_completos: [roteiro-abertura, roteiro-empatia]
    artefatos_pendentes: [roteiro-conteudo, roteiro-pitch, ...]
```

**É como um "cartão de visitas" do projeto:** mostra tudo que foi feito e o que falta.

---

## Próximos Passos (Técnicos)

### Para Implementação

1. **@architect** cria os templates (projeto.yaml, etc.)
2. **@squad-creator** atualiza o agente Maestro com os comandos novos
3. **@dev** implementa as tasks (criar-projeto, selecionar-projeto, criar-rodada)
4. **@dev** atualiza os 4 agentes especializados (Strategist, Creator, Operator, Analyst)
5. **@qa** testa o fluxo completo com múltiplos projetos e rodadas

### Se Você Já Tem Artefatos na Estrutura Antiga

O Maestro vai detectar e oferecer migração:

```
Maestro:
Detectei artefatos em docs/webinar/rodada-1/.
Quer migrar para o novo sistema de projetos?

Você: Sim

Maestro: Qual o nome do projeto?

Você: Meu Primeiro Webinário

Maestro:
✅ Migrado!
Artefatos movidos para: Projetos/meu-primeiro-webinario/rodada-1/
```

---

## Perguntas Frequentes

### 1. Posso trabalhar em vários projetos no mesmo dia?
**Sim.** Use `*mudar-projeto` para trocar. O sistema lembra onde você parou em cada um.

### 2. Preciso refazer tudo na rodada 2?
**Não.** Você pode copiar os canvases da rodada 1 e só ajustar o que mudou (ex: preço, oferta, avatar refinado).

### 3. E se eu quiser arquivar um projeto antigo?
**Fácil.** A pasta `Projetos/{nome}/` é independente. Você pode mover para outro lugar, zipar ou deletar sem afetar os outros.

### 4. Os comandos dos agentes mudaram?
**Não.** `*canvas-cliente`, `*roteiro`, `*mensagens`, `*kpis` — tudo igual. Só o Maestro (`@webinar`) ganhou comandos novos de gestão de projetos.

### 5. Preciso entender o arquivo `projeto.yaml`?
**Não.** Os agentes gerenciam ele automaticamente. Mas se você quiser ver o histórico de rodadas (faturamento, leads, vendas), pode abrir e ler — é legível.

---

## Resumo em 3 Frases

1. **Cada webinário tem sua própria pasta** dentro de `Projetos/`
2. **Cada projeto pode ter múltiplas rodadas** (rodada-1, rodada-2, rodada-3...)
3. **O Maestro pergunta qual projeto você quer trabalhar** no início de cada conversa

**Resultado:** Você pode gerenciar 5, 10, 20 webinários diferentes sem confusão. Cada um organizado, com histórico e reutilização de artefatos entre rodadas.

---

**Dúvidas? Pergunte ao Maestro (`@webinar`) digitando `*help`.**

*@architect (Aria) — Resumo Executivo — 2026-03-05*
