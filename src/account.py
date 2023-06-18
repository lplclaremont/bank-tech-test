class Account:
    def __init__(self):
        self.balance = 0
        
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
  