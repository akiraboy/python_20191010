"""
Napisz program zliczający liczbę wystąpień samogłosek
(a, e, i, o, u, y) w podanym przez użytkownika napisie.
"""

napis = input("Podaj napis: ") # .lower()
# samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
samogloski = "aeiouy"

for samogloska in samogloski:
    print(f"znaleziono {samogloska} = {napis.count(samogloska)}")