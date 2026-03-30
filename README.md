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


## Use:
    LLM → LLaMA 3 via Ollama
    Embeddings → nomic-embed-text
    Vector DB → Chroma
    Backend → FastAPI

## Naive RAG Application (Ollama + ChromaDB + FastAPI)

    This is a production-ready Naive RAG (Retrieval-Augmented Generation) application built with FastAPI, ChromaDB, and local Ollama LLMs.

    It allows you to query your documents semantically using a local LLM.

## What is Naive RAG?

    Naive RAG is a simple Retrieval-Augmented Generation pipeline:

    Convert documents into embeddings (vectors).
    Split documents into chunks.
    Store chunks in a vector database (ChromaDB).
    When a user asks a question, find similar chunks.
    Send the chunks + query to a local LLM to generate an answer.

    Use cases:
    FAQ bots
    Internal knowledge search
    Simple support systems

    Pros: Easy, low-cost, fast
    Cons: Weak reasoning, may miss deeper connections

## Requirements
    Python 3.13+
    Ollama
    installed and running (ollama serve)

    Models downloaded:
    ```
    ollama pull llama3
    ollama pull nomic-embed-text

    ```

    Python dependencies:
    ```
    pip install -r requirements.txt
    ```

## How to Run
1. Index your documents
   ```
   python -c "from app.ingestion.indexer import index_documents; index_documents()"
   ```

   This will load documents from data/docs/, chunk them, generate embeddings, and store them in ChromaDB.

2. Start the FastAPI server
    ```
    uvicorn app.main:app --reload
    ```
    The API will be available at:
    ```
    http://localhost:8000
    ```

3. Test the API
    ```
    curl -X POST http://localhost:8000/query \
    -H "Content-Type: application/json" \
    -d '{"query": "What is AI and usage of database and python here?"}'
    ```