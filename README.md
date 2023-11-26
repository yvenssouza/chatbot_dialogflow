CHATBOT PARA WHATSAPP


Ferramentas:

1. Google cloud
2. dialogflow
3. app auto responder
4. ngrok
5. Flask
6. Requests


1. passo
. acessar google cloud
. crie um projeto 
. acesse iam e administrador
. acesse criar conta de serviço
. configure papel: basico e proprietario
. concluir
. ações - gerenciar chaves - adicionar chave - criar nova chave - json
essa 
.envie para seu proprio email para não perder a chave e acessar no celular
. essa chave vai servir para autenticar o dialogflow no app autoresponder


2. passo
. criar agente no dialogflow
.escolha linguagem e escolha o projeto criado no google cloud
. atualize a página do navegador e vá para aba intents
. Acesse Default Welcome Intent
. Na sessão Responses no texto digite algo em que queria perguntar ao usuário, por exemplo:  Para abrir chamado, digite 1:
. Crie uma subpasta dentro de Default Welcome Intent no intents e coloque o nome de Abrir ou qualquer nome desde que altere o nome na API compartilhada app.py
.Dentro da subpasta criada na sessão Training phrases , crie a resposta em que usuário iria responder para pergunta anterior , exemplo: 1
. adicione ações e parâmetros dentro da subpasta, exemplo: Digite seu nome: e $nome, digite o número do tipo de chamado que você deseja abrir:
1 - REQUISIÇÃO
2- INCIDENTE

.Em Fulfillment habilite a primeira opção 


3. NGROK
acesse o site oficial da ngrok e crie seu login e crie seu token 
.\bgrok.exe config add-authtoken <TOKEN>
.\ngrok.exe http 5000

OBS: VOCÊ SÓ VAI EXECUTAR ESSES DOIS COMANDOS NO TERMINAL DO VS CODE, DEPOIS QUE NO PRIMEIRO TERMINAL EXTIVER INSTALADO O FLASK E REQUEST , ATIVADO O AMBIENTE VIRTUAL E DEPOIS EXECUTAR O APP.PY COM O COMANDO 'Flask run', DEIXE RODANDO ESSE COMANDO E ABRA O SEGUNDO TERMINAL E EXECUTE OS DOIS COMANDOS DO NGROK QUE PASSEI AI EM CIMA.

.Fazendo isso o NGROK irá criar uma url e essa url irá ser usada no gialogflow na aba Fulfillment insira a url e salve .


pronto! você já pode testar no dialogflow o chat de teste que eles oferecem


-INTEGRAÇÃO COM O WHATSAPP
-baixe e instale o app AUTO RESPONDER WA
crie uma regra e dentro desse regra configure para a opção dialogflow, ele irá solicitar uma chave que foi criada google cloud e se você seguiu minhas instruções desde o começo ele estará na caixa de entrada do seu email.
Baixe a chave e insira no auto responder

como funciona?
o auto responder funciona a base de notificações de mensagens do whatsapp do seu celular, ou seja, não abra o app do whastapp .
 









