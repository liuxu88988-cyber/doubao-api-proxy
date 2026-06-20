from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# 读取环境变量
load_dotenv()

API_KEY = os.getenv("DOUBAO_API_KEY")

app = FastAPI()


class ChatRequest(BaseModel):
    model: str
    messages: list


@app.get("/")
def home():
    return {
        "status": "running"
    }


@app.post("/v1/chat/completions")
def chat(request: ChatRequest):

    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": request.model,
        "messages": request.messages
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    return response.json()