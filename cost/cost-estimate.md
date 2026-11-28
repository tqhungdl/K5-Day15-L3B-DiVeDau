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
- **Tỉ lệ đạt** dùng để tính: __/__ (__%) — lượt `run-__` (lượt 2)
- Đo token trên model __, tính giá model `gpt-6-luna` và `gpt-6.1-terra`
- **Giới hạn của mô phỏng:** mỗi lượt hỏi lấy ngẫu nhiên, độc lập từ câu `thuong` và `kho` trong `eval/benchmark.csv`, không ghép ngữ cảnh lượt trước. Khi dùng thật, câu hỏi nối tiếp tốn thêm token vào.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-__.csv` · run ID __ · __ phiên · seed __

*(dán bảng từ `cost/simulate-N-summary.md`)*

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): __
- Chi phí / người / tháng (cơ sở, model __): __
- **Kết luận một dòng — đáng làm không:** __

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
