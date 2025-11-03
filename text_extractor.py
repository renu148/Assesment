import fitz
import docx2txt

def extract_text(path, filename):
    if filename.lower().endswith(".pdf"):
        doc = fitz.open(path)
        return " ".join(page.get_text("text") for page in doc)
    elif filename.lower().endswith(".docx"):
        return docx2txt.process(path)
    else:
        raise ValueError("Unsupported file type")
