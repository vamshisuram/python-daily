"""D2 P2 Flow: filter dicts, any/all, for-else, walrus, zip/enumerate."""
inv = {"apple": 5, "pear": 0, "kiwi": 12}
in_stock = {k: v for k, v in inv.items() if v}
assert set(in_stock) == {"apple", "kiwi"}
assert any(v == 0 for v in inv.values()) and not all(inv.values())
for name, q in inv.items():
    if q > 10:
        found = name
        break
else:
    found = None
assert found == "kiwi"
if (n := len(in_stock)) > 1: assert n == 2
names = list(inv)
assert list(zip(names, range(3)))[1] == ("pear", 1)
assert next(enumerate(names, 1)) == (1, "apple")
# VARIATION: change the threshold so for-else takes the else branch
# VARIATION: use zip(strict=True) with mismatched lengths and catch the error
