import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok"}).encode()
            content_type = "application/json"
        else:
            body = b"tes dari nol"
            content_type = "text/plain"
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


print("Server jalan di http://127.0.0.1:8000", flush=True)
HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
