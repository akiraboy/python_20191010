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

