"""
Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora swobodnego
na dwuwymiarowej płaszczyźnie.
Wektory powinny mieć możliwość dodawania, odejmowania,
mnożenia (przez liczbę), porównywania (po długości)
oraz powinny posiadać czytelną reprezentację napisową.
Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2
"""
import math


class Vector:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __add__(self, other):
        if type(other) is not Vector:
            raise TypeError('You can use only Vector')
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) is not Vector:
            raise TypeError('You can use only Vector')
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) not in [int, float]:
            raise TypeError('Use int or float')
        return Vector(self.x * other, self.y * other)

    # def __len__(self): # https://docs.python.org/3/reference/datamodel.html#object.__len__

    @property
    def len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, other): # >
        return self.len > other.len

    def __ge__(self, other): # >=
        return self.len >= other.len

    def __lt__(self, other): # <
        return self.len < other.len

    def __le__(self, other): # <=
        return self.len <= other.len

    def __eq__(self, other): # ==
        return self.len == other.len

    def __ne__(self, other): # !=
        return self.len != other.len


def test_dodawania():
    v1 = Vector(1, 2)
    v2 = Vector(3, 5)
    v3 = v1 + v2
    assert v3.x == 4 and v3.y == 7

import pytest
def test_dodawania_nie_vectora():
    v1 = Vector(1, 2)
    with pytest.raises(TypeError):
        v2 = v1 + 5

def test_odejmowania():
    v1 = Vector(1, 2)
    v2 = Vector(3, 5)
    v3 = v1 - v2
    assert v3.x == -2 and v3.y == -3

def test_mnozenia():
    v1 = Vector(x=1, y=2)
    v2 = v1 * 5
    assert v2.x == 5 and v2.y == 10




