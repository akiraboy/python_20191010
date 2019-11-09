"""
Napisz program wypisujący na konsolę tabliczkę mnożenia dla liczb od 0 do 9
w postaci tabelki.
"""
print(" "*3, end="")
for i in range(10):
    print(f"{i:2}", end=" ")

print()
print()

for i in range(10):
    print(f"{i:<3}", end="")
    for j in range(10):
        print(f"{i*j:2}", end=" ") # format specifier
    print()