from abc import ABC, abstractmethod

class Discount(ABC):
    def __init__(self, amount):
        self._amount = amount

    @abstractmethod
    def calculate(self, total_price):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

class ValueDiscount(Discount):
    def calculate(self, total_price):
        return total_price - self._amount

    def __add__(self, other):
        return ValueDiscount(self._amount + other._amount)

class PercentageDiscount(Discount):
    def calculate(self, total_price):
        return total_price - total_price * self._amount / 100.0

    def __add__(self, other):
        return PercentageDiscount(self._amount + other._amount)




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
        self._discounts = []

    def add_discount(self, discount: Discount):
        self._discounts.append(discount)

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
        basket_total_price = sum( [ product.price * quantity for product, quantity in self._items.items() ] )

        sum_vd = ValueDiscount(0)
        sum_pd = PercentageDiscount(0)

        for discount in self._discounts:
            if isinstance(discount, ValueDiscount):
                sum_vd += discount
            elif isinstance(discount, PercentageDiscount):
                sum_pd += discount

        basket_total_price = sum_vd.calculate(basket_total_price)
        basket_total_price = sum_pd.calculate(basket_total_price)

        # if basket_total_price < 0:
        #     return 0
        # else:
        #     return basket_total_price

        return basket_total_price if basket_total_price >= 0 else 0

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

