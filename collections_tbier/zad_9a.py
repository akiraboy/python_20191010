produkty = {
    'ziemniaki': 2.2,
    'pietruszka': 6.5,
    'pomidory': 3.4,
    'marchewka': 0.5,
    'cebula': 2.0,
}

print('Produkty w naszym super samie:')
for produkt, cena_za_kilo in produkty.items():
    print(f'{produkty} - {cena_za_kilo:.2f} zł / kg')
co = input('Co chcesz kupić? ')

if co not in produkty:
    print('Sorry, nie ma takiego produktu w sklepie!')
    exit(1)

liczba_kg = float(input(f'Ile kg {co} chcesz kupić? '))

wynik = produkty[co] * liczba_kg

print(f'Za {liczba_kg} kd produktu {co} zpłacisz{kwota:.2f} zł')

