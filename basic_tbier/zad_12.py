i = 1

# while i <= 100:
#     i += 1
#     print(i)

numer_dnia = 1
suma = 0
while numer_dnia < 8:
    suma += int(input(f"Podaj temperature z dnia {numer_dnia}: "))
    numer_dnia += 1

#3srednia = suma / 7

print(f"Srednia temperatur to {suma /7}")

