# The 8 pillars (one-page cheat sheet)

| # | Pillar | Reach for |
|---|---|---|
| 1 | Data & types | `str` methods, slicing `[a:b:c]`, unpacking `a, *b = x`, `dict`/`set` ops, `tuple` as record |
| 2 | Control flow | comprehensions, generator expr, `match`, `for/else`, walrus `:=`, `enumerate`/`zip` |
| 3 | Functions | `*args/**kw`, keyword-only `*`, closures, decorators + `functools.wraps`, `partial`, generators |
| 4 | Classes | `@dataclass(frozen/slots/order)`, dunders (`__iter__ __len__ __call__`), `Protocol`, `@property`, `@classmethod` |
| 5 | Errors & resources | `try/except/else/finally`, `raise ... from`, custom exceptions, `with`, `contextlib`, `pathlib` |
| 6 | Stdlib | `collections`, `itertools`, `functools`, `re`, `json`, `datetime`, `csv`, `urllib` |
| 7 | Concurrency | `ThreadPoolExecutor` (I/O), `ProcessPoolExecutor` (CPU), `asyncio` (many I/O waits), `Lock` |
| 8 | Quality | type hints, `assert`, `doctest`/pytest, `timeit`, `logging`, `pdb` |

## Mental loop for any problem
1. What is the **shape of the data**? (pillar 1)
2. What is the **transformation**? (2, 3)
3. Does it need **state / a name**? (4)
4. What can **fail** and what must be **cleaned up**? (5)
5. Does the **stdlib** already do it? (6)
6. Is it **waiting or computing**? (7)
7. How do I **prove** it works? (8)
