# embed/embedder.py
from sentence_transformers import SentenceTransformer
import numpy as np

class MiniLMEmbedder:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_chunks(self, chunks):
        if not chunks:
            return []
        
        texts = [chunk["content"] for chunk in chunks if chunk["content"].strip()]
        if not texts:
            return []
            
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return [
            {
                "embedding": emb.tolist(),
                "heading": chunk["heading"],
                "pdf_name": chunk["pdf_name"],
                "page_number": chunk["page_number"],
                "content": chunk["content"]
            }
            for chunk, emb in zip(chunks, embeddings)
            if chunk["content"].strip()
        ]
