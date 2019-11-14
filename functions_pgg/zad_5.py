"""
Zaimplementuj funkcję obliczającą silnie dla zadanej wartości. Przykład użycia:
silnia(5)
120
"""

def silnia(n):
    if n < 0:
        raise ValueError('n musi być większe/równe 0')
    # elif n == 0:
    #     return 1
    # else:
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik

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

