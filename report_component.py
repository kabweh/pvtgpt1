# ai_tutor_project/report_component.py
import streamlit as st
from report_generator import build_report
import smtplib
from email.message import EmailMessage

def send_report():
    pdf_bytes = build_report(st.session_state["user_id"])
    msg = EmailMessage()
    msg["Subject"] = "Your Child's Progress Report"
    msg["From"] = st.secrets["email"]["sender"]
    msg["To"] = ",".join(st.secrets["email"]["parents"])
    msg.set_content("Attached is the latest progress report.")
    msg.add_attachment(pdf_bytes, maintype="application", subtype="pdf", filename="report.pdf")
    with smtplib.SMTP(st.secrets["email"]["smtp_server"], port=587) as s:
        s.starttls()
        s.login(st.secrets["email"]["user"], st.secrets["email"]["pass"])
        s.send_message(msg)
    st.success("Report sent!")

# Button hookup (in main app)
st.button("Send Progress Report", on_click=send_report)
