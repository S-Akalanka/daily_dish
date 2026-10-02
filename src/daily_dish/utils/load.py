from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
PDF_PATH = ROOT /"docs/faqs.pdf"

def load_text():
    if not PDF_PATH.exists:
        raise FileNotFoundError(f"File not found: {PDF_PATH}")

    reader = PdfReader(PDF_PATH)
    for page in reader.pages:
        print(page.extract_text())

if __name__ == "__main__":
    load_text()
    