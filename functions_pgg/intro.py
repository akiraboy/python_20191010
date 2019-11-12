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
print()
print()

# zasięg zmiennych i funkcjach zagniezdzonych

a = 10
def zewnetrzna():

    def wewnetrzna(): # wewnatrz funkcji zewnetrzna mam do dyspozycji funkcje wewnetrzna
        print(f"Ala ma kota, a={a}")
        return 5

    wynik = wewnetrzna()
    print(f'Wynik funkcji wewnetrzna = {wynik}')


zewnetrzna()

# argumenty domyślne
def opakowywacz(napis, start=">>", end="<<", dopisek=""):
    return start + napis + end + dopisek

print(opakowywacz("Ala ma kota"))
print(opakowywacz("Ala ma kota", "[", ']'))
print(opakowywacz("Ala ma kota", "["))
print(opakowywacz("Ala ma kota", end="{{", dopisek="!"))
print(opakowywacz(start="}}", dopisek="!", napis="Ala ma kota")) # jak nie zaczynam od argumentu pozycyjnego, to go trzeba wymienić z nazwy










