# Funkcje

def powiedz_czesc():
    print("Cześć!")

powiedz_czesc()

def powiedz_czesc_komus(imie, nazwisko):
    print(f'Cześć {imie} {nazwisko}!')

powiedz_czesc_komus("Piotr", "GG")

def suma(a,b):
    return a+b

wynik = suma(2,3)
print(wynik)

# możemy zwracać kilka rzeczy z funkcji
def dodawanio_mnozenie(a,b):
    return a+b, a*b

print( dodawanio_mnozenie(2,3) )

wynik_dodawania, wynik_mnozenia = dodawanio_mnozenie(2,3)
print(wynik_dodawania, wynik_mnozenia)


# dokumentacja (docstring)
# type hinting
def iloczyn(a: int, b: int) -> int:
    """
    Funkcja, która liczy iloczyn a i b
    :param a:int
    :param b:int
    :return:int
    """
    return a*b


print(iloczyn(2,5))
# PyCharm podpowiada, że typy nam się nie zgadzają
# niemniej, to nie jest przeszkoda, żeby uruchomić program
# print(iloczyn('a', 'b'))
print()
print()

# zasięg zmiennych i funkcjach zagniezdzonych

a = 10
def zewnetrzna():

    def wewnetrzna(): # wewnatrz funkcji zewnetrzna mam do dyspozycji funkcje wewnetrzna
        print(f"Ala ma kota, a={a}")
        return 5

    wynik = wewnetrzna()
    print(f'Wynik funkcji wewnetrzna = {wynik}')


zewnetrzna()

# argumenty domyślne
def opakowywacz(napis, start=">>", end="<<", dopisek=""):
    return start + napis + end + dopisek

print(opakowywacz("Ala ma kota"))
print(opakowywacz("Ala ma kota", "[", ']'))
print(opakowywacz("Ala ma kota", "["))
print(opakowywacz("Ala ma kota", end="{{", dopisek="!"))
print(opakowywacz(start="}}", dopisek="!", napis="Ala ma kota")) # jak nie zaczynam od argumentu pozycyjnego, to go trzeba wymienić z nazwy
print()

# przekazywanie wielu argumentów do funkcji
print(1,2,'ala')

# *args
#   - możemy podać dowolnie wiele argumentów pozycyjnych
#   - argument args jest tupla
#   - nie ważna jest nazwa argumentu - args jest zwyczajowe, tylko istotna jest * przed nazwą tego argumentu
# **kwargs (key-word argument)
#   - argument kwargs jest słownikiem

def zliczacz(*args, **kwargs):
    print("*args ->", args)
    print("**kwargs ->", kwargs)


zliczacz()
zliczacz(1, 2, 'ala', 3.5, ('a', 'b'))
zliczacz(1,2,3,a=10,b=20)
zliczacz(a=1, b=2, c=(1,2,3,4))
# zliczacz(a=1, b=2, 'ala') # błąd kompilacji, najpierw argumenty pozycyjne, później nazwane

def fun(a, b, c=10, *args, **kwargs):
    print(a, b, c, args, kwargs)

# fun(1,2,3,4,5,6,7,8,9,10,a=11,b=12,c=13) # nie możemy przekazać kilku wartości dla tego samego argumentu
fun(1,2,3,4,5,6,7,8,9,10,x=11,y=12,z=13)
fun(1,2,x=11,y=12,z=13)


# FUNKCJE LAMBDA (lambda functions)
# https://pl.wikipedia.org/wiki/Rachunek_lambda
# https://pl.wikipedia.org/wiki/Funkcja_anonimowa
# określenia: funkcja lambda, funkcja anonimowa
# funkcja anonimowa: funkcja bez nazwy
# funkcja lambda: jest używana jako dane

def kwadrat(x):
    return x ** 2

print(kwadrat(3))

kwadrat2 = lambda x: x ** 2
print(kwadrat2(3))
square = kwadrat2
print(square(3))


def sumator(a,b,c):
    return a+b+c

print(sumator(1,2,3))

sumator2 = lambda a,b,c: a+b+c
print(type(sumator))
print(type(sumator2))
print(sumator2(1,2,3))


def x_mniejsze_y(x,y):
    if x<y:
        return True
    else:
        return False

print(x_mniejsze_y(1,2))


x_mniejsze_y = lambda x,y: x<y
print(x_mniejsze_y(1,2))

witaj_swiecie = lambda: "Hello World!"
print(witaj_swiecie())

lista = [1,2,3,4,5,6,7,8,9,10]

mapa = map(lambda x: x*10, lista)

# for i in mapa:
#     print(i)

lista_przemnozona = list(mapa)
print(lista_przemnozona)