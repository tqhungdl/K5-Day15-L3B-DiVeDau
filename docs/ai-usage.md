# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Coding agent (Mistral Vibe) | Viết khung luồng chính trong `codebase/agent.py`, `codebase/tools.py`, `codebase/web.py`; nối model thật vào `codebase/ai.py` (Gemini REST, rồi OpenAI `gpt-4o-mini`); gợi ý phân loại tình huống nặng / nhẹ bằng rule | Đọc lại từng hàm và docstring; chạy `python run.py`, `run.py eval --try` trước khi nhận; chạy eval lượt 1 (5/15 đạt) → sửa luật quyết định → lượt 2 đạt 15/15 (`eval/run-2.csv`) | Lương Thị Hồng Hạnh |
| Code bản chạy thử — nối OpenAI để chạy lượt 1 (PR #14) | Claude Code | Viết phần nối OpenAI trong `codebase/ai.py` theo `docs/connect-model.md` | Đã chạy `eval --try` (token > 0) và lượt 1 (30/30 câu, 0 lỗi); kiểm `.env` (có key) không bị commit | Ngọc Ánh (phần nối OpenAI) |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Codex | Hỗ trợ tìm các bài báo thật | Kiểm tay 15 dòng, khớp 15 | Trần Quang Hưng |
| Rà câu hỏi phỏng vấn / khảo sát | Codex | Chỉ rà câu dẫn dắt | Sửa lại câu từ | Trần Quang Hưng |
| Viết câu thử (benchmark) | Codex | Sinh các câu thử mẫu | Mỗi câu thử có `source`; lấy các câu thử mẫu và viết các câu mới dựa trên các câu mẫu đã cho | Trần Quang Hưng |
| Viết câu thử (benchmark) — mở rộng B16–B30 | Claude Code | Đề xuất câu B16–B30 (`input`, `expected`, `pass_criterion`); tìm và đọc 3 bài báo làm nguồn `data_that` cho B28–B30; rà độ phủ 4 tính năng và tỉ lệ nguồn bằng `run.py check` | Mỗi câu thử có `source`; câu tự viết ghi `tu_viet`. Người chốt phạm vi: chỉ tiếng Việt và tiếng Anh, phủ đủ 4 tính năng, mất hộ chiếu chỉ cho khách nước ngoài; chọn / bỏ câu trùng ý. | Ngọc Ánh |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` — lượt 1 (`run-1`) | Claude Code | Chấm đề xuất 30 câu lượt 1 (`eval/run-1.csv`) theo `pass_criterion`, ghi lý do ở cột `ghi_chu` | Kiểm tra thủ công 30 câu (đọc cột `ghi_chu`, kỹ 4 câu biên giới B06, B08, B22, B28), khớp 30/30 | Ngọc Ánh |
| Chấm cột `pass` — lượt 2 (`run-3`) | Claude Code | Đề xuất điểm cho `eval/run-3.csv` | Một thành viên duyệt; người thứ hai (Đào Thị Ngọc Ánh) chấm độc lập 5 đầu ra, khớp 5/5 | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
