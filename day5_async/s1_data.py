"""D5 P1 Data: deque frontier, seen-set, heap (crawler state)."""
import heapq
from collections import deque

graph = {"a": ["b", "c"], "b": ["c"], "c": []}
frontier, seen, order = deque(["a"]), {"a"}, []
while frontier:
    n = frontier.popleft()
    order.append(n)
    for m in graph[n]:
        if m not in seen:
            seen.add(m)
            frontier.append(m)
assert order == ["a", "b", "c"]
h = []
heapq.heappush(h, (2, "b")); heapq.heappush(h, (1, "a"))
assert heapq.heappop(h) == (1, "a")
# VARIATION: pop() from the right instead; BFS becomes DFS
# VARIATION: use heapq.nsmallest(2, ...) on a list of (priority, url)
