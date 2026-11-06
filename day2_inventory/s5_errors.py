"""D2 P5 Errors: raise from, JSON persistence."""
import json, tempfile
from pathlib import Path

class OutOfStock(Exception): pass

def take(inv, name, q):
    try: have = inv[name]
    except KeyError as e: raise OutOfStock(name) from e
    if have < q: raise OutOfStock(name)
    inv[name] = have - q

inv = {"a": 2}
take(inv, "a", 1)
assert inv["a"] == 1
for bad in ("a", "zzz"):
    try: take(inv, bad, 5)
    except OutOfStock: pass
    else: raise AssertionError
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "inv.json"
    p.write_text(json.dumps(inv))
    assert json.loads(p.read_text()) == inv
# VARIATION: catch OutOfStock and inspect e.__cause__
# VARIATION: add try/else/finally and log which branch ran
