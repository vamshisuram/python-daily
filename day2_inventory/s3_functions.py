"""D2 P3 Functions: defaults, *args/**kw, partial, sort key."""
from functools import partial

def restock(inv, name, qty=1, *, log=None):
    log = [] if log is None else log   # never use log=[] as a default
    inv[name] = inv.get(name, 0) + qty
    log.append(name)
    return log

inv = {}
restock(inv, "a"); restock(inv, "a", qty=4)
assert inv == {"a": 5}

def total(*qtys, **named): return sum(qtys) + sum(named.values())
assert total(1, 2, x=3) == 6
partial(restock, qty=10)(inv, "b")
assert sorted(inv, key=inv.get, reverse=True) == ["b", "a"]
# VARIATION: change log=None to log=[] and call twice to see the shared-default bug
# VARIATION: make restock positional-only for inv using `/`
