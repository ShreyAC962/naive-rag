# Embedding logic
import requests
from app.config import OLLAMA_BASE_URL, EMBED_MODEL

def get_embeddings(text : str):
    response = requests.post(f"{OLLAMA_BASE_URL}/api/embeddings",
        json = {
        "model" : EMBED_MODEL,
        "prompt" : text
    })
    return response.json()["embeddings"]