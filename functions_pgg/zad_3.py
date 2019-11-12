"""
Napisz funkcję obliczającą liczbę znaków w zadanym napisie pomiędzy zadanymi znakami. Znaki, pomiędzy którymi ma odbywać się zliczanie, powinny być argumentami z wartościami domyślnymi - odpowiednio < i >. Nawiasy mogą być zagnieżdżone i mogą wystąpić wiele razy. Znaki pomiędzy zagnieżdżonymi nawiasami liczone są zgodnie z poziomem zagnieżdżenia.
Przykład użycia:
policz_znaki('ala ma <kota> a kot ma ale')
4
policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') 18
policz_znaki('a <a<a<a>>>')
6
"""

def policz_znaki(napis:str, start='<', end='>'):
    poziom = 0
    liczba_znakow = 0

    for znak in napis:
        if znak == start:
            poziom += 1
        elif znak == end:
            poziom -= 1
        elif poziom > 0:
            liczba_znakow += poziom


    return liczba_znakow













