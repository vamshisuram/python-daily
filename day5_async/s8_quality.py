"""D5 P8 Quality: test async code with AsyncMock."""
import asyncio
from unittest.mock import AsyncMock

async def fetch_all(client, urls):
    return await asyncio.gather(*(client.get(u) for u in urls))

c = AsyncMock()
c.get.side_effect = lambda u: u.upper()
assert asyncio.run(fetch_all(c, ["a", "b"])) == ["A", "B"]
assert c.get.await_count == 2
# VARIATION: make get raise for "b" and assert the error propagates
# VARIATION: assert call args with c.get.assert_any_await("a")
