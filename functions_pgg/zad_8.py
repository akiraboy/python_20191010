"""
Zaimplementuj zestaw dekoratorów otaczających zwracany przez funkcję napis tagami HTML (pogrubienie, podkreślenie, przekreślenie):
Przykład użycia:
@bold
@italic
def foo(arg):
    return f'To jest {arg}'

@bold
def hello_world():
    return 'Hello world!'

Co oznacza, że bold
<strong>Hello world!</strong>

Co oznacza, że italic
<em>Hello world!</em>
"""


def bold(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return f'<strong>{wynik}</strong>'

    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return f'<em>{wynik}</em>'

    return wrapper

@italic
@bold
def hello_world():
    return 'Hello world!'

print( hello_world() )












