"""D2 KATA: low-stock report."""
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    qty: int
    price: float

def report(items, limit=5):
    low = sorted((i for i in items if i.qty < limit), key=lambda i: (i.qty, i.name))
    return [f"{i.name}: {i.qty}" for i in low]

items = [Item("pear", 0, .7), Item("apple", 3, .5), Item("kiwi", 12, .2), Item("fig", 3, 1)]
assert report(items) == ["pear: 0", "apple: 3", "fig: 3"]
# KATA: rewrite from memory; add total stock value line at the end
