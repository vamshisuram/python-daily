"""D5 P3 Functions: async def, gather, async decorator."""
import asyncio, functools, time

def timed(fn):
    @functools.wraps(fn)
    async def w(*a, **k):
        t = time.perf_counter()
        r = await fn(*a, **k)
        w.last = time.perf_counter() - t
        return r
    return w

@timed
async def work(x):
    await asyncio.sleep(0.05)
    return x

async def main():
    assert await asyncio.gather(*(work(i) for i in range(5))) == [0, 1, 2, 3, 4]
    assert work.last < 0.2   # 5 x 0.05s ran concurrently, not 0.25s

asyncio.run(main())
# VARIATION: call work(1) without await; what do you get back?
# VARIATION: replace gather with a sequential for-await loop and time it
