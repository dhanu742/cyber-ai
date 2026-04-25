import streamlit as st


def load_css():

    st.markdown("""
    <style>

    .stApp {
        background: url("https://images.unsplash.com/photo-1510511459019-5dda7724fd87?q=80&w=1974&auto=format&fit=crop") no-repeat center center fixed;
        background-size: cover;
    }

    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.82);
        z-index: -1;
    }

    .block-container {
        background: rgba(10,10,10,0.88);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid #00ffcc33;
    }

    h1,h2,h3,h4,p,label,div {
        color: white !important;
    }

    .main-title {
        text-align:center;
        color:#00ffcc;
        font-size:50px;
        font-weight:bold;
        text-shadow:0px 0px 20px #00ffcc;
    }

    .terminal {
        background:black;
        color:#00ff66;
        padding:15px;
        border-radius:10px;
        border:1px solid #00ff66;
        font-family:monospace;
    }

    .stButton button {
        background: linear-gradient(90deg,#00ffcc,#0066ff);
        color:white;
        border:none;
        border-radius:10px;
        height:45px;
        font-weight:bold;
    }

    .stTextInput input {
        background-color: rgba(255,255,255,0.08);
        color: white;
        border: 1px solid #00ffcc55;
        border-radius: 10px;
    }

    section[data-testid="stSidebar"] {
        background: rgba(0,0,0,0.95);
    }

    </style>
    """, unsafe_allow_html=True)