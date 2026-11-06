"""D3 P8 Quality: logging to a handler, tracebacks."""
import logging, traceback

class ListHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.msgs = []
    def emit(self, r): self.msgs.append(r.getMessage())

log = logging.getLogger("t")
log.setLevel(logging.INFO)
h = ListHandler()
log.addHandler(h)
log.info("x=%d", 3)
log.debug("skip")
assert h.msgs == ["x=3"]
try: 1 / 0
except ZeroDivisionError: assert "ZeroDivisionError" in traceback.format_exc()
# VARIATION: set level to DEBUG and assert both messages
# VARIATION: run this file with `python -m pdb` and step to the try block
