"""D3 P4 Classes: Protocol + registry, callable objects."""
from typing import Protocol

class Command(Protocol):
    def run(self, arg: str) -> str: ...

class Upper:
    def run(self, arg): return arg.upper()

class Rev:
    def run(self, arg): return arg[::-1]

REGISTRY: dict[str, Command] = {"upper": Upper(), "rev": Rev()}
def dispatch(name, arg): return REGISTRY[name].run(arg)

assert dispatch("upper", "ab") == "AB" and dispatch("rev", "ab") == "ba"

class Adder:
    def __init__(self, n): self.n = n
    def __call__(self, x): return x + self.n

assert Adder(2)(3) == 5
# VARIATION: register commands with a decorator @command("name")
# VARIATION: add a Title command; no base class needed (structural typing)
