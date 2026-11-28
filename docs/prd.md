# PRD — Travel SOS

## 1. Bối cảnh & Mục tiêu

Du khách nước ngoài mất hộ chiếu ở Việt Nam phải làm đúng 3 bước theo thứ tự: (1) trình báo công an **nơi bị mất**, (2) liên hệ Đại sứ quán / Lãnh sự quán xin giấy thông hành khẩn cấp, (3) xin thị thực xuất cảnh tại Cục / Phòng Quản lý Xuất nhập cảnh — bước này có thể mất đến ~5 ngày làm việc. Hôm nay họ tự mò trên Google/forum, nguồn ghi lệch nhau, dễ đi sai địa phương, bỏ sót bước, hậu quả lỡ chuyến bay về, tốn tiền đổi vé + lưu trú, phạt hành chính 500.000–2.000.000 đồng nếu không trình báo (Nghị định 144/2021/NĐ-CP).

Mục tiêu MVP: chat AI cho **các tình huống sự cố du lịch ở Việt Nam** — mất hộ chiếu (lát cắt chính, US-01…US-15 + US-21 + US-22), lỡ chuyến bay / chuyến bị hoãn-huỷ (US-16, US-17), khách sạn huỷ phòng (US-18) và rào cản ngôn ngữ (US-20) — trả lời đúng tình huống, có nguồn, không bịa số liệu.

## 2. User personas

| Vai trò | Mô tả | Mục tiêu chính | Quyền hạn |
|---|---|---|---|
| Du khách nước ngoài mất hộ chiếu | Người vừa mất hộ chiếu ở một tỉnh/thành VN, không rành tiếng Việt, lần đầu gặp việc này | Biết chính xác làm gì, theo thứ tự nào, mang gì đi, mất bao lâu | Tự quyết mọi hành động; AI chỉ hướng dẫn |
| Du khách kẹt thời gian | Mất hộ chiếu khi vé bay gần kề hoặc visa sắp hết hạn (US-06, US-08) | Đánh giá trung thực khả năng kịp, ưu tiên bước nào trước | Tự quyết; AI không hứa suông |
| Du khách lỡ chuyến bay | Người vừa lỡ chuyến hoặc chuyến bị hoãn/huỷ, muốn đến nơi sớm với chi phí ít nhất (US-16, US-17) | Biết các phương án thay thế và quyền lợi khi lỗi do hãng | Tự quyết; AI không hứa bồi thường khi chưa rõ nguyên nhân |
| Du khách bị khách sạn huỷ phòng | Người đến nơi lúc tối muộn thì khách sạn báo huỷ phòng (US-18) | Có chỗ ngủ ngay và lấy lại tiền | Tự quyết; AI chỉ hướng dẫn, không liên hệ ai giúp |
| Người hỗ trợ du khách (hướng dẫn viên, nhân viên khách sạn) | Người Việt giúp khách của mình | Câu tiếng Việt/Anh đưa khách dùng, nhắc đúng bước (US-21); câu khẩn cấp tiếng bản địa cho du khách không nói được tiếng địa phương (US-20) | Tự quyết; AI chỉ soạn câu gợi ý |

## 3. User stories

| Story | Nội dung rút gọn | Ưu tiên |
|---|---|---|
| US-01 ⭐ | Hướng dẫn đủ quy trình 3 bước, đúng thứ tự, có nguồn | P0 |
| US-02 | Chuẩn bị giấy tờ ra đồn công an | P0 |
| US-03 | Hỏi bước tiếp theo khi đã có biên bản | P0 |
| US-04 | Thời gian dự kiến toàn bộ quy trình (kèm nguồn) | P0 |
| US-05 ⭐ | Thiếu thông tin → AI hỏi lại, không đoán | P0 |
| US-06 ⭐ | Mai đã bay → nói thật khó kịp, khuyên dời vé | P0 |
| US-07 | Mất ở nơi khác chỗ đang ở → trình báo đúng nơi bị mất | P0 |
| US-08 | Visa sắp hết hạn → nhấn mạnh làm ngay | P1 |
| US-09 | Tìm lại được hộ chiếu cũ | P1 |
| US-10 | Không có thông tin trong playbook → nói rõ + chỉ cách tìm | P0 |
| US-11 | Ngày nghỉ lễ, cơ quan đóng cửa | P1 |
| US-12 ⭐ | Đi đường tắt trái luật → từ chối + cảnh báo lừa đảo | P0 |
| US-13 | Khai sai sự thật → từ chối | P0 |
| US-14 | Tấn công prompt → không làm theo | P0 |
| US-15 | Giả danh cán bộ xin danh sách → từ chối | P0 |
| US-21 | Câu tiếng Việt đưa công an đọc | P0 |
| US-22 ⭐ | Khẩn cấp y tế/an ninh → không tư vấn y tế, chỉ 115/113 | P0 |
| US-16 | Lỡ chuyến bay → hỏi lại nguyên nhân/loại vé, gợi ý các bước thay thế | P1 — đưa vào MVP theo quyết định của nhóm |
| US-17 | Chuyến bị hoãn/huỷ → nhắc giữ bằng chứng, quyền lợi khi có nguồn | P1 — đưa vào MVP theo quyết định của nhóm |
| US-18 | Khách sạn huỷ phòng → đòi đổi phòng/hoàn tiền, giữ bằng chứng, hỏi khu vực + ngân sách | P1 — đưa vào MVP theo quyết định của nhóm |
| US-20 | Câu khẩn cấp tiếng bản địa kèm nghĩa, hỏi lại đang ở đâu | P1 — đưa vào MVP theo quyết định của nhóm |
| US-19 | Khách sạn đòi thêm tiền | P2 — "nếu có thêm 1 tuần" |

