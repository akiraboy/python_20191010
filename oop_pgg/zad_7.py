"""
Zaimplementuj klasę PremiumEmployee, która będzie klasą pochodną Employee.
Klasa ta powinna umożliwiać dodatkowo przyznawanie bonusów pracownikowi.
employee = PremiumEmployee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.give_bonus(1000.0)
employee.pay_salary()
1500.0
"""

from oop_pgg.zad_2_1 import Employee

class PremiumEmployee(Employee):
    def __init__(self, first_name, last_name, rate):
        super().__init__(first_name, last_name, rate)
        self._bonus = 0

    def give_bonus(self, bonus):
        self._bonus += bonus

    def pay_salary(self):
        salary = super().pay_salary()
        salary += self._bonus
        self._bonus = 0
        return salary


def test_czy_dziala_dziedziczenie():
    jas = PremiumEmployee('Jan', 'Kowalski', 40)
    jas.register_time(6)
    assert jas.pay_salary() == 240

def test_daj_premie():
    jas = PremiumEmployee('Jan', 'Kowalski', 40)
    jas.register_time(6)
    jas.give_bonus(100)
    assert jas.pay_salary() == 340

def test_premia_tylko_raz():
    jas = PremiumEmployee('Jan', 'Kowalski', 40)
    jas.register_time(6)
    jas.give_bonus(100)
    assert jas.pay_salary() == 340
    jas.register_time(6)
    assert jas.pay_salary() == 240





