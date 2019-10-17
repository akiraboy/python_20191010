x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

# if x >= 0 and x <= 10:
#     pass
# if 0 <= x and x <= 10:
#     pass

# if 90 <= x <= 100 and 90 <= y <= 100:
#     print("PGR")
# ...

if 0 <= x <= 10:
    if 0 <= y <= 10:
        print("lewy dolny rog")
    elif 10 < y < 90:
        print("lewy bok")
    elif 90 <= y <= 100:
        print("lewy gorny rog")
    else:
        print("Jestes poza plansza")
elif 10 < x < 90:
    if 0 <= y <= 10:
        print("dolny bok")
    elif 10 < y < 90:
        print("srodek")
    elif 90 <= y <= 100:
        print("gorny bok")
    else:
        print("Jestes poza plansza")
elif 90 <= x <= 100:
    if 0 <= y <= 10:
        print("prawy dolny rog")
    elif 10 < y < 90:
        print("prawy bok")
    elif 90 <= y <= 100:
        print("prawy gorny rog")
    else:
        print("Jestes poza plansza")
else:
    print("Jestes poza plansza")