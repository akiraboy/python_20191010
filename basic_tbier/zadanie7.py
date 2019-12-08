liczba = int(input("Podaj liczbe: "))
wynik = (liczba % 2 != 0 and liczba % 3 == 0 and liczba > 10) or liczba == 7
wynik = (liczba % 2 == 1 and liczba % 3 == 0 and liczba > 10) or liczba == 7
wynik = (liczba % 2 > 0 and liczba % 3 == 0 and liczba > 10) or liczba == 7
wynik = (liczba % 2 >= 1 and liczba % 3 == 0 and liczba > 10) or liczba == 7

print(f"Wynik: {wynik}")
