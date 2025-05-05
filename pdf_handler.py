# ai_tutor_project/pdf_handler.py
import PyPDF2

def parse_pdf(path: str) -> str:
    reader = PyPDF2.PdfReader(path)
    full_text = []
    for page in reader.pages:
        try:
            text = page.extract_text()
        except:
            text = ''
        full_text.append(text)
    return '\n'.join(full_text)
