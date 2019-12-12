"""
Zaimplementuj iterator zwracający jedynie samogłoski
z zadanego ciągu znaków:
Przykładowe użycie:
for char in Vowels('ala ma kota a kot ma ale'): ...
"""

class Vowels:
    def __init__(self, text):
        self._text = text
        self._vowels = 'aieouy'

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        while self._index < len(self._text):
            tmp_index = self._index # 1 next -> tmp_index = 0
            self._index += 1 # 1 next -> self._index = 1
            if self._text[ tmp_index ].lower() in self._vowels:
                return self._text[ tmp_index ]

        raise StopIteration



for litera in Vowels("Ala ma kota a kot ma kompilator"):
    print(litera)

lista_samoglosek = list(Vowels("Ala ma kota a kot ma kompilator"))
print(lista_samoglosek)

print('='*60)

class CustomVowels(Vowels):
    def __init__(self, text, vowels):
        super().__init__(text)
        self._vowels = vowels

for litera in CustomVowels("Ala ma kota i zażółć gęślą jaźń", "aeiuoyąóę"):
    print(litera)

lista_costom_samoglosek = list(CustomVowels("Ala ma kota i zażółć gęślą jaźń", "aeiuoyąóę"))
print(lista_costom_samoglosek)




