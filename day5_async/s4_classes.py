"""D5 P4 Classes: async context manager."""
import asyncio

class Session:
    def __init__(self): self.open = False
    async def __aenter__(self):
        self.open = True
        return self
    async def __aexit__(self, *exc): self.open = False

async def main():
    async with Session() as s:
        assert s.open
    assert not s.open

asyncio.run(main())
# VARIATION: build the same with @contextlib.asynccontextmanager
# VARIATION: raise inside the block; confirm __aexit__ still runs
