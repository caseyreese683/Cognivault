import numpy as np
from typing import List, Dict
from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:
    def __init__(self):
        self.documents = []

    def add(self, embedding: List[float], metadata: Dict):
        self.documents.append({"embedding": embedding, "meta": metadata})

    def query(self, query_embedding: List[float], top_k: int = 3):
        if not self.documents:
            return []
        matrix = np.array([d["embedding"] for d in self.documents])
        scores = cosine_similarity([query_embedding], matrix)[0]
        top_idx = np.argsort(scores)[::-1][:top_k]
        return [self.documents[i] for i in top_idx]
