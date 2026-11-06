"""D1 P7 Concurrency: thread pool map."""
from concurrent.futures import ThreadPoolExecutor

docs = ["a b c", "d e", "f"]
def count(d): return len(d.split())

with ThreadPoolExecutor(max_workers=3) as ex:
    results = list(ex.map(count, docs))
assert results == [3, 2, 1] and sum(results) == 6
# VARIATION: use ex.submit + as_completed; why does order change?
# VARIATION: explain why threads won't speed up CPU-heavy count() (GIL)
