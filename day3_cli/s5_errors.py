"""D3 P5 Errors/IO: argparse, pathlib globbing, missing files."""
import argparse, tempfile
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("path")
p.add_argument("-n", type=int, default=2)
p.add_argument("-v", "--verbose", action="store_true")
a = p.parse_args(["f.txt", "-n", "5", "-v"])
assert (a.path, a.n, a.verbose) == ("f.txt", 5, True)

with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    (root / "sub").mkdir()
    (root / "sub" / "a.py").write_text("x\n")
    (root / "b.txt").write_text("y\n")
    assert [f.name for f in root.rglob("*.py")] == ["a.py"]
    try: (root / "nope").read_text()
    except FileNotFoundError: pass
    else: raise AssertionError
    assert (root / "b.txt").stat().st_size == 2
# VARIATION: add a subcommand with add_subparsers
# VARIATION: use Path.suffix/.stem/.with_suffix on "a/b.tar.gz"
