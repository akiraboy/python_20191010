#         0   1   2   3   4   5
liczby = [49, 50, 20, 40, 35, 10]

liczba_min = min(liczby)
liczba_max = max(liczby)

print(liczba_min, liczba_max)

index_liczba_min = liczby.index(liczba_min)
index_liczba_max = liczby.index(liczba_max)

print(index_liczba_min, index_liczba_max)

print(liczby)
liczby[index_liczba_min], liczby[index_liczba_max] = liczby[index_liczba_max], liczby[index_liczba_min]
print(liczby)
