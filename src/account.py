try:
    from .transaction import Transaction
except ImportError:
    from transaction import Transaction

class Account:
    def __init__(self):
        self.balance = 0
        self.activity_log = []
        
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.__check_transaction_input(amount)
        self.balance += amount
        self.__add_transaction(amount)

    def withdraw(self, amount):
        self.__check_transaction_input(amount)
        self.balance -= amount
        self.__add_transaction(-amount)

    def get_statement(self):
        return self.statement
    

    # Private
    def __check_transaction_input(self, amount):
        if (amount <= 0) or type(amount) != int:
            raise Exception("Input must be a positive integer")
        
    def __add_transaction(self, amount):
        transaction = Transaction(amount)
        activity = {
            "transaction": transaction,
            "balance": self.balance
            }
        self.activity_log.append(activity)
