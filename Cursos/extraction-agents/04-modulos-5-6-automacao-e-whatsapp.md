Agora vou compilar toda a analise. Todos os 17 arquivos foram lidos com sucesso.

---

# Analise Estruturada -- Modulos 5 e 6

## MODULO 5: Automatizando seu Webinario

---

### Aula 01: Configurando seu Webinario Automatico

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/01-configurando-seu-webinario-automatico.md`

#### Conceitos-chave e Definicoes

- **Webinario Perpetuo (automatico):** Webinario gravado que roda em loop como se fosse ao vivo, em dias e horarios programados.
- **Just-in-time:** Modalidade onde o webinario comeca a cada 15/30 minutos -- indicado para produtos de ticket mais baixo (R$200-300) e publico menos consciente.
- **Replay imediato:** Opcao para permitir que o lead assista a ultima edicao gravada ao inves de esperar o proximo horario.
- **Late joiners (atrasados):** Permite que usuarios entrem atrasados e vejam o webinario como se estivesse ao vivo (a partir do ponto atual).
- **Bloqueio same-day registration:** Impede o lead de se inscrever para o webinario do mesmo dia, forcando-o a ficar mais tempo no grupo antes do evento.
- **Funil diario vs. semanal:** Webinario pode rodar todo dia (diario) ou em dia fixo da semana (semanal). A escolha afeta a janela de nutricao.

#### Ferramentas/Plataformas

| Ferramenta | Funcao | Configuracoes |
|------------|--------|---------------|
| **EverWebinar** | Plataforma de webinario automatico | Hosting do video, agendamento, paginas |
| **Vimeo** | Hospedagem de video | Usar link HD 720p (links de arquivo do video) |
| **YouTube** | Alternativa de hospedagem de video | Link direto |
| **MP4 (servidor proprio)** | Alternativa de hospedagem | Hospedar no proprio servidor |

#### Configuracoes Tecnicas Detalhadas

**Origem do video:**
- Selecionar "video externo" (nao puxar de sessao live anterior)
- Vimeo: Menu tres pontinhos > "Links de arquivos do video" > Copiar link HD 720p
- Informar duracao exata do video

**Configuracoes basicas:**
- Nome interno (privado) + codigo curto para campanhas/tags (ex: "WP2" = Webinar Perpetuo 2)
- Titulo publico (headline principal) -- vai para pagina de captura
- Descricao (150 caracteres)
- Thumbnail (max 1MB)
- Moderadores: nome, e-mail de suporte

**Agendamento:**
- Frequencia: diaria ou semanal (dia especifico)
- Horario: ex. 20h (8 PM)
- Fuso horario: America/Sao_Paulo (GMT-3)
- Conversao de fuso para horario local: desabilitada quando usa grupos de WhatsApp (todos recebem o mesmo horario)
- Late joiners: habilitado (entram atrasados no ponto atual)
- Just-in-time: desabilitado para funil com grupo de WhatsApp
- Exibir apenas o proximo horario disponivel (display only the next)
- Bloqueio de datas especificas (feriados)

#### O que e especifico de plataforma vs. conceitual

| Especifico do EverWebinar | Conceitual/Reutilizavel |
|---------------------------|-------------------------|
| Interface de configuracao de schedule | Conceito de webinario perpetuo automatico |
| Just-in-time option | Estrategia de bloqueio same-day para nutricao |
| Campos de configuracao basica | Logica de late joiners |
| Formato de link Vimeo HD | Decisao diaria vs. semanal |

---

### Aula 02: Configurando a Pagina de Captura

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/02-configurando-a-pagina-de-captura.md`

#### Conceitos-chave

- **Pagina de captura padrao (do EverWebinar):** Template pronto com formulario integrado -- mais simples, porem com campo de fuso horario que pode confundir brasileiros.
- **Pagina de captura propria:** Pagina personalizada com formulario proprio, exige integracao via API/one-click registration.
- **Estrategia sem captura:** Botao direto para grupo de WhatsApp (sem coletar nome/email/telefone na pagina de captura).
- **Split testing (A/B):** EverWebinar permite criar versao B da pagina para teste.

#### Opcoes de Registro

1. **Usar pagina do EverWebinar:** Selecionar template, personalizar cor/texto do botao, popup com campos (nome, email, telefone).
2. **Usar pagina propria com API:** Criar formulario proprio, capturar dados e redirecionar via link one-click registration.
3. **Usar pagina propria sem captura:** Botao direto para WhatsApp (estrategia do autor).

#### Configuracoes Tecnicas

**Campos do formulario:**
- First name (obrigatorio)
- E-mail (obrigatorio)
- Phone number (opcional, pode ser obrigatorio)
- Last name: NAO pedir (recomendacao)

**Tipos de botao de registro:**
- Registration bar (barra fixa embaixo)
- Registration bubble
- Registration button
- Full form (formulario visivel)

**Popup de registro:** Personalizavel (cor, estilo, campos)

**Webinario pago vs. gratuito:**
- Free: registro gratuito (recomendado)
- Paid: exige link de checkout (Hotmart, etc.) -- NAO recomendado pelo autor

**One-click registration:**
- Link especial com parametros na URL (first_name, last_name, email, phone, timezone, schedule)
- Permite registro sem formulario do EverWebinar
- Requer conhecimento tecnico ou programador

**Link direto para sala (Direct Link to Live Room):**
- Entra direto na sala, bypassa todo registro
- Problema: aula comeca imediatamente independente do horario
- Usar somente na hora exata do webinario

#### Integracao com WhatsApp (estrategia do autor)

```
Pagina de captura (botao direto para WhatsApp)
    -> Lead entra no grupo de WhatsApp
    -> No dia do webinario: link para pagina "entrar" com formulario
    -> Formulario redireciona via one-click registration
    -> Lead registra no EverWebinar e cai na sala de espera
```

---

