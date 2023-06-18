class Account:
    def __init__(self):
        self.balance = 0
        
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.__check_transaction_input(amount)
        self.balance += amount

    def withdraw(self, amount):
        self.__check_transaction_input(amount)
        self.balance -= amount


    def __check_transaction_input(self, amount):
        if (amount <= 0) or type(amount) != int:
            raise Exception("Input must be a positive integer")
  