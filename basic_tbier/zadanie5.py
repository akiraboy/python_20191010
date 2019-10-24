miasto_a, miasto_b = input("Podaj miasto A i miasto B: ").split()

dystans = int(input("Podaj dystans: "))
print(type(dystans))
cena = float(input("Cena paliwa: "))
spalanie = float(input("Podaj spalanie na 100 km: "))

koszt = dystans / 100 * spalanie * cena
# string format specification
print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:_^10.2f} zł")

