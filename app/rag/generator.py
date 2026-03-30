# LLM calls
import requests
from app.config import OLLAMA_BASE_URL, LLM_MODEL

def generate_answer(query : str, context : str):
    prompt = f"""
    You are a helpful assistant.
    
    Context : {context}
    Question : {query}

    Answer:
    """
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={
            "model" : LLM_MODEL,
            "prompt" : prompt,
            "stream" : False
        }
    )
    return response.json()["response"]