liczby = [54, 98, 43, 65, 32, 21]

index_min = None
index_max = None

for index, wartosc in enumerate(liczby):
    #print(index, wartosc)
    if index_min is None or wartosc < liczby[index_min]:
        index_min = index
    if index_max is None or wartosc > liczby[index_max]:
        index_max = index
print(index_min, index_max)

print(liczby)

liczby[index_min], liczby[index_max] = liczby[index_max], liczby[index_min]

print(liczby)