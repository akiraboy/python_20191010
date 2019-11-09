"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
Sprawdź jak dużo z tych liczb jest liczbami parzystymi w zakresie 0-100
- w tym celu skorzystaj z operatora iloczynu.
"""

liczby = set() # {} - to nie stworzy pustego zbioru, tylko słownik

liczby_parzyste = set()
for i in range(0, 101, 2):
    liczby_parzyste.add(i)

liczby_parzyste = set(range(0,101,2))

liczby_parzyste = { x for x in range(0,101,2) }

print(liczby_parzyste)

while True:
    liczba = input("Podaj liczbę: ")
    if liczba == "koniec":
        break;
    else:
        liczby.add(int(liczba))

print(f'Podałeś {len(liczby)} unikalnych liczb')

czesc_wspolna = liczby & liczby_parzyste

print(f'Liczb parzystych od 0 do 100 = {len(czesc_wspolna)}')