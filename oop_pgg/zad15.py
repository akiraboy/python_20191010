class ElectricCar:
    def __init__(self, max_range: int):
        if max_range < 0:
            raise ValueError('Range cnnot be smaller than 0')
        self.max_range = max_range
        self.battery_level = self.max_range

    def charge(self):
        self.battery_level = self.max_range

    def drive(self, distance_to_drive: int):
        if distance_to_drive <= self.battery_level:
            self.battery_level -= distance_to_drive
            return distance_to_drive
        else:
            tmp = self.battery_level
            self.battery_level = 0
            return tmp


    def __str__(self):
        return f'Availabel range{self.battery_level}'

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