### Aula 03: Configurando Disparo de Emails

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/03-configurando-disparo-de-emails.md`

#### Conceitos-chave

- **Servico de email do EverWebinar:** Disparo integrado (requer configuracao de SMTP/dominio).
- **Notificacoes pre-webinario:** Emails enviados antes do webinario (confirmacao, lembretes).
- **Notificacoes pos-webinario:** Emails segmentados por comportamento (compareceu, nao compareceu, viu oferta, comprou, etc.).
- **Last minute notification:** Email padrao 15 minutos antes (nao editavel o tempo).

#### Sequencia de Emails Pre-Webinario

| Momento | Tipo | Conteudo |
|---------|------|----------|
| Imediato (ao registrar) | Confirmacao | Parabens, dados da aula, link de acesso, data/hora |
| X horas antes (configuravel) | Lembrete | Ex: 24h, 48h, 72h antes |
| 15 min antes (fixo) | Last minute | "Vamos entrar ao vivo, clique aqui" |

#### Segmentacao Pos-Webinario

| Segmento | Criterio |
|----------|----------|
| Todos os registrados | Qualquer pessoa registrada |
| Quem compareceu | Entrou na sala |
| Quem NAO compareceu | Registrou mas nao entrou |
| Compareceu e comprou | Entrou + comprou (via pixel de conversao) |
| Compareceu e NAO comprou | Entrou mas nao comprou |
| Saiu antes do pitch | Entrou mas saiu antes de X tempo (ex: 1h20min) |
| Ficou ate o final e NAO comprou | Viu a oferta completa |

#### Tags Dinamicas nos Emails

- `{webinar_title}` -- titulo do webinario
- `{presented_by}` -- nome do apresentador
- `{date_and_time}` -- data e hora
- `{first_name}` -- primeiro nome do lead
- `{webinar_link}` -- link de acesso

#### Configuracoes Tecnicas

**SMTP/Dominio:**
- Configurar registros CNAME no DNS do dominio
- 3 registros CNAME necessarios
- Onde configurar: Cloudflare, Amazon, Hostgator, etc.

**Phone notifications (SMS):**
- Requer integracao com servico de SMS (Twilio, etc.)
- Autor recomenda usar API oficial do WhatsApp ao inves de SMS

#### Estrategia do Autor (sem email pre)

Como captura direto para WhatsApp, o lead so se registra no EverWebinar no dia do webinario. Portanto:
- Pre-webinario: apenas email imediato + last minute (15min)
- Pos-webinario: emails segmentados por comportamento
- Recomendacao: email para quem NAO compareceu com link do replay; email para quem compareceu com link do WhatsApp para contato

---

### Aula 04: Configurando as Integracoes

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/04-configurando-as-integracoes.md`

#### Integracoes Disponiveis

| Tipo | Ferramentas | Funcao |
|------|-------------|--------|
| **Autoresponder** | ActiveCampaign, Zapier, e outros | Gerenciar leads, tags, automacoes |
| **SMTP** | SendGrid, etc. | Disparo de email personalizado |
| **SMS** | Twilio, etc. | Notificacoes por SMS |
| **Tracking** | Facebook Pixel, Google Analytics | Rastreamento de conversoes |

#### Configuracao ActiveCampaign

- Pegar API Key e URL na area de desenvolvedores do ActiveCampaign
- Colar no EverWebinar na secao de integracoes
- Permite: adicionar leads, adicionar tags por comportamento (registrou, compareceu, comprou, etc.)

#### Pixels de Rastreamento (Facebook Pixel)

| Pagina | Evento | Quando usar |
|--------|--------|-------------|
| Registration page | View | Quando usa pagina do EverWebinar |
| Registration form (popup) | Interaction | Quando usa formulario deles |
| Thank you page | Lead | Quando usa pagina de obrigado deles |
| Live room | Custom (compareceu) | SEMPRE usar |
| Replay page | Custom (replay) | SEMPRE usar |

**Importante:** Colocar script completo do pixel (nao apenas o ID).

#### Estrategia do Autor

- Nao usa paginas de captura/obrigado do EverWebinar (usa proprias)
- Pixel somente em: live room + replay page
- Tags no ActiveCampaign: por comportamento (fase de escala)

---

### Aula 05: Pagina de Obrigado

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/05-pagina-de-obrigado.md`

#### Conceitos-chave

- **Thank You Page (Pagina de Obrigado):** Pagina exibida apos registro no webinario.
- **Pesquisa pos-registro:** Formulario integrado para coletar dados do lead (interesses, perfil).

#### Opcoes de Pagina de Obrigado

1. **Pagina padrao do EverWebinar:** Template com dados do webinario, link da sala, pesquisa opcional.
2. **Pagina propria customizada:** URL personalizada com conteudo proprio.

#### Pesquisa Integrada (Survey)

**Tipos de perguntas:**
- Multipla escolha (selecionar varias opcoes)
- Escolha unica (radio)
- Resposta curta (texto breve)
- Resposta longa (textarea)

**Exemplos de perguntas:**
- "Voce ja vende no digital?" (sim/nao)
- "Quais funis voce geralmente usa?" (lancamento, perpetuo, webinario)
- "Qual o seu Instagram?"
- "Me conte mais do seu projeto"

#### Fluxo com Pagina Propria + WhatsApp

```
Pagina de captura propria (nome, telefone, email)
    -> One-click registration (registra no EverWebinar)
    -> Pagina de obrigado propria
        -> CTA: "Entre no nosso grupo de WhatsApp"
        -> Link para grupo de WhatsApp
```

---

### Aula 06: Configurando a Sala do Webinario

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/06-configurando-a-sala-do-webinario.md`

#### Conceitos-chave

- **Autoplay:** Video comeca automaticamente (mas no Chrome/Safari comeca MUDO -- ruim para UX). Recomendacao: desabilitar autoplay.
- **Countdown page:** Pagina de espera com contador regressivo ate o webinario comecar.
- **Eventos programados:** Acoes que acontecem em momentos especificos do video.
- **Chat simulado:** Mensagens pre-configuradas que simulam participacao ao vivo.
- **Participantes simulados:** Numero dinamico de participantes que sobe e desce.

#### Eventos Programaveis na Timeline

