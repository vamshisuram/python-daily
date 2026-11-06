"""D1 P5 Errors: custom exception, pathlib file IO, context manager."""
import contextlib, tempfile
from pathlib import Path

class EmptyTextError(ValueError): pass

def first_word(text):
    if not text.strip(): raise EmptyTextError("no words")
    return text.split()[0]

try:
    first_word("   ")
except EmptyTextError as e:
    assert str(e) == "no words"
else:
    raise AssertionError

with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "a.txt"
    p.write_text("hello\nworld\n")
    with p.open() as f:
        assert [l.rstrip() for l in f] == ["hello", "world"]

@contextlib.contextmanager
def tag(log, name):
    log.append(f"<{name}>")
    try: yield
    finally: log.append(f"</{name}>")

log = []
with tag(log, "b"): log.append("hi")
assert log == ["<b>", "hi", "</b>"]
# VARIATION: raise inside the `with tag` block; confirm the closing tag still appears
# VARIATION: write a class-based context manager (__enter__/__exit__) doing the same
