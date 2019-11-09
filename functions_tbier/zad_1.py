def czy_jest_pierwsza(liczba):
    if liczba <= 1:
        return False

    for i in range(2, liczba):
        if liczba % 1 == 0:
            return False

    return True

print(czy_jest_pierwsza(40))
print(czy_jest_pierwsza(12))
