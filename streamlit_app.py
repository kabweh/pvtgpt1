# ai_tutor_project/streamlit_app.py
import streamlit as st
from auth_component import auth_ui
from upload_component import *
from explanation_component import show_explanation
from tts_component import voice_playback
from quiz_component import show_quiz
from report_component import *

st.set_page_config(page_title="AI Tutor", layout="wide")

# --- Authentication ---
auth_ui()
if "user" not in st.session_state:
    st.stop()

# --- Sidebar Navigation ---
mode = st.sidebar.radio("Mode", ["Upload", "Explain", "Quiz", "Report"])

# Initialize state
if "last_text" not in st.session_state:
    st.session_state["last_text"] = ""
if "last_explanation" not in st.session_state:
    st.session_state["last_explanation"] = ""
if "user_id" not in st.session_state:
    # assign or fetch user_id from DB
    st.session_state["user_id"] = 1

# --- Main Views ---
if mode == "Upload":
    from upload_component import upload
    upload()

elif mode == "Explain":
    show_explanation(st.session_state["last_text"])
    if st.button("Speak Explanation"):
        voice_playback(st.session_state["last_explanation"])

elif mode == "Quiz":
    show_quiz(st.session_state["last_text"])

elif mode == "Report":
    send_report()
