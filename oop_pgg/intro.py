# ===== OOP =====
import math

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

print("="*60)

# ==== DZIEDZICZENIE =====

class Osoba:
    def __init__(self, id, imie, nazwisko):
        self.__id = id
        self._imie = imie
        self._nazwisko = nazwisko

    def __str__(self):
        return f'Osoba: {self.__id} {self._imie} {self._nazwisko}'

class Student(Osoba):
    def __init__(self, id, imie, nazwisko, kierunek, rok):
        super().__init__(id, imie, nazwisko)
        self._kierunek = kierunek
        self._rok = rok

    def __str__(self):
        osoba_info = super().__str__()
        return f'Student: {self._rok}, {self._kierunek}; {osoba_info}'


o1 = Osoba(1, 'Piotr', 'GG')
print(o1)

s1 = Student(2, 'Marek', 'Nowak', 'informatyka', 2)
print(s1)

# ===== WIELODZIEDZICZENIE ====
# czyli dziedziczymy po kilku klasach na raz

class Kolo:
    def __init__(self, r):
        self.r = r

    def powierzchnia(self):
        return math.pi * self.r ** 2

    def obwod(self):
        return 2 * math.pi * self.r

class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def powierzchnia(self):
        return self.a * self.b


class Walec(Kolo, Prostokat):
    def __init__(self, r, h):
        Kolo.__init__(self, r)
        Prostokat.__init__(self, self.obwod(), h)

    def powierzchnia(self):
        pole_kola = Kolo.powierzchnia(self)
        pole_prostokata = Prostokat.powierzchnia(self)
        return (2 * pole_kola) + pole_prostokata


print(Walec.__mro__)

w = Walec(5, 10)
print(w.powierzchnia())


print("="*60)

# ====== WYJATKI ======

def dzielenie(a, b):
    return a/b

# https://realpython.com/python-exceptions/




try:
    print("jestem w try")
    dzielenie(5, 0)
    print("po dzieleniu")

except (TypeError, ZeroDivisionError): # mozemy lapac kilka rodzajow wyjatkow
    print('TypeError, ZeroDivisionError')
except TypeError:
    print('TypeError')
except ArithmeticError as error:
    print('Arithmetic error', error.args)
except ZeroDivisionError:
    print("ZeroDivisionError - Nie można dzielić przez 0.")
except BaseException:
    print('Base Exception')
else:
    # uruchamia tylko wtedy, kiedy nie było wyjatku
    print("jestem w else")
finally:
    # wykonuje sie zawsze, nawet jak był wyjatek
    print("jestem w finally")


print("="*60)
# ===== STATIC METHODS ======
# metody statyczne
# - one nie przyjmują argumentu self, i nawet nie powinny
# - metod statycznych używa się najcześciej w kontekście narzedzi, ktore sa w naszej klasie

# https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html
class TemperatureConverter:
    @staticmethod
    def celc_to_fahr(celcjusz):
        return celcjusz * 1.8 + 32

    @staticmethod
    def fahr_to_celc(fahrenheit):
        return (fahrenheit - 32) / 1.8


wynik = TemperatureConverter.celc_to_fahr(35)
print(wynik)

wynik = TemperatureConverter.fahr_to_celc(104)
print(wynik)

print('='*60)
# ====== CLASS METHODS ========

class Employee:
    def __init__(self, first_name: str, last_name: str, rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.salary = 0

    def register_time(self, hours: int):
        if not 0 < hours <= 24:
            raise ValueError()
        if hours > 8:
            self.salary += 8 * self.rate + (hours - 8) * self.rate * 2
        else:
            self.salary += hours * self.rate

    def pay_salary(self):
        tmp = self.salary
        self.salary = 0
        return tmp

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name}'

    # class attribute
    standard_rates = { #dict
        'field_employee': 20,
        'office_employee': 60,
        'manager_employee': 120,
    }

    @classmethod
    def office_employer(cls, first_name, last_name):
        # cls - w tejj zmiennej znajduje sie odwolanie do naszej klasy - Employee
        print(cls)
        print(cls.standard_rates)
        obiekt_employee = cls(first_name, last_name, cls.standard_rates['office_employee'])
        return obiekt_employee


# print( Employee.standard_rates )
# Employee.office_employer()

jan = Employee.office_employer('Jan', 'Nowak')
print(jan)
print(jan.rate)

print("="*60)
# ==== ABSTRAKCJA =====
# modul ABC (Abstract Base Class)
# żeby oznaczyć klasę jako abstrakcyjną, to ta klasa musi dziedziczyc po ABC
# te metody w klasie abstrakcyjnej, co do ktorych nie wiemy jak maja dzialac
# oznaczamy dekoratorem @abstractmethod

from abc import ABC, abstractmethod

class Zwierze(ABC):
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print(f'Jestem {self.imie}')

    @abstractmethod
    def wydaj_dzwiek(self):
        pass

class Pies(Zwierze):
    def wydaj_dzwiek(self):
        print('Hau hau')

class Kot(Zwierze):
    def wydaj_dzwiek(self):
        print("Miau miau")

class Ryba(Zwierze):
    def wydaj_dzwiek(self):
        print("Bul bul")


# zwierze = Zwierze('Lucyfer')
burek = Pies('Burek')
mruczek = Kot('Mruczek')
nemo = Ryba('Nemo')

# zwierze.przedstaw_sie()
# zwierze.wydaj_dzwiek()
burek.przedstaw_sie()
burek.wydaj_dzwiek()
mruczek.przedstaw_sie()
mruczek.wydaj_dzwiek()
nemo.przedstaw_sie()
nemo.wydaj_dzwiek()


print('='*60)

zwierzyniec = [burek, mruczek, nemo]

for zwierzak in zwierzyniec:
    zwierzak.przedstaw_sie()
    zwierzak.wydaj_dzwiek()





