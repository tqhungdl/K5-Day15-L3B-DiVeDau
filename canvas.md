# Canvas — Đi về đâu · Track C

> Điền ở guide bước 1.4. CP1 17:00 Thứ Sáu 27/11: nộp bản đầu, đủ 7 dòng (dòng 4 được ghi giả thuyết + nguồn sẽ kiểm).
> CP2 19:30 Thứ Sáu 27/11: cập nhật (số bằng chứng đầu, lát cắt đã chốt) và điền dòng "Đã đổi gì so với CP1".
> Track F: chép thêm thẻ đề của nhóm (khung trong file track F) xuống dưới bảng này.

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | C - TravelSOS, hỗ trợ khách du lịch xử lý tình huống bất ngờ |
| 2 | Người dùng chính (một vai cụ thể — không phải "học viên nói chung") | Du khách nước ngoài vừa mất hộ chiếu tại Việt Nam |
| 3 | Pain một câu: ai — đang làm gì — vướng đâu — hậu quả | Du khách nước ngoài mất hộ chiếu tại Việt Nam đang tự tìm cách làm lại giấy tờ để về nước, vướng vì nguồn ghi lệch nhau, dễ đi sai địa phương hoặc bỏ sót bước, hậu quả là có thể lỡ chuyến bay, tốn tiền đổi vé và lưu trú. |
| 4 | Bằng chứng đầu — CP1: giả thuyết + nguồn sẽ kiểm · CP2: số đầu tiên + 1 trích dẫn | Giả thuyết: Khách mất thời gian, tiền bạc và công sức vì chưa biết quy trình cụ thể để giải quyết vấn đề. **Số đầu:** phỏng vấn 3 người; P2 (lỡ chuyến) và P3 (khách sạn hết phòng) tự gặp sự cố, P1 kể về người quen mất hộ chiếu; chỉ P3 được ghi là vướng vì không biết liên hệ bên nào, P2 biết quy trình. **Trích P3:** "vừa phải tìm cách lấy lại tiền đặt phòng, vừa phải tìm khách sạn mới trong thời gian gấp mà không biết chỗ nào còn phòng, giá cả có hợp lý hay không" (`evidence/interviews/P3.md`). Chưa đủ để kết luận. |
| 5 | **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả) | Du khách nước ngoài vừa mất hộ chiếu tại Việt Nam mô tả tình huống → AI chọn bước tiếp theo đúng thứ tự trong quy trình 3 bước (công an nơi mất → Đại sứ quán → Xuất nhập cảnh), hoặc hỏi lại khi thiếu thông tin, dựa trên playbook có mã nguồn `PB-xx` → đo bằng % câu benchmark đạt và 0 số liệu / địa chỉ không có nguồn. Luồng phụ: lỡ / hoãn / huỷ chuyến, khách sạn huỷ phòng, rào cản ngôn ngữ. |
| 6 | AI tự làm đến đâu + 1 dòng lý do: sai thì ai chịu gì | AI gợi ý bước tiếp theo và cho chỉ dẫn cụ thể cho khách du lịch. Khách du lịch tự liên hệ và giải quyết vấn đề. Khách phải tự xử lý tình huống vì nếu AI đưa ra lựa chọn sai thì sẽ gây mất thời gian cho người dùng và gây phiền hà người phải giải quyết. |
| 7 | Phân công có tên | Hưng - tìm hiểu bằng chứng pain, evaluation case; Đạt - vẽ sơ đồ kiến trúc AI,  ; Hạnh - xây dựng UI người dùng; Ngọc Ánh - mở rộng bộ eval |
| — | *(CP2)* Đã đổi gì so với CP1 | Thu hẹp từ "khách du lịch tự túc, mọi tình huống bất ngờ" sang luồng chính là du khách nước ngoài mất hộ chiếu tại Việt Nam, kèm 3 luồng phụ; AI dựa vào playbook có mã nguồn; thêm cách đo kết quả. |
