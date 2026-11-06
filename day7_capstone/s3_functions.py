"""D7 P3 Functions: cache + timing decorator."""
import functools, re, time
from functools import cache

@cache
def normalize(t: str) -> tuple[str, ...]:
    return tuple(re.findall(r"[a-z']+", t.lower()))

assert normalize("A b A") == ("a", "b", "a")
normalize("A b A")
assert normalize.cache_info().hits == 1

def timed(fn):
    @functools.wraps(fn)
    def w(*a, **k):
        t = time.perf_counter()
        r = fn(*a, **k)
        w.elapsed = time.perf_counter() - t
        return r
    return w

@timed
def f(): return 1

assert f() == 1 and f.elapsed >= 0
# VARIATION: why is returning a tuple (not list) important for @cache users?
