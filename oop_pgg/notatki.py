# el for el in banknotes if el in CashMachine.NOMINALS

banknotes = [100, 200, 'a']
valid_banknotes = []
for el in banknotes:
    if el in [500, 200, 100, 50, 20, 10]:
        valid_banknotes.append(el)

print(valid_banknotes)

#

from oop_pgg.zad_4 import *

p1 = Product(1, 'jablko', 1)
p2 = Product(1, 'jablko', 1)

print(p1.__hash__())
print(p2.__hash__())
