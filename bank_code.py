class BankAcc:
    def __init__(self, name, initial_balance=0):
        self.name = str(name)
        self.balance = float(initial_balance)
        """ Gives name, number, and balance.

        """

    def transaction(self, amount):
        self.balance += amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.transaction

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        print(self.balance)