"""D4 P7 Concurrency: parallel I/O waits with threads."""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def slow(n):
    time.sleep(0.1)
    return n * 2

t = time.perf_counter()
with ThreadPoolExecutor(5) as ex:
    futs = [ex.submit(slow, i) for i in range(5)]
    got = sorted(f.result() for f in as_completed(futs))
assert got == [0, 2, 4, 6, 8] and time.perf_counter() - t < 0.4
# VARIATION: use max_workers=1 and watch the timing assertion fail
# VARIATION: make one task raise; see where the exception surfaces
