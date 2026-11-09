import os
import time

from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI

from schemas import AskRequest

load_dotenv()
app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# TEST API KEY installation
print("API anahtarı yüklendi" if OPENAI_API_KEY else "API anahtarı bulunamadı")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(request: AskRequest):
    started_at = time.perf_counter()
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=request.instructions,
        input=request.question,
    )

    latency_ms = round((time.perf_counter() - started_at) * 1000, 2)
    usage = response.usage

    return {
        "question": request.question,
        "answer": response.output_text,
        "latency_ms": latency_ms,
        "usage": {
            "input_tokens": usage.input_tokens if usage else None,
            "output_tokens": usage.output_tokens if usage else None,
            "total_tokens": usage.total_tokens if usage else None,
        },
    }
