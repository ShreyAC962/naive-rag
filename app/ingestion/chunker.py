# Split text

def chunk_text(text, chunk_size = 300, overlap = 50):
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start : end])
    # If chunks are completely separate, you can lose context 
    # So we keep a small overlap between chunks
        start += chunk_size - overlap
    return chunks