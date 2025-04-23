# Hệ Thống Hỏi Đáp Tiếng Việt Dựa Trên RAG và PhoBERT

Hệ thống này tự động trả lời các câu hỏi tiếng Việt dựa trên tài liệu PDF, sử dụng phương pháp **RAG** (Retrieval-Augmented Generation) kết hợp với các mô hình AI tối ưu cho tiếng Việt như **PhoBERT** và **BARTpho**

## Mục Tiêu Dự Án
Xây dựng một hệ thống hỏi đáp tiếng Việt thông minh, giúp người dùng dễ dàng tra cứu thông tin từ tài liệu PDF

## Công Nghệ Sử Dụng
- **RAG**: Kết hợp truy xuất thông tin và sinh câu trả lời tự nhiên
- **PhoBERT**: Mô hình truy xuất đoạn văn liên quan (dùng Sentence Transformers)
- **BARTpho**: Mô hình sinh câu trả lời tiếng Việt (dùng Transformers)
- **Gradio**: Giao diện người dùng thân thiện
- **FAISS**: Lập chỉ mục để tìm kiếm nhanh

## Cách Sử Dụng
1. Chạy ứng dụng:
   ```bash
   python app/app.py
   ```
2. Truy cập giao diện Gradio
3. Tải file PDF vào mục "Tải lên file PDF"
4. Nhập câu hỏi (ví dụ: "Chủ tịch Hồ Chí Minh sinh năm nào?")
5. Nhận câu trả lời và các đoạn văn liên quan

## Kết Quả Dự Án
**Kết quả thành công** (câu hỏi: "Chủ tịch Hồ Chí Minh sinh năm nào?"):
![Kết quả thành công](https://raw.githubusercontent.com/CauNguyen276/RAG-Vietnamese-QA/main/images/result_success.png)

## Hướng Phát Triển
- Hỗ trợ thêm nhiều loại tài liệu (Word, text).
- Cải thiện tốc độ xử lý và độ chính xác của câu trả lời.
- Triển khai hệ thống trên nền tảng web hoặc ứng dụng di động.
