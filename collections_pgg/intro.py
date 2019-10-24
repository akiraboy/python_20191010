# Kolekcje

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

# lista
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

# PETLA FOR
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


# NAPISY

napis = "Ala ma kota a kot ma kompilator"

print(napis[0]) # napisy indeksujemy od 0
print(napis[1:])
print(napis[1:3])
print(napis[:-1])
print(napis[::2])
print(napis[::-1])

a = "Kamil ślimak"
a = a.lower().replace(" ", "")
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