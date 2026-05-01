import streamlit as st
import requests

# --- SUPREME CONFIG ---
# Gunakan API Key yang baru saja Anda buat di OpenRouter
API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

st.set_page_config(page_title="Grataca Research V1", layout="wide")

# CSS: Memaksa Sidebar dan Tombol Muncul
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #111d2b; min-width: 250px; }
    .stChatMessage { border: 1px solid #00d4ff; border-radius: 10px; }
    h1 { color: #00d4ff; text-shadow: 2px 2px #000; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 GratacaAI: Supreme Research")

# --- SIDEBAR (TOMBOL GANTI MODEL ADA DI SINI) ---
with st.sidebar:
    st.header("🧠 Research Center")
    model_choice = st.selectbox(
        "Pilih Mesin Kecerdasan:",
        [
            "GratacaUltraFlash 3.0 (Speed)",
            "GratacaUltraCoding 5.0 (Pro)",
            "GratacaUltraZoom 4.0 (Deep)"
        ],
        key="model_selector"
    )
    st.divider()
    st.write(f"Owner: **KAREEMXD**")
    st.write(f"Status: **Connected** ✅")
    if st.button("Reset All Memory"):
        st.session_state.messages = []
        st.rerun()

# --- ENGINE LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Berikan instruksi riset, Yang Mulia?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Research Identitas
    if "Flash" in model_choice:
        sys_p = "Anda GratacaUltraFlash 3.0. Respon sangat cepat, ramah, dan friendly kepada KAREEMXD."
    elif "Coding" in model_choice:
        sys_p = "Anda GratacaUltraCoding 5.0. Pakar riset teknologi dan coding. Friendly dan cerdas."
    else:
        sys_p = "Anda GratacaUltraZoom 4.0. Analisis mendalam dan strategis. Sangat loyal dan ramah."

    # Payload dengan model cadangan
    payload = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "system", "content": sys_p}] + st.session_state.messages,
        "temperature": 0.8
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/noxaascript/GratacaAI"
    }

    with st.chat_message("assistant"):
        try:
            # Gunakan st.spinner agar Yang Mulia tahu AI sedang riset
            with st.spinner(f"Sedang melakukan riset dengan {model_choice}..."):
                res = requests.post(URL, headers=headers, json=payload, timeout=30)
                res_data = res.json()
                
                if 'choices' in res_data:
                    response = res_data['choices'][0]['message']['content']
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                else:
                    st.error("API Menolak Koneksi! Coba cek API Key di OpenRouter, mungkin kena limit.")
        except Exception as e:
            st.error(f"Eror Sistem: {str(e)}")
            
