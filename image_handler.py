# ai_tutor_project/image_handler.py
import pytesseract
from PIL import Image

def parse_image(path: str) -> str:
    img = Image.open(path)
    return pytesseract.image_to_string(img)
