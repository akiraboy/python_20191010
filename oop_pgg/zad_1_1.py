# TDD

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


def test_create():
    woda = Product(1, "Woda", 10.99)

def test_create_and_access():
    woda = Product(1, "Woda", 10.99)
    assert woda.id == 1
    assert woda.name == "Woda"
    assert woda.price == 10.99

def test_get_info():
    woda = Product(1, "Woda", 10.99)
    info = woda.get_info()
    assert info == 'Produkt "Woda", id: 1, cena: 10.99 PLN'

def test_print_info(capsys):
    woda = Product(1, "Woda", 10.99)
    woda.print_info() # to powinno na konsolę printem coś wypluć

    out, err = capsys.readouterr() # w out siedzi string, który jest tym co poleciało na standardowe wyjście
    assert out == 'Produkt "Woda", id: 1, cena: 10.99 PLN\n'

def test_str():
    woda = Product(1, "Woda", 10.99)
    assert str(woda) == 'Produkt "Woda", id: 1, cena: 10.99 PLN'