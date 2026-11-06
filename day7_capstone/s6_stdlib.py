"""D7 P6 Stdlib: bigrams with pairwise + Counter."""
import re
from collections import Counter
from itertools import pairwise

words = re.findall(r"[a-z']+", "the cat. the cat sat".lower())
bi = Counter(pairwise(words))
assert bi[("the", "cat")] == 2 and bi.most_common(1) == [(("the", "cat"), 2)]
# VARIATION: trigrams with zip(words, words[1:], words[2:]); compare to pairwise
