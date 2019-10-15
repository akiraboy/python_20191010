miasto_a = input("Podaj miasto A: ")
miasto_b = input("Podaj miasto B: ")
dystans = int(input("Podaj dystans: "))
cena = float(input("Podaj cenę paliwa: "))
spalanie = float(input("Podaj spalanie na 100 km: "))

koszt = dystans / 100 * spalanie * cena

# https://www.python.org/dev/peps/pep-0498/#format-specifiers
# https://docs.python.org/3.4/library/string.html#formatspec

print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:_^10.2f} zł")
