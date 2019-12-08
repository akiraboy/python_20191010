
def wiecej_niz(napis:str, ile_znakow:int):
    '''

    :param napisz:
    :param ile_znakow:
    :return:
    '''

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


print(wiecej_niz('ala ma kota, kot ma ale', 3))


def test_przyklad_z_zadania():
    assert wiecej_niz('alama ma kota, kot ma ale', 3) == {'a', ' '}

def test_dla_pustego_napis():
    assert  wiecej_niz('', 2) == set()

def test_dla_roznej_wielkosci_znakow():
    assert wiecej_niz('AAAb', 2) == {'a'}
