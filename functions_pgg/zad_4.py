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

