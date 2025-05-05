# ai_tutor_project/report_generator.py
import weasyprint
from database import SessionLocal

def build_report(user_id: int) -> bytes:
    db = SessionLocal()
    # fetch scores, progress (pseudo-code)
    html = f"<h1>Progress Report for User {user_id}</h1>"
    # TODO: insert charts & tables
    pdf = weasyprint.HTML(string=html).write_pdf()
    return pdf
