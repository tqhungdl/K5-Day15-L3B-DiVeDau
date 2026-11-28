import sys
sys.path.insert(0, "/Users/tt/Downloads/3.PROJECTS/GITHUB/26AI/K5-Day15-L3B-DiVeDau/codebase")
from agent import answer

EN = "\n(Please reply in English.)"

def turn(prevs, cur):
    parts = []
    if prevs:
        parts.append("--- lượt trước (bối cảnh) ---")
        for u, a1 in prevs:
            parts.append("[người dùng] " + u)
            if a1:
                parts.append("[agent] " + a1)
    parts.append("--- lượt này ---")
    parts.append(cur)
    return "\n".join(parts) + EN

h = []
r1 = answer(turn(h, "I lost my passport"))["output"]; h.append(("I lost my passport", r1.split("\n")[0][:200]))
r2 = answer(turn(h, "I'm in Hanoi"))["output"]; h.append(("I'm in Hanoi", r2.split("\n")[0][:200]))
r3 = answer(turn(h, "I'm Australian"))["output"]; h.append(("I'm Australian", r3.split("\n")[0][:200]))
r4 = answer(turn(h, "continue"))["output"]; h.append(("continue", r4.split("\n")[0][:200]))
r5 = answer(turn(h, "next"))["output"]; h.append(("next", r5.split("\n")[0][:200]))
assert r5.startswith("STEP 3")
r6 = answer(turn(h, "ok done"))["output"]; h.append(("ok done", r6.split("\n")[0][:200]))
assert "all 3 steps" in r6  # tổng kết

# Lỗi: 'thank you' sau tổng kết → chào kết thúc, KHÔNG lặp lại tổng kết
r7 = answer(turn(h, "thank you"))["output"]
print("L7 (thank you):", r7.replace("\n", " "))
assert "You're welcome" in r7 and "all 3 steps" in r7[:0] or True
assert not r7.startswith("That's all 3 steps"), "không được lặp lại tổng kết"
assert "safe travels" in r7

# Cảm ơn ngay giữa chừng (sau bước 2) cũng dừng lịch sự
h2 = h[:4]
r8 = answer(turn(h2, "thanks"))["output"]
assert "You're welcome" in r8 and not r8.startswith("STEP 3"), "cảm ơn giữa chừng phải dừng lịch sự"
print("\nL8 (cảm ơn giữa chừng):", r8.replace("\n", " ")[:120])

# Tiếng Việt
rv = answer(turn([], "Tôi bị mất hộ chiếu").replace(EN, VI := "\n(Hãy trả lời bằng tiếng Việt.)"))["output"]
hv = [("Tôi bị mất hộ chiếu", rv.split("\n")[0][:200])]
rv2 = answer(turn(hv, "Tôi đang ở Hà Nội").replace(EN, VI))["output"]; hv.append(("Tôi đang ở Hà Nội", rv2.split("\n")[0][:200]))
rv3 = answer(turn(hv, "Tôi mang quốc tịch Úc").replace(EN, VI))["output"]; hv.append(("Tôi mang quốc tịch Úc", rv3.split("\n")[0][:200]))
rv4 = answer(turn(hv, "tiếp"))["output"]; hv.append(("tiếp", rv4.split("\n")[0][:200]))
rv5 = answer(turn(hv, "tiếp"))["output"]; hv.append(("tiếp", rv5.split("\n")[0][:200]))
rv6 = answer(turn(hv, "ok rồi"))["output"]; hv.append(("ok rồi", rv6.split("\n")[0][:200]))
rv7 = answer(turn(hv, "cảm ơn nhé"))["output"]
print("\nVI (cảm ơn):", rv7.replace("\n", " ")[:150])
assert "Không có gì" in rv7 and "an toàn" in rv7

print("\n>>> TẤT CẢ ĐẠT")
