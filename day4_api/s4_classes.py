"""D4 P4 Classes: dependency injection (fake transport), from_json."""
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    @classmethod
    def from_json(cls, d): return cls(id=d["id"], name=d["name"])

class Client:
    def __init__(self, transport): self._t = transport
    def user(self, id): return User.from_json(self._t(f"/users/{id}"))

fake = lambda path: {"id": int(path.split("/")[-1]), "name": "Ann"}
assert Client(fake).user(7) == User(7, "Ann")
# VARIATION: add Client.users(ids) returning a list
# VARIATION: add __repr__ to Client that hides secrets like a token
