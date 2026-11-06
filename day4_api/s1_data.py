"""D4 P1 Data: navigate nested JSON safely."""
import json

doc = json.loads('{"user":{"name":"Ann","langs":["py","go"],"addr":null}}')
assert doc["user"]["langs"][-1] == "go"
assert doc["user"]["addr"] is None
assert doc.get("missing", {}).get("x") is None
name, langs = doc["user"]["name"], doc["user"]["langs"]
assert (name, len(langs)) == ("Ann", 2)
assert "user.name" in {f"user.{k}": v for k, v in doc["user"].items()}
assert json.dumps({"b": 1, "a": 2}, sort_keys=True) == '{"a": 2, "b": 1}'
# VARIATION: write get_path(doc, "user.langs.0") that walks keys/indexes
# VARIATION: dump with indent=2 and separators=(",", ":")
