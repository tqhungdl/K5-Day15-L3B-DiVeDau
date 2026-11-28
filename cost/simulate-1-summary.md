# Tóm tắt mô phỏng simulate-1@20261128-113648

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| hoi_mot_lan | 25 | 1 | 64 | 31 | 0.1 | 1.2 |
| su_co_trong_ngay | 16 | 3 | 262 | 146 | 0.3 | 3.6 |
| mat_ho_chieu_nhieu_ngay | 9 | 3 | 287 | 162 | 0.3 | 3.7 |

Tỉ lệ đạt dùng để tính: 15/30 (50%) — lượt run-3@20261128-111029

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-3.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (90 người) | Chi phí / tháng — cơ sở (440 người) | Chi phí / tháng — cao (880 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-6-luna (vào 0.1 · ra 0.5 $/1M) | $0.000062 | $0.00012 | $0.000062 | $0.0096 | $0.0469 | $0.0937 | $0.00011 |
| gpt-6.1-terra (vào 1.0 · ra 5.0 $/1M) | $0.00062 | $0.0012 | $0.00062 | $0.0958 | $0.4686 | $0.9372 | $0.0011 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-nano. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
