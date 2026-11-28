# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`):

  | Persona | Tỉ lệ | Phiên / người / tháng | Lượt hỏi / phiên |
  |---|---|---|---|
  | `hoi_mot_lan` — hỏi một việc rồi tự làm | 50% | 1 | 1 |
  | `su_co_trong_ngay` — lỡ chuyến, mất phòng | 30% | 1 | 3 |
  | `mat_ho_chieu_nhieu_ngay` — quay lại hỏi theo từng bước | 20% | 3 | 3 |

  Nguồn: tỉ lệ, số phiên, số lượt đều *(tự ước tính)*. Phỏng vấn P1–P3 và `docs/prd.md` §1 chỉ gợi ý độ dài một vụ việc.
- **Số người dùng thật** (số người dùng trong một tháng) 3 kịch bản: thấp 90 · cơ sở 440 · cao 880. Cách tính: 21,2 triệu lượt khách quốc tế năm 2025 ([Báo Chính phủ](https://en.baochinhphu.vn/print/foreign-arrivals-soar-to-record-high-in-2025-111260106100233228.htm), xem 27/11/2026) ÷ 12 × 0,5% gặp sự cố × 1% / 5% / 10% dùng, làm tròn. Ba tỉ lệ đều *(tự ước tính)*; 21,2 triệu là số lượt, không phải số người.
- **Giá** (USD / 1 triệu token vào · ra; giá chuẩn, ngữ cảnh ngắn; [trang giá OpenAI](https://developers.openai.com/api/docs/pricing), xem 27/11/2026): `gpt-6-luna` 0,10 · 0,50 — `gpt-6.1-terra` 1,00 · 5,00
- **Tỉ lệ đạt** dùng để tính: 15/30 (50%) — lượt `run-3` (là lượt 2)
- Đo token trên model `gpt-5.4-nano`, tính giá model `gpt-6-luna` và `gpt-6.1-terra`
- **Giới hạn của mô phỏng:** mỗi lượt hỏi lấy ngẫu nhiên, độc lập từ câu `thuong` và `kho` trong `eval/benchmark.csv`, không ghép ngữ cảnh lượt trước. Khi dùng thật, câu hỏi nối tiếp tốn thêm token vào. Chỉ 10 lần gọi model trên 100 lượt hỏi mô phỏng; các lượt còn lại trả câu mẫu viết sẵn hoặc câu "không rõ tình huống" nên tốn 0 token. Luật chọn câu mẫu được viết khi đã có bộ câu thử, nên với câu lạ tỉ lệ gọi model và chi phí có thể khác.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-113648` · 50 phiên · seed 42 · 0 phiên lỗi

| Persona | Số phiên | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| hoi_mot_lan | 25 | 1 | 64 | 31 | 0.1 | 1.2 |
| su_co_trong_ngay | 16 | 3 | 262 | 146 | 0.3 | 3.6 |
| mat_ho_chieu_nhieu_ngay | 9 | 3 | 287 | 162 | 0.3 | 3.7 |

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| `gpt-6-luna` | $0.000062 | $0.00012 | $0.0096 | $0.0469 | $0.0937 | $0.00011 |
| `gpt-6.1-terra` | $0.00062 | $0.0012 | $0.0958 | $0.4686 | $0.9372 | $0.0011 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact / người / tháng ([spec §2](../spec.md#§2-impact--quyết-định-chọn-guide-13)): riêng nhánh mất hộ chiếu tiết kiệm khoảng **110 phút/tháng**, tương đương **0,25 phút/người dùng/tháng** tính trên 440 người dùng mọi tính năng ở kịch bản cơ sở *(tự ước tính)*. Với 5–20 phút tiết kiệm mỗi tác vụ thành công, tổng lợi ích ước khoảng 55–220 phút/tháng.
- Chi phí / người / tháng (cơ sở): $0.00011 (`gpt-6-luna`) · $0.0011 (`gpt-6.1-terra`).
- **Kết luận một dòng — đáng làm không:** chi phí model không phải rào cản, nhưng **chưa đáng đưa vào dùng thật**: tỉ lệ đạt 50% (chuẩn ≥ 80%), câu `tu_choi` đạt 2/6 (chuẩn 100%) → sửa và đo lại.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Độ nhạy theo model: `gpt-6.1-terra` đắt gấp 10 lần `gpt-6-luna` (theo giá vào và ra).
- Độ nhạy theo tỉ lệ gọi model *(tự ước tính, ngoại suy tuyến tính)*: nếu mọi lượt đều gọi model (gấp 10 lần số lần gọi đo được), chi phí cơ sở khoảng $0.47 / tháng (`gpt-6-luna`) và $4.7 / tháng (`gpt-6.1-terra`).
- Chi phí ngoài model (hosting, lưu trữ, giờ công cập nhật playbook): chưa tính.
