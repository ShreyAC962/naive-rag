# Vector Search
import chromadb
from app.config import CHROMA_DB_DIR, COLLECTION_NAME
from app.rag.embedder import get_embeddings

# “Persistent” means data is stored on disk and not lost when the program stops.
client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

def retrieve(query : str, k : int = 3):
    query_embedding = get_embeddings(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    # Chroma returns results as a nested list because it supports batch queries. Since I pass a single query, I extract the first element using [0] to get the relevant document chunks.
    return results["documents"][0]