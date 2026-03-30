# Store in DB

import chromadb
import uuid

from app.config import CHROMA_DB_DIR, COLLECTION_NAME
from app.rag.embedder import get_embeddings
from app.ingestion.loader import load_docs
from app.ingestion.chunker import chunk_text

client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

def index_documents():
    docs = load_docs()
    for doc in docs:
        chunks = chunk_text(doc)
        for chunk in chunks:
            embeddings = get_embeddings(chunk)
            collection.add(
                ids=[str(uuid.uuid4())],
                documents=[chunk],
                embeddings=[embeddings]
            )
    print("Documents indexed")