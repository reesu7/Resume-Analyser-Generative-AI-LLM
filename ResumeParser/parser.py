import PyPDF2 as pdf

def pdf_text(file_upload):
    reader = pdf.PdfReader(file_upload)
    text = ""
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text += page.extract_text() or ""
    return text
