"""D2 P7 Concurrency: shared state needs a Lock."""
import threading

inv = {"a": 0}
lock = threading.Lock()

def add():
    for _ in range(1000):
        with lock: inv["a"] += 1

ts = [threading.Thread(target=add) for _ in range(4)]
for t in ts: t.start()
for t in ts: t.join()
assert inv["a"] == 4000
# VARIATION: remove the lock and increase iterations; does it ever lose updates?
# VARIATION: replace the lock with queue.Queue and a single consumer
