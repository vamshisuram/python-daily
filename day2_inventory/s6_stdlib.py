"""D2 P6 Stdlib: namedtuple, deque, groupby, lru_cache, date math."""
from collections import namedtuple, deque
from functools import lru_cache
from itertools import groupby
from datetime import date, timedelta

P = namedtuple("P", "name qty")
assert P("a", 1)._replace(qty=2).qty == 2
d = deque(maxlen=2)
for i in range(4): d.append(i)
assert list(d) == [2, 3]
rows = sorted([("fruit", "apple"), ("veg", "kale"), ("fruit", "pear")])
g = {k: [n for _, n in v] for k, v in groupby(rows, key=lambda r: r[0])}
assert g == {"fruit": ["apple", "pear"], "veg": ["kale"]}

@lru_cache
def fib(n): return n if n < 2 else fib(n - 1) + fib(n - 2)

assert fib(50) == 12586269025
assert date(2026, 1, 30) + timedelta(days=3) == date(2026, 2, 2)
# VARIATION: call fib.cache_info() and print it
# VARIATION: groupby without sorting first; see why the result breaks
