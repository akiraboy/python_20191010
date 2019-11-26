"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu pracy
oraz wypłacanie pensji na podstawie zadanej stawki godzinowej.
Jeżeli pracownik będzie pracował więcej niż 8 godzin
(podczas pojedynczej rejestracji czasu) to kolejne godziny
policz jako nadgodziny (z podwójną stawką godzinową).

Przykład użycia:
employee = Employee('Jan', 'Nowak', 100.0) >>> employee.register_time(5)
employee.pay_salary()
500.0
employee.pay_salary() 0.0
employee.register_time(10)
employee.pay_salary() 1200.0

DODAJEMY ATRYBUTY KLASOWE
"""

class Employee:
    WORK_DAY = 8
    OVERTIME_MUL = 2

    def __init__(self, first_name: str, last_name: str, rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.salary = 0

    def register_time(self, hours: int):
        # if hours < 0 or hours > 24:
        #     raise ValueError()
        if not 0 < hours <= 24:
            raise ValueError()
        if hours > 8:
            self.salary += Employee.WORK_DAY * self.rate \
                           + (hours - Employee.WORK_DAY) \
                           * self.rate * Employee.OVERTIME_MUL

        else:
            self.salary += hours * self.rate

    def pay_salary(self):
        tmp = self.salary
        self.salary = 0
        return tmp

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name}'


def test_create():
    employee = Employee('Jan', 'Kowalski', 100.0)
    assert str(employee) == 'Employee Jan Kowalski'

def test_zwykle_godziny():
    employee = Employee('Jan', 'Kowalski', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500

def test_dwa_razy_wyplata():
    employee = Employee('Jan', 'Kowalski', 100.0)
    employee.register_time(5)
    wyplata1 = employee.pay_salary()
    wyplata2 = employee.pay_salary()
    assert wyplata1 == 500
    assert wyplata2 == 0

def test_nadgodziny():
    employee = Employee('Jan', 'Kowalski', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 1200

def test_kilka_dni_pracy():
    employee = Employee('Jan', 'Kowalski', 100.0)
    employee.register_time(5)
    employee.register_time(10)
    employee.register_time(8)
    assert employee.pay_salary() == (5*100 + 8*100 + 2*200 + 8*100)

import pytest
def test_spryciarz():
    employee = Employee('Jan', 'Kowalski', 100.0)
    with pytest.raises(ValueError):
        employee.register_time(-5)

    with pytest.raises(ValueError):
        employee.register_time(30)




