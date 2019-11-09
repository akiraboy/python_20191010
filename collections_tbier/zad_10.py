napis = input('Podaj napis: ')
wystapienia = {}

for znak in napis.lower():
    if znak not in wystapienia:
        wystapienia[znak] = 0

    wystapienia[znak] += 1
for litera, liczba_wystapien in wystapienia.items():
    print(f'{litera} = {liczba_wystapien}')

print(sorted(wystapienia))
for litera in sorted(wystapienia):
    print(f'{litera} = {wystapienia[litera]}')