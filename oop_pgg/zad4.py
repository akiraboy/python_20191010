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
    def add_product(self, product: Product, quantity: int):
        if not isinstance(product, Product):
            raise TypeError('product has to be instance of Product')

        if quantity <= 0:
            raise ValueError('quantity has to be greater than 0')

        if product in self._items:
            self._items[product] += quantity

        else:
            self._items[product] = quantity
    @property
    def is_empty(self):
        return not self._items

    def count_total_price(self):
       # total_price = 0.0
        #for product, quantity in self._items.items():
         #   total_price += product.price * quantity

        #return total_price

        return sum([ product.price * quantity for product, quantity in self._items.items() ])
    def generate_report(self):
        print('Produkt w koszyku:')
        for product, quantity in self._items.items():
            print(f'{product.name} ({product.id}), cena: {product.price: .2f} x {quantity}')
        print(f'W sumie: {self.count_total_price(): .2f}')


def test_pusty_koszyk():
    koszyk = Basket()
    assert koszyk.is_empty is True
    assert koszyk.is_empty
    jablko = Product(1, 'Jablko', 1.2)
    assert koszyk.is_empty is False
    assert len(koszyk._items) == 1

def test_dodanie_jednego_produktu():
    koszyk = Basket()
    jablko = Product(1, 'Jablko', 1.2)
    koszyk.add_product(jablko, 5)
    assert len(koszyk._items) == 1
    assert koszyk._items[jablko] == 5





def test_dodanie_produktu_dwa_razy():
    pass



