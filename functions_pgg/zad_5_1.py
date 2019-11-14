"""
Zaimplementuj funkcję obliczającą silnie dla zadanej wartości. Przykład użycia:
silnia(5)
120


Żeby zrozumieć rekurencję, najpierw trzeba zrozumieć rekrurencje.

REKURENCJA
1. warunek stopu
2. trzeba podzielić problem na mniejsze kawałki
3. wywolujemy siebie z innym zestawem argumentow
4. zbieramy
5. scalamy
6. oddajemy finalny wynik
"""


def silnia(n):
    if n < 0:
        raise ValueError('n musi być większe/równe 0')

    if n == 0:
        return 1
    else:
        return n * silnia(n-1)


import pytest

def test_liczb_ujemnych():
    with pytest.raises(ValueError):
        silnia(-1)

def test_liczb_nieujemnych():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6
    assert silnia(5) == 120
    assert silnia(8) == 40320

