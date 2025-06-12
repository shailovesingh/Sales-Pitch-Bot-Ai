import os
import faiss
import numpy as np
from dotenv import load_dotenv

load_dotenv()
INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "faiss_index.bin")

def build_faiss_index(embeddings: list[list[float]]):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    arr= np.array(embeddings, dtype="float32")
    index.add(arr)
    return index

def save_faiss(index, filepath=INDEX_PATH):
    faiss.write_index(index, filepath)

def load_faiss(filepath=INDEX_PATH):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No FAISS index at {filepath}")
    return faiss.read_index(filepath)