class BankAccount:
    def __init__(self, name: str, balance = 0):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value: int):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance += value

    @classmethod
    def from_string(cls, data):
        data = data.split(",")
        return BankAccount(data[0], int(data[1]))


parsa = BankAccount("Parsa")
print(parsa.balance)
parsa.balance = 200
print(parsa.balance)
BankAccount.from_string("SedMehdi, 380")


