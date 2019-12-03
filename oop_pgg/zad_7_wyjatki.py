from oop_pgg.zad_7 import PremiumEmployee, Employee

try:
    imie = input('Podaj imie: ')
    nazwisko = input('Podaj nazwisko: ')
    stawka = float(input('Podaj stawke: '))
    emp = Employee(imie, nazwisko, stawka)

    czas = int(input('Podaj czas pracy: '))
    emp.register_time(czas)
    print('Twoja wyplata: ', emp.pay_salary())

except ValueError:
    print('Niepoprawny czas pracy! Musi być między 1 a 24')