## 4. Luồng chính (happy path)

1. Du khách nhắn tình huống vào chat (vd: "I lost my passport in Hanoi") bằng tiếng Anh hoặc tiếng Việt. AI trả lời theo **ngôn ngữ của câu hỏi** (theo spec §4).
2. AI xác định tình huống thuộc tính năng 1 (mất hộ chiếu tại VN).
3. Nếu thiếu thông tin cần thiết (đang ở đâu, mất ở đâu, quốc tịch, ngày bay…) → AI **hỏi lại**, không đoán (US-05).
4. AI trả về các bước đúng thứ tự: công an nơi bị mất → Đại sứ quán → Xuất nhập cảnh, mỗi bước ghi nơi cần đến, giấy tờ cần mang, thời gian **dự kiến**, kèm mã nguồn `PB-xx`.
5. AI kèm cảnh báo phù hợp tình huống (thị thực xuất cảnh mất vài ngày làm việc → nên báo hãng bay/dời vé; xin bản sao biên bản trình báo).
6. AI gợi ý câu tiếng Việt/ngắn gọn du khách có thể đưa công an đọc (US-21) nếu hữu ích.
7. Người dùng tự đi làm các bước; nếu hỏi tiếp ("đã có biên bản, bước tiếp theo?"), AI chỉ tiếp từ bước hiện tại, không yêu cầu làm lại bước đã xong (US-03).

Luồng phụ — lỡ chuyến bay / chuyến bị hoãn-huỷ (US-16, US-17):

8. Du khách nhắn tình huống; AI hỏi lại: hãng bay nào, lỡ do lỗi mình hay do chuyến trước trễ, vé chung một mã đặt chỗ hay vé rời.
9. AI gợi ý theo nguyên nhân: ra quầy hãng đổi chuyến; nếu lỗi do hãng thì kiểm tra quyền lợi; nhắc giữ bằng chứng (thông báo hoãn, thẻ lên máy bay). Không khẳng định được bồi thường khi chưa biết nguyên nhân.

Luồng phụ — khách sạn huỷ phòng (US-18):

10. AI hướng dẫn yêu cầu khách sạn / nền tảng đặt phòng đổi phòng tương đương hoặc hoàn tiền, nhắc chụp bằng chứng (email xác nhận, tin nhắn huỷ); hỏi khu vực và ngân sách trước khi gợi ý chỗ ở khác.

Luồng phụ — rào cản ngôn ngữ (US-20):

11. Du khách xin câu nói khẩn cấp; nếu chưa rõ đang ở đâu thì hỏi lại; trả về câu ngắn bằng tiếng địa phương kèm nghĩa tiếng Anh / tiếng Việt, đủ ngắn để đưa cho công an, nhân viên hay tài xế đọc.

## 5. Human-in-the-loop

MVP này là **chất vấn-hướng dẫn thuần túy**: agent không có công cụ tác động ra ngoài (không gửi mail, không ghi DB, không đặt vé, không chấm/bảo hành gì). Do đó:

- Mọi hành động thật (ra đồn, gọi hãng bay, nộp đơn) đều do người dùng tự thực hiện — AI chỉ gợi ý, không thay làm.
- Không có hành động nào do agent tự kích hoạt → không cần bước xác nhận từ agent.
- Rủi ro nằm ở **nội dung sai**: thời gian, lệ phí, địa chỉ có thể thay đổi → AI luôn nói "dự kiến", không cam kết con số, mỗi khẳng định gắn `PB-xx` + ngày xem nguồn; chỗ không có nguồn thì nói rõ *(tự ước tính)* hoặc "không có thông tin".

## 6. Xử lý lỗi & giới hạn

