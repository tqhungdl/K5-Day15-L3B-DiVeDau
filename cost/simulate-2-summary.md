# Tóm tắt mô phỏng simulate-2@20261128-131515

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| hoi_mot_lan | 25 | 1 | 64 | 50 | 0.1 | 1.2 |
| su_co_trong_ngay | 16 | 3 | 262 | 188 | 0.3 | 3.6 |
| mat_ho_chieu_nhieu_ngay | 9 | 3 | 287 | 200 | 0.3 | 3.7 |

Tỉ lệ đạt dùng để tính: 15/15 (100%) — lượt run-2@20261128-092056

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from). ⚠️ Lượt này chạy bằng gpt-4o-mini, mô phỏng đo trên gpt-6-luna — khác model.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (90 người) | Chi phí / tháng — cơ sở (440 người) | Chi phí / tháng — cao (880 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-6-luna (vào 0.1 · ra 0.5 $/1M) | $0.000077 | $0.000077 | $0.000039 | $0.0116 | $0.0568 | $0.1136 | $0.00013 |
| gpt-6.1-terra (vào 1.0 · ra 5.0 $/1M) | $0.00077 | $0.00077 | $0.00039 | $0.1162 | $0.5681 | $1.14 | $0.0013 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-6-luna. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
