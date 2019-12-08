from math import sqrt
import random

x = 0
y = 0

def losowanie_pozycji(x, y):
    x = random.randint(0,10)
    y = random.randint(0,10)
    return x, y

gracz_x, gracz_y = losowanie_pozycji(x, y)
print(gracz_x, gracz_y)


skarb_x, skarb_y = losowanie_pozycji(x, y)
print(skarb_x, skarb_y)

liczba_krokow = 0


poczatkowa_odleglosc = sqrt( (skarb_x-gracz_x)**2 + (skarb_y-gracz_y)**2 )

while True:

    odleglosc_przed_ruchem = sqrt( (skarb_x-gracz_x)**2 + (skarb_y-gracz_y)**2 )

    print(f"Odległość od skarbu to: {odleglosc_przed_ruchem:.1f}")

    print(f"Pozycja: ({gracz_x:2},{gracz_y:2})")
    kierunek = input("Podaj kierunek (w,s,a,d): ")

    if kierunek == 'w':
        gracz_y += 1
    elif kierunek == 's':
        gracz_y -= 1
    elif kierunek == 'a':
        gracz_x -= 1
    elif kierunek == 'd':
        gracz_x += 1
    else:
        print("Niepoprawny kierunek")
        continue # dalszy fragment kodu NIE zostanie wykonany

    liczba_krokow += 1

    if gracz_x == skarb_x and gracz_y == skarb_y:
        if liczba_krokow == 1:
            print(f"Brawo! Znalazles skarb w {liczba_krokow} kroku!")
        else:
            print(f"Brawo! Znalazles skarb w {liczba_krokow} krokach!")
        break

    # if 0 < gracz_x > 10 or 0 < gracz_y > 10:
    if gracz_x < 0 or gracz_x > 10 or gracz_y < 0 or gracz_y > 10:
        print("jestes poza plansza")
        break

    odleglosc_po_ruchu = sqrt( (skarb_x-gracz_x)**2 + (skarb_y-gracz_y)**2 )

    if poczatkowa_odleglosc < (2 * liczba_krokow):
        skarb_x, skarb_y = losowanie_pozycji(x, y)
        print(f"Wykonałes dwukrotnosc minimalnej liczby kroków, nowa pozycja skarbu to: {skarb_x}, {skarb_y}")

    if odleglosc_po_ruchu < odleglosc_przed_ruchem:
        print("Cieplo!")
    else:
        print("Zimno")
    print("---------------")
