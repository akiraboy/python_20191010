'''
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`.
Np. dla parametru 3 powinno się wypisać:
   *
 * * *
* * * * *
'''

liczba = int(input("Podaj liczbę całkowitą: "))


def holidaybush(n):
    z = n - 1
    x = 1
    for i in range(n):
        print(' ' * z + '*' * x + ' ' * z)
        x+=2
        z-=1

holidaybush(liczba)