| Evento | Descricao | Configuracao |
|--------|-----------|--------------|
| **Poll/Pesquisa** | Enquete que aparece no chat | Inicio (ex: 0:00:05), fim (ex: 0:00:20), opcoes |
| **File Share** | PDF/arquivo para download | Inicio, fim, upload do arquivo |
| **Announcement** | Anuncio popup dentro do video | Inicio, fim, texto, nome do autor |
| **Sticky Message** | Mensagem fixada na area do chat | Inicio, fim, texto |
| **Product Offer** | Botao de compra com CTA | Inicio (momento do pitch), urgencia (countdown), link do checkout |
| **Live Sales Announcement** | Notificacao "fulano comprou" | Horario, nome da pessoa, nome do produto |
| **Redirect** | Redireciona ao final do video | Horario exato do fim do video, URL destino (pagina de vendas/checkout) |

#### Configuracao do Botao de Compra (Product Offer)

- **Headline:** Nome da oferta
- **Imagem:** Max 1MB
- **Texto acima do botao:** CTA descritivo
- **Texto do botao:** Ex: "Garantir a minha vaga agora"
- **Link:** URL do checkout (direto, sem pagina de vendas intermediaria)
- **Abrir em outra aba:** Sim
- **Horario de aparicao:** Momento exato do pitch no video
- **Horario de desaparicao:** Zero (fica ate o final)
- **Urgencia/Countdown:** Tempo ate "expirar" (ex: 30min, 40min) -- gera escassez

#### Live Sales Announcements

- Adicionar compras reais de webinarios anteriores
- Colocar nome real do comprador e horario real da compra
- Limitar quantidade para nao ficar excessivo
- Gera prova social

#### Chat Simulado

**Tipos de mensagem:**
- **Chat:** Mensagem normal de participante
- **Question:** Aparece vermelho como pergunta
- **Highlighted/Tip:** Mensagem destacada (usada por admin/apresentador)

**Configuracoes do chat:**
- Habilitar/desabilitar chat ao vivo
- Participantes verem mensagens uns dos outros: habilitado no inicio (para ter movimento), desabilitado depois
- Salvar comentarios reais: aprovados viram mensagens automaticas futuras
- Moderacao via link do apresentador (presenter link)

#### Numero de Participantes

| Modo | Descricao |
|------|-----------|
| Ocultar | Nao mostra numero |
| Real | Mostra numero real de pessoas ao vivo |
| Fixo | Valor fixo (ex: 233) |
| Dinamico | Simula entrada/saida gradual (pico no valor definido) |

#### Replay

- Habilitavel/desabilitavel
- Controles de avanco/retrocesso
- Expiracao: ex. 48 horas
- Perguntas: campo para duvidas (sem chat) -- vai para email
- Autor desabilita replay (usa pagina de "melhores momentos" propria)

#### Moderacao ao Vivo

- **Link do apresentador (Presenter Link):** Painel de controle em tempo real
- Mostra participantes reais e mensagens reais
- Permite responder publicamente ou no privado
- Criar multiplos apresentadores/moderadores (ex: "Suporte")

---

### Aula 07: Teste Final

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/07-teste-final.md`

#### Conceitos-chave

- **Teste end-to-end:** Simular toda a experiencia do usuario (registro, sala de espera, aula, chat, oferta, vendas).
- **Presenter Link:** Link de controle ao vivo para moderar chat e responder participantes.

#### Fluxo de Teste Validado

1. Entrar via Direct Link to Live Room
2. Preencher nome, email, telefone
3. Verificar pagina de espera com countdown
4. Clicar "iniciar" (autoplay desabilitado)
5. Verificar chat simulado aparecendo nos tempos corretos
6. Verificar enquete aparecendo e desaparecendo
7. Verificar arquivo para download
8. Verificar sticky message
9. Verificar announcement
10. Verificar oferta/botao de compra aparecendo
11. Verificar countdown de urgencia
12. Verificar notificacoes de venda ("fulano comprou")
13. Testar chat ao vivo (mensagem aparece no painel do apresentador)
14. Testar resposta publica e privada do apresentador
15. Verificar numero dinamico de participantes

#### Funcionalidades Confirmadas

- Chat do apresentador aparece com estrela de destaque
- Resposta privada: so visivel para o destinatario
- Ao minimizar o chat, a oferta some; ao expandir, reaparece
- Recomendacao: configurar mensagens no chat com link do checkout periodicamente

---

### Aula 08: Configurando Sua Propria Pagina de Captura

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/08-configurando-sua-propria-pagina-de-captura.md`

#### Conceitos-chave

- **Pagina de acesso a sala de aula:** Diferente de pagina de captura de leads -- usada no dia do webinario para registrar e direcionar.
- **Direct Link vs. One-Click Registration:** Direct link e simples mas nao respeita horario; one-click respeita agendamento.

#### Duas Opcoes Tecnicas

**Opcao 1: Link Direto (Simples)**
- Your Links > Direct Link to Live Room
- O lead preenche nome/email/telefone e entra direto na sala
- Problema: a aula comeca imediatamente, independente do horario programado
- Solucao: enviar esse link SOMENTE no horario exato do webinario (ex: 20h)

**Opcao 2: One-Click Registration (Sofisticado)**
- Criar pagina propria com formulario
- Formulario redireciona via one-click registration URL
- Respeita o agendamento: se antes do horario, cai na sala de espera
- Requer liberacao da API (nao disponivel no trial de 14 dias)

#### Configuracao da Pagina Propria

1. Editar webinario > Registration > Selecionar "Your own custom page"
2. Inserir URL da pagina propria (ex: `seudominio.com.br/acessar`)
3. Criar a pagina com formulario (nome, email, telefone)
4. Formulario redireciona para URL do one-click registration com parametros

---

