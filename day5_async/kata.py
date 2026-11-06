"""D5 KATA: bounded-concurrency fetcher (fake I/O)."""
import asyncio

async def fetch_all(urls, limit=2):
    sem, active, peak = asyncio.Semaphore(limit), 0, 0
    async def one(u):
        nonlocal active, peak
        async with sem:
            active += 1
            peak = max(peak, active)
            await asyncio.sleep(0.01)
            active -= 1
            return u.upper()
    return await asyncio.gather(*map(one, urls)), peak

res, peak = asyncio.run(fetch_all(list("abcde")))
assert res == list("ABCDE") and peak == 2
# KATA: add a per-request timeout and return None for timed-out urls
