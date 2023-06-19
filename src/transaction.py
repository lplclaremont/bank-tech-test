from datetime import date
class Transaction:
    def __init__(self, amount):
        self.check_input(amount)
        self.set_date()
        self.amount = amount

    def set_date(self):
        today = date.today()
        self.date = today.strftime("%y/%m/%d")
    
    def check_input(self, amount):
        if (type(amount) != int) or (amount == 0):
            raise Exception("Input must be a non zero integer")
        
    