class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):

        if not isinstance(amount, int):
            raise TypeError

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance = amount

    def withdraw(self, amount):

        if not isinstance(amount, int):
            raise TypeError

        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
