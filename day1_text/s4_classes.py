"""D1 P4 Classes: dataclass, ordering, dunder protocol."""
from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class WordStat:
    count: int
    word: str

a, b = WordStat(3, "the"), WordStat(1, "fox")
assert b < a and sorted([a, b])[0] == b
assert repr(a) == "WordStat(count=3, word='the')"

class Bag:
    def __init__(self, words): self._w = list(words)
    def __len__(self): return len(self._w)
    def __iter__(self): return iter(self._w)
    def __contains__(self, w): return w in self._w

c = Bag(["a", "b"])
assert len(c) == 2 and "a" in c and list(c) == ["a", "b"]
# VARIATION: add __getitem__ so c[0] works, and __add__ to merge two Bags
# VARIATION: try mutating a frozen WordStat and catch the error
