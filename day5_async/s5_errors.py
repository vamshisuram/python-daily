"""D5 P5 Errors: gather(return_exceptions), timeout, TaskGroup."""
import asyncio

async def boom(): raise ValueError("x")
async def slow(): await asyncio.sleep(1)

async def main():
    r = await asyncio.gather(boom(), asyncio.sleep(0, "ok"), return_exceptions=True)
    assert isinstance(r[0], ValueError) and r[1] == "ok"
    try: await asyncio.wait_for(slow(), 0.05)
    except TimeoutError: pass
    else: raise AssertionError
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(boom())
    except* ValueError:
        pass

asyncio.run(main())
# VARIATION: use `async with asyncio.timeout(0.05):` instead of wait_for
# VARIATION: cancel a task and catch CancelledError (re-raise it!)
