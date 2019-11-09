napis = input("Podaj napis: ")

liczba_znakow = 0
czy_zliczac = False

for znak in napis:
    if znak == '<':
        czy_zliczac = True
    elif znak == '>':
        czy_zliczac = False
    elif czy_zliczac is True:
        liczba_znakow += 1
print(f"Liczba zliczonych znaków = {liczba_znakow}")