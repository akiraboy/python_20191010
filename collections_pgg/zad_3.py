lista = [1, 5, 10, -1, 2, -3, 0, 8, 100]

liczb_dodatnich = 0
liczb_ujemnych = 0

for element in lista:
    if element < 0:
        liczb_ujemnych += 1
    elif element > 0:
        liczb_dodatnich += 1

print(f"Dodatnich = {liczb_dodatnich}, ujemnych = {liczb_ujemnych}")