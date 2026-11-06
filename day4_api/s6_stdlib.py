"""D4 P6 Stdlib: urllib.parse, HTTPStatus, base64, hashlib, datetime."""
import base64, hashlib
from urllib.parse import urlparse, parse_qs, urlencode
from http import HTTPStatus
from datetime import datetime, timezone

u = urlparse("https://x.com/a/b?q=1&q=2&z=3")
assert u.netloc == "x.com" and parse_qs(u.query)["q"] == ["1", "2"]
assert urlencode({"a": 1, "b": "x y"}) == "a=1&b=x+y"
assert HTTPStatus(404).phrase == "Not Found"
assert base64.b64encode(b"hi").decode() == "aGk="
assert hashlib.sha256(b"").hexdigest().startswith("e3b0c442")
assert datetime(2026, 1, 2, tzinfo=timezone.utc).isoformat() == "2026-01-02T00:00:00+00:00"
# VARIATION: parse an ISO string back with datetime.fromisoformat
# VARIATION: build an HMAC signature with the hmac module
