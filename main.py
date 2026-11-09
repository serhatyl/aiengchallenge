import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class AskRequest(BaseModel):
    question: str


# TEST API KEY installation
print("API anahtarı yüklendi" if OPENAI_API_KEY else "API anahtarı bulunamadı")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(request: AskRequest):
    return {"answer": f"Sorunu aldım: {request.question}"}
