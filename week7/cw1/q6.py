class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def __add__(self, other):
        return BankAccount(self.owner, self.__balance + other.__balance)

    def __eq__(self, other):
        return self.owner == other.owner

    def __str__(self):
        return f'owner: {self.owner}, balance: {self.__balance}'

    def __del__(self):
        print('Account Closed!')

acount1 = BankAccount('Mehdi', 1000)
account2 = BankAccount('Parsa', 1500)
print(acount1 + account2)