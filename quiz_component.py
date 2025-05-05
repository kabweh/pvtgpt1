# ai_tutor_project/quiz_component.py
import streamlit as st
from quiz_generator import QuizGenerator

def show_quiz(text: str):
    gen = QuizGenerator()
    questions = gen.generate(text)
    st.write("### Quiz Time!")
    for idx, q in enumerate(questions, 1):
        st.radio(f"{idx}. {q}", options=["A", "B", "C", "D"], key=f"q{idx}")
