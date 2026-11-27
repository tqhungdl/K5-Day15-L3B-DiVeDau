# Travel SOS — Brief

**Đội:** Đi về đâu   **Ngày:** 27/11/2026

## Bài toán

Du khách du lịch ở Việt Nam gặp sự cố hành trình và không biết xử lý: mất hộ chiếu (quy trình bắt buộc 3 bước phải đúng thứ tự), lỡ chuyến bay (không biết phương án thay thế và quyền lợi), hay khách sạn huỷ phòng lúc tối muộn (không biết đòi quyền lợi thế nào). Họ tự mò trên Google/forum, nguồn ghi lệch nhau, dễ đi sai bước, hậu quả là lỡ chuyến, mất tiền đổi vé và lưu trú thêm, thậm chí bị phạt hành chính 500.000–2.000.000 đồng vì không trình báo mất hộ chiếu (Nghị định 144/2021/NĐ-CP).

## Người dùng mục tiêu

- **Du khách nước ngoài vừa mất hộ chiếu ở Việt Nam** — cần quy trình 3 bước đúng thứ tự, đúng địa phương; đo bằng: trả lời đủ 3 bước có mã nguồn `PB-xx`, không bịa địa chỉ/số điện thoại (US-01, US-05, US-06).
- **Du khách đang bị kẹt thời gian (vé bay gần kề, visa sắp hết hạn)** — cần câu trả lời thật thà về khả năng kịp/mất bao lâu; đo bằng: nói rõ thị thực xuất cảnh mất vài ngày làm việc, không hứa "vẫn kịp", khuyên dời vé (US-04, US-06, US-08).
- **Du khách lỡ chuyến bay hoặc bị khách sạn huỷ phòng** — cần phương án thay thế và cách đòi quyền lợi đúng; đo bằng: hỏi lại nguyên nhân/bối cảnh trước khi gợi ý, nhắc giữ bằng chứng, không hứa bồi thường khi chưa biết nguyên nhân (US-16, US-17, US-18).

## Giải pháp

Chat AI hướng dẫn du khách xử lý sự cố hành trình ở Việt Nam, từng bước, kèm nguồn.

- AI hỏi lại thông tin thiếu (đang ở tỉnh nào, mất ở đâu, quốc tịch, ngày bay…) trước khi hướng dẫn, không tự đoán.
- Người dùng **chọn ngôn ngữ trả lời trên giao diện** (mặc định tiếng Anh).
- Trả về các bước đúng thứ tự, nơi cần đến, thời gian **dự kiến**, kèm mã nguồn playbook (`PB-xx`) và ngày xem nguồn.
- Biết nói "không có thông tin này trong nguồn" và chỉ cách tìm chính thức (US-10).
- **Lỡ chuyến bay / chuyến bị hoãn-huỷ:** hỏi lại nguyên nhân và loại vé trước khi gợi ý các bước (ra quầy hãng, kiểm tra quyền lợi, chuyến thay thế); không hứa bồi thường khi chưa biết nguyên nhân (US-16, US-17).
- **Khách sạn huỷ phòng:** hướng dẫn yêu cầu đổi phòng tương đương / hoàn tiền, nhắc giữ bằng chứng, hỏi khu vực và ngân sách trước khi gợi ý chỗ khác (US-18).
- **Rào cản ngôn ngữ:** đưa câu ngắn bằng tiếng bản địa cho tình huống khẩn cấp kèm nghĩa tiếng Anh / tiếng Việt, hỏi lại đang ở đâu nếu chưa rõ (US-20).
- Từ chối đi đường tắt trái luật, khai sai sự thật và các câu tấn công prompt/giả danh (US-12…US-15).
- Hỗ trợ câu tiếng Việt đưa công an đọc cho du khách không biết tiếng Việt (US-21 — phần nhỏ của tính năng 1).

## Vì sao cần AI

- **Bắt buộc LLM:** mỗi tình huống khác nhau (mất ở tỉnh khác nơi đang ở, mai đã bay, visa sắp hết hạn, tìm lại được hộ chiếu, lỡ chuyến do lỗi mình hay do hãng, vé chung hay rời mã đặt chỗ, bị huỷ phòng lúc tối, cần câu khẩn cấp theo đúng nước đang ở…) — AI phải hiểu tình huống tiếng Việt/tiếng Anh, hỏi lại thông tin thiếu và ghép đúng nhánh của playbook; template tĩnh không làm được (US-05, US-07…US-09, US-16, US-18, US-20).
- **Phần mềm thường:** lưu trữ và tra cứu playbook có nguồn; chấm điểm benchmark theo tiêu chí kiểm được; ghi trace.

## Không làm (Non-goals)

- **Khách sạn đòi thêm tiền mới giữ phòng** (US-19) — ghi vào "Nếu có thêm 1 tuần".
- Tra cứu số điện thoại / địa chỉ đại sứ quán ngoài playbook (US-10 chỉ chỉ cách tìm).
- Tư vấn y tế, hỗ trợ khẩn cấp y tế/an ninh — chỉ hướng dẫn gọi 115/113 (US-22).
- Mọi tác vụ có tác động ra ngoài (gửi mail, đặt/dời vé, giao dịch, liên hệ hãng/nền tảng giúp) — chỉ gợi ý bước, người dùng tự làm.

## Đo thành công bằng gì

*(đã chốt — nhóm tự đặt; ghi tương tự vào `spec.md` §7 và `eval/metric_spec.yaml` khi chốt chuẩn "đạt")*

- **≥ 80%** câu benchmark qua (`run.py score`), riêng nhóm `tu_choi` phải từ chối đúng **100%**.
- **0 câu** trả lời có địa chỉ / số điện thoại / con số không có nguồn `PB-xx`.
- **≥ 90%** câu "thiếu thông tin" (như US-05) phải hỏi lại ít nhất 2 thông tin, không tự đoán.
