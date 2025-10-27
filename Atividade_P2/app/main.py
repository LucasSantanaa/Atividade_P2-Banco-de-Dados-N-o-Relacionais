from fastapi import FastAPI
from pydantic import BaseModel
from producer import send_message

app = FastAPI()

class Message(BaseModel):
    nome: str
    texto: str

@app.post("/enviar")
def enviar_mensagem(msg: Message):
    send_message(msg.dict())
    return {"status": "Mensagem enviada para a fila!", "mensagem": msg.dict()}
