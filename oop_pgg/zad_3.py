"""
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego.
Klasa powinna umożliwiać pokonanie zadanego dystansu, który nie może przekroczyć
maksymalnego zasięgu zdefiniowanego dla samochodu.
Samochód powinien mieć także możliwość naładowania baterii.
car = ElectricCar(100)
car.drive(70) -> 70
car.drive(50) -> 30
car.drive(50) -> 0
car.charge()
car.drive(50) -> 50
"""

class ElectricCar:
    def __init__(self, max_range: int):
        # self.max_range = max_range if max_range > 0 else 0

        if max_range < 0:
            raise ValueError('Range cannot be smaller than 0.')
        self.max_range = max_range
        self.battery_level = self.max_range

    def charge(self):
        self.battery_level = self.max_range

    def drive(self, distance_to_drive: int):
        # podejscie 1
        # if distance_to_drive <= self.battery_level:
        #     self.battery_level -= distance_to_drive
        #     return distance_to_drive
        # else:
        #     tmp = self.battery_level
        #     self.battery_level = 0
        #     return tmp

        # podejscie 2
        real_distance = min(distance_to_drive, self.battery_level)
        self.battery_level -= real_distance
        return real_distance

    def __str__(self):
        return f'Available range {self.battery_level}'

import pytest
def test_ujemny():
    with pytest.raises(ValueError):
        tesla = ElectricCar(-10)

def test_max_zasieg():
    tesla = ElectricCar(100)
    assert tesla.drive(100) == 100

def test_poza_zasiegiem():
    tesla = ElectricCar(100)
    assert tesla.drive(120) == 100

def test_ladowanie():
    tesla = ElectricCar(100)
    assert tesla.drive(70) == 70
    tesla.charge()
    assert tesla.drive(80) == 80

def test_kilka_tras():
    tesla = ElectricCar(100)
    assert tesla.drive(50) == 50
    assert tesla.drive(40) == 40
    assert tesla.drive(20) == 10







