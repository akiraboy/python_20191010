"""
Zaimplementuj dekorator wypisujący wywołanie danej funkcji
(nazwa i argumenty) oraz czas jej wykonania.
Przykład użycia:
@log
def foo(arg):
return f'To jest {arg}'
"""

import time

def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = func(*args, **kwargs)
        stop = time.time()
        czas = stop - start
        print(f'Czas wykonania funkcji {func.__name__} to {czas} sekund')

        return wynik

    return wrapper

@log
def silnia(n):
    if n < 0:
        raise ValueError('n musi być większe/równe 0')
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik

print( silnia(50000) )