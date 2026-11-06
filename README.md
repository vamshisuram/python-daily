# python-daily

7 days x 1-2 hours. Build automatic Python fluency by repeating the **same full pass** daily with a new theme each time.

## Method
Every day walks the same 8 pillars (see [pillars.md](pillars.md)): data, control flow, functions, classes, errors/resources, stdlib, concurrency, quality. The *thought process* repeats; the *domain* changes. Repetition builds the pathways, variation stops it being rote.

## Daily ritual
| Time | What |
|---|---|
| 10 min | Blank-page recall from [recall.md](recall.md) |
| 60-80 min | 8 snippets `s1..s8`: run, read, then do each `# VARIATION:` (change it, predict, run) |
| 15 min | `kata.py`: rewrite from scratch without looking, then compare |
| 5 min | `journal.md` |

## Week
| Day | Theme | Leans on |
|---|---|---|
| [1](day1_text) | Text processing | baseline idioms |
| [2](day2_inventory) | Inventory data | dicts, dataclasses |
| [3](day3_cli) | CLI tool | I/O, errors, argparse |
| [4](day4_api) | JSON / HTTP API | typing, stdlib, retry |
| [5](day5_async) | Async fetcher | asyncio |
| [6](day6_pipeline) | Data pipeline | generators, itertools, perf |
| [7](day7_capstone) | Capstone | rebuild Day 1 idiomatically |

## Notebooks
Each day has `practice.ipynb` (blank attempt cells + **check** cells that start red) and `solution.ipynb` (the sister, filled in). Generated from the `.py` snippets, which stay the source of truth.
```
make setup   # uv sync: JupyterLab + ipykernel + nbclient into .venv
make lab     # open JupyterLab, then open dayN_*/practice.ipynb
make build   # regenerate notebooks after editing a snippet
make check   # run snippets, execute all solution notebooks, confirm practice checks are red
```

## Run snippets directly
Python 3.12+; snippets are stdlib-only (notebooks need `make setup`).
```
python3 day1_text/s1_data.py     # silent = all asserts passed
./run_all.sh                     # run everything
```
A snippet that raises `AssertionError` after you edit it is the feedback loop: fix your variation until it passes.
