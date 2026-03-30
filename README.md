## Naive RAG Pipeline:
    User Query
    ↓
    Convert to embedding
    ↓
    Search similar chunks (Vector DB)
    ↓
    Send context + query to LLM
    ↓
    Return answer


## se:
    LLM → LLaMA 3 via Ollama
    Embeddings → nomic-embed-text
    Vector DB → Chroma
    Backend → FastAPI