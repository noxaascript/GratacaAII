import streamlit as st

def load_css():
    st.markdown("""
        <style>
        /* Desain Chat Bubble Mewah */
        .stChatMessage {
            background: rgba(255, 255, 255, 0.05) !important;
            border-radius: 20px !important;
            border: 1px solid #00d4ff !important;
            padding: 15px !important;
            margin: 10px 0 !important;
        }
        /* Sidebar Glowing */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0e1117 0%, #1a1c23 100%) !important;
            border-right: 2px solid #00d4ff;
        }
        /* Input Field */
        .stChatInputContainer { padding-bottom: 30px; }
        h1 { color: #00d4ff; text-align: center; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; }
        </style>
    """, unsafe_allow_html=True)
  
