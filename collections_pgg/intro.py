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