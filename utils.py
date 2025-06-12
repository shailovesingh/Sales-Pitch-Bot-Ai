import os

def load_texts_from_folder(folder_path: str) -> list[tuple[str, str]]:
    docs = []
    for fname in os.listdir(folder_path):
        if fname.endswith(".txt"):
            with open(os.path.join(folder_path, fname), "r", encoding="utf-8") as f:
                docs.append((fname, f.read()))
    return docs

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunks.append(" ".join(words[i : i + chunk_size]))
        I  += chunk_size - overlap
    return chunks