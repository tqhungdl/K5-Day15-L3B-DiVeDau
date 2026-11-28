# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Coding agent (Mistral Vibe) | Viết khung luồng chính trong `codebase/agent.py`, `codebase/tools.py`, `codebase/web.py`; nối model thật vào `codebase/ai.py` (Gemini REST, rồi OpenAI `gpt-4o-mini`); gợi ý phân loại tình huống nặng / nhẹ bằng rule | Đọc lại từng hàm và docstring; chạy `python run.py`, `run.py eval --try` trước khi nhận; chạy eval lượt 1 (5/15 đạt) → sửa luật quyết định → lượt 2 đạt 15/15 (`eval/run-2.csv`) | Lương Thị Hồng Hạnh |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Codex | Hỗ trợ tìm các bài báo thật | Kiểm tay 15 dòng, khớp 15 | Trần Quang Hưng |
| Rà câu hỏi phỏng vấn / khảo sát | Codex | Chỉ rà câu dẫn dắt | Sửa lại câu từ | Trần Quang Hưng |
| Viết câu thử (benchmark) | Codex | Sinh các câu thử mẫu | Mỗi câu thử có `source`; lấy các câu thử mẫu và viết các câu mới dựa trên các câu mẫu đã cho | Trần Quang Hưng |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` | Claude Code | Đề xuất điểm cho `eval/run-3.csv` | Một thành viên duyệt; chưa có người thứ hai chấm độc lập 5 đầu ra | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
