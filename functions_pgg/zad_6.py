"""
Zaimplementuj funkcję spłaszczającą podaną listę. Przykład użycia:
splaszcz([1, 2, 3, [4, 5, [6]], 7])
[1, 2, 3, 4, 5, 6, 7]
"""

def splaszcz(lista):
    if type(lista) != list:
        raise TypeError("List expected.")

    wynik = []

    for element in lista:
        if type(element) == list:
            wynik += splaszcz(element)
        else:
            wynik.append(element)

    return wynik


def test_splaszcz():
    assert splaszcz( [ 1, 2, 3, [4,5] ] ) == [1,2,3,4,5]
    assert splaszcz([]) == []
    assert splaszcz([1,2,3,4,5]) == [1,2,3,4,5]
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert splaszcz([1, 2, 'a', 3.5]) == [1, 2, 'a', 3.5]
    assert splaszcz([1, 2, 3, [], 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert splaszcz([[[1,[2,3,[4,[5,6]]]],[7]],[8,9]]) == [1,2,3,4,5,6,7,8,9]

import pytest

def test_splaszcz_nie_z_lista():
    with pytest.raises(TypeError):
        splaszcz(1)

    with pytest.raises(TypeError):
        splaszcz('ala ma kota')

    with pytest.raises(TypeError):
        splaszcz({1,2,3,4,5})

