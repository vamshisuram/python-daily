"""D4 P8 Quality: generics, Literal, Callable, match on types."""
from typing import Callable, Literal, TypeVar

T = TypeVar("T")
def first(xs: list[T], default: T) -> T: return xs[0] if xs else default
assert first([], 0) == 0 and first(["a"], "z") == "a"

Method = Literal["GET", "POST"]
def req(m: Method, h: Callable[[str], str]) -> str: return h(m)
assert req("GET", str.lower) == "get"

def parse(v: int | str | None) -> int:
    match v:
        case None: return 0
        case int(): return v
        case str(): return int(v)

assert (parse(None), parse(3), parse("4")) == (0, 3, 4)
# VARIATION: rewrite `first` with PEP 695 syntax: def first[T](...)
# VARIATION: if mypy is installed, run it and break a type on purpose