### Aula 09: One-Click Registration (Detalhamento Tecnico)

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/09-one-click-registration.md`

#### Pre-requisito

- Solicitar liberacao da API ao EverWebinar (nao disponivel no trial de 14 dias)
- API > Informar que quer pagina propria de captura
- Fornecer link de uma pagina de captura

#### Estrutura da URL One-Click Registration

```
https://[dominio-everwebinar]/register?
first_name=VALOR
&last_name=VALOR        (opcional - pode remover)
&email=VALOR
&phone_country_code=55  (fixo para Brasil)
&phone_number=VALOR
&timezone=gmt-3         (fixo para Brasil)
&schedule=1             (ID do agendamento - geralmente 1)
```

#### Parametros Obrigatorios vs. Opcionais

| Parametro | Obrigatorio | Valor padrao |
|-----------|-------------|--------------|
| first_name | Sim | Campo do formulario |
| last_name | Nao | Pode remover |
| email | Sim | Campo do formulario |
| phone_country_code | Sim | "55" (fixo Brasil) |
| phone_number | Sim | Campo do formulario |
| timezone | Sim | "gmt-3" (fixo Brasil) |
| schedule | Sim | "1" (fixo) |

#### Implementacao com GreatPages

1. Criar formulario com campos visiveis: nome, email, whatsapp
2. Criar campos ocultos (hidden): phone_country_code (55), timezone (gmt-3), schedule (1)
3. Configurar redirecionamento: URL do one-click registration (ate o `?`)
4. Marcar "Enviar dados do formulario no redirecionamento"
5. Mapear nomes dos campos para os nomes dos parametros exatos

**Mapeamento de campos:**

| Campo do formulario | Nome do parametro |
|--------------------|-------------------|
| Nome | first_name |
| Email | email |
| WhatsApp | phone_number |
| (oculto) | phone_country_code = 55 |
| (oculto) | timezone = gmt-3 |
| (oculto) | schedule = 1 |

#### Implementacao com Elementor

1. Criar formulario com campos: nome, email, whatsapp
2. Em cada campo: Advanced > Short Field Name (copiar shortcode)
3. Montar URL manualmente substituindo valores pelos shortcodes dos campos
4. Em Actions After Submit: adicionar "Redirect" com a URL montada

---

### Aula 10: Redirecionar para Sala de Aula

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-05-automatizando-seu-webinario/10-redirecionar-para-sala-de-aula.md`

#### Conceito-chave

- **Pagina de obrigado que redireciona para sala de espera:** Ao inves do lead cair em uma pagina estatica de "obrigado", ele e redirecionado diretamente para a sala de espera/live do webinario.

#### Fluxo Tecnico Completo

```
Grupo WhatsApp (dia do webinario)
    -> Link da pagina "entrar/acessar" (formulario: nome, email, telefone)
    -> One-click registration (registra no EverWebinar)
    -> Pagina de obrigado (Thank You Page) customizada
        -> Codigo PHP redireciona automaticamente para sala de espera/live
    -> Sala de espera (countdown) ou sala ao vivo (se na hora)
```

#### Configuracao Passo a Passo

**1. Configurar pagina de obrigado no EverWebinar:**
- Editar webinario > Thank You Page
- Selecionar "Your own custom page"
- Inserir URL da pagina propria (ex: `seudominio.com.br/entrando`)
- Marcar opcao "Enviar informacoes do registro para a pagina"

**2. Criar a pagina no WordPress:**
- Paginas > Adicionar nova > Nome: "entrando"
- Publicar (pagina vazia por enquanto)

**3. Instalar plugin WPCode:**
- Plugins > Adicionar novo > Buscar "WPCode"
- Instalar e ativar

**4. Criar snippet PHP:**
- WPCode > Adicionar novo > "Adicionar seu codigo personalizado"
- Tipo: PHP
- Nome: "Redireciona para a aula"
- Colar codigo PHP fornecido (redireciona para URL da sala do EverWebinar)
- Salvar snippet
- Copiar shortcode gerado

**5. Inserir shortcode na pagina:**
- Editar pagina "entrando"
- Colar shortcode do WPCode
- Publicar

#### Ferramentas Utilizadas

| Ferramenta | Funcao |
|------------|--------|
| **WordPress** | CMS para criar a pagina de redirecionamento |
| **WPCode (plugin)** | Executar codigo PHP personalizado via shortcode |
| **EverWebinar** | Plataforma do webinario (recebe o registro e serve a sala) |

---

## MODULO 6: Gestao de Grupos de WhatsApp

---

### Aula 01: Gestao de Grupos com a SendFlow

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-06-gestao-grupos-wpp/01-gestao-de-grupos-com-a-sendflow.md`

#### Conceitos-chave

- **SendFlow:** Ferramenta principal de automacao de grupos de WhatsApp.
- **Campanha:** Conjunto de grupos + automacoes de mensagens no SendFlow.
- **Janela de 7 dias:** Cada campanha no SendFlow opera em ciclos semanais (segunda a domingo).
- **Fase 1 (pre-webinario):** Semana de captacao e nutricao ate o dia do webinario.
- **Fase 2 (pos-webinario):** Semana de follow-up, replay, fechamento de carrinho, downsell.
- **Duas campanhas necessarias:** O SendFlow so permite 7 dias de mensagens por campanha, entao o funil de 2 semanas exige 2 campanhas.

#### Estrutura do Funil Semanal

```
FASE 1 (Campanha 1): Pre-Webinario
    Dia 1-6: Captacao + nutricao de leads
    Dia 7: Webinario ao vivo (ex: terca 20h)

FASE 2 (Campanha 2): Pos-Webinario
    Dia 1: Replay anunciado
    Dia 2: Replay disponivel
    Dia 3: Fechamento de carrinho
    Dia 4: Downsell (opcional)
    Dia 5: Encerramento
