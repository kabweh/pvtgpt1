# ai_tutor_project/upload_manager.py
import os
from uuid import uuid4
from pdf_handler import parse_pdf
from docx_handler import parse_docx
from image_handler import parse_image

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

class UploadManager:
    @staticmethod
    def save(uploaded_file):
        ext = uploaded_file.name.split('.')[-1]
        filename = f"{uuid4()}.{ext}"
        path = os.path.join(UPLOAD_DIR, filename)
        with open(path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        # parse accordingly
        if ext == 'pdf':
            text = parse_pdf(path)
        elif ext == 'docx':
            text = parse_docx(path)
        else:
            text = parse_image(path)
        return {"path": path, "text": text}
