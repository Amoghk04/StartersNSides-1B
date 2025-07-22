import faiss
import numpy as np

def build_faiss_index(chunks, dim=384):
    index = faiss.IndexFlatL2(dim)
    embeddings = np.array([chunk['embedding'] for chunk in chunks], dtype=np.float32)
    index.add(embeddings)
    return index

def search_top_k(index, embedder, query, chunks, k=5):
    query_vec = embedder.model.encode([query])[0].astype(np.float32)
    D, I = index.search(np.array([query_vec]), k)
    return [chunks[i] for i in I[0]]