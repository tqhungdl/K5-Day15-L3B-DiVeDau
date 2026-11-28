"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. NHÓM VIẾT phần gọi model thật.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    trả một câu giả cố định, model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Nối model thật: điền .env (chép từ .env.example), rồi viết nhánh gọi API ở dưới theo docs/connect-model.md
(có ví dụ OpenAI, Claude, model chạy trên máy, và cách nối nhà cung cấp khác). Không dán API key vào file này.
"""
import json
import os
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or os.environ.get("OPENAI_API_KEY") or "").strip()

SHOW_RAW = False   # đổi thành True để in nguyên phản hồi của API khi cần tìm tên trường


def post_json(url, headers, body, timeout=60):
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib).
    Lỗi 503 (model quá tải, ngắt quãng) thử lại tối đa 2 lần, cách 5 giây."""
    import time
    last_err = None
    for attempt in range(3):
        req = urllib.request.Request(
            url, data=json.dumps(body).encode("utf-8"), method="POST",
            headers=dict({"Content-Type": "application/json"}, **headers))
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = json.loads(r.read().decode("utf-8"))
            if SHOW_RAW:
                print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
            return data
        except urllib.error.HTTPError as e:
            body_txt = e.read().decode("utf-8", "replace")[:300]
            if e.code == 503 and attempt < 2:
                last_err = RuntimeError("HTTP 503: %s" % body_txt)
                time.sleep(5)
                continue
            raise RuntimeError("HTTP %d: %s" % (e.code, body_txt))
    raise last_err


URL_OPENAI = "https://api.openai.com/v1/chat/completions"


def call_openai(system, user):
    """Gọi OpenAI (và nhà cung cấp API tương thích OpenAI), trả {text, tokens_in, tokens_out}."""
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(URL_OPENAI, {"Authorization": "Bearer " + API_KEY},
                     {"model": MODEL_NAME, "messages": messages})
    u = data["usage"]
    return {"text": data["choices"][0]["message"]["content"],
            "tokens_in": u["prompt_tokens"], "tokens_out": u["completion_tokens"]}


URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent" % MODEL_NAME


def call_gemini(system, user):
    """Gọi Google Gemini qua REST API generateContent, trả {text, tokens_in, tokens_out}."""
    body = {"contents": [{"role": "user", "parts": [{"text": user}]}]}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = post_json(URL_GEMINI, {"x-goog-api-key": API_KEY}, body, timeout=120)
    if data.get("promptFeedback", {}).get("blockReason"):
        raise RuntimeError("Gemini chặn input: %s" % data["promptFeedback"]["blockReason"])
    cand = (data.get("candidates") or [{}])[0]
    if cand.get("finishReason") and cand["finishReason"] not in ("STOP", "MAX_TOKENS"):
        raise RuntimeError("Gemini không trả lời được: %s" % cand["finishReason"])
    text = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []))
    u = data.get("usageMetadata", {})
    # tokens_out gồm cả token suy luận nếu model tính riêng (thoughtsTokenCount)
    return {"text": text,
            "tokens_in": int(u.get("promptTokenCount", 0)),
            "tokens_out": int(u.get("candidatesTokenCount", 0)) + int(u.get("thoughtsTokenCount", 0))}


def call_provider(system, user):
    """Nhà cung cấp chưa hỗ trợ: chép ví dụ quickstart của hãng vào đây (docs/connect-model.md mục 2.4)."""
    raise RuntimeError("Chưa hỗ trợ MODEL_PROVIDER=%s — chép ví dụ quickstart vào call_provider()" % MODEL_PROVIDER)


URL_OPENAI = "https://api.openai.com/v1/chat/completions"


def post_json(url, headers, body, timeout=90):
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib)."""
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))


def call_openai(system, user):
    """Gọi OpenAI Chat Completions một lần. Token lấy từ trường usage của API."""
    if not API_KEY:
        raise RuntimeError("Chưa có API_KEY trong file .env")
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(URL_OPENAI, {"Authorization": "Bearer " + API_KEY},
                     {"model": MODEL_NAME, "messages": messages})
    u = data["usage"]
    return {"text": data["choices"][0]["message"]["content"] or "",
            "tokens_in": u["prompt_tokens"], "tokens_out": u["completion_tokens"]}


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}
    if MODEL_PROVIDER == "openai":
        r = call_openai(system, user)
    elif MODEL_PROVIDER == "gemini":
        r = call_gemini(system, user)
    elif MODEL_PROVIDER == "anthropic":
        r = call_provider(system, user)   # xem docs/connect-model.md mục 2.2 khi cần nối
    elif MODEL_PROVIDER == "ollama":
        r = call_provider(system, user)   # xem docs/connect-model.md mục 2.3 khi cần nối
    else:
        r = call_provider(system, user)
    return {"text": r["text"], "model": MODEL_NAME,
            "tokens_in": int(r["tokens_in"]), "tokens_out": int(r["tokens_out"])}
