min = None
max = None

while True:
     dane_wejsciowe = input("Podaj liczbe lub KONIEC: ")
     if dane_wejsciowe.upper() == "KONIEC":
         break

     liczba = int(dane_wejsciowe)

     if max is None or liczba > max:
         max = liczba
     if min is None or liczba < min:
         min = liczba

if min is None or max is None:
    print("nie wprowadiłeś żadnej liczby")
else:
    print(f"Max = {max} i Min={min}")