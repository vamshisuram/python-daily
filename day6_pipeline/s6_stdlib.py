"""D6 P6 Stdlib: the itertools grab-bag."""
from itertools import combinations, groupby, islice, permutations, product, zip_longest

assert len(list(product("ab", repeat=2))) == 4
assert list(combinations("abc", 2)) == [("a", "b"), ("a", "c"), ("b", "c")]
assert len(list(permutations(range(3)))) == 6
assert list(zip_longest([1, 2], [9], fillvalue=0)) == [(1, 9), (2, 0)]
assert list(islice(iter(range(100)), 3)) == [0, 1, 2]
assert [(k, len(list(g))) for k, g in groupby("aabccc")] == [("a", 2), ("b", 1), ("c", 3)]
# VARIATION: itertools.tee a generator and consume both copies
# VARIATION: build a grid of coordinates with product(range(3), repeat=2)
