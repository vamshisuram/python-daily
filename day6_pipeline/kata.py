"""D6 KATA: streaming csv -> filter -> group-sum pipeline."""
import csv, io
from itertools import groupby
from operator import itemgetter

RAW = "cat,amt\nfood,5\nfun,3\nfood,7\nbad,x\nfun,1\n"

def rows(f):
    for r in csv.DictReader(f):
        try: yield r["cat"], int(r["amt"])
        except ValueError: continue

def totals(pairs):
    for k, g in groupby(sorted(pairs), key=itemgetter(0)):
        yield k, sum(a for _, a in g)

assert dict(totals(rows(io.StringIO(RAW)))) == {"food": 12, "fun": 4}
# KATA: rewrite totals with collections.Counter; which is clearer?
