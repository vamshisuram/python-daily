"""D2 P4 Classes: dataclass fields, __post_init__, property, classmethod."""
from dataclasses import dataclass, field

@dataclass
class Item:
    name: str
    qty: int = 0
    price: float = 0.0
    tags: list[str] = field(default_factory=list)
    def __post_init__(self):
        if self.qty < 0: raise ValueError("qty < 0")
    @property
    def value(self): return self.qty * self.price
    @classmethod
    def from_csv(cls, line):
        n, q, p = line.split(",")
        return cls(n, int(q), float(p))

assert Item.from_csv("apple,5,0.5").value == 2.5
assert Item("x").tags is not Item("y").tags
try: Item("bad", -1)
except ValueError: pass
else: raise AssertionError
# VARIATION: add a staticmethod `is_valid_name`
# VARIATION: make Item frozen and replace() it with dataclasses.replace
