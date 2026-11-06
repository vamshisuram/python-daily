"""D6 P5 Errors: csv with bad rows, StringIO as a fake file."""
import csv, io

data = "name,qty\na,1\nb,x\nc,3\n"
good, bad = [], []
for row in csv.DictReader(io.StringIO(data)):
    try: good.append((row["name"], int(row["qty"])))
    except ValueError: bad.append(row["name"])
assert good == [("a", 1), ("c", 3)] and bad == ["b"]
out = io.StringIO()
csv.writer(out).writerow(["a", 1])
assert out.getvalue() == "a,1\r\n"
# VARIATION: collect (line_number, error) for bad rows via enumerate
# VARIATION: handle a missing column (KeyError) separately from bad ints
