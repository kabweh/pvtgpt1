# ai_tutor_project/docx_handler.py
from docx import Document

def parse_docx(path: str) -> str:
    doc = Document(path)
    return '\n'.join([p.text for p in doc.paragraphs])
