"""
Napisz program zamieniający miejscami w zadanej liście liczb
element największy z najmniejszym.
"""

#         0   1   2   3   4   5
liczby = [49, 50, 20, 40, 35, 10]

# przygotowanie zmiennych do indexu max i min
index_min = None # nie mozemy wpisac 0, bo to legalna wartosc
index_max = None

# petla przeiteruje po wszystkich elementach tablicy i znajde
# najmniejszy i najwiekszy element -> ich indeksy wloze do zmiennych
for index, wartosc in enumerate(liczby):
    # print(index, wartosc)
    if index_min is None or wartosc < liczby[index_min]:
        index_min = index
    if index_max is None or wartosc > liczby[index_max]:
        index_max = index


print(index_min, index_max)

# zamienie miejscami wartosci pod znalezionymi indeksami
print(liczby)

# tmp = liczby[index_min]
# liczby[index_min] = liczby[index_max]
# liczby[index_max] = tmp

liczby[index_min], liczby[index_max] = liczby[index_max], liczby[index_min]

print(liczby)






