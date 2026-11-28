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
        ("lost_passport", ["mất hộ chiếu", "thất lạc hộ chiếu", "thất lạc", "hộ chiếu bị",
                           "lost my passport", "lost passport", "missing passport", "stolen passport",
                           "passport was stolen", "passport got lost", "không thấy hộ chiếu",
                           "lost my bag", "lost the bag", "bag with my passport"]),
        ("missed_flight", ["lỡ chuyến", "missed my flight", "missed the flight", "missed flight", "trễ chuyến bay"]),
        ("flight_disrupted", ["chuyến bị hoãn", "chuyến bị huỷ", "chuyến bị hủy", "chuyến bay bị hoãn",
                              "chuyến bay bị huỷ", "chuyến bay bị hủy", "bị hoãn", "bị huỷ", "bị hủy",
                              "huỷ chuyến", "hủy chuyến", "đổi chuyến",
                              "delayed", "cancelled my flight", "flight was cancelled", "flight got cancelled",
                              "overbooked"]),
        ("hotel_cancelled", ["khách sạn huỷ", "khách sạn hủy", "huỷ phòng", "hủy phòng", "hotel cancelled",
                             "cancelled my room", "cancelled my booking", "no room available", "hết phòng",
                             "không đặt được phòng", "đặt phòng không thành công", "không có phòng",
                             "booking failed", "booking didn't go through"]),
        ("emergency_phrases", ["tiếng việt", "vietnamese", "say it in", "câu để", "viết giúp", "dịch giúp",
                               "how do i say", "phrase", "viết một câu", "viết câu", "kèm nghĩa",
                               "bằng tiếng việt", "in vietnamese", "write a sentence", "a phrase"]),
    ]
    best, best_hits = "unknown", 0
    for topic, kws in rules:
        # cụm dài, cụ thể (vd "bị huỷ phòng") tính nặng hơn từ ngắn ("bị huỷ") để
        # không nhầm huỷ phòng → chuyến bay
        hits = sum(2 if len(kw) > 8 else 1 for kw in kws if kw in t)
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


@tool
def check_output(text: str, pb_codes: list) -> dict:
    """Chặn đầu ra: lọc câu trả lời của model trước khi trả cho người dùng (spec §4 khối ④).
    Input: câu trả lời của model (str); mã PB vừa tra được (list of str).
    Output: {"output": câu trả lời đã lọc, "fixes": danh sách chỗ đã sửa}.
    Không tác động ra ngoài."""
    import re
    fixes = []
    out = text

    # 1. Mã PB không nằm trong tập vừa tra → bỏ (không để dẫn nguồn không có thật)
    def _drop_pb(m):
        code = m.group(1)
        if code in pb_codes:
            return m.group(0)
        fixes.append("bỏ mã %s không có trong căn cứ vừa tra" % code)
        return ""
    out = re.sub(r"\[(PB-\d+)\]", _drop_pb, out)

    # 2. SĐT không có trong căn cứ và không thuộc 113/114/115 → "chưa xác minh"
    def _drop_phone(m):
        num = m.group(0).strip()
        if num in ("113", "114", "115"):
            return num
        fixes.append("thay SĐT '%s' không có trong căn cứ bằng 'chưa xác minh'" % num)
        return "chưa xác minh"
    out = re.sub(r"(?<![\w./-])\+?\d[\d .-]{7,12}\d(?![\w/-])", _drop_phone, out)

    # 3. Cụm tự nhận đã làm thay người dùng → thay bằng khuyến nghị
    claims = [("I have contacted", "you should contact"), ("I contacted", "you should contact"),
              ("I have confirmed", "please confirm"), ("I confirmed", "please confirm"),
              ("I have called", "you should call"), ("I called", "you should call"),
              ("I have booked", "you should book"),
              ("mình đã liên hệ", "bạn nên liên hệ"), ("tôi đã liên hệ", "bạn nên liên hệ"),
              ("mình đã xác nhận", "bạn nên xác nhận"), ("mình đã gọi", "bạn nên gọi"),
              ("mình đã đặt", "bạn nên đặt")]
    for a, b in claims:
        if a in out:
            out = out.replace(a, b)
            fixes.append("thay cụm tự nhận '%s' → '%s'" % (a, b))

    # 4. Cụm cam kết hoàn tiền / chắc chắn kịp → gắn cảnh báo (không xoá — tránh bắt nhầm câu phủ định)
    low = out.lower()
    commits = ("guarantee", "you will get your money back", "you'll get your money back",
               "definitely get", "will definitely", "chắc chắn được hoàn tiền",
               "chắc chắn kịp", "đảm bảo được hoàn tiền", "đảm bảo kịp")
    if any(c in low for c in commits):
        out += "\n⚠️ Lời cam kết trong câu trả lời này chưa có căn cứ — hãy xác minh trực tiếp với hãng/nền tảng/cơ quan."
        fixes.append("gắn cảnh báo sau cụm cam kết")

    return {"output": out, "fixes": fixes}
