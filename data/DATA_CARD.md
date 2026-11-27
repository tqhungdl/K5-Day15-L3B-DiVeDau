# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Bộ câu thử (`eval/benchmark.csv`)

| | |
|---|---|
| Dùng để làm gì | bộ câu thử |
| Từ đâu | phỏng vấn (`evidence/interviews/P1.md`–`P3.md`) · nguồn công khai (URL ở cột `source`) · nhóm tự viết |
| Xử lý những bước gì | viết lại tình huống thành câu hỏi, gắn `expected`, `pass_criterion`, `type`; phỏng vấn ghi theo mã P1–P3, không ghi tên |
| Số dòng / số đoạn | 15 (thuong 6 · kho 7 · tu_choi 2); nguồn: nguoi_dung 3 · data_that 3 · tu_viet 9 |
| Phiên bản / ngày lấy | bản CP2, 27/11/2026 |
| Nhãn | hỗn hợp: 6 câu dựa trên người dùng / nguồn công khai, 9 câu tự viết |
| Giới hạn | toàn tiếng Việt, dù người dùng chính ở `spec.md` §4 là khách nước ngoài; chỉ 2 câu từ chối / tấn công; mới có 3 phỏng vấn |

## Dataset 2 · Playbook (`data/playbook.json`)

| | |
|---|---|
| Dùng để làm gì | nguồn sự thật cho công cụ `search_playbook` — agent chỉ khẳng định nội dung có trong đây, gắn mã `PB-xx` |
| Từ đâu | nhóm biên soạn lại từ nguồn công khai (Nghị định 144/2021/NĐ-CP, Cổng Cục QLXNC, trang chính thức các đại sứ quán); URL + ngày xem nhóm bổ sung trước CP3 |
| Xử lý những bước gì | chia đoạn, gắn mã `PB-xx`, từ khoá, điều kiện áp dụng; mọi con số ghi "dự kiến" |
| Số dòng / số đoạn | 8 mục (PB-01…PB-08) · 4 chủ đề |
| Phiên bản / ngày lấy | bản 1 — repo này |
| Nhãn | `synthetic` (nhóm tự viết lại từ nguồn công khai) |
| Giới hạn | nguồn cho lỡ chuyến / huỷ phòng chưa chốt → trả lời chung kèm hướng dẫn hỏi hãng/nền tảng (PRD §9); địa chỉ, giờ mở cửa có thể thay đổi |
