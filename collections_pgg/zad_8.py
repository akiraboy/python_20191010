"""
Napisz program zliczający liczbę znaków w podanym przez użytkownika
napisie pomiędzy nawiasami <>. Nawiasy mogę wystąpić tylko raz.
Ala ma <kota>, a kot ma Alę
4
"""

napis = input("Podaj napis: ")

if napis.count('<') != 1 or napis.count('>') != 1:
    print("Nieprawidlowa liczba nawiasow!")
    exit()

liczba_znakow = 0
czy_zliczac = False

for znak in napis:
    if znak == '<':
        czy_zliczac = True
    elif znak == '>':
        czy_zliczac = False
    # elif czy_zliczac == True:
    # elif czy_zliczac is True:
    elif czy_zliczac:
        liczba_znakow += 1

print(f"Liczba zliczonych znakow = {liczba_znakow}")