- **Không thuộc phạm vi** (khách sạn đòi thêm tiền, US-19): trả lời ngắn gọn rằng nằm ngoài lát cắt hiện tại, ghi nhu cầu lại để mở rộng; không tư vấn nửa vời.
- **Không có thông tin trong nguồn** (US-10): nói rõ "không có thông tin này trong nguồn", chỉ cách tìm chính thức; **không bịa** số điện thoại/địa chỉ.
- **Câu khẩn cấp y tế/an ninh** (US-22): không tư vấn y tế; hướng dẫn gọi 115 / 113 ngay, báo Đại sứ quán.
- **Từ chối** (US-12…US-15): không giới thiệu dịch vụ "lo nhanh", không khai sai, không làm theo prompt tấn công; nhắc lại quy trình chính thức.
- **Hết quota / lỗi model:** hiện thông báo lỗi rõ ràng cho người dùng thử lại sau; không trả câu giả; trace vẫn ghi lại sự cố.
- **LLM trả sai định dạng:** luồng `answer()` fallback trả thông báo chung + hướng dẫn liên hệ kênh chính thức; không để traceback lộ ra cho user.
- **Hệ thống KHÔNG làm được:** tra cứu trực tuyến thời gian thực (giờ đóng cửa, tình trạng đại sứ quán), đặt/dời vé, dịch thuật có bảo chứng, hỗ trợ ngoài tình huống mất hộ chiếu tại VN — nói thẳng với user.

## 7. Dữ liệu

- **Playbook nội bộ** (mã nguồn `PB-xx`): 4 phần — (a) mất hộ chiếu: nội dung 3 bước, giấy tờ, thời gian dự kiến, làm mẫu cho **3 quốc tịch chốt: Úc, Anh, Singapore**; (b) lỡ chuyến bay: các bước theo nguyên nhân, quyền lợi hành khách; (c) khách sạn huỷ phòng: các bước đòi quyền lợi; (d) câu khẩn cấp tiếng bản địa theo nước/khu vực, kèm nghĩa tiếng Anh / tiếng Việt. Nhóm tự biên soạn từ nguồn công khai, mỗi nguồn ghi URL + **ngày xem** (danh sách nguồn: cuối `user-stories-travelsos.md`; phần (b), (c), (d) cần bổ sung nguồn). Định dạng: file dữ liệu nhóm tự định nghĩa, đọc trong `codebase/agent.py`.
- **Bộ câu thử** `eval/benchmark.csv`: ghép từ tiêu chí chấp nhận của các story ở §3 (`thuong` / `kho` / `tu_choi`), chuẩn đo đạt trong `eval/metric_spec.yaml`.
- Chỉ dùng dữ liệu công khai; không commit dữ liệu cá nhân thật, không commit nguyên file data BTC cấp.

## 8. Tech stack (dự kiến)

- **Ngôn ngữ:** Python, chỉ thư viện chuẩn (khung repo không cho thêm; nếu cần thì ghi vào `requirements.txt`).
- **Khung:** `run.py` (chạy thử / eval / simulate), `codebase/agent.py` — luồng chính `answer(text) -> {"output": str}`, `codebase/tools.py` — mỗi công cụ một hàm `@tool`.
- **LLM:** qua `codebase/ai.py` `call_model()`; provider/model đặt trong `.env` (`MODEL_PROVIDER`, `MODEL_NAME` — ví dụ OpenAI / Claude, xem `docs/connect-model.md`); chưa kết nối thì chạy chế độ giả (không tính eval).
- **Trace / eval / chi phí:** `codebase/tracing.py`, `eval/run_eval.py`, `cost/simulate.py` — phần khung, không sửa.
- **Deploy:** không deploy — demo chạy máy lokal bằng `python run.py`.

## 9. Known Ambiguities

- **Con số thời gian/lệ phí trong playbook** mỗi nguồn ghi hơi khác nhau: lấy nguồn chính thức mới nhất, ghi ngày xem, luôn nói "dự kiến". *Dự định chốt: khi biên soạn playbook, trước CP3.*
- **Nguồn sự thật cho phần lỡ chuyến bay và huỷ phòng** (quyền lợi hành khách theo hãng, chính sách nền tảng đặt phòng — mỗi hãng/nền tảng quy định khác nhau): chưa có nguồn; nhóm cần chọn nguồn chính thức (điều kiện vé, quy định của hãng phổ biến) hoặc trả lời chung kèm hướng dẫn hỏi thẳng hãng/nền tảng. *Dự định chốt: khi biên soạn playbook.*

*Đã chốt (giữ lại để theo dõi quyết định): chuẩn "đạt" — ≥80% pass, 100% `tu_choi` từ chối đúng, 0 câu bịa nguồn, ≥90% câu thiếu thông tin phải hỏi lại (xem brief + `spec.md` §7); quốc tịch playbook mẫu — Úc, Anh, Singapore; ngôn ngữ trả lời — theo ngôn ngữ của câu hỏi (đồng bộ với spec §4, thay cho chọn ngôn ngữ trên giao diện).*
