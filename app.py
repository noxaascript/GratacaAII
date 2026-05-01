import streamlit as st
import requests

# --- CONFIG ---
API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

st.set_page_config(page_title="GratacaAI Supreme", layout="centered")

# --- CSS BIAR GAK JELEK ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stChatMessage { background-color: #1e222b !important; border-radius: 15px; border: 1px solid #30363d; }
    .stChatInputContainer { padding-bottom: 2rem; }
    h1 { color: #00d4ff; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 GratacaAI Supreme")
st.markdown("<p style='text-align: center; color: #8b949e;'>Version 3.0WPPIDXM | Exclusive for KAREEMXD</p>", unsafe_allow_html=True)

# --- MODEL SELECTION ---
with st.sidebar:
    st.header("⚙️ Settings")
    model_choice = st.selectbox("Switch Model:", 
                                ["GratacaUltraFlash 3.0WPPIDXM", 
                                 "GratacaUltraCoding 5.0WPPIDXM", 
                                 "GratacaUltraZoom 4.0WPPIDXM"])
    st.divider()
    st.success(f"Mode: Friendly ✅")
    if st.button("Reset Chat"):
        st.session_state.messages = []

# --- CHAT ENGINE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Titah Anda, Yang Mulia?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Identitas Friendly
    if "Flash" in model_choice:
        sys_p = "Nama Anda GratacaUltraFlash 3.0WPPIDXM. Anda asisten yang sangat ramah, ceria, dan selalu panggil KAREEMXD 'Yang Mulia'."
    elif "Coding" in model_choice:
        sys_p = "Nama Anda GratacaUltraCoding 5.0WPPIDXM. Anda ahli teknologi yang sopan dan friendly pada KAREEMXD."
    else:
        sys_p = "Nama Anda GratacaUltraZoom 4.0WPPIDXM. Anda analis yang detail, ramah, dan sangat loyal pada KAREEMXD."

    payload = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "system", "content": sys_p}] + st.session_state.messages
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    with st.chat_message("assistant"):
        try:
            res = requests.post(URL, headers=headers, json=payload, timeout=20)
            response = res.json()['choices'][0]['message']['content']
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except:
            st.error("Waduh Yang Mulia, sinyal atau API lagi mogok. Coba lagi ya? 😊")
          
