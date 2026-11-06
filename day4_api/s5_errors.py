"""D4 P5 Errors: exception hierarchy, ExceptionGroup."""
class ApiError(Exception):
    def __init__(self, status):
        super().__init__(f"HTTP {status}")
        self.status = status

class NotFound(ApiError): pass

def check(status):
    if status == 404: raise NotFound(status)
    if status >= 400: raise ApiError(status)
    return status

for s, exc in [(404, NotFound), (500, ApiError)]:
    try: check(s)
    except exc as e: assert e.status == s
assert check(200) == 200
try:
    raise ExceptionGroup("many", [ValueError("a"), KeyError("b")])
except* ValueError as eg:
    assert len(eg.exceptions) == 1
except* KeyError as eg:
    assert len(eg.exceptions) == 1
# VARIATION: catch NotFound before ApiError, then swap the order; what changes?
# VARIATION: add .add_note() to an exception and print the traceback
