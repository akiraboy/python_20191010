'''
Stwórz następujące metody. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb,
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
podpowiedź: wartość PI jest dostępna jako `Math.PI`
5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.
'''
from math import pi
from math import sqrt

def stopy_na_metry(n:int):
    '''
    Przelicza stopy na metry.
    :param n:
    :return:
    '''
    return n * 3.28

def max(a:int, b:int):
    if a > b:
        return a
    elif a < b:
        return b

def srednia(a:int, b:int):
    return (a + b) / 2

def pole_kola(r):
    return (pi * r) ** 2

def bmi(wzrost:int, waga:int):
    return wzrost / (waga ** 2)

def pole_trojkata(a:int, b:int, c:int):
    '''
    Liczy pole trojkąta ze wzoru herona
    :param a:
    :param b:
    :param c:
    :return:
    '''
    p = (a + b + c) / 2
    pole = p * sqrt((p - a) * (p - b) * (p - c))
    return pole

def kilometry_na_mile(kilometry):
    return kilometry / 1.6

def mile_na_kilometry(mile):
    return mile * 1.6

a = int(input('Poodaj długosc: '))
b = int(input('Poodaj szerokosc: '))
c = int(input('Poodaj wysokosc: '))

print(f'Pole trójkąta wynosi: {pole_trojkata(a, b, c):.2f}')
