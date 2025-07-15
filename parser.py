import requests
import pdfplumber
from PIL import Image
import io
import os

# Use your API key from OCR.Space
OCR_SPACE_API_KEY = "OCR_API_KEY"

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def extract_text_from_image(file, api_key=OCR_SPACE_API_KEY):
    try:
        # Convert the uploaded file to binary
        image_bytes = file.read()

        # Send image to OCR.space API
        response = requests.post(
            url="https://api.ocr.space/parse/image",
            files={"file": ("image.jpg", image_bytes)},
            data={
                "apikey": api_key,
                "language": "eng",
                "isOverlayRequired": False,
                "OCREngine": 2  # Engine 2 supports handwriting better
            },
        )

        result = response.json()

        if result.get("IsErroredOnProcessing"):
            return f"❌ OCR API Error: {result.get('ErrorMessage', 'Unknown error')}"

        parsed = result.get("ParsedResults")
        if parsed and len(parsed) > 0:
            return parsed[0].get("ParsedText", "").strip() or "❌ No text detected."
        else:
            return "❌ OCR failed to return parsed results."

    except Exception as e:
        return f"❌ Failed to extract text from image: {e}"
