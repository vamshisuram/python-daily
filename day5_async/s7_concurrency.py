"""D5 P7 Concurrency: Queue + worker tasks + Semaphore."""
import asyncio

async def main():
    q, out, sem = asyncio.Queue(), [], asyncio.Semaphore(2)
    async def worker():
        while True:
            n = await q.get()
            async with sem:
                await asyncio.sleep(0)
                out.append(n * n)
            q.task_done()
    ws = [asyncio.create_task(worker()) for _ in range(3)]
    for i in range(5): q.put_nowait(i)
    await q.join()
    for w in ws: w.cancel()
    assert sorted(out) == [0, 1, 4, 9, 16]

asyncio.run(main())
# VARIATION: add a None sentinel per worker for clean shutdown instead of cancel()
# VARIATION: use asyncio.to_thread to call a blocking function from a worker
