"""
Napisz program zliczający liczbę wystąpień każdego znaku
w podanym przez użytkownika napisie.
"""

napis = input("Podaj napis: ")
wystapienia = {}

for znak in napis.lower():
    if znak not in wystapienia:
        wystapienia[znak] = 0

    wystapienia[znak] += 1

for litera, liczba_wystapien in wystapienia.items():
    print(f'{litera} = {liczba_wystapien}')

print(sorted(wystapienia))
print(sorted(wystapienia.items()))

for litera in sorted(wystapienia): # dostajemy listę kluczy ze słownika
    print(f'{litera} - {wystapienia[litera]}')

print()

for litera, liczba_wystapien in sorted(wystapienia.items()): # dostajemy listę tupli (klucz, wartosc) ze słownika
    print(f'{litera} = {liczba_wystapien}')