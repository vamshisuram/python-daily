"""D2 P8 Quality: TypedDict, table-driven checks."""
from typing import TypedDict

class Row(TypedDict):
    name: str
    qty: int

def low(rows: list[Row], limit: int = 3) -> list[str]:
    return [r["name"] for r in rows if r["qty"] < limit]

cases = [([], []), ([{"name": "a", "qty": 1}], ["a"]), ([{"name": "a", "qty": 9}], [])]
for rows, want in cases:
    assert low(rows) == want, (rows, want)
# VARIATION: add a boundary case (qty == limit)
# VARIATION: add NotRequired[str] field "note" to Row
