"""D7 P2 Flow: lazy tokenizer generator."""
import re

def tokens(text):
    for m in re.finditer(r"[A-Za-z']+|\d+|[^\s\w]", text):
        t = m.group()
        if t.isdigit(): yield ("NUM", t)
        elif t[0].isalpha(): yield ("WORD", t.lower())
        else: yield ("PUNCT", t)

assert list(tokens("Hi 5!")) == [("WORD", "hi"), ("NUM", "5"), ("PUNCT", "!")]
# VARIATION: rewrite the if/elif chain with match + guards
