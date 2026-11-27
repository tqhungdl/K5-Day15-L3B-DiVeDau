"""Giao diện web cho bản chạy thử — NHÓM VIẾT.

Chạy bằng:  python codebase/web.py          (macOS/Linux: python3 codebase/web.py)
            python codebase/web.py --port 8001
Mở http://localhost:8000 trên trình duyệt.

Chỉ dùng thư viện chuẩn (http.server) — khớp luật khung. UI nằm ở codebase/static/.
`python run.py` (giao diện dòng lệnh) vẫn hoạt động như trước, hai cách chạy song song.

API:
    GET  /api/health   → {"ok": true}
    POST /api/answer   body {"text": str} → agent.answer(text) → {"output", "meta"}
"""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tracing
from agent import answer

STATIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
PORT = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 8000

MIME = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".ico": "image/x-icon",
}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # im lặng, chỉ in lỗi thật
        pass

    def _send(self, code, body, ctype):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")  # trình duyệt luôn tải bản mới
        self.end_headers()
        self.wfile.write(body)

    def _static(self, path):
        rel = "index.html" if path in ("", "/") else path.lstrip("/")
        file_path = os.path.normpath(os.path.join(STATIC, rel))
        if not file_path.startswith(STATIC) or not os.path.isfile(file_path):
            self._send(404, "Không tìm thấy trang".encode("utf-8"), "text/plain; charset=utf-8")
            return
        ext = os.path.splitext(file_path)[1].lower()
        with open(file_path, "rb") as f:
            self._send(200, f.read(), MIME.get(ext, "application/octet-stream"))

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/api/health":
            self._send(200, b'{"ok": true}', "application/json; charset=utf-8")
            return
        self._static(path)

    def do_POST(self):
        if self.path.split("?", 1)[0] != "/api/answer":
            self._send(404, b'{"error": "not found"}', "application/json; charset=utf-8")
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            text = json.loads(self.rfile.read(length).decode("utf-8")).get("text", "").strip()
        except Exception:
            self._send(400, b'{"error": "bad request"}', "application/json; charset=utf-8")
            return
        if not text:
            self._send(400, b'{"error": "empty"}', "application/json; charset=utf-8")
            return
        tracing.begin("web")
        try:
            result = answer(text)
        except NotImplementedError as e:
            tracing.end()
            self._send(503, json.dumps({"error": "Chưa nối model: %s" % e}).encode("utf-8"),
                       "application/json; charset=utf-8")
            return
        except Exception as e:  # lỗi gọi model: trả lỗi rõ cho UI, không lộ traceback
            tracing.end()
            self._send(502, json.dumps({"error": "%s: %s" % (type(e).__name__, e)}).encode("utf-8"),
                       "application/json; charset=utf-8")
            return
        stats, _ = tracing.end()
        output = result.get("output", "") if isinstance(result, dict) else str(result)
        self._send(200, json.dumps({
            "output": output,
            "meta": {
                "model": ", ".join(stats["models"]) or None,
                "model_calls": stats["model_calls"],
                "tool_calls": stats["tool_calls"],
                "tokens_in": stats["tokens_in"],
                "tokens_out": stats["tokens_out"],
            },
        }, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")


if __name__ == "__main__":
    print("Travel SOS — http://localhost:%d  (thoát: Ctrl+C)" % PORT)
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
