from .transaction import Transaction

class Account:
    def __init__(self):
        self.balance = 0
        self.transactions = []
        self.statement = "date || credit || debit || balance"
        
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.__check_transaction_input(amount)
        self.__add_transaction(amount)
        self.balance += amount

    def withdraw(self, amount):
        self.__check_transaction_input(amount)
        self.__add_transaction(-amount)
        self.balance -= amount

    def get_statement(self):
        return self.statement

    def __check_transaction_input(self, amount):
        if (amount <= 0) or type(amount) != int:
            raise Exception("Input must be a positive integer")
        
    def __add_transaction(self, amount):
        transaction = Transaction(amount)
        self.transactions.append(transaction)
        print(self.__format_transaction(transaction))

    def __format_transaction(self, transaction):
        date = transaction.get_date()
        amount = transaction.get_amount()
        balance = self.get_balance()
        if amount > 0:
            return f'{date} || {amount} || || {balance}'
  