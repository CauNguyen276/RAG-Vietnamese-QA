import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def extract_text_from_pdf(pdf_path, output_dir="data"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    output_path = os.path.join(output_dir, "extracted_text.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    chunk_dir = os.path.join(output_dir, "chunks")
    if not os.path.exists(chunk_dir):
        os.makedirs(chunk_dir)
    for i, chunk in enumerate(chunks):
        with open(os.path.join(chunk_dir, f"chunk_{i}.txt"), "w", encoding="utf-8") as f:
            f.write(chunk)
    return chunks

if __name__ == "__main__":
    pdf_path = "data/Chu_tich_Ho_Chi_Minh.pdf"
    chunks = extract_text_from_pdf(pdf_path)
    print(f"Đã trích xuất {len(chunks)} đoạn văn.")