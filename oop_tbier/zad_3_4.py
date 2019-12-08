'''
Napisz dekorator `crazy_case`, który co drugą literę w słowie będzie zamieniał na dużą.
```python
@crazy_case
def powiedz_ala():
	return ‘Ala ma kota’
print(powiedz_ala()) # aLa mA KoTa
```
'''

def crazy_case(func):
	def wrapper(*args, **kwargs):
		wynik = func(*args, **kwargs)
		tekst = list(wynik)

		print(tekst)

		tekst[1::2] = [n.upper() for n in tekst[1::2]]
		wynik = ''.join(tekst)

		print(wynik)

		return wynik

	return wrapper


@crazy_case
def powiedz_ala():
	return 'Ala ma kota'

print(powiedz_ala())
