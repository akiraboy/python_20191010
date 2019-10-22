liczby = [] # tworzy pustą listę
liczby = list() # tworzy pustą listę

while len(liczby) < 10:
    liczby.append(int(input("Podaj liczbę: ")))

print(liczby)
srednia = sum(liczby) / len(liczby)
print(f"Srednia z wprowadzonych elementow: {srednia}")
