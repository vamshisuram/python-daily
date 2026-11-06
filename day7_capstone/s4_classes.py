"""D7 P4 Classes: frozen+slots dataclass, Protocol strategy."""
from collections import Counter
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True, slots=True)
class TextStats:
    total: int
    unique: int
    top: tuple[tuple[str, int], ...]
    @classmethod
    def of(cls, words, n=2):
        c = Counter(words)
        return cls(c.total(), len(c), tuple(c.most_common(n)))

class Scorer(Protocol):
    def score(self, s: TextStats) -> float: ...

class Diversity:
    def score(self, s): return s.unique / s.total

s = TextStats.of("a b a c".split())
assert (s.total, s.unique, s.top[0]) == (4, 3, ("a", 2)) and Diversity().score(s) == 0.75
# VARIATION: add a second Scorer (e.g. average word length) and pick via a dict
