"""D4 KATA: real HTTP round-trip against a local server."""
import json, threading, urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"path": self.path}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a): pass

srv = HTTPServer(("127.0.0.1", 0), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()

def get_json(path):
    with urllib.request.urlopen(f"http://127.0.0.1:{srv.server_port}{path}", timeout=2) as r:
        return json.load(r)

assert get_json("/users/1") == {"path": "/users/1"}
srv.shutdown()
# KATA: make the server return 404 for /missing and map it to NotFound (see s5)
