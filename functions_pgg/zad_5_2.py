"""
https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
"""

def fib(n):
    if n < 0:
        raise ValueError("n musi byc wieksze/rowne 0")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(5) == 5
    assert fib(15) == 610