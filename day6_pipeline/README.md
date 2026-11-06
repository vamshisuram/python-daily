# Day 6: Data pipeline

Same 8 pillars, laziness (generators, itertools) and measuring perf.

Ritual: recall (10) -> snippets (60-80) -> kata (15) -> journal (5). Run: `python3 s1_data.py`. Silent = pass.

| File | Pillar | Focus |
|---|---|---|
| `s1_data.py` | 1 Data | stability, transpose, set algebra, hashability. |
| `s2_flow.py` | 2 Flow | chained generators, takewhile, send(). |
| `s3_functions.py` | 3 Functions | compose, itemgetter, partial in map. |
| `s4_classes.py` | 4 Classes | iterable vs iterator, __slots__. |
| `s5_errors.py` | 5 Errors | csv with bad rows, StringIO as a fake file. |
| `s6_stdlib.py` | 6 Stdlib | the itertools grab-bag. |
| `s7_concurrency.py` | 7 Concurrency | CPU-bound fan-out with chunksize. |
| `s8_quality.py` | 8 Quality | measure, don't guess (memory + time). |
| `kata.py` | all | D6 KATA: streaming csv -> filter -> group-sum pipeline. |

Each file ends with `# VARIATION:` lines: change the code, predict the result, run it.
