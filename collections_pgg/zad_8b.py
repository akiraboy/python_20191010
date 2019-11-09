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

print( len(napis[ napis.index('<') + 1 : napis.index('>') ]) )