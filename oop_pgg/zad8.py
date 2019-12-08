class CashMachineAvailebileError(Exception):
    pass

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
