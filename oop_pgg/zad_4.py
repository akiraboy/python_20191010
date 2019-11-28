"""
Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w określonej liczbie do koszyka. Zaimplementuj metodę obliczającą całkowitą wartość koszyka oraz wypisującą informację o zawartości koszyka. Dodanie dwa razy tego samego produktu do koszyka powinno stworzyć tylko jedną pozycję.
Przykład użycia:
basket = Basket()
product = Product(1, 'Woda', 10.00)
basket.add_product(product, 5)
basket.count_total_price()
50.0
basket.generate_report()
'Produkty w koszyku:\n
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00'
"""

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_info(self):
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN'

    def print_info(self):
        print(f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN')

    def __str__(self):
        return self.get_info()


class Basket:
    def __init__(self):
        # W słowniku klucz=product a wartość pod kluczem=quantity
        self._items = dict()

    def add_product(self, product: Product, quantity: int):
        # sprawdzenie czy to co jes w argumencie product jest obiektem klasy Product
        # i rzucenie wyjatku jak NIE jest
        if not isinstance(product, Product):
            raise TypeError('product has to be instance of Product')

        if quantity <= 0:
            raise ValueError('quantity has to be greater than 0')

        if product in self._items:
            # dodajemy quantity
            self._items[product] += quantity
        else:
            # wkladamy do slownik i przypisujemy quantity
            self._items[product] = quantity

    @property
    def is_empty(self) -> bool:
        # jak cos jest w self._items chce zwrocic False
        # jak self._items jest pusty to chcemy zwrócić True
        # bool({}) -> False
        # bool({'a':1}) -> True
        return not self._items

    def count_total_price(self):
        total_price = 0.0
        for product, quantity in self._items.items():
            total_price += product.price * quantity

        return total_price


def test_pusty_koszyk():
    koszyk = Basket()
    assert koszyk.is_empty is True
    assert koszyk.is_empty
    assert len(koszyk._items) == 0

    jablko = Product(1, 'Jablko', 1.2)
    koszyk.add_product(jablko, 5)
    assert koszyk.is_empty is False
    assert len(koszyk._items) == 1


def test_dodanie_jednego_produktu():
    koszyk = Basket()
    jablko = Product(1, 'Jablko', 1.2)
    koszyk.add_product(jablko, 5)
    assert len(koszyk._items) == 1
    assert koszyk._items[jablko] == 5

import pytest
def test_dodanie_nie_produktu():
    koszyk = Basket()
    with pytest.raises(TypeError):
        koszyk.add_product("ala ma kota", 5)

def test_dodanie_ujemnej_liczby_produktu():
    koszyk = Basket()
    jablko = Product(1, 'Jablko', 1.2)
    with pytest.raises(ValueError):
        koszyk.add_product(jablko, -1)

def test_dodanie_produktu_dwa_razy():
    koszyk = Basket()
    gruszka = Product(2, 'Gruszka', 2)
    koszyk.add_product(gruszka, 5)
    koszyk.add_product(gruszka, 3)

    assert len(koszyk._items) == 1
    assert koszyk._items[gruszka] == 8 # 5 + 3

    assert koszyk.count_total_price() == 16

    kalosze = Product(3, 'Kalosze', 10)
    koszyk.add_product(kalosze, 1)

    assert koszyk.count_total_price() == 26














