import os, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def groq_chat(messages, model="llama3-70b-8192", temperature=0.7, max_tokens=512):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type":"application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": max_tokens
    }

    resp = requests.post(API_URL, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()