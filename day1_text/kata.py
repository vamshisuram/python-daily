"""D1 KATA: top-N words (plain loops on purpose; Day 7 rebuilds this idiomatically)."""
def top_words(text, n=3):
    counts = {}
    for raw in text.lower().split():
        w = "".join(c for c in raw if c.isalnum())
        if w: counts[w] = counts.get(w, 0) + 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

assert top_words("The cat. The hat! A cat?", 2) == [("cat", 2), ("the", 2)]
assert top_words("") == []
# KATA: delete the function body and rewrite from memory; add a stop-words param
