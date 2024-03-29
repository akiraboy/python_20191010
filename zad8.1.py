
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
            # dodajemy quantity
            self._items[product] += quantity
        else:
            # wkladamy do slownik i przypisujemy quantity
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

    @staticmethod
    def with_product(products):
        basket = Basket()
        for product in products:
            basket.add_product(product)

        return basket

def tets_with_products():
    produkty =[
        Product(1, 'jablko', 4),
        Product2(2, 'gruszka', 12),
    ]

    koszyk = Basket.with_products(produkty)

    assert koszyk.count_total_price() == 16