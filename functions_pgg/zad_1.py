"""
Napisz funkcję sprawdzającą, czy dane liczba jest liczbą pierwszą. Przykład użycia:
czy_jest_pierwsza(10)
False
czy_jest_pierwsza(17)
True
"""

# inty wieksze od 1, które się dzielą tylko przez 1 i samą siebie

def czy_jest_pierwsza(liczba):
    # if liczba <= 1:
    #     return False

    for i in range(2, liczba):
        if liczba % i == 0:
            return False

    return True


# print(czy_jest_pierwsza(10))
# print(czy_jest_pierwsza(17))
# print(czy_jest_pierwsza(1))
# print(czy_jest_pierwsza(-1))

# pytest
# Settings / Tools / Python Integrated Tools / Testing / Default test runner -> pytest
# pip install pytest
# jeżeli uruchomiliśmy program wcześniej, to trzeba usunąć konfigurację uruchomieniową

def test_czy_jest_pierwsza():
    liczba = -10
    wynik = czy_jest_pierwsza(liczba)
    assert wynik == False










