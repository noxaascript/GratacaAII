import streamlit as st
from brain import research_engine

st.set_page_config(page_title="GRATACA SUPREME", layout="wide")

# CSS Khusus Desain Chat Melengkung & Tombol Sidebar
st.markdown("""
<style>
    .stApp { background-color: #0b0e14; }
    [data-testid="stSidebar"] { background-color: #151921 !important; border-right: 1px solid #00d4ff; }
    .stChatMessage { border-radius: 25px !important; border: 1px solid #2d333b !important; background: #1c2128 !important; }
    .stChatInput { border: 1px solid #00d4ff !important; border-radius: 15px !important; }
    h1 { color: #00d4ff; font-family: 'Courier New'; text-shadow: 0 0 10px #00d4ff; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ GRATACA CORE RESEARCH")

# SIDEBAR - TOMBOL MODEL YANG JELAS
with st.sidebar:
    st.header("⚙️ SYSTEM CONTROL")
    mode = st.radio("PILIH ENGINE AKTIF:", 
                    ["GratacaUltraFlash 3.0WPPIDXM", 
                     "GratacaUltraCoding 5.0WPPIDXM", 
                     "GratacaUltraZoom 4.0WPPIDXM"])
    st.divider()
    st.markdown("**Status:** `ONLINE` ✅")
    st.markdown("**User:** `KAREEMXD` 👑")
    if st.button("🔄 REBOOT SYSTEM"):
        st.session_state.messages = []
        st.rerun()

# LOGIKA CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Titah Anda, Yang Mulia?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Tambahkan instruksi friendly secara rahasia
        sys_msg = {"role": "system", "content": f"Anda adalah {mode}. Anda sangat cerdas, ramah, dan panggil KAREEMXD 'Yang Mulia'."}
        full_history = [sys_msg] + st.session_state.messages
        
        response = research_engine(mode, full_history)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
