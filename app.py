import streamlit as st
import requests
from models import MODELS_CONFIG
from ui_components import load_css

# API KEY BARU (Pastikan ini private dan tidak kena limit)
API_KEY = "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"

st.set_page_config(page_title="GRATACA SUPREME", layout="wide")
load_css()

st.title("🛡️ GRATACA SUPREME")
st.markdown("<p style='text-align: center; opacity: 0.6;'>POWERED BY RESEARCH ENGINE V1</p>", unsafe_allow_html=True)

# SIDEBAR - TOMBOL MODEL
with st.sidebar:
    st.header("💎 ECOSYSTEM")
    # Menggunakan radio button agar tombolnya terlihat jelas
    selected_model = st.radio(
        "PILIH MODEL AKTIF:",
        list(MODELS_CONFIG.keys())
    )
    st.divider()
    st.info(f"Karakter: Friendly & Loyal\nOwner: KAREEMXD")
    if st.button("🗑️ CLEAR SYSTEM MEMORY"):
        st.session_state.messages = []
        st.rerun()

# LOGIK CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Berikan titah Anda, Yang Mulia?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        config = MODELS_CONFIG[selected_model]
        payload = {
            "model": config["id"],
            "messages": [{"role": "system", "content": config["prompt"]}] + st.session_state.messages,
            "temperature": 0.9
        }
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        
        try:
            res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=40)
            response = res.json()['choices'][0]['message']['content']
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except:
            st.error("API Error! Yang Mulia, coba cek API Key Anda atau ganti model cadangan.")
            
