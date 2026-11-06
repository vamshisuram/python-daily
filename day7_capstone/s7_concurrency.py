"""D7 P7 Concurrency: same job via threads and asyncio."""
import asyncio
from concurrent.futures import ThreadPoolExecutor

docs = ["a b", "c", "d e f"]
def n(d): return len(d.split())

with ThreadPoolExecutor() as ex:
    assert list(ex.map(n, docs)) == [2, 1, 3]

async def main(): return await asyncio.gather(*(asyncio.to_thread(n, d) for d in docs))
assert asyncio.run(main()) == [2, 1, 3]
# VARIATION: write the ProcessPoolExecutor version (remember the __main__ guard)
