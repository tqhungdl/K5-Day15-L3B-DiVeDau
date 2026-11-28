"""Công cụ của bài toán — NHÓM VIẾT. Điền ở guide bước 2.2 (thiết kế) và 3.2 (code).

Mỗi công cụ là một hàm Python có @tool. Docstring ghi đúng 4 ý như sơ đồ ở spec.md §4:
    tên · input · output · có tác động ra ngoài không (gửi tin, sửa dữ liệu, chấm điểm…)
Khung tự ghi mỗi lần gọi công cụ vào trace (tên, input, output rút gọn, thời gian, lỗi).

Cả hai công cụ đều CHỈ ĐỌC dữ liệu nội bộ (data/playbook.json) — không tác động ra ngoài.
MVP này là chất vấn-hướng dẫn thuần túy (PRD §5): không có công cụ gửi mail, sửa dữ liệu,
đặt vé — mọi hành động thật do người dùng tự làm.
"""
import json
import os

from tracing import tool, TOOLS  # noqa: F401  (TOOLS: danh sách công cụ đã đăng ký, dùng khi viết vòng lặp agent)

_PLAYBOOK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "playbook.json")
_cache = None


def load_playbook() -> dict:
    """Đọc playbook nội bộ (PRD §7) — đọc mỗi file một lần rồi nhớ."""
    global _cache
    if _cache is None:
        with open(_PLAYBOOK_PATH, encoding="utf-8") as f:
            _cache = json.load(f)
    return _cache


@tool
def classify_situation(text: str) -> dict:
    """Phân loại tình huống người dùng thành chủ đề trong playbook.
    Input: câu nhắn của người dùng (str, tiếng Việt hoặc tiếng Anh).
    Output: {"topic": lost_passport|missed_flight|flight_disrupted|hotel_cancelled|emergency_phrases|unknown}.
    Không tác động ra ngoài."""
    t = " " + text.lower() + " "
    rules = [
        ("lost_passport", ["mất hộ chiếu", "thất lạc hộ chiếu", "hộ chiếu bị", "lost my passport",
                           "lost passport", "missing passport", "stolen passport", "passport was stolen",
                           "passport got lost", "không thấy hộ chiếu"]),
        ("missed_flight", ["lỡ chuyến", "missed my flight", "missed the flight", "missed flight", "trễ chuyến bay"]),
        ("flight_disrupted", ["chuyến bị hoãn", "chuyến bị huỷ", "chuyến bay bị hoãn", "chuyến bay bị huỷ",
                              "delayed", "cancelled my flight", "flight was cancelled", "flight got cancelled",
                              "overbooked"]),
        ("hotel_cancelled", ["khách sạn huỷ", "khách sạn hủy", "huỷ phòng", "hủy phòng", "hotel cancelled",
                             "cancelled my room", "cancelled my booking", "no room available", "hết phòng"]),
        ("emergency_phrases", ["tiếng việt", "vietnamese", "say it in", "câu để", "viết giúp", "dịch giúp",
                               "how do i say", "phrase"]),
    ]
    best, best_hits = "unknown", 0
    for topic, kws in rules:
        hits = sum(1 for kw in kws if kw in t)
        if hits > best_hits:
            best, best_hits = topic, hits
    return {"topic": best}


@tool
def search_playbook(query: str, topic: str = "") -> list:
    """Tra playbook nội bộ (mã nguồn PB-xx) theo từ khoá, lọc chủ đề tuỳ chọn.
    Input: câu hỏi/từ khoá (str); chủ đề (str, rỗng = tất cả, vd 'lost_passport').
    Output: danh sách mục {code, title, text, title_vi, text_vi, source}, khớp nhất trước.
    Không tác động ra ngoài."""
    pb = load_playbook()
    words = [w for w in "".join(c if c.isalnum() else " " for c in query.lower()).split() if len(w) >= 3]
    scored = []
    for e in pb["entries"]:
        if topic and e["topic"] != topic:
            continue
        hay = " ".join([e["code"], e["title"], e["text"], e["title_vi"], e["text_vi"],
                        " ".join(e["keywords"])]).lower()
        score = sum(1 for w in words if w in hay)
        score += sum(3 for kw in e["keywords"] if kw in query.lower())
        if score > 0:
            scored.append((score, e))
    scored.sort(key=lambda pair: -pair[0])
    return [e for _, e in scored[:4]]
