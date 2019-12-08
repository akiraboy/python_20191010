x, y, z = int(input("Podaj długosz, szerokosc, wysokosc: ")).split()

wynik = x * y * z > 1000
print(f"Czy jest wieksze od 1 litra? -> {wynik}")