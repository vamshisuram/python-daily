"""D7 CAPSTONE KATA: Day 1's top_words, naive vs idiomatic, proven equivalent + timed."""
import doctest, random, re, timeit
from collections import Counter

def top_naive(text, n=3):       # Day 1 version
    counts = {}
    for raw in text.lower().split():
        w = "".join(c for c in raw if c.isalnum())
        if w: counts[w] = counts.get(w, 0) + 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

def top_idiomatic(text: str, n: int = 3) -> list[tuple[str, int]]:
    """
    >>> top_idiomatic("The cat. The hat! A cat?", 2)
    [('cat', 2), ('the', 2)]
    """
    c = Counter(re.findall(r"[a-z0-9]+", text.lower()))
    return sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

random.seed(1)
vocab = ["the", "cat", "hat", "a", "dog"]
text = " ".join(random.choice(vocab) + random.choice(["", ",", "."]) for _ in range(5000))
assert top_naive(text) == top_idiomatic(text)
assert doctest.testmod().failed == 0
print("naive     ", timeit.timeit(lambda: top_naive(text), number=20))
print("idiomatic ", timeit.timeit(lambda: top_idiomatic(text), number=20))
# KATA: write the Day 1 solution from memory FIRST, then the idiomatic one, then compare.
# Note the two differ on "don't" (naive -> dont, regex -> don, t): equal only on this input.
