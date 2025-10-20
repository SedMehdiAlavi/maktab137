class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def display_balance(self):
        return self.balance


class Bank():
    def __init__(self, name: str):
        self.name = name
        self.accounts = []

    def create_account(self, account_number: str, initial_deposit: float):
        for account in self.accounts:
            if account.account_number == account_number:
                print('Account number already exists')
                return
        account = BankAccount(account_number, initial_deposit)
        self.accounts.append(account)

    def close_account(self, account_number: str):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)

    def update_account(self, account_number: str, amount: float):
        for account in self.accounts:
            if account.account_number == account_number:
                if amount > 0:
                    account.deposit(amount)
                elif amount < 0 and account.balance > -amount:
                    account.withdraw(-amount)

    def display_accounts(self):
        print(f'---{self.name}---')
        for account in self.accounts:
            print(account.account_number,':', account.display_balance())


melli = Bank('Melli')
saderat = Bank('Saderat')

melli.create_account('123-789', 1500)
melli.create_account('159-753', 2000)
saderat.create_account('147-963', 1500)
saderat.create_account('158-753', 2000)
melli.close_account('123-789')
saderat.display_accounts()
melli.display_accounts()
saderat.update_account('158-753', -450)
saderat.display_accounts()
