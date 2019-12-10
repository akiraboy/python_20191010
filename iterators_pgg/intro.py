# ==== ITERATORY ====
import random

lista = [10, 20, 30, 40, 50]

iterator = iter(lista)
print(iterator)

print( next(iterator) )
print( next(iterator) )
print( next(iterator) )
print( next(iterator) )
print( next(iterator) )
# print( next(iterator) ) # wyjątek StopIteration kiedy próbujemy pobrać coś poza zasięgiem

print('='*60)

class Losowacz:
    def __init__(self, ile_liczb, od, do):
        self.ile_liczb = ile_liczb
        self.od = od
        self.do = do

    def __iter__(self):
        print("uruchamiam metodę __iter__")
        self.ile_wylosowano = 0
        return self

    def __next__(self):
        print("uruchamiam metodę __next__")
        if self.ile_wylosowano >= self.ile_liczb:
            raise StopIteration

        self.ile_wylosowano += 1
        return random.randint(self.od, self.do)


moj_losowacz = Losowacz(5, 0, 10)

print(moj_losowacz)

iterator_losowacza = iter(moj_losowacz)
print(iterator_losowacza)

try:
    print( next(iterator_losowacza) )
    print( next(iterator_losowacza) )
    print( next(iterator_losowacza) )
    print( next(iterator_losowacza) )
    print( next(iterator_losowacza) )
    print( next(iterator_losowacza) )
except StopIteration:
    print("skonczyl sie iterator")

print('='*60)

# tworze nowy obiekt losowacza
# przekazuję do pętli for
# python na tym obiekcie uruchamia __iter__, dostaje iterator
# i zaczyna iterować, czyli odpala metodę __next__
# jak for dostanie po oczach StopIteration, to po prostu konczy iterowanie i przechodzimy do kolejnej linijki kodu
# nie muszę opakowywać fora w żadnego try/excepta...
for liczba in Losowacz(10, 0, 100):
    print(liczba)

print('='*60)

lista = list(Losowacz(15, 0, 100))
print(lista)




