# KOLEKCJE

#########
# TUPLA #
#########
# tupla, krotka (ang. tuple)
# definiujemy w nawiasach ()

a = (1,2,3)
print(type(a))
print(a)

b = (1, 2.5, 'Ala', True, (1,2))
print(b)

# c = (100)
c = (100, )
print(type(c))
print(c)

d = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print( d[2] )
print( d[9] )
# print( d[10] ) # tuple index out of range
print( d[-1] )

# Operator wycinania []
# [ start : stop-1 : krok]
print( d[0:2] ) # elementy: 0,1
print( d[2:] ) # elementy: od 2 do końca
print( d[:2] )  # elementy: od 0 do 2
print( d[:-1] )
print( d[:] )
# print( d[] ) # NK
print( d[-4: -1] )
print( d[::2] )
print( d[::-1] )
print( d[::-2] )

# d[0] = 'A' # nie zmieniamy tupli!

print(len(d))
print( 'a' in d )

e = ( (10,20,30), 10,20,30,40,50)
f = (10,20,30)
print(f in e)

print(min(f))
print(max(f))
print(sum(f))
print(min(d))
print(max(d))

g = (1,2,3)
h = (4,5,6)

i = g + h
print(i)
# j = g*h
j = g*5
print(j)

#########
# LISTA #
#########
# tworzymy przy użyciu []
a = [10,20,30,40,50,60,70,80,90,100]

print(type(a))
# operator [] i wycinania, działa tak samo jak w tupli
print(a[0])

a[0] = 11
print(a)

a.append(72)
print(a)

a.insert(2, 25)
print(a)

a[0:2] = [1,2]
print(a)

a.insert(2, [3,4])
print(a)
print(a[2][1])

a[0:2] = [11,22,33] # dwa podmienił, trzeci dodał
print(a)

# CRUD - Create Read Update Delete
del(a[0])
print(a)

del(a[0:2])
print(a)

del(a[-3:])
print(a)

del(a[:])
print(a)

#############
# PETLA FOR #
#############
lista = [10,20,30,40,50,60,70,80,90,100]

i = 0
while i < len(lista):
    print(f"Element listy: {lista[i]}")
    i += 1

for x in lista:
    print(f"Element listy: {x}")

# range(start, stop-1, krok)
# range(10) - wartosci od 0 do 9

for wartosc in range(10):
    print(wartosc, end=" ")

print()

for wartosc in range(4, 10):
    print(wartosc, end=" ")

print()

for wartosc in range(0, 11, 2):
    print(wartosc, end=" ")

print()

a = [1, 10, 5, 9, 3, 4, 2, 11]
print(a)
a.sort()
print(a)

b = ['z', 'c', 'a', 'o', 'ą']
print(b)
b.sort() # sortowanie jak w encyklopedii, ale uwaga na polskie znaki
print(b)

##########
# NAPISY #
##########

napis = "Ala ma kota a kot ma kompilator"

print(napis[0]) # napisy indeksujemy od 0
print(napis[1:])
print(napis[1:3])
print(napis[:-1])
print(napis[::2])
print(napis[::-1])

a = "Kamil ślimak"
a = a.lower().replace(" ", "").strip()
print(a[:])
print(a[::-1])
print( a[:] == a[::-1] ) # sprawdzenie czy ciag znakow jest palindromem

print(napis.lower())
print(napis.upper())
print(napis.title())
print(napis.capitalize())

print(napis.split(' '))
print(napis.split()) # domyślnie dzieli po spacji
print(list(napis))
print( [c for c in napis] ) # list comprehension

print(len(napis))
print(napis.count('a'))
print(napis.index('a'))
print(napis.find('a'))

# print(napis.index('z')) # jak nie znajdzie znaku, to rzuca wyjatkiem
print(napis.find('z')) # jak nie znajdzie to daje -1

print("-"*30)

###########
# SLOWNIK #
###########

slownik = {
    'ala': 10,
    'ela': 20,
    'ula': 30,
    100: 40,
    2.5: 50,
    (1,2): 60,
    True: 70, # True.__hash()__ zwroci 1
    1: 75, # 1.__hash()__ zwroci 1
    None: 80,
    # [1,2]: 90,
    'kot': {
        'a': 1,
        'b': 2,
    }
}

print(slownik)
print(slownik['ala'])
print(slownik[100])
print('ala'.__hash__())
print('ala'.__hash__())
print(True.__hash__())
print(True.__hash__())
print(False.__hash__())
print(None.__hash__())
print(None.__hash__())

slownik['ala'] = 500
print(slownik)

print('ala' in slownik)
print(slownik.get('ala'))
print(slownik.get('krysia', 'brak'))
print(slownik.get('krysia'))

del(slownik['ala'])
print(slownik)

element = slownik.pop('ela') # wyciaga element ze slownika i usuwa go ze slownika
print(element)
print(slownik)
print()

slownik['marek'] = 1000
print(slownik)
element = slownik.popitem() # ściąga ostatnio dodany element, od pythona 3.7 to jest ostatnio dodany element, wcześniej to był losowy element
print(element)
print(slownik)

