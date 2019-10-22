"""
Stwórz tuplę zawierającą 10 różnych liczb całkowitych. Korzystając z operatora dostępu oraz wycinania pobierz:
- drugi element
- przedostatni element
- elementy od trzeciego do siódmego (włącznie) 􏰀 co trzeci element
- co drugi element licząc od końca
"""
# i  0 1 2 3 4 5 6 7 8 9
x = (1,2,3,4,5,6,7,8,9,10)

print(x[1]) # drugi element
print(x[-2]) # przedostatni element
print(x[2:7:3]) # od 3 do 7 (włącznie), ale co trzeci element
print(x[::-2]) # co drugi od końca