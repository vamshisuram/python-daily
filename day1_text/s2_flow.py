"""D1 P2 Flow: comprehensions, match, generator expression."""
words = "the quick brown fox jumps over the lazy dog".split()
assert [len(w) for w in words] == [3, 5, 5, 3, 5, 4, 3, 4, 3]
assert {w for w in words if len(w) > 4} == {"quick", "brown", "jumps"}
assert {w: len(w) for w in words}["quick"] == 5

def classify(w):
    match len(w):
        case n if n <= 3: return "short"
        case 4 | 5: return "medium"
        case _: return "long"

assert [classify(w) for w in ("fox", "quick", "elephants")] == ["short", "medium", "long"]
gen = (w.upper() for w in words)
assert next(gen) == "THE"
# VARIATION: add a "huge" class for len > 8
# VARIATION: turn the dict comprehension into one that keeps only the longest word per length
