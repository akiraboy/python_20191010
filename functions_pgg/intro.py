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

