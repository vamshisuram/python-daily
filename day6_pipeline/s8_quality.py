"""D6 P8 Quality: measure, don't guess (memory + time)."""
import sys, timeit

lst = [i for i in range(100_000)]
gen = (i for i in range(100_000))
assert sys.getsizeof(gen) < sys.getsizeof(lst)
a = timeit.timeit("sum(x for x in range(1000))", number=200)
b = timeit.timeit("sum(range(1000))", number=200)
assert b < a
print(f"genexp {a:.4f}s vs builtin {b:.4f}s")
# VARIATION: profile a function with cProfile.run and read the top lines
# VARIATION: use tracemalloc to compare list vs generator peak memory
