"""D4 P2 Flow: paginated generator, flatten."""
pages = [{"items": [1, 2], "next": 1}, {"items": [3], "next": 2}, {"items": [], "next": None}]
def fetch(i): return pages[i]

def all_items():
    i = 0
    while i is not None:
        p = fetch(i)
        yield from p["items"]
        i = p["next"]

assert list(all_items()) == [1, 2, 3]
nested = [[1, 2], [3], []]
assert [x for sub in nested for x in sub] == [1, 2, 3]
# VARIATION: stop after the first N items with itertools.islice (lazy!)
# VARIATION: add a max_pages guard to avoid infinite loops
