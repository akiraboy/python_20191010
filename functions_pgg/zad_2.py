"""
Napisz funkcję zwracającą zbiór wszystkich znaków
występujących w napisie więcej niż zadana liczba razy.
Przykład użycia:
wiecej_niz('ala ma kota a kot ma ale', 3) {'a', ' '}
"""

def wiecej_niz(napis:str, ile_znakow:int) -> set:
    """
    Zwraca zbior znaków wystepujacych w napis wiecej niz ile_znakow
    :param napis:
    :param ile_znakow:
    :return:
    """

    napis = napis.lower()
    zliczone_litery = {}
    for znak in napis:
        if znak in zliczone_litery:
            zliczone_litery[znak] += 1
        else:
            zliczone_litery[znak] = 1

    wynik = set()
    for litera in zliczone_litery:
        if zliczone_litery[litera] > ile_znakow:
            wynik.add(litera)

    return wynik


def test_przyklad_z_zadania():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {'a', ' '}


def test_dla_pustego_napis():
    assert wiecej_niz('', 1) == set()

def test_dla_roznej_wielkosci_znakow():
    assert wiecej_niz('AAAbb', 2) == {'a'}


