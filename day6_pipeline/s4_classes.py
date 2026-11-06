"""D6 P4 Classes: iterable vs iterator, __slots__."""
class Window:
    __slots__ = ("data", "size")
    def __init__(self, data, size): self.data, self.size = data, size
    def __iter__(self):
        for i in range(len(self.data) - self.size + 1):
            yield self.data[i:i + self.size]
    def __len__(self): return max(0, len(self.data) - self.size + 1)

w = Window([1, 2, 3, 4], 2)
assert list(w) == [[1, 2], [2, 3], [3, 4]] and len(w) == 3
assert list(w) == list(w)   # re-iterable: each iter() makes a fresh generator

class Countdown:
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0: raise StopIteration
        self.n -= 1
        return self.n + 1

c = Countdown(3)
assert list(c) == [3, 2, 1] and list(c) == []   # one-shot: it is its own iterator
# VARIATION: try adding a new attribute to Window to see __slots__ at work
# VARIATION: make Countdown re-iterable by returning a fresh iterator in __iter__
