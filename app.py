import streamlit as st
import requests
from interface import apply_design
import brain_flash, brain_pro

# MASUKKAN API KEY BARU ANDA DI SINI
API_KEY = "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"

st.set_page_config(page_title="Grataca AI", layout="wide")
apply_design()

# Sidebar untuk ganti Model
with st.sidebar:
    st.title("Grataca")
    st.write("Ecosystem Selection")
    
    if "active_model" not in st.session_state:
        st.session_state.active_model = "Flash"

    if st.button("✨ Grataca UltraFlash 3.0"):
        st.session_state.active_model = "Flash"
    
    if st.button("🛡️ Grataca UltraPro 5.0"):
        st.session_state.active_model = "Pro"
    
    st.divider()
    st.caption(f"Active: {st.session_state.active_model}")
    st.caption("Owner: KAREEMXD")

# Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Tulis titah Anda, Yang Mulia..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Ambil payload berdasarkan tombol yang dipilih
        if st.session_state.active_model == "Flash":
            payload = brain_flash.get_payload(st.session_state.messages)
        else:
            payload = brain_pro.get_payload(st.session_state.messages)
            
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        
        try:
            res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=30)
            answer = res.json()['choices'][0]['message']['content']
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except:
            st.error("Gagal memuat riset. Pastikan API Key valid, Yang Mulia.")
            