```

#### Configuracao do SendFlow

- **Automacoes:** Cronograma de disparo semanal (dia e horario especifico)
- **Formato campanha vs. lista:**
  - Campanha: enche um grupo, depois cria o proximo (sequencial)
  - Lista: distribui leads entre grupos simultaneamente (intercalado)
  - Usar sempre: **Campanha**
- **Webhooks:** Integracao com plataforma de pagamento (Ticto, Hotmart, etc.)

#### Exemplos de Webhooks

| Evento | Acao |
|--------|------|
| Compra aprovada | Mensagem de boas-vindas no privado |
| Cartao recusado | Mensagem de suporte no privado |
| Boleto gerado | Mensagem com codigo do boleto |
| PIX gerado | Mensagem com codigo PIX |

---

### Aula 02: Criacao Automatica dos Grupos

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-06-gestao-grupos-wpp/02-criacao-automatica-dos-grupos.md`

#### Configuracao dos Grupos

| Parametro | Valor recomendado | Descricao |
|-----------|-------------------|-----------|
| Foto do grupo | Foto pessoal | Obrigatoria para criacao |
| Nome do grupo | Ex: "Grupo VIP" | Nome padrao + numeracao automatica |
| Mensagens | Apenas admins | Grupo fechado por padrao |
| Mensagens temporarias | Desativado | Pode ativar por mensagem individual |
| Inicio da contagem | 11 (ou outro) | Numeracao inicial dos grupos (pode comecar maior para parecer maior) |
| Descricao | Texto formatado | Suporta formatacao WhatsApp (negrito com asterisco) |
| Grupos disponiveis a frente | 2-3 | Grupos pre-criados para absorver volume |
| Limite de pessoas por grupo | 250 | Recomendacao do SendFlow (>250 pode nao notificar todos) |
| Numeracao no inicio | Sim | Hashtag + numero no nome do grupo |

#### Administradores

- Obrigatorio: pelo menos 2 numeros de WhatsApp (conta associada + outro admin)
- O admin nao pode ser o mesmo numero da conta associada

#### Deep Link

- Elimina a necessidade do lead clicar "entrar na conversa" no site do WhatsApp
- Aumenta taxa de entrada significativamente
- Permite configurar **Facebook Pixel ID** para marcar evento de lead na entrada do grupo

#### Integracao com Facebook Pixel via SendFlow

| Cenario | Marcar lead no SendFlow? |
|---------|--------------------------|
| Pagina de captura sem formulario (direto para WhatsApp) | SIM -- unica forma de marcar lead |
| Pagina de captura COM formulario (nome, email, telefone) | NAO -- evitar duplicacao de lead |

#### Metricas do Dashboard

- Numero de cliques no link do grupo
- Numero de pessoas que entraram
- Percentual de entrada
- Numero de pessoas que sairam
- Participantes atuais
- Grupos cheios vs. disponiveis

#### Outras Configuracoes

- Redirecionar lead para o primeiro grupo tentado (evitar entrar em varios)
- Anti-hacker habilitado
- Atualizar link automaticamente quando alguem e banido
- Traducao automatica: desabilitar se roda so no Brasil
- Google Tag Manager: integracao disponivel

---

### Aula 03: Mensagens Automaticas nos Grupos

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-06-gestao-grupos-wpp/03-mensagens-automaticas-nos-grupos.md`

#### Tipos de Automacao

| Trigger | Quando dispara |
|---------|----------------|
| Cronograma de disparo | Dia/hora especifico da semana (semanal) |
| Quando encher o grupo | Grupo atinge limite de pessoas |
| Quando participante entrar | Lead entra no grupo |
| Quando participante sair | Lead sai do grupo |

#### Tipos de Acao por Automacao

| Acao | Descricao |
|------|-----------|
| Enviar mensagem | Texto, emoji, formatacao WhatsApp |
| Atualizar assunto/nome do grupo | Muda o titulo do grupo |
| Atualizar descricao | Muda a descricao do grupo |
| Atualizar foto | Muda a imagem do grupo |
| Atualizar configuracoes | Abrir/fechar grupo para mensagens |
| Tornar admin | Promover participante |
| Remover admin | Remover permissao de admin |
| Desativar comunidade | Desabilitar formato comunidade |
| Adicionar tag condicional | Taguear lead |

#### Tipos de Conteudo nas Mensagens

| Formato | Detalhes |
|---------|----------|
| Texto | Com formatacao WhatsApp (negrito, italico, emoji) |
| Enquete | Pergunta + opcoes |
| Contato | Compartilhar contato |
| Evento | Criar evento do WhatsApp |
| Arquivo | Upload de PDF, etc. |
| Audio | Upload de MP3 |
| Video | Upload de video (opcao de video instantaneo/redondo, max 1min) |
| Imagem | Upload de imagem |

#### Opcoes de Envio

- **Marcar todos os participantes:** Mencionar todos (usar com parcimonia, reservar para mensagens criticas)
- **Mensagens temporarias:** Configurar para sumir em 24h
- **Velocidade de envio:** Customizavel (lenta para seguranca)
- **Conta de envio:** "Todas as contas da campanha" (redundancia caso numero seja banido)

#### Exemplo de Cronograma Fase 1 (Pre-Webinario)

Supondo webinario na terca-feira 20h:

| Dia | Hora | Tipo | Conteudo |
|-----|------|------|----------|
| Quarta | 9h | Mensagem | Boas-vindas + compromisso |
| Quinta | 15h | Mudar nome grupo | "Presente liberado" |
| Quinta | 15:03 | Mensagem | Link do e-book/presente |
| Sexta | 9h | Mensagem | Nutricao/conteudo |
| Sabado | 9h | Mensagem | Nutricao/conteudo |
| Domingo | 9h | Mensagem | Antecipacao |
| Segunda | 9h | Mensagem | Antecipacao - "amanha" |
| Terca | AM | Mensagem | "Hoje e o dia" |
| Terca | 19:45 | Mensagem | "Faltam 15 minutos" |
| Terca | 20h | Mensagem | "Estamos ao vivo - link" |

#### Gestao de Mensagens Agendadas

- Mensagens dos proximos 7 dias ficam pre-agendadas
- Apos execucao, agenda automaticamente a proxima
- **Edicao de automacao NAO altera mensagens ja agendadas** -- editar na fila de agendados

#### Fase 1 -> Fase 2: Transicao

- Ultima mensagem da Fase 1: "Estamos ao vivo + link"
- Apos essa mensagem: mover TODOS os grupos da Fase 1 para a Fase 2
- Se nao mover: leads recebem o loop da Fase 1 novamente (boas-vindas, etc.)

---

### Aula 04: Criando a Campanha Fase 2

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-06-gestao-grupos-wpp/04-criando-a-campanha-fase-2.md`

