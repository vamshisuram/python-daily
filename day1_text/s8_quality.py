"""D1 P8 Quality: type hints, doctest, timeit."""
import doctest, timeit

def word_count(text: str) -> dict[str, int]:
    """
    >>> word_count("a b a")
    {'a': 2, 'b': 1}
    """
    out: dict[str, int] = {}
    for w in text.split(): out[w] = out.get(w, 0) + 1
    return out

assert doctest.testmod().failed == 0
t = timeit.timeit(lambda: word_count("a b a " * 100), number=100)
assert t < 5
# VARIATION: add a second doctest for the empty string
# VARIATION: rewrite with Counter and compare timeit numbers
