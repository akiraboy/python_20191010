LICZBA_DNI_TYGODNIA = 7
numer_dnia = 1
suma = 0

while numer_dnia <= LICZBA_DNI_TYGODNIA:
    suma += int(input(f"Podaj temperaturę z dnia {numer_dnia}: "))
    numer_dnia += 1

srednia = suma / LICZBA_DNI_TYGODNIA

print(f"Srednia temperatur to {suma / LICZBA_DNI_TYGODNIA}")
print(f"Srednia temperatur to {srednia}")

