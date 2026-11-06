"""D6 P1 Data: stability, transpose, set algebra, hashability."""
rows = [("a", 3), ("b", 1), ("c", 3)]
assert sorted(rows, key=lambda r: r[1]) == [("b", 1), ("a", 3), ("c", 3)]  # stable
names, nums = zip(*rows)
assert names == ("a", "b", "c")
assert {1, 2, 3} & {2, 3, 4} == {2, 3} and {1, 2} - {2} == {1} and {1} ^ {2} == {1, 2}
d = {(1, 2): "pt"}
assert d[(1, 2)] == "pt"
try: d[[1]] = 1
except TypeError: pass
else: raise AssertionError
assert list(range(10))[::3] == [0, 3, 6, 9]
# VARIATION: sort by two keys with a tuple key and reverse one using negation
# VARIATION: dedupe a list preserving order with dict.fromkeys
