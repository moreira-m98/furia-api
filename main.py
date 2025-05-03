import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configuração do CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP, incluindo OPTIONS
    allow_headers=["*"],  # Permite todos os headers
)

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1" # compound-beta-mini


class MessageRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(data: MessageRequest):
    user_message = data.message
    messages = [
        {"role": "system", "content": "Você é um assistente da FURIA."},
        {"role": "user", "content": user_message}
    ]
    response = openai.ChatCompletion.create(
        model="compound-beta-mini",
        messages=messages
    )
    bot_message = response['choices'][0]['message']['content']
    return {"response": bot_message}



