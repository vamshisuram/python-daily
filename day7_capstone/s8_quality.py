"""D7 P8 Quality: typed + doctest + benchmark, together."""
import doctest, re, timeit
from collections import Counter

def vocab_size(text: str) -> int:
    """
    >>> vocab_size("A a b")
    2
    >>> vocab_size("")
    0
    """
    return len(Counter(re.findall(r"[a-z']+", text.lower())))

assert doctest.testmod().failed == 0
assert timeit.timeit(lambda: vocab_size("a b c " * 200), number=50) < 5
# VARIATION: add a property-style check: vocab_size(t) <= len(t.split()) for random t
