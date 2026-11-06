"""D3 P1 Data: str methods, format specs, bytes vs str."""
k, _, v = "key=value=more".partition("=")
assert (k, v) == ("key", "value=more")
assert f"{3.14159:.2f}|{42:>5}|{255:#x}|{1234567:,}" == "3.14|   42|0xff|1,234,567"
assert "é".encode("utf-8") == b"\xc3\xa9" and b"\xc3\xa9".decode() == "é"
assert "a,b,,c".split(",") == ["a", "b", "", "c"]
assert "  x ".strip() == "x" and "abc"[::-1] == "cba"
# VARIATION: use rpartition and rsplit(maxsplit=1)
# VARIATION: format a table row with f"{name:<10}{qty:>5}"
