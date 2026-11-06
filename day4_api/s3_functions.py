"""D4 P3 Functions: retry decorator, positional-only, kwargs to query."""
import functools

def retry(times=3):
    def deco(fn):
        @functools.wraps(fn)
        def w(*a, **k):
            for attempt in range(times):
                try: return fn(*a, **k)
                except ConnectionError:
                    if attempt == times - 1: raise
        return w
    return deco

calls = []

@retry(3)
def flaky():
    calls.append(1)
    if len(calls) < 3: raise ConnectionError
    return "ok"

assert flaky() == "ok" and len(calls) == 3

def build_url(base, /, **params):
    return base + "?" + "&".join(f"{k}={v}" for k, v in params.items())

assert build_url("http://x", a=1, b=2) == "http://x?a=1&b=2"
# VARIATION: add exponential backoff via time.sleep(base * 2**attempt) (use tiny base)
# VARIATION: retry only on a tuple of exception types passed in
