"""D3 P3 Functions: decorator factory, generator function, multi-return."""
import functools

def repeat(n):
    def deco(fn):
        @functools.wraps(fn)
        def w(*a, **k): return [fn(*a, **k) for _ in range(n)]
        return w
    return deco

@repeat(3)
def hi(): return "hi"

assert hi() == ["hi"] * 3

def read_nonblank(lines):
    for l in lines:
        if l.strip(): yield l.strip()

assert list(read_nonblank(["a", " ", "b "])) == ["a", "b"]

def minmax(xs): return min(xs), max(xs)
lo, hi_ = minmax([3, 1, 2])
assert (lo, hi_) == (1, 3)
# VARIATION: make read_nonblank accept a comment prefix to skip
# VARIATION: stack two decorators and predict the order they apply
