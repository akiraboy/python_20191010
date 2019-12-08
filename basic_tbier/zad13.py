numer_dnia = 1
suma = 0

while numer_dnia <= 7:
    suma += int(input(f"Podaj temp z dnia {numer_dnia}:"))
    numer_dnia += 1

srednia = suma / 7

print(f"Srednia temp to {suma / 7}")
print(f"Srednia temp to {srednia}")
