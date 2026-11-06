"""D3 KATA: mini grep."""
import argparse, re, tempfile
from pathlib import Path

def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("pattern")
    p.add_argument("path")
    p.add_argument("-i", action="store_true")
    a = p.parse_args(argv)
    flags = re.I if a.i else 0
    return [l for l in Path(a.path).read_text().splitlines() if re.search(a.pattern, l, flags)]

with tempfile.TemporaryDirectory() as d:
    f = Path(d) / "x.txt"
    f.write_text("Foo\nbar\nfoo bar\n")
    assert main(["foo", str(f)]) == ["foo bar"]
    assert main(["-i", "foo", str(f)]) == ["Foo", "foo bar"]
# KATA: add -n (line numbers) and -c (count only) flags
