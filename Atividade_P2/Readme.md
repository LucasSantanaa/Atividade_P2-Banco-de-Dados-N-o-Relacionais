codigo usados: para enviar a mensagem pelo terminal no powershell dps de fazer o docker compose up


Invoke-RestMethod -Uri 'http://localhost:8000/enviar' `
  -Method POST `
  -ContentType 'application/json' `
  -Body '{"nome": "Alice", "texto": "Ola do FastAPI!"}'
