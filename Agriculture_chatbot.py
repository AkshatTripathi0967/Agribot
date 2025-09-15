import streamlit as st

from streamlit_mic_recorder import speech_to_text

# Gemini client
import google.generativeai as genai
client = genai.Client(api_key="AIzaSyBY-uaVly9sOrzS7osrse9-dD1cy1ZEEQI")

# Page config
st.set_page_config(page_title="एग्रीमित्र - Agriculture Chatbot", page_icon="🌱", layout="wide")

# 🌾 Custom CSS for Agriculture Theme
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
       color: black;
       padding: 18px;
       border-radius: 10px;
       text-align: center;
       font-size: 28px;
       font-weight: 700;   
       margin-bottom: 20px;
    }

    /* Chat container */
    .chat-container {
        max-width: 800px;
        margin: auto;
    }

    /* Chat bubbles with black text */
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

    /* Sidebar style */
    .css-1d391kg {
        background: #f9f9f9 !important; /* light grey for contrast */
    }

    /* Chat input box */
    div[data-testid="stChatInput"] {
        background: white !important;
        border: 1px solid #ddd !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }
    
    div[data-testid="stChatInput"] textarea {
        background: transparent !important;
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar


# Header
st.markdown('<div class="main-title">🌾 एग्रीमित्र में आपका स्वागत है 🌾</div>', unsafe_allow_html=True)

# 🎤 Voice input
voice_input = speech_to_text(language="hi-IN", use_container_width=True, just_once=True, key="voice")

# ⌨️ Chat input
text_input = st.chat_input("जो पूछना है वो यहाँ लिखें...")

# Prefer mic input first
user_input = None
if voice_input:
    user_input = voice_input
elif text_input:
    user_input = text_input

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# If user said or typed something
if user_input:
    st.markdown(f'<div class="chat-bubble farmer">👨‍🌾 {user_input}</div>', unsafe_allow_html=True)

    # Gemini response
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=user_input
    )

    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(user_input)
    bot_text = response.text

    st.markdown(f'<div class="chat-bubble bot">🤖 {bot_text}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
