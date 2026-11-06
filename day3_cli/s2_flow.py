"""D3 P2 Flow: match on command shapes, sentinel loop."""
def run(cmd):
    match cmd.split():
        case ["add", x, y]: return int(x) + int(y)
        case ["echo", *rest]: return " ".join(rest)
        case ["quit"]: return None
        case _: return "?"

assert run("add 2 3") == 5 and run("echo a b") == "a b"
assert run("quit") is None and run("zzz") == "?"
lines = ["a", "", "b"]
assert [(i, l) for i, l in enumerate(lines, 1) if l] == [(1, "a"), (3, "b")]
it, total = iter([1, 2, 3]), 0
while (x := next(it, None)) is not None: total += x
assert total == 6
# VARIATION: add a case ["mul", x, y] and a guard rejecting non-digits
# VARIATION: match a dict command {"op": "add", "args": [..]}
