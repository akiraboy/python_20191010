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

