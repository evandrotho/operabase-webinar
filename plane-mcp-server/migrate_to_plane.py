"""
Migrate Webinario project structure to Plane.so [OPERA] Operabase AI.
Creates 46 work items, assigns to modules, with correct states, labels, and dates.
"""

import httpx
import json
import time
import sys

API_BASE = "https://plane.operabase.io/api/v1/workspaces/operabaseai"
API_KEY = "plane_api_0360d1de894a475f909cfccd8451ec8d"
PROJECT_ID = "e191f747-0b7a-4163-af52-df237123d35c"

HEADERS = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json",
}

# State IDs
STATES = {
    "backlog": "35f8c95e-030e-40a6-9a78-c3851f60e747",
    "todo": "8ec37452-466d-4080-ad3c-c06379b1e32b",
    "in_progress": "cb194a70-d267-40c2-85f8-89025d2b829b",
    "done": "3903dd89-ba34-401e-b252-4384fdebd4cc",
}

# Label IDs
LABELS = {
    "planejamento": "af3b5deb-49dd-4854-9ab6-872461be9c6e",
    "construcao": "616a95f5-1447-4ac7-a498-c7524f798801",
    "execucao": "31892d8e-0f78-424c-9cfb-498d991cae48",
    "analise": "e34763b7-c70d-4989-96bb-6e1d52c52232",
    "estrategia": "83df1668-9f58-43f5-8cc0-d02c467ecb44",
    "artefato": "425ed01e-ed22-4c09-b9a6-487d0d6ae7a1",
    "milestone": "6ab3a315-4672-4143-ab47-83c2c6c501f0",
    "setup_guide": "d4d0396b-b7e3-4403-b368-67f091cd9a36",
    "checklist": "ef3898f3-7a26-4ec1-a730-0ec2cc77878d",
}

# Module IDs
MODULES = {
    "planejamento": "1f8fc2d1-7155-4589-a27c-b3b24509eff5",
    "construcao": "d28b0c39-5477-489d-8243-b6da6152d894",
    "execucao": "4ed7600d-cda2-448a-a785-6187277456f8",
    "analise": "4c46aa43-349e-4c3d-9ac1-890e05297b3d",
    "checklist": "547515c3-d4ce-4cc8-bd6a-222101c86559",
}

# ============================================================
# WORK ITEMS DEFINITION
# ============================================================

