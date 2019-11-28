# ===== OOP =====

tupla = (1, 2, 3, 4, 5, 6)
print( type(tupla) )


class Towar:
    pass

a = Towar() # utworzenie nowego obiektu klasy Towar

print(a)

a.nazwa = "Misio Koralgol"
a.cena = 5.99

print(a.nazwa, a.cena)
a.cena = 6.99
print(a.nazwa, a.cena)

b = Towar()
# print(b.nazwa, b.cena) # AttributeError: 'Towar' object has no attribute 'nazwa'


class Towar:
    def wypisz(self):
        print(f'Towar {self.nazwa} kosztuje {self.cena}')

c = Towar()
c.nazwa = "Rower"
c.cena = 1000
print(c)
c.wypisz()

d = Towar()
d.nazwa = "Mazak"
d.cena = 2.99
d.wypisz()


class Towar:
    def __init__(self, nazwa="cos", cena=2.99):
        self.nazwa = nazwa
        self.cena = cena

    def wypisz(self):
        print(f'Towar {self.nazwa} kosztuje {self.cena}')


a = Towar()
a.wypisz()

a = Towar("Kawa", 8.99)
a.wypisz()

a = Towar()
a.wypisz()


print("="*60)

class Towar:
    def __init__(self, nazwa="cos", cena=2.99):
        self.nazwa = nazwa
        self.cena = cena

    def wypisz(self):
        print(f'Towar {self.nazwa} kosztuje {self.cena}')

    def __str__(self):
        return f'Towar {self.nazwa} kosztuje {self.cena}'

a = Towar()
print(a) # tutaj uruchamia się metoda __str__ na naszym obiekcie

a_tekstowo = str(a) # tutaj uruchamia się metoda __str__ na naszym obiekcie
print(a_tekstowo)

print("="*60)


class Matematyka:
    PI = 3.14 # atrybut klasowy

# dostawanie się do atrybutu klasowego
print( Matematyka.PI )
Matematyka.PI = 10.0 # mozna go zmienic, ale skoro jest z duzych liter, to sie nie powinno tego robic
print( Matematyka.PI )



print("="*60)

# Atrybuty i ich widoczność
class Osoba:
    def __init__(self, imie, nazwisko, id):
        self.imie = imie # public
        self._nazwisko = nazwisko # protected
        self.__id = id # private


piotrek = Osoba('Piotr', 'GG', 10)
print(piotrek.imie)
print(piotrek._nazwisko)
# print(piotrek.__id) # Python tutaj robi tzw. name mangling
print(piotrek._Osoba__id)

print("="*60)

# Hermetyzacja / enkapsulacja
# to też konwencja w pythonie

class Osoba:
    def __init__(self, nazwisko, id):
        self._nazwisko = nazwisko
        self.__id = id

    def get_nazwisko(self):
        return self._nazwisko

    def set_nazwisko(self, nazwisko):
        self._nazwisko = nazwisko

    def get_id(self):
        return self.__id


piotrek = Osoba('GG', 1)
print(piotrek.get_nazwisko())
piotrek.set_nazwisko('Grabski-Gradzinski')
print(piotrek.get_nazwisko())

print("="*60)
# Można to zrobić prosciej wykorzystujac mechanizm Pythona - @property
# czyli tzw. atrybuty wyliczane

class Osoba:
    def __init__(self, nazwisko, id):
        self.nazwisko = nazwisko # self.nazwisko -> tu uruchomil sie setter!

    @property
    def nazwisko(self): # "getter"
        print("Jestem w geterze")
        return self._nazwisko

    @nazwisko.getter
    def nazwisko(self):
        print(123)

    @nazwisko.setter
    def nazwisko(self, nowe_nazwisko): # "setter"
        print("Jestem w seterze")
        self._nazwisko = nowe_nazwisko


piotrek = Osoba('GG', 1)
print(piotrek.nazwisko)

print("="*60)
# Co jest prawdą a co fałszem?

zmienna = 'ala ma kota' # PRAWDA
zmienna = '' # FALSZ
zmienna = ' ' # PRAWDA
zmienna = 'False' # PRAWDA
zmienna = '0' # PRAWDA
zmienna = 0 # FALSZ
zmienna = 1 # PRAWDA
zmienna = None # FALSZ
zmienna = () # FALSZ
zmienna = [] # FALSZ
zmienna = [None] # PRAWDA

if zmienna:
    print("PRAWDA")
else:
    print("FALSZ")

print("="*60)

if print("Ala ma kota"):
    print("Jest true")
else:
    print("Jest false")

print( type(print("Ala ma kota")) ) # print zwraca None

print("="*60)
# leniwe wyliczanie warunku
# leniwe wyliczanie działa tak, że jak lewa strona OR jest prawdziwa
# to python nie sprawdza już prawej
# jak lewa strona jest fałszywa, to sprawdza prawą strone
# zmienna = 0
zmienna = 2
if zmienna < 1 or print("Ala ma kota"):
    print("prawda")
else:
    print("falsz")

print("="*60)

# Słownik
slownik = {}
print(slownik)

# print( slownik['a'] ) # KeyError: 'a' - nie ma klucza 'a' w słowniku

print('a' in slownik)

slownik['a'] = 5
print(slownik['a'])
print('a' in slownik)

info = {}
# info['wiek'] += 10 # nie da sie tak zrobic, bo w slowniku nie ma klucza 'wiek'

# defaultdict
# słownik z domyślną wartością
# https://docs.python.org/2/library/collections.html#collections.defaultdict

from collections import defaultdict
info = defaultdict(int) # wartość domyślna, intowe 0

info['wiek'] += 10
print(info)

slownik = defaultdict(str)
print(f" >>{slownik['a']}<< ")

# fabryki wartości domyślnych: int, str, float, tuple, list, set, dict

slownik = defaultdict(list)
print(slownik['a'])

slownik = defaultdict(dict)
print(slownik['a'])

# slownik = defaultdict(5) # TypeError: first argument must be callable or None
# funkcja lambda jest callable, bo da się ją uruchomić
# dodatkowo mogę zdefiniować funkcję lambda bez argumentów i zwrócić jakąś
# konkretną wartość, na przykład 5
slownik = defaultdict(lambda : 5)
print(slownik['a'])


print("="*60)
# METODY SPECJALNE

class Liczba:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        return f'Jestem liczba o wartosci {self.wartosc}'

    def __add__(self, other):
        # Obiekt klasy liczba jest niemutowalny (konwencja)
        # Operacja dodawania dwóch obiektów albo obiektu i liczby
        # nie powoduje zmiany stanu żadnego z obiektów, tylko dostajemy nowy obiekt
        if isinstance(other, Liczba):
            return Liczba(self.wartosc + other.wartosc)
        else:
            return Liczba(self.wartosc + other)


l1 = Liczba(10)
print(l1)

l2 = Liczba(20)
print(l2)

l3 = l1 + l2
# l3 = l1.__add__(l2)
print(l3)

l4 = l1 + l2 + l3
# l4 = l3.__add__( l1.__add__(l2) )
print(l4)

l5 = l1 + 3
print(l5)



