# Day 1: Text processing

Baseline pass with plain idioms. Everything later is a variation on this.

Ritual: recall (10) -> snippets (60-80) -> kata (15) -> journal (5). Run: `python3 s1_data.py`. Silent = pass.

| File | Pillar | Focus |
|---|---|---|
| `s1_data.py` | 1 Data | split, slice, unpack, set, dict. |
| `s2_flow.py` | 2 Flow | comprehensions, match, generator expression. |
| `s3_functions.py` | 3 Functions | kw-only args, closure, decorator. |
| `s4_classes.py` | 4 Classes | dataclass, ordering, dunder protocol. |
| `s5_errors.py` | 5 Errors | custom exception, pathlib file IO, context manager. |
| `s6_stdlib.py` | 6 Stdlib | Counter, defaultdict, re, itertools, json. |
| `s7_concurrency.py` | 7 Concurrency | thread pool map. |
| `s8_quality.py` | 8 Quality | type hints, doctest, timeit. |
| `kata.py` | all | D1 KATA: top-N words (plain loops on purpose; Day 7 rebuilds this idiomatically). |

Each file ends with `# VARIATION:` lines: change the code, predict the result, run it.
