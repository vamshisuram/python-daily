"""D5 P2 Flow: async generator, async comprehension."""
import asyncio

async def agen(n):
    for i in range(n):
        await asyncio.sleep(0)
        yield i

async def main():
    assert [i async for i in agen(3)] == [0, 1, 2]
    assert [x * 2 async for x in agen(3) if x] == [2, 4]

asyncio.run(main())
# VARIATION: use `async for` in a plain loop and break early
# VARIATION: try `for i in agen(3)` and read the error
