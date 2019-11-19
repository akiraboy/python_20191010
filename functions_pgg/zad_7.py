"""
Zaimplementuj funkcję przycinającą listę na podstawie podanego warunku początkowego oraz końcowego:
Przykład użycia:
przytnij(
klucz 0  1  2  3  4  5  6
data=[1, 2, 3, 4, 5, 6, 7],
start=lambda x: x > 3,
stop=lambda x: x == 6, )
[4, 5, 6]
"""

def przytnij(data, start, stop):
    index_start = -1
    for index, wartosc in enumerate(data):
        if start(wartosc):
            index_start = index
            break

    if index_start == -1:
        return []

    wynik = []
    for wartosc in data[index_start:]:
        wynik.append(wartosc)
        if stop(wartosc):
            break

    return wynik


def test_zaden():
    assert przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: False,
        stop=lambda x: x == 6
    ) == []


def test_ostatni():
    assert przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x == 7,
        stop=lambda x: x == 6
    ) == [7]

def test_wieksze_od_3_i_rowne_6():
    assert przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6
    ) == [4, 5, 6]

