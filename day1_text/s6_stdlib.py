"""D1 P6 Stdlib: Counter, defaultdict, re, itertools, json."""
import re, json, itertools
from collections import Counter, defaultdict

text = "the cat and the hat and the bat"
c = Counter(text.split())
assert c.most_common(1) == [("the", 3)]
assert re.findall(r"\b\w{3}\b", "a cat sat") == ["cat", "sat"]
groups = defaultdict(list)
for w in text.split(): groups[len(w)].append(w)
assert groups[3][:2] == ["the", "cat"]
assert list(itertools.pairwise("abc")) == [("a", "b"), ("b", "c")]
assert json.loads(json.dumps(dict(c)))["and"] == 2
# VARIATION: find all words ending in "at" with one regex
# VARIATION: use Counter arithmetic: c - Counter(["the"]) and c + c
