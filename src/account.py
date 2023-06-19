# I was unable to get the imports to work for both
# the tests and the REPL. So this try catch was the
# only solution which worked for me
try:
    from .transaction import Transaction
except ImportError:
    from transaction import Transaction

class Account:
    def __init__(self):
        self.balance = 0
        self.activity_log = []
    
    def deposit(self, amount):
        self.__check_transaction_input(amount)
        self.balance += amount
        self.__add_transaction(amount)

    def withdraw(self, amount):
        self.__check_transaction_input(amount)
        self.balance -= amount
        self.__add_transaction(-amount)
    
    # private
    def __check_transaction_input(self, amount):
        if amount <= 0:
            raise Exception("Input must be positive")
        
    def __add_transaction(self, amount):
        transaction = Transaction(amount)
        activity = {
            "transaction": transaction,
            "balance": self.balance
            }
        self.activity_log.append(activity)
