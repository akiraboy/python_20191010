from math import sqrt
import random
gracz_x = random.randint(0,10)
gracz_y = random.randint(0,10)

skarb_x = random.randint(0,10)
skarb_y = random.randint(0,10)

liczba_krokow = 0

while True:

    odleglosc_przed_ruchem = sqrt((skarb_x - gracz_x)**2 + (skarb_y - gracz_y)**2)

    print(f"Pozycja: ({gracz_x:2}, {gracz_y:2})")
    kierunek = input("Podaj kierunek (w,s,a,d):")

    if kierunek == 'w':
        gracz_y += 1
    elif kierunek == 's':
        gracz_y -= 1
    elif kierunek == 'a':
        gracz_x -= 1
    elif kierunek == 'd':
        gracz_x += 1
    else:
        print ("Niepoprawny kierunek")
        continue

    liczba_krokow += 1



    if gracz_x == skarb_x and gracz_y == skarb_y:
        if liczba_kroko == 1:
        print(f"Brawo! Znalazles skarb w {liczba_krokow} kroku!")
        print(f"Brawo! Znalazles skarb w {liczba_krokow} krokach!")
        break
    if  gracz_x < 0 or gracz_x >10 or gracz_y < 0 or gracz_y > 10:
        print("jestes poza plansza")
        break
    odleglosc_po_ruchu = sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)
        print("Ciepło")