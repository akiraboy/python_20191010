class CashMachine:
    NOMINALS = [500, 200, 100, 50, 20, 10] # class attribute

    def __init__(self):
        self._banknotes = []

    def put_money(self, banknotes):
        valid_banknotes = self._filter_valid_banknotes(banknotes)
        self._banknotes.extend(valid_banknotes)

    def _filter_valid_banknotes(self, banknotes):
        valid_banknotes = [el for el in banknotes if el in CashMachine.NOMINALS]
        return valid_banknotes

    @property
    def is_available(self):
        return bool(self._banknotes)

    def withdraw_money(self, amount):
        if not self.is_available:
            raise ValueError('Cash machine is not available')
        if amount % min(self._banknotes) != 0:
            raise ValueError('Unable to withdraw money.')

        # sortujemy banknoty
        self._banknotes.sort(reverse=True)

        withdrawal = []
        for banknote in self._banknotes:
            if banknote <= amount:
                withdrawal.append(banknote)
                amount -= banknote

        if amount == 0:
            for banknote in withdrawal:
                self._banknotes.remove(banknote)
            return withdrawal
        else:
            return []


import pytest
def test_availability():
    cash_machine = CashMachine()
    assert not cash_machine.is_available


def test_put_money_if_available():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available

def test_put_no_money():
    cm = CashMachine()
    cm.put_money([])
    assert [] == cm._banknotes

def test_put_money_with_rubbish():
    cm = CashMachine()
    cm.put_money(['ala',25,0,'0','200'])
    assert [] == cm._banknotes

def test_put_money():
    cm = CashMachine()
    cm.put_money([200,50,100,50])
    copy = cm._banknotes.copy()
    copy.sort()
    assert [50,50,100,200] == copy

def test_withdraw_money_from_empty():
    cash_machine = CashMachine()
    with pytest.raises(ValueError):
        cash_machine.withdraw_money(150)

def test_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]

def test_withdraw_money_impossible():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 50])
    assert cash_machine.withdraw_money(100) == []

def test_withdraw_money_2times_impossible():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]
    with pytest.raises(ValueError):
        cash_machine.withdraw_money(150)

def test_withdraw_money_2times_possible():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50, 50])
    cash_machine.withdraw_money(150)
    assert cash_machine.withdraw_money(150) == [100, 50]

def test_withdraw_money_all_banknotes():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(450) == [200, 100, 100, 50]

def test_withdraw_money_put_back_if_impossible():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    cash_machine.withdraw_money(550)
    assert cash_machine.withdraw_money(450) == [200, 100, 100, 50]

def test_amount_unable_to_withdraw():
    cm = CashMachine()
    cm.put_money([200, 100, 100, 50, 50, 50])
    with pytest.raises(ValueError):
        cm.withdraw_money(165)

