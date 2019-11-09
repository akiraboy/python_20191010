"""
Napisz program wyliczający kwotę należną za zakupiony towar na podstawie
podanej przez użytkownika wagi i nazwy produktu.
Do przechowywania informacji o cenie za kilogram danego produktu użyj słownika.
Wypisz wszystkie dostępne produkty w sklepie.
"""

produkty = {
    'ziemniaki': 2.2,
    'pietruszka': 6.5,
    'pomidory': 3.4,
    'marchewka': 0.5,
    'cebula': 2.0,
}

print('Produkty w naszym super samie:')
for produkt, cena_za_kilo in produkty.items(): # uwaga! "Czary" sie dzieją jak damy for produkty, cena_za_kilo...
    print(f'{produkt} - {cena_za_kilo:.2f} zł / kg')

co = input("Co chcesz kupić? ")

if co not in produkty:
    print('Sory, ale nie ma takiego produktu w sklepie!')
    exit(1) # 0 - podajemy jak program skonczył działanie normalnie, tzn. wszystko jes OK, cokolwiek innego oznacza, że nie jest OK

liczba_kg = float(input(f'Ile kg {co} chcesz kupić? '))

kwota = produkty[co] * liczba_kg

print(f'Za {liczba_kg} kg produktu {co} zaplacisz {kwota:.2f} zł')
