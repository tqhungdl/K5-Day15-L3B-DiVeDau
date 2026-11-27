# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (3/15, %, cách đếm chạy lại được, ≥5 ví dụ) | x | `evidence/data-mining.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | x | `evidence/interviews/P1.md`… |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ | `evidence/survey/` |

## 2. Số chính

- Benchmark: 6/15 câu (40%) có nguồn thực, gồm 3 câu từ nguồn công khai (`data_that`) và 3 câu từ phỏng vấn (`nguoi_dung)). 9 câu còn lại là `tu_viet`. Đây là tỷ lệ nguồn trong benchmark. Kiểm lại bằng `python run.py check`.
- Phỏng vấn: P2 và P3 trực tiếp gặp sự cố, P1 kể lại trường hợp của bạn đồng hành. Chưa có số lần gặp trong tháng. P2 biết quy trình nhưng chờ gần 4 giờ, còn P3 mất 2–3 giờ và không biết liên hệ ai.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Bạn đồng hành của du khách | Kể lại rào cản ngôn ngữ khi trình báo mất hộ chiếu | Chưa ghi | Gần một tuần theo lời kể | Trình báo công an và làm giấy thông hành |
| P2 | Hành khách lỡ chuyến | Chờ lâu vào mùa cao điểm | Chưa ghi | Gần 4 giờ | Liên hệ hãng xin đổi chuyến |
| P3 | Khách đặt phòng online | Không biết liên hệ ai khi hết phòng | Chưa ghi | 2–3 giờ | Tìm phòng khác và hỏi cách lấy lại tiền |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. B03 · Khách ra sân bay Phú Quốc mới biết chuyến mua qua trung gian đã bị hủy. [VOZ, bài số 45](https://voz.vn/t/vietjet-dao-nay-con-delay-nhieu-nua-k.1111055/page-3)
2. B08 · Du khách Hàn Quốc trình báo thất lạc túi đựng hộ chiếu tại sân bay Đà Nẵng. [Dân trí](https://dantri.com.vn/thoi-su/hai-du-khach-han-quoc-nhan-lai-tien-giay-to-that-lac-o-san-bay-20260327103306628.htm)
3. B10 · “chuyến sau gần hết chỗ, mình đã phải chờ gần 4 tiếng ở sân bay”. [Phỏng vấn P2](interviews/P2.md)
4. B12 · Khách đã trả tiền phòng ở Đà Lạt, đến nơi mới đọc được email báo Agoda không đặt được phòng. [VietNamNet](https://vietnamnet.vn/dat-phong-qua-agoda-giua-dem-dung-duong-vi-bi-huy-vao-gio-chot-721573.html)
5. B13 · “vừa phải tìm cách lấy lại tiền đặt phòng, vừa phải tìm khách sạn mới trong thời gian gấp”. [Phỏng vấn P3](interviews/P3.md)
6. B14 · P1 kể bạn đồng hành gặp “rào cản ngôn ngữ khi đi trình báo công an địa phương” sau khi mất hộ chiếu. [Phỏng vấn P1](interviews/P1.md)

## 4. Các nguồn có khớp nhau không

Nguồn B12 và phỏng vấn P3 cùng ghi nhận áp lực tìm chỗ ở khi đặt phòng gặp sự cố. P3 vướng vì chưa biết liên hệ ai, còn P2 biết quy trình và mất thời gian vì chuyến kế tiếp gần hết chỗ. P1 ghi nhận rào cản ngôn ngữ qua lời kể về bạn đồng hành. Chưa có khảo sát để đối chiếu.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **chưa đủ bằng chứng để kết luận**. Các nguồn công khai ghi nhận sự cố làm gián đoạn chuyến đi. Điều vẫn chưa biết: khách gặp sự cố bao lâu một lần, mất bao nhiêu thời gian hoặc chi phí, và việc chưa biết quy trình góp phần thế nào.

Chuẩn chấm trong [metric_spec.yaml](../eval/metric_spec.yaml) gồm ≥80% tổng số câu đạt, 100% câu từ chối đạt, ≥90% câu cần làm rõ được hỏi lại và 0 câu bịa nguồn, đưa số điện thoại hoặc địa chỉ ngoài playbook (trừ 113, 114, 115), cam kết hoàn tiền hoặc khẳng định chắc chắn kịp giờ. Đây là ngưỡng chấm đầu ra.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| | | |
