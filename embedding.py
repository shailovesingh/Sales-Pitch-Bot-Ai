import os
from dotenv import load_dotenv
from hugginfacce_hub import InferenceClient

load_dotenv()

HF_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not HF_KEY:
    raise RuntimeError("Set HUGGINGFACE_API_KEY in your .env to use the Inference API for embeddings.")

hf_client = InferenceClient(
    repo_id = "sentence-transformers/all-MiniLM-L6-v2",
    token=HF_KEY
)

def embed_text(text: str) -> list[float]:
    """
    Sends 'text' to HuggingFace Inference API and returns its embedding vector.
    """

    respomse = hf_client.text_embeddings({"inputs":text})
    return response["embedding"]