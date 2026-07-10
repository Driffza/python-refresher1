class BankAcc:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def transaction(self, amount):
        self.balance += amount
        return self.balance