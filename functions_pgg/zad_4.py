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

# formatuj('Hello world!') == 'Hello world!'
# formatuj('Hello world!', 'Ala ma kota') == 'Hello world!\nAla ma kota'
# formatuj('Hello world!', imie='Ala') == 'Hello world!'
# formatuj('Hello $imie!', imie='Ala') == 'Hello Ala!'
# formatuj('Hello $imie, $nazwisko!', imie='Ala') == 'Hello Ala, $nazwisko!'
# formatuj('Hello $imie, $nazwisko!', imie='Ala', nazwisko='Kowalski')
# == 'Hello Ala, Kowalski!'

