import io
from PyPDF2 import PdfReader
from docx import Document

async def extract_text_from_file(file):
    contents = await file.read()
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(contents))
        return " ".join(page.extract_text() for page in reader.pages if page.extract_text())

    elif filename.endswith(".docx"):
        doc = Document(io.BytesIO(contents))
        return " ".join(p.text for p in doc.paragraphs)

    elif filename.endswith(".txt"):
        return contents.decode("utf-8")

    else:
        return 