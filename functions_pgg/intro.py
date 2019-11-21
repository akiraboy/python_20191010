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
# https://docs.python.org/3/reference/expressions.html#lambda
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


def czy_dodatnie(x):
    return x > 0

lista = [-10, -4, 8, 12, -123, 0]
print(lista)

tylko_dodatnie = []
for i in lista:
    if czy_dodatnie(i):
        tylko_dodatnie.append(i)

print(tylko_dodatnie)

tylko_dodatnie = list( filter(czy_dodatnie, lista) )
print(tylko_dodatnie)

tylko_dodatnie = list( filter(lambda x: x>0, lista) )
print(tylko_dodatnie)


# SORTOWANIE po swojemu

lista = [ (2,2), (3,4), (4,1), (1,3) ]
print(lista)

lista.sort()
print(lista)
print()

lista = [ (2,2), (3,4), (4,1), (1,3) ]
print(lista)

lista.sort(key=lambda x: x[1])

print(lista)

# Nasz wlasny komparator
# komparator to jest funkcja, która dla dwóch elementów (a i b)
# ma zwrócić nastepujące wartości
# -1 -> a powinno być przed b
# 0 -> kiedy a i b "są równe"
# 1 -> b powinno być przed a

def komparator(a, b):
    if a[1] < b[1]:
        return 1
    elif a[1] == b[1]:
        return 0
    else:
        return -1

lista = [ (2,2), (3,4), (4,1), (1,3) ]
print(lista)

from functools import cmp_to_key

lista.sort(key=cmp_to_key(komparator))

print(lista)

# DEKORATORY
print()
# funkcje w funkcji

def przedstaw_dzieciaki():
    def pierwsze_dziecko():
        print("Ala")

    def drugie_dziecko():
        print("Piotr")

    pierwsze_dziecko()
    drugie_dziecko()

przedstaw_dzieciaki()

# zasieg zmiennych
print()

def a(x):
    def b():
        print(x)

    b()

a(5)

def dekorator(x):
    def opakowywacz():
        print(x)

    return opakowywacz

funkcja_z_srodka = dekorator(10)

funkcja_z_srodka()
funkcja_z_srodka()

funkcja2 = dekorator(30)
funkcja2()

def hello_world():
    return "hello world!"

opakowana = dekorator(hello_world)
opakowana()



def powiedz_czesc(imie):
    return f'Czesc {imie}!'

def powiedz_jestes_super(imie):
    return f'{imie}, jesteś super!!!'

def pozdrow_piotrka(funkcja_do_pozdrawiania, imie):
    return funkcja_do_pozdrawiania(imie)


print( pozdrow_piotrka(powiedz_czesc, 'Piotr') )
print( pozdrow_piotrka(powiedz_jestes_super, 'Ala') )


def przedstaw_dzieciaki(ktore):
    def pierwsze_dziecko():
        print("Ala")

    def drugie_dziecko():
        print("Piotr")

    if ktore == 1:
        pierwsze_dziecko()
    else:
        drugie_dziecko()

przedstaw_dzieciaki(1)
przedstaw_dzieciaki(2)
print()


def przedstaw_dzieciaki(ktore):
    def pierwsze_dziecko():
        print("Ala")

    def drugie_dziecko():
        print("Piotr")

    if ktore == 1:
        return pierwsze_dziecko
    else:
        return drugie_dziecko

funkcja_dziecko = przedstaw_dzieciaki(2)
funkcja_dziecko()
print()
przedstaw_dzieciaki(1)()

def funkcja(*args, **kwargs):
    print(args, kwargs)

funkcja(1,2,3, a=1,b=2,c=3)


# no to teraz już na prawde dekoratory :D
def dekorator(funkcja_do_udekorowania):
    def opakowanie(*args, **kwargs):
        print('Przed wywołaniem')
        wynik = funkcja_do_udekorowania(*args, **kwargs)
        print('Po wywołaniu')
        return wynik

    return opakowanie

def hello_world():
    print('Hello world!')

hello_world()


udekorowane_hello_world = dekorator(hello_world)
udekorowane_hello_world()


udekorowane_print = dekorator(print)
udekorowane_print('Ala', 1, 3, True, None)


udekorowane_sum = dekorator(sum)
print( udekorowane_sum([10,20,30]) )

@dekorator
def sumator(a, b):
    return a+b

def sumator1(a, b):
    return a+b

sumator_udekorowany1 = dekorator(sumator1)

suma = sumator(5, 3)
print(suma)


# domknięcie / closure
def stworz_przemnazacz(x):
    def przemnazacz(y):
        return x*y

    return przemnazacz


przez_5 = stworz_przemnazacz(5)

print( przez_5(10) )






