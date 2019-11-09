napis = input("POdaj ciag znaków: ")

samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

ile_samoglosek = 0

for znak in napis:
    if znak in samogloski:
        ile_samoglosek += 1

print(f"Znaleziono samoglosek: {ile_samoglosek}")