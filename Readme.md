Codigos Usados:
cd app - ir para pasta app onde o requirements.txt esta

pip install --no-cache-dir -r requirements.txt

docker compose up -d --build  

codigo usados: para enviar a mensagem pelo terminal no powershell dps de fazer o docker compose up

Invoke-RestMethod -Uri 'http://localhost:8000/enviar' `
  -Method POST `
  -ContentType 'application/json' `
  -Body '{"nome": "Alice", "texto": "Ola do FastAPI!"}'


Invoke-RestMethod -Uri 'http://localhost:8000/enviar' `
    -Method POST `
    -ContentType 'application/json' `
    -Body '{"nome": "Alice", "texto": "Ola do FastAPI2!"}'

docker logs -f consumer
para ver o log de mensagens

exemplo ja funcionando:

PS C:\Users\ALUNO\Desktop\Atividade_P2> docker logs -f consumer

Aguardando RabbitMQ subir...

Aguardando RabbitMQ subir...

Aguardando RabbitMQ subir...

 Aguardando mensagens...
 
Mensagem recebida: {'nome': 'Alice', 'texto': 'Ola do FastAPI4!'}

Mensagem recebida: {'nome': 'Alice', 'texto': 'Ola do FastAPI!'}

Mensagem recebida: {'nome': 'Alice', 'texto': 'Ola do FastAPI2!'}

Mensagem recebida: {'nome': 'Alice', 'texto': 'Ola do FastAPI3!'}


