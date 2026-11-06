"""D7 P1 Data: Counter algebra + set overlap (Day 1 revisited)."""
from collections import Counter

a, b = Counter("the cat sat".split()), Counter("the dog sat".split())
assert set(a) & set(b) == {"the", "sat"}
assert len(set(a) & set(b)) / len(set(a) | set(b)) == 0.5    # Jaccard
assert (a & b) == Counter({"the": 1, "sat": 1}) and (a + b)["the"] == 2
# VARIATION: compare two real paragraphs; which words are unique to each?
