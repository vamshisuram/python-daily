"""D7 P5 Errors: streaming file count + domain error."""
import tempfile
from pathlib import Path

class EmptyTextError(ValueError): pass

def count_file(path):
    n = 0
    with Path(path).open() as f:
        for line in f: n += len(line.split())
    if n == 0: raise EmptyTextError(path)
    return n

with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "a.txt"
    p.write_text("a b\nc\n")
    assert count_file(p) == 3
    p.write_text("\n")
    try: count_file(p)
    except EmptyTextError: pass
    else: raise AssertionError
# VARIATION: accept a directory and count all *.txt recursively
