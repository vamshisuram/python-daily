"""D6 P3 Functions: compose, itemgetter, partial in map."""
from functools import partial, reduce
from operator import itemgetter

def compose(*fs): return reduce(lambda f, g: lambda x: g(f(x)), fs)

inc, dbl = (lambda x: x + 1), (lambda x: x * 2)
assert compose(inc, dbl)(3) == 8
rows = [{"n": "a", "v": 2}, {"n": "b", "v": 1}]
assert [r["n"] for r in sorted(rows, key=itemgetter("v"))] == ["b", "a"]
assert list(map(partial(pow, 2), [1, 2, 3])) == [2, 4, 8]
# VARIATION: swap compose order to apply right-to-left
# VARIATION: use attrgetter on dataclass instances instead of dicts
