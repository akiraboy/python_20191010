# To jest komentarz
# kolejna linijka

# TYPY DANYCH
# str - string
print("Hello world!")
print('Hello world!')

# int
print(10)
print(-8)
print(123)

# float
print(3.5)
print(-2.8)
print(5.0)
print(10.0)
print(10.) # 10.0
print(.5)

import sys
print(sys.float_info)

# bool
print(True)
print(False)

# wartość pusta
# None - w innych językach to jest null
# wartość, która oznacza brak wartości

print(None)

# Operatory matematyczne
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 % 3)
print(10 // 3) # dzielenie całkowitoliczbowe
print(10 ** 3) # potegowanie

# Definiowanie napisów
print("Ala ma kota")
print('Ala ma kota')
print('Ala ma "kota" ')
print("Ala ma 'kota' ")
print('Ala ma \'kota\' ') # eskejpowanie
print("Ala ma \"kota\" ")
print("Ala "
      "ma "
      "kota")
print("""
Ala
ma 
kota
""")

print("Ala " + "ma kota") # konkatenacja
# print("Ala" + 10) # to sie nie uruchomi, bo nie można łączyć str z int (czy innymi typami)
print("Ala" + str(10)) # str(10) przerabia typ int na str
print("-" * 30)










