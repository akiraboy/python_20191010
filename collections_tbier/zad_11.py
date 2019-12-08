liczby = set()

liczby_parzyste = set()

for i in range(0, 101, 2):
    liczby_parzyste.add(i)

liczby_parzyste = set(range(0, 101, 2))

while True:
    liczba = input("")
    if liczba == 'koniec':
        break
    else:
        liczby.add(int(liczba))

print(f'Podałes {len(liczby)} unikalnych liczb')

czesc_wspolna = liczby & liczby_parzyste

print(czesc_wspolna)

print(f'Liczb parzystych jest {len(czesc_wspolna)}')