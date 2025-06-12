import numpy as np 
from embedding import embed_text
from vectore_store import load_faiss

def retrieve_top_k(query: str, k: int = 3):
    q_vec = np.array(embed_text(query), dtype="float32").reshape(1, -1)
    index = load_faiss()
    distances, indices = index.search(q_vec, k)
    return indices[0].tolist(), distances[0].tolist()