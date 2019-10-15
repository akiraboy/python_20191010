liczba_1 = int(input("Podaj pierwszą liczbę: "))
liczba_2 = int(input("Podaj drugą liczbę: "))
operacja = input("Podaj operację (+, -, *, /): ")

if operacja == "+":
    wynik = liczba_1 + liczba_2
elif operacja == "-":
    wynik = liczba_1 - liczba_2
elif operacja == "*":
    wynik = liczba_1 * liczba_2
elif operacja == "/":
    wynik = liczba_1 / liczba_2
else:
    wynik = None


if wynik is None:
    print("Niepoprawne dane")
else:
    print(f"Wynik = {wynik}")