#### Configuracao da Fase 2

| Parametro | Valor | Diferenca da Fase 1 |
|-----------|-------|----------------------|
| Modo | Campanha | Igual |
| Foto | Mesma da Fase 1 | Lead nao percebe mudanca |
| Nome do grupo | Mesmo da Fase 1 | Lead nao percebe mudanca |
| Descricao | Mesma/atualizada | Pode mudar para contexto pos-webinario |
| Criacao de grupos | **DESATIVADA** | Nao cria grupos novos |
| Grupos disponiveis | 3 | Igual |
| Limite por grupo | 250 | Igual |
| Administradores | Mesmo(s) | Igual |

**Ponto critico:** Desativar criacao de grupos na Fase 2, pois os grupos serao IMPORTADOS da Fase 1.

#### Fluxo de Transicao

```
Fase 1 (captacao + nutricao)
    -> Ultima mensagem: "Estamos ao vivo" (terca 20h)
    -> MANUALMENTE: importar grupos da Fase 1 para Fase 2
    -> Fase 2 (pos-webinario: replay, fechamento, downsell)
```

**Observacao:** A transferencia de grupos entre campanhas e MANUAL (o autor menciona que espera que o SendFlow implemente automacao para isso).

---

### Aula 05: Automatizando a Fase 2

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-06-gestao-grupos-wpp/05-automatizando-a-fase-2.md`

#### Cronograma Fase 2 (Pos-Webinario)

Supondo webinario na terca-feira 20h:

| Dia | Hora | Tipo | Conteudo | Automatizado? |
|-----|------|------|----------|---------------|
| Terca | 22h | Mensagem | "Aula foi incrivel" + reacao | Sim |
| Quarta | AM | Mensagem | Anuncio do replay | Sim |
| Quarta | PM | Mensagem(ns) | Replay + conteudo | Sim |
| Quinta | 8:30-9h | Mensagem | Anuncio fechamento de carrinho | Sim |
| Quinta | 9:30 | Acao | Abrir grupo (todos podem enviar) | Sim |
| Quinta | 9:30 | Mensagem | "Grupo aberto, bora tirar duvidas" | Sim |
| Quinta | 10h-20h | Mensagens | Depoimentos, oferta, garantia, objecoes | MANUAL (modelos) |
| Quinta | 20h | Mensagem | "Faltam 2 horas" | Sim |
| Quinta | 21h | Mensagem | "O que esta te impedindo?" | Sim |
| Quinta | 21:30 | Mensagem | "Vamos fechar em 3, 2, 1" | Sim |
| Quinta | 22h | Acao | Fechar grupo (apenas admins enviam) | Sim |
| Quinta | 22h | Mensagem | "Inscricoes encerradas" | Sim |

#### Abertura do Grupo

- Automacao: "Atualizar configuracoes do grupo" > "Todos podem enviar mensagens"
- Mensagem seguinte: "Grupo aberto, manda suas duvidas"
- Proposito: gerar interacao, tirar duvidas, converter indecisos

#### Modelos de Mensagem (Templates)

**Organizacao por pastas:**
- **Elementos da oferta:** Garantia, bonuses, preco, condicoes
- **Depoimentos:** Resultados de alunos, prints, videos
- **Quebra de objecao:** Respostas para duvidas comuns ("funciona pra mim?", "e caro", etc.)

**Uso dos modelos:**
1. Mensagens > Modelo de mensagens > Criar pastas
2. Dentro de cada pasta: criar modelos com texto pronto
3. Para enviar: Enviar mensagem > Selecionar modelo > Enviar agora

#### Estrategia de Abertura de Grupo vs. Comunidade

| Abordagem | Quando usar | Pros | Contras |
|-----------|-------------|------|---------|
| Grupo aberto | Produtos mais caros | Interacao publica, prova social | Risco de mensagens negativas |
| Comunidade (fechada) | Quando nao quer abrir grupo | Sem risco de mensagens | Precisa de equipe de vendas no 1-a-1 |

---

### Aula 06: Movendo os Grupos para Fase 2

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-06-gestao-grupos-wpp/06-movendo-os-grupos-para-fase-2.md`

#### Processo de Transferencia (Manual)

**Importar grupos para Fase 2:**
1. Ir para campanha Fase 2 > Grupos > Importar grupos
2. Selecionar "Da campanha" > Fase 1
3. Selecionar todos os grupos
4. Opcao "Padronizar grupos": aplica configuracoes da Fase 2 (foto, nome, descricao)
5. Clicar em "Proximo" e importar

**Remover grupos da Fase 1:**
- APOS importar na Fase 2: voltar a Fase 1 > Grupos > Remover cada grupo
- Se nao remover: leads recebem mensagens de AMBAS as campanhas

#### Padronizar vs. Nao Padronizar

| Opcao | Efeito | Pro | Contra |
|-------|--------|-----|--------|
| Padronizar | Aplica configuracoes da Fase 2 (numeracao, nome, descricao) | Grupos com ID unico para gestao | Numeracao reseta (ex: volta para 11) |
| Nao padronizar | Mantem exatamente como estava | Nome e numero inalterados | Todos ficam com mesmo nome (sem ID) |

**Recomendacao:** Padronizar (a mudanca de numeracao e aceitavel).

#### Ciclo Completo de 3 Campanhas

```
Campanha FASE 1 (pre-webinario)
    -> Grupos enchendo com leads novos
    -> Mensagens de nutricao + antecipacao
    -> "Estamos ao vivo" (ultima mensagem)
    -> MOVER grupos para Fase 2

Campanha FASE 2 (pos-webinario)
    -> Mensagens de replay + fechamento + downsell
    -> "Inscricoes encerradas" (ultima mensagem)
    -> MOVER grupos para Grupo de Conteudo

Campanha GRUPO DE CONTEUDO (long-term)
    -> Leads acumulados de todos os ciclos
    -> Conteudo de valor periodico
    -> Convites para futuros webinarios/eventos
    -> Divulgacao de conteudo (YouTube, TikTok, Instagram, podcasts)
```

