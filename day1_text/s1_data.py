"""D1 P1 Data: split, slice, unpack, set, dict."""
text = "the quick brown fox jumps over the lazy dog the end"
words = text.split()
assert words[1:4] == ["quick", "brown", "fox"]
first, *middle, last = words
assert (first, last) == ("the", "end") and len(middle) == len(words) - 2
assert len(set(words)) == 9
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
assert counts["the"] == 3
# VARIATION: build counts with dict.setdefault instead of .get
# VARIATION: get the last 3 words with a negative slice; reverse them with [::-1]
