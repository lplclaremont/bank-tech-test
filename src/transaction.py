from datetime import date
class Transaction:
    def __init__(self, amount):
        self.__check_input(amount)
        self.amount = amount

    def get_amount(self):
        return self.amount

    def get_date(self):
        today = date.today()
        return today.strftime("%y/%m/%d")
    
    def __check_input(self, amount):
        if (type(amount) != int) or (amount == 0):
            raise Exception("Input must be a non zero integer")
        
    