#### Recuperacao de Erro

Se apagou grupos da Fase 1 ANTES de importar na Fase 2:
1. Na Fase 2 > Grupos > Importar > Selecionar "Da conta"
2. Selecionar o numero de WhatsApp
3. Lista TODOS os grupos existentes na conta
4. Selecionar manualmente os grupos corretos e importar

---

### Aula 07: Removendo Compradores dos Grupos

**Arquivo:** `/Users/evandrothomazini/Claude Code Antigravity/Webinário/Cursos/modulo-06-gestao-grupos-wpp/07-removendo-compradores-dos-grupos.md`

#### Conceito-chave

- **Webhook:** Conexao entre a plataforma de pagamento e o SendFlow para acoes automaticas baseadas em eventos de compra.
- **Remocao de compradores:** Evitar que quem ja comprou veja ofertas futuras de downsell e peca reembolso.

#### Configuracao do Webhook

**1. Criar projeto no SendFlow:**
- Selecionar plataforma de pagamento (Ticto, Hotmart, etc.)
- Cada plataforma exige dados diferentes

**Dados necessarios por plataforma:**

| Plataforma | Dados necessarios |
|------------|-------------------|
| Ticto | Token |
| Hotmart | Token, Client ID, Client Secret, Hotmart Basic |

**2. Obter token na plataforma:**
- Ticto: Ticto Tools > Webhook > Adicionar > Copiar token
- Hotmart: Documentacao da plataforma

**3. Configurar URL do webhook na plataforma de pagamento:**
- Copiar URL do SendFlow (gerada ao criar o projeto)
- Colar na configuracao de webhook da plataforma
- Selecionar produto especifico
- Selecionar eventos a monitorar

**Eventos disponiveis:**

| Evento | Descricao |
|--------|-----------|
| Venda realizada | Pagamento aprovado |
| Abandono de carrinho | Lead nao concluiu a compra |
| Boleto atrasado | Boleto gerado mas nao pago |
| Boleto impresso | Boleto foi gerado |
| Chargeback | Contestacao de pagamento |
| PIX gerado | Codigo PIX criado |
| PIX expirado | PIX nao pago no prazo |
| Pedido de reembolso | Cliente solicitou devolucao |
| Venda recusada | Cartao recusado |

#### Automacoes por Evento

**Quando VENDA REALIZADA:**

| Acao | Configuracao | Timing |
|------|-------------|--------|
| Remover da campanha | Remover da Fase 2 | Delay de 1 minuto |
| Enviar mensagem privada | "Seja bem-vindo!" | Delay de 3 minutos |
| Adicionar tag | "comprou" (ou por oferta) | Imediato |

**Quando REEMBOLSO:**

| Acao | Configuracao |
|------|-------------|
| Enviar mensagem privada | "Vi que solicitou cancelamento, me conte o que houve" |
| Adicionar black list | Impedir reentrada nos grupos |

#### Sistema de Tags

- Tags criadas em: Leads > Tags > Adicionar
- Formato recomendado: `[codigo_produto]_[acao]` (ex: "WP1_comprou", "WP1_downsell")
- Tags por oferta: permite segmentar clientes VIP vs. padrao
- **Tags condicionais:** Adicionar tag somente se condicao for atendida (ex: item_offer_code = codigo_da_oferta)

**Condicoes disponiveis:**
- Filtrar por oferta especifica (item_offer_code)
- Empilhar condicoes (E/OU)

#### Usos das Tags

| Uso | Exemplo |
|-----|---------|
| Disparar mensagens segmentadas | Mensagem so para clientes VIP |
| Identificar compradores | Tag "comprou" para filtragem |
| Convidar para eventos | Selecionar todos com tag "aluno" |
| Black list | Evitar reentrada de quem pediu reembolso |

---

## MAPA COMPLETO DE FERRAMENTAS E INTEGRACOES

### Stack Tecnica Principal

| Ferramenta | Funcao | Categoria |
|------------|--------|-----------|
| **EverWebinar** | Webinario automatico (sala, agendamento, eventos, chat) | Webinario |
| **SendFlow** | Automacao de grupos de WhatsApp | Comunicacao |
| **Vimeo** | Hospedagem de video | Video |
| **ActiveCampaign** | Autoresponder, tags, email marketing | CRM/Email |
| **Facebook/Meta Ads** | Trafego pago + Pixel de rastreamento | Trafego |
| **Ticto/Hotmart** | Plataforma de pagamento (checkout, webhooks) | Pagamento |
| **WordPress** | CMS para paginas personalizadas | Website |
| **WPCode (plugin WP)** | Executar codigo PHP em paginas WP | Website |
| **GreatPages** | Construtor de landing pages | Landing Pages |
| **Elementor** | Construtor de paginas WordPress | Landing Pages |
| **SendGrid** | SMTP para disparo de email | Email |
| **Twilio** | SMS (alternativa menos recomendada) | Comunicacao |
| **Google Analytics** | Tracking de comportamento | Analytics |
| **Google Tag Manager** | Gerenciamento de tags | Analytics |
| **Cloudflare** | DNS e CDN | Infraestrutura |

### Fluxo de Integracoes Completo

