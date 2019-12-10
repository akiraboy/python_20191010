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
        self._items = dict()

    def add_product(self, product: Product, quantity: int = 1):
        if not isinstance(product, Product):
            raise TypeError('product has to be instance of Product')

        if quantity <= 0:
            raise ValueError('quantity has to be greater than 0')

        if product in self._items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity

    @property
    def is_empty(self) -> bool:
        return not self._items

    def count_total_price(self):
        return sum( [ product.price * quantity for product, quantity in self._items.items() ] )

    def generate_report(self):
        print("Produkty w koszyku:")
        for product, quantity in self._items.items():
            print(f'{product.name} ({product.id}), cena: {product.price:.2f} x {quantity}')
        print(f'W sumie: {self.count_total_price():.2f}')

    @classmethod
    def with_products(cls, products):
        basket = cls()
        for product in products:
            basket.add_product(product)
        return basket

def test_with_products():
    produkty = [
        Product(1, 'Jablko', 4),
        # Product(1, 'Jablko', 4),
        Product(2, 'Gruszka', 12),
    ]

    koszyk = Basket.with_products(produkty)

    assert koszyk.count_total_price() == 16
    assert len(koszyk._items) == 2

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

