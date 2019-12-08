'''
Przygotuj funkcję, która będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.

- `suma(liczby)` - zwraca sumę liczb z listy `liczby`
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby`
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(tab, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `ile_wiekszych(tab, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
'''

x = list(map(int, input("Podaj liczby oddzielone spacja: ").split())) 

def suma(n:list):
    return sum(n)
  
print(suma(x))

def srednia(n):
    a = sum(n)
    b = len(n)
    return a / b
    
print(srednia(x))

def max(x):
    return max(x)

def roznica_min_max(x:list):
    if len(x) != 0:
        return max(x) - min(x)
    else:
        return 0