```
META ADS (trafego)
    -> PAGINA DE CAPTURA (GreatPages/Elementor/WordPress)
        -> Opcao A: Formulario (nome, email, telefone) -> One-Click Registration
        -> Opcao B: Botao direto para WhatsApp (sem captura)
    -> SENDFLOW (grupo WhatsApp)
        -> Automacoes de mensagem (fase 1: nutricao, fase 2: pos-webinario)
        -> Deep Link + Facebook Pixel (marca lead)
    -> EVERWEBINAR (webinario)
        -> One-Click Registration URL (registra lead)
        -> Pagina de espera (countdown)
        -> Sala do webinario (video + chat + oferta)
        -> Facebook Pixel (marca presenca)
        -> Emails segmentados (pos-webinario)
    -> ACTIVECAMPAIGN (CRM)
        -> Tags por comportamento (registrou, compareceu, comprou)
        -> Email marketing segmentado
    -> TICTO/HOTMART (pagamento)
        -> Checkout do produto
        -> Webhook -> SendFlow
            -> Remove comprador do grupo
            -> Mensagem privada de boas-vindas
            -> Adiciona tag de comprador
```

### O que e Especifico de Plataforma vs. Conceitual/Reutilizavel

| Especifico de Plataforma | Conceitual/Reutilizavel |
|--------------------------|------------------------|
| Interface do EverWebinar (configuracao, templates) | Conceito de webinario perpetuo automatico |
| API/one-click registration do EverWebinar | Fluxo de registro via URL com parametros |
| Interface do SendFlow (campanhas, automacoes) | Sistema de 2 fases (pre + pos webinario) |
| Webhooks especificos da Ticto/Hotmart | Remocao automatica de compradores dos grupos |
| WPCode plugin para WordPress | Redirecionamento pos-registro para sala |
| GreatPages campos ocultos | Campos ocultos em formularios com valores padrao |
| Elementor shortcodes de campos | Formularios que redirecionam com parametros |
| Facebook Pixel no SendFlow deep link | Marcacao de lead na entrada do grupo |
| ActiveCampaign tags e API | Segmentacao por comportamento |
| Chat simulado do EverWebinar | Prova social com mensagens e vendas simuladas |
| Numero dinamico de participantes do EverWebinar | Simulacao de audiencia ao vivo |
| Modelos de mensagem do SendFlow | Biblioteca de mensagens por categoria (oferta, depoimentos, objecoes) |
| Cronograma semanal do SendFlow | Funil semanal com loop automatico |

---

## SEQUENCIA DE MENSAGENS DO FUNIL COMPLETO (WhatsApp)

### Fase 1: Pre-Webinario (Nutricao + Antecipacao)

| # | Dia Relativo | Categoria | Tema |
|---|-------------|-----------|------|
| 1 | Dia 1 (quarta) | Nutricao | Boas-vindas + compromisso |
| 2 | Dia 2 (quinta) | Nutricao | Presente/e-book + mudar nome do grupo |
| 3-10 | Dia 2-6 | Nutricao | Conteudo de valor (1 msg/dia maximo) |
| 11 | Dia 6 (segunda) | Antecipacao | "Amanha e o dia" |
| 12 | Dia 7 (terca AM) | Antecipacao | "Hoje e o dia" |
| 13 | Dia 7 (terca 19:45) | Antecipacao | "Faltam 15 minutos" (marcar todos) |
| 14 | Dia 7 (terca 20h) | Webinario | "Estamos ao vivo - LINK" (marcar todos) |

### Fase 2: Pos-Webinario (Ampliacao + Fechamento)

| # | Dia Relativo | Categoria | Tema |
|---|-------------|-----------|------|
| 1 | Dia 7 (terca 22h) | Ampliacao | "Aula foi incrivel" + pedidos de replay |
| 2 | Dia 8 (quarta AM) | Replay | Anuncio do replay disponivel + link |
| 3 | Dia 9 (quinta 8:30) | Fechamento | "Hoje e um dia importante" - anuncio de fechamento |
| 4 | Dia 9 (quinta 9:30) | Fechamento | ABRIR GRUPO + "Grupo aberto, manda duvidas" |
| 5-N | Dia 9 (quinta 10-20h) | Fechamento | MANUAL: depoimentos, oferta, garantia, objecoes |
| N+1 | Dia 9 (quinta 20h) | Urgencia | "Faltam 2 horas" |
| N+2 | Dia 9 (quinta 21h) | Urgencia | "O que esta te impedindo?" |
| N+3 | Dia 9 (quinta 21:30) | Urgencia | "Vamos fechar em 3, 2, 1" (marcar todos) |
| N+4 | Dia 9 (quinta 22h) | Encerramento | FECHAR GRUPO + "Inscricoes encerradas" |
| (Opcional) | Dia 10 (sexta) | Downsell | Reabertura temporaria |
| (Opcional) | Dia 10 (sexta 22h) | Encerramento final | Fechamento definitivo |

### Fase 3: Grupo de Conteudo (Long-term)

- Sem cronograma fixo
- Conteudo de valor periodico
- Divulgacao de lives, podcasts, videos
- Convites para novos webinarios/eventos

---

---

A analise completa foi compilada acima. Todos os 17 arquivos dos Modulos 5 e 6 foram lidos e processados. Segue um resumo das principais entregas:

**Modulo 5 (10 aulas)** cobriu toda a configuracao tecnica do EverWebinar:
- Configuracao do webinario automatico (agendamento, video, moderadores)
- Pagina de captura (padrao vs. propria, one-click registration)
- Disparo de emails segmentados (pre e pos-webinario com 7 segmentos de comportamento)
- Integracoes (ActiveCampaign, Facebook Pixel, SMTP, SMS)
- Pagina de obrigado (com pesquisa integrada)
- Sala do webinario (7 tipos de eventos programaveis, chat simulado, participantes dinamicos)
- Teste end-to-end
- Implementacao tecnica com GreatPages, Elementor e WordPress/WPCode

**Modulo 6 (7 aulas)** cobriu toda a automacao de grupos de WhatsApp com o SendFlow:
- Sistema de 2 campanhas (Fase 1 pre-webinario + Fase 2 pos-webinario + Grupo de Conteudo)
- Criacao automatica de grupos (limite 250 pessoas, deep link, Facebook Pixel)
- Mensagens automaticas com cronograma semanal
- Modelos de mensagem por categoria (oferta, depoimentos, objecoes)
- Transferencia manual de grupos entre campanhas
- Webhooks com plataforma de pagamento (remover compradores, boas-vindas, tags)