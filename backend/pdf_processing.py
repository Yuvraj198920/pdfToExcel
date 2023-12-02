# pdf_processing.py
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

def pdf_to_img(pdf_path):
    return convert_from_path(pdf_path)

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

def process_pdf(pdf_path):
    images = pdf_to_img(pdf_path)
    all_text = ''
    for img in images:
        text = extract_text_from_image(img)
        all_text += text
    return all_text
