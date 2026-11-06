"""D2 P1 Data: nested dicts, merge, sort records."""
inv = {"apple": {"qty": 5, "price": 0.5}, "pear": {"qty": 0, "price": 0.75}}
inv["kiwi"] = {"qty": 12, "price": 0.2}
merged = inv | {"apple": {"qty": 9, "price": 0.5}}
assert merged["apple"]["qty"] == 9 and inv["apple"]["qty"] == 5
assert round(sum(v["qty"] * v["price"] for v in inv.values()), 2) == 4.9
rows = sorted(((k, v["qty"]) for k, v in inv.items()), key=lambda r: -r[1])
assert rows[0] == ("kiwi", 12)
# VARIATION: use dict.pop with a default to remove "pear" safely
# VARIATION: invert to {qty: [names]} with setdefault
