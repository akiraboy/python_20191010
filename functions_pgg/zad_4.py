"""
Zaimplementuj funkcję formatującą podane napisy.
Przykład użycia:
formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena=10, )
'koszt 10 PLN\nkwota 10 brutto'
"""

def formatuj(*args, **kwargs):
    wynik = []
    for napis in args:
        for nazwa, wartosc in kwargs.items():
            napis = napis.replace(f'${nazwa}', str(wartosc))

        wynik.append(napis)

    # napis_wynikowy = ''
    # for napis in wynik:
    #     napis_wynikowy += '\n' + napis

    return '\n'.join(wynik)

def testy_zbiorcze():
    assert formatuj('Hello world!') == 'Hello world!'
    assert formatuj('Hello world!', 'Ala ma kota') == 'Hello world!\nAla ma kota'
    assert formatuj('Hello world!', imie='Ala') == 'Hello world!'
    assert formatuj('Hello $imie!', imie='Ala') == 'Hello Ala!'
    assert formatuj('Hello $imie, $nazwisko!', imie='Ala') == 'Hello Ala, $nazwisko!'
    assert formatuj('Hello $imie, $nazwisko!', imie='Ala', nazwisko='Kowalski') == 'Hello Ala, Kowalski!'

