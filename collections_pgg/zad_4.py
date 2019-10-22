"""
wypisac liczby od 0 do 100,
ale takie co są podzielne przez 3 lub 5
Wypisz także jak dużo takich liczb wystąpiło w tym przedziale.
"""
ile = 0
for x in range(0, 101):
    if x % 3 == 0 or x % 5 == 0:
        print(x)
        ile += 1

print(f"Wystapilo {ile} takich liczb")

i = 0
ile = 0
while i <= 100:
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        ile += 1

    i += 1

print(f"Wystapilo {ile} takich liczb")