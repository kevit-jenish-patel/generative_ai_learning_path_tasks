import os

import pymupdf
import pytesseract
from pathlib import Path
from  PIL import Image

# ../brochures for __main__.py
brochures = Path("brochures")

def extract_text(file: Path) -> str:
    doc = pymupdf.open(file)
    doc_text = ""

    for page in doc:
        text = page.get_text().encode("utf-8").decode("utf-8").strip()

        if not text:
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

            text = pytesseract.image_to_string(img).strip()

        doc_text += text

    return doc_text


def get_brochures():
    brochures_data = []
    files = os.listdir(brochures)
    for filename in files:
        if filename.endswith(".pdf"):
            filepath = brochures / filename
            extracted_text = extract_text(filepath)
            brochures_data.append({"filename":filename,"text":extracted_text})

    return brochures_data


def write_brochures():
    brochures_data = get_brochures()
    with open(brochures / "brochures.txt", "w",encoding="utf-8") as f:
        for brochure in brochures_data:
            f.write("File:" + brochure["filename"] + "\n")
            f.write(brochure["text"] + "\n")


def get_text_from_brochures():
    with open(brochures / "brochures.txt", "r", encoding="utf-8") as f:
        brochures_text = f.read()

    brochures_text = brochures_text.strip()

    if brochures_text:
        return brochures_text
    else:
        print("writing brochures")
        write_brochures()
        with open(brochures / "brochures.txt", "r", encoding="utf-8") as f:
            brochures_text = f.read()

        brochures_text = brochures_text.strip()
        return brochures_text