for key, value in slownik.items():
    print(f"klucz={key} wartosc={value}")

print(slownik.items())
print(slownik.keys())
print(slownik.values())

print('-'*30)

#########
# ZBIÓR #
#########

zbior = {10,20,30,40,50,60}

print(zbior)
# print(zbior[0]) # [] nie działa na zbiorach
zbior.add(70)
print(zbior)

zbior.remove(60)
# zbior.remove(60) # jak próbuje usunac element, ktore nie ma, to dostaje wyjatek
zbior.discard(60) # jak nie ma elementu to nie będzie wyjatku
print(zbior)

print(len(zbior))

for x in zbior:
    print(x)

# operacje teoriomnogościowe

a = {1,2,3}
b = {1,2,4,5}

# SUMA
print(a | b)
print(a.union(b))

# ILOCZYN - część wspólna, przecięcie
print(a & b)
print(a.intersection(b))

# RÓŻNICA  - od a odejmiemy b
print(a - b)
print(a.difference(b))

print(b - a)

# RÓŻNICA SYMETRYCZNA
print(a ^ b)
print(a.symmetric_difference(b))

# Czy zbiory są rozłączne - nie mają części wspólnej
print(a.isdisjoint(b))

# Czy a jest podzbiorem b? Zbiory mogą być takie same
print(a <= b)

c = {1,2}
print(c <= a)

print(c < a) # bez =, czyli zbiory nie mogą być takie same
d = {1,2,3}
print(d < a)

# a < b, a > b, a <= b, a >= b

# Modyfikacja elementów
# update - dołożyć elementy z b do a
a = {1,2,3}
b = {1,2,4,5}

# a |= b
a.update(b)
print(a)
print(b)

# chcemy zostawić tylko część wspólną
a = {1,2,3}
b = {1,2,4,5}

# a &= b
a.intersection_update(b)

print(a)
print(b)

# chcemy zostawić tylko różnicę
a = {1,2,3}
b = {1,2,4,5}

# a -= b
a.difference_update(b)

print(a)
print(b)

# zostawiamy w a tylko to co nie jest częścią wspólna
a = {1,2,3}
b = {1,2,4,5}

# a ^= b
a.symmetric_difference_update(b)

print(a)
print(b)

pusty_zbior = set()

#####################
# WYRAŻENIA LISTOWE #
#####################
# https://realpython.com/lessons/generalized-list-comprehension-structure/
# wyrażenia listowe (list comprehension) - []
# wyrażenia zbiorowe (set comprehension) - {}
# wyrażenia słownikowe (dict comprehension) - { x:y }
# nie ma wyrażeń tuplowych, bo ( ) będzie tzw. generatorem

dane = [10,20,30,40,50,60,70,80,90,100]
print(dane)

# chce zrobić listę, gdzie elementy są kwadratami tych danych
wynik = []
for wartosc in dane:
    wynik.append(wartosc ** 2)

print(wynik)

wynik = [ wartosc ** 2 for wartosc in dane ]
print(wynik)

"""
Jak odczytac wyrazenia listowe:
(values) = [ (expression) for (value) in (collection) if (condition) ]

(values) = []
for (value) in (collection):
    if (condition):
        (values).append( (expression) )
"""

# pensje brutto
pensje = [1000, 2000, 2500, 1500, 5000]

# potrzebuje mieć listę kwot do wypłaty pracownikom
# potrzebuję pensje netto, podatek dochodowy to 19%
do_wyplaty = []
for pensja in pensje:
    do_wyplaty.append( round(pensja * 0.81, 2) )

do_wyplaty = [ round(pensja * 0.81, 2) for pensja in pensje ]

print(do_wyplaty)

# Premie - jeżeli pensja (brutto) <= 2000 to wtedy 10% premii, w przeciwnym przypadku 0
premie = []
for pensja in pensje:
    if pensja <= 2000:
        premie.append(0.1)
    else:
        premie.append(0.0)

#          |    expression              |
premie = [ 0.1 if pensja <= 2000 else 0.0 for pensja in pensje ]

print(premie)

# https://docs.python.org/3.3/library/functions.html#zip
print(do_wyplaty)
print(premie)
print(list( zip(do_wyplaty, premie) ))
print(list( zip([1,2,3], [1,2]) ))

wartosc_premii = [ pensja * premia for pensja, premia in zip(do_wyplaty, premie) ]
print(wartosc_premii)

do_wyplaty_z_premia = [ pensja + premia for pensja, premia in zip(do_wyplaty, wartosc_premii)]
print(do_wyplaty_z_premia)

# chcemy wiedzieć, kto dostanie więcej niż 2000 zł wypłaty
najdrozsi = [ pensja for pensja in do_wyplaty_z_premia if pensja > 2000 ]
print(najdrozsi)


liczby = [10,20,30,40,50,60,70,80,90,100]
generator_liczb = (x for x in liczby) # to nie jest tupla, to jest generator

for liczba in generator_liczb:
    print(liczba)