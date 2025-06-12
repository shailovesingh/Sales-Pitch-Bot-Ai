import os, pickle
from dotenv import load_dotenv
from utils import load_texts_from_folder, chunk_text
from embedding import embed_text
from vectore_store import build_faiss_index, save_faiss

load_dotenv()

def main():
    docs = load_texts_from_folder("docs")
    chunk_metadata, embedding = [], []

    for doc_id, text in docs:
        for chunk in chunk_text(text):
            embedding.append(embed_text(chunk))
            chunk_metadata.append((doc_id, chunk))

    index = build_faiss_index(embedding)
    save_faiss(index)
    with open("chunk_metadata.pkl", "wb") as f:
        pickle.dump(chunk_metadata, f)
    print(f"Indexed {len(embeddings)} chunks.")

if __name__== "__main__":
    main()
