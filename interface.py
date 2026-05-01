import streamlit as st

def apply_design():
    st.markdown("""
    <style>
    /* Background Putih Bersih */
    .stApp { background-color: #F8F9FA; color: #212529; }
    
    /* Bubble Chat Bulat & Bersih */
    .stChatMessage {
        border-radius: 20px;
        border: 1px solid #E9ECEF;
        background-color: #FFFFFF !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        color: #212529 !important;
    }
    
    /* Sidebar Elegan */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #DEE2E6;
    }
    
    /* Tombol Model Minimalis */
    .stButton>button {
        border-radius: 10px;
        border: 1px solid #CED4DA;
        background: white;
        color: #495057;
        transition: 0.3s;
    }
    .stButton>button:hover {
        border-color: #007BFF;
        color: #007BFF;
    }
    
    h1 { font-weight: 700; color: #1A1A1A; text-align: left; }
    </style>
    """, unsafe_allow_html=True)
  
