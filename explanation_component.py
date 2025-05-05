# ai_tutor_project/explanation_component.py
import streamlit as st
from lesson_explainer import LessonExplainer

def show_explanation(text: str):
    explainer = LessonExplainer(api_key=st.secrets.get("MANUS_API_KEY"))
    resp = explainer.explain(text, level=st.selectbox("Difficulty", ["easy","medium","hard"]))
    # display annotated text
    st.markdown(resp['annotated_html'], unsafe_allow_html=True)
    st.session_state["last_explanation"] = resp.get("text", "")
