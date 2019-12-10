"""
Zaimplementuj iterator odliczający od 0 do zadanego limitu.
Przykładowe użycie:
for number in Counter(10): ...
"""

class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.index = 0
        return self # zawsze w __iter__ musimy zwrócić "iterator", w tym wypadku to ten sam obiekt

    def __next__(self):
        if self.index > self.limit:
            raise StopIteration

        result = self.index
        self.index += 1
        return result


for i in Counter(10):
    print(i)


