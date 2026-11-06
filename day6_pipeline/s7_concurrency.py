"""D6 P7 Concurrency: CPU-bound fan-out with chunksize."""
from concurrent.futures import ProcessPoolExecutor

def cpu(n): return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor(2) as ex:
        r = list(ex.map(cpu, [1000] * 4, chunksize=2))
    assert r == [cpu(1000)] * 4
# VARIATION: time sequential vs pool for n=2_000_000; when does the pool win?
# VARIATION: why must `cpu` be defined at module top level (pickling)?
