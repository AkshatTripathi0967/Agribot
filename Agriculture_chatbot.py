import streamlit as st
import google.generativeai as genai
from streamlit_mic_recorder import speech_to_text

# 🔑 Gemini client (API key from Streamlit secrets)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# 🌱 Page config
st.set_page_config(page_title="एग्रीमित्र - Agriculture Chatbot", page_icon="🌱", layout="wide")

# 🎨 Custom CSS
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: white !important;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Header */
    .main-title {
        background: #4caf50;
        color: white;
        padding: 18px;
        border-radius: 10px;
        text-align: center;
        font-size: 21px;
        font-weight: 700;   /* Bold */
        margin-bottom: 20px;
    }

    /* Chat container */
    .chat-container {
        max-width: 800px;
        margin: auto;
    }

    /* Chat bubbles */
    .chat-bubble {
        background: white;
        color: black;
        padding: 12px 18px;
        border-radius: 14px;
        margin: 8px 0;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.15);
        max-width: 70%;
        word-wrap: break-word;
        font-size: 16px;
    }

    /* Farmer (left) */
    .farmer {
        border-left: 6px solid #388e3c;
        margin-right: auto;
    }

    /* Agrimitra (right) */
    .bot {
        border-right: 6px solid #1565c0;
        margin-left: auto;
        background: #f5f5f5;
    }

    /* Sidebar */
    .css-1d391kg {
        background: #f9f9f9 !important;
    }

    

    div[data-testid="stChatInput"] textarea {
        background: transparent !important;
        color: white !important;
    }

    
    
    </style>
""", unsafe_allow_html=True)

# 🌾 Header
st.markdown('<div class="main-title">🌾 एग्रीमित्र में आपका स्वागत है 🌾</div>', unsafe_allow_html=True)

# 🎤 Voice input
voice_input = speech_to_text(language="hi-IN", use_container_width=True, just_once=True, key="voice")

# ⌨️ Chat input
text_input = st.chat_input("जो पूछना है वो यहाँ लिखें...")

# Prefer mic input first
user_input = voice_input if voice_input else text_input

# 💬 Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

if user_input:
    # Show farmer input
    st.markdown(f'<div class="chat-bubble farmer">👨‍🌾 {user_input}</div>', unsafe_allow_html=True)

    # Gemini response
    response = model.generate_content(user_input)
    bot_text = response.text

    # Show bot reply
    st.markdown(f'<div class="chat-bubble bot">🤖 {bot_text}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
