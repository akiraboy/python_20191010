from random import randint
x = randint(0, 99)
y = randint(0, 99)

suma = x + y

while True:

    podaj_wynik = int(input(f"Podaj wynik dla {x} + {y}: "))

    if suma != podaj_wynik:
        podaj_wynik = int(input(f"Podałeś niepoprawny wynik, podaj5 sume dla {x} + {y}: "))
    elif suma == podaj_wynik:
        print('Podałeś własciwy wynik dla ', suma)
        break

