x = int(input("Podaj wysokosc i szerokosc w przedziale od 0 do 100: "))
y = int(input("Podaj wysokosc i szerokosc w przedziale od 0 do 100: "))
#Lewa strona.
if (0 <= x <= 10) and (y <= 10):
    print("Jestes w LDR")
elif 0 <= x <= 10 and (10 < y <= 90):
    print("Jestes w Lewym boku")
elif 0 <= x <= 10 and (90 < y <= 100):
    print("Jestes w LGR")
# Srodek
elif (10 <= x <= 90) and (y <= 10):
    print("Jestes w dolnym boku")
elif (10 <= x <= 90) and (10 < y <= 90):
    print("Jestes w srodku")
elif (10 <= x <= 90) and (90 < y <= 100):
    print("Jestes na gorze")
#Prawa strona
elif (90 < x <= 100) and (y <= 10):
    print("Jestes w PDR")
elif (90 < x <= 100) and (10 < y <= 90):
    print("jeste w prawym boku")
elif (90 < x <= 100) and (90 < y <=100):
    print("Jeste w PGR")
# elif (x or y) > 100:
#     print("Jestes poza polem")
else:
    print("Jestes poza planszą!")