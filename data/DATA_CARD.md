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
| Dùng để làm gì | nguồn cho công cụ `search_playbook` |
| Từ đâu | dự kiến: trích / viết lại từ nguồn chính thức, mỗi đoạn ghi URL và ngày xem |
| Xử lý những bước gì | dự kiến: chia đoạn, gắn mã `PB-xx`, nhánh, từ khoá, điều kiện áp dụng |
| Số dòng / số đoạn | chưa biên soạn (dự kiến 20–40, *tự ước tính*) |
| Phiên bản / ngày lấy | chưa có |
| Nhãn | chưa có dữ liệu |
| Giới hạn | chỉ 4 nhánh (`ho_chieu`, `chuyen_bay`, `luu_tru`, `ngon_ngu`) và một đoạn cấp cứu `khan_cap`; nguồn cho lỡ chuyến / huỷ phòng chưa chốt; địa chỉ, giờ mở cửa có thể thay đổi |
