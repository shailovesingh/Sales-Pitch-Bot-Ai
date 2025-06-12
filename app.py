import streamlit as streamlit
import pickle
from groq_api import groq_chat
from retriever import retriever_top_k
from dotenv import load_dotenv

load_dotenv()
with open("chunk_metadata.pkl", "rb") as f:
    CHUNKS = pickle.load(f)

st.set_page_config(page_title="RAG-Groq Bot", layout="wide")
st.title("🔍📚 RAG-Groq Chatbot")

mode = st.radio("Choose mode:", ["Plain Chat", "RAG Chat"], horizontal=True)
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Clear Chat"):
    st.session_state.history = []

query = st.text_input("Your query:", key="input")
if query:
    st.session_state.history.append({"role":"user", "content":query})

    if mode == "Plain Chat":
        msgs = [
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user","content":query}
        ]
    else:
        ids, _ = retriever_top_k(query, k=3)
        context = "\n\n---\n\n".join(CHUNKS[i][1] for i in ids)
        prompt = (
            "Use the following context to answer the question. \n\n"
            f"{context}\n\nQuestion: {query}"
        )
        msgs = [
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user","content":prompt}
        ]

    with st.spinner("Generating..."):
        resp = groq_chat(msgs)
    st.session_state.history.append({"role":"assistant","content":resp})

for msg in st.session_state.history[::-1]:
    if msg["role"] == "user":
        st.markdown(f"**You**: {msg['content']}")
    else:
        st.markdown(f"**Bot**: {msg['content']}")