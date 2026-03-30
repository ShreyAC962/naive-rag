# Core RAG Logic

from app.rag.retriever import retrieve
from app.rag.generator import generate_answer

def rag_pipeline(query : str):
    docs = retrieve(query)
    context = "\n\n".join(docs)
    answer = generate_answer(query, context)
    return {
        "query" : query,
        "context" : docs,
        "answer" : answer
    }