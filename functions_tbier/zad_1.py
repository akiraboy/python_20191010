def czy_jest_pierwsza(liczba):
    if liczba <= 1:
        return False

    for i in range(2, liczba):
        if liczba % 1 == 0:
            return False

    return True

print(czy_jest_pierwsza(40))
print(czy_jest_pierwsza(12))


def test_czy_jest_pierwsza():
    liczba = -10
    wynik = czy_jest_pierwsza(liczba)
    assert wynik == False

def test_czy_jest_pierwsza2():
    assert test_czy_jest_pierwsza(-10) == False
    assert test_czy_jest_pierwsza(-10) is False
    assert  not czy_jest_pierwsza(-10)

def test_czy_jest_pierwsza3():
    assert czy_jest_pierwsza(2)
    assert czy_jest_pierwsza(5) is True


