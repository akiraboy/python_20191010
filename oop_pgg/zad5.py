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
            raise TypeError('You can us only Vector')
        return Vector(self.x + other.x, self.y + other.y)
    @property
    def len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, other):
        return self.len > other.len
     def __ge__(self, other):
         return self.len >= other.len

    def __lt__(self, other):
        return self.len < other.len

    def __le__(self, other):
        return self.len <= other.len

    def __eq__(self, other):
        return self.len = other.len



def test_grater_than():
    v1 = Vector(2, 3)
    v2 = Vector(1, 1)
    assert v1 > v2


def test_dodawania():
    v1 = Vector(1, 2)
    v2 = Vector(3, 5)
    v3 = v1 + v2
    assert v3.x == 4 and v3.y == 7

def test_dodawania_nievectora():
    v1 = Vector(1, 2)
    with pytest.raises(TypeError):
        v2 v1 + 5
        