"""D3 P7 Concurrency: process pool for CPU work."""
from concurrent.futures import ProcessPoolExecutor

def sq(n): return n * n

if __name__ == "__main__":   # required: child processes re-import this module
    with ProcessPoolExecutor(2) as ex:
        assert list(ex.map(sq, range(5))) == [0, 1, 4, 9, 16]
# VARIATION: delete the __main__ guard and read the error (macOS/Windows spawn)
# VARIATION: swap in ThreadPoolExecutor; same result, different cost model
