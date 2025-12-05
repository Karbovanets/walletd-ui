from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

WALLETD_URL = "http://127.0.0.1:16000/json_rpc"

class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.end_headers()

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length)

        r = requests.post(
            WALLETD_URL,
            data=body,
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(r.content)

print("CORS proxy running on http://127.0.0.1:16001")
HTTPServer(("127.0.0.1", 16001), Handler).serve_forever()

