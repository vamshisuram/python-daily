"""D6 P2 Flow: chained generators, takewhile, send()."""
import itertools

def nums(): yield from range(10)
def evens(it): return (x for x in it if x % 2 == 0)
def squares(it): return (x * x for x in it)

assert list(squares(evens(nums()))) == [0, 4, 16, 36, 64]
assert sum(itertools.takewhile(lambda x: x < 20, squares(nums()))) == 30

def running_avg():
    total = n = 0
    while True:
        x = yield (total / n if n else 0)
        total += x
        n += 1

g = running_avg()
next(g)
assert g.send(10) == 10 and g.send(20) == 15
# VARIATION: add a stage that drops multiples of 3; nothing runs until you consume
# VARIATION: replace nums() with itertools.count() and still take 5 results
