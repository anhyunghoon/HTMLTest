import http.server
import socketserver

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 요청된 경로가 apple-app-site-association 이면 강제로 Content-Type 변경
        if "apple-app-site-association" in self.path:
            self.send_header("Content-Type", "application/json")
        super().end_headers()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving HTTP on port {PORT} (AASA JSON Content-Type patch applied)...")
    httpd.serve_forever()



# python3 server.py