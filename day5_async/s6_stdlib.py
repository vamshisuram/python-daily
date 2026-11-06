"""D5 P6 Stdlib: batched, accumulate, reduce, statistics, seeded random."""
import operator, random, statistics
from functools import reduce
from itertools import accumulate, batched, chain

assert list(batched(range(5), 2)) == [(0, 1), (2, 3), (4,)]
assert list(accumulate([1, 2, 3])) == [1, 3, 6]
assert reduce(operator.mul, [1, 2, 3, 4]) == 24
assert statistics.median([3, 1, 2]) == 2 and statistics.mean([1, 2, 3]) == 2
assert random.Random(0).random() == random.Random(0).random()
assert list(chain([1], [2, 3])) == [1, 2, 3]
# VARIATION: batch URLs in groups of 3 for a rate-limited fetch
# VARIATION: shuffle a list with a seeded Random and sample 2
