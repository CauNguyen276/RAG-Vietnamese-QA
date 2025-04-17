import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import gradio as gr
from retriever.index_documents import create_index
from retriever.retrieve import retrieve
from generator.generate_answer import generate_answer
from extract_text import extract_text_from_pdf
import os
import shutil

def process_pdf_and_answer(pdf_file, question):
    try:
        print("Bắt đầu xử lý PDF...")  # Debug
        pdf_path = "data/uploaded.pdf"
        os.makedirs("data", exist_ok=True)  # Tạo thư mục data/ nếu chưa có

        # Sử dụng pdf_file.name để lấy đường dẫn file tạm thời
        if pdf_file is None:
            raise ValueError("Không có file PDF nào được tải lên.")
        temp_pdf_path = pdf_file.name  # Đường dẫn file tạm thời từ Gradio
        print("Đường dẫn file tạm thời:", temp_pdf_path)  # Debug

        # Sao chép file tạm thời vào data/uploaded.pdf
        shutil.copy(temp_pdf_path, pdf_path)
        print("Đã lưu PDF vào", pdf_path)  # Debug

        print("Trích xuất văn bản từ PDF...")  # Debug
        chunks = extract_text_from_pdf(pdf_path)
        print(f"Đã trích xuất {len(chunks)} đoạn văn.")  # Debug

        print("Lập chỉ mục các đoạn văn...")  # Debug
        create_index(chunks)
        print("Đã lập chỉ mục.")  # Debug

        print("Truy xuất các đoạn văn liên quan...")  # Debug
        retrieved_chunks = retrieve(question)
        print(f"Đã truy xuất {len(retrieved_chunks)} đoạn văn.")  # Debug

        print("Sinh câu trả lời...")  # Debug
        answer = generate_answer(question, retrieved_chunks)
        print("Đã sinh câu trả lời:", answer)  # Debug

        retrieved_text = "\n\n".join([f"Đoạn {i+1}: {chunk[:200]}..." for i, (chunk, _) in enumerate(retrieved_chunks)])
        return answer, retrieved_text
    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)  # In lỗi ra Terminal
        return error_message, error_message

with gr.Blocks() as demo:
    gr.Markdown("# Hệ Thống Hỏi Đáp Tiếng Việt Dựa Trên RAG")
    with gr.Row():
        pdf_input = gr.File(label="Tải lên file PDF")
        question_input = gr.Textbox(label="Nhập câu hỏi")
    submit_button = gr.Button("Gửi")
    answer_output = gr.Textbox(label="Câu trả lời")
    chunks_output = gr.Textbox(label="Các đoạn văn truy xuất")
    submit_button.click(
        fn=process_pdf_and_answer,
        inputs=[pdf_input, question_input],
        outputs=[answer_output, chunks_output]
    )

if __name__ == "__main__":
    demo.launch()