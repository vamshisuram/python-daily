"""D1 P3 Functions: kw-only args, closure, decorator."""
import functools

def normalize(text, *, lower=True, strip_punct=True):
    if lower: text = text.lower()
    if strip_punct: text = "".join(c for c in text if c.isalnum() or c.isspace())
    return text

assert normalize("Hello, World!") == "hello world"
assert normalize("Hello!", lower=False) == "Hello"

def make_min_len(n):
    return lambda w: len(w) >= n

assert make_min_len(4)("four") and not make_min_len(4)("it")

def logged(fn):
    calls = []
    @functools.wraps(fn)
    def wrapper(*a, **k):
        calls.append((a, k))
        return fn(*a, **k)
    wrapper.calls = calls
    return wrapper

@logged
def shout(s): return s.upper()

shout("a"); shout("b")
assert len(shout.calls) == 2 and shout.__name__ == "shout"
# VARIATION: make `logged` take a prefix argument (decorator factory)
# VARIATION: remove @functools.wraps and see what shout.__name__ becomes
