import sys
sys.path.insert(0, "/Users/tt/Downloads/3.PROJECTS/GITHUB/26AI/K5-Day15-L3B-DiVeDau/codebase")
from agent import answer

EN = "\n(Please reply in English.)"

def turn(prevs, cur):
    parts = []
    if prevs:
        parts.append("--- lượt trước (bối cảnh) ---")
        for u, a in prevs:
            parts.append("[người dùng] " + u)
            if a:
                parts.append("[agent] " + a)
    parts.append("--- lượt này ---")
    parts.append(cur)
    return "\n".join(parts) + EN

def body_sentences(out):
    """Phần nội dung (bỏ dòng Sources và câu hỏi ❓) có bao nhiêu câu."""
    body = "\n".join(ln for ln in out.splitlines()
                     if not ln.startswith("Sources:") and not ln.startswith("Nguồn:")
                     and not ln.startswith("❓") and not ln.startswith("Say \"")
                     and not ln.startswith("Nói \"") and not ln.startswith("You've seen")
                     and not ln.startswith("Bạn đã xem") and not ln.startswith("Say '"))
    return len([s for s in body.replace("\\n", " ").split(". ") if s.strip(" .")])

h = []
r1 = answer(turn(h, "I lost my passport"))["output"]; h.append(("I lost my passport", r1))
print("L1 câu:", body_sentences(r1), "|", r1.split("\n")[0][:60])
assert body_sentences(r1) <= 3

r2 = answer(turn(h, "I'm in Hanoi"))["output"]; h.append(("I'm in Hanoi", r2))
r3 = answer(turn(h, "I'm Australian"))["output"]; h.append(("I'm Australian", r3))
print("L3 câu:", body_sentences(r3), "|", r3.split("\n")[0][:60])
assert r3.startswith("STEP 1") and body_sentences(r3) <= 3
assert "stop here" in r3, "phải hỏi 'tiếp hay dừng'"

r4 = answer(turn(h, "continue"))["output"]; h.append(("continue", r4))
assert r4.startswith("STEP 2") and body_sentences(r4) <= 3 and "stop here" in r4
r5 = answer(turn(h, "next"))["output"]; h.append(("next", r5))
assert r5.startswith("STEP 3") and body_sentences(r5) <= 3 and "stop here" in r5

# summarize vẫn 3 câu + hỏi
r6 = answer(turn(h, "summarize"))["output"]
print("L6 câu:", body_sentences(r6))
assert body_sentences(r6) <= 3

# Single-turn (eval): model soạn — kiểm có câu hỏi tiếp/dừng và gọn
r7 = answer("Tôi là công dân Úc. Mất hộ chiếu hôm nay ở quận Hoàn Kiếm, Hà Nội, tôi vẫn ở Hà Nội và bay về sau hai tuần. Tôi cần làm gì theo thứ tự?" + EN)["output"]
print("\nL7 (eval 1 tin):", r7.replace("\n", " ")[:280])
assert "Tiếp" in r7 or "tiếp" in r7 or "continue" in r7.lower() or "stop" in r7.lower()

# VI: bước hỏi dừng
rv = answer(turn([], "Tôi bị mất hộ chiếu").replace(EN, "\n(Hãy trả lời bằng tiếng Việt.)"))["output"]
hv = [("Tôi bị mất hộ chiếu", rv)]
rv2 = answer(turn(hv, "Tôi đang ở Hà Nội").replace(EN, "\n(Hãy trả lời bằng tiếng Việt.)"))["output"]
hv.append(("Tôi đang ở Hà Nội", rv2))
rv3 = answer(turn(hv, "Tôi mang quốc tịch Úc").replace(EN, "\n(Hãy trả lời bằng tiếng Việt.)"))["output"]
print("\nVI bước 1:", rv3.replace("\n", " ")[:200])
assert "dừng" in rv3 and body_sentences(rv3) <= 3

print("\n>>> TẤT CẢ ĐẠT")