ITEMS = [
    # --- PLANEJAMENTO (6 items, all Done) ---
    {
        "name": "Canvas do Cliente Ideal (9 perguntas)",
        "description_html": "<p><strong>Agente:</strong> @webinar-strategist (Sage)</p><p><strong>Comando:</strong> <code>*canvas-cliente</code></p><p><strong>Artefato:</strong> <code>rodada-1/planejamento/canvas-cliente-ideal.md</code></p><p>9 perguntas interativas para mapear o cliente ideal: dor principal, desejo secreto, objecoes, linguagem, canais, momento de compra.</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["planejamento"], LABELS["artefato"]],
        "start_date": "2026-03-05",
        "target_date": "2026-03-05",
        "module": "planejamento",
    },
    {
        "name": "Canvas do Produto (7 blocos)",
        "description_html": "<p><strong>Agente:</strong> @webinar-strategist (Sage)</p><p><strong>Comando:</strong> <code>*canvas-produto</code></p><p><strong>Artefato:</strong> <code>rodada-1/planejamento/canvas-produto.md</code></p><p>7 blocos: Grande Promessa, Mecanismo Unico, Produto Principal, Formato de Entrega, Garantia, Ticket R$2.500, Bonus.</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["planejamento"], LABELS["artefato"]],
        "start_date": "2026-03-05",
        "target_date": "2026-03-05",
        "module": "planejamento",
    },
    {
        "name": "Avatar Blueprint (7 perguntas + Problema x Solucao)",
        "description_html": "<p><strong>Agente:</strong> @webinar-strategist (Sage)</p><p><strong>Comando:</strong> <code>*avatar</code></p><p><strong>Artefato:</strong> <code>rodada-1/planejamento/avatar-blueprint.md</code></p><p>7 perguntas sobre o avatar + tabela Problema x Solucao. Input critico para quase todas as tasks de construcao.</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["planejamento"], LABELS["artefato"]],
        "start_date": "2026-03-05",
        "target_date": "2026-03-05",
        "module": "planejamento",
    },
    {
        "name": "Canvas do Webinario Infalivel (15 blocos)",
        "description_html": "<p><strong>Agente:</strong> @webinar-strategist (Sage)</p><p><strong>Comando:</strong> <code>*canvas-webinar</code></p><p><strong>Artefato:</strong> <code>rodada-1/planejamento/canvas-webinar.md</code></p><p>15 blocos: crenca-alvo, ponte de crencas, 3 segredos, falsas crencas, stack slide, oferta irresistivel, bonus, garantia, escassez.</p><p><strong>Dependencias:</strong> canvas-produto.md, avatar-blueprint.md</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["planejamento"], LABELS["artefato"]],
        "start_date": "2026-03-05",
        "target_date": "2026-03-05",
        "module": "planejamento",
    },
    {
        "name": "Orcamento e Meta (12 premissas)",
        "description_html": "<p><strong>Agente:</strong> @webinar-strategist (Sage)</p><p><strong>Comando:</strong> <code>*orcamento</code></p><p><strong>Artefato:</strong> <code>rodada-1/planejamento/orcamento-meta.md</code></p><p>12 premissas: investimento R$3.000, CPL R$20, meta 150 leads, ticket R$2.500, taxa de conversao 3%, ROAS esperado 3.75x.</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["planejamento"], LABELS["artefato"]],
        "start_date": "2026-03-05",
        "target_date": "2026-03-05",
        "module": "planejamento",
    },
    {
        "name": "Resumo Consolidado do Planejamento",
        "description_html": "<p><strong>Agente:</strong> @webinar-strategist (Sage)</p><p><strong>Comando:</strong> <code>*resumo</code></p><p><strong>Artefato:</strong> <code>rodada-1/planejamento/planejamento-resumo.md</code></p><p>Consolidacao de todos os 4 canvases + avatar em relatorio executivo.</p><p><strong>Dependencias:</strong> Todos os 5 artefatos anteriores.</p>",
        "state": STATES["done"],
        "priority": "medium",
        "labels": [LABELS["planejamento"], LABELS["artefato"]],
        "start_date": "2026-03-05",
        "target_date": "2026-03-05",
        "module": "planejamento",
    },

    # --- CONSTRUCAO DE CONTEUDO (9 items, all Done) ---
    {
        "name": "Roteiro de Abertura (7 blocos + Origin Story)",
        "description_html": "<p><strong>Agente:</strong> @webinar-creator (Spark)</p><p><strong>Comando:</strong> <code>*abertura</code></p><p><strong>Artefato:</strong> <code>rodada-1/conteudo/roteiro-abertura.md</code></p><p>7 blocos da abertura do webinario + One Thing + Origin Story (metodo Brunson). Primeiros 15 min.</p><p><strong>Dependencias:</strong> avatar-blueprint.md, canvas-produto.md</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["construcao"], LABELS["artefato"]],
        "start_date": "2026-03-05",
        "target_date": "2026-03-05",
        "module": "construcao",
    },
    {
        "name": "Roteiro de Empatia (Epiphany Bridge)",
        "description_html": "<p><strong>Agente:</strong> @webinar-creator (Spark)</p><p><strong>Comando:</strong> <code>*empatia</code></p><p><strong>Artefato:</strong> <code>rodada-1/conteudo/roteiro-empatia.md</code></p><p>Secao de empatia: 2 modelos de historia + Epiphany Bridge (Brunson). Min 15-25.</p><p><strong>Dependencias:</strong> avatar-blueprint.md</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["construcao"], LABELS["artefato"]],
        "start_date": "2026-03-05",
        "target_date": "2026-03-05",
        "module": "construcao",
    },
    {
        "name": "Roteiro de Conteudo (3 Segredos + Falsas Crencas)",
        "description_html": "<p><strong>Agente:</strong> @webinar-creator (Spark)</p><p><strong>Comando:</strong> <code>*conteudo</code></p><p><strong>Artefato:</strong> <code>rodada-1/conteudo/roteiro-conteudo.md</code></p><p>3 Segredos que quebram falsas crencas do avatar. Min 25-50. Corpo principal do webinario.</p><p><strong>Dependencias:</strong> avatar-blueprint.md, canvas-webinar.md (blocos 10-11)</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["construcao"], LABELS["artefato"]],
        "start_date": "2026-03-05",
        "target_date": "2026-03-05",
        "module": "construcao",
    },
    {
        "name": "Roteiro de Pitch (15 passos + Stack Slide)",
        "description_html": "<p><strong>Agente:</strong> @webinar-creator (Spark)</p><p><strong>Comando:</strong> <code>*pitch</code></p><p><strong>Artefato:</strong> <code>rodada-1/conteudo/roteiro-pitch.md</code></p><p>15 passos da oferta irresistivel + Stack Slide. Min 50-75. Fechamento do webinario.</p><p><strong>Dependencias:</strong> canvas-webinar.md (blocos 12-15), canvas-produto.md</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["construcao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "construcao",
    },
    {
        "name": "Roteiro Completo Consolidado (60-90min)",
        "description_html": "<p><strong>Agente:</strong> @webinar-creator (Spark)</p><p><strong>Comando:</strong> <code>*roteiro</code></p><p><strong>Artefato:</strong> <code>rodada-1/conteudo/roteiro-completo.md</code></p><p>Roteiro completo do webinario com timeline minuto-a-minuto. 60-90 minutos.</p><p><strong>Dependencias:</strong> abertura + empatia + conteudo + pitch</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["construcao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "construcao",
    },
    {
        "name": "Mensagens WhatsApp (33 templates por fase)",
        "description_html": "<p><strong>Agente:</strong> @webinar-creator (Spark)</p><p><strong>Comando:</strong> <code>*mensagens</code></p><p><strong>Artefato:</strong> <code>rodada-1/conteudo/mensagens-whatsapp.md</code></p><p>33 mensagens organizadas por fase: 5 nutricao, 9 antecipacao, 1 pos-webinario, 7 ampliacao, 11 fechamento.</p><p><strong>Dependencias:</strong> canvas-produto.md, avatar-blueprint.md</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["construcao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "construcao",
    },
    {
        "name": "Copy Pagina de Captura",
        "description_html": "<p><strong>Agente:</strong> @webinar-creator (Spark)</p><p><strong>Comando:</strong> <code>*copy-captura</code></p><p><strong>Artefato:</strong> <code>rodada-1/conteudo/copy-pagina-captura.md</code></p><p>Copy da landing page de captura em 2 formatos (longa e curta).</p><p><strong>Dependencias:</strong> canvas-produto.md, avatar-blueprint.md</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["construcao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "construcao",
    },
    {
        "name": "Copy Pagina de Replay",
        "description_html": "<p><strong>Agente:</strong> @webinar-creator (Spark)</p><p><strong>Comando:</strong> <code>*copy-replay</code></p><p><strong>Artefato:</strong> <code>rodada-1/conteudo/copy-pagina-replay.md</code></p><p>Copy da pagina de replay com delay de 55min na oferta.</p><p><strong>Dependencias:</strong> roteiro-completo.md, canvas-webinar.md</p>",
        "state": STATES["done"],
        "priority": "medium",
        "labels": [LABELS["construcao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "construcao",
    },
    {
        "name": "Copy Pagina de Fechamento",
        "description_html": "<p><strong>Agente:</strong> @webinar-creator (Spark)</p><p><strong>Comando:</strong> <code>*copy-fechamento</code></p><p><strong>Artefato:</strong> <code>rodada-1/conteudo/copy-pagina-fechamento.md</code></p><p>Copy da pagina de fechamento com urgencia e escassez.</p><p><strong>Dependencias:</strong> canvas-webinar.md (blocos 12-15), canvas-produto.md</p>",
        "state": STATES["done"],
        "priority": "medium",
        "labels": [LABELS["construcao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "construcao",
    },

    # --- EXECUCAO DA CAMPANHA (11 items) ---
    {
        "name": "Timeline da Campanha (06/03 a 15/03)",
        "description_html": "<p><strong>Agente:</strong> @webinar-operator (Atlas)</p><p><strong>Comando:</strong> <code>*timeline</code></p><p><strong>Artefato:</strong> <code>rodada-1/execucao/timeline-campanha.md</code></p><p>Cronograma dia-a-dia: 6 fases, 33 msgs WhatsApp, marcos e checkpoints. Periodo: D-4 (06/03) a D+5 (15/03).</p>",
        "state": STATES["done"],
        "priority": "urgent",
        "labels": [LABELS["execucao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "execucao",
    },
    {
        "name": "Funil de 7 Etapas",
        "description_html": "<p><strong>Agente:</strong> @webinar-operator (Atlas)</p><p><strong>Comando:</strong> <code>*funil</code></p><p><strong>Artefato:</strong> <code>rodada-1/execucao/funil-7-etapas.md</code></p><p>Visualizacao do funil completo: Captacao > Nutricao > Antecipacao > Abertura > Ampliacao > Fechamento > Impulsionamento.</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["execucao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "execucao",
    },
    {
        "name": "Checklist de Lancamento",
        "description_html": "<p><strong>Agente:</strong> @webinar-operator (Atlas)</p><p><strong>Comando:</strong> <code>*checklist</code></p><p><strong>Artefato:</strong> <code>rodada-1/execucao/checklist-lancamento.md</code></p><p>Checklist completo de pre-lancamento. Os 14 items individuais estao no modulo 'Checklist Pre-Lancamento'.</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["execucao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "execucao",
    },
    {
        "name": "Agenda Completa da Campanha",
        "description_html": "<p><strong>Agente:</strong> @webinar-operator (Atlas)</p><p><strong>Artefato:</strong> <code>rodada-1/execucao/agenda-completa.md</code></p><p>Agenda detalhada com todas as acoes por dia e horario.</p>",
        "state": STATES["done"],
        "priority": "high",
        "labels": [LABELS["execucao"], LABELS["artefato"]],
        "start_date": "2026-03-06",
        "target_date": "2026-03-06",
        "module": "execucao",
    },
    {
        "name": "Guia de Setup: EverWebinar",
        "description_html": "<p><strong>Agente:</strong> @webinar-operator (Atlas)</p><p><strong>Comando:</strong> <code>*setup-everwebinar</code></p><p>Guia passo-a-passo para configurar o webinario no EverWebinar: upload do video, agendamento, configuracao do chat simulado, pagina de registro.</p><p><strong>Dependencias:</strong> roteiro-completo.md, copy-pagina-captura.md</p>",
        "state": STATES["todo"],
        "priority": "high",
        "labels": [LABELS["execucao"], LABELS["setup_guide"]],
        "target_date": "2026-03-08",
        "module": "execucao",
    },
    {
        "name": "Guia de Setup: SendFlow",
        "description_html": "<p><strong>Agente:</strong> @webinar-operator (Atlas)</p><p><strong>Comando:</strong> <code>*setup-sendflow</code></p><p>Guia para configurar automacao WhatsApp no SendFlow: criar grupos, agendar 33 mensagens, configurar segmentacao por fase, automacao de boas-vindas.</p><p><strong>Dependencias:</strong> mensagens-whatsapp.md</p>",
        "state": STATES["todo"],
        "priority": "high",
        "labels": [LABELS["execucao"], LABELS["setup_guide"]],
        "target_date": "2026-03-08",
        "module": "execucao",
    },
    {
        "name": "Guia de Setup: Pagamento (Webhook)",
        "description_html": "<p><strong>Agente:</strong> @webinar-operator (Atlas)</p><p><strong>Comando:</strong> <code>*setup-pagamento</code></p><p>Guia para configurar webhooks de pagamento (Zouti, Hotmart ou Kiwify): checkout, confirmacao, integracao com SendFlow para parar msgs de venda.</p><p><strong>Dependencias:</strong> canvas-produto.md (ticket, condicoes)</p>",
        "state": STATES["todo"],
        "priority": "high",
        "labels": [LABELS["execucao"], LABELS["setup_guide"]],
        "target_date": "2026-03-08",
        "module": "execucao",
    },
    {
        "name": "Guia de Setup: Facebook Pixel",
        "description_html": "<p><strong>Agente:</strong> @webinar-operator (Atlas)</p><p><strong>Comando:</strong> <code>*setup-pixel</code></p><p>Guia para instalar e configurar o Facebook Pixel: eventos de conversao (Lead, ViewContent, Purchase), integracao com paginas de captura/replay/checkout.</p>",
        "state": STATES["todo"],
        "priority": "high",
        "labels": [LABELS["execucao"], LABELS["setup_guide"]],
        "target_date": "2026-03-08",
        "module": "execucao",
    },
    {
        "name": "MARCO: Ativar Anuncios Facebook/Instagram",
        "description_html": "<p><strong>Data:</strong> 06/03/2026 (HOJE) as 08:00</p><p><strong>Acoes:</strong></p><ul><li>Ativar campanha Facebook Ads (captacao) — Budget R$3.000/semana</li><li>Ativar campanha Instagram Ads (mesmos criativos)</li><li>Publicar post organico (teaser)</li><li>Pagina de captura ATIVA com pixel e redirect para grupo WhatsApp</li></ul><p><strong>Meta:</strong> CPL &lt;= R$20, 150 leads em 5 dias</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["execucao"], LABELS["milestone"]],
        "target_date": "2026-03-06",
        "module": "execucao",
    },
    {
        "name": "MARCO: Webinario Ao Vivo (Terca 20h)",
        "description_html": "<p><strong>Data:</strong> 10/03/2026 (Terca-feira) as 20:00</p><p><strong>Acoes:</strong></p><ul><li>Entrar no Zoom 15min antes</li><li>Monitorar chat e presenca</li><li>Abrir checkout no min 62 (~21:00)</li><li>Bonus Acao Rapida — Mentoria (3 vagas)</li><li>Encerrar ~21:30</li><li>Enviar MSG-POS-01 as 22:00</li></ul><p><strong>Produto:</strong> OperaBase R$2.500 | Meta: 4-5 vendas</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["execucao"], LABELS["milestone"]],
        "target_date": "2026-03-10",
        "module": "execucao",
    },
    {
        "name": "MARCO: Fechamento do Carrinho (23:59)",
        "description_html": "<p><strong>Data:</strong> 15/03/2026 (Domingo) as 23:59</p><p><strong>Acoes:</strong></p><ul><li>11 mensagens de fechamento ao longo do dia (08h ate 23:45)</li><li>Sequencia: resumo oferta > depoimento > bonus expira > FAQ > prova social > garantia > 4h > 3h > 2h > 1h > 15min</li><li>As 23:59: desativar checkout e remover TODOS os links de compra</li></ul><p><strong>Pico 2 de vendas esperado:</strong> 20:00-23:59</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["execucao"], LABELS["milestone"]],
        "target_date": "2026-03-15",
        "module": "execucao",
    },

    # --- ANALISE POS-WEBINARIO (6 items) ---
    {
        "name": "Relatorio de KPIs (CPL, presenca, vendas, ROAS)",
        "description_html": "<p><strong>Agente:</strong> @webinar-analyst (Lens)</p><p><strong>Comando:</strong> <code>*kpis</code></p><p>Registrar e analisar KPIs da campanha: CPL real, total de leads, taxa de presenca, taxa de conversao, faturamento, ROAS.</p><p><strong>Dependencias:</strong> orcamento-meta.md + dados reais pos-campanha</p>",
        "state": STATES["backlog"],
        "priority": "high",
        "labels": [LABELS["analise"], LABELS["artefato"]],
        "target_date": "2026-03-16",
        "module": "analise",
    },
    {
        "name": "Diagnostico do Funil (gargalos)",
        "description_html": "<p><strong>Agente:</strong> @webinar-analyst (Lens)</p><p><strong>Comando:</strong> <code>*diagnostico</code></p><p>Identificar onde o funil esta perdendo mais pessoas: captacao? presenca? engagement? conversao?</p><p><strong>Dependencias:</strong> relatorio-kpis.md, funil-7-etapas.md</p>",
        "state": STATES["backlog"],
        "priority": "high",
        "labels": [LABELS["analise"], LABELS["artefato"]],
        "target_date": "2026-03-17",
        "module": "analise",
    },
    {
        "name": "Orcado vs Realizado",
        "description_html": "<p><strong>Agente:</strong> @webinar-analyst (Lens)</p><p><strong>Comando:</strong> <code>*orcado-vs-realizado</code></p><p>Comparar premissas do orcamento com resultados reais. Identificar desvios e causas.</p><p><strong>Dependencias:</strong> orcamento-meta.md, relatorio-kpis.md</p>",
        "state": STATES["backlog"],
        "priority": "medium",
        "labels": [LABELS["analise"], LABELS["artefato"]],
        "target_date": "2026-03-17",
        "module": "analise",
    },
    {
        "name": "Plano da Proxima Rodada",
        "description_html": "<p><strong>Agente:</strong> @webinar-analyst (Lens)</p><p><strong>Comando:</strong> <code>*proxima-rodada</code></p><p>Definir otimizacoes para rodada 2: ajustes no roteiro, novas mensagens, mudancas no funil, budget ajustado.</p><p><strong>Dependencias:</strong> diagnostico-funil.md + todos os canvases</p>",
        "state": STATES["backlog"],
        "priority": "medium",
        "labels": [LABELS["analise"], LABELS["artefato"]],
        "target_date": "2026-03-18",
        "module": "analise",
    },
    {
        "name": "Estrategia de Empilhamento de Funis",
        "description_html": "<p><strong>Agente:</strong> @webinar-analyst (Lens)</p><p><strong>Comando:</strong> <code>*empilhamento</code></p><p>Planejar empilhamento: como conectar webinario com VSL, mini-webinario, ou outros funis para maximizar LTV.</p><p><strong>Dependencias:</strong> relatorio-kpis.md</p>",
        "state": STATES["backlog"],
        "priority": "low",
        "labels": [LABELS["estrategia"], LABELS["artefato"]],
        "target_date": "2026-03-20",
        "module": "analise",
    },
    {
        "name": "Estrategia de Perpetuo/Evergreen",
        "description_html": "<p><strong>Agente:</strong> @webinar-analyst (Lens)</p><p><strong>Comando:</strong> <code>*perpetuo</code></p><p>Planejar conversao para modelo evergreen: EverWebinar automatizado, funil continuo, otimizacao sem dependencia de lancamento.</p><p><strong>Dependencias:</strong> roteiro-completo.md, relatorio-kpis.md</p>",
        "state": STATES["backlog"],
        "priority": "low",
        "labels": [LABELS["estrategia"], LABELS["artefato"]],
        "target_date": "2026-03-20",
        "module": "analise",
    },

    # --- CHECKLIST PRE-LANCAMENTO (14 items, deadline 09/03) ---
    {
        "name": "Pagina de captura ativa e testada",
        "description_html": "<p><strong>Verificar:</strong> Landing page esta online, formulario funciona, redirect para grupo WhatsApp esta correto.</p><p><strong>URL:</strong> {{link}} (definir antes do lancamento)</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Pixel do Facebook instalado e disparando",
        "description_html": "<p><strong>Verificar:</strong> Pixel instalado na pagina de captura, replay e checkout. Eventos: PageView, Lead, ViewContent, Purchase.</p><p>Testar com Facebook Pixel Helper (extensao Chrome).</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Criativos dos anuncios aprovados",
        "description_html": "<p><strong>Verificar:</strong> Criativos de Facebook e Instagram Ads aprovados pela plataforma. Sem rejeicoes ou restricoes.</p><p>Formatos: Feed, Stories, Reels. Foco na headline do webinario.</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Grupo/lista WhatsApp criado no SendFlow",
        "description_html": "<p><strong>Verificar:</strong> Grupo ou lista de broadcast criado no SendFlow para receber inscritos automaticamente.</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Automacao de boas-vindas configurada (MSG-NUT-01)",
        "description_html": "<p><strong>Verificar:</strong> Mensagem automatica de boas-vindas (MSG-NUT-01) configurada no SendFlow para disparar no momento da inscricao.</p><p>Testar: inscrever email de teste e verificar se msg chega.</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "33 mensagens agendadas no SendFlow",
        "description_html": "<p><strong>Verificar:</strong> Todas as 33 mensagens WhatsApp agendadas com datas e horarios corretos no SendFlow.</p><p>Conferir: MSG-NUT (5), MSG-ANT (9), MSG-POS (1), MSG-AMP (7), MSG-FEC (11).</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Segmentacao de compradores configurada (parar msgs)",
        "description_html": "<p><strong>Verificar:</strong> Webhook de compra integrado com SendFlow para remover compradores da sequencia de venda automaticamente.</p><p>Quem comprou NAO pode receber msgs de urgencia/escassez.</p>",
        "state": STATES["todo"],
        "priority": "high",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Sala Zoom criada e testada",
        "description_html": "<p><strong>Verificar:</strong> Sala Zoom agendada para 10/03 as 20:00. Link testado. Configuracoes: chat ativo, gravacao automatica, co-host definido.</p><p><strong>Link:</strong> {{link_sala}}</p>",
        "state": STATES["todo"],
        "priority": "high",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Slides do webinario prontos (~45 slides)",
        "description_html": "<p><strong>Verificar:</strong> ~45 slides prontos seguindo o roteiro-completo.md. Abertura (7 blocos) + Empatia + 3 Segredos + Pitch (15 passos + Stack Slide).</p>",
        "state": STATES["todo"],
        "priority": "high",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Link de compra/checkout ativo e testado",
        "description_html": "<p><strong>Verificar:</strong> Checkout configurado com preco R$2.500. Parcelamento definido. Pagamento via cartao e PIX. Testar compra simulada.</p><p><strong>Link:</strong> {{link_compra}}</p>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Pagina de replay preparada (ativar so em D+1)",
        "description_html": "<p><strong>Verificar:</strong> Pagina de replay criada mas NAO publicada ainda. Ativar somente em 11/03 as 08:00. Delay de 55min na oferta.</p><p><strong>Link:</strong> {{link_replay}}</p>",
        "state": STATES["todo"],
        "priority": "medium",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Depoimentos selecionados para mensagens",
        "description_html": "<p><strong>Verificar:</strong> Depoimentos reais selecionados para MSG-NUT-04, MSG-AMP-03, MSG-FEC-02, MSG-FEC-05.</p><p>Se nao houver depoimentos de clientes, usar case do Caio (18 funcionarios → 0) com mais detalhes.</p>",
        "state": STATES["todo"],
        "priority": "medium",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Backup do link de compra pronto",
        "description_html": "<p><strong>Verificar:</strong> Link de compra salvo em local acessivel para colar rapidamente no chat do Zoom durante o webinario.</p>",
        "state": STATES["todo"],
        "priority": "medium",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
    {
        "name": "Teste completo do funil: inscricao > WhatsApp > sala > compra",
        "description_html": "<p><strong>Verificar:</strong> Testar o funil de ponta a ponta:</p><ol><li>Inscrever com email de teste na pagina de captura</li><li>Verificar redirect para grupo WhatsApp</li><li>Verificar MSG-NUT-01 automatica</li><li>Verificar link da sala Zoom funciona</li><li>Verificar link de compra funciona</li><li>Verificar webhook de compra para segmentacao</li></ol>",
        "state": STATES["todo"],
        "priority": "urgent",
        "labels": [LABELS["checklist"]],
        "target_date": "2026-03-09",
        "module": "checklist",
    },
]


def create_issue(client, item):
    """Create a single issue via Plane API."""
    body = {
        "name": item["name"],
        "priority": item.get("priority", "none"),
    }
    if item.get("description_html"):
        body["description_html"] = item["description_html"]
    if item.get("state"):
        body["state"] = item["state"]
    if item.get("labels"):
        body["labels"] = item["labels"]
    if item.get("start_date"):
        body["start_date"] = item["start_date"]
    if item.get("target_date"):
        body["target_date"] = item["target_date"]

    url = f"{API_BASE}/projects/{PROJECT_ID}/issues/"
    resp = client.post(url, headers=HEADERS, json=body)

    if resp.status_code == 429:
        time.sleep(5)
        resp = client.post(url, headers=HEADERS, json=body)

    if resp.status_code in (200, 201):
        data = resp.json()
        return {"success": True, "id": data.get("id"), "name": item["name"], "module": item.get("module")}
    else:
        return {"success": False, "name": item["name"], "status": resp.status_code, "detail": resp.text[:200]}


def add_to_module(client, module_id, issue_ids):
    """Add issues to a module."""
    url = f"{API_BASE}/projects/{PROJECT_ID}/modules/{module_id}/module-issues/"
    body = {"issues": issue_ids}
    resp = client.post(url, headers=HEADERS, json=body)
    return resp.status_code in (200, 201)


def main():
    print("=" * 60)
    print("MIGRACAO: Webinario -> Plane.so [OPERA]")
    print("=" * 60)

    created = []
    failed = []
    module_items = {k: [] for k in MODULES}

    with httpx.Client(timeout=30.0) as client:
        # Create all issues
        for i, item in enumerate(ITEMS, 1):
            print(f"[{i:2d}/46] Criando: {item['name'][:50]}...", end=" ")
            result = create_issue(client, item)
            if result["success"]:
                print(f"OK (id: {result['id'][:8]}...)")
                created.append(result)
                mod = result.get("module")
                if mod and mod in module_items:
                    module_items[mod].append(result["id"])
            else:
                print(f"FALHOU ({result['status']})")
                failed.append(result)
            time.sleep(0.3)  # Rate limit protection

        # Add to modules
        print("\n" + "=" * 60)
        print("ASSOCIANDO AOS MODULOS")
        print("=" * 60)

        for mod_name, issue_ids in module_items.items():
            if not issue_ids:
                continue
            mod_id = MODULES[mod_name]
            print(f"Modulo '{mod_name}': {len(issue_ids)} items...", end=" ")
            ok = add_to_module(client, mod_id, issue_ids)
            print("OK" if ok else "FALHOU")
            time.sleep(0.3)

    # Summary
    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)
    print(f"Criados: {len(created)}/46")
    print(f"Falharam: {len(failed)}/46")

    if failed:
        print("\nItens que falharam:")
        for f in failed:
            print(f"  - {f['name']} (HTTP {f['status']}): {f['detail']}")

    # Output IDs for reference
    print("\n" + "=" * 60)
    print("IDS CRIADOS")
    print("=" * 60)
    for r in created:
        print(f"  {r['id']}  {r['name'][:60]}")

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
